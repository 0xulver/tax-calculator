"""Kraken normalizer — ported from exchange_normalizer.py with no logic changes."""
from __future__ import annotations

import csv
import os
import sys
from collections import defaultdict
from datetime import datetime, timezone
from decimal import Decimal
from typing import Any

from tax_calc.constants import KRAKEN_ASSET_MAP, is_fiat
from tax_calc.models import Transaction
from tax_calc.normalizers.base import parse_decimal


def _normalize_asset(raw: str) -> str:
    raw = raw.strip()
    return KRAKEN_ASSET_MAP.get(raw, raw)


def _parse_time(time_str: str) -> datetime:
    return datetime.strptime(time_str.strip(), "%Y-%m-%d %H:%M:%S").replace(tzinfo=timezone.utc)


def _tx(dt: datetime, tx_type: str, asset: str, amount: Decimal,
        fee: Decimal = Decimal("0"), fee_asset: str = "",
        cp_asset: str = "", cp_amount: Decimal = Decimal("0"),
        notes: str = "", txid: str = "") -> Transaction:
    return Transaction(
        date=dt.isoformat(), source="kraken", source_tx_id=txid,
        tx_type=tx_type, asset=asset, amount=amount,
        fee=fee, fee_asset=fee_asset,
        counterparty_asset=cp_asset, counterparty_amount=cp_amount,
        notes=notes,
    )


def normalize_kraken(kraken_dir: str) -> list[Transaction]:
    all_entries: list[dict[str, Any]] = []

    for fname in sorted(os.listdir(kraken_dir)):
        if not fname.endswith(".csv"):
            continue
        path = os.path.join(kraken_dir, fname)
        with open(path, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                all_entries.append(row)

    # Deduplicate by txid
    seen: set[str] = set()
    unique: list[dict[str, Any]] = []
    for entry in all_entries:
        txid = entry.get("txid", "").strip()
        if txid and txid in seen:
            continue
        if txid:
            seen.add(txid)
        unique.append(entry)

    refid_groups: dict[str, list[dict[str, Any]]] = defaultdict(list)
    standalone: list[Transaction] = []

    for entry in unique:
        tx_type = entry.get("type", "").strip()
        subtype = entry.get("subtype", "").strip()
        subclass = entry.get("subclass", "").strip()
        asset_raw = entry.get("asset", "").strip()
        asset = _normalize_asset(asset_raw)
        amount = parse_decimal(entry.get("amount", "0"))
        fee = parse_decimal(entry.get("fee", "0"))
        time_str = entry.get("time", "").strip()
        txid = entry.get("txid", "").strip()
        refid = entry.get("refid", "").strip()

        if not time_str:
            continue

        dt = _parse_time(time_str)

        if tx_type == "trade":
            refid_groups[refid].append({
                "dt": dt, "asset": asset, "asset_raw": asset_raw,
                "amount": amount, "fee": fee, "txid": txid,
                "subclass": subclass, "subtype": subtype,
            })
        elif tx_type == "deposit":
            standalone.append(_tx(dt, "deposit", asset, amount.copy_abs(),
                                  fee=fee.copy_abs(), fee_asset=asset if fee else "",
                                  notes=f"Kraken deposit ({subclass})", txid=txid))
        elif tx_type == "withdrawal":
            wtype = "withdrawal" if subclass == "crypto" else "fiat_withdrawal"
            standalone.append(_tx(dt, wtype, asset, amount.copy_abs(),
                                  fee=fee.copy_abs(), fee_asset=asset if fee else "",
                                  notes=f"Kraken withdrawal ({subclass})", txid=txid))
        elif tx_type == "staking":
            note = f"Kraken staking ({subclass})"
            if asset_raw != asset:
                note += f" raw_asset={asset_raw}"
            standalone.append(_tx(dt, "staking_reward", asset, amount.copy_abs(),
                                  notes=note, txid=txid))
        elif tx_type == "earn":
            if subtype == "reward":
                standalone.append(_tx(dt, "earn_reward", asset, amount.copy_abs(),
                                      notes=f"Kraken earn reward ({subclass})", txid=txid))
            elif subtype in ("autoallocation", "deallocation", "migration"):
                standalone.append(_tx(dt, "earn_allocation", asset, amount,
                                      notes=f"Kraken earn {subtype} ({subclass})", txid=txid))
            else:
                standalone.append(_tx(dt, "earn_other", asset, amount,
                                      notes=f"Kraken earn {subtype} ({subclass})", txid=txid))
        elif tx_type == "transfer":
            standalone.append(_tx(dt, "internal_transfer", asset, amount,
                                  notes=f"Kraken transfer {subtype} ({subclass})", txid=txid))
        elif tx_type in ("receive", "spend"):
            refid_groups[refid].append({
                "dt": dt, "asset": asset, "asset_raw": asset_raw,
                "amount": amount, "fee": fee, "txid": txid,
                "subclass": subclass, "subtype": subtype,
                "original_type": tx_type,
            })
        else:
            standalone.append(_tx(dt, "unknown", asset, amount,
                                  notes=f"Kraken unknown type: {tx_type}/{subtype}/{subclass}",
                                  txid=txid))

    # Reconstruct trades from refid groups
    trades: list[Transaction] = []
    for refid, legs in sorted(refid_groups.items(), key=lambda x: x[1][0]["dt"]):
        if len(legs) < 2:
            for leg in legs:
                trades.append(_tx(leg["dt"], "unknown_trade_leg", leg["asset"], leg["amount"],
                                  notes=f"Kraken orphaned trade leg refid={refid}",
                                  txid=leg["txid"]))
            continue

        dt = legs[0]["dt"]
        gave_legs = [l for l in legs if l["amount"] < 0]
        got_legs = [l for l in legs if l["amount"] > 0]

        if not gave_legs or not got_legs:
            for leg in legs:
                trades.append(_tx(leg["dt"], "unknown_trade_leg", leg["asset"], leg["amount"],
                                  notes=f"Kraken ambiguous trade refid={refid}",
                                  txid=leg["txid"]))
            continue

        gave = gave_legs[0]
        got = got_legs[0]

        total_fee = sum(l["fee"].copy_abs() for l in legs if l["fee"])
        fee_asset = gave["asset"] if gave["fee"] else (got["asset"] if got["fee"] else "")

        gave_is_fiat = is_fiat(gave["asset"])
        got_is_fiat = is_fiat(got["asset"])

        if gave_is_fiat and not got_is_fiat:
            trades.append(_tx(dt, "buy", got["asset"], got["amount"].copy_abs(),
                              fee=total_fee, fee_asset=fee_asset,
                              cp_asset=gave["asset"], cp_amount=gave["amount"].copy_abs(),
                              notes="Kraken Trade", txid=got["txid"]))
        elif not gave_is_fiat and got_is_fiat:
            trades.append(_tx(dt, "sell", gave["asset"], gave["amount"].copy_abs(),
                              fee=total_fee, fee_asset=fee_asset,
                              cp_asset=got["asset"], cp_amount=got["amount"].copy_abs(),
                              notes="Kraken Trade", txid=gave["txid"]))
        elif not gave_is_fiat and not got_is_fiat:
            trades.append(_tx(dt, "swap_out", gave["asset"], gave["amount"].copy_abs(),
                              fee=total_fee, fee_asset=fee_asset,
                              cp_asset=got["asset"], cp_amount=got["amount"].copy_abs(),
                              notes="Kraken Crypto-to-Crypto Trade", txid=gave["txid"]))
            trades.append(_tx(dt, "swap_in", got["asset"], got["amount"].copy_abs(),
                              cp_asset=gave["asset"], cp_amount=gave["amount"].copy_abs(),
                              notes="Kraken Crypto-to-Crypto Trade", txid=got["txid"]))
        else:
            trades.append(_tx(dt, "fiat_exchange", gave["asset"], gave["amount"],
                              cp_asset=got["asset"], cp_amount=got["amount"],
                              notes="Kraken Fiat Exchange", txid=gave["txid"]))

    result = standalone + trades
    result.sort(key=lambda t: t.date)
    return result
