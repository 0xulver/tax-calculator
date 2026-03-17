#!/usr/bin/env python3
"""
crypto_wallet_tracker.py
Track crypto wallets and generate tax-year transaction reports.

Usage examples:
  python3 crypto_wallet_tracker.py --wallets-file wallets.txt --config config.json --year 2025
  python3 crypto_wallet_tracker.py --wallets-file wallets.txt --config config.json --discover-only
  python3 crypto_wallet_tracker.py --wallets-file wallets.txt --config config.json --year 2025 --full-history
"""

from __future__ import annotations

import argparse
import csv
import datetime as dt
import json
import os
import re
import sys
import time
import urllib.parse
import urllib.request
from collections import defaultdict
from decimal import Decimal, getcontext
from typing import Any, Dict, Iterable, List, Optional, Tuple

getcontext().prec = 36


BASE58_ALPHABET = set("123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz")
CSV_COLUMNS = [
    "wallet_label",
    "wallet_address",
    "chain",
    "chain_family",
    "tx_hash",
    "tx_type",
    "direction",
    "asset_symbol",
    "amount",
    "amount_raw",
    "counterparty",
    "status",
    "tx_time_utc",
    "year",
    "month",
    "notes",
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Track wallet activity and export tax-year CSV files."
    )
    parser.add_argument(
        "--wallets-file",
        default="wallets.txt",
        help="Path to wallet list (label + address per line).",
    )
    parser.add_argument(
        "--config",
        default="config.json",
        help="Path to chain config JSON.",
    )
    parser.add_argument(
        "--output-dir",
        default="outputs",
        help="Directory for generated CSV files.",
    )
    parser.add_argument("--year", type=int, default=None, help="Tax year for report files.")
    parser.add_argument(
        "--from-date",
        default=None,
        help="Override report start date (YYYY-MM-DD).",
    )
    parser.add_argument(
        "--to-date",
        default=None,
        help="Override report end date (YYYY-MM-DD).",
    )
    parser.add_argument(
        "--discover-only",
        action="store_true",
        help="Only discover active wallet+chain combinations; do not fetch all tx records.",
    )
    parser.add_argument(
        "--full-history",
        action="store_true",
        help="Fetch all configured history (from config history_start) instead of report period only.",
    )
    parser.add_argument(
        "--wallet-filter",
        action="append",
        default=[],
        help="Optional wallet label filter; may be passed multiple times.",
    )
    parser.add_argument(
        "--chain-filter",
        action="append",
        default=[],
        help="Optional chain name filter; may be passed multiple times.",
    )
    return parser.parse_args()


def read_json(path: str) -> Dict[str, Any]:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def parse_utc_date(value: str) -> dt.datetime:
    return dt.datetime.strptime(value, "%Y-%m-%d").replace(tzinfo=dt.timezone.utc)


def dt_utc_now() -> dt.datetime:
    return dt.datetime.now(tz=dt.timezone.utc)


def to_datetime(ts: int) -> dt.datetime:
    return dt.datetime.fromtimestamp(ts, tz=dt.timezone.utc)


def format_decimal(value: Any) -> str:
    d = Decimal(str(value))
    return str(d.normalize())


def to_bool(value: str) -> bool:
    return str(value).lower() in {"1", "true", "yes", "y"}


def normalize_line(s: str) -> str:
    return " ".join(s.strip().split())


def is_hex_address(value: str) -> bool:
    return value.startswith("0x") and all(c in "0123456789abcdefABCDEF" for c in value[2:])


def is_solana_address(value: str) -> bool:
    if not value or value.startswith("0x"):
        return False
    if not (32 <= len(value) <= 44):
        return False
    return all(c in BASE58_ALPHABET for c in value)


def infer_family(address: str) -> str:
    if is_solana_address(address):
        return "solana"
    if is_hex_address(address):
        if len(address) == 42:
            return "evm"
        if len(address) == 66:
            return "sui"
        return "unknown_hex"
    return "unknown"


def read_wallets(path: str, label_filter: Iterable[str]) -> List[Dict[str, str]]:
    wallets: List[Dict[str, str]] = []
    wanted = {x.lower() for x in label_filter}

    with open(path, "r", encoding="utf-8") as f:
        for raw in f:
            line = normalize_line(raw)
            if not line or line.startswith("#"):
                continue
            if " " not in line:
                continue
            label, address = line.rsplit(" ", 1)
            if not is_hex_address(address) and not is_solana_address(address):
                continue
            if wanted and label.lower() not in wanted:
                continue
            wallets.append(
                {
                    "label": label,
                    "address": address,
                    "family": infer_family(address),
                }
            )

    return wallets


def http_get_json(url: str, timeout: int = 40) -> Dict[str, Any]:
    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": "crypto-wallet-tracker/1.0",
            "Accept": "application/json",
        },
    )
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return json.loads(resp.read().decode("utf-8"))


def http_post_json(url: str, payload: Dict[str, Any], timeout: int = 40) -> Dict[str, Any]:
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=data,
        headers={"User-Agent": "crypto-wallet-tracker/1.0", "Content-Type": "application/json"},
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return json.loads(resp.read().decode("utf-8"))


def chain_is_compatible(chain_cfg: Dict[str, Any], wallet_family: str) -> bool:
    return chain_cfg.get("family") in {"all", wallet_family}


def in_date_range(ts: int, start: dt.datetime, end: dt.datetime) -> bool:
    dtobj = to_datetime(ts)
    return start <= dtobj <= end


def build_record(
    wallet: Dict[str, str],
    chain_name: str,
    chain_family: str,
    tx_hash: str,
    tx_type: str,
    direction: str,
    asset_symbol: str,
    amount: Decimal,
    amount_raw: Any,
    counterparty: str,
    status: str,
    tx_time: dt.datetime,
    notes: str = "",
) -> Dict[str, str]:
    return {
        "wallet_label": wallet["label"],
        "wallet_address": wallet["address"],
        "chain": chain_name,
        "chain_family": chain_family,
        "tx_hash": tx_hash,
        "tx_type": tx_type,
        "direction": direction,
        "asset_symbol": asset_symbol,
        "amount": format_decimal(amount),
        "amount_raw": str(amount_raw),
        "counterparty": counterparty or "",
        "status": status,
        "tx_time_utc": tx_time.astimezone(dt.timezone.utc).isoformat(),
        "year": str(tx_time.year),
        "month": f"{tx_time.month:02d}",
        "notes": notes or "",
    }


def parse_hex_amount(raw: str, decimals: int) -> Decimal:
    try:
        return Decimal(str(int(raw))) / (Decimal(10) ** decimals)
    except Exception:
        return Decimal("0")


def fetch_evm_transactions(
    wallet: Dict[str, str],
    chain_cfg: Dict[str, Any],
    fetch_start: dt.datetime,
    fetch_end: dt.datetime,
    full_history: bool,
    request_delay: float,
) -> Tuple[bool, List[Dict[str, str]], str]:
    api_url = chain_cfg.get("api_url") or chain_cfg.get("base_url")
    chainid = str(chain_cfg.get("chainid", "")).strip()
    api_key = os.getenv(chain_cfg.get("api_key_env", ""), "")
    native_symbol = chain_cfg.get("native_symbol", "ETH")
    native_decimals = int(chain_cfg.get("native_decimals", 18))
    records: List[Dict[str, str]] = []
    discovered = False
    last_error = ""
    page = 1
    page_size = 1000

    def call(action: str, page_num: int) -> List[Dict[str, Any]]:
        params = {
            "module": "account",
            "action": action,
            "address": wallet["address"],
            "startblock": 0,
            "endblock": 99999999,
            "page": page_num,
            "offset": page_size,
            "sort": "desc",
        }
        if chainid:
            params["chainid"] = chainid
        if api_key:
            params["apikey"] = api_key
        q = urllib.parse.urlencode(params)
        payload = http_get_json(f"{api_url}?{q}")
        if not isinstance(payload, dict):
            raise RuntimeError(f"Bad response for {action}: {payload!r}")
        status = str(payload.get("status", ""))
        result = payload.get("result")
        if status != "1" and result not in (None, [], "No transactions found"):
            # Example "status":"0" with API errors
            message = result or payload.get("message", "unknown")
            raise RuntimeError(f"Etherscan API error ({action}): {message}")
        if isinstance(result, list):
            return result
        return []

    try:
        # txlist / normal coin transfers
        page = 1
        while True:
            tx_list = call("txlist", page)
            if tx_list:
                discovered = True
            if not tx_list:
                break
            parsed_any = False
            for tx in tx_list:
                if not isinstance(tx, dict):
                    continue
                ts = int(tx.get("timeStamp", "0") or 0)
                if ts == 0:
                    continue
                if not full_history and ts > int(fetch_end.timestamp()):
                    continue
                if not in_date_range(ts, fetch_start, fetch_end):
                    if not full_history and ts < int(fetch_start.timestamp()):
                        # descending order; older than requested => stop this action
                        break
                    if not full_history:
                        continue
                direction = "in"
                frm = (tx.get("from") or "").lower()
                to = (tx.get("to") or "").lower()
                wallet_addr = wallet["address"].lower()
                if frm == wallet_addr and to == wallet_addr:
                    direction = "self"
                elif frm == wallet_addr:
                    direction = "out"
                elif to == wallet_addr:
                    direction = "in"
                else:
                    direction = "unknown"
                amount = parse_hex_amount(str(tx.get("value", "0")), native_decimals)
                if amount == 0:
                    continue
                records.append(
                    build_record(
                        wallet=wallet,
                        chain_name=chain_cfg["name"],
                        chain_family=chain_cfg.get("family", "evm"),
                        tx_hash=tx.get("hash", ""),
                        tx_type="native_transfer",
                        direction=direction,
                        asset_symbol=native_symbol,
                        amount=amount,
                        amount_raw=tx.get("value", "0"),
                        counterparty=(to if direction == "out" else frm) if direction != "self" else "",
                        status=str(tx.get("txreceipt_status", "1")),
                        tx_time=to_datetime(ts),
                        notes=tx.get("functionName", "") or tx.get("methodId", ""),
                    )
                )
                parsed_any = True
            time.sleep(request_delay)
            if parsed_any and len(tx_list) < page_size:
                break
            if not tx_list:
                break
            if not full_history and page > 50:
                break
            if not full_history and any(
                int(tx.get("timeStamp", "0") or 0) < int(fetch_start.timestamp()) for tx in tx_list
            ):
                break
            page += 1

        # token transfers
        page = 1
        while True:
            tx_list = call("tokentx", page)
            if tx_list:
                discovered = True
            if not tx_list:
                break
            parsed_any = False
            for tx in tx_list:
                if not isinstance(tx, dict):
                    continue
                ts = int(tx.get("timeStamp", "0") or 0)
                if ts == 0:
                    continue
                if not full_history and ts > int(fetch_end.timestamp()):
                    continue
                if not in_date_range(ts, fetch_start, fetch_end):
                    if not full_history and ts < int(fetch_start.timestamp()):
                        break
                    if not full_history:
                        continue

                frm = (tx.get("from") or "").lower()
                to = (tx.get("to") or "").lower()
                wallet_addr = wallet["address"].lower()
                if frm == wallet_addr and to == wallet_addr:
                    direction = "self"
                elif frm == wallet_addr:
                    direction = "out"
                elif to == wallet_addr:
                    direction = "in"
                else:
                    direction = "unknown"
                decimals = int(tx.get("tokenDecimal", "18") or 18)
                amount = parse_hex_amount(tx.get("value", "0"), decimals)
                symbol = tx.get("tokenSymbol", "UNKNOWN")
                if amount == 0:
                    continue
                records.append(
                    build_record(
                        wallet=wallet,
                        chain_name=chain_cfg["name"],
                        chain_family=chain_cfg.get("family", "evm"),
                        tx_hash=tx.get("hash", ""),
                        tx_type="token_transfer",
                        direction=direction,
                        asset_symbol=symbol,
                        amount=amount,
                        amount_raw=tx.get("value", "0"),
                        counterparty=(to if direction == "out" else frm) if direction != "self" else "",
                        status=str(tx.get("txreceipt_status", "1")),
                        tx_time=to_datetime(ts),
                        notes=tx.get("tokenName", ""),
                    )
                )
                parsed_any = True
            time.sleep(request_delay)
            if parsed_any and len(tx_list) < page_size:
                break
            if not tx_list:
                break
            if not full_history and page > 50:
                break
            if not full_history and any(
                int(tx.get("timeStamp", "0") or 0) < int(fetch_start.timestamp()) for tx in tx_list
            ):
                break
            page += 1
    except Exception as exc:
        last_error = str(exc)

    return discovered, records, last_error


def fetch_solana_transactions(
    wallet: Dict[str, str],
    chain_cfg: Dict[str, Any],
    fetch_start: dt.datetime,
    fetch_end: dt.datetime,
    full_history: bool,
    request_delay: float,
) -> Tuple[bool, List[Dict[str, str]], str]:
    rpc_url = chain_cfg["rpc_url"]
    native_symbol = chain_cfg.get("native_symbol", "SOL")
    native_decimals = int(chain_cfg.get("native_decimals", 9))
    records: List[Dict[str, str]] = []
    discovered = False
    last_error = ""

    try:
        before = None
        while True:
            params = {
                "limit": 1000,
            }
            if before:
                params["before"] = before
            req = {
                "jsonrpc": "2.0",
                "id": 1,
                "method": "getSignaturesForAddress",
                "params": [wallet["address"], params],
            }
            resp = http_post_json(rpc_url, req)
            sigs = resp.get("result") or []
            if not isinstance(sigs, list) or not sigs:
                break
            if sigs:
                discovered = True
            oldest_ts = None
            for sig in sigs:
                if not isinstance(sig, dict):
                    continue
                signature = sig.get("signature")
                block_time = sig.get("blockTime")
                if not signature or block_time is None:
                    continue
                ts = int(block_time)
                if oldest_ts is None or ts < oldest_ts:
                    oldest_ts = ts
                if not full_history and ts > int(fetch_end.timestamp()):
                    continue
                if not in_date_range(ts, fetch_start, fetch_end):
                    if not full_history and ts < int(fetch_start.timestamp()):
                        continue
                    if not full_history and ts < int(fetch_start.timestamp()):
                        continue

                tx_req = {
                    "jsonrpc": "2.0",
                    "id": 1,
                    "method": "getTransaction",
                    "params": [signature, {"encoding": "jsonParsed", "maxSupportedTransactionVersion": 0}],
                }
                tx_resp = http_post_json(rpc_url, tx_req)
                tx_data = tx_resp.get("result")
                if not isinstance(tx_data, dict):
                    continue
                meta = tx_data.get("meta") or {}
                message = (
                    tx_data.get("transaction") or {}
                ).get("message") or {}
                keys = message.get("accountKeys") or []
                if keys and isinstance(keys[0], dict):
                    account_keys = [k.get("pubkey") for k in keys]
                else:
                    account_keys = keys
                if wallet["address"] not in account_keys:
                    # For parsed format, maybe list of account objects
                    pass
                if wallet["address"] in account_keys:
                    idx = account_keys.index(wallet["address"])
                else:
                    idx = None

                if idx is not None and meta.get("preBalances") and meta.get("postBalances"):
                    pre_balances = meta.get("preBalances") or []
                    post_balances = meta.get("postBalances") or []
                    if idx < len(pre_balances) and idx < len(post_balances):
                        delta = int(post_balances[idx]) - int(pre_balances[idx])
                        amount = Decimal(delta) / (Decimal(10) ** native_decimals)
                        if amount != 0:
                            direction = "in" if amount > 0 else "out"
                            records.append(
                                build_record(
                                    wallet=wallet,
                                    chain_name=chain_cfg["name"],
                                    chain_family=chain_cfg.get("family", "solana"),
                                    tx_hash=signature,
                                    tx_type="solana_native",
                                    direction=direction,
                                    asset_symbol=native_symbol,
                                    amount=amount.copy_abs(),
                                    amount_raw=delta,
                                    counterparty="",
                                    status="success" if not meta.get("err") else "failed",
                                    tx_time=to_datetime(ts),
                                    notes=f"slot={sig.get('slot', '')}",
                                )
                            )

                # Simple SPL token transfer inference from token balances snapshots.
                pre_token = meta.get("preTokenBalances") or []
                post_token = meta.get("postTokenBalances") or []
                pre_map: Dict[Tuple[str, int], Decimal] = {}
                post_map: Dict[Tuple[str, int], Decimal] = {}
                for entry in pre_token:
                    if not isinstance(entry, dict):
                        continue
                    if entry.get("owner") and entry.get("owner") != wallet["address"]:
                        continue
                    key = (entry.get("mint", ""), int(entry.get("accountIndex", -1)))
                    amount = Decimal(str(entry.get("uiTokenAmount", {}).get("uiAmountString", "0")))
                    pre_map[key] = amount
                for entry in post_token:
                    if not isinstance(entry, dict):
                        continue
                    if entry.get("owner") and entry.get("owner") != wallet["address"]:
                        continue
                    key = (entry.get("mint", ""), int(entry.get("accountIndex", -1)))
                    amount = Decimal(str(entry.get("uiTokenAmount", {}).get("uiAmountString", "0")))
                    post_map[key] = amount
                for key in set(pre_map) | set(post_map):
                    prev = pre_map.get(key, Decimal("0"))
                    nxt = post_map.get(key, Decimal("0"))
                    delta = nxt - prev
                    if delta == 0:
                        continue
                    direction = "in" if delta > 0 else "out"
                    records.append(
                        build_record(
                            wallet=wallet,
                            chain_name=chain_cfg["name"],
                            chain_family=chain_cfg.get("family", "solana"),
                            tx_hash=signature,
                            tx_type="solana_token",
                            direction=direction,
                            asset_symbol=str(key[0][:8]) + "..." if key[0] else "SPL",
                            amount=delta.copy_abs(),
                            amount_raw=str(delta.copy_abs()),
                            counterparty="",
                            status="success" if not meta.get("err") else "failed",
                            tx_time=to_datetime(ts),
                            notes=f"token_account_index={key[1]}",
                        )
                    )

                time.sleep(request_delay)

            before = sigs[-1].get("signature")
            if not isinstance(before, str):
                break
            if not full_history and oldest_ts is not None and oldest_ts < int(fetch_start.timestamp()):
                break
            if len(sigs) < 1000:
                break
    except Exception as exc:
        last_error = str(exc)

    return discovered, records, last_error


def fetch_sui_transactions(
    wallet: Dict[str, str],
    chain_cfg: Dict[str, Any],
    fetch_start: dt.datetime,
    fetch_end: dt.datetime,
    full_history: bool,
    request_delay: float,
) -> Tuple[bool, List[Dict[str, str]], str]:
    rpc_url = chain_cfg["rpc_url"]
    native_symbol = chain_cfg.get("native_symbol", "SUI")
    coin_decimals = chain_cfg.get("coin_decimals", {})
    records: List[Dict[str, str]] = []
    discovered = False
    last_error = ""

    try:
        cursor = None
        while True:
            page_oldest_ts: Optional[int] = None
            query_payload = {
                "jsonrpc": "2.0",
                "id": 1,
                "method": "suix_queryTransactionBlocks",
                "params": [
                    {"FromOrToAddress": wallet["address"]},
                    cursor,
                    50,
                    True,
                ],
            }
            response = http_post_json(rpc_url, query_payload)
            result = response.get("result") or {}
            data = result.get("data") or []
            if not isinstance(data, list) or not data:
                break
            discovered = True
            digests = [item.get("digest") for item in data if isinstance(item, dict) and item.get("digest")]
            if not digests:
                break
            detail_payload = {
                "jsonrpc": "2.0",
                "id": 1,
                "method": "sui_multiGetTransactionBlocks",
                "params": [
                    digests,
                    {
                        "showInput": False,
                        "showEffects": True,
                        "showEvents": True,
                        "showObjectChanges": True,
                        "showBalanceChanges": True,
                        "showRawEffects": False,
                    },
                ],
            }
            details = http_post_json(rpc_url, detail_payload).get("result") or []
            for detail in details:
                if not isinstance(detail, dict):
                    continue
                digest = detail.get("digest", "")
                ts = int(detail.get("timestampMs", "0")) // 1000 if detail.get("timestampMs") else 0
                if not ts:
                    continue
                if page_oldest_ts is None or ts < page_oldest_ts:
                    page_oldest_ts = ts
                if not full_history and ts > int(fetch_end.timestamp()):
                    continue
                if not in_date_range(ts, fetch_start, fetch_end):
                    if not full_history and ts < int(fetch_start.timestamp()):
                        continue
                    if not full_history:
                        continue

                for change in detail.get("balanceChanges") or []:
                    owner = change.get("owner") or {}
                    owner_addr = owner.get("AddressOwner") or ""
                    if owner_addr.lower() != wallet["address"].lower():
                        continue
                    coin_type = change.get("coinType", native_symbol)
                    amount_raw = Decimal(str(change.get("amount", "0")))
                    if amount_raw == 0:
                        continue
                    decimals = int(coin_decimals.get(coin_type, 0))
                    if decimals:
                        amount = amount_raw / (Decimal(10) ** decimals)
                    else:
                        amount = amount_raw
                    direction = "in" if amount_raw > 0 else "out"
                    records.append(
                        build_record(
                            wallet=wallet,
                            chain_name=chain_cfg["name"],
                            chain_family=chain_cfg.get("family", "sui"),
                            tx_hash=digest,
                            tx_type="sui_balance_change",
                            direction=direction,
                            asset_symbol=coin_type,
                            amount=amount.copy_abs(),
                            amount_raw=amount_raw,
                            counterparty="",
                            status=detail.get("effects", {}).get("status", {}).get("status", ""),
                            tx_time=to_datetime(ts),
                            notes=f"checkpoint={detail.get('checkpoint', '')}",
                        )
                    )
            time.sleep(request_delay)

            next_cursor = result.get("nextCursor")
            has_next = bool(result.get("hasNextPage"))
            cursor = next_cursor
            if not has_next or not cursor:
                break
            if not full_history and page_oldest_ts is not None and page_oldest_ts < int(fetch_start.timestamp()):
                break
            time.sleep(request_delay)
    except Exception as exc:
        last_error = str(exc)

    return discovered, records, last_error


def discover_chain(wallet: Dict[str, str], chain_cfg: Dict[str, Any], request_delay: float) -> bool:
    chain_type = chain_cfg.get("type")
    try:
        if chain_type == "evm_explorer":
            api_url = chain_cfg.get("api_url") or chain_cfg.get("base_url")
            chainid = str(chain_cfg.get("chainid", "")).strip()
            api_key = os.getenv(chain_cfg.get("api_key_env", ""), "")
            params = {
                "module": "account",
                "action": "txlist",
                "address": wallet["address"],
                "startblock": 0,
                "endblock": 99999999,
                "page": 1,
                "offset": 1,
                "sort": "desc",
            }
            if chainid:
                params["chainid"] = chainid
            if api_key:
                params["apikey"] = api_key
            payload = http_get_json(f"{api_url}?{urllib.parse.urlencode(params)}")
            result = payload.get("result") or []
            return isinstance(result, list) and bool(result)
        if chain_type == "solana_rpc":
            req = {
                "jsonrpc": "2.0",
                "id": 1,
                "method": "getSignaturesForAddress",
                "params": [wallet["address"], {"limit": 1}],
            }
            payload = http_post_json(chain_cfg["rpc_url"], req)
            sigs = payload.get("result") or []
            return isinstance(sigs, list) and bool(sigs)
        if chain_type == "sui_rpc":
            req = {
                "jsonrpc": "2.0",
                "id": 1,
                "method": "suix_queryTransactionBlocks",
                "params": [{"FromOrToAddress": wallet["address"]}, None, 1, True],
            }
            payload = http_post_json(chain_cfg["rpc_url"], req)
            data = (payload.get("result") or {}).get("data") or []
            return isinstance(data, list) and bool(data)
    except Exception:
        return False
    finally:
        time.sleep(request_delay)
    return False


def write_csv(path: str, rows: List[Dict[str, str]], columns: List[str]) -> None:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=columns)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)


def summarize_by_month(records: List[Dict[str, str]]) -> List[Dict[str, str]]:
    totals: Dict[Tuple[str, str, str, str, str], Decimal] = defaultdict(Decimal)
    counts: Dict[Tuple[str, str, str, str, str], int] = defaultdict(int)
    for row in records:
        key = (
            row["month"],
            row["wallet_address"],
            row["chain"],
            row["asset_symbol"],
            row["direction"],
        )
        totals[key] += Decimal(row["amount"])
        counts[key] += 1
    out: List[Dict[str, str]] = []
    for key in sorted(totals.keys()):
        month, wallet_address, chain, symbol, direction = key
        out.append(
            {
                "month": month,
                "wallet_address": wallet_address,
                "chain": chain,
                "asset_symbol": symbol,
                "direction": direction,
                "tx_count": str(counts[key]),
                "total_amount": format_decimal(totals[key]),
            }
        )
    return out


def filter_salary_candidates(
    records: List[Dict[str, str]],
    salary_cfg: Dict[str, Any],
) -> List[Dict[str, str]]:
    if not salary_cfg.get("enabled"):
        return []
    chains = {name.lower() for name in salary_cfg.get("chain_names", [])}
    keywords = [k.lower() for k in salary_cfg.get("keywords", [])]
    min_amount = Decimal(str(salary_cfg.get("min_amount", "0")))
    out: List[Dict[str, str]] = []
    for row in records:
        if row["chain"].lower() not in chains:
            continue
        if row["direction"] != "in":
            continue
        if Decimal(row["amount"]) < min_amount:
            continue
        hay = " ".join([row.get("notes", ""), row.get("tx_hash", ""), row.get("counterparty", "")]).lower()
        if keywords and not any(k in hay for k in keywords):
            continue
        out.append(row)
    return out


def main() -> int:
    args = parse_args()
    cfg = read_json(args.config)
    wallets = read_wallets(args.wallets_file, args.wallet_filter)
    if not wallets:
        print("No wallets loaded from file.", file=sys.stderr)
        return 1

    if args.year is not None:
        year_start = dt.datetime(args.year, 1, 1, tzinfo=dt.timezone.utc)
        year_end = dt.datetime(args.year, 12, 31, 23, 59, 59, tzinfo=dt.timezone.utc)
    elif args.from_date and args.to_date:
        year_start = parse_utc_date(args.from_date)
        year_end = parse_utc_date(args.to_date)
    else:
        cfg_year = int(cfg.get("default_report_year", dt_utc_now().year))
        year_start = dt.datetime(cfg_year, 1, 1, tzinfo=dt.timezone.utc)
        year_end = dt.datetime(cfg_year, 12, 31, 23, 59, 59, tzinfo=dt.timezone.utc)

    if args.full_history:
        fetch_start = parse_utc_date(cfg.get("history_start", "2019-01-01"))
    else:
        fetch_start = year_start
    fetch_end = year_end

    chains = cfg.get("chains", [])
    request_delay = float(cfg.get("request_delay_seconds", 0.2))
    output_dir = args.output_dir

    wallet_chain_rows = []
    all_records: List[Dict[str, str]] = []
    discover_filter = {x.lower() for x in args.chain_filter}

    for wallet in wallets:
        for chain_cfg in chains:
            chain_name = chain_cfg.get("name")
            if discover_filter and chain_name.lower() not in discover_filter:
                continue
            if not chain_is_compatible(chain_cfg, wallet["family"]):
                continue

            chain_type = chain_cfg.get("type")
            if args.discover_only:
                active = discover_chain(wallet, chain_cfg, request_delay)
                wallet_chain_rows.append(
                    {
                        "wallet_label": wallet["label"],
                        "wallet_address": wallet["address"],
                        "chain": chain_name,
                        "chain_type": chain_type,
                        "active": str(to_bool(active)),
                        "status": "discover_only",
                    }
                )
                continue

            if chain_type == "evm_explorer":
                active, records, error = fetch_evm_transactions(
                    wallet, chain_cfg, fetch_start, fetch_end, args.full_history, request_delay
                )
            elif chain_type == "solana_rpc":
                active, records, error = fetch_solana_transactions(
                    wallet, chain_cfg, fetch_start, fetch_end, args.full_history, request_delay
                )
            elif chain_type == "sui_rpc":
                active, records, error = fetch_sui_transactions(
                    wallet, chain_cfg, fetch_start, fetch_end, args.full_history, request_delay
                )
            else:
                active = False
                records = []
                error = f"Unsupported chain type: {chain_type}"

            wallet_chain_rows.append(
                {
                    "wallet_label": wallet["label"],
                    "wallet_address": wallet["address"],
                    "chain": chain_name,
                    "chain_type": chain_type,
                    "active": str(bool(active)),
                    "status": "ok" if not error else error,
                }
            )
            all_records.extend(records)

    all_records.sort(key=lambda r: (r["tx_time_utc"], r["wallet_label"], r["chain"]))
    year_str = str(fetch_start.year) if args.year is None else str(args.year)
    year_records = [r for r in all_records if year_start <= dt.datetime.fromisoformat(r["tx_time_utc"]) <= fetch_end]

    os.makedirs(output_dir, exist_ok=True)
    write_csv(
        os.path.join(output_dir, "wallet_chain_activity.csv"),
        wallet_chain_rows,
        ["wallet_label", "wallet_address", "chain", "chain_type", "active", "status"],
    )
    write_csv(os.path.join(output_dir, "all_transactions.csv"), all_records, CSV_COLUMNS)
    write_csv(
        os.path.join(output_dir, f"transactions_{year_str}.csv"),
        year_records,
        CSV_COLUMNS,
    )
    write_csv(
        os.path.join(output_dir, f"monthly_summary_{year_str}.csv"),
        summarize_by_month(year_records),
        ["month", "wallet_address", "chain", "asset_symbol", "direction", "tx_count", "total_amount"],
    )

    salary_candidates = filter_salary_candidates(year_records, cfg.get("salary_detection", {}))
    if salary_candidates:
        write_csv(
            os.path.join(output_dir, f"salary_candidates_{year_str}.csv"),
            salary_candidates,
            CSV_COLUMNS,
        )

    print(f"wallets: {len(wallets)}")
    print(f"wallet_chain combinations checked: {len(wallet_chain_rows)}")
    print(f"records written: {len(all_records)} total, {len(year_records)} in {year_str}")
    print(f"output dir: {output_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
