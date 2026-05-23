#!/usr/bin/env python3
"""Build a move-date on-chain inventory from archived raw evidence.

The output is a reproducible balance snapshot at the Polish residency start
cut-off. It is not a PIT-38 cost-basis calculation by itself: the balances must
still be mapped to documented acquisition-cost layers.

Default cut-off: 2023-04-12T00:00:00Z.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
from collections import defaultdict
from dataclasses import dataclass, field
from datetime import datetime, timezone
from decimal import Decimal
from pathlib import Path
from typing import Any


EVM_ADDRESS_RE = re.compile(r"^0x[a-fA-F0-9]{40}$")
TRANSFER_TOPIC = "0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef"
ZERO_ADDRESS = "0x0000000000000000000000000000000000000000"
NATIVE_SYMBOLS = {
    "ethereum": "ETH",
    "polygon": "MATIC",
    "arbitrum": "ETH",
    "optimism": "ETH",
    "fantom": "FTM",
}
SPAM_HINTS = (
    "visit",
    "claim",
    "airdrop",
    "casino",
    "gambling",
    "reward.xyz",
    "rewards",
    "free",
    ".com",
    ".net",
    ".org",
    "2xcoin",
    "2xbnb",
    "minereum",
)


@dataclass
class Movement:
    chain: str
    wallet_label: str
    wallet_address: str
    asset_type: str
    contract_address: str
    token_id: str
    symbol: str
    name: str
    decimals: int
    amount_raw: Decimal
    direction: str
    timestamp: str
    block_number: str
    tx_hash: str
    source_file: str
    method: str = ""
    confidence: str = "token-transfer"
    limitation: str = ""

    @property
    def amount(self) -> Decimal:
        if self.decimals <= 0:
            return self.amount_raw
        return self.amount_raw / (Decimal(10) ** self.decimals)


@dataclass
class Balance:
    chain: str
    wallet_label: str
    wallet_address: str
    asset_type: str
    contract_address: str
    token_id: str
    symbol: str
    name: str
    decimals: int
    amount_raw: Decimal = Decimal("0")
    in_count: int = 0
    out_count: int = 0
    first_seen: str = ""
    last_seen: str = ""
    confidence: set[str] = field(default_factory=set)
    limitations: set[str] = field(default_factory=set)

    @property
    def amount(self) -> Decimal:
        if self.decimals <= 0:
            return self.amount_raw
        return self.amount_raw / (Decimal(10) ** self.decimals)


def read_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def compact(value: Any) -> str:
    return " ".join(str(value or "").split())


def normalize_address(value: Any) -> str:
    if isinstance(value, dict):
        value = value.get("hash", "")
    text = str(value or "").lower()
    return text if EVM_ADDRESS_RE.match(text) else ""


def address_from_topic(topic: str) -> str:
    topic = str(topic or "").lower()
    if len(topic) != 66:
        return ""
    return "0x" + topic[-40:]


def parse_int(value: Any) -> int:
    if value in (None, ""):
        return 0
    text = str(value)
    if text.startswith("0x"):
        return int(text, 16)
    return int(text)


def parse_decimal_int(value: Any) -> Decimal:
    if value in (None, ""):
        return Decimal("0")
    text = str(value)
    if text.startswith("0x"):
        return Decimal(int(text, 16))
    return Decimal(text)


def parse_iso_timestamp(value: str) -> int:
    text = value.replace("Z", "+00:00")
    return int(datetime.fromisoformat(text).timestamp())


def fmt_decimal(value: Decimal) -> str:
    text = format(value.normalize(), "f")
    if "." in text:
        text = text.rstrip("0").rstrip(".")
    return text or "0"


def looks_like_spam(symbol: str, name: str) -> bool:
    text = f"{symbol} {name}".lower()
    return any(hint in text for hint in SPAM_HINTS)


def is_partial_fantom_native(balance: "Balance") -> bool:
    return balance.chain == "fantom" and balance.asset_type == "native" and any(
        c.startswith("fantom-trace-transaction") for c in balance.confidence
    )


def basis_status(balance: "Balance") -> str:
    if balance.amount_raw < 0:
        return "reconciliation exception: negative movement-derived balance or debt token; do not import as cost"
    if is_partial_fantom_native(balance):
        return "partial native-flow estimate from known Fantom token tx traces; not a complete balance snapshot"
    if looks_like_spam(balance.symbol, balance.name):
        return "likely spam/airdrop; exclude unless independently verified"
    return "needs acquisition-cost provenance; do not treat as PIT-38 imported cost by amount alone"


def read_evm_wallets(path: Path) -> dict[str, str]:
    wallets: dict[str, str] = {}
    for raw in path.read_text(encoding="utf-8", errors="replace").splitlines():
        line = compact(raw)
        if not line or line.startswith("#") or " " not in line:
            continue
        label, address = line.rsplit(" ", 1)
        if EVM_ADDRESS_RE.match(address):
            wallets[address.lower()] = label
    return wallets


def timestamp_text(ts: int) -> str:
    return datetime.fromtimestamp(ts, timezone.utc).isoformat().replace("+00:00", "Z")


def movement_key(event: dict[str, Any]) -> tuple[str, ...]:
    return (
        str(event.get("chain", "")),
        str(event.get("tx_hash", "")),
        str(event.get("log_index", "")),
        str(event.get("contract_address", "")),
        str(event.get("token_id", "")),
        str(event.get("from_address", "")),
        str(event.get("to_address", "")),
        str(event.get("amount_raw", "")),
        str(event.get("source_kind", "")),
    )


def add_token_event(
    events: list[Movement],
    seen: set[tuple[str, ...]],
    wallets: dict[str, str],
    *,
    chain: str,
    asset_type: str,
    contract_address: str,
    token_id: str,
    symbol: str,
    name: str,
    decimals: int,
    amount_raw: Decimal,
    from_address: str,
    to_address: str,
    timestamp: int,
    block_number: str,
    tx_hash: str,
    source_file: Path,
    log_index: str = "",
    method: str = "",
    confidence: str = "token-transfer",
    limitation: str = "",
) -> None:
    if not tx_hash or amount_raw == 0:
        return
    event = {
        "chain": chain,
        "tx_hash": tx_hash.lower(),
        "log_index": log_index,
        "contract_address": contract_address.lower(),
        "token_id": token_id,
        "from_address": from_address.lower(),
        "to_address": to_address.lower(),
        "amount_raw": str(amount_raw),
        "source_kind": confidence,
    }
    key = movement_key(event)
    if key in seen:
        return
    seen.add(key)

    ts_text = timestamp_text(timestamp)
    for direction, address in (("out", from_address.lower()), ("in", to_address.lower())):
        if address not in wallets:
            continue
        sign = Decimal("-1") if direction == "out" else Decimal("1")
        events.append(
            Movement(
                chain=chain,
                wallet_label=wallets[address],
                wallet_address=address,
                asset_type=asset_type,
                contract_address=contract_address.lower(),
                token_id=token_id,
                symbol=symbol,
                name=name,
                decimals=decimals,
                amount_raw=amount_raw * sign,
                direction=direction,
                timestamp=ts_text,
                block_number=str(block_number),
                tx_hash=tx_hash.lower(),
                source_file=str(source_file),
                method=method,
                confidence=confidence,
                limitation=limitation,
            )
        )


def iter_evm_explorer_files(raw_dir: Path) -> list[Path]:
    roots = [
        raw_dir / "evm-explorer-pre-move-core",
        raw_dir / "evm-explorer-mantle-arbitrum",
    ]
    paths: list[Path] = []
    for root in roots:
        if root.exists():
            paths.extend(root.glob("*/*/*_page_*.json"))
    return sorted(paths)


def chain_from_explorer_path(path: Path, payload: dict[str, Any]) -> str:
    if payload.get("chain"):
        return str(payload["chain"]).lower()
    parts = path.parts
    for marker in ("evm-explorer-pre-move-core", "evm-explorer-mantle-arbitrum"):
        if marker in parts:
            return parts[parts.index(marker) + 1].lower()
    return ""


def load_evm_explorer_events(
    raw_dir: Path,
    wallets: dict[str, str],
    cutoff_ts: int,
) -> tuple[list[Movement], list[Movement]]:
    token_events: list[Movement] = []
    native_events: list[Movement] = []
    seen_token_events: set[tuple[str, ...]] = set()
    seen_native_transfers: set[tuple[str, ...]] = set()
    seen_gas_fees: set[tuple[str, str, str]] = set()

    for path in iter_evm_explorer_files(raw_dir):
        payload = read_json(path)
        chain = chain_from_explorer_path(path, payload)
        action = str(payload.get("action") or path.name.split("_page_")[0])
        if chain in {"mantle", "scroll", "mode", "optimism", "fantom"}:
            continue
        rows = payload.get("result")
        if not isinstance(rows, list):
            continue
        for row in rows:
            ts = parse_int(row.get("timeStamp"))
            if not ts or ts >= cutoff_ts:
                continue
            tx_hash = str(row.get("hash", "")).lower()
            block_number = str(row.get("blockNumber", ""))
            if action in {"tokentx", "tokennfttx", "token1155tx"}:
                if action == "tokentx":
                    asset_type = "ERC-20"
                    amount_raw = parse_decimal_int(row.get("value"))
                    decimals = parse_int(row.get("tokenDecimal"))
                    token_id = ""
                elif action == "tokennfttx":
                    asset_type = "ERC-721"
                    amount_raw = Decimal("1")
                    decimals = 0
                    token_id = str(row.get("tokenID", ""))
                else:
                    asset_type = "ERC-1155"
                    amount_raw = parse_decimal_int(row.get("tokenValue") or row.get("value") or "1")
                    decimals = 0
                    token_id = str(row.get("tokenID", ""))
                add_token_event(
                    token_events,
                    seen_token_events,
                    wallets,
                    chain=chain,
                    asset_type=asset_type,
                    contract_address=str(row.get("contractAddress", "")),
                    token_id=token_id,
                    symbol=str(row.get("tokenSymbol", "")),
                    name=str(row.get("tokenName", "")),
                    decimals=decimals,
                    amount_raw=amount_raw,
                    from_address=normalize_address(row.get("from")),
                    to_address=normalize_address(row.get("to")),
                    timestamp=ts,
                    block_number=block_number,
                    tx_hash=tx_hash,
                    source_file=path,
                    log_index=str(row.get("logIndex", "")),
                    method=str(row.get("functionName", "")),
                )
                continue

            if action == "txlist":
                from_address = normalize_address(row.get("from"))
                to_address = normalize_address(row.get("to"))
                native_symbol = NATIVE_SYMBOLS.get(chain, chain.upper())
                success = str(row.get("isError", "0")) == "0" and str(row.get("txreceipt_status", "1")) != "0"
                value_raw = parse_decimal_int(row.get("value"))
                if success and value_raw:
                    key = (chain, tx_hash, "native-transfer")
                    if key not in seen_native_transfers:
                        seen_native_transfers.add(key)
                        add_token_event(
                            native_events,
                            seen_token_events,
                            wallets,
                            chain=chain,
                            asset_type="native",
                            contract_address="native",
                            token_id="",
                            symbol=native_symbol,
                            name=f"{native_symbol} native",
                            decimals=18,
                            amount_raw=value_raw,
                            from_address=from_address,
                            to_address=to_address,
                            timestamp=ts,
                            block_number=block_number,
                            tx_hash=tx_hash,
                            source_file=path,
                            confidence="native-txlist",
                        )
                if from_address in wallets:
                    gas_fee_raw = parse_decimal_int(row.get("gasUsed")) * parse_decimal_int(row.get("gasPrice"))
                    if gas_fee_raw:
                        fee_key = (chain, tx_hash, "gas")
                        if fee_key not in seen_gas_fees:
                            seen_gas_fees.add(fee_key)
                            native_events.append(
                                Movement(
                                    chain=chain,
                                    wallet_label=wallets[from_address],
                                    wallet_address=from_address,
                                    asset_type="native",
                                    contract_address="native",
                                    token_id="",
                                    symbol=native_symbol,
                                    name=f"{native_symbol} native gas",
                                    decimals=18,
                                    amount_raw=-gas_fee_raw,
                                    direction="fee",
                                    timestamp=timestamp_text(ts),
                                    block_number=block_number,
                                    tx_hash=tx_hash,
                                    source_file=str(path),
                                    confidence="native-gas-txlist",
                                )
                            )
                continue

            if action == "txlistinternal":
                success = str(row.get("isError", "0")) == "0"
                if not success:
                    continue
                value_raw = parse_decimal_int(row.get("value"))
                if not value_raw:
                    continue
                key = (chain, tx_hash, str(row.get("traceId", "")), "internal")
                if key in seen_native_transfers:
                    continue
                seen_native_transfers.add(key)
                native_symbol = NATIVE_SYMBOLS.get(chain, chain.upper())
                add_token_event(
                    native_events,
                    seen_token_events,
                    wallets,
                    chain=chain,
                    asset_type="native",
                    contract_address="native",
                    token_id="",
                    symbol=native_symbol,
                    name=f"{native_symbol} native internal",
                    decimals=18,
                    amount_raw=value_raw,
                    from_address=normalize_address(row.get("from")),
                    to_address=normalize_address(row.get("to")),
                    timestamp=ts,
                    block_number=block_number,
                    tx_hash=tx_hash,
                    source_file=path,
                    confidence="native-internal",
                )

    return token_events, native_events


def load_blockscout_events(
    raw_dir: Path,
    wallets: dict[str, str],
    cutoff_ts: int,
) -> tuple[list[Movement], list[Movement]]:
    token_events: list[Movement] = []
    native_events: list[Movement] = []
    seen_token_events: set[tuple[str, ...]] = set()
    seen_native_transfers: set[tuple[str, ...]] = set()
    seen_gas_fees: set[tuple[str, str, str]] = set()
    root = raw_dir / "blockscout-v2" / "optimism"
    if not root.exists():
        return token_events, native_events

    for path in sorted(root.glob("*/*_page_*.json")):
        payload = read_json(path)
        endpoint = str(payload.get("endpoint") or path.name.split("_page_")[0])
        chain = str(payload.get("chain") or "optimism").lower()
        items = payload.get("items")
        if not isinstance(items, list):
            continue
        for item in items:
            ts = parse_iso_timestamp(str(item.get("timestamp", "")))
            if ts >= cutoff_ts:
                continue
            tx_hash = str(item.get("transaction_hash") or item.get("hash") or "").lower()
            block_number = str(item.get("block_number", ""))
            if endpoint == "token-transfers":
                token = item.get("token") if isinstance(item.get("token"), dict) else {}
                total = item.get("total") if isinstance(item.get("total"), dict) else {}
                token_type = str(item.get("token_type") or token.get("type") or "ERC-20")
                decimals = parse_int(total.get("decimals") or token.get("decimals") or "0")
                amount_raw = parse_decimal_int(total.get("value") or item.get("value") or "0")
                asset_type = token_type.upper()
                if asset_type == "ERC-721" and not amount_raw:
                    amount_raw = Decimal("1")
                add_token_event(
                    token_events,
                    seen_token_events,
                    wallets,
                    chain=chain,
                    asset_type=asset_type,
                    contract_address=str(token.get("address_hash", "")),
                    token_id=str(item.get("token_id") or ""),
                    symbol=str(token.get("symbol", "")),
                    name=str(token.get("name", "")),
                    decimals=decimals,
                    amount_raw=amount_raw,
                    from_address=normalize_address(item.get("from")),
                    to_address=normalize_address(item.get("to")),
                    timestamp=ts,
                    block_number=block_number,
                    tx_hash=tx_hash,
                    source_file=path,
                    log_index=str(item.get("log_index", "")),
                    method=str(item.get("method", "")),
                )
                continue

            if endpoint == "transactions":
                from_address = normalize_address(item.get("from"))
                to_address = normalize_address(item.get("to"))
                native_symbol = NATIVE_SYMBOLS.get(chain, chain.upper())
                success = str(item.get("status", "")) == "ok" and str(item.get("result", "")) == "success"
                value_raw = parse_decimal_int(item.get("value"))
                if success and value_raw:
                    key = (chain, tx_hash, "native-transfer")
                    if key not in seen_native_transfers:
                        seen_native_transfers.add(key)
                        add_token_event(
                            native_events,
                            seen_token_events,
                            wallets,
                            chain=chain,
                            asset_type="native",
                            contract_address="native",
                            token_id="",
                            symbol=native_symbol,
                            name=f"{native_symbol} native",
                            decimals=18,
                            amount_raw=value_raw,
                            from_address=from_address,
                            to_address=to_address,
                            timestamp=ts,
                            block_number=block_number,
                            tx_hash=tx_hash,
                            source_file=path,
                            confidence="native-blockscout",
                        )
                if from_address in wallets:
                    fee = item.get("fee") if isinstance(item.get("fee"), dict) else {}
                    fee_raw = parse_decimal_int(fee.get("value"))
                    fee_key = (chain, tx_hash, "gas")
                    if fee_raw and fee_key not in seen_gas_fees:
                        seen_gas_fees.add(fee_key)
                        native_events.append(
                            Movement(
                                chain=chain,
                                wallet_label=wallets[from_address],
                                wallet_address=from_address,
                                asset_type="native",
                                contract_address="native",
                                token_id="",
                                symbol=native_symbol,
                                name=f"{native_symbol} native gas",
                                decimals=18,
                                amount_raw=-fee_raw,
                                direction="fee",
                                timestamp=timestamp_text(ts),
                                block_number=block_number,
                                tx_hash=tx_hash,
                                source_file=str(path),
                                method=str(item.get("method", "")),
                                confidence="native-gas-blockscout",
                            )
                        )
                continue

            if endpoint == "internal-transactions":
                if item.get("success") is False:
                    continue
                value_raw = parse_decimal_int(item.get("value"))
                if not value_raw:
                    continue
                trace_id = str(item.get("index", ""))
                key = (chain, tx_hash, trace_id, "internal")
                if key in seen_native_transfers:
                    continue
                seen_native_transfers.add(key)
                native_symbol = NATIVE_SYMBOLS.get(chain, chain.upper())
                add_token_event(
                    native_events,
                    seen_token_events,
                    wallets,
                    chain=chain,
                    asset_type="native",
                    contract_address="native",
                    token_id="",
                    symbol=native_symbol,
                    name=f"{native_symbol} native internal",
                    decimals=18,
                    amount_raw=value_raw,
                    from_address=normalize_address(item.get("from")),
                    to_address=normalize_address(item.get("to")),
                    timestamp=ts,
                    block_number=block_number,
                    tx_hash=tx_hash,
                    source_file=path,
                    confidence="native-internal-blockscout",
                )

    return token_events, native_events


def load_fantom_events(
    raw_dir: Path,
    wallets: dict[str, str],
    cutoff_ts: int,
) -> tuple[list[Movement], list[Movement]]:
    token_events: list[Movement] = []
    native_events: list[Movement] = []
    seen_token_events: set[tuple[str, ...]] = set()
    root = raw_dir / "rpc-transfer-logs" / "fantom"
    if root.exists():
        timestamps_path = root / "block_timestamps.json"
        metadata_path = root / "token_metadata.json"
        timestamps = {int(k): int(v) for k, v in read_json(timestamps_path).items()} if timestamps_path.exists() else {}
        metadata = read_json(metadata_path) if metadata_path.exists() else {}
        for path in sorted(root.glob("0x*/transfer_*_chunk_*.json")):
            payload = read_json(path)
            for log in payload.get("logs", []):
                topics = [str(t).lower() for t in log.get("topics", [])]
                if len(topics) < 3 or topics[0] != TRANSFER_TOPIC:
                    continue
                block_number = parse_int(log.get("blockNumber"))
                ts = timestamps.get(block_number)
                if not ts or ts >= cutoff_ts:
                    continue
                contract = normalize_address(log.get("address"))
                meta = metadata.get(contract, {}) if isinstance(metadata.get(contract), dict) else {}
                if len(topics) >= 4:
                    asset_type = "ERC-721"
                    amount_raw = Decimal("1")
                    decimals = 0
                    token_id = str(parse_int(topics[3]))
                else:
                    asset_type = "ERC-20"
                    amount_raw = parse_decimal_int(log.get("data"))
                    decimals = parse_int(meta.get("decimals") or "18")
                    token_id = ""
                add_token_event(
                    token_events,
                    seen_token_events,
                    wallets,
                    chain="fantom",
                    asset_type=asset_type,
                    contract_address=contract,
                    token_id=token_id,
                    symbol=str(meta.get("symbol") or ""),
                    name=str(meta.get("name") or ""),
                    decimals=decimals,
                    amount_raw=amount_raw,
                    from_address=address_from_topic(topics[1]),
                    to_address=address_from_topic(topics[2]),
                    timestamp=ts,
                    block_number=str(block_number),
                    tx_hash=str(log.get("transactionHash", "")).lower(),
                    source_file=path,
                    log_index=str(parse_int(log.get("logIndex"))),
                    confidence="fantom-rpc-transfer-log",
                )

    trace_root = raw_dir / "rpc-transaction-traces" / "fantom"
    seen_traces: set[tuple[str, str, str]] = set()
    if trace_root.exists():
        for path in sorted(trace_root.glob("0x*.json")):
            payload = read_json(path)
            ts = parse_int(payload.get("block_timestamp"))
            if not ts or ts >= cutoff_ts:
                continue
            tx_hash = str(payload.get("tx_hash") or path.stem).lower()
            for trace in payload.get("traces", []):
                action = trace.get("action") if isinstance(trace.get("action"), dict) else {}
                value_raw = parse_decimal_int(action.get("value"))
                if not value_raw:
                    continue
                from_address = normalize_address(action.get("from"))
                to_address = normalize_address(action.get("to"))
                trace_address = ".".join(str(x) for x in trace.get("traceAddress", []))
                key = (tx_hash, trace_address, str(value_raw))
                if key in seen_traces:
                    continue
                seen_traces.add(key)
                add_token_event(
                    native_events,
                    seen_token_events,
                    wallets,
                    chain="fantom",
                    asset_type="native",
                    contract_address="native",
                    token_id="",
                    symbol="FTM",
                    name="FTM native trace value",
                    decimals=18,
                    amount_raw=value_raw,
                    from_address=from_address,
                    to_address=to_address,
                    timestamp=ts,
                    block_number=str(payload.get("block_number", "")),
                    tx_hash=tx_hash,
                    source_file=path,
                    log_index=trace_address,
                    confidence="fantom-trace-transaction-known-token-tx",
                    limitation="Only transactions already discovered from token-transfer logs; gas fees and native-only txs are not included.",
                )

    return token_events, native_events


def aggregate_balances(movements: list[Movement]) -> list[Balance]:
    balances: dict[tuple[str, ...], Balance] = {}
    for m in movements:
        key = (
            m.chain,
            m.wallet_address,
            m.asset_type,
            m.contract_address,
            m.token_id,
            m.symbol,
        )
        if key not in balances:
            balances[key] = Balance(
                chain=m.chain,
                wallet_label=m.wallet_label,
                wallet_address=m.wallet_address,
                asset_type=m.asset_type,
                contract_address=m.contract_address,
                token_id=m.token_id,
                symbol=m.symbol,
                name=m.name,
                decimals=m.decimals,
            )
        b = balances[key]
        b.amount_raw += m.amount_raw
        if m.direction == "in":
            b.in_count += 1
        else:
            b.out_count += 1
        b.first_seen = min([x for x in [b.first_seen, m.timestamp] if x], default=m.timestamp)
        b.last_seen = max([x for x in [b.last_seen, m.timestamp] if x], default=m.timestamp)
        b.confidence.add(m.confidence)
        if m.limitation:
            b.limitations.add(m.limitation)
    return sorted(balances.values(), key=lambda b: (b.chain, b.wallet_label, b.symbol, b.contract_address, b.token_id))


def write_movements(path: Path, movements: list[Movement]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=[
                "timestamp",
                "chain",
                "wallet_label",
                "wallet_address",
                "direction",
                "asset_type",
                "contract_address",
                "token_id",
                "symbol",
                "name",
                "decimals",
                "amount_raw",
                "amount",
                "block_number",
                "tx_hash",
                "method",
                "confidence",
                "limitation",
                "source_file",
            ],
        )
        writer.writeheader()
        for m in sorted(movements, key=lambda x: (x.timestamp, x.chain, x.wallet_label, x.tx_hash)):
            writer.writerow(
                {
                    "timestamp": m.timestamp,
                    "chain": m.chain,
                    "wallet_label": m.wallet_label,
                    "wallet_address": m.wallet_address,
                    "direction": m.direction,
                    "asset_type": m.asset_type,
                    "contract_address": m.contract_address,
                    "token_id": m.token_id,
                    "symbol": m.symbol,
                    "name": m.name,
                    "decimals": str(m.decimals),
                    "amount_raw": fmt_decimal(m.amount_raw),
                    "amount": fmt_decimal(m.amount),
                    "block_number": m.block_number,
                    "tx_hash": m.tx_hash,
                    "method": m.method,
                    "confidence": m.confidence,
                    "limitation": m.limitation,
                    "source_file": m.source_file,
                }
            )


def write_balances(path: Path, balances: list[Balance]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=[
                "chain",
                "wallet_label",
                "wallet_address",
                "asset_type",
                "contract_address",
                "token_id",
                "symbol",
                "name",
                "decimals",
                "amount_raw",
                "amount",
                "in_count",
                "out_count",
                "first_seen",
                "last_seen",
                "confidence",
                "limitations",
                "basis_status",
            ],
        )
        writer.writeheader()
        for b in balances:
            if b.amount_raw == 0:
                continue
            writer.writerow(
                {
                    "chain": b.chain,
                    "wallet_label": b.wallet_label,
                    "wallet_address": b.wallet_address,
                    "asset_type": b.asset_type,
                    "contract_address": b.contract_address,
                    "token_id": b.token_id,
                    "symbol": b.symbol,
                    "name": b.name,
                    "decimals": str(b.decimals),
                    "amount_raw": fmt_decimal(b.amount_raw),
                    "amount": fmt_decimal(b.amount),
                    "in_count": str(b.in_count),
                    "out_count": str(b.out_count),
                    "first_seen": b.first_seen,
                    "last_seen": b.last_seen,
                    "confidence": "; ".join(sorted(b.confidence)),
                    "limitations": "; ".join(sorted(b.limitations)),
                    "basis_status": basis_status(b),
                }
            )


def write_exceptions(path: Path, balances: list[Balance]) -> None:
    exceptions = [
        b for b in balances
        if b.amount_raw < 0 or is_partial_fantom_native(b)
    ]
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=[
                "chain",
                "wallet_label",
                "asset_type",
                "symbol",
                "name",
                "amount",
                "contract_address",
                "token_id",
                "first_seen",
                "last_seen",
                "confidence",
                "basis_status",
            ],
        )
        writer.writeheader()
        for b in sorted(exceptions, key=lambda x: (x.chain, x.wallet_label, x.symbol, x.contract_address)):
            writer.writerow(
                {
                    "chain": b.chain,
                    "wallet_label": b.wallet_label,
                    "asset_type": b.asset_type,
                    "symbol": b.symbol,
                    "name": b.name,
                    "amount": fmt_decimal(b.amount),
                    "contract_address": b.contract_address,
                    "token_id": b.token_id,
                    "first_seen": b.first_seen,
                    "last_seen": b.last_seen,
                    "confidence": "; ".join(sorted(b.confidence)),
                    "basis_status": basis_status(b),
                }
            )


def write_json_summary(path: Path, cutoff: str, movements: list[Movement], balances: list[Balance]) -> None:
    nonzero = [b for b in balances if b.amount_raw != 0]
    exceptions = [b for b in nonzero if b.amount_raw < 0 or is_partial_fantom_native(b)]
    likely_spam = [b for b in nonzero if looks_like_spam(b.symbol, b.name)]
    by_chain: dict[str, int] = defaultdict(int)
    by_wallet: dict[str, int] = defaultdict(int)
    for b in nonzero:
        by_chain[b.chain] += 1
        by_wallet[b.wallet_label] += 1
    payload = {
        "cutoff": cutoff,
        "movement_rows": len(movements),
        "nonzero_balance_rows": len(nonzero),
        "reconciliation_exception_rows": len(exceptions),
        "likely_spam_or_airdrop_rows": len(likely_spam),
        "nonzero_rows_by_chain": dict(sorted(by_chain.items())),
        "nonzero_rows_by_wallet": dict(sorted(by_wallet.items())),
        "limitations": [
            "Balances are reconstructed from archived movement evidence, not from archive-node balanceOf calls.",
            "Token balances must still be mapped to documented acquisition-cost layers before becoming PIT-38 imported costs.",
            "Fantom native balances are partial: known token-movement transaction traces are included, but native-only transactions and gas fees are not.",
            "Protocol positions may require separate contract-state reconstruction where balances are represented by vault, gauge, LP, or debt tokens.",
        ],
    }
    path.write_text(json.dumps(payload, indent=2, sort_keys=True), encoding="utf-8")


def top_balances(balances: list[Balance], limit: int = 80) -> list[Balance]:
    nonzero = [
        b for b in balances
        if b.amount_raw > 0 and not is_partial_fantom_native(b) and not looks_like_spam(b.symbol, b.name)
    ]
    stable_priority = {"USDC", "USDC.E", "USDT", "DAI", "ERN", "FRAX", "MIM", "SUSD", "DOLA"}

    def sort_key(b: Balance) -> tuple[int, str, str, str]:
        symbol = b.symbol.upper()
        priority = 0 if symbol in stable_priority or b.asset_type == "native" else 1
        return (priority, b.chain, b.wallet_label, symbol)

    return sorted(nonzero, key=sort_key)[:limit]


def write_markdown(path: Path, cutoff: str, movements: list[Movement], balances: list[Balance]) -> None:
    nonzero = [b for b in balances if b.amount_raw != 0]
    chain_counts: dict[str, int] = defaultdict(int)
    wallet_counts: dict[str, int] = defaultdict(int)
    for b in nonzero:
        chain_counts[b.chain] += 1
        wallet_counts[b.wallet_label] += 1

    lines = [
        "# Move-Date On-Chain Inventory",
        "",
        f"Cut-off: `{cutoff}`",
        "",
        "This is a reconstructed asset-position snapshot from archived on-chain movement evidence. It is not yet a Polish PIT-38 cost-basis number.",
        "",
        "## Summary",
        "",
        f"- Movement rows parsed: `{len(movements)}`",
        f"- Non-zero balance rows: `{len(nonzero)}`",
        "- Main output CSV: `move-date-token-balances.csv`",
        "- Movement evidence CSV: `move-date-movements.csv`",
        "- Reconciliation exceptions CSV: `move-date-reconciliation-exceptions.csv`",
        "- JSON summary: `move-date-inventory-summary.json`",
        "",
        "## Non-Zero Rows By Chain",
        "",
        "| Chain | Rows |",
        "| --- | ---: |",
    ]
    for chain, count in sorted(chain_counts.items()):
        lines.append(f"| {chain} | {count} |")
    lines.extend(["", "## Non-Zero Rows By Wallet", "", "| Wallet | Rows |", "| --- | ---: |"])
    for wallet, count in sorted(wallet_counts.items()):
        lines.append(f"| {wallet} | {count} |")

    lines.extend(
        [
            "",
            "## Priority Balances To Reconcile",
            "",
            "These are not automatically deductible costs. Each row needs provenance into Layer A, Layer B, Layer C, or excluded/no-basis treatment.",
            "",
            "| Chain | Wallet | Asset | Amount | Contract / token id | Confidence |",
            "| --- | --- | --- | ---: | --- | --- |",
        ]
    )
    for b in top_balances(balances):
        asset = f"{b.symbol or b.asset_type} ({b.asset_type})"
        token_ref = b.contract_address
        if b.token_id:
            token_ref = f"{token_ref} #{b.token_id}"
        lines.append(
            f"| {b.chain} | {b.wallet_label} | {asset} | {fmt_decimal(b.amount)} | `{token_ref}` | {'; '.join(sorted(b.confidence))} |"
        )

    exceptions = [b for b in balances if b.amount_raw < 0 or is_partial_fantom_native(b)]
    lines.extend(
        [
            "",
            "## Reconciliation Exceptions",
            "",
            "These rows should not be imported as PIT-38 costs. They either reflect incomplete native-flow evidence, debt-token behavior, or missing earlier legs in the archived movement history.",
            "",
            "| Chain | Wallet | Asset | Amount | Reason |",
            "| --- | --- | --- | ---: | --- |",
        ]
    )
    for b in sorted(exceptions, key=lambda x: (x.chain, x.wallet_label, x.symbol, x.contract_address))[:80]:
        asset = f"{b.symbol or b.asset_type} ({b.asset_type})"
        lines.append(f"| {b.chain} | {b.wallet_label} | {asset} | {fmt_decimal(b.amount)} | {basis_status(b)} |")

    lines.extend(
        [
            "",
            "## Use For PIT-38",
            "",
            "- Layer A can only be populated from balances whose unrecovered acquisition cost is traceable to documented fiat purchases.",
            "- Layer B can only be populated from same-token pre-residency salary USDC that was taxed in Sweden and still exists as USDC at the move date.",
            "- Layer C is the high-risk successor-basis bucket for value that moved through pre-move crypto-to-crypto swaps.",
            "- A token amount or LP/vault token balance is not enough by itself; we still need acquisition-cost provenance.",
            "",
            "## Known Limitations",
            "",
            "- This pass reconstructs from archived movements rather than querying every contract at a historical archive block.",
            "- Fantom token movements are strong, but native FTM remains partial because native-only transactions and gas fees are not discoverable from token logs.",
            "- DeFi positions may be represented as LP, vault, gauge, receipt, or debt tokens. Those rows require protocol-specific interpretation before assigning cost basis.",
            "- Dust/spam NFTs and airdrops can appear as balance rows; they should not be imported as costs without evidence.",
            "",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--wallets-file", type=Path, default=Path("docs/crypto-transactions/wallets.txt"))
    parser.add_argument("--raw-dir", type=Path, default=Path("private/evidence/onchain/raw"))
    parser.add_argument("--output-dir", type=Path, default=Path("private/evidence/onchain/move-date-inventory-2023-04-12"))
    parser.add_argument("--cutoff", default="2023-04-12T00:00:00Z")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    cutoff_ts = parse_iso_timestamp(args.cutoff)
    wallets = read_evm_wallets(args.wallets_file)

    explorer_tokens, explorer_native = load_evm_explorer_events(args.raw_dir, wallets, cutoff_ts)
    blockscout_tokens, blockscout_native = load_blockscout_events(args.raw_dir, wallets, cutoff_ts)
    fantom_tokens, fantom_native = load_fantom_events(args.raw_dir, wallets, cutoff_ts)
    movements = explorer_tokens + explorer_native + blockscout_tokens + blockscout_native + fantom_tokens + fantom_native
    balances = aggregate_balances(movements)

    args.output_dir.mkdir(parents=True, exist_ok=True)
    write_movements(args.output_dir / "move-date-movements.csv", movements)
    write_balances(args.output_dir / "move-date-token-balances.csv", balances)
    write_exceptions(args.output_dir / "move-date-reconciliation-exceptions.csv", balances)
    write_json_summary(args.output_dir / "move-date-inventory-summary.json", args.cutoff, movements, balances)
    write_markdown(args.output_dir / "move-date-inventory-2023-04-12.md", args.cutoff, movements, balances)

    print(f"wallets: {len(wallets)}")
    print(f"movement rows: {len(movements)}")
    print(f"nonzero balance rows: {sum(1 for b in balances if b.amount_raw != 0)}")
    print(f"output dir: {args.output_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
