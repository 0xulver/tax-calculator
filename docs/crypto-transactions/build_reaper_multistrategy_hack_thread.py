#!/usr/bin/env python3
"""Build a workpaper for the Reaper multi-strategy vault hack/compensation thread."""

from __future__ import annotations

import argparse
import csv
import json
from decimal import Decimal
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_INVENTORY_DIR = REPO_ROOT / "private/evidence/onchain/move-date-inventory-2023-04-12"

KNOWN_WALLET = "0xb573f01f2901c0db3e14ec80c6e12e4868dec864"
COMPENSATION_TX = "0xb67d094cad2b8641086c3218fb7064d93840b82dc21b79da6bc422b57b29a2ca"
REAPER_POSTMORTEM_ATTACKER = "0x5636e55e4a72299a0f194c001841e2ce75bb527a"
REAPER_RECOVERY_CALLER = "0x60bc5e0440c867eeb4cbce84bb1123fad2b262b1"
REAPER_RECOVERY_TARGET = "0xd152f549545093347a162dce210e7293f1452150"
STABLE_RF_SYMBOLS = {"rfUSDC", "rfDAI", "rfUSDT"}
LOSS_TO_RECOVERY_SYMBOLS = {
    "rfUSDC": "USDC",
    "rfDAI": "DAI",
    "rfUSDT": "fUSDT",
    "rfETH": "ETH",
    "rfBTC": "BTC",
    "rfWFTM": "WFTM",
}
RECOVERY_TXS = {
    "0x1c683b67e342d1a0796b9c3e45c622cab16ffcce668af09153f931b78cf4f400",
    "0x57cb4b9f3148a40cef52ff9506cdb100da7e5b915bb6a46581882b57fd432cf1",
    "0x90e90b546d999ef969afb2f463bb12241b81e6af7920d4b36b92c3c2eca973de",
    "0x9ffcca3fdeb404cfbca98def7e378b75a55763a4fbbc2ec49971e2a110f187b4",
    "0xfe07d8a6cc83e6ea29bb1fdf7d2b3dc5a150c75cf47779b2b3b68162af084800",
    "0x6d3788f5d795204a0eea1f928ed9d8cc671647299ab6569a8b58985ed2c552fd",
}

REAPER_INCIDENT_REFERENCES = [
    "https://docs.reaper.farm/crypts/multi-strategy-vaults",
    "https://docs.google.com/document/d/1aCEbz40BBC3y1RqDksnD9d-5IOXXgbeKAvJWMH2GoI4/edit",
    "https://docs.google.com/document/d/1wymADZrvisr8UNU9BHWh9bgEsO28D2-awhOHlxlQ3X8/edit",
    "https://pexx.com/chaindebrief/reaper-farm-got-hacked/",
]


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    if not rows:
        path.write_text("", encoding="utf-8")
        return
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def dec(value: str | None) -> Decimal:
    text = (value or "0").strip()
    return Decimal(text) if text else Decimal("0")


def fmt(value: Decimal, places: str = "0.000000000001") -> str:
    quantized = value.quantize(Decimal(places))
    text = format(quantized, "f")
    if "." in text:
        text = text.rstrip("0").rstrip(".")
    return text or "0"


def norm(value: str | None) -> str:
    return (value or "").strip().lower()


def date_part(timestamp: str) -> str:
    return timestamp[:10]


def is_reaper_multistrategy_receipt(row: dict[str, str]) -> bool:
    symbol = row.get("symbol", "")
    name = row.get("name", "")
    return row.get("chain") == "fantom" and symbol.startswith("rf") and "Crypt" in name


def load_json(path: Path) -> object | None:
    if not path.exists():
        return None
    return json.loads(path.read_text(encoding="utf-8", errors="replace"))


def trace_summary(tx_hash: str) -> dict[str, object]:
    trace_path = REPO_ROOT / f"private/evidence/onchain/raw/rpc-transaction-traces/fantom/{norm(tx_hash)}.json"
    payload = load_json(trace_path)
    if not isinstance(payload, dict):
        return {
            "tx_hash": tx_hash,
            "trace_path": str(trace_path.relative_to(REPO_ROOT)),
            "trace_available": False,
        }
    traces = payload.get("traces")
    if not isinstance(traces, list) or not traces:
        return {
            "tx_hash": tx_hash,
            "trace_path": str(trace_path.relative_to(REPO_ROOT)),
            "trace_available": False,
            "trace_count": 0,
        }
    first = traces[0]
    action = first.get("action") if isinstance(first, dict) else {}
    if not isinstance(action, dict):
        action = {}
    input_text = norm(action.get("input"))
    caller = norm(action.get("from"))
    return {
        "tx_hash": tx_hash,
        "trace_path": str(trace_path.relative_to(REPO_ROOT)),
        "trace_available": True,
        "trace_count": len(traces),
        "top_level_from": caller,
        "top_level_to": norm(action.get("to")),
        "top_level_selector": input_text[:10],
        "top_level_input_mentions_known_wallet": KNOWN_WALLET.removeprefix("0x") in input_text.removeprefix("0x"),
        "top_level_matches_reaper_postmortem_attacker": caller == REAPER_POSTMORTEM_ATTACKER,
        "block_number": payload.get("block_number"),
    }


def totals_by_symbol(rows: list[dict[str, str]]) -> dict[str, str]:
    totals: dict[str, Decimal] = {}
    for row in rows:
        totals[row["symbol"]] = totals.get(row["symbol"], Decimal("0")) + dec(row.get("amount"))
    return {symbol: fmt(amount) for symbol, amount in sorted(totals.items())}


def totals_by_symbol_decimal(rows: list[dict[str, object]], amount_field: str = "amount") -> dict[str, Decimal]:
    totals: dict[str, Decimal] = {}
    for row in rows:
        symbol = str(row.get("symbol", ""))
        totals[symbol] = totals.get(symbol, Decimal("0")) + dec(str(row.get(amount_field, "")))
    return totals


def build_loss_recovery_match_rows(
    loss_rows: list[dict[str, object]],
    recovery_rows: list[dict[str, object]],
) -> list[dict[str, object]]:
    loss_totals = totals_by_symbol_decimal(loss_rows)
    recovery_totals = totals_by_symbol_decimal(recovery_rows)
    loss_txs: dict[str, set[str]] = {}
    recovery_txs: dict[str, set[str]] = {}
    for row in loss_rows:
        symbol = str(row.get("symbol", ""))
        loss_txs.setdefault(symbol, set()).add(str(row.get("tx_hash", "")))
    for row in recovery_rows:
        symbol = str(row.get("symbol", ""))
        recovery_txs.setdefault(symbol, set()).add(str(row.get("tx_hash", "")))

    rows: list[dict[str, object]] = []
    for receipt_symbol, recovery_symbol in LOSS_TO_RECOVERY_SYMBOLS.items():
        lost_amount = abs(loss_totals.get(receipt_symbol, Decimal("0")))
        recovered_amount = recovery_totals.get(recovery_symbol, Decimal("0"))
        ratio = recovered_amount / lost_amount if lost_amount else Decimal("0")
        rows.append(
            {
                "lost_receipt_symbol": receipt_symbol,
                "lost_receipt_amount": fmt(lost_amount),
                "recovery_symbol": recovery_symbol,
                "recovery_amount": fmt(recovered_amount),
                "recovery_to_loss_ratio": fmt(ratio, "0.000001"),
                "difference_recovery_minus_loss": fmt(recovered_amount - lost_amount),
                "loss_txs": "; ".join(sorted(tx for tx in loss_txs.get(receipt_symbol, set()) if tx)),
                "recovery_txs": "; ".join(sorted(tx for tx in recovery_txs.get(recovery_symbol, set()) if tx)),
                "status": "same_family_recovery_found" if lost_amount and recovered_amount else "missing_or_zero",
            }
        )
    return rows


def enrich_loss_rows(rows: list[dict[str, str]]) -> list[dict[str, object]]:
    enriched: list[dict[str, object]] = []
    for row in rows:
        trace = trace_summary(row["tx_hash"])
        enriched.append(
            {
                "timestamp": row.get("timestamp", ""),
                "wallet_label": row.get("wallet_label", ""),
                "wallet_address": row.get("wallet_address", ""),
                "symbol": row.get("symbol", ""),
                "name": row.get("name", ""),
                "amount": row.get("amount", ""),
                "contract_address": row.get("contract_address", ""),
                "tx_hash": row.get("tx_hash", ""),
                "top_level_from": trace.get("top_level_from", ""),
                "top_level_to": trace.get("top_level_to", ""),
                "top_level_selector": trace.get("top_level_selector", ""),
                "trace_count": trace.get("trace_count", ""),
                "top_level_matches_reaper_postmortem_attacker": trace.get("top_level_matches_reaper_postmortem_attacker", ""),
                "top_level_input_mentions_known_wallet": trace.get("top_level_input_mentions_known_wallet", ""),
                "trace_path": trace.get("trace_path", ""),
            }
        )
    return enriched


def enrich_recovery_rows(rows: list[dict[str, str]]) -> list[dict[str, object]]:
    enriched: list[dict[str, object]] = []
    for row in rows:
        trace = trace_summary(row["tx_hash"])
        enriched.append(
            {
                "timestamp": row.get("timestamp", ""),
                "wallet_label": row.get("wallet_label", ""),
                "wallet_address": row.get("wallet_address", ""),
                "symbol": row.get("symbol", ""),
                "name": row.get("name", ""),
                "amount": row.get("amount", ""),
                "contract_address": row.get("contract_address", ""),
                "tx_hash": row.get("tx_hash", ""),
                "top_level_from": trace.get("top_level_from", ""),
                "top_level_to": trace.get("top_level_to", ""),
                "top_level_selector": trace.get("top_level_selector", ""),
                "trace_count": trace.get("trace_count", ""),
                "top_level_matches_reaper_recovery_caller": trace.get("top_level_from") == REAPER_RECOVERY_CALLER,
                "top_level_matches_reaper_recovery_target": trace.get("top_level_to") == REAPER_RECOVERY_TARGET,
                "top_level_input_mentions_known_wallet": trace.get("top_level_input_mentions_known_wallet", ""),
                "trace_path": trace.get("trace_path", ""),
            }
        )
    return enriched


def build(args: argparse.Namespace) -> None:
    inventory_dir = Path(args.inventory_dir)
    movements = read_csv(inventory_dir / "move-date-movements.csv")

    incident_window_rows = [
        row
        for row in movements
        if is_reaper_multistrategy_receipt(row)
        and "2022-07-01" <= date_part(row.get("timestamp", "")) <= "2022-08-03"
    ]
    incident_window_rows.sort(key=lambda row: (row.get("timestamp", ""), row.get("tx_hash", ""), row.get("symbol", "")))

    known_wallet_received_rows = [
        row
        for row in incident_window_rows
        if norm(row.get("wallet_address")) == KNOWN_WALLET
        and dec(row.get("amount")) > 0
        and date_part(row.get("timestamp", "")) < "2022-08-02"
    ]
    known_wallet_loss_rows = [
        row
        for row in incident_window_rows
        if norm(row.get("wallet_address")) == KNOWN_WALLET
        and dec(row.get("amount")) < 0
        and "2022-08-02" <= date_part(row.get("timestamp", "")) <= "2022-08-03"
    ]
    known_wallet_loss_rows.sort(key=lambda row: (row.get("timestamp", ""), row.get("symbol", "")))
    enriched_loss_rows = enrich_loss_rows(known_wallet_loss_rows)

    recovery_rows = [
        row
        for row in movements
        if norm(row.get("wallet_address")) == KNOWN_WALLET
        and norm(row.get("tx_hash")) in RECOVERY_TXS
        and dec(row.get("amount")) > 0
    ]
    recovery_rows.sort(key=lambda row: (row.get("timestamp", ""), row.get("symbol", "")))
    enriched_recovery_rows = enrich_recovery_rows(recovery_rows)

    compensation_rows = [row for row in movements if norm(row.get("tx_hash")) == COMPENSATION_TX]
    compensation_known_wallet_in = sum(
        (
            dec(row.get("amount"))
            for row in compensation_rows
            if norm(row.get("wallet_address")) == KNOWN_WALLET
            and row.get("symbol") == "USDC"
            and dec(row.get("amount")) > 0
        ),
        Decimal("0"),
    )

    stable_receipt_face_loss = sum(
        (abs(dec(row.get("amount"))) for row in known_wallet_loss_rows if row.get("symbol") in STABLE_RF_SYMBOLS),
        Decimal("0"),
    )

    sender_summary = load_json(inventory_dir / "move-date-wbtc-fantom-usdc-sender-scan-summary.json")
    if not isinstance(sender_summary, dict):
        sender_summary = {}

    attacker_match_count = sum(1 for row in enriched_loss_rows if row["top_level_matches_reaper_postmortem_attacker"] is True)
    recovery_caller_match_count = sum(
        1 for row in enriched_recovery_rows if row["top_level_matches_reaper_recovery_caller"] is True
    )
    recovery_target_match_count = sum(
        1 for row in enriched_recovery_rows if row["top_level_matches_reaper_recovery_target"] is True
    )
    loss_recovery_match_rows = build_loss_recovery_match_rows(enriched_loss_rows, enriched_recovery_rows)
    recovered_families = [
        f"{row['lost_receipt_symbol']}->{row['recovery_symbol']}"
        for row in loss_recovery_match_rows
        if row["status"] == "same_family_recovery_found"
    ]
    missing_recovery_families = [
        str(row["lost_receipt_symbol"])
        for row in loss_recovery_match_rows
        if row["status"] != "same_family_recovery_found"
    ]
    stable_recovery_face_amount = sum(
        (
            dec(str(row.get("recovery_amount")))
            for row in loss_recovery_match_rows
            if row.get("lost_receipt_symbol") in STABLE_RF_SYMBOLS
        ),
        Decimal("0"),
    )

    summary = {
        "purpose": "Reaper multi-strategy vault hack/compensation evidence thread for the WBTC source-open basis row",
        "known_wallet": KNOWN_WALLET,
        "reaper_postmortem_attacker": REAPER_POSTMORTEM_ATTACKER,
        "reaper_recovery_caller": REAPER_RECOVERY_CALLER,
        "reaper_recovery_target": REAPER_RECOVERY_TARGET,
        "incident_window_receipt_row_count": len(incident_window_rows),
        "known_wallet_received_before_incident_by_symbol": totals_by_symbol(known_wallet_received_rows),
        "known_wallet_loss_rows": len(known_wallet_loss_rows),
        "known_wallet_loss_by_symbol": totals_by_symbol(known_wallet_loss_rows),
        "known_wallet_stable_receipt_face_loss": fmt(stable_receipt_face_loss),
        "known_wallet_stable_direct_recovery": fmt(stable_recovery_face_amount),
        "known_wallet_stable_direct_recovery_to_loss_ratio": fmt(
            stable_recovery_face_amount / stable_receipt_face_loss if stable_receipt_face_loss else Decimal("0"),
            "0.000001",
        ),
        "loss_tx_count_matching_reaper_postmortem_attacker": attacker_match_count,
        "loss_tx_count_externally_initiated": len(
            [row for row in enriched_loss_rows if row["top_level_from"] and row["top_level_from"] != KNOWN_WALLET]
        ),
        "known_wallet_direct_recovery_rows": len(enriched_recovery_rows),
        "known_wallet_direct_recovery_by_symbol": totals_by_symbol(recovery_rows),
        "loss_recovery_families_covered": recovered_families,
        "loss_recovery_families_missing": missing_recovery_families,
        "recovery_tx_count_matching_common_caller": recovery_caller_match_count,
        "recovery_tx_count_matching_common_target": recovery_target_match_count,
        "proposed_compensation_tx": COMPENSATION_TX,
        "proposed_compensation_to_known_wallet_usdc": fmt(compensation_known_wallet_in),
        "proposed_compensation_sender": sender_summary.get("sender_address", ""),
        "proposed_compensation_sender_account_type": sender_summary.get("sender_account_type", ""),
        "proposed_compensation_recent_inbound_by_source": sender_summary.get("recent_inbound_by_source", {}),
        "taxpayer_context": (
            "Taxpayer context from 2026-04-25: the taxpayer invested stablecoins into "
            "Reaper Farm multistrategy vaults on Fantom, lost those positions in the "
            "Reaper hack/recovery process, received in-kind recovery assets in August 2022, "
            "and later used recovered/compensated value to fund the BTC/WBTC path."
        ),
        "external_reaper_incident_references": REAPER_INCIDENT_REFERENCES,
    }

    write_csv(inventory_dir / "move-date-reaper-multistrategy-hack-thread-incident-window.csv", incident_window_rows)
    write_csv(inventory_dir / "move-date-reaper-multistrategy-hack-thread-losses.csv", enriched_loss_rows)
    write_csv(inventory_dir / "move-date-reaper-multistrategy-hack-thread-recovery.csv", enriched_recovery_rows)
    write_csv(inventory_dir / "move-date-reaper-multistrategy-loss-recovery-match.csv", loss_recovery_match_rows)
    (inventory_dir / "move-date-reaper-multistrategy-hack-thread-summary.json").write_text(
        json.dumps(summary, indent=2, sort_keys=True),
        encoding="utf-8",
    )
    write_markdown(
        inventory_dir / "move-date-reaper-multistrategy-hack-thread.md",
        incident_window_rows,
        enriched_loss_rows,
        enriched_recovery_rows,
        loss_recovery_match_rows,
        summary,
    )
    print(json.dumps(summary, indent=2, sort_keys=True))


def write_markdown(
    path: Path,
    incident_rows: list[dict[str, str]],
    loss_rows: list[dict[str, object]],
    recovery_rows: list[dict[str, object]],
    loss_recovery_match_rows: list[dict[str, object]],
    summary: dict[str, object],
) -> None:
    lines = [
        "# Reaper Multi-Strategy Vault Hack / Compensation Evidence Thread",
        "",
        "This generated workpaper isolates the taxpayer-specific Reaper multi-strategy receipt-token evidence that may explain the Fantom USDC source-open row in the Ethos WBTC basis roll-forward. It is a provenance workpaper only; it is not a final PIT-38 cost value.",
        "",
        "## Current Finding",
        "",
        f"- Taxpayer context to verify: {summary['taxpayer_context']}",
        f"- Incident-window Reaper receipt rows found: `{summary['incident_window_receipt_row_count']}`.",
        f"- Known-wallet receipt tokens moved out on 2022-08-02/2022-08-03: `{summary['known_wallet_loss_rows']}` rows.",
        f"- Known-wallet stable receipt face loss (`rfUSDC` + `rfDAI` + `rfUSDT`): `{summary['known_wallet_stable_receipt_face_loss']}` receipt units.",
        f"- Same-family stable direct recovery (`USDC` + `DAI` + `fUSDT`): `{summary['known_wallet_stable_direct_recovery']}` tokens, ratio `{summary['known_wallet_stable_direct_recovery_to_loss_ratio']}` against stable receipt face loss.",
        f"- Receipt-token families with direct same-family recovery: `{', '.join(summary['loss_recovery_families_covered'])}`.",
        f"- Loss transactions whose top-level caller matches Reaper's post-mortem attacker `{REAPER_POSTMORTEM_ATTACKER}`: `{summary['loss_tx_count_matching_reaper_postmortem_attacker']}`.",
        f"- Loss transactions externally initiated by non-known-wallet callers: `{summary['loss_tx_count_externally_initiated']}`.",
        f"- Direct known-wallet recovery rows on 2022-08-18: `{summary['known_wallet_direct_recovery_rows']}`.",
        f"- Direct recovery rows whose top-level caller matches `{REAPER_RECOVERY_CALLER}`: `{summary['recovery_tx_count_matching_common_caller']}`.",
        f"- Direct recovery rows whose top-level target matches `{REAPER_RECOVERY_TARGET}`: `{summary['recovery_tx_count_matching_common_target']}`.",
        f"- Later WBTC-source USDC leg to known wallet: `{summary['proposed_compensation_to_known_wallet_usdc']} USDC` in tx `{summary['proposed_compensation_tx']}`.",
        f"- Later WBTC-source sender from the Fantom USDC sender scan: `{summary.get('proposed_compensation_sender', '')}` (`{summary.get('proposed_compensation_sender_account_type', '')}`).",
        "",
        "Known-wallet received balances before the incident, by receipt token:",
        "",
    ]
    for symbol, amount in dict(summary["known_wallet_received_before_incident_by_symbol"]).items():
        lines.append(f"- `{symbol}`: `{amount}`")

    lines.extend(
        [
            "",
            "Known-wallet August 2/3 outflows, by receipt token:",
            "",
        ]
    )
    for symbol, amount in dict(summary["known_wallet_loss_by_symbol"]).items():
        lines.append(f"- `{symbol}`: `{amount}`")

    lines.extend(
        [
            "",
            "Known-wallet August 18 direct recovery rows, by token:",
            "",
        ]
    )
    for symbol, amount in dict(summary["known_wallet_direct_recovery_by_symbol"]).items():
        lines.append(f"- `{symbol}`: `{amount}`")

    lines.extend(
        [
            "",
            "Interpretation: the local ledger confirms the issue was not just `rfUSDC`. The known wallet held and then lost Reaper multi-strategy receipt tokens for ETH, USDC, DAI, USDT, BTC, and WFTM. The official Reaper post-mortem identifies the same attacker address seen in several local trace top-level calls. The wallet then received a same-asset-family recovery set on 2022-08-18: USDC, DAI, ETH, BTC, fUSDT, and WFTM, all through transactions sharing the same recovery caller and target. The later March 2023 USDC receipt remains useful WBTC-source provenance, but the strongest Reaper compensation evidence is now the August 2022 direct recovery set, not the March 2023 transfer by itself.",
            "",
            "## Loss-to-Recovery Family Match",
            "",
            "| Lost receipt token | Lost amount | Recovery token | Recovery amount | Recovery / loss | Difference | Status |",
            "| --- | ---: | --- | ---: | ---: | ---: | --- |",
        ]
    )
    for row in loss_recovery_match_rows:
        lines.append(
            "| {lost_symbol} | {lost_amount} | {recovery_symbol} | {recovery_amount} | {ratio} | {difference} | `{status}` |".format(
                lost_symbol=row.get("lost_receipt_symbol", ""),
                lost_amount=row.get("lost_receipt_amount", ""),
                recovery_symbol=row.get("recovery_symbol", ""),
                recovery_amount=row.get("recovery_amount", ""),
                ratio=row.get("recovery_to_loss_ratio", ""),
                difference=row.get("difference_recovery_minus_loss", ""),
                status=row.get("status", ""),
            )
        )

    lines.extend(
        [
            "",
            "External Reaper incident references to archive with the evidence packet:",
            *[f"- {reference}" for reference in REAPER_INCIDENT_REFERENCES],
            "",
            "Evidence still needed before treating this as supported imported basis:",
            "",
            "- Transaction-level tracing from the August 18 recovery assets through later swaps, bridges, and WBTC acquisition.",
            "- Reaper vault UI/export, claim page, Discord/support record, or recovery-plan allocation, if available, to tie out the taxpayer-specific recovery values.",
            "- Swedish treatment of the original stablecoin sale, Reaper vault loss, and later compensation receipt.",
            "",
            "## Known-Wallet August 2/3 Receipt-Token Outflows",
            "",
            "| Time | Symbol | Amount | Top-level caller | Matches post-mortem attacker | Tx |",
            "| --- | --- | ---: | --- | --- | --- |",
        ]
    )
    for row in loss_rows:
        lines.append(
            "| {timestamp} | {symbol} | {amount} | `{caller}` | `{matches}` | `{tx}` |".format(
                timestamp=row.get("timestamp", ""),
                symbol=row.get("symbol", ""),
                amount=row.get("amount", ""),
                caller=row.get("top_level_from", ""),
                matches=row.get("top_level_matches_reaper_postmortem_attacker", ""),
                tx=row.get("tx_hash", ""),
            )
        )

    lines.extend(
        [
            "",
            "## Known-Wallet August 18 Direct Recovery Rows",
            "",
            "| Time | Symbol | Amount | Top-level caller | Top-level target | Tx |",
            "| --- | --- | ---: | --- | --- | --- |",
        ]
    )
    for row in recovery_rows:
        lines.append(
            "| {timestamp} | {symbol} | {amount} | `{caller}` | `{target}` | `{tx}` |".format(
                timestamp=row.get("timestamp", ""),
                symbol=row.get("symbol", ""),
                amount=row.get("amount", ""),
                caller=row.get("top_level_from", ""),
                target=row.get("top_level_to", ""),
                tx=row.get("tx_hash", ""),
            )
        )

    lines.extend(
        [
            "",
            "## Incident-Window Reaper Receipt Rows",
            "",
            "| Time | Wallet | Direction | Symbol | Amount | Tx |",
            "| --- | --- | --- | --- | ---: | --- |",
        ]
    )
    for row in incident_rows:
        lines.append(
            "| {timestamp} | {wallet} | {direction} | {symbol} | {amount} | `{tx}` |".format(
                timestamp=row.get("timestamp", ""),
                wallet=row.get("wallet_label", ""),
                direction=row.get("direction", ""),
                symbol=row.get("symbol", ""),
                amount=row.get("amount", ""),
                tx=row.get("tx_hash", ""),
            )
        )
    lines.extend(
        [
            "",
            "## Outputs",
            "",
            "- CSV incident rows: `move-date-reaper-multistrategy-hack-thread-incident-window.csv`",
            "- CSV known-wallet loss rows: `move-date-reaper-multistrategy-hack-thread-losses.csv`",
            "- CSV known-wallet recovery rows: `move-date-reaper-multistrategy-hack-thread-recovery.csv`",
            "- CSV receipt loss to recovery match: `move-date-reaper-multistrategy-loss-recovery-match.csv`",
            "- JSON summary: `move-date-reaper-multistrategy-hack-thread-summary.json`",
            "",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--inventory-dir", default=str(DEFAULT_INVENTORY_DIR))
    build(parser.parse_args())


if __name__ == "__main__":
    main()
