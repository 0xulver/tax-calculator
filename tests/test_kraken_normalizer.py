"""Tests for the Kraken normalizer."""
import csv
import os
from decimal import Decimal

import pytest

from tax_calc.normalizers.kraken import normalize_kraken


def _write_kraken_csv(rows, tmpdir, filename="kraken_test.csv"):
    path = os.path.join(tmpdir, filename)
    fieldnames = ["txid", "refid", "time", "type", "subtype", "aclass", "subclass",
                  "asset", "wallet", "amount", "fee", "balance"]
    with open(path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)
    return tmpdir


def _row(txid, refid, time, type_, subtype, subclass, asset, amount, fee, balance="0"):
    return {
        "txid": txid, "refid": refid, "time": time, "type": type_,
        "subtype": subtype, "aclass": "currency", "subclass": subclass,
        "asset": asset, "wallet": "spot / main",
        "amount": str(amount), "fee": str(fee), "balance": str(balance),
    }


class TestKrakenTrades:

    def test_sell_crypto_for_fiat(self, tmp_path):
        """USDC -> EUR trade: gave USDC, got EUR."""
        rows = [
            _row("TX1", "REF1", "2025-01-16 08:48:23", "trade", "tradespot",
                 "stable_coin", "USDC", "-4000.00000100", "0"),
            _row("TX2", "REF1", "2025-01-16 08:48:23", "trade", "tradespot",
                 "fiat", "EUR", "3883.6000", "7.7672"),
        ]
        txns = normalize_kraken(str(_write_kraken_csv(rows, str(tmp_path))))
        sells = [t for t in txns if t.tx_type == "sell"]
        assert len(sells) == 1

        s = sells[0]
        assert s.asset == "USDC"
        assert s.amount == Decimal("4000.00000100")
        assert s.counterparty_asset == "EUR"
        assert s.counterparty_amount == Decimal("3883.6000")
        assert s.fee == Decimal("7.7672")

    def test_buy_crypto_with_fiat(self, tmp_path):
        """EUR -> DOT trade: gave EUR, got DOT."""
        rows = [
            _row("TX1", "REF1", "2025-08-07 19:43:53", "trade", "tradespot",
                 "fiat", "ZEUR", "-6.7805", "0.0271"),
            _row("TX2", "REF1", "2025-08-07 19:43:53", "trade", "tradespot",
                 "crypto", "DOT", "2.1009309200", "0"),
        ]
        txns = normalize_kraken(str(_write_kraken_csv(rows, str(tmp_path))))
        buys = [t for t in txns if t.tx_type == "buy"]
        assert len(buys) == 1
        assert buys[0].asset == "DOT"

    def test_dedup_by_txid(self, tmp_path):
        """Duplicate txids across year files should be deduplicated."""
        rows = [
            _row("TX1", "REF1", "2025-01-16 08:48:23", "trade", "tradespot",
                 "stable_coin", "USDC", "-4000", "0"),
            _row("TX2", "REF1", "2025-01-16 08:48:23", "trade", "tradespot",
                 "fiat", "EUR", "3883.6", "7.7672"),
        ]
        # Write to two "year" files
        d = str(tmp_path)
        _write_kraken_csv(rows, d, "kraken_2024.csv")
        _write_kraken_csv(rows, d, "kraken_2025.csv")

        txns = normalize_kraken(d)
        sells = [t for t in txns if t.tx_type == "sell"]
        assert len(sells) == 1  # not 2


class TestKrakenDepositsWithdrawals:

    def test_deposit(self, tmp_path):
        rows = [
            _row("TX1", "REF1", "2025-01-16 08:45:16", "deposit", "",
                 "stable_coin", "USDC", "3997", "0"),
        ]
        txns = normalize_kraken(str(_write_kraken_csv(rows, str(tmp_path))))
        deps = [t for t in txns if t.tx_type == "deposit"]
        assert len(deps) == 1
        assert deps[0].asset == "USDC"
        assert deps[0].amount == Decimal("3997")

    def test_fiat_withdrawal(self, tmp_path):
        rows = [
            _row("TX1", "REF1", "2025-01-16 08:50:09", "withdrawal", "",
                 "fiat", "ZEUR", "-3874.83", "1.0"),
        ]
        txns = normalize_kraken(str(_write_kraken_csv(rows, str(tmp_path))))
        w = [t for t in txns if t.tx_type == "fiat_withdrawal"]
        assert len(w) == 1
        assert w[0].asset == "EUR"  # normalized from ZEUR
