"""Tests for the FTX normalizer."""
import csv
import os
from decimal import Decimal

from tax_calc.normalizers.ftx import normalize_ftx


def _write_ftx_csv(rows, tmpdir, filename="ftx.csv"):
    path = os.path.join(tmpdir, filename)
    fieldnames = ["Time", "Coin", "Quantity", "Description"]
    with open(path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)
    return tmpdir


def _row(time, coin, qty, desc):
    return {
        "Time": time,
        "Coin": coin,
        "Quantity": str(qty),
        "Description": desc,
    }


def test_ftx_buy_after_fiat_conversion(tmp_path):
    rows = [
        _row("2021-05-14 02:27:35.870651", "EUR", "860.84", "fiat_deposit 68957"),
        _row("2021-05-14 07:20:35.997919", "EUR", "-860.84", "spot_base"),
        _row("2021-05-14 07:20:35.997919", "USD", "1036.88349307", "spot_quote"),
        _row("2021-05-14 15:36:59.475463", "CEL", "9.4", "spot_base"),
        _row("2021-05-14 15:36:59.475463", "CEL", "20.6", "spot_base"),
        _row("2021-05-14 15:36:59.475463", "USD", "-69.5365", "spot_quote"),
        _row("2021-05-14 15:36:59.475463", "USD", "-152.44", "spot_quote"),
        _row("2021-05-14 15:36:59.475463", "CEL", "-0.00658", "spot_fee"),
        _row("2021-05-14 15:36:59.475463", "CEL", "-0.01442", "spot_fee"),
    ]

    txns = normalize_ftx(_write_ftx_csv(rows, str(tmp_path)))

    fiat = [t for t in txns if t.tx_type == "fiat_exchange"]
    assert len(fiat) == 1
    assert fiat[0].asset == "EUR"
    assert fiat[0].counterparty_asset == "USD"
    assert fiat[0].counterparty_amount == Decimal("1036.88349307")

    buys = [t for t in txns if t.tx_type == "buy"]
    assert len(buys) == 1
    buy = buys[0]
    assert buy.asset == "CEL"
    assert buy.amount == Decimal("30.0")
    assert buy.counterparty_asset == "USD"
    assert buy.counterparty_amount == Decimal("221.9765")
    assert buy.fee == Decimal("0.02100")
    assert buy.fee_asset == "CEL"


def test_ftx_sell_and_stablecoin_deposit(tmp_path):
    rows = [
        _row("2021-08-26 07:53:59.249210", "USDT", "2577.637285", "deposit 7277160"),
        _row("2021-09-03 11:38:27.920604", "CEL", "-20", "spot_base"),
        _row("2021-09-03 11:38:27.920604", "CEL", "-0.2", "spot_base"),
        _row("2021-09-03 11:38:27.920604", "USD", "125.01", "spot_quote"),
        _row("2021-09-03 11:38:27.920604", "USD", "1.25", "spot_quote"),
        _row("2021-09-03 11:38:27.920604", "USD", "-0.087507", "spot_fee"),
        _row("2021-09-03 11:38:27.920604", "USD", "-0.000875", "spot_fee"),
    ]

    txns = normalize_ftx(_write_ftx_csv(rows, str(tmp_path)))

    deposits = [t for t in txns if t.tx_type == "deposit"]
    assert len(deposits) == 1
    assert deposits[0].asset == "USDT"
    assert deposits[0].amount == Decimal("2577.637285")

    sells = [t for t in txns if t.tx_type == "sell"]
    assert len(sells) == 1
    sell = sells[0]
    assert sell.asset == "CEL"
    assert sell.amount == Decimal("20.2")
    assert sell.counterparty_asset == "USD"
    assert sell.counterparty_amount == Decimal("126.26")
    assert sell.fee == Decimal("0.088382")
    assert sell.fee_asset == "USD"


def test_ftx_circle_deposit_fee_and_withdrawal(tmp_path):
    rows = [
        _row("2021-05-11 14:08:04.344445", "USD", "3088.88", "Circle deposit"),
        _row("2021-05-11 14:08:04.344445", "USD", "-89.88", "Circle deposit fee"),
        _row("2021-05-31 07:03:25.977117", "BTC", "-0.001", "withdrawal 3409111"),
        _row("2021-08-28 13:00:40.587613", "USD", "-2995", "withdrawal 4894040"),
    ]

    txns = normalize_ftx(_write_ftx_csv(rows, str(tmp_path)))

    assert [t.tx_type for t in txns] == ["fiat_deposit", "fee", "withdrawal", "fiat_withdrawal"]
    assert txns[1].amount == Decimal("89.88")
    assert txns[2].asset == "BTC"
    assert txns[3].asset == "USD"
