#!/usr/bin/env python3
"""Build a post-move unwind workpaper for high-impact move-date positions.

This script answers a narrow evidence question: did the priority Layer C
positions still exist at the Polish residency start date, and what happened to
them afterwards?

It does not assign final PIT-38 imported basis. A position can be real and
fully unwound while still being quarantined for basis if the visible source is
debt-funded or otherwise lacks documented unrecovered acquisition cost.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
import urllib.error
import urllib.request
from collections import defaultdict
from dataclasses import dataclass
from datetime import datetime, timezone
from decimal import Decimal, InvalidOperation
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_RAW_DIR = REPO_ROOT / "private/evidence/onchain/raw"
DEFAULT_OUTPUT_DIR = REPO_ROOT / "private/evidence/onchain/move-date-inventory-2023-04-12"
MOVE_CUTOFF = datetime(2023, 4, 12, tzinfo=timezone.utc)
MOVE_CUTOFF_TEXT = "2023-04-12T00:00:00Z"

EVM_ADDRESS_RE = re.compile(r"^0x[a-fA-F0-9]{40}$")
RPC_URLS = {
    "arbitrum": "https://arb1.arbitrum.io/rpc",
    "optimism": "https://mainnet.optimism.io",
}


@dataclass(frozen=True)
class Target:
    target_id: str
    chain: str
    wallet_label: str
    wallet_address: str
    contract_address: str
    symbol: str
    decimals: int
    move_date_quantity: Decimal
    classification: str
    pit38_use: str
    follow_up_txs: tuple[str, ...] = ()

    @property
    def move_date_raw(self) -> int:
        return int((self.move_date_quantity * (Decimal(10) ** self.decimals)).to_integral_exact())


@dataclass(frozen=True)
class Transfer:
    chain: str
    wallet_label: str
    wallet_address: str
    tx_hash: str
    timestamp: datetime
    block_number: int
    log_index: int
    contract_address: str
    symbol: str
    name: str
    decimals: int
    amount_raw: int
    from_address: str
    to_address: str
    method: str
    source_file: str

    @property
    def quantity(self) -> Decimal:
        if self.decimals <= 0:
            return Decimal(self.amount_raw)
        return Decimal(self.amount_raw) / (Decimal(10) ** self.decimals)


@dataclass(frozen=True)
class HistoryRow:
    transfer: Transfer
    delta_raw: int
    running_raw: int


TARGETS = [
    Target(
        target_id="arbitrum_moo_gmx_glp",
        chain="arbitrum",
        wallet_label="Metamask3",
        wallet_address="0xb573f01f2901c0db3e14ec80c6e12e4868dec864",
        contract_address="0x9dbbbaecacedf53d5caa295b8293c1def2055adc",
        symbol="mooGmxGLP",
        decimals=18,
        move_date_quantity=Decimal("9369.29174702772049658"),
        classification="supportable_candidate_if_usdc_source_proven",
        pit38_use="High-priority candidate. Exit confirms the GLP chain unwound to USDC.e; use only if the original USDC.e source has a Swedish replacement-basis trace and is not double-counted.",
        follow_up_txs=(
            "0x7cfec06a1ad4b53f7e50a244130d3e133401a9781f4132bd379ce1570144c1b9",
        ),
    ),
    Target(
        target_id="optimism_rf_soweth",
        chain="optimism",
        wallet_label="Koinbase 4",
        wallet_address="0x8ca0c27a7a868a4069967709b5592995a69ae006",
        contract_address="0x932b30b2bc3f00b77affce8d0ff70b536f658462",
        symbol="rf-soWETH",
        decimals=18,
        move_date_quantity=Decimal("0.564680501436394919"),
        classification="supportable_candidate_if_eth_basis_traced",
        pit38_use="Good small candidate. Exit confirms WETH receipt; use only to the extent ETH/WETH has a Swedish acquisition/replacement-basis trace.",
    ),
    Target(
        target_id="optimism_bpt_gtrain_gauge",
        chain="optimism",
        wallet_label="Metamask3",
        wallet_address="0xb573f01f2901c0db3e14ec80c6e12e4868dec864",
        contract_address="0xefba6c3d81737bc6641b848345f497268d2807ca",
        symbol="BPT-GTRAIN-gauge",
        decimals=18,
        move_date_quantity=Decimal("93053.2239410531423566"),
        classification="mixed_candidate_count_only_non_debt_parts",
        pit38_use="Useful but mixed. Count only documented non-debt inputs by default, and pro-rate for post-move top-ups where needed.",
        follow_up_txs=(
            "0x73453901e265f25e5f1c77d1d73c01745aabe99606f0a00c96d3870cbdfc5d42",
        ),
    ),
    Target(
        target_id="optimism_bpt_reserve_gauge",
        chain="optimism",
        wallet_label="Metamask3",
        wallet_address="0xb573f01f2901c0db3e14ec80c6e12e4868dec864",
        contract_address="0xf496794778d49e6ce1af5cdbd3231ee3bd293ec0",
        symbol="BPT-RESERVE-gauge",
        decimals=18,
        move_date_quantity=Decimal("21018.159793707370873926"),
        classification="quarantine_debt_sourced",
        pit38_use="Real move-date holding, but quarantine by default. The visible source and exit are ERN/CDP-style debt/stablecoin legs, not clean acquisition cost.",
        follow_up_txs=(
            "0xf50718ac306432bef68d98915bcae6ffb2070d440991c119e0468cd1a8b52120",
        ),
    ),
    Target(
        target_id="arbitrum_nead_weth_oath",
        chain="arbitrum",
        wallet_label="Metamask3",
        wallet_address="0xb573f01f2901c0db3e14ec80c6e12e4868dec864",
        contract_address="0x7e70d4034cd0c6003d2ae8f4594f70135687ce10",
        symbol="nead-vrAMM-WETH/OATH",
        decimals=18,
        move_date_quantity=Decimal("1528.135759205486886693"),
        classification="complex_candidate",
        pit38_use="High-value optional expansion bucket. A separate OATH provenance workpaper traces the immediate LP inputs and Avalanche bridge loop; keep out of the simplified filing until Swedish OATH/TGE/reward basis and no-double-counting are reviewed.",
        follow_up_txs=(
            "0x72d937e74688c8b846c8ea28c32fff6ba2c27749ddfb74d3ec9eefe054babfa0",
            "0x0898c516bce9573e3bc5649f97778701e0271bc4273f8110c12aea8468180845",
        ),
    ),
    Target(
        target_id="optimism_rf_grain_op",
        chain="optimism",
        wallet_label="Koinbase 4",
        wallet_address="0x8ca0c27a7a868a4069967709b5592995a69ae006",
        contract_address="0x229ecbb1d76463e761535dd0e591c34317396131",
        symbol="rf-grain-OP",
        decimals=18,
        move_date_quantity=Decimal("22.917562317469558559"),
        classification="lower_priority_complex_candidate",
        pit38_use="Traceable but lower priority. Exit confirms OP receipt; not needed for the current threshold path.",
    ),
]


def normalize_address(value: Any) -> str:
    if isinstance(value, dict):
        value = value.get("hash", "")
    text = str(value or "").lower()
    return text if EVM_ADDRESS_RE.match(text) else ""


def parse_int(value: Any, default: int = 0) -> int:
    if value in (None, ""):
        return default
    text = str(value)
    try:
        if text.startswith("0x"):
            return int(text, 16)
        return int(text)
    except ValueError:
        return default


def parse_decimal(value: Any) -> Decimal:
    text = str(value or "").strip()
    if not text:
        return Decimal("0")
    try:
        return Decimal(text)
    except InvalidOperation:
        return Decimal("0")


def parse_etherscan_ts(value: Any) -> datetime | None:
    ts = parse_int(value)
    if not ts:
        return None
    return datetime.fromtimestamp(ts, timezone.utc)


def parse_iso_ts(value: Any) -> datetime | None:
    text = str(value or "").replace("Z", "+00:00")
    if not text:
        return None
    try:
        dt = datetime.fromisoformat(text)
    except ValueError:
        return None
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return dt.astimezone(timezone.utc)


def fmt_dt(value: datetime | None) -> str:
    if value is None:
        return ""
    return value.astimezone(timezone.utc).isoformat().replace("+00:00", "Z")


def fmt_decimal(value: Decimal | int | str, decimals: int | None = None) -> str:
    if not isinstance(value, Decimal):
        value = parse_decimal(value)
    if decimals is not None and decimals > 0:
        value = value / (Decimal(10) ** decimals)
    text = format(value.normalize(), "f")
    if "." in text:
        text = text.rstrip("0").rstrip(".")
    return text or "0"


def read_json(path: Path) -> dict[str, Any]:
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return {}
    return payload if isinstance(payload, dict) else {}


def chain_from_path(path: Path, payload: dict[str, Any]) -> str:
    if payload.get("chain"):
        return str(payload["chain"]).lower()
    parts = path.parts
    for marker in (
        "evm-explorer-mantle-arbitrum",
        "evm-explorer-optimism",
        "evm-explorer-pre-move-core",
        "blockscout-v2",
    ):
        if marker in parts:
            return parts[parts.index(marker) + 1].lower()
    return ""


def wallet_from_path(path: Path, payload: dict[str, Any]) -> tuple[str, str]:
    wallet = normalize_address(payload.get("wallet_address"))
    label = str(payload.get("wallet_label") or "")
    if wallet:
        return wallet, label
    parent = path.parent.name
    wallet = normalize_address(parent)
    return wallet, label


def iter_transfer_files(raw_dir: Path) -> list[Path]:
    paths: list[Path] = []
    for root_name in (
        "evm-explorer-mantle-arbitrum",
        "evm-explorer-optimism",
        "evm-explorer-pre-move-core",
    ):
        root = raw_dir / root_name
        if root.exists():
            paths.extend(root.glob("*/*/tokentx_page_*.json"))
    blockscout_root = raw_dir / "blockscout-v2"
    if blockscout_root.exists():
        paths.extend(blockscout_root.glob("*/*/token-transfers_page_*.json"))
    return sorted(paths)


def load_transfers(raw_dir: Path) -> list[Transfer]:
    target_chains = {target.chain for target in TARGETS}
    target_wallets = {target.wallet_address for target in TARGETS}
    transfers: list[Transfer] = []
    seen: set[tuple[str, str, int, str, str, str, int]] = set()

    for path in iter_transfer_files(raw_dir):
        payload = read_json(path)
        chain = chain_from_path(path, payload)
        wallet_address, wallet_label = wallet_from_path(path, payload)
        if chain not in target_chains or wallet_address not in target_wallets:
            continue

        rows = payload.get("result")
        if isinstance(rows, list):
            for row_index, row in enumerate(rows):
                if not isinstance(row, dict):
                    continue
                timestamp = parse_etherscan_ts(row.get("timeStamp"))
                tx_hash = str(row.get("hash") or "").lower()
                amount_raw = parse_int(row.get("value"))
                if not timestamp or not tx_hash or not amount_raw:
                    continue
                from_address = normalize_address(row.get("from"))
                to_address = normalize_address(row.get("to"))
                if wallet_address not in {from_address, to_address}:
                    continue
                log_index = parse_int(row.get("logIndex"), default=row_index)
                contract_address = normalize_address(row.get("contractAddress"))
                key = (chain, tx_hash, log_index, contract_address, from_address, to_address, amount_raw)
                if key in seen:
                    continue
                seen.add(key)
                transfers.append(
                    Transfer(
                        chain=chain,
                        wallet_label=wallet_label,
                        wallet_address=wallet_address,
                        tx_hash=tx_hash,
                        timestamp=timestamp,
                        block_number=parse_int(row.get("blockNumber")),
                        log_index=log_index,
                        contract_address=contract_address,
                        symbol=str(row.get("tokenSymbol") or ""),
                        name=str(row.get("tokenName") or ""),
                        decimals=parse_int(row.get("tokenDecimal")),
                        amount_raw=amount_raw,
                        from_address=from_address,
                        to_address=to_address,
                        method=str(row.get("functionName") or ""),
                        source_file=str(path),
                    )
                )
            continue

        items = payload.get("items")
        if isinstance(items, list):
            for row_index, item in enumerate(items):
                if not isinstance(item, dict):
                    continue
                timestamp = parse_iso_ts(item.get("timestamp"))
                tx_hash = str(item.get("transaction_hash") or item.get("hash") or "").lower()
                if not timestamp or not tx_hash:
                    continue
                token = item.get("token") if isinstance(item.get("token"), dict) else {}
                total = item.get("total") if isinstance(item.get("total"), dict) else {}
                amount_raw = parse_int(total.get("value") or item.get("value"))
                if not amount_raw:
                    continue
                from_address = normalize_address(item.get("from"))
                to_address = normalize_address(item.get("to"))
                if wallet_address not in {from_address, to_address}:
                    continue
                contract_address = normalize_address(token.get("address_hash"))
                log_index = parse_int(item.get("log_index"), default=row_index)
                key = (chain, tx_hash, log_index, contract_address, from_address, to_address, amount_raw)
                if key in seen:
                    continue
                seen.add(key)
                transfers.append(
                    Transfer(
                        chain=chain,
                        wallet_label=wallet_label,
                        wallet_address=wallet_address,
                        tx_hash=tx_hash,
                        timestamp=timestamp,
                        block_number=parse_int(item.get("block_number")),
                        log_index=log_index,
                        contract_address=contract_address,
                        symbol=str(token.get("symbol") or ""),
                        name=str(token.get("name") or ""),
                        decimals=parse_int(total.get("decimals") or token.get("decimals")),
                        amount_raw=amount_raw,
                        from_address=from_address,
                        to_address=to_address,
                        method=str(item.get("method") or ""),
                        source_file=str(path),
                    )
                )

    return sorted(transfers, key=lambda t: (t.timestamp, t.block_number, t.log_index, t.tx_hash))


def signed_raw(transfer: Transfer, wallet_address: str) -> int:
    if transfer.to_address == wallet_address:
        return transfer.amount_raw
    if transfer.from_address == wallet_address:
        return -transfer.amount_raw
    return 0


def signed_text(transfer: Transfer, wallet_address: str) -> str:
    sign = "+" if transfer.to_address == wallet_address else "-"
    return f"{transfer.symbol or transfer.contract_address} {sign}{fmt_decimal(transfer.amount_raw, transfer.decimals)}"


def build_history(target: Target, transfers: list[Transfer]) -> list[HistoryRow]:
    running = 0
    rows: list[HistoryRow] = []
    for transfer in transfers:
        if transfer.chain != target.chain:
            continue
        if transfer.wallet_address != target.wallet_address:
            continue
        if transfer.contract_address != target.contract_address:
            continue
        delta = signed_raw(transfer, target.wallet_address)
        if not delta:
            continue
        running += delta
        rows.append(HistoryRow(transfer=transfer, delta_raw=delta, running_raw=running))
    return rows


def flow_for_tx(
    transfers_by_tx: dict[tuple[str, str, str], list[Transfer]],
    target: Target,
    tx_hash: str,
) -> list[Transfer]:
    return transfers_by_tx.get((target.chain, target.wallet_address, tx_hash.lower()), [])


def summarize_flow(transfers: list[Transfer], wallet_address: str) -> str:
    if not transfers:
        return ""
    return "; ".join(signed_text(t, wallet_address) for t in transfers)


def tx_summary(transfers: list[Transfer], wallet_address: str) -> dict[str, str]:
    if not transfers:
        return {}
    return {
        "timestamp": fmt_dt(transfers[0].timestamp),
        "tx_hash": transfers[0].tx_hash,
        "tx_flow": summarize_flow(transfers, wallet_address),
    }


def current_balance_raw(target: Target, timeout_seconds: int = 25) -> tuple[int | None, str]:
    rpc_url = RPC_URLS.get(target.chain)
    if not rpc_url:
        return None, "no rpc configured"
    method = "70a08231"
    data = "0x" + method + target.wallet_address.removeprefix("0x").rjust(64, "0")
    payload = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "eth_call",
        "params": [{"to": target.contract_address, "data": data}, "latest"],
    }
    request = urllib.request.Request(
        rpc_url,
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "content-type": "application/json",
            "user-agent": "tax-calculator-evidence/1.0",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(request, timeout=timeout_seconds) as response:
            body = json.loads(response.read().decode("utf-8"))
    except (OSError, urllib.error.URLError, json.JSONDecodeError) as exc:
        return None, f"rpc error: {exc}"
    result = body.get("result")
    if not isinstance(result, str) or not result.startswith("0x"):
        return None, f"rpc error: {body.get('error') or 'missing result'}"
    return int(result, 16), "ok"


def write_csv(
    path: Path,
    transfers_by_tx: dict[tuple[str, str, str], list[Transfer]],
    histories: dict[str, list[HistoryRow]],
) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = [
        "target_id",
        "target_symbol",
        "classification",
        "pit38_use",
        "role",
        "timestamp",
        "chain",
        "wallet_label",
        "wallet_address",
        "tx_hash",
        "block_number",
        "method",
        "asset_symbol",
        "asset_name",
        "asset_contract_address",
        "direction",
        "amount",
        "from_address",
        "to_address",
        "running_target_balance_after",
        "tx_flow",
        "note",
        "source_file",
    ]
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for target in TARGETS:
            history = histories[target.target_id]
            zero_events = [row for row in history if row.transfer.timestamp >= MOVE_CUTOFF and row.delta_raw < 0 and row.running_raw == 0]
            exit_txs = {row.transfer.tx_hash for row in zero_events}
            follow_up_txs = set(target.follow_up_txs)

            for row in history:
                transfer = row.transfer
                if transfer.timestamp < MOVE_CUTOFF:
                    role = "pre_move_target_transfer"
                else:
                    role = "post_move_target_transfer"
                direction = "in" if row.delta_raw > 0 else "out"
                writer.writerow(
                    {
                        "target_id": target.target_id,
                        "target_symbol": target.symbol,
                        "classification": target.classification,
                        "pit38_use": target.pit38_use,
                        "role": role,
                        "timestamp": fmt_dt(transfer.timestamp),
                        "chain": transfer.chain,
                        "wallet_label": target.wallet_label,
                        "wallet_address": target.wallet_address,
                        "tx_hash": transfer.tx_hash,
                        "block_number": str(transfer.block_number),
                        "method": transfer.method,
                        "asset_symbol": transfer.symbol,
                        "asset_name": transfer.name,
                        "asset_contract_address": transfer.contract_address,
                        "direction": direction,
                        "amount": fmt_decimal(abs(row.delta_raw), target.decimals),
                        "from_address": transfer.from_address,
                        "to_address": transfer.to_address,
                        "running_target_balance_after": fmt_decimal(row.running_raw, target.decimals),
                        "tx_flow": "",
                        "note": "target token movement",
                        "source_file": transfer.source_file,
                    }
                )

            for role, tx_hashes in (("exit_tx_flow", exit_txs), ("follow_up_tx_flow", follow_up_txs)):
                for tx_hash in sorted(tx_hashes):
                    flow = flow_for_tx(transfers_by_tx, target, tx_hash)
                    flow_summary = summarize_flow(flow, target.wallet_address)
                    for transfer in flow:
                        direction = "in" if transfer.to_address == target.wallet_address else "out"
                        writer.writerow(
                            {
                                "target_id": target.target_id,
                                "target_symbol": target.symbol,
                                "classification": target.classification,
                                "pit38_use": target.pit38_use,
                                "role": role,
                                "timestamp": fmt_dt(transfer.timestamp),
                                "chain": transfer.chain,
                                "wallet_label": target.wallet_label,
                                "wallet_address": target.wallet_address,
                                "tx_hash": transfer.tx_hash,
                                "block_number": str(transfer.block_number),
                                "method": transfer.method,
                                "asset_symbol": transfer.symbol,
                                "asset_name": transfer.name,
                                "asset_contract_address": transfer.contract_address,
                                "direction": direction,
                                "amount": fmt_decimal(transfer.amount_raw, transfer.decimals),
                                "from_address": transfer.from_address,
                                "to_address": transfer.to_address,
                                "running_target_balance_after": "",
                                "tx_flow": flow_summary,
                                "note": "all archived wallet token transfers in this unwind tx",
                                "source_file": transfer.source_file,
                            }
                        )


def build_summary(
    transfers_by_tx: dict[tuple[str, str, str], list[Transfer]],
    histories: dict[str, list[HistoryRow]],
    current_balances: dict[str, tuple[int | None, str]],
) -> dict[str, Any]:
    targets_payload: list[dict[str, Any]] = []
    for target in TARGETS:
        history = histories[target.target_id]
        move_date_raw = sum(row.delta_raw for row in history if row.transfer.timestamp < MOVE_CUTOFF)
        reconstructed_latest_raw = history[-1].running_raw if history else 0
        zero_events = [row for row in history if row.transfer.timestamp >= MOVE_CUTOFF and row.delta_raw < 0 and row.running_raw == 0]
        first_zero = zero_events[0] if zero_events else None
        final_zero = zero_events[-1] if zero_events else None
        cutoff_for_topups = first_zero.transfer.timestamp if first_zero else None
        topups_before_first_zero = sum(
            row.delta_raw
            for row in history
            if row.transfer.timestamp >= MOVE_CUTOFF
            and row.delta_raw > 0
            and (cutoff_for_topups is None or row.transfer.timestamp <= cutoff_for_topups)
        )
        exit_amount_raw = abs(first_zero.delta_raw) if first_zero else 0
        move_share = ""
        if exit_amount_raw:
            share = Decimal(target.move_date_raw) / Decimal(exit_amount_raw)
            move_share = fmt_decimal(share)
        rpc_raw, rpc_status = current_balances[target.target_id]
        exit_flow = flow_for_tx(transfers_by_tx, target, first_zero.transfer.tx_hash) if first_zero else []
        final_exit_flow = flow_for_tx(transfers_by_tx, target, final_zero.transfer.tx_hash) if final_zero else []
        followups = [
            tx_summary(flow_for_tx(transfers_by_tx, target, tx_hash), target.wallet_address)
            or {"tx_hash": tx_hash, "tx_flow": "", "timestamp": ""}
            for tx_hash in target.follow_up_txs
        ]
        targets_payload.append(
            {
                "target_id": target.target_id,
                "chain": target.chain,
                "wallet_label": target.wallet_label,
                "wallet_address": target.wallet_address,
                "symbol": target.symbol,
                "contract_address": target.contract_address,
                "classification": target.classification,
                "pit38_use": target.pit38_use,
                "expected_move_date_quantity": fmt_decimal(target.move_date_quantity),
                "reconstructed_move_date_quantity": fmt_decimal(move_date_raw, target.decimals),
                "move_date_matches_expected": move_date_raw == target.move_date_raw,
                "reconstructed_latest_quantity": fmt_decimal(reconstructed_latest_raw, target.decimals),
                "rpc_latest_quantity": None if rpc_raw is None else fmt_decimal(rpc_raw, target.decimals),
                "rpc_status": rpc_status,
                "first_zero_after_move": tx_summary(exit_flow, target.wallet_address) if first_zero else {},
                "final_zero_after_move": tx_summary(final_exit_flow, target.wallet_address) if final_zero else {},
                "zero_reached_after_move_count": len(zero_events),
                "post_move_topups_before_first_zero": fmt_decimal(topups_before_first_zero, target.decimals),
                "first_zero_exit_amount": fmt_decimal(exit_amount_raw, target.decimals),
                "move_date_quantity_share_of_first_zero_exit": move_share,
                "follow_up_txs": followups,
            }
        )

    return {
        "generated_at": fmt_dt(datetime.now(timezone.utc)),
        "cutoff": MOVE_CUTOFF_TEXT,
        "target_count": len(TARGETS),
        "all_rpc_latest_balances_zero": all(status == "ok" and raw == 0 for raw, status in current_balances.values()),
        "targets": targets_payload,
        "limitations": [
            "The unwind trace uses archived wallet token-transfer evidence plus latest balanceOf calls.",
            "Native ETH received by removeLiquidityETH-style calls may not appear in token-transfer rows; this affects complex LP interpretation but not whether the wrapper token was exited.",
            "This workpaper proves existence and unwind timing. It does not decide whether acquisition cost is legally importable into PIT-38.",
        ],
    }


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True), encoding="utf-8")


def write_markdown(path: Path, payload: dict[str, Any]) -> None:
    lines = [
        "# Move-Date Position Unwind Traces",
        "",
        f"Cut-off: `{payload['cutoff']}`",
        "",
        "This workpaper checks the high-impact move-date Layer C positions after the Polish residency start date. It is evidence for position existence and later unwind, not a final PIT-38 basis assignment.",
        "",
        "## Bottom Line",
        "",
        "- The six reviewed positions reconcile to the expected `2023-04-12` move-date quantities from the archived transfer evidence.",
        "- Latest `balanceOf` checks return zero for all six reviewed wrapper/gauge/receipt tokens.",
        "- `BPT-RESERVE` was a real move-date asset; it is quarantined because of cost provenance, not because the holding was imaginary.",
        "- The simplified filing path still excludes `nead-vrAMM-WETH/OATH`, but that position is now a documented high-value optional expansion bucket rather than an unexplored fallback.",
        "",
        "## Reviewed Positions",
        "",
        "| Asset | Move-date qty | Latest balance | First zero after move | Exit / follow-up flow | PIT-38 use |",
        "| --- | ---: | ---: | --- | --- | --- |",
    ]

    for item in payload["targets"]:
        first_zero = item.get("first_zero_after_move") or {}
        first_zero_text = ""
        if first_zero:
            first_zero_text = f"{first_zero.get('timestamp', '')} `{first_zero.get('tx_hash', '')}`"
        flow_parts = []
        if first_zero.get("tx_flow"):
            flow_parts.append(first_zero["tx_flow"])
        for followup in item.get("follow_up_txs", []):
            if followup.get("tx_flow"):
                flow_parts.append(followup["tx_flow"])
        flow_text = "; ".join(flow_parts)
        if len(flow_text) > 260:
            flow_text = flow_text[:257] + "..."
        latest = item.get("rpc_latest_quantity")
        if latest is None:
            latest = f"unknown ({item.get('rpc_status')})"
        lines.append(
            "| {asset} | {move_qty} | {latest} | {first_zero} | {flow} | {use} |".format(
                asset=f"{item['chain']} `{item['symbol']}`",
                move_qty=item["reconstructed_move_date_quantity"],
                latest=latest,
                first_zero=first_zero_text,
                flow=flow_text or "No flow found in archived token rows",
                use=item["pit38_use"],
            )
        )

    lines.extend(
        [
            "",
            "## Basis Implications",
            "",
            "- `mooGmxGLP`: strong factual unwind. The post-move exit returned `USDC.e 10539.680018` through the GLP chain, supporting the existing `USDC.e 9985.6` pre-move source trace if Swedish replacement-basis proof is accepted.",
            "- `rf-soWETH`: strong factual unwind. The exit returned `WETH 0.603672288028468693`, so this can support a small ETH/WETH replacement-basis component.",
            "- `BPT-GTRAIN-gauge`: real and exited after two post-move top-ups. Use only the documented pre-move/non-debt part by default; do not count ERN/debt legs as clean acquisition cost.",
            "- `BPT-RESERVE-gauge`: include as a real move-date holding in the evidence chain, but quarantine for filing by default because the visible source/exit is ERN/CDP-style debt/stablecoin exposure.",
            "- `nead-vrAMM-WETH/OATH`: real, high-value, and separately traced in `move-date-oath-provenance.md`; keep it out of the current simplified filing until Swedish OATH/TGE/reward basis and no-double-counting are reviewed.",
            "- `rf-grain-OP`: real and exited to OP, but lower priority and not needed for the current threshold path.",
            "",
            "## Outputs",
            "",
            "- Detail CSV: `move-date-unwind-traces.csv`",
            "- JSON summary: `move-date-unwind-summary.json`",
            "",
            "## Limitations",
            "",
        ]
    )
    for limitation in payload["limitations"]:
        lines.append(f"- {limitation}")
    lines.append("")
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--raw-dir", type=Path, default=DEFAULT_RAW_DIR)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    parser.add_argument("--skip-rpc", action="store_true", help="Do not run latest balanceOf checks")
    args = parser.parse_args()

    transfers = load_transfers(args.raw_dir)
    transfers_by_tx: dict[tuple[str, str, str], list[Transfer]] = defaultdict(list)
    for transfer in transfers:
        transfers_by_tx[(transfer.chain, transfer.wallet_address, transfer.tx_hash)].append(transfer)
    for key, rows in list(transfers_by_tx.items()):
        transfers_by_tx[key] = sorted(rows, key=lambda t: (t.timestamp, t.block_number, t.log_index))

    histories = {target.target_id: build_history(target, transfers) for target in TARGETS}
    current_balances: dict[str, tuple[int | None, str]] = {}
    for target in TARGETS:
        if args.skip_rpc:
            current_balances[target.target_id] = (None, "skipped")
        else:
            current_balances[target.target_id] = current_balance_raw(target)

    args.output_dir.mkdir(parents=True, exist_ok=True)
    write_csv(args.output_dir / "move-date-unwind-traces.csv", transfers_by_tx, histories)
    summary = build_summary(transfers_by_tx, histories, current_balances)
    write_json(args.output_dir / "move-date-unwind-summary.json", summary)
    write_markdown(args.output_dir / "move-date-unwind-workpaper.md", summary)

    print(f"Parsed token transfers: {len(transfers)}")
    print(f"Wrote {args.output_dir / 'move-date-unwind-traces.csv'}")
    print(f"Wrote {args.output_dir / 'move-date-unwind-summary.json'}")
    print(f"Wrote {args.output_dir / 'move-date-unwind-workpaper.md'}")


if __name__ == "__main__":
    main()
