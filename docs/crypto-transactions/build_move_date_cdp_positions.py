#!/usr/bin/env python3
"""Build a move-date CDP protocol-state workpaper.

The transfer-derived move-date inventory can miss collateral locked inside a
borrowing protocol when the protocol does not mint a wallet-held receipt token.
This script queries the Optimism Ethos Reserve trove state at the Polish
residency start cut-off and compares every collateral type visible in the
wallet's BorrowerOperations history.
"""

from __future__ import annotations

import argparse
import csv
import json
import urllib.error
import urllib.request
from collections import defaultdict
from dataclasses import dataclass, field
from datetime import datetime, timezone
from decimal import Decimal
from pathlib import Path
from typing import Any

from eth_hash.auto import keccak


REPO_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_RAW_DIR = (
    REPO_ROOT
    / "private/evidence/onchain/raw/blockscout-v2/optimism/0xb573f01f2901c0db3e14ec80c6e12e4868dec864"
)
DEFAULT_OUTPUT_DIR = REPO_ROOT / "private/evidence/onchain/move-date-inventory-2023-04-12"

RPC_URL = "https://mainnet.optimism.io"
MOVE_BLOCK = 89_200_417
MOVE_CUTOFF = datetime(2023, 4, 12, tzinfo=timezone.utc)
MOVE_CUTOFF_TEXT = "2023-04-12T00:00:00Z"
MOVE_BLOCK_TIMESTAMP = "2023-04-11T23:59:55Z"

CHAIN = "optimism"
WALLET_LABEL = "Metamask3"
WALLET_ADDRESS = "0xb573f01f2901c0db3e14ec80c6e12e4868dec864"
BORROWER_OPERATIONS = "0x0a4582d3d9ecbab80a66dad8a881be3b771d3e5b"
FALLBACK_TROVE_MANAGER = "0xd584a5e956106db2fe74d56a0b14a9d64be8dc93"
PROTOCOL = "Ethos Reserve"
DEBT_SYMBOL = "ERN"
DEBT_DECIMALS = 18

COLLATERALS = {
    "0x4200000000000000000000000000000000000006": ("WETH", 18),
    "0x68f180fcce6836688e9084f035309e29bf0a2095": ("WBTC", 8),
}

STATUS_TEXT = {
    0: "non_existent",
    1: "active",
    2: "closed_by_owner",
    3: "closed_by_liquidation",
    4: "closed_by_redemption",
}


@dataclass
class TroveOperation:
    timestamp: datetime
    block_number: int
    tx_hash: str
    status: str
    method: str
    collateral_address: str
    collateral_top_up_raw: int = 0
    collateral_withdrawal_raw: int = 0
    debt_increase_raw: int = 0
    debt_repayment_raw: int = 0
    source_file: str = ""


@dataclass
class CollateralSummary:
    collateral_address: str
    symbol: str
    decimals: int
    operations: list[TroveOperation] = field(default_factory=list)
    move_status: int = 0
    move_collateral_raw: int = 0
    move_debt_raw: int = 0
    move_entire_debt_raw: int = 0
    move_entire_collateral_raw: int = 0
    move_pending_debt_reward_raw: int = 0
    move_pending_collateral_reward_raw: int = 0
    latest_status: int = 0


def normalize_address(value: Any) -> str:
    if isinstance(value, dict):
        value = value.get("hash", "")
    text = str(value or "").lower()
    if text.startswith("0x") and len(text) == 42:
        return text
    return ""


def parse_int(value: Any) -> int:
    if value in (None, ""):
        return 0
    text = str(value)
    if text.startswith("0x"):
        return int(text, 16)
    return int(text)


def parse_bool(value: Any) -> bool:
    return str(value).strip().lower() == "true"


def parse_ts(value: Any) -> datetime:
    text = str(value or "").replace("Z", "+00:00")
    return datetime.fromisoformat(text).astimezone(timezone.utc)


def fmt_dt(value: datetime | None) -> str:
    if value is None:
        return ""
    return value.astimezone(timezone.utc).isoformat().replace("+00:00", "Z")


def fmt_decimal_raw(value: int, decimals: int) -> str:
    amount = Decimal(value) / (Decimal(10) ** decimals)
    text = format(amount.normalize(), "f")
    if "." in text:
        text = text.rstrip("0").rstrip(".")
    return text or "0"


def calldata(signature: str, args: list[tuple[str, str]] | None = None) -> str:
    data = keccak(signature.encode("utf-8")).hex()[:8]
    for arg_type, value in args or []:
        if arg_type != "address":
            raise ValueError(f"unsupported ABI argument type: {arg_type}")
        data += value.lower().removeprefix("0x").rjust(64, "0")
    return "0x" + data


def rpc_call(to_address: str, data: str, block: int | str, timeout_seconds: int = 30) -> str:
    block_param = hex(block) if isinstance(block, int) else block
    payload = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "eth_call",
        "params": [{"to": to_address, "data": data}, block_param],
    }
    request = urllib.request.Request(
        RPC_URL,
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "content-type": "application/json",
            "user-agent": "tax-calculator-evidence/1.0",
        },
        method="POST",
    )
    with urllib.request.urlopen(request, timeout=timeout_seconds) as response:
        body = json.loads(response.read().decode("utf-8"))
    if "error" in body:
        raise RuntimeError(body["error"])
    result = body.get("result")
    if not isinstance(result, str) or not result.startswith("0x"):
        raise RuntimeError(f"missing RPC result: {body}")
    return result


def decode_uints(hex_data: str) -> list[int]:
    text = hex_data.removeprefix("0x")
    return [int(text[index : index + 64], 16) for index in range(0, len(text), 64) if text[index : index + 64]]


def decode_address(hex_data: str) -> str:
    text = hex_data.removeprefix("0x")
    if len(text) < 64:
        return ""
    return "0x" + text[-40:].lower()


def get_trove_manager(move_block: int) -> tuple[str, str]:
    try:
        result = rpc_call(BORROWER_OPERATIONS, calldata("troveManager()"), move_block)
    except (OSError, urllib.error.URLError, RuntimeError) as exc:
        return FALLBACK_TROVE_MANAGER, f"fallback used after RPC error: {exc}"
    address = decode_address(result)
    if not address:
        return FALLBACK_TROVE_MANAGER, "fallback used after empty troveManager() result"
    return address, "queried from BorrowerOperations.troveManager() at move block"


def decoded_params(tx: dict[str, Any]) -> dict[str, Any]:
    decoded = tx.get("decoded_input") if isinstance(tx.get("decoded_input"), dict) else {}
    params = decoded.get("parameters") if isinstance(decoded.get("parameters"), list) else []
    return {str(param.get("name")): param.get("value") for param in params if isinstance(param, dict)}


def load_operations(raw_dir: Path) -> list[TroveOperation]:
    operations: list[TroveOperation] = []
    for path in sorted(raw_dir.glob("transactions_page_*.json")):
        payload = json.loads(path.read_text(encoding="utf-8"))
        for tx in payload.get("items", []):
            if not isinstance(tx, dict):
                continue
            method = str(tx.get("method") or "")
            if method not in {"openTrove", "adjustTrove", "closeTrove"}:
                continue
            params = decoded_params(tx)
            collateral_address = normalize_address(params.get("_collateral"))
            if not collateral_address:
                continue

            collateral_top_up = 0
            collateral_withdrawal = 0
            debt_increase = 0
            debt_repayment = 0

            if method == "openTrove":
                collateral_top_up = parse_int(params.get("_collAmount"))
                debt_increase = parse_int(params.get("_LUSDAmount"))
            elif method == "adjustTrove":
                collateral_top_up = parse_int(params.get("_collTopUp"))
                collateral_withdrawal = parse_int(params.get("_collWithdrawal"))
                debt_change = parse_int(params.get("_LUSDChange"))
                if parse_bool(params.get("_isDebtIncrease")):
                    debt_increase = debt_change
                else:
                    debt_repayment = debt_change

            operations.append(
                TroveOperation(
                    timestamp=parse_ts(tx.get("timestamp")),
                    block_number=parse_int(tx.get("block_number") or tx.get("block")),
                    tx_hash=str(tx.get("hash") or "").lower(),
                    status=str(tx.get("status") or ""),
                    method=method,
                    collateral_address=collateral_address,
                    collateral_top_up_raw=collateral_top_up,
                    collateral_withdrawal_raw=collateral_withdrawal,
                    debt_increase_raw=debt_increase,
                    debt_repayment_raw=debt_repayment,
                    source_file=str(path),
                )
            )
    return sorted(operations, key=lambda op: (op.timestamp, op.block_number, op.tx_hash))


def query_collateral_state(
    collateral_address: str,
    symbol: str,
    decimals: int,
    trove_manager: str,
    move_block: int,
) -> tuple[int, int, int, int, int, int, int, int]:
    args = [("address", WALLET_ADDRESS), ("address", collateral_address)]
    move_status = decode_uints(rpc_call(trove_manager, calldata("getTroveStatus(address,address)", args), move_block))[0]
    move_collateral = decode_uints(rpc_call(trove_manager, calldata("getTroveColl(address,address)", args), move_block))[0]
    move_debt = decode_uints(rpc_call(trove_manager, calldata("getTroveDebt(address,address)", args), move_block))[0]
    entire = decode_uints(rpc_call(trove_manager, calldata("getEntireDebtAndColl(address,address)", args), move_block))
    latest_status = decode_uints(rpc_call(trove_manager, calldata("getTroveStatus(address,address)", args), "latest"))[0]
    while len(entire) < 4:
        entire.append(0)
    return (
        move_status,
        move_collateral,
        move_debt,
        entire[0],
        entire[1],
        entire[2],
        entire[3],
        latest_status,
    )


def build_summaries(operations: list[TroveOperation], trove_manager: str, move_block: int) -> list[CollateralSummary]:
    collaterals = set(COLLATERALS)
    collaterals.update(op.collateral_address for op in operations)
    grouped: dict[str, list[TroveOperation]] = defaultdict(list)
    for operation in operations:
        grouped[operation.collateral_address].append(operation)

    summaries: list[CollateralSummary] = []
    for collateral_address in sorted(collaterals):
        symbol, decimals = COLLATERALS.get(collateral_address, (collateral_address, 18))
        summary = CollateralSummary(
            collateral_address=collateral_address,
            symbol=symbol,
            decimals=decimals,
            operations=grouped.get(collateral_address, []),
        )
        (
            summary.move_status,
            summary.move_collateral_raw,
            summary.move_debt_raw,
            summary.move_entire_debt_raw,
            summary.move_entire_collateral_raw,
            summary.move_pending_debt_reward_raw,
            summary.move_pending_collateral_reward_raw,
            summary.latest_status,
        ) = query_collateral_state(collateral_address, symbol, decimals, trove_manager, move_block)
        summaries.append(summary)
    return summaries


def summarize_operations(summary: CollateralSummary) -> dict[str, Any]:
    ok_ops = [op for op in summary.operations if op.status == "ok"]
    ok_pre_move = [op for op in ok_ops if op.timestamp < MOVE_CUTOFF]
    ok_post_move = [op for op in ok_ops if op.timestamp >= MOVE_CUTOFF]
    all_pre_move = [op for op in summary.operations if op.timestamp < MOVE_CUTOFF]
    return {
        "first_seen": fmt_dt(summary.operations[0].timestamp) if summary.operations else "",
        "last_seen": fmt_dt(summary.operations[-1].timestamp) if summary.operations else "",
        "first_success": fmt_dt(ok_ops[0].timestamp) if ok_ops else "",
        "first_success_after_move": fmt_dt(ok_post_move[0].timestamp) if ok_post_move else "",
        "total_calls": len(summary.operations),
        "successful_calls": len(ok_ops),
        "failed_calls": len([op for op in summary.operations if op.status != "ok"]),
        "successful_pre_move_calls": len(ok_pre_move),
        "all_pre_move_calls": len(all_pre_move),
        "pre_move_collateral_top_up_raw": sum(op.collateral_top_up_raw for op in ok_pre_move),
        "pre_move_collateral_withdrawal_raw": sum(op.collateral_withdrawal_raw for op in ok_pre_move),
        "pre_move_debt_increase_raw": sum(op.debt_increase_raw for op in ok_pre_move),
        "pre_move_debt_repayment_raw": sum(op.debt_repayment_raw for op in ok_pre_move),
    }


def summary_row(summary: CollateralSummary, trove_manager: str, trove_manager_source: str) -> dict[str, str]:
    ops = summarize_operations(summary)
    note = ""
    if summary.symbol == "WBTC" and summary.move_status == 1:
        note = (
            "Active move-date protocol-state collateral. This is not represented by the wallet token balance rows; "
            "it must be considered separately from ERN-funded LP/gauge positions to avoid double-counting debt proceeds."
        )
    elif summary.symbol == "WETH" and summary.move_collateral_raw == 0:
        note = "No WETH trove existed at the move date. WETH collateral activity starts after Polish residency began."
    else:
        note = "Review protocol state before using in any PIT-38 imported-basis calculation."

    return {
        "chain": CHAIN,
        "wallet_label": WALLET_LABEL,
        "wallet_address": WALLET_ADDRESS,
        "protocol": PROTOCOL,
        "borrower_operations": BORROWER_OPERATIONS,
        "trove_manager": trove_manager,
        "trove_manager_source": trove_manager_source,
        "move_cutoff": MOVE_CUTOFF_TEXT,
        "move_block": str(MOVE_BLOCK),
        "move_block_timestamp": MOVE_BLOCK_TIMESTAMP,
        "collateral_symbol": summary.symbol,
        "collateral_address": summary.collateral_address,
        "collateral_decimals": str(summary.decimals),
        "move_status": str(summary.move_status),
        "move_status_text": STATUS_TEXT.get(summary.move_status, "unknown"),
        "move_collateral_raw": str(summary.move_collateral_raw),
        "move_collateral_quantity": fmt_decimal_raw(summary.move_collateral_raw, summary.decimals),
        "move_debt_raw": str(summary.move_debt_raw),
        "move_debt_ern": fmt_decimal_raw(summary.move_debt_raw, DEBT_DECIMALS),
        "move_entire_debt_raw": str(summary.move_entire_debt_raw),
        "move_entire_debt_ern": fmt_decimal_raw(summary.move_entire_debt_raw, DEBT_DECIMALS),
        "move_entire_collateral_raw": str(summary.move_entire_collateral_raw),
        "move_entire_collateral_quantity": fmt_decimal_raw(summary.move_entire_collateral_raw, summary.decimals),
        "move_pending_debt_reward_raw": str(summary.move_pending_debt_reward_raw),
        "move_pending_collateral_reward_raw": str(summary.move_pending_collateral_reward_raw),
        "latest_status": str(summary.latest_status),
        "latest_status_text": STATUS_TEXT.get(summary.latest_status, "unknown"),
        "first_seen": ops["first_seen"],
        "last_seen": ops["last_seen"],
        "first_success": ops["first_success"],
        "first_success_after_move": ops["first_success_after_move"],
        "total_calls": str(ops["total_calls"]),
        "successful_calls": str(ops["successful_calls"]),
        "failed_calls": str(ops["failed_calls"]),
        "successful_pre_move_calls": str(ops["successful_pre_move_calls"]),
        "all_pre_move_calls": str(ops["all_pre_move_calls"]),
        "pre_move_collateral_top_up_quantity": fmt_decimal_raw(ops["pre_move_collateral_top_up_raw"], summary.decimals),
        "pre_move_collateral_withdrawal_quantity": fmt_decimal_raw(
            ops["pre_move_collateral_withdrawal_raw"], summary.decimals
        ),
        "pre_move_debt_increase_ern": fmt_decimal_raw(ops["pre_move_debt_increase_raw"], DEBT_DECIMALS),
        "pre_move_debt_repayment_ern": fmt_decimal_raw(ops["pre_move_debt_repayment_raw"], DEBT_DECIMALS),
        "note": note,
    }


def write_summary_csv(path: Path, summaries: list[CollateralSummary], trove_manager: str, trove_manager_source: str) -> None:
    rows = [summary_row(summary, trove_manager, trove_manager_source) for summary in summaries]
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def write_transactions_csv(path: Path, summaries: list[CollateralSummary]) -> None:
    fieldnames = [
        "timestamp",
        "block_number",
        "chain",
        "wallet_label",
        "wallet_address",
        "protocol",
        "tx_hash",
        "status",
        "method",
        "collateral_symbol",
        "collateral_address",
        "collateral_top_up",
        "collateral_withdrawal",
        "debt_increase_ern",
        "debt_repayment_ern",
        "relative_to_move",
        "source_file",
    ]
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for summary in summaries:
            for operation in summary.operations:
                writer.writerow(
                    {
                        "timestamp": fmt_dt(operation.timestamp),
                        "block_number": str(operation.block_number),
                        "chain": CHAIN,
                        "wallet_label": WALLET_LABEL,
                        "wallet_address": WALLET_ADDRESS,
                        "protocol": PROTOCOL,
                        "tx_hash": operation.tx_hash,
                        "status": operation.status,
                        "method": operation.method,
                        "collateral_symbol": summary.symbol,
                        "collateral_address": summary.collateral_address,
                        "collateral_top_up": fmt_decimal_raw(operation.collateral_top_up_raw, summary.decimals),
                        "collateral_withdrawal": fmt_decimal_raw(operation.collateral_withdrawal_raw, summary.decimals),
                        "debt_increase_ern": fmt_decimal_raw(operation.debt_increase_raw, DEBT_DECIMALS),
                        "debt_repayment_ern": fmt_decimal_raw(operation.debt_repayment_raw, DEBT_DECIMALS),
                        "relative_to_move": "pre_move" if operation.timestamp < MOVE_CUTOFF else "post_move",
                        "source_file": operation.source_file,
                    }
                )


def build_json_payload(
    summaries: list[CollateralSummary],
    trove_manager: str,
    trove_manager_source: str,
) -> dict[str, Any]:
    transactions: list[dict[str, str]] = []
    for summary in summaries:
        for operation in summary.operations:
            transactions.append(
                {
                    "timestamp": fmt_dt(operation.timestamp),
                    "block_number": str(operation.block_number),
                    "tx_hash": operation.tx_hash,
                    "status": operation.status,
                    "method": operation.method,
                    "collateral_symbol": summary.symbol,
                    "collateral_address": summary.collateral_address,
                    "collateral_top_up": fmt_decimal_raw(operation.collateral_top_up_raw, summary.decimals),
                    "collateral_withdrawal": fmt_decimal_raw(operation.collateral_withdrawal_raw, summary.decimals),
                    "debt_increase_ern": fmt_decimal_raw(operation.debt_increase_raw, DEBT_DECIMALS),
                    "debt_repayment_ern": fmt_decimal_raw(operation.debt_repayment_raw, DEBT_DECIMALS),
                    "relative_to_move": "pre_move" if operation.timestamp < MOVE_CUTOFF else "post_move",
                }
            )
    return {
        "generated_at": fmt_dt(datetime.now(timezone.utc)),
        "chain": CHAIN,
        "wallet_label": WALLET_LABEL,
        "wallet_address": WALLET_ADDRESS,
        "protocol": PROTOCOL,
        "borrower_operations": BORROWER_OPERATIONS,
        "trove_manager": trove_manager,
        "trove_manager_source": trove_manager_source,
        "move_cutoff": MOVE_CUTOFF_TEXT,
        "move_block": MOVE_BLOCK,
        "move_block_timestamp": MOVE_BLOCK_TIMESTAMP,
        "debt_symbol": DEBT_SYMBOL,
        "collaterals": [summary_row(summary, trove_manager, trove_manager_source) for summary in summaries],
        "transactions": transactions,
        "limitations": [
            "This is protocol state, not token-transfer state. It must be merged conceptually with the move-date inventory.",
            "ERN borrowed from the CDP is debt proceeds. Do not count both borrowed ERN-funded LPs and the underlying WBTC collateral as independent imported cost.",
            "The protocol debt at the block can differ from the sum of visible borrow inputs because it includes protocol accounting such as fees/reserves.",
        ],
    }


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True), encoding="utf-8")


def write_markdown(path: Path, payload: dict[str, Any]) -> None:
    rows = payload["collaterals"]
    active_rows = [row for row in rows if row["move_status"] == "1" and row["move_collateral_raw"] != "0"]
    lines = [
        "# Move-Date CDP Protocol Positions",
        "",
        f"Cut-off: `{payload['move_cutoff']}`",
        f"Optimism block: `{payload['move_block']}` (`{payload['move_block_timestamp']}`)",
        "",
        "This workpaper answers whether the move-date inventory counted collateral locked inside the Optimism Ethos Reserve CDP. The transfer-derived inventory does not see this kind of protocol-internal collateral unless a wallet-held receipt token exists.",
        "",
        "## Bottom Line",
        "",
    ]
    if active_rows:
        active = active_rows[0]
        lines.extend(
            [
                f"- At the move-date block, the active Ethos trove collateral is `{active['move_collateral_quantity']} {active['collateral_symbol']}` with protocol debt `{active['move_debt_ern']} ERN`.",
                "- The WETH collateral path is not active at the move date. WETH trove activity starts after Polish residency began.",
                "- The prior wallet-token inventory therefore missed the main CDP collateral position. It counted wallet-visible LP/gauge tokens, but not the locked trove collateral itself.",
                "- For PIT-38 basis, treat the locked collateral as the asset-position evidence. ERN borrowed against it is a liability/debt-proceeds leg, not a second independent acquisition cost.",
            ]
        )
    else:
        lines.append("- No active Ethos collateral was found at the move-date block.")
    lines.extend(
        [
            "",
            "## Collateral State",
            "",
            "| Collateral | Move status | Move collateral | Move debt | First successful call | First success after move | Pre-move successful calls |",
            "| --- | --- | ---: | ---: | --- | --- | ---: |",
        ]
    )
    for row in rows:
        lines.append(
            "| {symbol} | {status} | {coll} | {debt} ERN | {first} | {first_after} | {count} |".format(
                symbol=f"`{row['collateral_symbol']}`",
                status=row["move_status_text"],
                coll=row["move_collateral_quantity"],
                debt=row["move_debt_ern"],
                first=row["first_success"] or "",
                first_after=row["first_success_after_move"] or "",
                count=row["successful_pre_move_calls"],
            )
        )

    lines.extend(
        [
            "",
            "## Pre-Move WBTC Trove Inputs",
            "",
            "| Date | Method | Collateral top-up | Collateral withdrawal | Debt increase | Debt repayment | Tx |",
            "| --- | --- | ---: | ---: | ---: | ---: | --- |",
        ]
    )
    for tx in payload.get("transactions", []):
        if tx.get("collateral_symbol") != "WBTC" or tx.get("relative_to_move") != "pre_move" or tx.get("status") != "ok":
            continue
        lines.append(
            "| {date} | {method} | {top_up} | {withdrawal} | {debt_inc} | {debt_repay} | `{tx_hash}` |".format(
                date=tx["timestamp"],
                method=tx["method"],
                top_up=tx["collateral_top_up"],
                withdrawal=tx["collateral_withdrawal"],
                debt_inc=tx["debt_increase_ern"],
                debt_repay=tx["debt_repayment_ern"],
                tx_hash=tx["tx_hash"],
            )
        )

    lines.extend(
        [
            "",
            "The generated `move-date-cdp-transactions.csv` contains each `openTrove`, `adjustTrove`, and `closeTrove` call. The successful pre-move WBTC inputs sum to:",
            f"- Collateral top-up: `{next((r['pre_move_collateral_top_up_quantity'] for r in rows if r['collateral_symbol'] == 'WBTC'), '0')} WBTC`",
            f"- Borrow input: `{next((r['pre_move_debt_increase_ern'] for r in rows if r['collateral_symbol'] == 'WBTC'), '0')} ERN`",
            "",
            "The protocol debt at the move block is higher than the raw borrow input total, so use the queried protocol debt for liability state and the transaction inputs only for source tracing.",
            "",
            "## PIT-38 Implication",
            "",
            "- The move-date basis-decision workpaper is incomplete without this CDP protocol-state row.",
            "- If the `WBTC` collateral can be tied to Swedish K4/Koinly acquisition or replacement-basis evidence, this is likely the primary imported-basis candidate.",
            "- Do not add ERN-funded BPT/LP positions on top of the WBTC collateral as if they were separately paid acquisition cost. They are proceeds of the same debt position unless a separate non-debt source is proved.",
            "- Later BTC/WBTC to WETH movement should be traced for Polish-year disposal accounting, but it does not change the move-date collateral type: at the move-date block the active trove collateral was WBTC, not WETH.",
            "",
            "## Outputs",
            "",
            "- Summary CSV: `move-date-cdp-positions.csv`",
            "- Transaction CSV: `move-date-cdp-transactions.csv`",
            "- JSON summary: `move-date-cdp-positions-summary.json`",
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
    parser.add_argument("--move-block", type=int, default=MOVE_BLOCK)
    args = parser.parse_args()

    operations = load_operations(args.raw_dir)
    trove_manager, trove_manager_source = get_trove_manager(args.move_block)
    summaries = build_summaries(operations, trove_manager, args.move_block)

    args.output_dir.mkdir(parents=True, exist_ok=True)
    write_summary_csv(args.output_dir / "move-date-cdp-positions.csv", summaries, trove_manager, trove_manager_source)
    write_transactions_csv(args.output_dir / "move-date-cdp-transactions.csv", summaries)
    payload = build_json_payload(summaries, trove_manager, trove_manager_source)
    write_json(args.output_dir / "move-date-cdp-positions-summary.json", payload)
    write_markdown(args.output_dir / "move-date-cdp-positions.md", payload)

    print(f"Parsed trove operations: {len(operations)}")
    print(f"Trove manager: {trove_manager} ({trove_manager_source})")
    print(f"Wrote {args.output_dir / 'move-date-cdp-positions.csv'}")
    print(f"Wrote {args.output_dir / 'move-date-cdp-transactions.csv'}")
    print(f"Wrote {args.output_dir / 'move-date-cdp-positions-summary.json'}")
    print(f"Wrote {args.output_dir / 'move-date-cdp-positions.md'}")


if __name__ == "__main__":
    main()
