"""Shared helpers for exchange normalizers."""
from __future__ import annotations

import csv
import os
from decimal import Decimal, getcontext

from tax_calc.models import Transaction

getcontext().prec = 36

UNIFIED_COLUMNS = [
    "date", "source", "source_tx_id", "tx_type", "asset", "amount",
    "fee", "fee_asset", "counterparty_asset", "counterparty_amount", "notes",
]


def parse_decimal(value: str) -> Decimal:
    try:
        return Decimal(value.strip())
    except Exception:
        return Decimal("0")


def write_csv(path: str, rows: list[dict[str, str]], columns: list[str] | None = None) -> None:
    columns = columns or UNIFIED_COLUMNS
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=columns)
        writer.writeheader()
        for row in rows:
            writer.writerow({col: row.get(col, "") for col in columns})
