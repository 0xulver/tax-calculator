"""Coinbase transaction history normalizer."""
from __future__ import annotations

import csv
import glob
import os
import re
from datetime import datetime, timezone
from decimal import Decimal

from tax_calc.constants import is_fiat
from tax_calc.models import Transaction
from tax_calc.normalizers.base import parse_decimal


_CONVERT_RE = re.compile(
    r"Converted\s+([0-9.]+)\s+([A-Z0-9]+)\s+to\s+([0-9.]+)\s+([A-Z0-9]+)",
    re.IGNORECASE,
)


def _parse_time(time_str: str) -> datetime:
    value = time_str.strip()
    if not value:
        raise ValueError("Missing Coinbase timestamp")

    if value.endswith("Z"):
        value = value[:-1] + "+00:00"
    dt = datetime.fromisoformat(value)
    if dt.tzinfo is None:
        return dt.replace(tzinfo=timezone.utc)
    return dt.astimezone(timezone.utc)


def _tx(
    dt: datetime,
    tx_type: str,
    asset: str,
    amount: Decimal,
    *,
    fee: Decimal = Decimal("0"),
    fee_asset: str = "",
    cp_asset: str = "",
    cp_amount: Decimal = Decimal("0"),
    notes: str = "",
    txid: str = "",
) -> Transaction:
    return Transaction(
        date=dt.isoformat(),
        source="coinbase",
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


def normalize_coinbase(coinbase_dir: str) -> list[Transaction]:
    """Normalize Coinbase transaction-history CSVs into the unified shape."""
    if not os.path.isdir(coinbase_dir):
        return []

    csv_files = sorted(glob.glob(os.path.join(coinbase_dir, "*.csv")))
    if not csv_files:
        return []

    txns: list[Transaction] = []
    for path in csv_files:
        with open(path, "r", encoding="utf-8-sig") as f:
            reader = csv.DictReader(f)
            for row in reader:
                txns.extend(_normalize_row(row))

    txns.sort(key=lambda t: t.date)
    return txns


def _normalize_row(row: dict[str, str]) -> list[Transaction]:
    time_str = _field(row, "Timestamp", "timestamp")
    raw_type = _field(row, "Transaction Type", "Type", "type")
    asset = _field(row, "Asset", "asset").upper()
    notes = _field(row, "Notes", "notes")
    txid = _field(row, "ID", "Transaction ID", "Transaction Hash", "Reference")

    if not time_str or not raw_type or not asset:
        return []

    dt = _parse_time(time_str)
    qty = parse_decimal(_field(row, "Quantity Transacted", "Quantity", "quantity"))
    subtotal, subtotal_currency = _amount_field(row, direct_names=("Subtotal",), suffixes=(" Subtotal",))
    total, total_currency = _amount_field(
        row,
        direct_names=("Total (inclusive of fees and/or spread)", "Total (inclusive of fees)", "Total"),
        suffixes=(" Total (inclusive of fees and/or spread)", " Total (inclusive of fees)", " Total"),
    )
    fee, fee_currency = _amount_field(
        row,
        direct_names=("Fees and/or Spread", "Fees", "Fee"),
        suffixes=(" Fees and/or Spread", " Fees", " Fee"),
    )
    fiat_currency = (
        _field(row, "Spot Price Currency", "Settlement Currency").upper()
        or subtotal_currency
        or fee_currency
        or total_currency
    )

    tx_type = raw_type.strip().lower()
    qty_abs = qty.copy_abs()
    subtotal_abs = subtotal.copy_abs()
    total_abs = total.copy_abs()
    fee_abs = fee.copy_abs()

    if tx_type in {"buy", "advanced trade buy"}:
        cp_amount = subtotal_abs or max(total_abs - fee_abs, Decimal("0"))
        return [_tx(
            dt, "buy", asset, qty_abs,
            fee=fee_abs, fee_asset=fiat_currency,
            cp_asset=fiat_currency, cp_amount=cp_amount,
            notes=f"Coinbase {raw_type}", txid=txid,
        )]

    if tx_type in {"sell", "advanced trade sell"}:
        cp_amount = subtotal_abs or (total_abs + fee_abs if total_abs else Decimal("0"))
        return [_tx(
            dt, "sell", asset, qty_abs,
            fee=fee_abs, fee_asset=fiat_currency,
            cp_asset=fiat_currency, cp_amount=cp_amount,
            notes=f"Coinbase {raw_type}", txid=txid,
        )]

    if tx_type == "convert":
        return _normalize_convert(dt, notes, txid)

    if tx_type in {"receive", "deposit"}:
        kind = "fiat_deposit" if is_fiat(asset) else "deposit"
        return [_tx(dt, kind, asset, qty_abs, notes=f"Coinbase {raw_type}", txid=txid)]

    if tx_type in {"send", "withdrawal", "withdraw"}:
        kind = "fiat_withdrawal" if is_fiat(asset) else "withdrawal"
        return [_tx(dt, kind, asset, qty_abs, notes=f"Coinbase {raw_type}", txid=txid)]

    if tx_type in {"rewards income", "staking income", "learning reward", "inflation reward"}:
        return [_tx(dt, "earn_reward", asset, qty_abs, notes=f"Coinbase {raw_type}", txid=txid)]

    return [_tx(dt, "unknown", asset, qty, notes=f"Coinbase {raw_type}", txid=txid)]


def _normalize_convert(dt: datetime, notes: str, txid: str) -> list[Transaction]:
    match = _CONVERT_RE.search(notes)
    if not match:
        return []

    from_amount = Decimal(match.group(1))
    from_asset = match.group(2).upper()
    to_amount = Decimal(match.group(3))
    to_asset = match.group(4).upper()

    return [
        _tx(dt, "swap_out", from_asset, from_amount, cp_asset=to_asset, cp_amount=to_amount, notes="Coinbase Convert", txid=txid),
        _tx(dt, "swap_in", to_asset, to_amount, cp_asset=from_asset, cp_amount=from_amount, notes="Coinbase Convert", txid=txid),
    ]


def _field(row: dict[str, str], *names: str) -> str:
    for name in names:
        value = row.get(name, "")
        if value and value.strip():
            return value.strip()
    return ""


def _amount_field(row: dict[str, str], *, direct_names: tuple[str, ...], suffixes: tuple[str, ...]) -> tuple[Decimal, str]:
    for name in direct_names:
        value = row.get(name, "")
        if value and value.strip():
            return parse_decimal(value), ""

    for key, value in row.items():
        if not value or not value.strip():
            continue
        for suffix in suffixes:
            if key.endswith(suffix):
                currency = key.removesuffix(suffix).strip().upper()
                return parse_decimal(value), currency
    return Decimal("0"), ""
