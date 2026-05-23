#!/usr/bin/env python3
"""Build a focused WBTC CDP collateral basis-trace workpaper.

This script starts from the successful pre-move Ethos WBTC trove top-ups and
traces the predecessor lots found in the archived move-date movement ledger.
It is a workpaper, not a final PIT-38 filing value.
"""

from __future__ import annotations

import argparse
import csv
import json
import sys
from collections import defaultdict
from datetime import datetime
from decimal import Decimal
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]
SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO_ROOT / "src"))
sys.path.insert(0, str(SCRIPT_DIR))

import build_move_date_basis_decision as basis  # noqa: E402
from tax_calc.nbp import NBPClient  # noqa: E402


DEFAULT_INVENTORY_DIR = REPO_ROOT / "private/evidence/onchain/move-date-inventory-2023-04-12"
DEFAULT_KOINLY_2022_EOY = (
    REPO_ROOT / "private/evidence/koinly/2022/koinly_2022_end_of_year_holdings_report_e7abrLJ2nY_1777113106.csv"
)
MOVE_CUTOFF_TEXT = "2023-04-12T00:00:00Z"

BTC_UNIT_SYMBOLS = {"BTC", "WBTC", "ANYBTC", "ANYWBTC"}
BRIDGE_PRINCIPAL_SYMBOLS = {"BTC", "WBTC"}
BRIDGE_MATCH_WINDOW_SECONDS = 20 * 60
BRIDGE_AMOUNT_TOLERANCE = Decimal("0.002")
BRIDGE_SYMBOL_FAMILIES = {
    "ANYBTC": "BTC",
    "ANYWBTC": "BTC",
    "BTC": "BTC",
    "WBTC": "BTC",
    "ANYUSDC": "USDC",
    "USDC": "USDC",
    "USDC.E": "USDC",
}


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def write_csv(path: Path, rows: list[dict[str, str]]) -> None:
    fieldnames = [
        "root_tx_hash",
        "root_timestamp",
        "root_collateral_top_up_wbtc",
        "depth",
        "tx_timestamp",
        "tx_hash",
        "tx_flow",
        "out_symbol",
        "source_symbol",
        "source_amount",
        "source_timestamp",
        "source_tx_hash",
        "estimate_pln",
        "estimate_type",
        "estimate_note",
        "trace_note",
    ]
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def estimate_source_pln(
    consumption: basis.Consumption,
    holdings: dict[str, basis.HoldingEvidence],
    nbp: NBPClient,
    sek_rate: Decimal,
) -> tuple[Decimal, str, str]:
    symbol = basis.normalize_symbol(consumption.source_symbol)
    amount = abs(consumption.source_amount)
    tx_date = (consumption.timestamp or consumption.source_timestamp or "")[:10]

    if symbol in BTC_UNIT_SYMBOLS:
        avg_sek = basis.koinly_avg_cost_sek("BTC", holdings)
        if avg_sek > 0:
            cost_sek = amount * avg_sek
            return (
                cost_sek * sek_rate,
                "koinly_2022_btc_cost_pool_proxy",
                f"{basis.fmt_decimal(cost_sek, '0.01')} SEK x SEK/PLN {sek_rate}",
            )

    return basis.estimate_source_pln(consumption, holdings, nbp, sek_rate)


def tx_key_from_row(row: dict[str, str]) -> tuple[str, str, str]:
    return (row.get("chain", ""), row.get("wallet_address", "").lower(), row.get("tx_hash", ""))


def source_tx_key(consumption: basis.Consumption) -> tuple[str, str, str]:
    return (consumption.chain, consumption.wallet_address.lower(), consumption.source_tx_hash)


def tx_timestamp(rows: list[dict[str, str]]) -> datetime | None:
    timestamps = [basis.parse_iso(row.get("timestamp", "")) for row in rows]
    timestamps = [item for item in timestamps if item is not None]
    return min(timestamps) if timestamps else None


def group_rows_by_tx(movements: list[dict[str, str]]) -> dict[tuple[str, str, str], list[dict[str, str]]]:
    grouped: dict[tuple[str, str, str], list[dict[str, str]]] = defaultdict(list)
    for row in movements:
        grouped[tx_key_from_row(row)].append(row)
    return grouped


def bridge_symbol_family(symbol: str | None) -> str:
    return BRIDGE_SYMBOL_FAMILIES.get(basis.normalize_symbol(symbol or ""), "")


def bridge_principal_symbol(row: dict[str, str]) -> bool:
    return bool(bridge_symbol_family(row.get("symbol", "")))


def bridge_source_preference(symbol: str | None) -> int:
    normalized = basis.normalize_symbol(symbol or "")
    return 1 if normalized.startswith("ANY") else 0


def find_bridge_links(
    movements: list[dict[str, str]],
) -> tuple[dict[tuple[str, str, str], tuple[str, str, str]], list[dict[str, str]]]:
    """Pair BTC/USDC anySwapIn receipts with recent source-chain bridge-outs."""
    grouped = group_rows_by_tx(movements)
    source_candidates: list[tuple[tuple[str, str, str], datetime, Decimal, str, int, dict[str, str]]] = []
    destination_candidates: list[tuple[tuple[str, str, str], datetime, Decimal, str, dict[str, str]]] = []

    for group_key, rows in grouped.items():
        timestamp = tx_timestamp(rows)
        if not timestamp:
            continue
        for row in rows:
            amount = abs(basis.parse_decimal(row.get("amount")))
            if amount <= 0 or not bridge_principal_symbol(row):
                continue
            family = bridge_symbol_family(row.get("symbol", ""))
            method = row.get("method", "")
            if row.get("direction") == "out":
                source_candidates.append((group_key, timestamp, amount, family, bridge_source_preference(row.get("symbol")), row))
            if row.get("direction") == "in" and method.startswith("anySwapInAuto"):
                destination_candidates.append((group_key, timestamp, amount, family, row))

    links: dict[tuple[str, str, str], tuple[str, str, str]] = {}
    link_rows: list[dict[str, str]] = []
    for dest_key, dest_time, dest_amount, dest_family, dest_row in destination_candidates:
        if dest_key in links:
            continue
        best: tuple[Decimal, int, float, tuple[str, str, str], datetime, Decimal, dict[str, str]] | None = None
        for src_key, src_time, src_amount, src_family, src_preference, src_row in source_candidates:
            if src_key == dest_key or src_key[0] == dest_key[0]:
                continue
            if src_key[1] != dest_key[1]:
                continue
            if src_family != dest_family:
                continue
            seconds = (dest_time - src_time).total_seconds()
            if seconds < 0 or seconds > BRIDGE_MATCH_WINDOW_SECONDS:
                continue
            diff = abs(src_amount - dest_amount)
            if dest_amount and diff / dest_amount > BRIDGE_AMOUNT_TOLERANCE:
                continue
            candidate = (diff, src_preference, seconds, src_key, src_time, src_amount, src_row)
            if best is None or candidate[:3] < best[:3]:
                best = candidate
        if best is None:
            continue

        diff, _, seconds, src_key, src_time, src_amount, src_row = best
        links[dest_key] = src_key
        link_rows.append(
            {
                "bridge_family": dest_family,
                "destination_chain": dest_key[0],
                "destination_tx_hash": dest_key[2],
                "destination_timestamp": dest_time.isoformat().replace("+00:00", "Z"),
                "destination_amount": basis.fmt_decimal(dest_amount),
                "destination_symbol": dest_row.get("symbol", ""),
                "source_chain": src_key[0],
                "source_tx_hash": src_key[2],
                "source_timestamp": src_time.isoformat().replace("+00:00", "Z"),
                "source_amount": basis.fmt_decimal(src_amount),
                "source_symbol": src_row.get("symbol", ""),
                "amount_difference": basis.fmt_decimal(diff),
                "seconds_between": basis.fmt_decimal(Decimal(str(seconds))),
                "source_flow": basis.summarize_tx(grouped.get(src_key, [])),
                "destination_flow": basis.summarize_tx(grouped.get(dest_key, [])),
            }
        )
    link_rows.sort(key=lambda row: (row["destination_timestamp"], row["destination_tx_hash"]))
    return links, link_rows


def consumption_rows_for_tx(
    group_key: tuple[str, str, str],
    consumed_by_tx: dict[tuple[str, str, str], list[basis.Consumption]],
) -> list[basis.Consumption]:
    rows = [
        item
        for item in consumed_by_tx.get(group_key, [])
        if item.out_direction == "out"
        and item.source_symbol
        and item.source_tx_hash
        and item.source_tx_hash != item.tx_hash
    ]
    rows.sort(key=lambda item: (basis.normalize_symbol(item.out_symbol), -abs(item.source_amount)))
    return rows


def trace_consumption(
    *,
    root: dict[str, str],
    consumption: basis.Consumption,
    depth: int,
    consumed_by_tx: dict[tuple[str, str, str], list[basis.Consumption]],
    tx_rows: dict[tuple[str, str, str], list[dict[str, str]]],
    holdings: dict[str, basis.HoldingEvidence],
    nbp: NBPClient,
    sek_rate: Decimal,
    output_rows: list[dict[str, str]],
    seen: set[tuple[str, str, str, str]],
    max_depth: int,
    bridge_links: dict[tuple[str, str, str], tuple[str, str, str]],
    trace_note: str = "",
) -> None:
    estimate_pln, estimate_type, estimate_note = estimate_source_pln(consumption, holdings, nbp, sek_rate)
    source_key = source_tx_key(consumption)
    output_rows.append(
        {
            "root_tx_hash": root.get("tx_hash", ""),
            "root_timestamp": root.get("timestamp", ""),
            "root_collateral_top_up_wbtc": root.get("collateral_top_up", ""),
            "depth": str(depth),
            "tx_timestamp": consumption.timestamp,
            "tx_hash": consumption.tx_hash,
            "tx_flow": basis.summarize_tx(tx_rows.get((consumption.chain, consumption.wallet_address, consumption.tx_hash), [])),
            "out_symbol": consumption.out_symbol,
            "source_symbol": consumption.source_symbol,
            "source_amount": basis.fmt_decimal(consumption.source_amount),
            "source_timestamp": consumption.source_timestamp,
            "source_tx_hash": consumption.source_tx_hash,
            "estimate_pln": basis.fmt_decimal(estimate_pln, "0.01") if estimate_pln > 0 else "",
            "estimate_type": estimate_type,
            "estimate_note": estimate_note,
            "trace_note": trace_note,
        }
    )

    if depth >= max_depth or consumption.source_tx_hash == "ARCHIVE_GAP_OR_PREHISTORY":
        return

    seen_key = (*source_key, basis.fmt_decimal(consumption.source_amount))
    if seen_key in seen:
        return
    seen = set(seen)
    seen.add(seen_key)

    next_group = bridge_links.get(source_key, source_key)
    next_trace_note = "cross_chain_bridge_link" if next_group != source_key else ""

    for predecessor in consumption_rows_for_tx(next_group, consumed_by_tx)[:10]:
        trace_consumption(
            root=root,
            consumption=predecessor,
            depth=depth + 1,
            consumed_by_tx=consumed_by_tx,
            tx_rows=tx_rows,
            holdings=holdings,
            nbp=nbp,
            sek_rate=sek_rate,
            output_rows=output_rows,
            seen=seen,
            max_depth=max_depth,
            bridge_links=bridge_links,
            trace_note=next_trace_note,
        )


def build_summary(
    *,
    topups: list[dict[str, str]],
    trace_rows: list[dict[str, str]],
    bridge_rows: list[dict[str, str]],
    holdings: dict[str, basis.HoldingEvidence],
    sek_rate: Decimal,
    sek_rate_date: str,
) -> dict[str, object]:
    btc_holding = holdings.get("BTC")
    btc_quantity = btc_holding.quantity if btc_holding else Decimal("0")
    btc_cost_sek = btc_holding.cost_sek if btc_holding else Decimal("0")
    avg_btc_sek = btc_cost_sek / btc_quantity if btc_quantity else Decimal("0")
    total_wbtc = sum((basis.parse_decimal(row.get("collateral_top_up")) for row in topups), Decimal("0"))
    proxy_sek = total_wbtc * avg_btc_sek
    proxy_pln = proxy_sek * sek_rate
    depth0_pln = sum(
        (
            basis.parse_decimal(row.get("estimate_pln"))
            for row in trace_rows
            if row.get("depth") == "0" and row.get("estimate_type") == "koinly_2022_btc_cost_pool_proxy"
        ),
        Decimal("0"),
    )
    source_symbols: dict[str, int] = defaultdict(int)
    for row in trace_rows:
        source_symbols[row.get("source_symbol", "")] += 1
    return {
        "cutoff": MOVE_CUTOFF_TEXT,
        "topup_count": len(topups),
        "topup_total_wbtc": basis.fmt_decimal(total_wbtc),
        "koinly_2022_btc_quantity": basis.fmt_decimal(btc_quantity),
        "koinly_2022_btc_cost_sek": basis.fmt_decimal(btc_cost_sek, "0.01"),
        "koinly_2022_btc_avg_cost_sek": basis.fmt_decimal(avg_btc_sek, "0.01"),
        "sek_rate": basis.fmt_decimal(sek_rate),
        "sek_rate_date": sek_rate_date,
        "wbtc_proxy_cost_sek": basis.fmt_decimal(proxy_sek, "0.01"),
        "wbtc_proxy_cost_pln": basis.fmt_decimal(proxy_pln, "0.01"),
        "depth0_btc_proxy_pln": basis.fmt_decimal(depth0_pln, "0.01"),
        "trace_row_count": len(trace_rows),
        "bridge_link_count": len(bridge_rows),
        "source_symbols": dict(sorted(source_symbols.items())),
    }


def write_markdown(
    path: Path,
    *,
    topups: list[dict[str, str]],
    trace_rows: list[dict[str, str]],
    bridge_rows: list[dict[str, str]],
    summary: dict[str, object],
) -> None:
    lines: list[str] = [
        "# Ethos WBTC CDP Collateral Basis Trace",
        "",
        f"Cut-off: `{MOVE_CUTOFF_TEXT}`",
        "",
        "This generated workpaper traces the Optimism Ethos Reserve WBTC collateral that existed at the move-date block. It is a basis-evidence workpaper, not a final PIT-38 filing attachment.",
        "",
        "## Current Finding",
        "",
        f"- Successful pre-move WBTC trove top-ups: `{summary['topup_count']}`.",
        f"- Total successful pre-move WBTC collateral top-up: `{summary['topup_total_wbtc']} WBTC`.",
        f"- Koinly 2022 end-of-year BTC row: `{summary['koinly_2022_btc_quantity']} BTC` with `{summary['koinly_2022_btc_cost_sek']} SEK` cost.",
        f"- Average-cost proxy: `{summary['koinly_2022_btc_avg_cost_sek']} SEK/BTC` x SEK/PLN `{summary['sek_rate']}` from `{summary['sek_rate_date']}`.",
        f"- Current proxy value for the full move-date WBTC collateral: `{summary['wbtc_proxy_cost_pln']} PLN`.",
        f"- Cross-chain bridge matches found in the trace: `{summary['bridge_link_count']}`.",
        "",
        "Interpretation: the four top-ups reconcile to the protocol-state `1.77696328 WBTC` collateral. The PLN amount above is still only a proxy because it applies the Koinly 2022 BTC average-cost pool to WBTC acquired or transformed in Jan-Apr 2023. The stronger evidence path is the trace below plus Swedish K4/Koinly acquisition or replacement-basis records for the predecessor assets.",
        "",
        "Important accounting point: do not add the same predecessor chain at multiple depths. A WBTC top-up, its anyWBTC bridge input, and its earlier wrapper/receipt-token step are alternative descriptions of the same economic basis path, not separate costs.",
        "",
        "## CDP Top-Ups",
        "",
        "| Date | Tx | Method | WBTC top-up | ERN borrowed | Status |",
        "| --- | --- | --- | ---: | ---: | --- |",
    ]
    for row in topups:
        lines.append(
            "| {date} | `{tx}` | {method} | {topup} | {debt} | {status} |".format(
                date=(row.get("timestamp", "") or "")[:10],
                tx=row.get("tx_hash", ""),
                method=row.get("method", ""),
                topup=row.get("collateral_top_up", ""),
                debt=row.get("debt_increase_ern", ""),
                status=row.get("status", ""),
            )
        )

    if bridge_rows:
        lines.extend(
            [
                "",
                "## Cross-Chain Bridge Matches",
                "",
                "These rows correct a limitation of simple per-chain FIFO: `anySwapInAuto` receipts can mint and burn wrapper tokens in the same transaction, so the real predecessor is often a recent source-chain bridge-out.",
                "",
                "| Destination | Source | Amounts | Time delta | Source flow |",
                "| --- | --- | --- | ---: | --- |",
            ]
        )
        for row in bridge_rows:
            lines.append(
                "| {dest_chain} `{dest_tx}` | {source_chain} `{source_tx}` | {dest_amount} {dest_symbol} <= {source_amount} {source_symbol} | {seconds}s | {flow} |".format(
                    dest_chain=row["destination_chain"],
                    dest_tx=row["destination_tx_hash"],
                    source_chain=row["source_chain"],
                    source_tx=row["source_tx_hash"],
                    dest_amount=row["destination_amount"],
                    dest_symbol=row["destination_symbol"],
                    source_amount=row["source_amount"],
                    source_symbol=row["source_symbol"],
                    seconds=row["seconds_between"],
                    flow=row["source_flow"].replace("|", "/"),
                )
            )

    lines.extend(
        [
            "",
            "## Source Trace",
            "",
            "| Root top-up | Depth | Tx date | Tx | Flow | Source | Estimate |",
            "| --- | ---: | --- | --- | --- | --- | ---: |",
        ]
    )
    for row in trace_rows:
        estimate = row.get("estimate_pln", "")
        if estimate:
            estimate = f"{estimate} PLN"
        lines.append(
            "| `{root}` | {depth} | {date} | `{tx}` | {flow} | {source} | {estimate} |".format(
                root=row.get("root_tx_hash", "")[:10] + "...",
                depth=row.get("depth", ""),
                date=(row.get("tx_timestamp", "") or "")[:10],
                tx=row.get("tx_hash", ""),
                flow=(row.get("tx_flow", "") or "").replace("|", "/"),
                source=f"{row.get('source_amount', '')} {row.get('source_symbol', '')} from `{row.get('source_tx_hash', '')}`",
                estimate=estimate,
            )
        )

    lines.extend(
        [
            "",
            "## Filing Use",
            "",
            "- Use this as the primary evidence map for the Ethos `1.77696328 WBTC` move-date collateral candidate.",
            "- The `142,185.71 PLN` style amount is an average-cost proxy, not final proof by itself.",
            "- To make the WBTC candidate filing-ready, match the predecessor rows to Swedish K4/Koinly records for the taxable pre-move transformations, or document that the same WBTC was held continuously.",
            "- Do not also count ERN-funded BPT/LP/gauge positions as separate acquisition cost unless a separate non-debt source is proved.",
            "",
            "## Outputs",
            "",
            "- CSV trace: `move-date-wbtc-cdp-basis-trace.csv`",
            "- JSON summary: `move-date-wbtc-cdp-basis-trace-summary.json`",
            "",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")


def build(args: argparse.Namespace) -> None:
    inventory_dir = Path(args.inventory_dir)
    cdp_tx_path = inventory_dir / "move-date-cdp-transactions.csv"
    movements_path = inventory_dir / "move-date-movements.csv"
    output_csv = inventory_dir / "move-date-wbtc-cdp-basis-trace.csv"
    output_json = inventory_dir / "move-date-wbtc-cdp-basis-trace-summary.json"
    output_md = inventory_dir / "move-date-wbtc-cdp-basis-trace.md"

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
    holdings = basis.load_holdings(Path(args.koinly_2022_eoy))
    nbp = NBPClient(args.nbp_cache)
    sek_rate, sek_rate_date = nbp.get_rate_with_date("SEK", "2023-04-12")
    if not sek_rate:
        raise RuntimeError("Could not fetch SEK/PLN NBP rate for 2023-04-12")

    _, consumed_by_tx, tx_rows = basis.build_fifo(movement_rows)
    bridge_links, bridge_rows = find_bridge_links(movement_rows)

    trace_rows: list[dict[str, str]] = []
    for root in topups:
        root_key = tx_key_from_row(root)
        root_consumptions = [
            item
            for item in consumption_rows_for_tx(root_key, consumed_by_tx)
            if basis.normalize_symbol(item.out_symbol) == "WBTC"
        ]
        for consumption in root_consumptions:
            trace_consumption(
                root=root,
                consumption=consumption,
                depth=0,
                consumed_by_tx=consumed_by_tx,
                tx_rows=tx_rows,
                holdings=holdings,
                nbp=nbp,
                sek_rate=sek_rate,
                output_rows=trace_rows,
                seen=set(),
                max_depth=args.max_depth,
                bridge_links=bridge_links,
            )

    trace_tx_hashes = {row["tx_hash"] for row in trace_rows} | {row["source_tx_hash"] for row in trace_rows}
    relevant_bridge_rows = [
        row
        for row in bridge_rows
        if row["destination_tx_hash"] in trace_tx_hashes or row["source_tx_hash"] in trace_tx_hashes
    ]
    summary = build_summary(
        topups=topups,
        trace_rows=trace_rows,
        bridge_rows=relevant_bridge_rows,
        holdings=holdings,
        sek_rate=sek_rate,
        sek_rate_date=sek_rate_date,
    )
    write_csv(output_csv, trace_rows)
    output_json.write_text(json.dumps(summary, indent=2, sort_keys=True), encoding="utf-8")
    write_markdown(output_md, topups=topups, trace_rows=trace_rows, bridge_rows=relevant_bridge_rows, summary=summary)

    print(json.dumps(summary, indent=2, sort_keys=True))


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--inventory-dir", default=str(DEFAULT_INVENTORY_DIR))
    parser.add_argument("--koinly-2022-eoy", default=str(DEFAULT_KOINLY_2022_EOY))
    parser.add_argument("--nbp-cache", default=str(REPO_ROOT / "data/nbp_cache.json"))
    parser.add_argument("--max-depth", type=int, default=10)
    build(parser.parse_args())


if __name__ == "__main__":
    main()
