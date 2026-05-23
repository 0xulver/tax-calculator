"""Tests for the fixed Binance normalizer."""
import csv
import os
import tempfile
from decimal import Decimal

import pytest

from tax_calc.normalizers.binance import normalize_binance


def _write_csv(rows, tmpdir):
    """Write test rows as a Binance CSV file and return the directory."""
    path = os.path.join(tmpdir, "binance_all_transactions_2020_2025.csv")
    fieldnames = ["user_id", "time", "account", "operation", "coin", "change", "remark", "source_file", "export_year"]
    with open(path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)
    return tmpdir


def _row(time, op, coin, change, remark=""):
    return {
        "user_id": "1", "time": time, "account": "Spot",
        "operation": op, "coin": coin, "change": str(change),
        "remark": remark, "source_file": "test.csv", "export_year": "2025",
    }


class TestPatternA_BuySpend:
    """Fix 5a: Transaction Buy (fiat) + Transaction Spend (crypto) = SELL crypto."""

    def test_single_fill_usdc_to_eur(self, tmp_path):
        """Single fill: 1000.645 USDC -> 971.5 EUR."""
        rows = [
            _row("25-01-16 09:41:12", "Transaction Fee", "EUR", "-0.922925"),
            _row("25-01-16 09:41:12", "Transaction Spend", "USDC", "-1000.645"),
            _row("25-01-16 09:41:12", "Transaction Buy", "EUR", "971.5"),
        ]
        txns = normalize_binance(_write_csv(rows, str(tmp_path)))

        sells = [t for t in txns if t.tx_type == "sell"]
        assert len(sells) == 1

        s = sells[0]
        assert s.asset == "USDC"
        assert s.amount == Decimal("1000.645")
        assert s.counterparty_asset == "EUR"
        assert s.counterparty_amount == Decimal("971.5")
        assert s.fee == Decimal("0.922925")

    def test_multi_fill_aggregation(self, tmp_path):
        """Multi-fill: 3 buy + 3 spend rows -> 1 aggregated sell."""
        rows = [
            _row("25-02-04 11:26:36", "Transaction Fee", "EUR", "-0.527345"),
            _row("25-02-04 11:26:36", "Transaction Fee", "EUR", "-0.389785"),
            _row("25-02-04 11:26:36", "Transaction Spend", "USDC", "-2000.45572"),
            _row("25-02-04 11:26:36", "Transaction Spend", "USDC", "-573.64034"),
            _row("25-02-04 11:26:36", "Transaction Fee", "EUR", "-1.83901"),
            _row("25-02-04 11:26:36", "Transaction Buy", "EUR", "1935.8"),
            _row("25-02-04 11:26:36", "Transaction Buy", "EUR", "555.1"),
            _row("25-02-04 11:26:36", "Transaction Buy", "EUR", "410.3"),
            _row("25-02-04 11:26:36", "Transaction Spend", "USDC", "-424.04505"),
        ]
        txns = normalize_binance(_write_csv(rows, str(tmp_path)))

        sells = [t for t in txns if t.tx_type == "sell"]
        assert len(sells) == 1, f"Expected 1 sell, got {len(sells)}: {sells}"

        s = sells[0]
        assert s.asset == "USDC"
        assert s.amount == Decimal("2998.14111")  # sum of all spends
        assert s.counterparty_asset == "EUR"
        assert s.counterparty_amount == Decimal("2901.2")  # sum of all buys

    def test_not_inverted_asset(self, tmp_path):
        """The sell row must have asset=crypto, not asset=fiat."""
        rows = [
            _row("25-01-16 09:41:12", "Transaction Spend", "USDC", "-100"),
            _row("25-01-16 09:41:12", "Transaction Buy", "EUR", "95"),
        ]
        txns = normalize_binance(_write_csv(rows, str(tmp_path)))
        sells = [t for t in txns if t.tx_type == "sell"]
        assert len(sells) == 1
        assert sells[0].asset == "USDC"  # NOT EUR
        assert sells[0].counterparty_asset == "EUR"


class TestPatternB_SoldRevenue:
    """Fix 5c: Transaction Sold (crypto) + Transaction Revenue."""

    def test_sold_btc_for_usdt_is_swap(self, tmp_path):
        """BTC -> USDT is crypto-to-crypto swap (not taxable under Polish law)."""
        rows = [
            _row("21-08-11 13:45:53", "Transaction Sold", "BTC", "-0.087955"),
            _row("21-08-11 13:45:53", "Transaction Sold", "BTC", "-0.012045"),
            _row("21-08-11 13:45:53", "Transaction Revenue", "USDT", "4000"),
            _row("21-08-11 13:45:53", "Transaction Revenue", "USDT", "704.49"),
            _row("21-08-11 13:45:53", "Transaction Fee", "USDT", "-4.70"),
        ]
        txns = normalize_binance(_write_csv(rows, str(tmp_path)))
        swaps = [t for t in txns if t.tx_type == "swap_out"]
        assert len(swaps) == 1

        s = swaps[0]
        assert s.asset == "BTC"
        assert s.amount == Decimal("0.1")  # 0.087955 + 0.012045
        assert s.counterparty_asset == "USDT"
        assert s.counterparty_amount == Decimal("4704.49")

        # Should also have a swap_in for USDT
        swap_ins = [t for t in txns if t.tx_type == "swap_in"]
        assert len(swap_ins) == 1
        assert swap_ins[0].asset == "USDT"

    def test_sold_btc_for_eur_is_sell(self, tmp_path):
        """BTC -> EUR is a taxable sell."""
        rows = [
            _row("21-08-11 13:45:53", "Transaction Sold", "BTC", "-0.1"),
            _row("21-08-11 13:45:53", "Transaction Revenue", "EUR", "4000"),
        ]
        txns = normalize_binance(_write_csv(rows, str(tmp_path)))
        sells = [t for t in txns if t.tx_type == "sell"]
        assert len(sells) == 1
        assert sells[0].asset == "BTC"
        assert sells[0].counterparty_asset == "EUR"


class TestPatternC_SellCryptoToFiat:
    """Fix 5b: 'Sell Crypto To Fiat' with 1-second merge."""

    def test_paired_1_second_apart(self, tmp_path):
        """EUR at :55 and ETH at :56 should merge into one sell."""
        rows = [
            _row("24-10-15 12:19:55", "Sell Crypto To Fiat", "EUR", "1362.04",
                 "Via CashBalance"),
            _row("24-10-15 12:19:56", "Sell Crypto To Fiat", "ETH", "-0.575001",
                 "Via CashBalance"),
        ]
        txns = normalize_binance(_write_csv(rows, str(tmp_path)))
        sells = [t for t in txns if t.tx_type == "sell"]
        assert len(sells) == 1

        s = sells[0]
        assert s.asset == "ETH"
        assert s.amount == Decimal("0.575001")
        assert s.counterparty_asset == "EUR"
        assert s.counterparty_amount == Decimal("1362.04")

    def test_same_second_pair(self, tmp_path):
        """Paired rows at the same second."""
        rows = [
            _row("24-11-04 16:54:40", "Sell Crypto To Fiat", "ETH", "-1.3151",
                 "Via CashBalance"),
            _row("24-11-04 16:54:40", "Sell Crypto To Fiat", "EUR", "2939.89",
                 "Via CashBalance"),
        ]
        txns = normalize_binance(_write_csv(rows, str(tmp_path)))
        sells = [t for t in txns if t.tx_type == "sell"]
        assert len(sells) == 1
        assert sells[0].asset == "ETH"
        assert sells[0].counterparty_asset == "EUR"

    def test_unpaired_lone_eth_sell(self, tmp_path):
        """Lone ETH debit with no paired EUR row -> sell with no counterparty."""
        rows = [
            _row("24-11-04 16:52:04", "Sell Crypto To Fiat", "ETH", "-0.015",
                 "via Paymonade"),
        ]
        txns = normalize_binance(_write_csv(rows, str(tmp_path)))
        sells = [t for t in txns if t.tx_type == "sell"]
        assert len(sells) == 1
        assert sells[0].asset == "ETH"
        assert sells[0].amount == Decimal("0.015")

    def test_unpaired_lone_eth_sell_with_manual_counterparty(self, tmp_path):
        """Manual override supplies missing Paymonade fiat proceeds."""
        rows = [
            _row("24-11-04 16:52:04", "Sell Crypto To Fiat", "ETH", "-0.015",
                 "via Paymonade - Ref - 2024110415420487673581626368"),
        ]
        _write_csv(rows, str(tmp_path))
        with open(tmp_path / "binance_fiat_counterparty_overrides.csv", "w", newline="") as f:
            writer = csv.DictWriter(
                f,
                fieldnames=[
                    "time", "operation", "coin", "change",
                    "counterparty_asset", "counterparty_amount", "notes",
                ],
            )
            writer.writeheader()
            writer.writerow({
                "time": "24-11-04 16:52:04",
                "operation": "Sell Crypto To Fiat",
                "coin": "ETH",
                "change": "-0.015",
                "counterparty_asset": "EUR",
                "counterparty_amount": "33.53231693",
                "notes": "Estimated from adjacent sale",
            })

        txns = normalize_binance(str(tmp_path))
        sells = [t for t in txns if t.tx_type == "sell"]
        assert len(sells) == 1
        assert sells[0].asset == "ETH"
        assert sells[0].amount == Decimal("0.015")
        assert sells[0].counterparty_asset == "EUR"
        assert sells[0].counterparty_amount == Decimal("33.53231693")


class TestConversions:
    """Binance Convert: crypto-to-fiat, stablecoin-to-stablecoin."""

    def test_stablecoin_to_fiat_convert(self, tmp_path):
        """USDC -> EUR via Binance Convert should be a sell."""
        rows = [
            _row("25-02-04 11:27:13", "Binance Convert", "EUR", "0.09921139"),
            _row("25-02-04 11:27:13", "Binance Convert", "USDC", "-0.10334"),
        ]
        txns = normalize_binance(_write_csv(rows, str(tmp_path)))
        sells = [t for t in txns if t.tx_type == "sell"]
        assert len(sells) == 1
        assert sells[0].asset == "USDC"
        assert sells[0].counterparty_asset == "EUR"

    def test_stablecoin_to_stablecoin_convert(self, tmp_path):
        """USDT -> USDC is a swap, not a sell."""
        rows = [
            _row("25-05-06 10:57:54", "Binance Convert", "USDC", "3000"),
            _row("25-05-06 10:57:54", "Binance Convert", "USDT", "-3000"),
        ]
        txns = normalize_binance(_write_csv(rows, str(tmp_path)))
        swaps = [t for t in txns if t.tx_type in ("swap_in", "swap_out")]
        assert len(swaps) == 2
        sells = [t for t in txns if t.tx_type == "sell"]
        assert len(sells) == 0


class TestBuyWithFiat:
    """Buying crypto with fiat: fiat spend + crypto buy."""

    def test_sol_buy_with_usdc(self, tmp_path):
        """Buy SOL with USDC -> buy transaction."""
        rows = [
            _row("25-03-02 17:06:36", "Transaction Spend", "USDC", "-894.08"),
            _row("25-03-02 17:06:36", "Transaction Buy", "SOL", "5.5"),
            _row("25-03-02 17:06:36", "Transaction Fee", "SOL", "-0.005225"),
        ]
        txns = normalize_binance(_write_csv(rows, str(tmp_path)))
        swaps = [t for t in txns if t.tx_type in ("swap_in", "swap_out")]
        assert len(swaps) == 2  # crypto-to-crypto swap

    def test_buy_crypto_with_card_pairs_fiat_spend(self, tmp_path):
        """Buy Crypto With Card should become one crypto buy with EUR counterparty."""
        rows = [
            _row("21-09-24 14:34:08", "Buy Crypto With Card", "EUR", "-882.9",
                 "Ref - N01137894764195629056092434"),
            _row("21-09-24 14:34:08", "Buy Crypto With Card", "LUNA", "30.43532966",
                 "Ref - N01137894764195629056092434"),
        ]
        txns = normalize_binance(_write_csv(rows, str(tmp_path)))
        buys = [t for t in txns if t.tx_type == "buy"]
        assert len(buys) == 1
        assert buys[0].asset == "LUNA"
        assert buys[0].amount == Decimal("30.43532966")
        assert buys[0].counterparty_asset == "EUR"
        assert buys[0].counterparty_amount == Decimal("882.9")

    def test_buy_crypto_with_fiat_manual_counterparty(self, tmp_path):
        """Manual override supplies missing Paymonade fiat cost."""
        rows = [
            _row("25-06-20 13:14:58", "Buy Crypto With Fiat", "USDC", "2275.36649",
                 "via Paymonade - Ref - 20250620125030584868150282"),
        ]
        _write_csv(rows, str(tmp_path))
        with open(tmp_path / "binance_fiat_counterparty_overrides.csv", "w", newline="") as f:
            writer = csv.DictWriter(
                f,
                fieldnames=[
                    "time", "operation", "coin", "change",
                    "counterparty_asset", "counterparty_amount", "notes",
                ],
            )
            writer.writeheader()
            writer.writerow({
                "time": "25-06-20 13:14:58",
                "operation": "Buy Crypto With Fiat",
                "coin": "USDC",
                "change": "2275.36649",
                "counterparty_asset": "EUR",
                "counterparty_amount": "2000",
                "notes": "Matched to private bank evidence",
            })

        txns = normalize_binance(str(tmp_path))
        buys = [t for t in txns if t.tx_type == "buy"]
        assert len(buys) == 1
        assert buys[0].asset == "USDC"
        assert buys[0].amount == Decimal("2275.36649")
        assert buys[0].counterparty_asset == "EUR"
        assert buys[0].counterparty_amount == Decimal("2000")
