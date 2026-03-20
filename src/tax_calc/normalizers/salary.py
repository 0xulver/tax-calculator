"""Parse Polygon salary payments into FIFO lots with NBP-based cost basis."""
from __future__ import annotations

import re
from datetime import datetime
from decimal import Decimal
from typing import Optional

from tax_calc.models import FIFOLot
from tax_calc.nbp import NBPClient


def parse_salary_payments(
    path: str,
    nbp: NBPClient,
) -> list[FIFOLot]:
    """Parse 2025-polygon-payments.txt format into FIFOLots.

    Format (repeating blocks):
        https://polygonscan.com/tx/0x...
        Apr-01-2025
        4500 USDC

    Each payment produces a FIFOLot:
        date = payment date
        amount = USDC amount
        cost_pln = amount * NBP USD rate (from last business day before payment)
        source = "polygon_salary"
    """
    with open(path, "r") as f:
        text = f.read()

    lots: list[FIFOLot] = []
    lines = [l.strip() for l in text.strip().splitlines() if l.strip()]

    i = 0
    while i < len(lines):
        line = lines[i]

        # Skip "Total" summary lines
        if line.lower().startswith("total"):
            break

        # Look for URL line
        if line.startswith("http"):
            tx_url = line
            i += 1
            if i >= len(lines):
                break

            # Date line: "Apr-01-2025"
            date_str = lines[i]
            i += 1
            if i >= len(lines):
                break

            # Amount line: "4500 USDC"
            amount_line = lines[i]
            i += 1

            lot = _parse_payment(tx_url, date_str, amount_line, nbp)
            if lot:
                lots.append(lot)
        else:
            i += 1

    lots.sort(key=lambda l: l.date)
    return lots


def _parse_payment(
    tx_url: str,
    date_str: str,
    amount_line: str,
    nbp: NBPClient,
) -> Optional[FIFOLot]:
    # Parse date: "Apr-01-2025" -> "2025-04-01"
    try:
        dt = datetime.strptime(date_str, "%b-%d-%Y")
        iso_date = dt.strftime("%Y-%m-%d")
    except ValueError:
        return None

    # Parse amount: "4500 USDC"
    match = re.match(r"(\d+(?:\.\d+)?)\s+(\w+)", amount_line)
    if not match:
        return None

    amount = Decimal(match.group(1))
    asset = match.group(2).upper()

    # Get NBP USD rate for cost basis
    usd_rate = nbp.get_rate("USD", iso_date)
    cost_pln = amount * usd_rate if usd_rate else Decimal("0")

    # Extract tx hash from URL for source_tx_id
    tx_hash = tx_url.split("/tx/")[-1] if "/tx/" in tx_url else ""

    return FIFOLot(
        date=iso_date,
        amount=amount,
        cost_pln=cost_pln,
        source="polygon_salary",
        source_tx_id=tx_hash,
    )
