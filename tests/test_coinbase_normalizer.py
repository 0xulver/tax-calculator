"""Tests for the Coinbase normalizer."""
import csv
import os
from decimal import Decimal

from tax_calc.normalizers.coinbase import normalize_coinbase


def _write_coinbase_csv(rows, tmpdir, filename="coinbase.csv"):
    path = os.path.join(tmpdir, filename)
    fieldnames = [
        "Timestamp", "Transaction Type", "Asset", "Quantity Transacted",
        "Spot Price Currency", "Subtotal", "Total (inclusive of fees and/or spread)",
        "Fees and/or Spread", "Notes", "ID",
    ]
    with open(path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)
    return tmpdir


def _row(timestamp, tx_type, asset, qty, subtotal="", total="", fee="", notes="", txid=""):
    return {
        "Timestamp": timestamp,
        "Transaction Type": tx_type,
        "Asset": asset,
        "Quantity Transacted": str(qty),
        "Spot Price Currency": "EUR",
        "Subtotal": str(subtotal),
        "Total (inclusive of fees and/or spread)": str(total),
        "Fees and/or Spread": str(fee),
        "Notes": notes,
        "ID": txid,
    }


def test_coinbase_buy_with_fee(tmp_path):
    rows = [
        _row(
            "2021-03-13T10:00:00Z", "Buy", "SNX", "30",
            subtotal="590", total="604.99", fee="14.99", txid="cb-buy-1",
        ),
    ]

    txns = normalize_coinbase(_write_coinbase_csv(rows, str(tmp_path)))

    assert len(txns) == 1
    buy = txns[0]
    assert buy.tx_type == "buy"
    assert buy.asset == "SNX"
    assert buy.amount == Decimal("30")
    assert buy.counterparty_asset == "EUR"
    assert buy.counterparty_amount == Decimal("590")
    assert buy.fee == Decimal("14.99")
    assert buy.fee_asset == "EUR"


def test_coinbase_sell_with_fee(tmp_path):
    rows = [
        _row(
            "2025-02-03T11:00:00+00:00", "Sell", "ETH", "0.5",
            subtotal="1200", total="1191.5", fee="8.5", txid="cb-sell-1",
        ),
    ]

    txns = normalize_coinbase(_write_coinbase_csv(rows, str(tmp_path)))

    assert len(txns) == 1
    sell = txns[0]
    assert sell.tx_type == "sell"
    assert sell.asset == "ETH"
    assert sell.amount == Decimal("0.5")
    assert sell.counterparty_asset == "EUR"
    assert sell.counterparty_amount == Decimal("1200")
    assert sell.fee == Decimal("8.5")
    assert sell.fee_asset == "EUR"


def test_coinbase_convert_parses_swap_pair(tmp_path):
    rows = [
        _row(
            "2021-06-01T12:00:00Z", "Convert", "ETH", "1.5",
            notes="Converted 0.1 BTC to 1.5 ETH", txid="cb-convert-1",
        ),
    ]

    txns = normalize_coinbase(_write_coinbase_csv(rows, str(tmp_path)))

    assert [t.tx_type for t in txns] == ["swap_out", "swap_in"]
