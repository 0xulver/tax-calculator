#!/usr/bin/env python3
"""Build a scaled WBTC CDP basis roll-forward workpaper.

This sits after ``build_wbtc_cdp_basis_trace.py``. The trace workpaper is an
evidence map; this script scales predecessor quantities to each actual WBTC
trove top-up and separates exact Koinly-backed anchors from proxy/open legs.
"""

from __future__ import annotations

import argparse
import csv
import json
import sys
from collections import Counter, defaultdict
from dataclasses import dataclass
from decimal import Decimal
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]
SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO_ROOT / "src"))
sys.path.insert(0, str(SCRIPT_DIR))

import build_move_date_basis_decision as basis  # noqa: E402
import build_wbtc_cdp_basis_trace as wbtc_trace  # noqa: E402
from tax_calc.nbp import NBPClient  # noqa: E402


DEFAULT_INVENTORY_DIR = REPO_ROOT / "private/evidence/onchain/move-date-inventory-2023-04-12"
DEFAULT_KOINLY_DIR = REPO_ROOT / "private/evidence/koinly"
MOVE_CUTOFF_TEXT = "2023-04-12T00:00:00Z"

BTC_EQUIVALENTS = {"BTC", "WBTC"}
STABLE_EQUIVALENTS = {
    "BUSD",
    "DAI",
    "DAI+",
    "DOLA",
    "ERN",
    "FRAX",
    "SUSD",
    "USDC",
    "USDC.E",
    "USDT",
    "XUSD",
}


@dataclass
class TerminalCost:
    cost_pln: Decimal
    cost_sek: Decimal
    status: str
    note: str
    source_file: str = ""


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def read_csv_after_header(path: Path, header_prefix: str) -> list[dict[str, str]]:
    lines = path.read_text(encoding="utf-8-sig", errors="replace").splitlines()
    while lines and not lines[0].startswith(header_prefix):
        lines.pop(0)
    if not lines:
        return []
    return list(csv.DictReader(lines))


def norm_hash(value: str | None) -> str:
    text = (value or "").strip().lower()
    if text.startswith("0x"):
        return text[2:]
    return text


def display_hash(value: str) -> str:
    if not value:
        return ""
    if value == "archive_gap_or_prehistory":
        return "ARCHIVE_GAP_OR_PREHISTORY"
    return "0x" + value


def symbol_key(symbol: str | None) -> str:
    return basis.normalize_symbol(symbol or "").replace("USDC.E", "USDC.E")


def symbols_equivalent(left: str | None, right: str | None) -> bool:
    lhs = symbol_key(left)
    rhs = symbol_key(right)
    if lhs == rhs:
        return True
    if lhs in BTC_EQUIVALENTS and rhs in BTC_EQUIVALENTS:
        return True
    if lhs == "USDC.E" and rhs == "USDC":
        return True
    if lhs == "USDC" and rhs == "USDC.E":
        return True
    return False


def is_stable(symbol: str | None) -> bool:
    return symbol_key(symbol) in STABLE_EQUIVALENTS


def load_koinly_transactions(koinly_dir: Path) -> dict[str, list[dict[str, str]]]:
    index: dict[str, list[dict[str, str]]] = defaultdict(list)
    for path in sorted(koinly_dir.glob("*/*transaction_history*.csv")):
        for row in read_csv_after_header(path, "Date,"):
            tx_hash = norm_hash(row.get("TxHash"))
            if not tx_hash:
                continue
            enriched = dict(row)
            enriched["_source_file"] = str(path.relative_to(REPO_ROOT))
            enriched["_year"] = path.parent.name
            index[tx_hash].append(enriched)
    return index


def koinly_terminal_cost(
    *,
    tx_hash: str,
    symbol: str,
    amount: Decimal,
    koinly_index: dict[str, list[dict[str, str]]],
    sek_rate: Decimal,
) -> TerminalCost | None:
    matches = koinly_index.get(norm_hash(tx_hash), [])
    candidates: list[tuple[Decimal, str, str]] = []
    for row in matches:
        received_amount = basis.parse_decimal(row.get("Received Amount"))
        received_cost = basis.parse_decimal(row.get("Received Cost Basis"))
        if received_amount > 0 and received_cost > 0 and symbols_equivalent(symbol, row.get("Received Currency")):
            unit_cost_sek = received_cost / received_amount
            candidates.append(
                (
                    unit_cost_sek,
                    row.get("_source_file", ""),
                    (
                        f"Koinly received {basis.fmt_decimal(received_amount)} {row.get('Received Currency')} "
                        f"with {basis.fmt_decimal(received_cost, '0.01')} SEK cost"
                    ),
                )
            )

        sent_amount = basis.parse_decimal(row.get("Sent Amount"))
        sent_cost = basis.parse_decimal(row.get("Sent Cost Basis"))
        if sent_amount > 0 and sent_cost > 0 and symbols_equivalent(symbol, row.get("Sent Currency")):
            unit_cost_sek = sent_cost / sent_amount
            candidates.append(
                (
                    unit_cost_sek,
                    row.get("_source_file", ""),
                    (
                        f"Koinly sent {basis.fmt_decimal(sent_amount)} {row.get('Sent Currency')} "
                        f"with {basis.fmt_decimal(sent_cost, '0.01')} SEK cost"
                    ),
                )
            )

    if not candidates:
        return None

    unit_cost_sek, source_file, note = candidates[0]
    cost_sek = amount * unit_cost_sek
    return TerminalCost(
        cost_pln=cost_sek * sek_rate,
        cost_sek=cost_sek,
        status="exact_koinly_transaction_history_anchor",
        note=f"{note}; scaled to {basis.fmt_decimal(amount)} {symbol}",
        source_file=source_file,
    )


def stable_terminal_cost(
    *,
    symbol: str,
    amount: Decimal,
    timestamp: str,
    nbp: NBPClient,
) -> TerminalCost | None:
    if not is_stable(symbol):
        return None
    tx_date = (timestamp or "")[:10]
    if not tx_date:
        return None
    usd_rate, usd_rate_date = nbp.get_rate_with_date("USD", tx_date)
    if not usd_rate:
        return None
    return TerminalCost(
        cost_pln=amount * usd_rate,
        cost_sek=Decimal("0"),
        status="stablecoin_usd_value_proxy_source_open",
        note=f"{basis.fmt_decimal(amount)} {symbol} x USD/PLN {usd_rate} from {usd_rate_date}; source proof still open",
    )


def tx_timestamp(rows: list[dict[str, str]]) -> str:
    timestamps = sorted(row.get("timestamp", "") for row in rows if row.get("timestamp"))
    return timestamps[0] if timestamps else ""


def row_amount(row: dict[str, str]) -> Decimal:
    return basis.parse_decimal(row.get("amount"))


def asset_value_pln(symbol: str, amount: Decimal, timestamp: str, nbp: NBPClient) -> Decimal | None:
    if is_stable(symbol):
        usd_rate, _ = nbp.get_rate_with_date("USD", (timestamp or "")[:10])
        if usd_rate:
            return amount * usd_rate
    return None


def allocation_scale(
    *,
    group_rows: list[dict[str, str]],
    requested_symbol: str,
    requested_amount: Decimal,
    nbp: NBPClient,
) -> tuple[Decimal, str, str]:
    timestamp = tx_timestamp(group_rows)
    positive_rows = [row for row in group_rows if row.get("direction") == "in" and row_amount(row) > 0]
    matching_positive = [row for row in positive_rows if symbols_equivalent(row.get("symbol"), requested_symbol)]
    total_requested_positive = sum((row_amount(row) for row in matching_positive), Decimal("0"))

    if total_requested_positive > 0:
        output_values: list[Decimal] = []
        value_complete = True
        for row in positive_rows:
            value = asset_value_pln(row.get("symbol", ""), row_amount(row), timestamp, nbp)
            if value is None:
                value_complete = False
                break
            output_values.append(value)

        if value_complete and output_values:
            requested_value = asset_value_pln(requested_symbol, requested_amount, timestamp, nbp)
            total_value = sum(output_values, Decimal("0"))
            if requested_value is not None and total_value > 0:
                return (
                    requested_value / total_value,
                    "output_value_fraction",
                    f"Requested output value / total tx output value using stablecoin USD proxy at {timestamp[:10]}",
                )

        return (
            requested_amount / total_requested_positive,
            "single_or_unknown_output_quantity_fraction",
            f"Requested {basis.fmt_decimal(requested_amount)} / produced {basis.fmt_decimal(total_requested_positive)} {requested_symbol}",
        )

    negative_rows = [
        row
        for row in group_rows
        if row.get("direction") in {"out", "fee"}
        and row_amount(row) < 0
        and symbols_equivalent(row.get("symbol"), requested_symbol)
    ]
    total_requested_negative = sum((-row_amount(row) for row in negative_rows), Decimal("0"))
    if total_requested_negative > 0:
        return (
            requested_amount / total_requested_negative,
            "outflow_quantity_fraction",
            f"Requested bridge/source outflow {basis.fmt_decimal(requested_amount)} / total outflow {basis.fmt_decimal(total_requested_negative)} {requested_symbol}",
        )

    return Decimal("1"), "fallback_full_tx", "Could not identify matching output/outflow quantity; used full predecessor set"


def write_csv(path: Path, rows: list[dict[str, str]]) -> None:
    fieldnames = [
        "root_tx_hash",
        "root_timestamp",
        "root_collateral_top_up_wbtc",
        "depth",
        "terminal_status",
        "terminal_tx_hash",
        "terminal_timestamp",
        "terminal_symbol",
        "terminal_amount",
        "cost_pln",
        "cost_sek",
        "allocation_method",
        "allocation_note",
        "terminal_note",
        "source_file",
        "path",
    ]
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def summarize(rows: list[dict[str, str]], topups: list[dict[str, str]]) -> dict[str, object]:
    by_status: dict[str, Decimal] = defaultdict(Decimal)
    by_root: dict[str, Decimal] = defaultdict(Decimal)
    counts = Counter(row["terminal_status"] for row in rows)
    for row in rows:
        cost = basis.parse_decimal(row.get("cost_pln"))
        by_status[row["terminal_status"]] += cost
        by_root[row["root_tx_hash"]] += cost

    exact = by_status.get("exact_koinly_transaction_history_anchor", Decimal("0"))
    stable = by_status.get("stablecoin_usd_value_proxy_source_open", Decimal("0"))
    total = sum(by_status.values(), Decimal("0"))
    return {
        "cutoff": MOVE_CUTOFF_TEXT,
        "topup_count": len(topups),
        "topup_total_wbtc": basis.fmt_decimal(sum((basis.parse_decimal(row.get("collateral_top_up")) for row in topups), Decimal("0"))),
        "terminal_row_count": len(rows),
        "terminal_status_counts": dict(sorted(counts.items())),
        "basis_pln_by_status": {key: basis.fmt_decimal(value, "0.01") for key, value in sorted(by_status.items())},
        "exact_koinly_anchor_pln": basis.fmt_decimal(exact, "0.01"),
        "stablecoin_proxy_open_pln": basis.fmt_decimal(stable, "0.01"),
        "current_supported_plus_proxy_pln": basis.fmt_decimal(total, "0.01"),
        "basis_pln_by_root": {key: basis.fmt_decimal(value, "0.01") for key, value in sorted(by_root.items())},
    }


def write_markdown(path: Path, rows: list[dict[str, str]], summary: dict[str, object]) -> None:
    lines = [
        "# Ethos WBTC Basis Roll-Forward",
        "",
        f"Cut-off: `{MOVE_CUTOFF_TEXT}`",
        "",
        "This generated workpaper scales the WBTC CDP predecessor paths to the actual collateral top-ups. It is a calculation aid for imported-basis review, not a final PIT-38 filing attachment.",
        "",
        "## Current Finding",
        "",
        f"- WBTC collateral top-ups reconciled: `{summary['topup_count']}`.",
        f"- Total WBTC collateral: `{summary['topup_total_wbtc']} WBTC`.",
        f"- Exact Koinly transaction-history anchor basis: `{summary['exact_koinly_anchor_pln']} PLN`.",
        f"- Stablecoin proxy / source-open basis: `{summary['stablecoin_proxy_open_pln']} PLN`.",
        f"- Current supported-plus-proxy roll-forward: `{summary['current_supported_plus_proxy_pln']} PLN`.",
        f"- Terminal status counts: `{json.dumps(summary['terminal_status_counts'], sort_keys=True)}`.",
        "",
        "Interpretation: exact Koinly anchors are stronger evidence. Stablecoin proxy rows are economically traceable on-chain, but still need source proof and final legal acceptance before becoming filing values. Unresolved rows should not be included without more evidence.",
        "",
        "## Basis By Status",
        "",
        "| Status | PLN |",
        "| --- | ---: |",
    ]
    by_status = summary.get("basis_pln_by_status", {})
    if isinstance(by_status, dict):
        for status, value in by_status.items():
            lines.append(f"| `{status}` | {value} |")

    lines.extend(
        [
            "",
            "## Terminal Rows",
            "",
            "| Root top-up | Depth | Status | Terminal | Amount | Cost | Note |",
            "| --- | ---: | --- | --- | ---: | ---: | --- |",
        ]
    )
    for row in rows:
        cost = row.get("cost_pln", "")
        if cost:
            cost = f"{cost} PLN"
        lines.append(
            "| `{root}` | {depth} | {status} | `{tx}` | {amount} {symbol} | {cost} | {note} |".format(
                root=row["root_tx_hash"][:10] + "...",
                depth=row["depth"],
                status=row["terminal_status"],
                tx=row["terminal_tx_hash"],
                amount=row["terminal_amount"],
                symbol=row["terminal_symbol"],
                cost=cost,
                note=(row["terminal_note"] or row["allocation_note"]).replace("|", "/"),
            )
        )

    lines.extend(
        [
            "",
            "## Filing Use",
            "",
            "- Use `exact_koinly_transaction_history_anchor` rows as the strongest current evidence for the WBTC path.",
            "- Treat `stablecoin_usd_value_proxy_source_open` rows as candidate basis only after source proof is accepted.",
            "- Do not add this roll-forward on top of the older `142,185.71 PLN` average-cost proxy; this workpaper is an alternative, more granular calculation.",
            "- Do not count ERN-funded LP/gauge positions separately from the WBTC collateral path unless a separate non-debt source is proved.",
            "",
            "## Outputs",
            "",
            "- CSV roll-forward: `move-date-wbtc-basis-rollforward.csv`",
            "- JSON summary: `move-date-wbtc-basis-rollforward-summary.json`",
            "",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")


def build(args: argparse.Namespace) -> None:
    inventory_dir = Path(args.inventory_dir)
    cdp_tx_path = inventory_dir / "move-date-cdp-transactions.csv"
    movements_path = inventory_dir / "move-date-movements.csv"
    output_csv = inventory_dir / "move-date-wbtc-basis-rollforward.csv"
    output_json = inventory_dir / "move-date-wbtc-basis-rollforward-summary.json"
    output_md = inventory_dir / "move-date-wbtc-basis-rollforward.md"

    cdp_rows = read_csv(cdp_tx_path)
    topups = [
        row
        for row in cdp_rows
        if row.get("status") == "ok"
        and row.get("relative_to_move") == "pre_move"
        and row.get("collateral_symbol") == "WBTC"
        and basis.parse_decimal(row.get("collateral_top_up")) > 0
    ]
    topups.sort(key=lambda row: (row.get("timestamp", ""), row.get("tx_hash", "")))

    movement_rows = basis.read_csv(movements_path)
    nbp = NBPClient(args.nbp_cache)
    sek_rate, sek_rate_date = nbp.get_rate_with_date("SEK", "2023-04-12")
    if not sek_rate:
        raise RuntimeError("Could not fetch SEK/PLN NBP rate for 2023-04-12")

    _, consumed_by_tx, tx_rows = basis.build_fifo(movement_rows)
    bridge_links, bridge_rows = wbtc_trace.find_bridge_links(movement_rows)
    bridge_by_dest = {
        (row["destination_chain"], "", row["destination_tx_hash"]): row
        for row in bridge_rows
    }
    # The wallet address is part of the internal key but not needed to look up
    # the displayed bridge row; tx hashes are unique within this evidence set.
    bridge_by_dest_hash = {row["destination_tx_hash"]: row for row in bridge_rows}
    koinly_index = load_koinly_transactions(Path(args.koinly_dir))

    terminal_rows: list[dict[str, str]] = []

    def walk(
        *,
        root: dict[str, str],
        source_group: tuple[str, str, str],
        requested_symbol: str,
        requested_amount: Decimal,
        requested_timestamp: str,
        depth: int,
        path: list[str],
        allocation_method: str,
        allocation_note: str,
    ) -> None:
        tx_hash = source_group[2]
        normalized_hash = norm_hash(tx_hash)
        display_tx_hash = display_hash(normalized_hash)

        terminal = koinly_terminal_cost(
            tx_hash=tx_hash,
            symbol=requested_symbol,
            amount=requested_amount,
            koinly_index=koinly_index,
            sek_rate=sek_rate,
        )
        if terminal is None:
            terminal = stable_terminal_cost(
                symbol=requested_symbol,
                amount=requested_amount,
                timestamp=requested_timestamp,
                nbp=nbp,
            )

        if terminal is not None:
            terminal_rows.append(
                {
                    "root_tx_hash": root.get("tx_hash", ""),
                    "root_timestamp": root.get("timestamp", ""),
                    "root_collateral_top_up_wbtc": root.get("collateral_top_up", ""),
                    "depth": str(depth),
                    "terminal_status": terminal.status,
                    "terminal_tx_hash": display_tx_hash,
                    "terminal_timestamp": requested_timestamp,
                    "terminal_symbol": requested_symbol,
                    "terminal_amount": basis.fmt_decimal(requested_amount),
                    "cost_pln": basis.fmt_decimal(terminal.cost_pln, "0.01"),
                    "cost_sek": basis.fmt_decimal(terminal.cost_sek, "0.01") if terminal.cost_sek else "",
                    "allocation_method": allocation_method,
                    "allocation_note": allocation_note,
                    "terminal_note": terminal.note,
                    "source_file": terminal.source_file,
                    "path": " > ".join(path + [display_tx_hash]),
                }
            )
            return

        if tx_hash == "ARCHIVE_GAP_OR_PREHISTORY" or depth >= args.max_depth:
            status = "archive_gap_or_pre_history" if tx_hash == "ARCHIVE_GAP_OR_PREHISTORY" else "max_depth_unresolved"
            terminal_rows.append(
                {
                    "root_tx_hash": root.get("tx_hash", ""),
                    "root_timestamp": root.get("timestamp", ""),
                    "root_collateral_top_up_wbtc": root.get("collateral_top_up", ""),
                    "depth": str(depth),
                    "terminal_status": status,
                    "terminal_tx_hash": display_tx_hash,
                    "terminal_timestamp": requested_timestamp,
                    "terminal_symbol": requested_symbol,
                    "terminal_amount": basis.fmt_decimal(requested_amount),
                    "cost_pln": "",
                    "cost_sek": "",
                    "allocation_method": allocation_method,
                    "allocation_note": allocation_note,
                    "terminal_note": "No terminal cost evidence found before trace stopped",
                    "source_file": "",
                    "path": " > ".join(path + [display_tx_hash]),
                }
            )
            return

        next_group = source_group
        next_symbol = requested_symbol
        next_amount = requested_amount
        bridge_row = bridge_by_dest_hash.get(tx_hash)
        if source_group in bridge_links and bridge_row:
            source_amount = basis.parse_decimal(bridge_row.get("source_amount"))
            dest_amount = basis.parse_decimal(bridge_row.get("destination_amount"))
            if dest_amount > 0:
                next_amount = requested_amount * source_amount / dest_amount
            next_group = bridge_links[source_group]
            next_symbol = bridge_row.get("source_symbol", requested_symbol)

        group_rows = tx_rows.get(next_group, [])
        if not group_rows:
            terminal_rows.append(
                {
                    "root_tx_hash": root.get("tx_hash", ""),
                    "root_timestamp": root.get("timestamp", ""),
                    "root_collateral_top_up_wbtc": root.get("collateral_top_up", ""),
                    "depth": str(depth),
                    "terminal_status": "missing_transaction_rows_unresolved",
                    "terminal_tx_hash": display_tx_hash,
                    "terminal_timestamp": requested_timestamp,
                    "terminal_symbol": requested_symbol,
                    "terminal_amount": basis.fmt_decimal(requested_amount),
                    "cost_pln": "",
                    "cost_sek": "",
                    "allocation_method": allocation_method,
                    "allocation_note": allocation_note,
                    "terminal_note": "No transaction rows found for source group",
                    "source_file": "",
                    "path": " > ".join(path + [display_tx_hash]),
                }
            )
            return

        scale, scale_method, scale_note = allocation_scale(
            group_rows=group_rows,
            requested_symbol=next_symbol,
            requested_amount=next_amount,
            nbp=nbp,
        )
        predecessors = wbtc_trace.consumption_rows_for_tx(next_group, consumed_by_tx)
        if not predecessors:
            terminal_rows.append(
                {
                    "root_tx_hash": root.get("tx_hash", ""),
                    "root_timestamp": root.get("timestamp", ""),
                    "root_collateral_top_up_wbtc": root.get("collateral_top_up", ""),
                    "depth": str(depth),
                    "terminal_status": "no_predecessor_unresolved",
                    "terminal_tx_hash": display_tx_hash,
                    "terminal_timestamp": requested_timestamp,
                    "terminal_symbol": requested_symbol,
                    "terminal_amount": basis.fmt_decimal(requested_amount),
                    "cost_pln": "",
                    "cost_sek": "",
                    "allocation_method": scale_method,
                    "allocation_note": scale_note,
                    "terminal_note": "No predecessor lots found for this transaction",
                    "source_file": "",
                    "path": " > ".join(path + [display_tx_hash]),
                }
            )
            return

        next_path = path + [display_tx_hash]
        for predecessor in predecessors:
            child_amount = abs(predecessor.source_amount) * scale
            if child_amount <= 0:
                continue
            walk(
                root=root,
                source_group=wbtc_trace.source_tx_key(predecessor),
                requested_symbol=predecessor.source_symbol,
                requested_amount=child_amount,
                requested_timestamp=predecessor.source_timestamp or predecessor.timestamp,
                depth=depth + 1,
                path=next_path,
                allocation_method=scale_method,
                allocation_note=scale_note,
            )

    for root in topups:
        root_key = wbtc_trace.tx_key_from_row(root)
        root_consumptions = [
            item
            for item in wbtc_trace.consumption_rows_for_tx(root_key, consumed_by_tx)
            if basis.normalize_symbol(item.out_symbol) == "WBTC"
        ]
        for consumption in root_consumptions:
            walk(
                root=root,
                source_group=wbtc_trace.source_tx_key(consumption),
                requested_symbol=consumption.source_symbol,
                requested_amount=abs(consumption.source_amount),
                requested_timestamp=consumption.source_timestamp or consumption.timestamp,
                depth=0,
                path=[root.get("tx_hash", "")],
                allocation_method="root_lot_consumption",
                allocation_note="Actual WBTC lot consumed by Ethos trove top-up",
            )

    summary = summarize(terminal_rows, topups)
    summary["sek_rate"] = basis.fmt_decimal(sek_rate)
    summary["sek_rate_date"] = sek_rate_date
    write_csv(output_csv, terminal_rows)
    output_json.write_text(json.dumps(summary, indent=2, sort_keys=True), encoding="utf-8")
    write_markdown(output_md, terminal_rows, summary)
    print(json.dumps(summary, indent=2, sort_keys=True))


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--inventory-dir", default=str(DEFAULT_INVENTORY_DIR))
    parser.add_argument("--koinly-dir", default=str(DEFAULT_KOINLY_DIR))
    parser.add_argument("--nbp-cache", default=str(REPO_ROOT / "data/nbp_cache.json"))
    parser.add_argument("--max-depth", type=int, default=12)
    build(parser.parse_args())


if __name__ == "__main__":
    main()
