"""FTX core transactions normalizer."""
from __future__ import annotations

import csv
import glob
import os
import sys
from collections import defaultdict
from datetime import datetime, timezone
from decimal import Decimal

from tax_calc.constants import is_fiat
from tax_calc.models import Transaction
from tax_calc.normalizers.base import parse_decimal


def _parse_time(time_str: str) -> datetime:
    time_str = time_str.strip()
    for fmt in ("%Y-%m-%d %H:%M:%S.%f", "%Y-%m-%d %H:%M:%S"):
        try:
            return datetime.strptime(time_str, fmt).replace(tzinfo=timezone.utc)
        except ValueError:
            continue
    raise ValueError(f"Unsupported FTX timestamp: {time_str}")


def _tx(
    dt: datetime,
    tx_type: str,
    asset: str,
    amount: Decimal,
    fee: Decimal = Decimal("0"),
    fee_asset: str = "",
    cp_asset: str = "",
    cp_amount: Decimal = Decimal("0"),
    notes: str = "",
    txid: str = "",
) -> Transaction:
    return Transaction(
        date=dt.isoformat(),
        source="ftx",
        source_tx_id=txid,
        tx_type=tx_type,
        asset=asset,
        amount=amount,
        fee=fee,
        fee_asset=fee_asset,
        counterparty_asset=cp_asset,
        counterparty_amount=cp_amount,
        notes=notes,
    )


def normalize_ftx(ftx_dir: str) -> list[Transaction]:
    """Normalize FTX core transaction exports into the unified transaction shape."""
    csv_files = sorted(glob.glob(os.path.join(ftx_dir, "*.csv")))
    if not csv_files:
        print(f"Warning: no FTX CSV files found in {ftx_dir}", file=sys.stderr)
        return []

    rows: list[dict[str, str]] = []
    for path in csv_files:
        with open(path, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            rows.extend(reader)

    time_groups: dict[str, list[dict[str, object]]] = defaultdict(list)
    for row in rows:
        time_str = row.get("Time", "").strip()
        coin = row.get("Coin", "").strip().upper()
        if not time_str or not coin:
            continue
        time_groups[time_str].append({
            "dt": _parse_time(time_str),
            "coin": coin,
            "quantity": parse_decimal(row.get("Quantity", "0")),
            "description": row.get("Description", "").strip(),
        })

    result: list[Transaction] = []
    for time_str, entries in sorted(time_groups.items(), key=lambda x: x[1][0]["dt"]):
        dt = entries[0]["dt"]
        result.extend(_normalize_non_spot_entries(dt, entries))
        result.extend(_normalize_spot_group(dt, time_str, entries))

    result.sort(key=lambda t: t.date)
    return result


def _normalize_non_spot_entries(dt: datetime, entries: list[dict[str, object]]) -> list[Transaction]:
    out: list[Transaction] = []
    for entry in entries:
        desc = str(entry["description"])
        coin = str(entry["coin"])
        qty = Decimal(entry["quantity"])

        if desc == "Circle deposit":
            out.append(_tx(dt, "fiat_deposit", coin, qty.copy_abs(), notes="FTX Circle deposit"))
        elif desc == "Circle deposit fee":
            out.append(_tx(dt, "funding_fee", coin, qty.copy_abs(), notes="FTX Circle deposit fee"))
        elif desc.startswith("fiat_deposit "):
            ref = desc.split()[-1]
            out.append(_tx(dt, "fiat_deposit", coin, qty.copy_abs(), notes=f"FTX {desc}", txid=ref))
        elif desc.startswith("deposit "):
            ref = desc.split()[-1]
            out.append(_tx(dt, "deposit", coin, qty.copy_abs(), notes=f"FTX {desc}", txid=ref))
        elif desc.startswith("withdrawal "):
            ref = desc.split()[-1]
            tx_type = "fiat_withdrawal" if is_fiat(coin) else "withdrawal"
            out.append(_tx(dt, tx_type, coin, qty.copy_abs(), notes=f"FTX {desc}", txid=ref))
    return out


def _normalize_spot_group(
    dt: datetime,
    time_str: str,
    entries: list[dict[str, object]],
) -> list[Transaction]:
    spot_rows = [e for e in entries if str(e["description"]).startswith("spot_")]
    if not spot_rows:
        return []

    bases = [e for e in spot_rows if e["description"] == "spot_base"]
    quotes = [e for e in spot_rows if e["description"] == "spot_quote"]
    fees = [e for e in spot_rows if e["description"] == "spot_fee"]

    # EUR -> USD and similar fiat-only conversions are useful for traceability
    # but should not affect PIT-38.
    if bases and quotes and all(is_fiat(str(e["coin"])) for e in bases + quotes):
        gave = [e for e in bases if Decimal(e["quantity"]) < 0]
        got = [e for e in quotes if Decimal(e["quantity"]) > 0]
        if len({str(e["coin"]) for e in gave}) == 1 and len({str(e["coin"]) for e in got}) == 1:
            gave_asset = str(gave[0]["coin"])
            got_asset = str(got[0]["coin"])
            gave_amount = sum(-Decimal(e["quantity"]) for e in gave)
            got_amount = sum(Decimal(e["quantity"]) for e in got)
            return [
                _tx(
                    dt,
                    "fiat_exchange",
                    gave_asset,
                    gave_amount,
                    cp_asset=got_asset,
                    cp_amount=got_amount,
                    notes="FTX fiat conversion",
                    txid=time_str,
                )
            ]
        return []

    asset_candidates = {str(e["coin"]) for e in bases if not is_fiat(str(e["coin"]))}
    if len(asset_candidates) != 1:
        return []

    asset = next(iter(asset_candidates))
    asset_bases = [e for e in bases if e["coin"] == asset]
    net_base = sum(Decimal(e["quantity"]) for e in asset_bases)
    if net_base == 0:
        return []

    trade_fee, fee_asset = _extract_fee(fees)

    if net_base > 0:
        quote_rows = [e for e in quotes if Decimal(e["quantity"]) < 0]
        quote_assets = {str(e["coin"]) for e in quote_rows}
        if len(quote_assets) != 1:
            return []
        quote_asset = next(iter(quote_assets))
        quote_amount = sum(-Decimal(e["quantity"]) for e in quote_rows)
        return [
            _tx(
                dt,
                "buy",
                asset,
                net_base,
                fee=trade_fee,
                fee_asset=fee_asset,
                cp_asset=quote_asset,
                cp_amount=quote_amount,
                notes="FTX spot trade",
                txid=time_str,
            )
        ]

    quote_rows = [e for e in quotes if Decimal(e["quantity"]) > 0]
    quote_assets = {str(e["coin"]) for e in quote_rows}
    if len(quote_assets) != 1:
        return []
    quote_asset = next(iter(quote_assets))
    quote_amount = sum(Decimal(e["quantity"]) for e in quote_rows)
    return [
        _tx(
            dt,
            "sell",
            asset,
            -net_base,
            fee=trade_fee,
            fee_asset=fee_asset,
            cp_asset=quote_asset,
            cp_amount=quote_amount,
            notes="FTX spot trade",
            txid=time_str,
        )
    ]


def _extract_fee(fees: list[dict[str, object]]) -> tuple[Decimal, str]:
    negative_fees = [e for e in fees if Decimal(e["quantity"]) < 0]
    if not negative_fees:
        return Decimal("0"), ""

    fee_assets = {str(e["coin"]) for e in negative_fees}
    if len(fee_assets) != 1:
        return Decimal("0"), ""

    fee_asset = next(iter(fee_assets))
    fee_amount = sum(-Decimal(e["quantity"]) for e in negative_fees)
    return fee_amount, fee_asset
