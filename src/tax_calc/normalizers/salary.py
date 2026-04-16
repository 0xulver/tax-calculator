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
    source_name: str = "polygon_salary",
) -> list[FIFOLot]:
    """Parse salary/purchase payment files into FIFOLots.

    Format (repeating blocks):
        https://example.com/tx/0x...
        Apr-01-2025
        4500 USDC

    Each payment produces a FIFOLot with cost_pln based on the
    appropriate NBP rate (USD for USDC/USDT, EUR for EUR, etc.).
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

            fee_lines: list[str] = []
            while i < len(lines):
                next_line = lines[i]
                if next_line.startswith("http") or next_line.lower().startswith("total"):
                    break
                if next_line.lower().startswith("fee"):
                    fee_lines.append(next_line)
                i += 1

            lot = _parse_payment(tx_url, date_str, amount_line, nbp, source_name, fee_lines=fee_lines)
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
    source_name: str = "polygon_salary",
    fee_lines: Optional[list[str]] = None,
) -> Optional[FIFOLot]:
    # Parse date: "Apr-01-2025" -> "2025-04-01"
    try:
        dt = datetime.strptime(date_str, "%b-%d-%Y")
        iso_date = dt.strftime("%Y-%m-%d")
    except ValueError:
        return None

    parsed = _parse_amount_line(amount_line)
    if not parsed:
        return None

    amount, asset = parsed

    # Determine NBP currency based on asset
    # USDC/USDT -> USD rate; EUR -> EUR rate; SEK -> SEK rate
    nbp_currency = _nbp_currency_for_asset(asset)

    rate = nbp.get_rate(nbp_currency, iso_date)
    cost_pln = amount * rate if rate else Decimal("0")

    for fee_line in fee_lines or []:
        parsed_fee = _parse_fee_line(fee_line)
        if not parsed_fee:
            continue

        fee_amount, fee_asset = parsed_fee
        fee_currency = _nbp_currency_for_asset(fee_asset)
        fee_rate = nbp.get_rate(fee_currency, iso_date)
        if fee_rate:
            cost_pln += fee_amount * fee_rate
        if fee_asset == asset:
            amount += fee_amount

    # Extract tx hash from URL for source_tx_id
    tx_hash = tx_url.split("/tx/")[-1] if "/tx/" in tx_url else ""

    return FIFOLot(
        date=iso_date,
        amount=amount,
        cost_pln=cost_pln,
        source=source_name,
        source_tx_id=tx_hash,
        asset=asset,
        fiat_currency=nbp_currency,
    )


def _parse_amount_line(amount_line: str) -> Optional[tuple[Decimal, str]]:
    match = re.match(r"(\d+(?:\.\d+)?)\s+(\w+)", amount_line.strip())
    if not match:
        return None
    return Decimal(match.group(1)), match.group(2).upper()


def _parse_fee_line(fee_line: str) -> Optional[tuple[Decimal, str]]:
    match = re.match(r"fee\s*:?\s*(\d+(?:\.\d+)?)\s+(\w+)", fee_line.strip(), re.IGNORECASE)
    if not match:
        return None
    return Decimal(match.group(1)), match.group(2).upper()


def _nbp_currency_for_asset(asset: str) -> str:
    asset = asset.upper()
    return asset if asset in ("EUR", "SEK", "USD", "GBP") else "USD"
