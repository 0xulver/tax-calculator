#!/usr/bin/env python3
"""
fifo_calculator.py
FIFO cost basis calculator for Polish PIT-38 crypto tax reporting.

Reads the unified exchange ledger and computes:
- FIFO cost basis for every disposal (crypto → fiat)
- Capital gains/losses per asset per year
- PIT-38 summary totals

Polish tax rules:
- Taxable: crypto → fiat, crypto → goods/services
- Non-taxable: crypto-to-crypto swaps, wallet transfers, staking receipt
- Cost basis: FIFO (First-In, First-Out)
- Rate: 19% flat on net profit
- Loss carry-forward: up to 5 years

Usage:
  python3 fifo_calculator.py --input outputs/normalized_all_exchanges.csv --year 2025
  python3 fifo_calculator.py --input outputs/normalized_all_exchanges.csv --all-years
"""

from __future__ import annotations

import argparse
import csv
import json
import os
import sys
import time
import urllib.parse
import urllib.request
from collections import defaultdict, deque
from datetime import datetime, timezone
from decimal import Decimal, getcontext, ROUND_HALF_UP
from typing import Any, Dict, List, Optional, Tuple

getcontext().prec = 36

FIAT = {"EUR", "USD", "GBP", "PLN", "SEK", "JPY", "CAD", "AUD"}
STABLECOINS = {"USDC", "USDT", "UST", "DAI", "BUSD", "TUSD", "PYUSD"}
IGNORED_TX_TYPES = {
    "internal_transfer", "earn_allocation", "earn_other",
    "fiat_deposit", "fiat_withdrawal", "adjustment", "recovery",
    "unknown",
}


def parse_decimal(v: str) -> Decimal:
    try:
        return Decimal(v.strip())
    except Exception:
        return Decimal("0")


def fmt(v: Decimal) -> str:
    return str(v.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP))


def fmt_full(v: Decimal) -> str:
    if not isinstance(v, Decimal):
        v = Decimal(str(v))
    return str(v.normalize())


# ============================================================================
# NBP (National Bank of Poland) Exchange Rate API
# ============================================================================

_nbp_cache: Dict[Tuple[str, str], Decimal] = {}


def get_nbp_rate(currency: str, date_str: str) -> Optional[Decimal]:
    """
    Get PLN exchange rate from NBP API for a given currency and date.
    Polish tax law requires using NBP mid-rate from the last business day
    before the transaction date.

    Returns PLN value of 1 unit of the given currency.
    """
    if currency.upper() == "PLN":
        return Decimal("1")

    cache_key = (currency.upper(), date_str)
    if cache_key in _nbp_cache:
        return _nbp_cache[cache_key]

    # Try the exact date, then go back up to 7 days
    base_date = datetime.strptime(date_str, "%Y-%m-%d")
    for delta in range(0, 8):
        d = base_date
        from datetime import timedelta
        d = base_date - timedelta(days=delta)
        ds = d.strftime("%Y-%m-%d")

        url = f"https://api.nbp.pl/api/exchangerates/rates/a/{currency.upper()}/{ds}/?format=json"
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "tax-calc/1.0"})
            with urllib.request.urlopen(req, timeout=10) as resp:
                data = json.loads(resp.read().decode("utf-8"))
                rate = Decimal(str(data["rates"][0]["mid"]))
                _nbp_cache[cache_key] = rate
                return rate
        except Exception:
            continue

    return None


# ============================================================================
# CoinGecko Price Lookups
# ============================================================================

COINGECKO_ID_MAP = {
    "BTC": "bitcoin", "ETH": "ethereum", "SOL": "solana",
    "DOT": "polkadot", "KSM": "kusama", "ATOM": "cosmos",
    "LINK": "chainlink", "AAVE": "aave", "SNX": "havven",
    "MATIC": "matic-network", "FTM": "fantom",
    "SUI": "sui", "XMR": "monero",
    "LUNA": "terra-luna", "UST": "terrausd",
    "LUNA2": "terra-luna-2",
    "ACA": "acala", "KAR": "karura",
    "USDC": "usd-coin", "USDT": "tether",
    "XRP": "ripple", "ADA": "cardano",
    "AVAX": "avalanche-2", "NEAR": "near",
    "ALGO": "algorand", "XTZ": "tezos",
    "FLOW": "flow", "MINA": "mina-protocol",
    "KAVA": "kava", "TRX": "tron",
}

_cg_cache: Dict[Tuple[str, str], Optional[Decimal]] = {}


def get_crypto_price_pln(asset: str, date_str: str) -> Optional[Decimal]:
    """Get the PLN price of a crypto asset on a given date via CoinGecko."""
    cache_key = (asset.upper(), date_str)
    if cache_key in _cg_cache:
        return _cg_cache[cache_key]

    cg_id = COINGECKO_ID_MAP.get(asset.upper())
    if not cg_id:
        _cg_cache[cache_key] = None
        return None

    # CoinGecko expects dd-mm-yyyy
    parts = date_str.split("-")
    cg_date = f"{parts[2]}-{parts[1]}-{parts[0]}"

    url = f"https://api.coingecko.com/api/v3/coins/{cg_id}/history?date={cg_date}&localization=false"
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "tax-calc/1.0"})
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            market_data = data.get("market_data", {})
            price_pln = market_data.get("current_price", {}).get("pln")
            if price_pln is not None:
                result = Decimal(str(price_pln))
                _cg_cache[cache_key] = result
                return result
    except Exception:
        pass

    _cg_cache[cache_key] = None
    return None


# ============================================================================
# Price Resolution
# ============================================================================

def resolve_pln_value(
    asset: str,
    amount: Decimal,
    counterparty_asset: str,
    counterparty_amount: Decimal,
    date_str: str,
    use_api: bool = False,
) -> Tuple[Decimal, str]:
    """
    Resolve the PLN value of a transaction.

    Priority:
    1. If counterparty is fiat → convert using NBP rate (or direct if PLN)
    2. If counterparty is stablecoin → treat as ~1 USD → convert via NBP USD rate
    3. If use_api and asset is known → use CoinGecko historical price
    4. Return 0 with "unresolved" note

    Returns (pln_value, resolution_method)
    """
    if counterparty_asset and counterparty_amount and counterparty_amount != Decimal("0"):
        if counterparty_asset.upper() == "PLN":
            return counterparty_amount.copy_abs(), "direct_pln"

        if counterparty_asset.upper() in FIAT:
            if use_api:
                rate = get_nbp_rate(counterparty_asset, date_str)
                if rate:
                    return (counterparty_amount.copy_abs() * rate), f"nbp_{counterparty_asset}"
            # Offline estimate: use approximate static rates as fallback
            approx_rates = {
                "EUR": Decimal("4.30"), "USD": Decimal("3.95"),
                "GBP": Decimal("5.10"), "SEK": Decimal("0.38"),
            }
            rate = approx_rates.get(counterparty_asset.upper(), Decimal("4.0"))
            return (counterparty_amount.copy_abs() * rate), f"approx_{counterparty_asset}"

        if counterparty_asset.upper() in STABLECOINS:
            # Treat stablecoins as ~1 USD
            if use_api:
                usd_rate = get_nbp_rate("USD", date_str)
                if usd_rate:
                    return (counterparty_amount.copy_abs() * usd_rate), f"nbp_usd_via_{counterparty_asset}"
            return (counterparty_amount.copy_abs() * Decimal("3.95")), f"approx_usd_via_{counterparty_asset}"

    # Try CoinGecko for the asset itself
    if use_api and asset.upper() not in FIAT and asset.upper() not in STABLECOINS:
        price = get_crypto_price_pln(asset, date_str)
        if price:
            return (amount.copy_abs() * price), "coingecko_pln"

    return Decimal("0"), "unresolved"


# ============================================================================
# FIFO Lot Tracking
# ============================================================================

class FIFOLot:
    __slots__ = ("date", "amount", "cost_pln", "source", "source_tx_id")

    def __init__(self, date: str, amount: Decimal, cost_pln: Decimal,
                 source: str = "", source_tx_id: str = ""):
        self.date = date
        self.amount = amount
        self.cost_pln = cost_pln  # Total cost for this lot in PLN
        self.source = source
        self.source_tx_id = source_tx_id

    @property
    def cost_per_unit(self) -> Decimal:
        if self.amount == 0:
            return Decimal("0")
        return self.cost_pln / self.amount

    def __repr__(self) -> str:
        return f"Lot({self.date}, {self.amount}, {fmt(self.cost_pln)} PLN)"


class FIFOTracker:
    """Per-asset FIFO lot queue."""

    def __init__(self):
        self.lots: deque[FIFOLot] = deque()

    def add_lot(self, lot: FIFOLot) -> None:
        if lot.amount > 0:
            self.lots.append(lot)

    def consume(self, amount: Decimal) -> Tuple[Decimal, List[dict]]:
        """
        Consume `amount` units using FIFO ordering.
        Returns (total_cost_pln, consumed_lot_details).
        """
        total_cost = Decimal("0")
        remaining = amount
        consumed = []

        while remaining > 0 and self.lots:
            lot = self.lots[0]
            if lot.amount <= remaining:
                # Consume entire lot
                total_cost += lot.cost_pln
                consumed.append({
                    "lot_date": lot.date,
                    "lot_amount": fmt_full(lot.amount),
                    "lot_cost_pln": fmt(lot.cost_pln),
                    "consumed": fmt_full(lot.amount),
                })
                remaining -= lot.amount
                self.lots.popleft()
            else:
                # Partial consumption
                fraction = remaining / lot.amount
                partial_cost = lot.cost_pln * fraction
                total_cost += partial_cost
                consumed.append({
                    "lot_date": lot.date,
                    "lot_amount": fmt_full(lot.amount),
                    "lot_cost_pln": fmt(lot.cost_pln),
                    "consumed": fmt_full(remaining),
                })
                lot.amount -= remaining
                lot.cost_pln -= partial_cost
                remaining = Decimal("0")

        if remaining > 0:
            consumed.append({
                "lot_date": "MISSING",
                "lot_amount": "0",
                "lot_cost_pln": "0",
                "consumed": fmt_full(remaining),
            })

        return total_cost, consumed

    @property
    def total_remaining(self) -> Decimal:
        return sum(lot.amount for lot in self.lots)

    @property
    def total_cost_remaining(self) -> Decimal:
        return sum(lot.cost_pln for lot in self.lots)


# ============================================================================
# Tax Engine
# ============================================================================

def process_ledger(
    rows: List[Dict[str, str]],
    report_year: Optional[int] = None,
    use_api: bool = False,
) -> Dict[str, Any]:
    """
    Process the unified ledger and compute FIFO cost basis.

    Returns a dict with:
    - tax_events: list of taxable events with cost basis
    - lot_inventory: remaining lots per asset
    - yearly_summary: per-year totals
    - warnings: list of issues
    """
    trackers: Dict[str, FIFOTracker] = defaultdict(FIFOTracker)
    tax_events: List[Dict[str, str]] = []
    warnings: List[str] = []
    yearly: Dict[int, Dict[str, Decimal]] = defaultdict(
        lambda: {"revenue_pln": Decimal("0"), "cost_pln": Decimal("0"),
                 "gain_pln": Decimal("0"), "loss_pln": Decimal("0")}
    )

    for row in rows:
        tx_type = row["tx_type"]
        asset = row["asset"]
        amount = parse_decimal(row["amount"])
        fee = parse_decimal(row.get("fee", "0"))
        fee_asset = row.get("fee_asset", "")
        cp_asset = row.get("counterparty_asset", "")
        cp_amount = parse_decimal(row.get("counterparty_amount", "0"))
        date_iso = row["date"]
        date_str = date_iso[:10]  # YYYY-MM-DD
        year = int(date_str[:4])
        source = row.get("source", "")

        if tx_type in IGNORED_TX_TYPES:
            continue

        # ----- ACQUISITIONS (add FIFO lots) -----
        if tx_type == "buy":
            # Bought crypto with fiat → add lot
            pln_cost, method = resolve_pln_value(
                asset, amount, cp_asset, cp_amount, date_str, use_api
            )
            # Include fee in cost basis
            if fee and fee_asset:
                if fee_asset.upper() in FIAT:
                    fee_rate = get_nbp_rate(fee_asset, date_str) if use_api else Decimal("4.0")
                    pln_cost += fee * (fee_rate or Decimal("4.0"))
                elif fee_asset == asset:
                    # Fee in same asset means you got less, but cost is the same
                    pass

            trackers[asset].add_lot(FIFOLot(
                date=date_str, amount=amount, cost_pln=pln_cost,
                source=source,
            ))

        elif tx_type == "swap_in":
            # Received crypto from crypto-to-crypto swap
            # Under Polish law, no taxable event. Cost basis = fair market value at time.
            pln_cost, method = resolve_pln_value(
                asset, amount, cp_asset, cp_amount, date_str, use_api
            )
            if pln_cost == 0 and cp_asset and cp_amount > 0:
                # Try to derive from the counterparty's cost basis
                pln_cost, method = resolve_pln_value(
                    cp_asset, cp_amount, "", Decimal("0"), date_str, use_api
                )
            trackers[asset].add_lot(FIFOLot(
                date=date_str, amount=amount, cost_pln=pln_cost,
                source=f"{source}_swap_from_{cp_asset}",
            ))

        elif tx_type in ("deposit",):
            # Deposit from self-custody or external.
            # Not a taxable event itself. However, if this is a crypto deposit
            # from a wallet (not preceded by a buy on this exchange), we need
            # a lot so FIFO can track it. Use 0 cost here; the actual cost
            # was at original purchase time. This is conservative — it means
            # if later sold, the full amount is treated as gain.
            if asset.upper() not in FIAT:
                pln_cost = Decimal("0")
                if use_api:
                    price = get_crypto_price_pln(asset, date_str)
                    if price:
                        pln_cost = amount * price
                trackers[asset].add_lot(FIFOLot(
                    date=date_str, amount=amount, cost_pln=pln_cost,
                    source=f"{source}_deposit",
                ))

        elif tx_type in ("staking_reward", "earn_reward", "interest", "airdrop"):
            # Received as income. Under Polish law, not taxed at receipt
            # but becomes taxable at disposal. Cost basis = 0 or market value.
            # Using 0 cost basis (conservative approach).
            pln_cost = Decimal("0")
            if use_api:
                price = get_crypto_price_pln(asset, date_str)
                if price:
                    pln_cost = amount * price
            trackers[asset].add_lot(FIFOLot(
                date=date_str, amount=amount, cost_pln=pln_cost,
                source=f"{source}_{tx_type}",
            ))

        elif tx_type == "token_swap":
            # Redenomination/rebranding
            if amount > 0:
                trackers[asset].add_lot(FIFOLot(
                    date=date_str, amount=amount.copy_abs(), cost_pln=Decimal("0"),
                    source=f"{source}_token_swap",
                ))

        elif tx_type == "conversion":
            # Stablecoin auto-conversion (e.g., BUSD → USDC)
            if amount > 0:
                trackers[asset].add_lot(FIFOLot(
                    date=date_str, amount=amount, cost_pln=Decimal("0"),
                    source=f"{source}_conversion",
                ))

        # ----- DISPOSALS (consume FIFO lots) -----
        elif tx_type == "sell":
            # Sold crypto for fiat → TAXABLE EVENT
            # Skip if the "asset" sold is actually fiat (e.g., EUR withdrawal)
            if asset.upper() in FIAT:
                continue
            revenue_pln, method = resolve_pln_value(
                asset, amount, cp_asset, cp_amount, date_str, use_api
            )
            cost_basis, consumed_lots = trackers[asset].consume(amount)
            gain = revenue_pln - cost_basis

            tax_events.append({
                "date": date_str,
                "asset": asset,
                "amount": fmt_full(amount),
                "revenue_pln": fmt(revenue_pln),
                "cost_basis_pln": fmt(cost_basis),
                "gain_loss_pln": fmt(gain),
                "price_method": method,
                "source": source,
                "counterparty_asset": cp_asset,
                "counterparty_amount": fmt_full(cp_amount),
                "lots_consumed": str(len(consumed_lots)),
                "year": str(year),
            })

            if gain >= 0:
                yearly[year]["revenue_pln"] += revenue_pln
                yearly[year]["cost_pln"] += cost_basis
                yearly[year]["gain_pln"] += gain
            else:
                yearly[year]["revenue_pln"] += revenue_pln
                yearly[year]["cost_pln"] += cost_basis
                yearly[year]["loss_pln"] += gain.copy_abs()

            if any(c["lot_date"] == "MISSING" for c in consumed_lots):
                warnings.append(
                    f"[{date_str}] Sold {fmt_full(amount)} {asset} but insufficient FIFO lots. "
                    f"Some cost basis is 0."
                )

        elif tx_type == "swap_out":
            # Crypto-to-crypto swap — NOT taxable under Polish law
            # But we still consume the FIFO lots to track cost basis transfer
            trackers[asset].consume(amount)

        elif tx_type == "withdrawal":
            # Moving crypto off exchange — NOT taxable
            # Don't consume lots; the crypto is still yours
            pass

        elif tx_type == "fee":
            # Standalone fee — consume from FIFO
            if asset.upper() not in FIAT:
                trackers[asset].consume(fee if fee else amount)

    # Build lot inventory summary
    lot_inventory = {}
    for asset_name, tracker in sorted(trackers.items()):
        if tracker.total_remaining > 0:
            lot_inventory[asset_name] = {
                "total_amount": fmt_full(tracker.total_remaining),
                "total_cost_pln": fmt(tracker.total_cost_remaining),
                "lot_count": len(tracker.lots),
            }

    # Build yearly summaries
    yearly_summary = {}
    for y in sorted(yearly.keys()):
        d = yearly[y]
        net = d["gain_pln"] - d["loss_pln"]
        yearly_summary[y] = {
            "revenue_pln": fmt(d["revenue_pln"]),
            "cost_pln": fmt(d["cost_pln"]),
            "gain_pln": fmt(d["gain_pln"]),
            "loss_pln": fmt(d["loss_pln"]),
            "net_income_pln": fmt(net),
            "tax_due_19pct": fmt(max(net * Decimal("0.19"), Decimal("0"))),
        }

    return {
        "tax_events": tax_events,
        "lot_inventory": lot_inventory,
        "yearly_summary": yearly_summary,
        "warnings": warnings,
    }


# ============================================================================
# CLI
# ============================================================================

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="FIFO cost basis calculator for PIT-38.")
    parser.add_argument("--input", required=True, help="Path to normalized exchange CSV.")
    parser.add_argument("--output-dir", default="outputs", help="Output directory.")
    parser.add_argument("--year", type=int, default=None, help="Report year (filter tax events).")
    parser.add_argument("--all-years", action="store_true", help="Report all years.")
    parser.add_argument("--use-api", action="store_true",
                        help="Use NBP and CoinGecko APIs for live price resolution.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()

    # Read normalized ledger
    with open(args.input, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    print(f"Loaded {len(rows)} records from {args.input}")

    result = process_ledger(rows, report_year=args.year, use_api=args.use_api)

    tax_events = result["tax_events"]
    yearly_summary = result["yearly_summary"]
    lot_inventory = result["lot_inventory"]
    warnings = result["warnings"]

    # Filter by year if requested
    if args.year and not args.all_years:
        tax_events = [e for e in tax_events if e["year"] == str(args.year)]

    os.makedirs(args.output_dir, exist_ok=True)

    # Write tax events CSV
    suffix = f"_{args.year}" if args.year else "_all"
    tax_cols = [
        "date", "asset", "amount", "revenue_pln", "cost_basis_pln",
        "gain_loss_pln", "price_method", "source", "counterparty_asset",
        "counterparty_amount", "lots_consumed", "year",
    ]
    tax_path = os.path.join(args.output_dir, f"tax_events{suffix}.csv")
    with open(tax_path, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=tax_cols)
        writer.writeheader()
        for e in tax_events:
            writer.writerow(e)

    # Write PIT-38 summary JSON
    summary_path = os.path.join(args.output_dir, f"pit38_summary{suffix}.json")
    with open(summary_path, "w", encoding="utf-8") as f:
        json.dump({
            "yearly_summary": yearly_summary,
            "lot_inventory": lot_inventory,
            "total_tax_events": len(tax_events),
            "warnings": warnings,
        }, f, indent=2, default=str)

    # Print report
    print("\n" + "=" * 70)
    print("PIT-38 CRYPTO TAX SUMMARY")
    print("=" * 70)
    for y, s in sorted(yearly_summary.items()):
        print(f"\n  {y}:")
        print(f"    Revenue (przychód):        {s['revenue_pln']:>15} PLN")
        print(f"    Costs (koszty):            {s['cost_pln']:>15} PLN")
        print(f"    Gains:                     {s['gain_pln']:>15} PLN")
        print(f"    Losses:                    {s['loss_pln']:>15} PLN")
        print(f"    Net income (dochód):       {s['net_income_pln']:>15} PLN")
        print(f"    Tax due (19%):             {s['tax_due_19pct']:>15} PLN")

    if lot_inventory:
        print(f"\n  Remaining FIFO lots ({len(lot_inventory)} assets):")
        for asset, info in sorted(lot_inventory.items()):
            print(f"    {asset}: {info['total_amount']} units, "
                  f"cost basis {info['total_cost_pln']} PLN, "
                  f"{info['lot_count']} lots")

    if warnings:
        print(f"\n  ⚠ {len(warnings)} warnings:")
        for w in warnings[:20]:
            print(f"    - {w}")
        if len(warnings) > 20:
            print(f"    ... and {len(warnings) - 20} more")

    print(f"\nOutput: {tax_path}")
    print(f"        {summary_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
