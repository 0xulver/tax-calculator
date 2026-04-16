"""Tests for the Polish PIT-38 cost pool engine."""
from decimal import Decimal
from unittest.mock import MagicMock

import pytest

from tax_calc.cost_pool import process_cost_pool
from tax_calc.models import FIFOLot
from tax_calc.nbp import NBPClient
from tax_calc.prices import PriceResolver


def _make_prices(usd_rate="4.0", eur_rate="4.3"):
    nbp = MagicMock(spec=NBPClient)
    def get_rate(currency, date_str):
        rates = {"PLN": Decimal("1"), "USD": Decimal(usd_rate), "EUR": Decimal(eur_rate)}
        return rates.get(currency.upper())
    def get_rate_with_date(currency, date_str):
        rate = get_rate(currency, date_str)
        return rate, "2025-01-15"  # mock rate date
    nbp.get_rate = get_rate
    nbp.get_rate_with_date = get_rate_with_date
    prices = PriceResolver(nbp)
    prices._get_coingecko_price = MagicMock(return_value=None)
    return prices


class TestBasicCostPool:

    def test_sell_creates_revenue(self):
        """Selling USDC for EUR creates revenue in the cost pool."""
        prices = _make_prices()
        rows = [
            {"date": "2025-01-16T09:41:12+00:00", "source": "binance", "source_tx_id": "",
             "tx_type": "sell", "asset": "USDC", "amount": "1000", "fee": "0",
             "fee_asset": "", "counterparty_asset": "EUR", "counterparty_amount": "950",
             "notes": ""},
        ]
        result = process_cost_pool(rows, prices)
        r2025 = result["yearly_results"][2025]
        assert r2025.disposal_count == 1
        # 950 EUR * 4.3 PLN/EUR = 4085 PLN
        assert r2025.revenue_pln == Decimal("950") * Decimal("4.3")

    def test_buy_creates_cost(self):
        """Buying BTC with EUR creates cost in the cost pool."""
        prices = _make_prices()
        rows = [
            {"date": "2025-01-10T10:00:00+00:00", "source": "kraken", "source_tx_id": "",
             "tx_type": "buy", "asset": "BTC", "amount": "0.1", "fee": "0",
             "fee_asset": "", "counterparty_asset": "EUR", "counterparty_amount": "5000",
             "notes": ""},
        ]
        result = process_cost_pool(rows, prices)
        r2025 = result["yearly_results"][2025]
        assert r2025.disposal_count == 0
        # 5000 EUR * 4.3 = 21500 PLN
        assert r2025.costs_current_year_pln == Decimal("5000") * Decimal("4.3")

    def test_standalone_fee_creates_cost(self):
        """Standalone trade-fee rows should be deductible costs."""
        prices = _make_prices()
        rows = [
            {"date": "2021-05-11T14:08:04+00:00", "source": "ftx", "source_tx_id": "",
             "tx_type": "fee", "asset": "USD", "amount": "10", "fee": "0",
             "fee_asset": "", "counterparty_asset": "", "counterparty_amount": "0",
             "notes": "FTX spot trade fee"},
        ]
        result = process_cost_pool(rows, prices)
        r2021 = result["yearly_results"][2021]
        assert r2021.costs_current_year_pln == Decimal("10") * Decimal("4.0")

    def test_funding_fee_is_ignored(self):
        """Funding and withdrawal-side fees should not enter the PIT-38 cost pool."""
        prices = _make_prices()
        rows = [
            {"date": "2021-05-11T14:08:04+00:00", "source": "ftx", "source_tx_id": "",
             "tx_type": "funding_fee", "asset": "USD", "amount": "10", "fee": "0",
             "fee_asset": "", "counterparty_asset": "", "counterparty_amount": "0",
             "notes": "FTX Circle deposit fee"},
        ]
        result = process_cost_pool(rows, prices)
        r2021 = result["yearly_results"][2021]
        assert r2021.costs_current_year_pln == Decimal("0")

    def test_withdrawal_fee_is_ignored(self):
        prices = _make_prices()
        rows = [
            {"date": "2025-01-16T08:50:09+00:00", "source": "kraken", "source_tx_id": "",
             "tx_type": "fiat_withdrawal", "asset": "EUR", "amount": "3874.83", "fee": "1.0",
             "fee_asset": "EUR", "counterparty_asset": "", "counterparty_amount": "0",
             "notes": "Kraken withdrawal (fiat)"},
        ]

    def test_non_fiat_fee_on_buy_uses_trade_implied_value(self):
        """Fees charged in the acquired asset should still enter the cost pool."""
        prices = _make_prices()
        rows = [
            {"date": "2025-01-10T10:00:00+00:00", "source": "ftx", "source_tx_id": "",
             "tx_type": "buy", "asset": "SNX", "amount": "10", "fee": "0.1",
             "fee_asset": "SNX", "counterparty_asset": "USD", "counterparty_amount": "200",
             "notes": ""},
        ]
        result = process_cost_pool(rows, prices)
        r2025 = result["yearly_results"][2025]
        # Main cost: 200 USD * 4.0 = 800 PLN
        # Fee cost: 0.1 / 10 * 800 = 8 PLN
        assert r2025.costs_current_year_pln == Decimal("808")

    def test_crypto_to_crypto_ignored(self):
        """Crypto-to-crypto swaps create no revenue or cost events."""
        prices = _make_prices()
        rows = [
            {"date": "2025-02-01T10:00:00+00:00", "source": "binance", "source_tx_id": "",
             "tx_type": "swap_out", "asset": "BTC", "amount": "0.1", "fee": "0",
             "fee_asset": "", "counterparty_asset": "ETH", "counterparty_amount": "1.5",
             "notes": ""},
            {"date": "2025-02-01T10:00:00+00:00", "source": "binance", "source_tx_id": "",
             "tx_type": "swap_in", "asset": "ETH", "amount": "1.5", "fee": "0",
             "fee_asset": "", "counterparty_asset": "BTC", "counterparty_amount": "0.1",
             "notes": ""},
        ]
        result = process_cost_pool(rows, prices)
        # Swaps are non-taxable — no revenue, no costs, no tax
        r = result["yearly_results"][2025]
        assert r.revenue_pln == Decimal("0")
        assert r.costs_current_year_pln == Decimal("0")
        assert r.disposal_count == 0
        assert r.tax_due_pln == Decimal("0")


class TestCostCarryForward:

    def test_costs_exceed_revenue_carry_forward(self):
        """When costs > revenue, excess carries forward to next year."""
        prices = _make_prices()
        rows = [
            # 2024: buy BTC for 10000 EUR, no sales
            {"date": "2024-06-01T10:00:00+00:00", "source": "kraken", "source_tx_id": "",
             "tx_type": "buy", "asset": "BTC", "amount": "0.2", "fee": "0",
             "fee_asset": "", "counterparty_asset": "EUR", "counterparty_amount": "10000",
             "notes": ""},
            # 2025: sell BTC for 8000 EUR (smaller amount)
            {"date": "2025-03-01T10:00:00+00:00", "source": "kraken", "source_tx_id": "",
             "tx_type": "sell", "asset": "BTC", "amount": "0.15", "fee": "0",
             "fee_asset": "", "counterparty_asset": "EUR", "counterparty_amount": "8000",
             "notes": ""},
        ]
        result = process_cost_pool(rows, prices)

        r2024 = result["yearly_results"][2024]
        assert r2024.revenue_pln == Decimal("0")
        assert r2024.costs_current_year_pln == Decimal("10000") * Decimal("4.3")
        assert r2024.income_pln == Decimal("0")
        assert r2024.carry_forward_pln == Decimal("10000") * Decimal("4.3")  # 43000

        r2025 = result["yearly_results"][2025]
        assert r2025.revenue_pln == Decimal("8000") * Decimal("4.3")  # 34400
        assert r2025.costs_prior_years_pln == Decimal("10000") * Decimal("4.3")  # 43000 from 2024
        # revenue 34400 < prior costs 43000 → income 0, carry 43000 - 34400 = 8600
        assert r2025.income_pln == Decimal("0")
        assert r2025.carry_forward_pln == (Decimal("10000") - Decimal("8000")) * Decimal("4.3")

    def test_no_tax_when_costs_exceed(self):
        """Zero tax when cost pool exceeds revenue."""
        prices = _make_prices()
        rows = [
            {"date": "2025-01-01T10:00:00+00:00", "source": "binance", "source_tx_id": "",
             "tx_type": "buy", "asset": "ETH", "amount": "10", "fee": "0",
             "fee_asset": "", "counterparty_asset": "EUR", "counterparty_amount": "20000",
             "notes": ""},
            {"date": "2025-06-01T10:00:00+00:00", "source": "binance", "source_tx_id": "",
             "tx_type": "sell", "asset": "ETH", "amount": "1", "fee": "0",
             "fee_asset": "", "counterparty_asset": "EUR", "counterparty_amount": "2500",
             "notes": ""},
        ]
        result = process_cost_pool(rows, prices)
        r = result["yearly_results"][2025]
        assert r.tax_due_pln == Decimal("0")


class TestSalaryUSDCCosts:

    def test_salary_usdc_enters_cost_pool(self):
        """Salary USDC payments become costs in the year received."""
        prices = _make_prices()
        salary_lots = [
            FIFOLot("2025-01-02", Decimal("6000"), Decimal("24000"), "polygon_salary"),
            FIFOLot("2025-01-15", Decimal("6000"), Decimal("24000"), "polygon_salary"),
        ]
        rows = [
            {"date": "2025-01-16T09:41:12+00:00", "source": "binance", "source_tx_id": "",
             "tx_type": "sell", "asset": "USDC", "amount": "6000", "fee": "0",
             "fee_asset": "", "counterparty_asset": "EUR", "counterparty_amount": "5500",
             "notes": ""},
        ]
        result = process_cost_pool(rows, prices, salary_lots)
        r = result["yearly_results"][2025]
        # Costs: 24000 + 24000 = 48000 from salary
        assert r.costs_current_year_pln == Decimal("48000")
        # Revenue: 5500 * 4.3 = 23650
        assert r.revenue_pln == Decimal("5500") * Decimal("4.3")
        # Costs > revenue → 0 tax
        assert r.tax_due_pln == Decimal("0")
        assert r.carry_forward_pln > Decimal("0")


class TestPreResidencyCosts:

    def test_pre_residency_costs_in_first_year(self):
        """Pre-residency costs enter as prior-year costs in the first Polish year."""
        prices = _make_prices()
        rows = [
            {"date": "2023-06-01T10:00:00+00:00", "source": "kraken", "source_tx_id": "",
             "tx_type": "sell", "asset": "BTC", "amount": "0.5", "fee": "0",
             "fee_asset": "", "counterparty_asset": "EUR", "counterparty_amount": "12000",
             "notes": ""},
        ]
        result = process_cost_pool(
            rows, prices,
            pre_residency_costs=Decimal("100000"),
            first_polish_year=2023,
        )
        r = result["yearly_results"][2023]
        assert r.costs_prior_years_pln == Decimal("100000")
        # Revenue: 12000 * 4.3 = 51600
        # Total costs: 100000 > 51600 → income 0
        assert r.income_pln == Decimal("0")
        assert r.carry_forward_pln == Decimal("100000") - Decimal("12000") * Decimal("4.3")
