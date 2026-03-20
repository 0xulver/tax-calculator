"""Tests for the salary payment parser."""
import os
from decimal import Decimal
from unittest.mock import MagicMock

import pytest

from tax_calc.models import FIFOLot
from tax_calc.nbp import NBPClient
from tax_calc.normalizers.salary import parse_salary_payments


def test_parse_salary_payments(tmp_path):
    """Parse the salary payments file format."""
    content = """  https://polygonscan.com/tx/0xabc123
  Apr-01-2025
  4500 USDC

  https://polygonscan.com/tx/0xdef456
  Mar-17-2025
  6000 USDC

  Total
 10500 USDC"""

    path = str(tmp_path / "payments.txt")
    with open(path, "w") as f:
        f.write(content)

    nbp = MagicMock(spec=NBPClient)
    nbp.get_rate.return_value = Decimal("4.05")

    lots = parse_salary_payments(path, nbp)

    assert len(lots) == 2
    # Sorted by date
    assert lots[0].date == "2025-03-17"
    assert lots[0].amount == Decimal("6000")
    assert lots[0].cost_pln == Decimal("24300")  # 6000 * 4.05
    assert lots[0].source == "polygon_salary"

    assert lots[1].date == "2025-04-01"
    assert lots[1].amount == Decimal("4500")
    assert lots[1].cost_pln == Decimal("18225")  # 4500 * 4.05


def test_salary_lot_has_tx_hash(tmp_path):
    content = """  https://polygonscan.com/tx/0xabc123
  Jan-02-2025
  6000 USDC"""

    path = str(tmp_path / "payments.txt")
    with open(path, "w") as f:
        f.write(content)

    nbp = MagicMock(spec=NBPClient)
    nbp.get_rate.return_value = Decimal("4.0")

    lots = parse_salary_payments(path, nbp)
    assert lots[0].source_tx_id == "0xabc123"
