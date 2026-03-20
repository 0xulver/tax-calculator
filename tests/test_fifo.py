"""Tests for the FIFO engine."""
from decimal import Decimal
from unittest.mock import MagicMock

import pytest

from tax_calc.fifo import FIFOTracker, process_ledger
from tax_calc.models import FIFOLot
from tax_calc.nbp import NBPClient
from tax_calc.prices import PriceResolver


class TestFIFOTracker:

    def test_basic_consume(self):
        tracker = FIFOTracker()
        tracker.add_lot(FIFOLot("2025-01-01", Decimal("100"), Decimal("400"), "test"))
        cost, consumed = tracker.consume(Decimal("50"))
        assert cost == Decimal("200")
        assert len(consumed) == 1
        assert tracker.total_remaining == Decimal("50")

    def test_consume_across_lots(self):
        tracker = FIFOTracker()
        tracker.add_lot(FIFOLot("2025-01-01", Decimal("30"), Decimal("120"), "test1"))
        tracker.add_lot(FIFOLot("2025-01-15", Decimal("70"), Decimal("350"), "test2"))
        cost, consumed = tracker.consume(Decimal("50"))
        # First lot: 30 units @ 4 PLN = 120 PLN
        # Second lot: 20 units @ 5 PLN = 100 PLN
        assert cost == Decimal("220")
        assert len(consumed) == 2

    def test_consume_insufficient_lots(self):
        tracker = FIFOTracker()
        tracker.add_lot(FIFOLot("2025-01-01", Decimal("10"), Decimal("40"), "test"))
        cost, consumed = tracker.consume(Decimal("20"))
        assert cost == Decimal("40")
        assert any(c["lot_date"] == "MISSING" for c in consumed)


class TestSalaryLotInjection:

    def test_salary_lots_consumed_before_zero_cost_deposits(self):
        """Salary FIFO lots should be consumed before exchange deposits."""
        nbp = MagicMock(spec=NBPClient)
        nbp.get_rate.return_value = Decimal("4.0")

        prices = PriceResolver(nbp)
        # Override CoinGecko to not make network calls
        prices._get_coingecko_price = MagicMock(return_value=None)

        salary_lots = [
            FIFOLot("2025-01-02", Decimal("6000"), Decimal("24000"), "polygon_salary"),
        ]

        rows = [
            # Deposit of USDC (would get NBP USD rate valuation)
            {"date": "2025-01-16T09:00:00+00:00", "source": "binance", "source_tx_id": "",
             "tx_type": "deposit", "asset": "USDC", "amount": "1000", "fee": "0",
             "fee_asset": "", "counterparty_asset": "", "counterparty_amount": "0", "notes": ""},
            # Sell USDC for EUR
            {"date": "2025-01-16T09:41:12+00:00", "source": "binance", "source_tx_id": "",
             "tx_type": "sell", "asset": "USDC", "amount": "1000", "fee": "0",
             "fee_asset": "", "counterparty_asset": "EUR", "counterparty_amount": "971.5",
             "notes": ""},
        ]

        result = process_ledger(rows, prices, salary_lots)
        events = result["tax_events"]
        assert len(events) == 1

        # Cost basis should come from salary lot (4 PLN/USD), not zero
        e = events[0]
        assert e.cost_basis_pln > Decimal("0")
        # Salary lot: 6000 USDC @ 24000 PLN = 4 PLN/USDC
        # Selling 1000 USDC -> cost = 1000 * 4 = 4000 PLN (allow precision tolerance)
        assert abs(e.cost_basis_pln - Decimal("4000")) < Decimal("0.01")


class TestStablecoinDepositValuation:

    def test_stablecoin_deposit_gets_nbp_rate(self):
        """USDC deposits should be valued at NBP USD rate, not 0."""
        nbp = MagicMock(spec=NBPClient)
        nbp.get_rate.return_value = Decimal("4.0")

        prices = PriceResolver(nbp)
        prices._get_coingecko_price = MagicMock(return_value=None)

        rows = [
            {"date": "2025-01-16T09:00:00+00:00", "source": "binance", "source_tx_id": "",
             "tx_type": "deposit", "asset": "USDC", "amount": "1000", "fee": "0",
             "fee_asset": "", "counterparty_asset": "", "counterparty_amount": "0", "notes": ""},
            {"date": "2025-01-16T09:41:12+00:00", "source": "binance", "source_tx_id": "",
             "tx_type": "sell", "asset": "USDC", "amount": "1000", "fee": "0",
             "fee_asset": "", "counterparty_asset": "EUR", "counterparty_amount": "971.5",
             "notes": ""},
        ]

        result = process_ledger(rows, prices)
        events = result["tax_events"]
        assert len(events) == 1
        # Deposit should be valued at 1000 * 4.0 = 4000 PLN
        assert events[0].cost_basis_pln == Decimal("4000")
