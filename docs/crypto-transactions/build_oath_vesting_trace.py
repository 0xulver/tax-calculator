#!/usr/bin/env python3
"""Build a focused OATH vesting/distributor trace workpaper."""

from __future__ import annotations

import csv
import json
from collections import defaultdict
from datetime import datetime, timezone
from decimal import Decimal, InvalidOperation
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]
INVENTORY_DIR = REPO_ROOT / "private/evidence/onchain/move-date-inventory-2023-04-12"
MOVEMENTS = INVENTORY_DIR / "move-date-movements.csv"
KOINLY_2022_TX = (
    REPO_ROOT / "private/evidence/koinly/2022/koinly_2022_transaction_history_krYwagtox4_1777112970.csv"
)

OATH_TOKEN = "0x21ada0d2ac28c3a5fa3cd2ee30882da8812279b6"
USDC_TOKEN = "0x04068da6c83afcfa0e13ba15a6696662335d5b75"
ZERO = "0x0000000000000000000000000000000000000000"
EARLY_DISTRIBUTOR = "0x8b4441e79151e3fc5264733a3c5da4ff8eac16c1"
BATCH_VESTING = "0xd152f549545093347a162dce210e7293f1452150"
BATCH_CALLER = "0xcadcb387a3db3c491e00310cbcdf0a8f0855be37"
CLAIM_OR_MINTER = "0x96662f375a9734654cb57bbfeb31db9dd7784a7f"

EXTERNAL_DISTRIBUTOR_SWAP_TX = (
    "0x8060081fb3d3330ede456e87aa4e20b4df4ac58a25a384c57739662decf7794c"
)
EXTERNAL_DISTRIBUTOR_SWAP_INTERMEDIARY = "0x97d73d3dddd68fcd16b344093592ade819d46dcf"

MOVE_DATE_CUTOFF = "2023-04-12"


def parse_decimal(value: str | None) -> Decimal:
    text = str(value or "").strip().replace("\u00a0", " ").replace(" ", "")
    if not text:
        return Decimal("0")
    if "," in text and "." in text:
        text = text.replace(",", "")
    elif "," in text:
        text = text.replace(",", ".")
    try:
        return Decimal(text)
    except InvalidOperation:
        return Decimal("0")


def fmt(value: Decimal) -> str:
    text = format(value.normalize(), "f")
    return text.rstrip("0").rstrip(".") if "." in text else text


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def read_koinly(path: Path) -> list[dict[str, str]]:
    lines = path.read_text(encoding="utf-8-sig", errors="replace").splitlines()
    while lines and not lines[0].startswith("Date,"):
        lines.pop(0)
    if not lines:
        return []
    return list(csv.DictReader(lines))


def topic_addr(topic: str) -> str:
    return "0x" + str(topic)[-40:].lower()


def decode_transfer_endpoints(row: dict[str, str]) -> tuple[str, str]:
    source_file = row.get("source_file", "")
    if not source_file:
        return "", ""
    path = REPO_ROOT / source_file
    if not path.exists():
        return "", ""
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return "", ""
    tx_hash = row.get("tx_hash", "").lower()
    contract = row.get("contract_address", "").lower()
    for log in payload.get("logs", []):
        if str(log.get("transactionHash", "")).lower() != tx_hash:
            continue
        if str(log.get("address", "")).lower() != contract:
            continue
        topics = log.get("topics") or []
        if len(topics) >= 3:
            return topic_addr(topics[1]), topic_addr(topics[2])
    return "", ""


def trace_meta(tx_hash: str) -> tuple[str, str, str]:
    path = REPO_ROOT / f"private/evidence/onchain/raw/rpc-transaction-traces/fantom/{tx_hash}.json"
    if not path.exists():
        return "", "", ""
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return "", "", ""
    traces = payload.get("traces") or []
    if not traces:
        return "", "", ""
    action = traces[0].get("action", {})
    input_data = action.get("input", "")
    return (
        str(action.get("from", "")).lower(),
        str(action.get("to", "")).lower(),
        input_data[:10] if input_data else "",
    )


def external_distributor_swap() -> dict[str, str]:
    path = (
        REPO_ROOT
        / f"private/evidence/onchain/raw/rpc-transaction-receipts/fantom/{EXTERNAL_DISTRIBUTOR_SWAP_TX}.json"
    )
    if not path.exists():
        return {}
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return {}

    receipt = payload.get("receipt", {})
    tx = payload.get("transaction", {})
    usdc_spent = Decimal("0")
    oath_received = Decimal("0")
    for log in receipt.get("logs", []):
        topics = log.get("topics") or []
        if len(topics) < 3:
            continue
        token = str(log.get("address", "")).lower()
        from_address = topic_addr(topics[1])
        to_address = topic_addr(topics[2])
        raw_value = Decimal(int(str(log.get("data", "0x0")), 16))
        if token == USDC_TOKEN and from_address == EARLY_DISTRIBUTOR:
            usdc_spent += raw_value / Decimal(10**6)
        if token == OATH_TOKEN and to_address == EARLY_DISTRIBUTOR:
            oath_received += raw_value / Decimal(10**18)

    unit_price = usdc_spent / oath_received if oath_received else Decimal("0")
    block_timestamp = payload.get("block_timestamp", "")
    if block_timestamp:
        timestamp = datetime.fromtimestamp(int(block_timestamp), timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    else:
        timestamp = ""

    return {
        "timestamp": timestamp,
        "tx_hash": EXTERNAL_DISTRIBUTOR_SWAP_TX,
        "top_level_from": str(tx.get("from", "")).lower(),
        "top_level_to": str(tx.get("to", "")).lower(),
        "usdc_spent": fmt(usdc_spent),
        "oath_received": fmt(oath_received),
        "unit_price_usdc_per_oath": fmt(unit_price),
        "raw_receipt": str(path.relative_to(REPO_ROOT)),
    }


def source_kind(from_address: str, to_address: str, known_wallets: set[str]) -> str:
    from_l = from_address.lower()
    to_l = to_address.lower()
    if from_l == EARLY_DISTRIBUTOR:
        return "early_tge_or_launch_distributor"
    if from_l == BATCH_VESTING:
        return "batch_vesting_distributor"
    if from_l == ZERO:
        return "mint_or_reward_claim"
    if from_l in known_wallets and to_l in known_wallets:
        return "internal_wallet_transfer"
    return "lp_farm_or_other_contract"


def koinly_rows_by_tx() -> dict[str, list[dict[str, str]]]:
    rows = read_koinly(KOINLY_2022_TX) if KOINLY_2022_TX.exists() else []
    mapped: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        tx_hash = row.get("TxHash", "").lower()
        if not tx_hash:
            continue
        for key in {tx_hash, tx_hash.removeprefix("0x"), f"0x{tx_hash.removeprefix('0x')}"}:
            mapped[key].append(row)
    return mapped


def match_koinly(
    rows_by_tx: dict[str, list[dict[str, str]]],
    tx_hash: str,
    direction: str,
    amount: Decimal,
) -> dict[str, str]:
    candidates = rows_by_tx.get(tx_hash) or rows_by_tx.get(tx_hash.removeprefix("0x")) or []
    if not candidates:
        return {}
    if direction == "in":
        amount_abs = abs(amount)
        oath_rows = [row for row in candidates if row.get("Received Currency", "").upper() == "OATH"]
        exact = [
            row
            for row in oath_rows
            if abs(parse_decimal(row.get("Received Amount")) - amount_abs) < Decimal("0.000001")
        ]
        return (exact or oath_rows or candidates)[0]
    if direction == "out":
        amount_abs = abs(amount)
        oath_rows = [row for row in candidates if row.get("Sent Currency", "").upper() == "OATH"]
        exact = [
            row
            for row in oath_rows
            if abs(parse_decimal(row.get("Sent Amount")) - amount_abs) < Decimal("0.000001")
        ]
        return (exact or oath_rows or candidates)[0]
    return candidates[0]


def build() -> None:
    rows = read_csv(MOVEMENTS)
    koinly_by_tx = koinly_rows_by_tx()
    known_wallets = {
        row.get("wallet_address", "").lower()
        for row in rows
        if row.get("wallet_address")
    }

    oath_rows: list[dict[str, str]] = []
    for row in rows:
        if row.get("chain") != "fantom":
            continue
        if row.get("contract_address", "").lower() != OATH_TOKEN:
            continue
        if row.get("timestamp", "")[:10] >= MOVE_DATE_CUTOFF:
            continue
        from_address, to_address = decode_transfer_endpoints(row)
        top_from, top_to, top_selector = trace_meta(row.get("tx_hash", ""))
        amount = parse_decimal(row.get("amount"))
        tx_hash = row.get("tx_hash", "").lower()
        koinly = match_koinly(koinly_by_tx, tx_hash, row.get("direction", ""), amount)
        record = {
            "timestamp": row.get("timestamp", ""),
            "wallet_label": row.get("wallet_label", ""),
            "wallet_address": row.get("wallet_address", "").lower(),
            "direction": row.get("direction", ""),
            "amount": fmt(amount),
            "from_address": from_address,
            "to_address": to_address,
            "source_kind": source_kind(from_address, to_address, known_wallets),
            "top_level_from": top_from,
            "top_level_to": top_to,
            "top_level_selector": top_selector,
            "koinly_type": koinly.get("Type", ""),
            "koinly_tag": koinly.get("Tag", ""),
            "koinly_net_value_sek": koinly.get("Net Value (SEK)", ""),
            "tx_hash": row.get("tx_hash", ""),
            "source_file": row.get("source_file", ""),
        }
        oath_rows.append(record)

    incoming = [
        row
        for row in oath_rows
        if row["direction"] == "in" and parse_decimal(row["amount"]) > 0
    ]

    totals: dict[str, Decimal] = defaultdict(Decimal)
    counts: dict[str, int] = defaultdict(int)
    value_sek: dict[str, Decimal] = defaultdict(Decimal)
    by_kind: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in incoming:
        kind = row["source_kind"]
        totals[kind] += parse_decimal(row["amount"])
        counts[kind] += 1
        value_sek[kind] += parse_decimal(row["koinly_net_value_sek"])
        by_kind[kind].append(row)

    source_csv = INVENTORY_DIR / "move-date-oath-vesting-source-transfers.csv"
    summary_json = INVENTORY_DIR / "move-date-oath-vesting-trace-summary.json"
    markdown = INVENTORY_DIR / "move-date-oath-vesting-trace.md"

    fieldnames = [
        "timestamp",
        "wallet_label",
        "wallet_address",
        "direction",
        "amount",
        "from_address",
        "to_address",
        "source_kind",
        "top_level_from",
        "top_level_to",
        "top_level_selector",
        "koinly_type",
        "koinly_tag",
        "koinly_net_value_sek",
        "tx_hash",
        "source_file",
    ]
    with source_csv.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(oath_rows)

    summary = {
        "cutoff": MOVE_DATE_CUTOFF,
        "incoming_totals": {
            kind: {
                "amount_oath": fmt(totals[kind]),
                "rows": counts[kind],
                "koinly_net_value_sek_present": fmt(value_sek[kind]),
            }
            for kind in sorted(totals)
        },
        "early_distributor": EARLY_DISTRIBUTOR,
        "batch_vesting_distributor": BATCH_VESTING,
        "batch_caller": BATCH_CALLER,
        "claim_or_minter": CLAIM_OR_MINTER,
        "external_distributor_swap": external_distributor_swap(),
    }
    summary_json.write_text(json.dumps(summary, indent=2), encoding="utf-8")

    swap = summary["external_distributor_swap"]
    swap_csv = None
    if swap:
        swap_csv = INVENTORY_DIR / "move-date-oath-external-distributor-swaps.csv"
        with swap_csv.open("w", encoding="utf-8", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=list(swap.keys()))
            writer.writeheader()
            writer.writerow(swap)

    lines = [
        "# OATH Vesting / Distributor Source Trace",
        "",
        f"Cut-off: `{MOVE_DATE_CUTOFF}`.",
        "",
        "This workpaper traces where the pre-move Fantom OATH came from. It is a source-provenance workpaper, not a final PIT-38 valuation decision.",
        "",
        "## Bottom Line",
        "",
        "- The OATH was not just an unexplained Avalanche/Arbitrum balance.",
        f"- `0x8b4441e79151e3fc5264733a3c5da4ff8eac16c1` sent `{fmt(totals['early_tge_or_launch_distributor'])}` OATH in `{counts['early_tge_or_launch_distributor']}` direct distributor transfers to the Fantom wallet in 2022.",
        f"- `0xd152f549545093347a162dce210e7293f1452150` sent `{fmt(totals['batch_vesting_distributor'])}` OATH in `{counts['batch_vesting_distributor']}` recurring batch vesting/distributor transfers from November 2022 through April 2023.",
        f"- Those batch transfers were initiated by `{BATCH_CALLER}` into `{BATCH_VESTING}` with selector `0xc73a2d60`, then `{BATCH_VESTING}` transferred OATH to the recipient wallets.",
        f"- Zero-address mint/reward claims add `{fmt(totals['mint_or_reward_claim'])}` OATH across `{counts['mint_or_reward_claim']}` rows; these are calls into `{CLAIM_OR_MINTER}` with selector `0x4e71d92d` and are separate from the distributor/vesting stream.",
        "",
        "## Incoming OATH By Source",
        "",
        "| Source kind | Amount OATH | Rows | Koinly 2022 value present |",
        "| --- | ---: | ---: | ---: |",
    ]
    for kind in sorted(totals, key=lambda item: totals[item], reverse=True):
        lines.append(
            f"| `{kind}` | `{fmt(totals[kind])}` | `{counts[kind]}` | `{fmt(value_sek[kind])} SEK` |"
        )

    lines.extend(
        [
            "",
            "## Direct Distributor / Vesting Receipts",
            "",
            "| Date | Wallet | Source | Amount OATH | Koinly value | Tx |",
            "| --- | --- | --- | ---: | ---: | --- |",
        ]
    )
    for kind in ["early_tge_or_launch_distributor", "batch_vesting_distributor"]:
        for row in sorted(by_kind.get(kind, []), key=lambda item: item["timestamp"]):
            value = row["koinly_net_value_sek"] or ""
            lines.append(
                f"| {row['timestamp']} | {row['wallet_label']} | `{row['from_address']}` | `{row['amount']}` | {value} SEK | `{row['tx_hash']}` |"
            )

    claim_rows = sorted(by_kind.get("mint_or_reward_claim", []), key=lambda item: item["timestamp"])
    if claim_rows:
        final_claim = claim_rows[-1]
        lines.extend(
            [
                "",
                "## Claim / Mint Contract Calls",
                "",
                f"Claim contract: `{CLAIM_OR_MINTER}`. Observed selector: `0x4e71d92d`.",
                "",
                f"Final pre-bridge claim found: `{final_claim['timestamp']}`, `{final_claim['amount']}` OATH, tx `{final_claim['tx_hash']}`. This is followed in the route by the `2023-03-18T19:42:19Z` Fantom bridge-out of `42,319.4` OATH from Metamask3.",
                "",
                "| Date | Wallet | Amount OATH | Caller | Contract | Koinly value | Tx |",
                "| --- | --- | ---: | --- | --- | ---: | --- |",
            ]
        )
        for row in claim_rows:
            value = row["koinly_net_value_sek"] or ""
            lines.append(
                f"| {row['timestamp']} | {row['wallet_label']} | `{row['amount']}` | `{row['top_level_from']}` | `{row['top_level_to']}` | {value} SEK | `{row['tx_hash']}` |"
            )

    lines.extend(
        [
            "",
            "## Link Into The Move-Date WETH/OATH LP",
            "",
            "- `2023-03-16`: the Reaper wallet bridged `48,000` OATH from Fantom to Arbitrum. This came out of the Reaper wallet's recurring vesting/distributor OATH inventory.",
            "- `2023-03-18`: the Reaper wallet sent `35,333.3333333332` OATH to Metamask3. Together with `6,478.39929035235455552` OATH minted/claimed to Metamask2 and transferred to Metamask3, this funded the March Fantom -> Arbitrum bridge branch used in the later WETH/OATH LP path.",
            "- `2023-04-01` and `2023-04-06`: the Reaper wallet received another `20,833.3333333333` OATH vesting/distributor transfer, moved it to Metamask3, then bridged it Fantom -> Optimism -> Arbitrum. The current LP allocation consumes `5,518.155490623468125458` OATH from that April bridge bucket.",
            "- Therefore the OATH-native bucket in `move-date-oath-provenance.md` is mostly a traced TGE/vesting/distributor source bucket, not an unknown token source. The remaining issue is valuation and tax-basis treatment.",
            "",
            "## External Distributor Swap Candidate",
            "",
            f"User-linked OKLink transaction: `{EXTERNAL_DISTRIBUTOR_SWAP_TX}`.",
            "",
        ]
    )
    if swap:
        lines.extend(
            [
                f"- Block timestamp: `{swap['timestamp']}`.",
                f"- Top-level call: `{swap['top_level_from']}` -> `{swap['top_level_to']}`.",
                f"- Mechanics from receipt logs: `{swap['usdc_spent']}` USDC left `{EARLY_DISTRIBUTOR}` and `{swap['oath_received']}` OATH returned to `{EARLY_DISTRIBUTOR}` through intermediary `{EXTERNAL_DISTRIBUTOR_SWAP_INTERMEDIARY}`.",
                f"- Implied swap price: `{swap['unit_price_usdc_per_oath']}` USDC per OATH.",
                "- This is useful distributor-inventory evidence, but it is not yet a direct user-wallet acquisition cost because the top-level sender is the distributor address, not one of the watched personal wallets.",
                "- It also happens after the April-August 2022 direct distributor transfers already received by Metamask2, so it cannot be the source for those earlier receipts. It may still matter if later distributor/vesting flows can be connected to that treasury inventory.",
                f"- A focused RPC log scan found no direct OATH transfer from `{EARLY_DISTRIBUTOR}` to the batch vesting distributor `{BATCH_VESTING}` between the linked swap block and the move-date cut-off.",
            ]
        )
    else:
        lines.append("- Receipt evidence is not archived locally yet, so this candidate is noted but not summarized.")
    lines.extend(
        [
            "",
            "## Filing Impact",
            "",
            "- This strengthens the factual support for the excluded OATH-native bucket.",
            "- It does not by itself add a separate PIT-38 cost amount because 2023 pre-move vesting/distributor rows have no Koinly 2023 export in the repo, and the treatment depends on whether the pre-move receipt/vesting value is accepted as acquisition or taxed-value basis.",
            "- Koinly 2022 already contains SEK values for the 2022 distributor and reward receipts, so those rows are better evidenced than the 2023 pre-move rows.",
            "",
            "## Outputs",
            "",
            "- Source transfer CSV: `move-date-oath-vesting-source-transfers.csv`",
            "- Summary JSON: `move-date-oath-vesting-trace-summary.json`",
        ]
    )
    if swap_csv is not None:
        lines.append("- External distributor swap CSV: `move-date-oath-external-distributor-swaps.csv`")
    lines.append("")
    markdown.write_text("\n".join(lines), encoding="utf-8")

    print(f"Wrote {source_csv.relative_to(REPO_ROOT)}")
    print(f"Wrote {summary_json.relative_to(REPO_ROOT)}")
    print(f"Wrote {markdown.relative_to(REPO_ROOT)}")


if __name__ == "__main__":
    build()
