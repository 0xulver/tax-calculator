#!/usr/bin/env python3
"""Build a focused Reaper recovery to WBTC basis-link workpaper.

This sits after the Reaper incident workpaper and the WBTC CDP trace. It
answers a narrow evidence question: which August 2022 Reaper recovery assets
are actually seen in the predecessor chain for the move-date WBTC collateral?
"""

from __future__ import annotations

import argparse
import csv
import json
import sys
from collections import defaultdict, deque
from decimal import Decimal
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]
SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO_ROOT / "src"))
sys.path.insert(0, str(SCRIPT_DIR))

import build_move_date_basis_decision as basis  # noqa: E402
import build_wbtc_cdp_basis_trace as wbtc_trace  # noqa: E402


DEFAULT_INVENTORY_DIR = REPO_ROOT / "private/evidence/onchain/move-date-inventory-2023-04-12"
MOVE_CUTOFF_TEXT = "2023-04-12T00:00:00Z"
MARCH_COMPENSATION_USDC_TX = "0xb67d094cad2b8641086c3218fb7064d93840b82dc21b79da6bc422b57b29a2ca"
ARBITRUM_USDC_BRIDGE_TX = "0x17b3b972abccc1f6f3ca791e7b59d5d5a10a47f17644f53efb260321ab8ab4bd"
ARBITRUM_DOLA_TO_WBTC_TX = "0x89c1ea89c71ddcf1cca0fb583b48593dd7738b01065c55b912f72bde131a3e33"
FANTOM_DIGI_TO_USDC_TX = "0x19a2b48f2900a3603481a9468b92d729bac80dc9bf18a9859e4b313f917627d9"
FANTOM_DAI_TO_USDC_TX = "0xe665837ca3ab860a79a87f319946ec0bcbdc8ef6a9075a0533142da8f6dde25b"
MAX_FORWARD_DEPTH = 12
FORWARD_BRIDGE_SYMBOL_FAMILIES = {
    "ANYBTC": "BTC",
    "ANYWBTC": "BTC",
    "BTC": "BTC",
    "WBTC": "BTC",
    "ANYUSDC": "USDC",
    "USDC": "USDC",
    "USDC.E": "USDC",
    "ANYETH": "ETH",
    "ANYWETH": "ETH",
    "ETH": "ETH",
    "WETH": "ETH",
}
RECOVERY_FORWARD_INTERPRETATIONS = {
    "USDC": (
        "Indirect provenance only: the recovered USDC path reaches the Fantom USDC "
        "bridge-out and Arbitrum DOLA branch. Use it as support for the source-open "
        "rows, not as a separately counted amount."
    ),
    "DAI": (
        "Direct support for 9,000 DAI used in the November 2022 BTC buys. Additional "
        "forward hits show other DAI-derived value reaching the DOLA branch; only the "
        "direct proxy is counted here."
    ),
    "ETH": (
        "Indirect/contextual provenance only: the ETH-derived path intersects the same "
        "USDC/DIGI/DOLA branch, but no direct WBTC trace amount is assigned."
    ),
    "BTC": (
        "Direct support: recovered BTC enters the sWBTC path. Later downstream hits are "
        "corroborating context, not additive basis."
    ),
    "fUSDT": (
        "Captured as Reaper recovery evidence, but not WBTC support: later traced to DAI "
        "and then out of the known wallet with no WBTC-trace intersection."
    ),
    "WFTM": (
        "Captured as Reaper recovery evidence, but not WBTC support: later traced to AVAX "
        "and then out of the known wallet with no WBTC-trace intersection."
    ),
}


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def write_link_csv(path: Path, rows: list[dict[str, str]]) -> None:
    fieldnames = [
        "recovery_tx_hash",
        "recovery_timestamp",
        "symbol",
        "recovery_amount",
        "direct_trace_amount",
        "direct_estimate_pln",
        "direct_trace_rows",
        "forward_hit_count",
        "forward_hit_txs",
        "linked_roots",
        "status",
        "note",
    ]
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def write_forward_csv(path: Path, rows: list[dict[str, str]]) -> None:
    fieldnames = [
        "recovery_tx_hash",
        "recovery_symbol",
        "depth",
        "edge_type",
        "tx_timestamp",
        "tx_hash",
        "tx_flow",
        "source_symbol",
        "source_amount",
        "child_outputs",
        "wbtc_trace_hit",
        "wbtc_trace_roots",
        "note",
    ]
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def fmt(value: Decimal, quantum: str = "0.00000001") -> str:
    return basis.fmt_decimal(value, quantum)


def norm_hash(value: str | None) -> str:
    return (value or "").strip().lower()


def short_hash(value: str | None) -> str:
    normalized = norm_hash(value)
    if not normalized:
        return ""
    return normalized[:10] + "..."


def sum_decimal(rows: list[dict[str, str]], field: str) -> Decimal:
    return sum((basis.parse_decimal(row.get(field)) for row in rows), Decimal("0"))


def trace_rows_by_recovery(trace_rows: list[dict[str, str]], recovery_txs: set[str]) -> dict[str, list[dict[str, str]]]:
    grouped: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in trace_rows:
        source_tx = norm_hash(row.get("source_tx_hash"))
        if source_tx in recovery_txs:
            grouped[source_tx].append(row)
    return grouped


def rollforward_rows_for_tx(rows: list[dict[str, str]], tx_hash: str) -> list[dict[str, str]]:
    target = norm_hash(tx_hash)
    return [row for row in rows if norm_hash(row.get("terminal_tx_hash")) == target]


def bridge_context(movements_path: Path) -> dict[str, str]:
    movements = basis.read_csv(movements_path)
    _, bridge_rows = wbtc_trace.find_bridge_links(movements)
    for row in bridge_rows:
        if norm_hash(row.get("destination_tx_hash")) == ARBITRUM_USDC_BRIDGE_TX:
            return row
    return {}


def tx_key_from_row(row: dict[str, str]) -> tuple[str, str, str]:
    return (row.get("chain", ""), row.get("wallet_address", "").lower(), row.get("tx_hash", ""))


def bridge_family(symbol: str | None) -> str:
    return FORWARD_BRIDGE_SYMBOL_FAMILIES.get(basis.normalize_symbol(symbol or ""), "")


def bridge_source_preference(symbol: str | None) -> int:
    normalized = basis.normalize_symbol(symbol or "")
    return 1 if normalized.startswith("ANY") else 0


def build_forward_bridge_links(
    movements: list[dict[str, str]],
) -> dict[tuple[str, str, str], dict[str, str]]:
    """Build source-chain to destination-chain bridge links for forward evidence.

    This is intentionally broader than the WBTC filing trace and includes ETH.
    The output is only used as provenance context; it does not change the scaled
    WBTC filing candidate.
    """
    grouped = wbtc_trace.group_rows_by_tx(movements)
    source_candidates: list[tuple[tuple[str, str, str], object, Decimal, str, int, dict[str, str]]] = []
    destination_candidates: list[tuple[tuple[str, str, str], object, Decimal, str, dict[str, str]]] = []

    for group_key, rows in grouped.items():
        timestamp = wbtc_trace.tx_timestamp(rows)
        if not timestamp:
            continue
        for row in rows:
            family = bridge_family(row.get("symbol", ""))
            if not family:
                continue
            amount = abs(basis.parse_decimal(row.get("amount")))
            if amount <= 0:
                continue
            method = row.get("method", "")
            if row.get("direction") == "out":
                source_candidates.append(
                    (group_key, timestamp, amount, family, bridge_source_preference(row.get("symbol")), row)
                )
            if row.get("direction") == "in" and method.startswith("anySwapInAuto"):
                destination_candidates.append((group_key, timestamp, amount, family, row))

    by_source: dict[tuple[str, str, str], dict[str, str]] = {}
    for dest_key, dest_time, dest_amount, dest_family, dest_row in destination_candidates:
        best: tuple[Decimal, int, float, tuple[str, str, str], object, Decimal, dict[str, str]] | None = None
        for src_key, src_time, src_amount, src_family, src_preference, src_row in source_candidates:
            if src_key == dest_key or src_key[0] == dest_key[0] or src_key[1] != dest_key[1]:
                continue
            if src_family != dest_family:
                continue
            seconds = (dest_time - src_time).total_seconds()  # type: ignore[operator]
            if seconds < 0 or seconds > wbtc_trace.BRIDGE_MATCH_WINDOW_SECONDS:
                continue
            diff = abs(src_amount - dest_amount)
            if dest_amount and diff / dest_amount > wbtc_trace.BRIDGE_AMOUNT_TOLERANCE:
                continue
            candidate = (diff, src_preference, seconds, src_key, src_time, src_amount, src_row)
            if best is None or candidate[:3] < best[:3]:
                best = candidate
        if best is None:
            continue
        diff, _, seconds, src_key, src_time, src_amount, src_row = best
        by_source[src_key] = {
            "bridge_family": dest_family,
            "source_chain": src_key[0],
            "source_tx_hash": src_key[2],
            "source_timestamp": src_time.isoformat().replace("+00:00", "Z"),  # type: ignore[attr-defined]
            "source_amount": basis.fmt_decimal(src_amount),
            "source_symbol": src_row.get("symbol", ""),
            "destination_chain": dest_key[0],
            "destination_tx_hash": dest_key[2],
            "destination_timestamp": dest_time.isoformat().replace("+00:00", "Z"),  # type: ignore[attr-defined]
            "destination_amount": basis.fmt_decimal(dest_amount),
            "destination_symbol": dest_row.get("symbol", ""),
            "amount_difference": basis.fmt_decimal(diff),
            "seconds_between": basis.fmt_decimal(Decimal(str(seconds))),
        }
    return by_source


def wbtc_trace_index(trace_rows: list[dict[str, str]]) -> tuple[set[str], dict[str, set[str]]]:
    hashes: set[str] = set()
    roots_by_hash: dict[str, set[str]] = defaultdict(set)
    for row in trace_rows:
        root = row.get("root_tx_hash", "")
        for field in ("tx_hash", "source_tx_hash"):
            tx_hash = norm_hash(row.get(field))
            if not tx_hash or tx_hash == "archive_gap_or_prehistory":
                continue
            hashes.add(tx_hash)
            if root:
                roots_by_hash[tx_hash].add(root)
    return hashes, roots_by_hash


def recovery_start_rows(
    recovery_rows: list[dict[str, str]],
    movement_rows: list[dict[str, str]],
) -> list[dict[str, str]]:
    recovery_txs = {norm_hash(row.get("tx_hash")) for row in recovery_rows}
    rows = [
        row
        for row in movement_rows
        if norm_hash(row.get("tx_hash")) in recovery_txs
        and row.get("direction") == "in"
        and basis.parse_decimal(row.get("amount")) > 0
    ]
    rows.sort(key=lambda row: (row.get("timestamp", ""), row.get("symbol", "")))
    return rows


def positive_outputs(rows: list[dict[str, str]]) -> list[dict[str, str]]:
    return [
        row
        for row in rows
        if row.get("direction") == "in" and basis.parse_decimal(row.get("amount")) > 0
    ]


def build_forward_trace_rows(
    *,
    recovery_rows: list[dict[str, str]],
    movement_rows: list[dict[str, str]],
    trace_rows: list[dict[str, str]],
    max_depth: int = MAX_FORWARD_DEPTH,
) -> list[dict[str, str]]:
    _, consumed_by_tx, tx_rows = basis.build_fifo(movement_rows)
    bridge_by_source = build_forward_bridge_links(movement_rows)
    trace_hashes, roots_by_hash = wbtc_trace_index(trace_rows)

    consumptions_by_source: dict[tuple[tuple[str, str, str, str, str, str], str], list[basis.Consumption]] = defaultdict(list)
    for consumptions in consumed_by_tx.values():
        for consumption in consumptions:
            if consumption.source_tx_hash and consumption.source_tx_hash != "ARCHIVE_GAP_OR_PREHISTORY":
                consumptions_by_source[(consumption.source_key, norm_hash(consumption.source_tx_hash))].append(consumption)
    for consumptions in consumptions_by_source.values():
        consumptions.sort(key=lambda item: (item.timestamp, item.tx_hash, basis.fmt_decimal(item.source_amount)))

    output_rows: list[dict[str, str]] = []
    queue: deque[dict[str, object]] = deque()
    for row in recovery_start_rows(recovery_rows, movement_rows):
        amount = basis.parse_decimal(row.get("amount"))
        queue.append(
            {
                "recovery_tx_hash": norm_hash(row.get("tx_hash")),
                "recovery_symbol": row.get("symbol", ""),
                "key": basis.asset_key(row),
                "tx_hash": norm_hash(row.get("tx_hash")),
                "symbol": row.get("symbol", ""),
                "amount": amount,
                "depth": 0,
                "path": [norm_hash(row.get("tx_hash"))],
            }
        )

    seen: set[tuple[str, tuple[str, str, str, str, str, str], str, str, int]] = set()
    while queue:
        state = queue.popleft()
        recovery_tx = str(state["recovery_tx_hash"])
        recovery_symbol = str(state["recovery_symbol"])
        key = state["key"]  # type: ignore[assignment]
        tx_hash = str(state["tx_hash"])
        symbol = str(state["symbol"])
        amount = state["amount"]  # type: ignore[assignment]
        depth = int(state["depth"])
        path = list(state["path"])  # type: ignore[arg-type]
        if not isinstance(amount, Decimal) or amount <= 0 or depth >= max_depth:
            continue
        seen_key = (recovery_tx, key, tx_hash, basis.fmt_decimal(amount, "0.00000001"), depth)  # type: ignore[arg-type]
        if seen_key in seen:
            continue
        seen.add(seen_key)

        bridge = bridge_by_source.get((key[0], key[1], tx_hash))  # type: ignore[index]
        if bridge and bridge["destination_tx_hash"] not in path:
            source_amount = basis.parse_decimal(bridge.get("source_amount"))
            dest_amount = basis.parse_decimal(bridge.get("destination_amount"))
            bridged_amount = amount
            if source_amount > 0:
                bridged_amount = amount * dest_amount / source_amount
            dest_key = (bridge["destination_chain"], key[1], bridge["destination_tx_hash"])  # type: ignore[index]
            dest_rows = tx_rows.get(dest_key, [])
            dest_outputs = [
                row
                for row in positive_outputs(dest_rows)
                if bridge_family(row.get("symbol")) == bridge_family(bridge.get("destination_symbol"))
            ]
            child_outputs = [
                f"{basis.fmt_decimal(bridged_amount, '0.00000001')} {row.get('symbol', '')}"
                for row in dest_outputs[:3]
            ]
            hit = norm_hash(bridge["destination_tx_hash"]) in trace_hashes
            output_rows.append(
                {
                    "recovery_tx_hash": recovery_tx,
                    "recovery_symbol": recovery_symbol,
                    "depth": str(depth + 1),
                    "edge_type": "cross_chain_bridge",
                    "tx_timestamp": bridge.get("destination_timestamp", ""),
                    "tx_hash": bridge["destination_tx_hash"],
                    "tx_flow": basis.summarize_tx(dest_rows),
                    "source_symbol": symbol,
                    "source_amount": basis.fmt_decimal(amount),
                    "child_outputs": "; ".join(child_outputs),
                    "wbtc_trace_hit": "yes" if hit else "",
                    "wbtc_trace_roots": "; ".join(sorted(roots_by_hash.get(norm_hash(bridge["destination_tx_hash"]), set()))),
                    "note": (
                        f"Bridge from {bridge['source_chain']} {bridge['source_tx_hash']} "
                        f"to {bridge['destination_chain']} {bridge['destination_tx_hash']}"
                    ),
                }
            )
            for dest_output in dest_outputs:
                queue.append(
                    {
                        "recovery_tx_hash": recovery_tx,
                        "recovery_symbol": recovery_symbol,
                        "key": basis.asset_key(dest_output),
                        "tx_hash": norm_hash(dest_output.get("tx_hash")),
                        "symbol": dest_output.get("symbol", ""),
                        "amount": bridged_amount,
                        "depth": depth + 1,
                        "path": path + [norm_hash(bridge["destination_tx_hash"])],
                    }
                )

        remaining = amount
        for consumption in consumptions_by_source.get((key, tx_hash), []):  # type: ignore[arg-type]
            if remaining <= 0:
                break
            if norm_hash(consumption.tx_hash) == tx_hash:
                continue
            consumed = min(remaining, consumption.source_amount)
            if consumed <= 0:
                continue
            remaining -= consumed
            tx_key = (consumption.chain, consumption.wallet_address, consumption.tx_hash)
            rows = tx_rows.get(tx_key, [])
            scale = consumed / consumption.out_amount if consumption.out_amount else Decimal("1")
            children = []
            for child in positive_outputs(rows):
                child_amount = basis.parse_decimal(child.get("amount")) * scale
                if child_amount <= 0:
                    continue
                children.append((child, child_amount))
            hit = norm_hash(consumption.tx_hash) in trace_hashes
            output_rows.append(
                {
                    "recovery_tx_hash": recovery_tx,
                    "recovery_symbol": recovery_symbol,
                    "depth": str(depth + 1),
                    "edge_type": "token_consumption",
                    "tx_timestamp": consumption.timestamp,
                    "tx_hash": consumption.tx_hash,
                    "tx_flow": basis.summarize_tx(rows),
                    "source_symbol": symbol,
                    "source_amount": basis.fmt_decimal(consumed),
                    "child_outputs": "; ".join(
                        f"{basis.fmt_decimal(child_amount, '0.00000001')} {child.get('symbol', '')}"
                        for child, child_amount in children[:6]
                    ),
                    "wbtc_trace_hit": "yes" if hit else "",
                    "wbtc_trace_roots": "; ".join(sorted(roots_by_hash.get(norm_hash(consumption.tx_hash), set()))),
                    "note": "Consumption transaction is present in WBTC trace" if hit else "",
                }
            )
            for child, child_amount in children:
                queue.append(
                    {
                        "recovery_tx_hash": recovery_tx,
                        "recovery_symbol": recovery_symbol,
                        "key": basis.asset_key(child),
                        "tx_hash": norm_hash(child.get("tx_hash")),
                        "symbol": child.get("symbol", ""),
                        "amount": child_amount,
                        "depth": depth + 1,
                        "path": path + [norm_hash(consumption.tx_hash)],
                    }
                )

    output_rows.sort(
        key=lambda row: (
            row["recovery_timestamp"] if "recovery_timestamp" in row else "",
            row["recovery_symbol"],
            int(row["depth"]),
            row["tx_timestamp"],
            row["tx_hash"],
        )
    )
    return output_rows


def forward_hits_by_recovery(forward_rows: list[dict[str, str]]) -> dict[str, list[dict[str, str]]]:
    grouped: dict[str, list[dict[str, str]]] = defaultdict(list)
    seen: set[tuple[str, str]] = set()
    for row in forward_rows:
        if row.get("wbtc_trace_hit") != "yes":
            continue
        key = (row["recovery_tx_hash"], row["tx_hash"])
        if key in seen:
            continue
        seen.add(key)
        grouped[row["recovery_tx_hash"]].append(row)
    return grouped


def selected_forward_refs(
    link_row: dict[str, str],
    hit_rows: list[dict[str, str]],
    all_forward_rows: list[dict[str, str]],
    bridge_source_tx: str,
) -> str:
    labels: list[tuple[str, str]] = []
    for tx_hash in link_row.get("direct_trace_rows", "").split("; "):
        if tx_hash:
            labels.append((tx_hash, "direct WBTC trace consumption"))
    for tx_hash, label in (
        (FANTOM_DAI_TO_USDC_TX, "DAI to USDC"),
        (FANTOM_DIGI_TO_USDC_TX, "DIGI to USDC"),
        (bridge_source_tx, "Fantom USDC bridge-out"),
        (ARBITRUM_USDC_BRIDGE_TX, "Arbitrum USDC bridge-in"),
        (ARBITRUM_DOLA_TO_WBTC_TX, "DOLA to WBTC"),
    ):
        if tx_hash and any(norm_hash(row.get("tx_hash")) == norm_hash(tx_hash) for row in hit_rows):
            labels.append((tx_hash, label))

    seen: set[str] = set()
    refs: list[str] = []
    for tx_hash, label in labels:
        normalized = norm_hash(tx_hash)
        if not normalized or normalized in seen:
            continue
        seen.add(normalized)
        refs.append(f"`{short_hash(normalized)}` {label}")
    if refs:
        return "; ".join(refs[:6])
    if hit_rows:
        distinct = len({norm_hash(row.get("tx_hash")) for row in hit_rows})
        return f"{distinct} WBTC-trace intersections in the raw forward CSV"
    if all_forward_rows:
        fallback_refs = []
        for row in all_forward_rows[:4]:
            child_outputs = row.get("child_outputs", "")
            if child_outputs:
                child_symbols = ", ".join(
                    part.strip().split(" ")[-1]
                    for part in child_outputs.split("; ")
                    if part.strip()
                )
                label = f"{row.get('source_symbol', '')} to {child_symbols}"
            else:
                label = f"{row.get('source_symbol', '')} spent/no in-wallet output"
            fallback_refs.append(f"`{short_hash(row.get('tx_hash'))}` {label}")
        return "; ".join(fallback_refs)
    return "none"


def forward_trace_summary_rows(
    link_rows: list[dict[str, str]],
    forward_rows: list[dict[str, str]],
    bridge_source_tx: str,
) -> list[dict[str, str]]:
    hits_by_recovery = forward_hits_by_recovery(forward_rows)
    all_by_recovery: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in forward_rows:
        all_by_recovery[row["recovery_tx_hash"]].append(row)
    rows: list[dict[str, str]] = []
    for link_row in link_rows:
        recovery_tx = link_row["recovery_tx_hash"]
        hit_rows = hits_by_recovery.get(recovery_tx, [])
        all_rows = sorted(
            all_by_recovery.get(recovery_tx, []),
            key=lambda row: (int(row.get("depth", "0")), row.get("tx_timestamp", ""), row.get("tx_hash", "")),
        )
        status = link_row["status"].replace("_", " ")
        if link_row.get("direct_estimate_pln"):
            status += f"; direct proxy {link_row['direct_estimate_pln']} PLN"
        rows.append(
            {
                "symbol": link_row["symbol"],
                "status": status,
                "selected_refs": selected_forward_refs(link_row, hit_rows, all_rows, bridge_source_tx),
                "hit_count": str(len({norm_hash(row.get("tx_hash")) for row in hit_rows})),
                "interpretation": RECOVERY_FORWARD_INTERPRETATIONS.get(
                    link_row["symbol"],
                    "Review raw forward CSV before using this row.",
                ),
            }
        )
    return rows


def build_link_rows(
    recovery_rows: list[dict[str, str]],
    trace_rows: list[dict[str, str]],
    forward_rows: list[dict[str, str]],
) -> list[dict[str, str]]:
    recovery_txs = {norm_hash(row.get("tx_hash")) for row in recovery_rows}
    trace_by_recovery = trace_rows_by_recovery(trace_rows, recovery_txs)
    forward_hits = forward_hits_by_recovery(forward_rows)
    output_rows: list[dict[str, str]] = []

    for recovery in recovery_rows:
        tx_hash = norm_hash(recovery.get("tx_hash"))
        matches = trace_by_recovery.get(tx_hash, [])
        indirect_hits = forward_hits.get(tx_hash, [])
        linked_amount = sum_decimal(matches, "source_amount")
        linked_pln = sum_decimal(matches, "estimate_pln")
        roots = sorted(
            {row.get("root_tx_hash", "") for row in matches if row.get("root_tx_hash")}
            | {
                root
                for row in indirect_hits
                for root in row.get("wbtc_trace_roots", "").split("; ")
                if root
            }
        )
        trace_refs = sorted({row.get("tx_hash", "") for row in matches if row.get("tx_hash")})
        hit_refs = sorted({row.get("tx_hash", "") for row in indirect_hits if row.get("tx_hash")})
        symbol = recovery.get("symbol", "")
        recovery_amount = basis.parse_decimal(recovery.get("amount"))
        if matches and indirect_hits:
            status = "direct_and_indirect_wbtc_trace_link"
            note = "Recovery lot is directly consumed by WBTC predecessor rows and also has later forward-trace hits."
        elif matches:
            status = "directly_linked_to_wbtc_trace"
            note = "Recovery lot is explicitly consumed by a predecessor transaction in the WBTC CDP trace."
        elif indirect_hits:
            status = "indirectly_linked_to_wbtc_trace"
            note = "Recovery lot is not a direct WBTC trace source row, but forward tracing reaches transactions in the WBTC trace."
        else:
            status = "not_seen_in_wbtc_trace"
            note = "Recovery lot is not currently tied to the move-date WBTC predecessor chain."
        output_rows.append(
            {
                "recovery_tx_hash": tx_hash,
                "recovery_timestamp": recovery.get("timestamp", ""),
                "symbol": symbol,
                "recovery_amount": fmt(recovery_amount),
                "direct_trace_amount": fmt(linked_amount) if linked_amount else "",
                "direct_estimate_pln": fmt(linked_pln, "0.01") if linked_pln else "",
                "direct_trace_rows": "; ".join(trace_refs),
                "forward_hit_count": str(len(indirect_hits)) if indirect_hits else "0",
                "forward_hit_txs": "; ".join(hit_refs[:12]),
                "linked_roots": "; ".join(roots),
                "status": status,
                "note": note,
            }
        )
    return output_rows


def build_summary(
    *,
    link_rows: list[dict[str, str]],
    forward_rows: list[dict[str, str]],
    rollforward_rows: list[dict[str, str]],
    bridge_row: dict[str, str],
) -> dict[str, object]:
    direct_rows = [row for row in link_rows if row["status"] in {"directly_linked_to_wbtc_trace", "direct_and_indirect_wbtc_trace_link"}]
    indirect_only_rows = [row for row in link_rows if row["status"] == "indirectly_linked_to_wbtc_trace"]
    unlinked_rows = [row for row in link_rows if row["status"] == "not_seen_in_wbtc_trace"]
    linked_pln = sum_decimal(direct_rows, "direct_estimate_pln")
    b67d_amount = sum_decimal(rollforward_rows, "terminal_amount")
    b67d_pln = sum_decimal(rollforward_rows, "cost_pln")
    forward_hit_txs = sorted({row["tx_hash"] for row in forward_rows if row.get("wbtc_trace_hit") == "yes"})
    return {
        "cutoff": MOVE_CUTOFF_TEXT,
        "direct_recovery_linked_symbols": [row["symbol"] for row in direct_rows],
        "indirect_recovery_linked_symbols": [row["symbol"] for row in indirect_only_rows],
        "recovery_unlinked_symbols": [row["symbol"] for row in unlinked_rows],
        "direct_recovery_linked_proxy_pln": fmt(linked_pln, "0.01"),
        "forward_wbtc_trace_hit_count": len(forward_hit_txs),
        "forward_wbtc_trace_hit_txs": forward_hit_txs,
        "march_compensation_usdc_tx": MARCH_COMPENSATION_USDC_TX,
        "march_compensation_usdc_rollforward_amount": fmt(b67d_amount),
        "march_compensation_usdc_rollforward_pln": fmt(b67d_pln, "0.01"),
        "arbitrum_usdc_bridge_destination_tx": ARBITRUM_USDC_BRIDGE_TX,
        "arbitrum_usdc_bridge_source_tx": bridge_row.get("source_tx_hash", ""),
        "arbitrum_usdc_bridge_destination_amount": bridge_row.get("destination_amount", ""),
        "arbitrum_usdc_bridge_source_amount": bridge_row.get("source_amount", ""),
        "arbitrum_usdc_bridge_seconds_between": bridge_row.get("seconds_between", ""),
        "filing_position": (
            "Direct Reaper recovery evidence supports the DAI/BTC subchain. Forward tracing adds provenance "
            "links for USDC and ETH, plus additional DAI/BTC downstream hops, into the Arbitrum DOLA "
            "source-open branch. These forward links are not additive filing amounts. The March 2023 USDC "
            "leg remains a separate source-open/compensation leg in the WBTC roll-forward."
        ),
    }


def write_markdown(
    path: Path,
    *,
    link_rows: list[dict[str, str]],
    forward_rows: list[dict[str, str]],
    rollforward_rows: list[dict[str, str]],
    bridge_row: dict[str, str],
    summary: dict[str, object],
) -> None:
    lines = [
        "# Reaper Recovery Link to WBTC Collateral",
        "",
        f"Cut-off: `{MOVE_CUTOFF_TEXT}`",
        "",
        "This generated workpaper links the August 2022 Reaper multistrategy recovery rows to the predecessor chain for the Ethos WBTC collateral held at the Poland move date. It is an evidence map, not a final legal conclusion.",
        "",
        "## Current Finding",
        "",
        f"- Direct Reaper recovery rows visible in the WBTC trace: `{', '.join(summary['direct_recovery_linked_symbols'])}`.",
        f"- Recovery rows linked only through forward tracing: `{', '.join(summary['indirect_recovery_linked_symbols'])}`.",
        f"- Recovery rows still not tied to the WBTC trace: `{', '.join(summary['recovery_unlinked_symbols'])}`.",
        f"- Direct linked recovery proxy amount in the WBTC trace: `{summary['direct_recovery_linked_proxy_pln']} PLN`.",
        f"- Distinct forward-trace hits inside the WBTC trace: `{summary['forward_wbtc_trace_hit_count']}`.",
        f"- Separate March 2023 USDC compensation/source-open leg in the scaled roll-forward: `{summary['march_compensation_usdc_rollforward_amount']} USDC`, `{summary['march_compensation_usdc_rollforward_pln']} PLN`.",
        "",
        "Interpretation: the Reaper evidence materially improves the WBTC basis story, but it does not convert the whole WBTC candidate into final proof by itself. The directly linked Reaper assets are the 9,000 DAI used in the November 2022 BTC purchases and the 0.04636763 BTC that flowed through the sWBTC path. Forward tracing also ties the August 18 USDC and ETH recovery rows, plus additional DAI-derived value, into the Arbitrum DOLA source-open branch through the Fantom-to-Arbitrum USDC bridge. The March 2023 USDC transfer remains a separate source-open compensation/provenance leg.",
        "",
        "## Direct Recovery Rows",
        "",
        "| Recovery date | Recovery tx | Symbol | Recovery amount | Direct amount | Direct proxy PLN | Forward hits | Status |",
        "| --- | --- | --- | ---: | ---: | ---: | ---: | --- |",
    ]
    for row in link_rows:
        lines.append(
            "| {date} | `{tx}` | {symbol} | {recovery_amount} | {linked_amount} | {pln} | {hits} | `{status}` |".format(
                date=(row.get("recovery_timestamp", "") or "")[:10],
                tx=row["recovery_tx_hash"],
                symbol=row["symbol"],
                recovery_amount=row["recovery_amount"],
                linked_amount=row["direct_trace_amount"],
                pln=row["direct_estimate_pln"],
                hits=row["forward_hit_count"],
                status=row["status"],
            )
        )

    trace_summary_rows = forward_trace_summary_rows(
        link_rows,
        forward_rows,
        str(summary.get("arbitrum_usdc_bridge_source_tx", "")),
    )
    lines.extend(
        [
            "",
            "## Forward Trace Summary",
            "",
            "The raw forward trace CSV is intentionally verbose and includes converging downstream paths. Use this summary for filing reasoning; do not sum raw forward rows as acquisition cost.",
            "",
            "| Recovery | Evidence status | Selected intersections | Distinct hit txs | Treatment |",
            "| --- | --- | --- | ---: | --- |",
        ]
    )
    for row in trace_summary_rows:
        lines.append(
            "| {symbol} | {status} | {refs} | {hits} | {interpretation} |".format(
                symbol=row["symbol"],
                status=row["status"],
                refs=row["selected_refs"],
                hits=row["hit_count"],
                interpretation=row["interpretation"],
            )
        )

    lines.extend(
        [
            "",
            "## Separate March 2023 USDC Leg",
            "",
            f"- Roll-forward terminal tx: `{MARCH_COMPENSATION_USDC_TX}`.",
            f"- Scaled amount allocated to WBTC predecessor chain: `{summary['march_compensation_usdc_rollforward_amount']} USDC`.",
            f"- USD/PLN proxy in the roll-forward: `{summary['march_compensation_usdc_rollforward_pln']} PLN`.",
            "- This is not an August 2022 recovery tx. Treat it as source-open compensation/provenance evidence unless and until the company/Reaper relationship and legal basis are documented.",
            "",
        ]
    )

    if rollforward_rows:
        lines.extend(
            [
                "| Root top-up | Amount | Cost | Path tail |",
                "| --- | ---: | ---: | --- |",
            ]
        )
        for row in rollforward_rows:
            lines.append(
                "| `{root}` | {amount} {symbol} | {cost} PLN | `{tx}` |".format(
                    root=row.get("root_tx_hash", "")[:10] + "...",
                    amount=row.get("terminal_amount", ""),
                    symbol=row.get("terminal_symbol", ""),
                    cost=row.get("cost_pln", ""),
                    tx=row.get("terminal_tx_hash", ""),
                )
            )

    lines.extend(
        [
            "",
            "## Arbitrum USDC Bridge Context",
            "",
        ]
    )
    if bridge_row:
        lines.extend(
            [
                f"- Destination: `{bridge_row['destination_chain']}` `{bridge_row['destination_tx_hash']}`, `{bridge_row['destination_amount']} {bridge_row['destination_symbol']}`.",
                f"- Source: `{bridge_row['source_chain']}` `{bridge_row['source_tx_hash']}`, `{bridge_row['source_amount']} {bridge_row['source_symbol']}`.",
                f"- Time delta: `{bridge_row['seconds_between']}` seconds.",
                "- This narrows the Arbitrum DOLA/FRAX branch to a Fantom USDC bridge-out, but the trace CSV remains an unscaled evidence map. Do not add repeated deep-trace rows as separate filing values.",
            ]
        )
    else:
        lines.append("- No bridge link found for the Arbitrum USDC.e receipt.")

    lines.extend(
        [
            "",
            "## Filing Use",
            "",
            "- Count the Reaper recovery evidence as support for the WBTC predecessor chain where directly linked.",
            "- Treat forward-trace hits as provenance support, not additive filing amounts.",
            "- Do not assume the still-unlinked August 2022 recovery assets funded WBTC without a trace.",
            "- Keep the WBTC filing candidate anchored to the scaled roll-forward: `41086.89 PLN` exact Koinly anchors plus `101493.55 PLN` stablecoin/source-open proxy, total `142580.44 PLN` before final legal acceptance.",
            "- The Reaper facts strengthen the source-open proxy story, especially for the DAI/BTC and Arbitrum DOLA subchains, but the March 2023 USDC leg still needs final legal treatment as compensation/replacement/source evidence.",
            "",
            "## Outputs",
            "",
            "- CSV link table: `move-date-wbtc-reaper-recovery-link.csv`",
            "- Forward trace CSV: `move-date-wbtc-reaper-recovery-forward-trace.csv`",
            "- JSON summary: `move-date-wbtc-reaper-recovery-link-summary.json`",
            "",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")


def build(args: argparse.Namespace) -> None:
    inventory_dir = Path(args.inventory_dir)
    recovery_path = inventory_dir / "move-date-reaper-multistrategy-hack-thread-recovery.csv"
    trace_path = inventory_dir / "move-date-wbtc-cdp-basis-trace.csv"
    rollforward_path = inventory_dir / "move-date-wbtc-basis-rollforward.csv"
    movements_path = inventory_dir / "move-date-movements.csv"
    output_csv = inventory_dir / "move-date-wbtc-reaper-recovery-link.csv"
    output_forward_csv = inventory_dir / "move-date-wbtc-reaper-recovery-forward-trace.csv"
    output_json = inventory_dir / "move-date-wbtc-reaper-recovery-link-summary.json"
    output_md = inventory_dir / "move-date-wbtc-reaper-recovery-link.md"

    recovery_rows = read_csv(recovery_path)
    trace_rows = read_csv(trace_path)
    movement_rows = basis.read_csv(movements_path)
    rollforward_rows = rollforward_rows_for_tx(read_csv(rollforward_path), MARCH_COMPENSATION_USDC_TX)
    bridge_row = bridge_context(movements_path)

    forward_rows = build_forward_trace_rows(
        recovery_rows=recovery_rows,
        movement_rows=movement_rows,
        trace_rows=trace_rows,
    )
    link_rows = build_link_rows(recovery_rows, trace_rows, forward_rows)
    summary = build_summary(
        link_rows=link_rows,
        forward_rows=forward_rows,
        rollforward_rows=rollforward_rows,
        bridge_row=bridge_row,
    )

    write_link_csv(output_csv, link_rows)
    write_forward_csv(output_forward_csv, forward_rows)
    output_json.write_text(json.dumps(summary, indent=2, sort_keys=True), encoding="utf-8")
    write_markdown(
        output_md,
        link_rows=link_rows,
        forward_rows=forward_rows,
        rollforward_rows=rollforward_rows,
        bridge_row=bridge_row,
        summary=summary,
    )

    print(json.dumps(summary, indent=2, sort_keys=True))


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--inventory-dir", default=str(DEFAULT_INVENTORY_DIR))
    build(parser.parse_args())


if __name__ == "__main__":
    main()
