#!/usr/bin/env python3
"""
exchange_normalizer.py
Normalize Binance and Kraken CSV exports into a unified transaction ledger.

Usage:
  python3 exchange_normalizer.py --output-dir outputs

Reads CSVs from:
  - ../crypto-cex-transactions/binance/
  - ../crypto-cex-transactions/kraken/
"""

from __future__ import annotations

import argparse
import csv
import os
import re
import sys
from collections import defaultdict
from datetime import datetime, timezone
from decimal import Decimal, getcontext
from typing import Any, Dict, List, Optional, Tuple

getcontext().prec = 36

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
BINANCE_DIR = os.path.join(SCRIPT_DIR, "..", "crypto-cex-transactions", "binance")
KRAKEN_DIR = os.path.join(SCRIPT_DIR, "..", "crypto-cex-transactions", "kraken")

UNIFIED_COLUMNS = [
    "date",
    "source",
    "source_tx_id",
    "tx_type",
    "asset",
    "amount",
    "fee",
    "fee_asset",
    "counterparty_asset",
    "counterparty_amount",
    "notes",
]

# Kraken asset name normalization (Kraken uses X-prefixed tickers for some)
KRAKEN_ASSET_MAP = {
    "XXBT": "BTC", "XBT": "BTC", "XBTC": "BTC",
    "XETH": "ETH", "XXRP": "XRP", "XLTC": "LTC",
    "XXLM": "XLM", "XDOGE": "DOGE", "XZEC": "ZEC",
    "XXMR": "XMR", "XREP": "REP", "XETC": "ETC",
    "XICN": "ICN", "XMLN": "MLN",
    "ZUSD": "USD", "ZEUR": "EUR", "ZGBP": "GBP",
    "ZJPY": "JPY", "ZCAD": "CAD", "ZAUD": "AUD",
    "DOT.S": "DOT", "DOT28.S": "DOT",
    "KSM.S": "KSM",
    "ATOM.S": "ATOM", "ATOM21.S": "ATOM",
    "ETH2.S": "ETH", "ETH.S": "ETH",
    "SOL.S": "SOL",
    "XTZ.S": "XTZ",
    "FLOW.S": "FLOW", "FLOWH.S": "FLOW",
    "KAVA.S": "KAVA",
    "MINA.S": "MINA",
    "TRX.S": "TRX",
    "ADA.S": "ADA",
    "LUNA2": "LUNA2",
}

FIAT_CURRENCIES = {"EUR", "USD", "GBP", "JPY", "CAD", "AUD", "PLN", "SEK"}


def normalize_kraken_asset(raw: str) -> str:
    """Convert Kraken's internal asset names to standard tickers."""
    raw = raw.strip()
    if raw in KRAKEN_ASSET_MAP:
        return KRAKEN_ASSET_MAP[raw]
    return raw


def is_fiat(asset: str) -> bool:
    return asset.upper() in FIAT_CURRENCIES


def is_stablecoin(asset: str) -> bool:
    return asset.upper() in {"USDC", "USDT", "UST", "DAI", "BUSD", "TUSD", "PYUSD"}


def parse_decimal(value: str) -> Decimal:
    try:
        return Decimal(value.strip())
    except Exception:
        return Decimal("0")


def format_decimal(value) -> str:
    if not isinstance(value, Decimal):
        value = Decimal(str(value))
    return str(value.normalize())


def parse_binance_time(time_str: str) -> datetime:
    """Parse Binance time format: '21-08-11 14:38:41' → datetime."""
    time_str = time_str.strip()
    # Binance uses YY-MM-DD HH:MM:SS
    if len(time_str.split("-")[0]) == 2:
        return datetime.strptime(time_str, "%y-%m-%d %H:%M:%S").replace(tzinfo=timezone.utc)
    return datetime.strptime(time_str, "%Y-%m-%d %H:%M:%S").replace(tzinfo=timezone.utc)


def parse_kraken_time(time_str: str) -> datetime:
    """Parse Kraken time format: '2022-01-04 11:17:42' → datetime."""
    return datetime.strptime(time_str.strip(), "%Y-%m-%d %H:%M:%S").replace(tzinfo=timezone.utc)


def make_row(
    date: datetime,
    source: str,
    source_tx_id: str,
    tx_type: str,
    asset: str,
    amount: Decimal,
    fee: Decimal = Decimal("0"),
    fee_asset: str = "",
    counterparty_asset: str = "",
    counterparty_amount: Decimal = Decimal("0"),
    notes: str = "",
) -> Dict[str, str]:
    return {
        "date": date.isoformat(),
        "source": source,
        "source_tx_id": source_tx_id,
        "tx_type": tx_type,
        "asset": asset,
        "amount": format_decimal(amount),
        "fee": format_decimal(fee),
        "fee_asset": fee_asset,
        "counterparty_asset": counterparty_asset,
        "counterparty_amount": format_decimal(counterparty_amount),
        "notes": notes,
    }


# ============================================================================
# BINANCE NORMALIZATION
# ============================================================================

def normalize_binance(binance_dir: str) -> List[Dict[str, str]]:
    """
    Normalize Binance transaction history.

    Binance exports have paired rows for trades:
      - Transaction Buy: amount > 0 (you received asset)
      - Transaction Sold: amount < 0 (you sold asset)
      - Transaction Fee: fee deducted
      - Transaction Spend: you spent fiat/stablecoin to buy
      - Transaction Revenue: you received fiat/stablecoin from selling

    These are grouped by timestamp to reconstruct full trades.
    """
    csv_path = os.path.join(binance_dir, "binance_all_transactions_2020_2025.csv")
    if not os.path.exists(csv_path):
        print(f"Warning: {csv_path} not found", file=sys.stderr)
        return []

    rows: List[Dict[str, Any]] = []
    with open(csv_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            rows.append(row)

    # Group by timestamp to reconstruct trades
    time_groups: Dict[str, List[Dict[str, Any]]] = defaultdict(list)
    standalone: List[Dict[str, str]] = []

    for row in rows:
        op = row.get("operation", "").strip()
        coin = row.get("coin", "").strip()
        change = parse_decimal(row.get("change", "0"))
        time_str = row.get("time", "").strip()
        remark = row.get("remark", "").strip()

        if not time_str or not coin:
            continue

        dt = parse_binance_time(time_str)

        # Simple events that don't need grouping
        if op == "Deposit":
            standalone.append(make_row(
                date=dt, source="binance", source_tx_id="",
                tx_type="deposit", asset=coin, amount=change.copy_abs(),
                notes=f"Binance {op}",
            ))
        elif op == "Withdraw":
            standalone.append(make_row(
                date=dt, source="binance", source_tx_id="",
                tx_type="withdrawal", asset=coin, amount=change.copy_abs(),
                notes=f"Binance {op}" + (f" ({remark})" if remark and remark != "Withdraw fee is included" else ""),
            ))
        elif op == "Fiat Withdraw":
            standalone.append(make_row(
                date=dt, source="binance", source_tx_id="",
                tx_type="fiat_withdrawal", asset=coin, amount=change.copy_abs(),
                notes=f"Binance {op}",
            ))
        elif op == "Airdrop Assets":
            standalone.append(make_row(
                date=dt, source="binance", source_tx_id="",
                tx_type="airdrop", asset=coin, amount=change.copy_abs(),
                notes=f"Binance {op}",
            ))
        elif op in ("Simple Earn Flexible Interest",):
            standalone.append(make_row(
                date=dt, source="binance", source_tx_id="",
                tx_type="interest", asset=coin, amount=change.copy_abs(),
                notes=f"Binance {op}",
            ))
        elif op == "Stablecoins Auto-Conversion":
            standalone.append(make_row(
                date=dt, source="binance", source_tx_id="",
                tx_type="conversion", asset=coin, amount=change,
                notes=f"Binance {op}",
            ))
        elif op == "Token Swap - Redenomination/Rebranding":
            standalone.append(make_row(
                date=dt, source="binance", source_tx_id="",
                tx_type="token_swap", asset=coin, amount=change,
                notes=f"Binance {op}",
            ))
        elif op == "Token Swap - Distribution":
            standalone.append(make_row(
                date=dt, source="binance", source_tx_id="",
                tx_type="token_swap", asset=coin, amount=change,
                notes=f"Binance {op}",
            ))
        elif op == "Asset Recovery":
            standalone.append(make_row(
                date=dt, source="binance", source_tx_id="",
                tx_type="recovery", asset=coin, amount=change,
                notes=f"Binance {op}",
            ))
        elif op == "Fiat OCBS - Add Fiat and Fees":
            standalone.append(make_row(
                date=dt, source="binance", source_tx_id="",
                tx_type="fiat_deposit", asset=coin, amount=change,
                notes=f"Binance {op}",
            ))
        elif op in ("Transaction Buy", "Transaction Sold", "Transaction Fee",
                     "Transaction Spend", "Transaction Revenue",
                     "Binance Convert",
                     "Sell Crypto To Fiat", "Buy Crypto With Card",
                     "Buy Crypto With Fiat", "Transaction Related"):
            # Group these by timestamp for trade reconstruction
            time_groups[time_str].append({
                "op": op, "coin": coin, "change": change, "dt": dt, "remark": remark,
            })
        else:
            standalone.append(make_row(
                date=dt, source="binance", source_tx_id="",
                tx_type="unknown", asset=coin, amount=change,
                notes=f"Binance unknown op: {op}",
            ))

    # Reconstruct trades from time-grouped entries
    trades: List[Dict[str, str]] = []
    for time_str, entries in sorted(time_groups.items()):
        dt = entries[0]["dt"]
        buys = [e for e in entries if e["op"] in ("Transaction Buy", "Buy Crypto With Card", "Buy Crypto With Fiat")]
        sells = [e for e in entries if e["op"] in ("Transaction Sold", "Sell Crypto To Fiat")]
        fees = [e for e in entries if e["op"] == "Transaction Fee"]
        spends = [e for e in entries if e["op"] == "Transaction Spend"]
        revenues = [e for e in entries if e["op"] == "Transaction Revenue"]
        converts = [e for e in entries if e["op"] == "Binance Convert"]
        related = [e for e in entries if e["op"] == "Transaction Related"]

        # Calculate total fee
        total_fee = Decimal("0")
        fee_asset = ""
        for fe in fees:
            total_fee += fe["change"].copy_abs()
            fee_asset = fe["coin"]

        if converts:
            # Binance Convert: one positive (received) and one negative (spent)
            for conv in converts:
                if conv["change"] > 0:
                    trades.append(make_row(
                        date=dt, source="binance", source_tx_id="",
                        tx_type="swap_in", asset=conv["coin"], amount=conv["change"],
                        notes="Binance Convert",
                    ))
                else:
                    trades.append(make_row(
                        date=dt, source="binance", source_tx_id="",
                        tx_type="swap_out", asset=conv["coin"], amount=conv["change"].copy_abs(),
                        notes="Binance Convert",
                    ))
        elif buys and (spends or revenues or sells):
            # Buy trade: you spent fiat/stablecoin to buy crypto
            for buy in buys:
                # Find the matching spend
                spend_asset = ""
                spend_amount = Decimal("0")
                for sp in spends:
                    spend_asset = sp["coin"]
                    spend_amount += sp["change"].copy_abs()

                tx_type = "buy"
                if is_fiat(buy["coin"]):
                    tx_type = "sell"  # If you "bought" fiat, you sold crypto
                elif is_fiat(spend_asset):
                    tx_type = "buy"
                else:
                    tx_type = "swap_in"  # crypto-to-crypto

                trades.append(make_row(
                    date=dt, source="binance", source_tx_id="",
                    tx_type=tx_type, asset=buy["coin"], amount=buy["change"].copy_abs(),
                    fee=total_fee, fee_asset=fee_asset,
                    counterparty_asset=spend_asset, counterparty_amount=spend_amount,
                    notes="Binance Trade",
                ))
                total_fee = Decimal("0")  # Only apply fee once
        elif sells and (revenues or spends):
            for sell in sells:
                rev_asset = ""
                rev_amount = Decimal("0")
                for rv in revenues:
                    rev_asset = rv["coin"]
                    rev_amount += rv["change"].copy_abs()

                tx_type = "sell"
                if is_fiat(sell["coin"]):
                    tx_type = "buy"
                elif is_fiat(rev_asset):
                    tx_type = "sell"
                else:
                    tx_type = "swap_out"

                trades.append(make_row(
                    date=dt, source="binance", source_tx_id="",
                    tx_type=tx_type, asset=sell["coin"], amount=sell["change"].copy_abs(),
                    fee=total_fee, fee_asset=fee_asset,
                    counterparty_asset=rev_asset, counterparty_amount=rev_amount,
                    notes="Binance Trade",
                ))
                total_fee = Decimal("0")
        elif buys and not spends and not revenues and not sells:
            # Standalone buy (e.g., Buy Crypto With Card without a paired spend entry)
            for buy in buys:
                trades.append(make_row(
                    date=dt, source="binance", source_tx_id="",
                    tx_type="buy", asset=buy["coin"], amount=buy["change"].copy_abs(),
                    fee=total_fee, fee_asset=fee_asset,
                    notes=f"Binance {buy['op']}",
                ))
                total_fee = Decimal("0")
        elif related:
            for r in related:
                trades.append(make_row(
                    date=dt, source="binance", source_tx_id="",
                    tx_type="adjustment", asset=r["coin"], amount=r["change"],
                    notes="Binance Transaction Related",
                ))
        else:
            # Ungrouped fees or other
            for e in entries:
                if e["op"] == "Transaction Fee":
                    trades.append(make_row(
                        date=dt, source="binance", source_tx_id="",
                        tx_type="fee", asset=e["coin"], amount=e["change"].copy_abs(),
                        notes="Binance Fee (orphaned)",
                    ))
                else:
                    trades.append(make_row(
                        date=dt, source="binance", source_tx_id="",
                        tx_type="unknown", asset=e["coin"], amount=e["change"],
                        notes=f"Binance ungrouped: {e['op']}",
                    ))

    return standalone + trades


# ============================================================================
# KRAKEN NORMALIZATION
# ============================================================================

def normalize_kraken(kraken_dir: str) -> List[Dict[str, str]]:
    """
    Normalize Kraken ledger exports.

    Kraken uses paired ledger entries for trades: two rows with the same `refid`,
    one for each leg of the trade (e.g., -69 LUNA2 and +387 EUR).
    """
    all_entries: List[Dict[str, Any]] = []

    for fname in sorted(os.listdir(kraken_dir)):
        if not fname.endswith(".csv"):
            continue
        path = os.path.join(kraken_dir, fname)
        with open(path, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                all_entries.append(row)

    # Deduplicate by txid (multiple year files may overlap)
    seen_txids: set = set()
    unique_entries: List[Dict[str, Any]] = []
    for entry in all_entries:
        txid = entry.get("txid", "").strip()
        if txid and txid in seen_txids:
            continue
        if txid:
            seen_txids.add(txid)
        unique_entries.append(entry)

    # Group by refid for trade reconstruction
    refid_groups: Dict[str, List[Dict[str, Any]]] = defaultdict(list)
    standalone: List[Dict[str, str]] = []

    for entry in unique_entries:
        tx_type = entry.get("type", "").strip()
        subtype = entry.get("subtype", "").strip()
        subclass = entry.get("subclass", "").strip()
        asset_raw = entry.get("asset", "").strip()
        asset = normalize_kraken_asset(asset_raw)
        amount = parse_decimal(entry.get("amount", "0"))
        fee = parse_decimal(entry.get("fee", "0"))
        time_str = entry.get("time", "").strip()
        txid = entry.get("txid", "").strip()
        refid = entry.get("refid", "").strip()

        if not time_str:
            continue

        dt = parse_kraken_time(time_str)

        if tx_type == "trade":
            refid_groups[refid].append({
                "dt": dt, "asset": asset, "asset_raw": asset_raw,
                "amount": amount, "fee": fee, "txid": txid,
                "subclass": subclass, "subtype": subtype,
            })
        elif tx_type == "deposit":
            standalone.append(make_row(
                date=dt, source="kraken", source_tx_id=txid,
                tx_type="deposit",
                asset=asset, amount=amount.copy_abs(),
                fee=fee.copy_abs(), fee_asset=asset if fee else "",
                notes=f"Kraken deposit ({subclass})",
            ))
        elif tx_type == "withdrawal":
            standalone.append(make_row(
                date=dt, source="kraken", source_tx_id=txid,
                tx_type="withdrawal" if subclass == "crypto" else "fiat_withdrawal",
                asset=asset, amount=amount.copy_abs(),
                fee=fee.copy_abs(), fee_asset=asset if fee else "",
                notes=f"Kraken withdrawal ({subclass})",
            ))
        elif tx_type == "staking":
            standalone.append(make_row(
                date=dt, source="kraken", source_tx_id=txid,
                tx_type="staking_reward", asset=asset, amount=amount.copy_abs(),
                notes=f"Kraken staking ({subclass})" + (f" raw_asset={asset_raw}" if asset_raw != asset else ""),
            ))
        elif tx_type == "earn":
            if subtype == "reward":
                standalone.append(make_row(
                    date=dt, source="kraken", source_tx_id=txid,
                    tx_type="earn_reward", asset=asset, amount=amount.copy_abs(),
                    notes=f"Kraken earn reward ({subclass})",
                ))
            elif subtype in ("autoallocation", "deallocation", "migration"):
                standalone.append(make_row(
                    date=dt, source="kraken", source_tx_id=txid,
                    tx_type="earn_allocation", asset=asset, amount=amount,
                    notes=f"Kraken earn {subtype} ({subclass})",
                ))
            else:
                standalone.append(make_row(
                    date=dt, source="kraken", source_tx_id=txid,
                    tx_type="earn_other", asset=asset, amount=amount,
                    notes=f"Kraken earn {subtype} ({subclass})",
                ))
        elif tx_type == "transfer":
            standalone.append(make_row(
                date=dt, source="kraken", source_tx_id=txid,
                tx_type="internal_transfer", asset=asset, amount=amount,
                notes=f"Kraken transfer {subtype} ({subclass})",
            ))
        elif tx_type in ("receive", "spend"):
            # Part of instant buy/sell — group by refid like trades
            refid_groups[refid].append({
                "dt": dt, "asset": asset, "asset_raw": asset_raw,
                "amount": amount, "fee": fee, "txid": txid,
                "subclass": subclass, "subtype": subtype,
                "original_type": tx_type,
            })
        else:
            standalone.append(make_row(
                date=dt, source="kraken", source_tx_id=txid,
                tx_type="unknown", asset=asset, amount=amount,
                notes=f"Kraken unknown type: {tx_type}/{subtype}/{subclass}",
            ))

    # Reconstruct trades from refid-grouped entries
    trades: List[Dict[str, str]] = []
    for refid, legs in sorted(refid_groups.items(), key=lambda x: x[1][0]["dt"]):
        if len(legs) < 2:
            # Orphaned trade leg
            for leg in legs:
                trades.append(make_row(
                    date=leg["dt"], source="kraken", source_tx_id=leg["txid"],
                    tx_type="unknown_trade_leg", asset=leg["asset"], amount=leg["amount"],
                    notes=f"Kraken orphaned trade leg refid={refid}",
                ))
            continue

        dt = legs[0]["dt"]
        # Separate into "gave" (negative) and "got" (positive) legs
        gave_legs = [l for l in legs if l["amount"] < 0]
        got_legs = [l for l in legs if l["amount"] > 0]

        if not gave_legs or not got_legs:
            for leg in legs:
                trades.append(make_row(
                    date=leg["dt"], source="kraken", source_tx_id=leg["txid"],
                    tx_type="unknown_trade_leg", asset=leg["asset"], amount=leg["amount"],
                    notes=f"Kraken ambiguous trade refid={refid}",
                ))
            continue

        gave = gave_legs[0]
        got = got_legs[0]

        # Total fees from both legs
        total_fee = sum(l["fee"].copy_abs() for l in legs if l["fee"])
        fee_asset = gave["asset"] if gave["fee"] else (got["asset"] if got["fee"] else "")

        # Determine trade type
        gave_is_fiat = is_fiat(gave["asset"])
        got_is_fiat = is_fiat(got["asset"])

        if gave_is_fiat and not got_is_fiat:
            # Spent fiat → got crypto = BUY
            trades.append(make_row(
                date=dt, source="kraken", source_tx_id=got["txid"],
                tx_type="buy", asset=got["asset"], amount=got["amount"].copy_abs(),
                fee=total_fee, fee_asset=fee_asset,
                counterparty_asset=gave["asset"], counterparty_amount=gave["amount"].copy_abs(),
                notes="Kraken Trade",
            ))
        elif not gave_is_fiat and got_is_fiat:
            # Sold crypto → got fiat = SELL
            trades.append(make_row(
                date=dt, source="kraken", source_tx_id=gave["txid"],
                tx_type="sell", asset=gave["asset"], amount=gave["amount"].copy_abs(),
                fee=total_fee, fee_asset=fee_asset,
                counterparty_asset=got["asset"], counterparty_amount=got["amount"].copy_abs(),
                notes="Kraken Trade",
            ))
        elif not gave_is_fiat and not got_is_fiat:
            # Crypto-to-crypto swap
            trades.append(make_row(
                date=dt, source="kraken", source_tx_id=gave["txid"],
                tx_type="swap_out", asset=gave["asset"], amount=gave["amount"].copy_abs(),
                fee=total_fee, fee_asset=fee_asset,
                counterparty_asset=got["asset"], counterparty_amount=got["amount"].copy_abs(),
                notes="Kraken Crypto-to-Crypto Trade",
            ))
            trades.append(make_row(
                date=dt, source="kraken", source_tx_id=got["txid"],
                tx_type="swap_in", asset=got["asset"], amount=got["amount"].copy_abs(),
                counterparty_asset=gave["asset"], counterparty_amount=gave["amount"].copy_abs(),
                notes="Kraken Crypto-to-Crypto Trade",
            ))
        else:
            # Fiat-to-fiat (shouldn't happen normally)
            trades.append(make_row(
                date=dt, source="kraken", source_tx_id=gave["txid"],
                tx_type="fiat_exchange", asset=gave["asset"], amount=gave["amount"],
                counterparty_asset=got["asset"], counterparty_amount=got["amount"],
                notes="Kraken Fiat Exchange",
            ))

    return standalone + trades


# ============================================================================
# MAIN
# ============================================================================

def write_csv(path: str, rows: List[Dict[str, str]], columns: List[str]) -> None:
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=columns)
        writer.writeheader()
        for row in rows:
            writer.writerow({col: row.get(col, "") for col in columns})


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Normalize exchange exports into unified ledger.")
    parser.add_argument("--binance-dir", default=BINANCE_DIR, help="Path to Binance CSV directory.")
    parser.add_argument("--kraken-dir", default=KRAKEN_DIR, help="Path to Kraken CSV directory.")
    parser.add_argument("--output-dir", default="outputs", help="Output directory.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()

    print("Normalizing Binance exports...")
    binance_rows = normalize_binance(args.binance_dir)
    print(f"  Binance: {len(binance_rows)} records")

    print("Normalizing Kraken exports...")
    kraken_rows = normalize_kraken(args.kraken_dir)
    print(f"  Kraken: {len(kraken_rows)} records")

    all_rows = binance_rows + kraken_rows
    all_rows.sort(key=lambda r: r["date"])

    # Write outputs
    os.makedirs(args.output_dir, exist_ok=True)
    write_csv(os.path.join(args.output_dir, "normalized_binance.csv"), binance_rows, UNIFIED_COLUMNS)
    write_csv(os.path.join(args.output_dir, "normalized_kraken.csv"), kraken_rows, UNIFIED_COLUMNS)
    write_csv(os.path.join(args.output_dir, "normalized_all_exchanges.csv"), all_rows, UNIFIED_COLUMNS)

    # Print summary
    from collections import Counter
    type_counts = Counter(r["tx_type"] for r in all_rows)
    print(f"\nTotal: {len(all_rows)} normalized records")
    print("By type:")
    for t, c in type_counts.most_common():
        print(f"  {t}: {c}")

    # Print by year
    year_counts = Counter(r["date"][:4] for r in all_rows)
    print("By year:")
    for y, c in sorted(year_counts.items()):
        print(f"  {y}: {c}")

    print(f"\nOutput written to {args.output_dir}/")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
