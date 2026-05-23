#!/usr/bin/env python3
"""Build a focused evidence checklist for the Ethos WBTC CDP basis trace.

The checklist compares transaction hashes from ``move-date-wbtc-cdp-basis-trace``
with available Koinly transaction-history exports. It does not compute final
replacement basis.
"""

from __future__ import annotations

import argparse
import csv
import json
from collections import Counter, defaultdict
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_INVENTORY_DIR = REPO_ROOT / "private/evidence/onchain/move-date-inventory-2023-04-12"
DEFAULT_KOINLY_DIR = REPO_ROOT / "private/evidence/koinly"


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


def normalize_hash(value: str | None) -> str:
    text = (value or "").strip().lower()
    if text.startswith("0x"):
        return text[2:]
    return text


def prefixed_hash(value: str) -> str:
    if not value or value == "archive_gap_or_prehistory":
        return value.upper()
    return "0x" + value


def join_values(values: set[str], limit: int = 8) -> str:
    items = sorted(item for item in values if item)
    if len(items) > limit:
        return "; ".join(items[:limit]) + f"; +{len(items) - limit} more"
    return "; ".join(items)


def compact_koinly_row(row: dict[str, str]) -> str:
    parts = [
        row.get("Date", ""),
        row.get("Type", ""),
        f"sent {row.get('Sent Amount', '')} {row.get('Sent Currency', '')}".strip(),
        f"sent cost {row.get('Sent Cost Basis', '')} SEK".strip(),
        f"received {row.get('Received Amount', '')} {row.get('Received Currency', '')}".strip(),
        f"received cost {row.get('Received Cost Basis', '')} SEK".strip(),
        f"gain {row.get('Gain (SEK)', '')} SEK".strip(),
        f"net {row.get('Net Value (SEK)', '')} SEK".strip(),
    ]
    return " | ".join(part for part in parts if part)


def load_koinly_transactions(koinly_dir: Path) -> dict[str, list[dict[str, str]]]:
    index: dict[str, list[dict[str, str]]] = defaultdict(list)
    for path in sorted(koinly_dir.glob("*/*transaction_history*.csv")):
        year = path.parent.name
        for row in read_csv_after_header(path, "Date,"):
            tx_hash = normalize_hash(row.get("TxHash"))
            if not tx_hash:
                continue
            enriched = dict(row)
            enriched["_source_file"] = str(path.relative_to(REPO_ROOT))
            enriched["_year"] = year
            index[tx_hash].append(enriched)
    return index


def evidence_status(timestamp: str, matches: list[dict[str, str]], has_archive_gap: bool) -> tuple[str, str]:
    if matches:
        return (
            "exact_koinly_transaction_history_match",
            "Use matched Koinly rows and, if needed, tie them to the filed Swedish K4/PDF totals.",
        )
    if has_archive_gap:
        return (
            "archive_gap_or_prehistory",
            "Needs upstream wallet/bridge history or a documented decision to leave this branch unresolved.",
        )
    year = (timestamp or "")[:4]
    if year == "2023":
        return (
            "onchain_only_pre_move_2023_no_koinly_export",
            "Self-calculate Jan-Apr 2023 replacement basis from on-chain trace; no 2023 Koinly export is in the repo.",
        )
    if year == "2021":
        return (
            "no_2021_koinly_export",
            "Use on-chain evidence or obtain/build 2021 Koinly-style transaction history if this branch becomes material.",
        )
    if year in {"2020", "2022"}:
        return (
            "no_exact_match_in_available_koinly_export",
            "Review hash formatting, wallet coverage, or Koinly export completeness.",
        )
    return (
        "unmatched_or_missing_timestamp",
        "Review manually.",
    )


def build_rows(trace_rows: list[dict[str, str]], koinly_index: dict[str, list[dict[str, str]]]) -> list[dict[str, str]]:
    facts: dict[str, dict[str, set[str]]] = defaultdict(lambda: defaultdict(set))
    archive_gap_rows = 0

    for row in trace_rows:
        tx_hash = normalize_hash(row.get("tx_hash"))
        source_hash = normalize_hash(row.get("source_tx_hash"))
        if tx_hash:
            facts[tx_hash]["roles"].add("trace_tx")
            facts[tx_hash]["timestamps"].add(row.get("tx_timestamp", ""))
            facts[tx_hash]["depths"].add(row.get("depth", ""))
            facts[tx_hash]["flows"].add(row.get("tx_flow", ""))
            facts[tx_hash]["roots"].add(row.get("root_tx_hash", ""))
        if source_hash == "archive_gap_or_prehistory":
            archive_gap_rows += 1
            continue
        if source_hash:
            facts[source_hash]["roles"].add("source_tx")
            facts[source_hash]["timestamps"].add(row.get("source_timestamp", "") or row.get("tx_timestamp", ""))
            facts[source_hash]["depths"].add(row.get("depth", ""))
            facts[source_hash]["source_symbols"].add(row.get("source_symbol", ""))
            facts[source_hash]["source_amounts"].add(f"{row.get('source_amount', '')} {row.get('source_symbol', '')}".strip())
            facts[source_hash]["roots"].add(row.get("root_tx_hash", ""))

    output: list[dict[str, str]] = []
    for tx_hash, fact in sorted(facts.items(), key=lambda item: (min(item[1]["timestamps"] or {""}), item[0])):
        timestamps = sorted(item for item in fact["timestamps"] if item)
        first_timestamp = timestamps[0] if timestamps else ""
        matches = koinly_index.get(tx_hash, [])
        status, next_step = evidence_status(first_timestamp, matches, False)
        years = {row.get("_year", "") for row in matches}
        files = {row.get("_source_file", "") for row in matches}
        output.append(
            {
                "tx_hash": prefixed_hash(tx_hash),
                "first_seen_timestamp": first_timestamp,
                "trace_roles": join_values(fact["roles"]),
                "trace_depths": join_values(fact["depths"]),
                "root_count": str(len(fact["roots"])),
                "source_symbols": join_values(fact["source_symbols"]),
                "source_amounts": join_values(fact["source_amounts"], limit=12),
                "trace_flows": join_values(fact["flows"], limit=4),
                "evidence_status": status,
                "koinly_match_count": str(len(matches)),
                "koinly_years": join_values(years),
                "koinly_files": join_values(files, limit=4),
                "koinly_rows": " || ".join(compact_koinly_row(row) for row in matches[:6]),
                "recommended_next_step": next_step,
            }
        )

    if archive_gap_rows:
        status, next_step = evidence_status("", [], True)
        output.append(
            {
                "tx_hash": "ARCHIVE_GAP_OR_PREHISTORY",
                "first_seen_timestamp": "",
                "trace_roles": "source_tx",
                "trace_depths": "",
                "root_count": "",
                "source_symbols": "",
                "source_amounts": "",
                "trace_flows": "",
                "evidence_status": status,
                "koinly_match_count": "0",
                "koinly_years": "",
                "koinly_files": "",
                "koinly_rows": "",
                "recommended_next_step": f"{archive_gap_rows} WBTC trace rows point to archive gaps or prehistory. {next_step}",
            }
        )

    return output


def write_csv(path: Path, rows: list[dict[str, str]]) -> None:
    fieldnames = [
        "tx_hash",
        "first_seen_timestamp",
        "trace_roles",
        "trace_depths",
        "root_count",
        "source_symbols",
        "source_amounts",
        "trace_flows",
        "evidence_status",
        "koinly_match_count",
        "koinly_years",
        "koinly_files",
        "koinly_rows",
        "recommended_next_step",
    ]
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def build_summary(rows: list[dict[str, str]], koinly_index: dict[str, list[dict[str, str]]]) -> dict[str, object]:
    statuses = Counter(row["evidence_status"] for row in rows)
    matched = [row for row in rows if row["evidence_status"] == "exact_koinly_transaction_history_match"]
    return {
        "unique_trace_hashes_including_archive_gap": len(rows),
        "exact_koinly_matches": len(matched),
        "available_koinly_transaction_hashes": len(koinly_index),
        "status_counts": dict(sorted(statuses.items())),
        "matched_years": dict(sorted(Counter(row["koinly_years"] for row in matched).items())),
    }


def write_markdown(path: Path, rows: list[dict[str, str]], summary: dict[str, object]) -> None:
    lines = [
        "# Ethos WBTC Swedish Evidence Checklist",
        "",
        "This generated checklist compares the WBTC CDP basis trace against the available Koinly transaction-history exports. It is an evidence-control workpaper, not a final PIT-38 imported-basis calculation.",
        "",
        "## Current Finding",
        "",
        f"- Unique trace hashes / archive-gap bucket: `{summary['unique_trace_hashes_including_archive_gap']}`.",
        f"- Exact Koinly transaction-history matches: `{summary['exact_koinly_matches']}`.",
        f"- Available Koinly transaction hashes indexed: `{summary['available_koinly_transaction_hashes']}`.",
        f"- Status counts: `{json.dumps(summary['status_counts'], sort_keys=True)}`.",
        "",
        "Interpretation: the current repo evidence already matches the visible 2022 WBTC predecessor transactions by exact Koinly transaction hash. The remaining unmatched non-archive hashes are Jan-Apr 2023 pre-move on-chain transactions, where no 2023 Koinly export is present. Those need a self-calculated replacement-basis chain or a later Koinly export, not another 2022 K4 form.",
        "",
        "## Exact Koinly Matches",
        "",
        "| Date | Tx | Trace symbols | Koinly rows |",
        "| --- | --- | --- | --- |",
    ]
    for row in rows:
        if row["evidence_status"] != "exact_koinly_transaction_history_match":
            continue
        lines.append(
            "| {date} | `{tx}` | {symbols} | {koinly} |".format(
                date=(row["first_seen_timestamp"] or "")[:10],
                tx=row["tx_hash"],
                symbols=(row["source_amounts"] or row["source_symbols"] or "").replace("|", "/"),
                koinly=(row["koinly_rows"] or "").replace("|", "/"),
            )
        )

    lines.extend(
        [
            "",
            "## Open Items",
            "",
            "| Status | Count | Meaning |",
            "| --- | ---: | --- |",
        ]
    )
    counts = summary["status_counts"]
    if isinstance(counts, dict):
        meanings = {
            "exact_koinly_transaction_history_match": "Exact transaction hash appears in available Koinly transaction history.",
            "onchain_only_pre_move_2023_no_koinly_export": "Visible Jan-Apr 2023 pre-move transaction; calculate replacement basis from on-chain trace or obtain a 2023 Koinly report.",
            "archive_gap_or_prehistory": "Trace points outside the archived movement graph.",
            "no_2021_koinly_export": "Would require 2021 reconstruction if material.",
            "no_exact_match_in_available_koinly_export": "Available Koinly year exists but no exact hash match.",
            "unmatched_or_missing_timestamp": "Manual review.",
        }
        for status, count in sorted(counts.items()):
            lines.append(f"| `{status}` | {count} | {meanings.get(status, '')} |")

    lines.extend(
        [
            "",
            "## Missing / Self-Calculate Rows",
            "",
            "| Date | Tx | Role | Symbols | Next step |",
            "| --- | --- | --- | --- | --- |",
        ]
    )
    for row in rows:
        if row["evidence_status"] == "exact_koinly_transaction_history_match":
            continue
        lines.append(
            "| {date} | `{tx}` | {role} | {symbols} | {step} |".format(
                date=(row["first_seen_timestamp"] or "")[:10],
                tx=row["tx_hash"],
                role=row["trace_roles"],
                symbols=(row["source_amounts"] or row["source_symbols"] or row["trace_flows"]).replace("|", "/"),
                step=row["recommended_next_step"].replace("|", "/"),
            )
        )

    lines.extend(
        [
            "",
            "## Outputs",
            "",
            "- CSV checklist: `move-date-wbtc-swedish-evidence-checklist.csv`",
            "- JSON summary: `move-date-wbtc-swedish-evidence-checklist-summary.json`",
            "",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")


def build(args: argparse.Namespace) -> None:
    inventory_dir = Path(args.inventory_dir)
    trace_path = inventory_dir / "move-date-wbtc-cdp-basis-trace.csv"
    output_csv = inventory_dir / "move-date-wbtc-swedish-evidence-checklist.csv"
    output_json = inventory_dir / "move-date-wbtc-swedish-evidence-checklist-summary.json"
    output_md = inventory_dir / "move-date-wbtc-swedish-evidence-checklist.md"

    trace_rows = read_csv(trace_path)
    koinly_index = load_koinly_transactions(Path(args.koinly_dir))
    checklist_rows = build_rows(trace_rows, koinly_index)
    summary = build_summary(checklist_rows, koinly_index)

    write_csv(output_csv, checklist_rows)
    output_json.write_text(json.dumps(summary, indent=2, sort_keys=True), encoding="utf-8")
    write_markdown(output_md, checklist_rows, summary)

    print(json.dumps(summary, indent=2, sort_keys=True))


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--inventory-dir", default=str(DEFAULT_INVENTORY_DIR))
    parser.add_argument("--koinly-dir", default=str(DEFAULT_KOINLY_DIR))
    build(parser.parse_args())


if __name__ == "__main__":
    main()
