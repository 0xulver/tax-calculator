"""FIFO cost basis engine with salary lot injection and stablecoin deposit valuation."""
from __future__ import annotations

import csv
from collections import defaultdict, deque
from decimal import Decimal
from typing import Any, Optional

from tax_calc.constants import FIAT, IGNORED_TX_TYPES, STABLECOINS, is_fiat, is_stablecoin
from tax_calc.models import FIFOLot, TaxEvent, fmt, fmt_full
from tax_calc.prices import PriceResolver


class FIFOTracker:
    """Per-asset FIFO lot queue."""

    def __init__(self) -> None:
        self.lots: deque[FIFOLot] = deque()

    def add_lot(self, lot: FIFOLot) -> None:
        if lot.amount > 0:
            self.lots.append(lot)

    def consume(self, amount: Decimal) -> tuple[Decimal, list[dict]]:
        total_cost = Decimal("0")
        remaining = amount
        consumed: list[dict] = []

        while remaining > 0 and self.lots:
            lot = self.lots[0]
            if lot.amount <= remaining:
                total_cost += lot.cost_pln
                consumed.append({
                    "lot_date": lot.date,
                    "lot_amount": fmt_full(lot.amount),
                    "lot_cost_pln": fmt(lot.cost_pln),
                    "lot_source": lot.source,
                    "consumed": fmt_full(lot.amount),
                })
                remaining -= lot.amount
                self.lots.popleft()
            else:
                fraction = remaining / lot.amount
                partial_cost = lot.cost_pln * fraction
                total_cost += partial_cost
                consumed.append({
                    "lot_date": lot.date,
                    "lot_amount": fmt_full(lot.amount),
                    "lot_cost_pln": fmt(lot.cost_pln),
                    "lot_source": lot.source,
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
                "lot_source": "",
                "consumed": fmt_full(remaining),
            })

        return total_cost, consumed

    @property
    def total_remaining(self) -> Decimal:
        return sum(lot.amount for lot in self.lots)

    @property
    def total_cost_remaining(self) -> Decimal:
        return sum(lot.cost_pln for lot in self.lots)


def process_ledger(
    rows: list[dict[str, str]],
    prices: PriceResolver,
    salary_lots: list[FIFOLot] | None = None,
) -> dict[str, Any]:
    """Process unified ledger with FIFO cost basis tracking.

    Args:
        rows: Normalized transaction dicts (from CSV or Transaction.to_dict())
        prices: PriceResolver instance for PLN conversions
        salary_lots: Pre-loaded salary FIFOLots to inject into stablecoin trackers
    """
    trackers: dict[str, FIFOTracker] = defaultdict(FIFOTracker)
    tax_events: list[TaxEvent] = []
    warnings: list[str] = []
    yearly: dict[int, dict[str, Decimal]] = defaultdict(
        lambda: {"revenue_pln": Decimal("0"), "cost_pln": Decimal("0"),
                 "gain_pln": Decimal("0"), "loss_pln": Decimal("0")}
    )

    # Inject salary lots BEFORE processing exchange ledger
    if salary_lots:
        for lot in sorted(salary_lots, key=lambda l: l.date):
            asset = "USDC"  # salary payments are in USDC
            trackers[asset].add_lot(lot)

    for row in rows:
        tx_type = row["tx_type"]
        asset = row["asset"]
        amount = _dec(row["amount"])
        fee = _dec(row.get("fee", "0"))
        fee_asset = row.get("fee_asset", "")
        cp_asset = row.get("counterparty_asset", "")
        cp_amount = _dec(row.get("counterparty_amount", "0"))
        date_iso = row["date"]
        date_str = date_iso[:10]
        year = int(date_str[:4])
        source = row.get("source", "")

        if tx_type in IGNORED_TX_TYPES:
            continue

        # ----- ACQUISITIONS -----
        if tx_type == "buy":
            pln_cost, method = prices.resolve(asset, amount, cp_asset, cp_amount, date_str)
            if fee and fee_asset and fee_asset.upper() in FIAT:
                fee_rate = prices.nbp.get_rate(fee_asset, date_str)
                if fee_rate:
                    pln_cost += fee * fee_rate
            trackers[asset].add_lot(FIFOLot(
                date=date_str, amount=amount, cost_pln=pln_cost, source=source))

        elif tx_type == "swap_in":
            pln_cost, method = prices.resolve(asset, amount, cp_asset, cp_amount, date_str)
            if pln_cost == 0 and cp_asset and cp_amount > 0:
                pln_cost, method = prices.resolve(cp_asset, cp_amount, "", Decimal("0"), date_str)
            trackers[asset].add_lot(FIFOLot(
                date=date_str, amount=amount, cost_pln=pln_cost,
                source=f"{source}_swap_from_{cp_asset}"))

        elif tx_type == "deposit":
            if asset.upper() not in FIAT:
                # Fix: stablecoin deposits get valued at NBP USD rate, not 0
                if is_stablecoin(asset):
                    pln_cost, method = prices.stablecoin_pln_value(amount, date_str)
                else:
                    pln_cost = Decimal("0")
                    price = prices._get_coingecko_price(asset, date_str)
                    if price:
                        pln_cost = amount * price
                trackers[asset].add_lot(FIFOLot(
                    date=date_str, amount=amount, cost_pln=pln_cost,
                    source=f"{source}_deposit"))

        elif tx_type in ("staking_reward", "earn_reward", "interest", "airdrop"):
            pln_cost = Decimal("0")
            if asset.upper() not in FIAT and asset.upper() not in STABLECOINS:
                price = prices._get_coingecko_price(asset, date_str)
                if price:
                    pln_cost = amount * price
            elif is_stablecoin(asset):
                pln_cost, _ = prices.stablecoin_pln_value(amount, date_str)
            trackers[asset].add_lot(FIFOLot(
                date=date_str, amount=amount, cost_pln=pln_cost,
                source=f"{source}_{tx_type}"))

        elif tx_type == "token_swap":
            if amount > 0:
                trackers[asset].add_lot(FIFOLot(
                    date=date_str, amount=amount.copy_abs(), cost_pln=Decimal("0"),
                    source=f"{source}_token_swap"))

        elif tx_type == "conversion":
            # Stablecoin auto-conversion: transfer cost basis from source to dest
            if amount > 0:
                # This is the destination — try to get cost from prior consumption
                # For stablecoin-to-stablecoin, use USD rate as fallback
                pln_cost, _ = prices.stablecoin_pln_value(amount, date_str)
                trackers[asset].add_lot(FIFOLot(
                    date=date_str, amount=amount, cost_pln=pln_cost,
                    source=f"{source}_conversion"))
            elif amount < 0:
                # This is the source being consumed
                trackers[asset].consume(amount.copy_abs())

        # ----- DISPOSALS -----
        elif tx_type == "sell":
            if asset.upper() in FIAT:
                continue

            revenue_pln, method = prices.resolve(
                asset, amount, cp_asset, cp_amount, date_str)
            cost_basis, consumed_lots = trackers[asset].consume(amount)
            gain = revenue_pln - cost_basis

            event = TaxEvent(
                date=date_str, asset=asset, amount=amount,
                revenue_pln=revenue_pln, cost_basis_pln=cost_basis,
                gain_loss_pln=gain, price_method=method,
                source=source,
                counterparty_asset=cp_asset, counterparty_amount=cp_amount,
                lots_consumed=len(consumed_lots), year=year,
                lot_details=consumed_lots,
            )
            tax_events.append(event)

            yearly[year]["revenue_pln"] += revenue_pln
            yearly[year]["cost_pln"] += cost_basis
            if gain >= 0:
                yearly[year]["gain_pln"] += gain
            else:
                yearly[year]["loss_pln"] += gain.copy_abs()

            if any(c["lot_date"] == "MISSING" for c in consumed_lots):
                warnings.append(
                    f"[{date_str}] Sold {fmt_full(amount)} {asset} but insufficient FIFO lots.")

        elif tx_type == "swap_out":
            trackers[asset].consume(amount)

        elif tx_type == "withdrawal":
            pass  # Moving off exchange, not taxable

        elif tx_type == "fee":
            if asset.upper() not in FIAT:
                trackers[asset].consume(fee if fee else amount)

    # Build inventory
    lot_inventory: dict[str, dict] = {}
    for asset_name, tracker in sorted(trackers.items()):
        if tracker.total_remaining > 0:
            lot_inventory[asset_name] = {
                "total_amount": fmt_full(tracker.total_remaining),
                "total_cost_pln": fmt(tracker.total_cost_remaining),
                "lot_count": len(tracker.lots),
            }

    # Build yearly summaries
    yearly_summary: dict[int, dict[str, str]] = {}
    for y in sorted(yearly.keys()):
        d = yearly[y]
        net = d["revenue_pln"] - d["cost_pln"]
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


def _dec(v: str) -> Decimal:
    try:
        return Decimal(v.strip())
    except Exception:
        return Decimal("0")
