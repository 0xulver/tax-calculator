"""Fixed Binance normalizer.

Fixes vs original exchange_normalizer.py:
- Fix 5a: Buy/Spend pattern — aggregate all fills into ONE sell row with correct
  asset orientation (asset=crypto sold, counterparty=fiat received).
- Fix 5b: "Sell Crypto To Fiat" 1-second merge — merge groups within 2s window
  so paired rows (EUR +X at :55, ETH -Y at :56) become one sell event.
- Fix 5c: Sold/Revenue pattern — same aggregation fix as 5a.
"""
from __future__ import annotations

import csv
import os
import sys
from collections import defaultdict
from datetime import datetime, timedelta, timezone
from decimal import Decimal
from typing import Any

from tax_calc.constants import is_fiat, is_stablecoin
from tax_calc.models import Transaction
from tax_calc.normalizers.base import parse_decimal


def _parse_time(time_str: str) -> datetime:
    time_str = time_str.strip()
    if len(time_str.split("-")[0]) == 2:
        return datetime.strptime(time_str, "%y-%m-%d %H:%M:%S").replace(tzinfo=timezone.utc)
    return datetime.strptime(time_str, "%Y-%m-%d %H:%M:%S").replace(tzinfo=timezone.utc)


def _tx(dt: datetime, tx_type: str, asset: str, amount: Decimal,
        fee: Decimal = Decimal("0"), fee_asset: str = "",
        cp_asset: str = "", cp_amount: Decimal = Decimal("0"),
        notes: str = "") -> Transaction:
    return Transaction(
        date=dt.isoformat(), source="binance", source_tx_id="",
        tx_type=tx_type, asset=asset, amount=amount,
        fee=fee, fee_asset=fee_asset,
        counterparty_asset=cp_asset, counterparty_amount=cp_amount,
        notes=notes,
    )


def normalize_binance(binance_dir: str) -> list[Transaction]:
    csv_path = os.path.join(binance_dir, "binance_all_transactions_2020_2025.csv")
    if not os.path.exists(csv_path):
        print(f"Warning: {csv_path} not found", file=sys.stderr)
        return []

    rows: list[dict[str, Any]] = []
    with open(csv_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            rows.append(row)

    time_groups: dict[str, list[dict[str, Any]]] = defaultdict(list)
    standalone: list[Transaction] = []

    GROUPED_OPS = {
        "Transaction Buy", "Transaction Sold", "Transaction Fee",
        "Transaction Spend", "Transaction Revenue",
        "Binance Convert",
        "Sell Crypto To Fiat", "Buy Crypto With Card",
        "Buy Crypto With Fiat", "Transaction Related",
    }

    for row in rows:
        op = row.get("operation", "").strip()
        coin = row.get("coin", "").strip()
        change = parse_decimal(row.get("change", "0"))
        time_str = row.get("time", "").strip()
        remark = row.get("remark", "").strip()

        if not time_str or not coin:
            continue

        dt = _parse_time(time_str)

        if op == "Deposit":
            standalone.append(_tx(dt, "deposit", coin, change.copy_abs(),
                                  notes="Binance Deposit"))
        elif op == "Withdraw":
            note = "Binance Withdraw"
            if remark and remark != "Withdraw fee is included":
                note += f" ({remark})"
            standalone.append(_tx(dt, "withdrawal", coin, change.copy_abs(), notes=note))
        elif op == "Fiat Withdraw":
            standalone.append(_tx(dt, "fiat_withdrawal", coin, change.copy_abs(),
                                  notes="Binance Fiat Withdraw"))
        elif op == "Airdrop Assets":
            standalone.append(_tx(dt, "airdrop", coin, change.copy_abs(),
                                  notes="Binance Airdrop Assets"))
        elif op == "Simple Earn Flexible Interest":
            standalone.append(_tx(dt, "interest", coin, change.copy_abs(),
                                  notes="Binance Simple Earn Flexible Interest"))
        elif op == "Stablecoins Auto-Conversion":
            standalone.append(_tx(dt, "conversion", coin, change,
                                  notes="Binance Stablecoins Auto-Conversion"))
        elif op in ("Token Swap - Redenomination/Rebranding", "Token Swap - Distribution"):
            standalone.append(_tx(dt, "token_swap", coin, change, notes=f"Binance {op}"))
        elif op == "Asset Recovery":
            standalone.append(_tx(dt, "recovery", coin, change, notes="Binance Asset Recovery"))
        elif op == "Fiat OCBS - Add Fiat and Fees":
            standalone.append(_tx(dt, "fiat_deposit", coin, change,
                                  notes="Binance Fiat OCBS - Add Fiat and Fees"))
        elif op in GROUPED_OPS:
            time_groups[time_str].append({
                "op": op, "coin": coin, "change": change, "dt": dt, "remark": remark,
            })
        else:
            standalone.append(_tx(dt, "unknown", coin, change,
                                  notes=f"Binance unknown op: {op}"))

    # --- Fix 5b: merge "Sell Crypto To Fiat" groups within 2-second window ---
    time_groups = _merge_sell_crypto_to_fiat_groups(time_groups)

    # Reconstruct trades from time-grouped entries
    trades: list[Transaction] = []
    for time_str, entries in sorted(time_groups.items()):
        trades.extend(_process_group(entries))

    result = standalone + trades
    result.sort(key=lambda t: t.date)
    return result


def _merge_sell_crypto_to_fiat_groups(
    groups: dict[str, list[dict[str, Any]]],
) -> dict[str, list[dict[str, Any]]]:
    """Merge 'Sell Crypto To Fiat' groups that are within 2 seconds of each other.

    Binance sometimes splits paired Sell Crypto To Fiat rows (EUR credit at :55,
    ETH debit at :56) across 1-second-apart timestamps. This merges them so
    they're processed as one trade.
    """
    # Identify groups that contain ONLY "Sell Crypto To Fiat" entries
    sell_keys: list[tuple[datetime, str]] = []
    for ts, entries in groups.items():
        if all(e["op"] == "Sell Crypto To Fiat" for e in entries):
            sell_keys.append((entries[0]["dt"], ts))

    if len(sell_keys) < 2:
        return groups

    sell_keys.sort()
    merged_into: dict[str, str] = {}  # old_key -> merge_target_key

    for i in range(1, len(sell_keys)):
        prev_dt, prev_ts = sell_keys[i - 1]
        curr_dt, curr_ts = sell_keys[i]
        if abs((curr_dt - prev_dt).total_seconds()) <= 2:
            # Merge current into previous (or into whatever previous was merged into)
            target = merged_into.get(prev_ts, prev_ts)
            merged_into[curr_ts] = target

    if not merged_into:
        return groups

    new_groups = dict(groups)
    for src_ts, tgt_ts in merged_into.items():
        new_groups[tgt_ts] = new_groups.get(tgt_ts, []) + new_groups.pop(src_ts, [])

    return new_groups


def _process_group(entries: list[dict[str, Any]]) -> list[Transaction]:
    """Process a time-grouped set of Binance entries into transactions."""
    dt = entries[0]["dt"]

    buys = [e for e in entries if e["op"] in ("Transaction Buy", "Buy Crypto With Card", "Buy Crypto With Fiat")]
    sells = [e for e in entries if e["op"] == "Transaction Sold"]
    fees = [e for e in entries if e["op"] == "Transaction Fee"]
    spends = [e for e in entries if e["op"] == "Transaction Spend"]
    revenues = [e for e in entries if e["op"] == "Transaction Revenue"]
    converts = [e for e in entries if e["op"] == "Binance Convert"]
    related = [e for e in entries if e["op"] == "Transaction Related"]
    sell_fiat = [e for e in entries if e["op"] == "Sell Crypto To Fiat"]

    # Aggregate fee
    total_fee = sum((e["change"].copy_abs() for e in fees), Decimal("0"))
    fee_asset = fees[0]["coin"] if fees else ""

    result: list[Transaction] = []

    if converts:
        return _process_converts(dt, converts)

    if sell_fiat:
        return _process_sell_crypto_to_fiat(dt, sell_fiat)

    # --- Fix 5a: Transaction Buy/Spend pattern ---
    if buys and (spends or revenues or sells):
        return _process_buy_spend(dt, buys, spends, total_fee, fee_asset)

    # --- Fix 5c: Transaction Sold/Revenue pattern ---
    if sells and (revenues or spends):
        return _process_sold_revenue(dt, sells, revenues, total_fee, fee_asset)

    if buys and not spends and not revenues and not sells:
        for buy in buys:
            result.append(_tx(dt, "buy", buy["coin"], buy["change"].copy_abs(),
                              fee=total_fee, fee_asset=fee_asset,
                              notes=f"Binance {buy['op']}"))
            total_fee = Decimal("0")
        return result

    if related:
        for r in related:
            result.append(_tx(dt, "adjustment", r["coin"], r["change"],
                              notes="Binance Transaction Related"))
        return result

    # Fallback
    for e in entries:
        if e["op"] == "Transaction Fee":
            result.append(_tx(dt, "fee", e["coin"], e["change"].copy_abs(),
                              notes="Binance Fee (orphaned)"))
        else:
            result.append(_tx(dt, "unknown", e["coin"], e["change"],
                              notes=f"Binance ungrouped: {e['op']}"))
    return result


def _process_converts(dt: datetime, converts: list[dict[str, Any]]) -> list[Transaction]:
    result: list[Transaction] = []
    pos = [c for c in converts if c["change"] > 0]
    neg = [c for c in converts if c["change"] < 0]

    if len(pos) == 1 and len(neg) == 1:
        got = pos[0]
        gave = neg[0]
        got_is_fiat = is_fiat(got["coin"])
        gave_is_fiat = is_fiat(gave["coin"])

        if got_is_fiat and not gave_is_fiat:
            # Sold crypto/stablecoin for fiat
            result.append(_tx(dt, "sell", gave["coin"], gave["change"].copy_abs(),
                              cp_asset=got["coin"], cp_amount=got["change"].copy_abs(),
                              notes="Binance Convert"))
        elif not got_is_fiat and gave_is_fiat:
            # Bought crypto with fiat
            result.append(_tx(dt, "buy", got["coin"], got["change"].copy_abs(),
                              cp_asset=gave["coin"], cp_amount=gave["change"].copy_abs(),
                              notes="Binance Convert"))
        else:
            # Crypto-to-crypto or stablecoin-to-stablecoin
            result.append(_tx(dt, "swap_out", gave["coin"], gave["change"].copy_abs(),
                              cp_asset=got["coin"], cp_amount=got["change"].copy_abs(),
                              notes="Binance Convert"))
            result.append(_tx(dt, "swap_in", got["coin"], got["change"].copy_abs(),
                              cp_asset=gave["coin"], cp_amount=gave["change"].copy_abs(),
                              notes="Binance Convert"))
    else:
        for conv in converts:
            if conv["change"] > 0:
                result.append(_tx(dt, "swap_in", conv["coin"], conv["change"],
                                  notes="Binance Convert"))
            else:
                result.append(_tx(dt, "swap_out", conv["coin"], conv["change"].copy_abs(),
                                  notes="Binance Convert"))
    return result


def _process_sell_crypto_to_fiat(
    dt: datetime, entries: list[dict[str, Any]]
) -> list[Transaction]:
    """Process 'Sell Crypto To Fiat' entries (after 2-second merge).

    Positive change = fiat received. Negative change = crypto sold.
    """
    fiat_entries = [e for e in entries if e["change"] > 0 and is_fiat(e["coin"])]
    crypto_entries = [e for e in entries if e["change"] < 0 and not is_fiat(e["coin"])]

    result: list[Transaction] = []

    if fiat_entries and crypto_entries:
        # Normal paired case: aggregate
        total_fiat = sum((e["change"].copy_abs() for e in fiat_entries), Decimal("0"))
        fiat_asset = fiat_entries[0]["coin"]

        # Group crypto by asset
        crypto_by_asset: dict[str, Decimal] = defaultdict(Decimal)
        for e in crypto_entries:
            crypto_by_asset[e["coin"]] += e["change"].copy_abs()

        for crypto_asset, crypto_amount in crypto_by_asset.items():
            result.append(_tx(dt, "sell", crypto_asset, crypto_amount,
                              cp_asset=fiat_asset, cp_amount=total_fiat,
                              notes="Binance Sell Crypto To Fiat"))
        return result

    # Edge case: lone crypto debit with no fiat pair (e.g., Paymonade)
    for e in entries:
        if e["change"] < 0 and not is_fiat(e["coin"]):
            result.append(_tx(dt, "sell", e["coin"], e["change"].copy_abs(),
                              notes=f"Binance Sell Crypto To Fiat (unpaired, {e['remark']})"))
        elif e["change"] > 0 and is_fiat(e["coin"]):
            # Lone fiat credit — shouldn't happen, but handle gracefully
            result.append(_tx(dt, "fiat_deposit", e["coin"], e["change"],
                              notes="Binance Sell Crypto To Fiat (lone fiat credit)"))
        else:
            result.append(_tx(dt, "unknown", e["coin"], e["change"],
                              notes=f"Binance Sell Crypto To Fiat ungrouped: {e['remark']}"))

    return result


def _process_buy_spend(
    dt: datetime,
    buys: list[dict[str, Any]],
    spends: list[dict[str, Any]],
    total_fee: Decimal,
    fee_asset: str,
) -> list[Transaction]:
    """Fix 5a: Aggregate Buy/Spend into correct sell rows.

    When all buys are fiat (EUR) and all spends are crypto (USDC), this is
    actually a SELL of crypto for fiat. Aggregate into ONE row with:
      asset = crypto, counterparty = fiat
    """
    buy_coins = {b["coin"] for b in buys}
    spend_coins = {s["coin"] for s in spends}

    all_buys_fiat = all(is_fiat(c) for c in buy_coins)
    all_spends_crypto = all(not is_fiat(c) for c in spend_coins)
    all_buys_crypto = all(not is_fiat(c) for c in buy_coins)
    all_spends_fiat = all(is_fiat(c) for c in spend_coins)

    if all_buys_fiat and all_spends_crypto:
        # SELL crypto for fiat — aggregate into one row per crypto asset
        total_fiat = sum((b["change"].copy_abs() for b in buys), Decimal("0"))
        fiat_asset = buys[0]["coin"]

        crypto_totals: dict[str, Decimal] = defaultdict(Decimal)
        for sp in spends:
            crypto_totals[sp["coin"]] += sp["change"].copy_abs()

        result: list[Transaction] = []
        for crypto_asset, crypto_amount in crypto_totals.items():
            result.append(_tx(dt, "sell", crypto_asset, crypto_amount,
                              fee=total_fee, fee_asset=fee_asset,
                              cp_asset=fiat_asset, cp_amount=total_fiat,
                              notes="Binance Trade"))
            total_fee = Decimal("0")  # fee only on first
        return result

    if all_buys_crypto and (all_spends_fiat or not spend_coins):
        # BUY crypto with fiat — aggregate
        total_crypto: dict[str, Decimal] = defaultdict(Decimal)
        for b in buys:
            total_crypto[b["coin"]] += b["change"].copy_abs()

        total_spent = sum((s["change"].copy_abs() for s in spends), Decimal("0"))
        spent_asset = spends[0]["coin"] if spends else ""

        result = []
        for crypto_asset, crypto_amount in total_crypto.items():
            result.append(_tx(dt, "buy", crypto_asset, crypto_amount,
                              fee=total_fee, fee_asset=fee_asset,
                              cp_asset=spent_asset, cp_amount=total_spent,
                              notes="Binance Trade"))
            total_fee = Decimal("0")
        return result

    # Crypto-to-crypto swap
    total_got: dict[str, Decimal] = defaultdict(Decimal)
    for b in buys:
        total_got[b["coin"]] += b["change"].copy_abs()
    total_gave: dict[str, Decimal] = defaultdict(Decimal)
    for s in spends:
        total_gave[s["coin"]] += s["change"].copy_abs()

    result = []
    for asset, amount in total_gave.items():
        got_asset = next(iter(total_got))
        got_amount = next(iter(total_got.values()))
        result.append(_tx(dt, "swap_out", asset, amount,
                          fee=total_fee, fee_asset=fee_asset,
                          cp_asset=got_asset, cp_amount=got_amount,
                          notes="Binance Trade"))
        total_fee = Decimal("0")
    for asset, amount in total_got.items():
        gave_asset = next(iter(total_gave))
        gave_amount = next(iter(total_gave.values()))
        result.append(_tx(dt, "swap_in", asset, amount,
                          cp_asset=gave_asset, cp_amount=gave_amount,
                          notes="Binance Trade"))
    return result


def _process_sold_revenue(
    dt: datetime,
    sells: list[dict[str, Any]],
    revenues: list[dict[str, Any]],
    total_fee: Decimal,
    fee_asset: str,
) -> list[Transaction]:
    """Fix 5c: Aggregate Sold/Revenue into correct sell rows.

    Same fix as 5a — aggregate all sells and all revenues into one row per asset.
    """
    sell_coins = {s["coin"] for s in sells}
    rev_coins = {r["coin"] for r in revenues}

    all_sells_crypto = all(not is_fiat(c) for c in sell_coins)
    all_revs_fiat_or_stable = all(
        is_fiat(c) or is_stablecoin(c) for c in rev_coins
    ) if rev_coins else False

    # Aggregate
    total_sold: dict[str, Decimal] = defaultdict(Decimal)
    for s in sells:
        total_sold[s["coin"]] += s["change"].copy_abs()

    total_rev = sum((r["change"].copy_abs() for r in revenues), Decimal("0"))
    rev_asset = revenues[0]["coin"] if revenues else ""

    result: list[Transaction] = []

    all_revs_fiat = all(is_fiat(c) for c in rev_coins) if rev_coins else False

    if all_sells_crypto and (all_revs_fiat_or_stable or not rev_coins):
        for crypto_asset, crypto_amount in total_sold.items():
            if all_revs_fiat:
                # Crypto sold for fiat (EUR) -> taxable sell
                tx_type = "sell"
            else:
                # Crypto sold for stablecoin (USDC) -> crypto-to-crypto swap
                tx_type = "swap_out"
            result.append(_tx(dt, tx_type, crypto_asset, crypto_amount,
                              fee=total_fee, fee_asset=fee_asset,
                              cp_asset=rev_asset, cp_amount=total_rev,
                              notes="Binance Trade"))
            total_fee = Decimal("0")
        # For stablecoin revenue, also emit swap_in
        if not all_revs_fiat and rev_asset:
            result.append(_tx(dt, "swap_in", rev_asset, total_rev,
                              cp_asset=next(iter(total_sold)),
                              cp_amount=sum(total_sold.values()),
                              notes="Binance Trade"))
    else:
        # Fiat sold for crypto or other edge cases
        for s in sells:
            if is_fiat(s["coin"]):
                result.append(_tx(dt, "buy", rev_asset, total_rev,
                                  fee=total_fee, fee_asset=fee_asset,
                                  cp_asset=s["coin"], cp_amount=s["change"].copy_abs(),
                                  notes="Binance Trade"))
            else:
                result.append(_tx(dt, "sell", s["coin"], s["change"].copy_abs(),
                                  fee=total_fee, fee_asset=fee_asset,
                                  cp_asset=rev_asset, cp_amount=total_rev,
                                  notes="Binance Trade"))
            total_fee = Decimal("0")

    return result
