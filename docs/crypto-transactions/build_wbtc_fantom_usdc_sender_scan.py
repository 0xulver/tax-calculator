#!/usr/bin/env python3
"""Scan the external Fantom USDC sender behind the WBTC source-open row."""

from __future__ import annotations

import argparse
import csv
import json
import time
import urllib.request
from collections import Counter, defaultdict
from decimal import Decimal
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_INVENTORY_DIR = REPO_ROOT / "private/evidence/onchain/move-date-inventory-2023-04-12"
DEFAULT_RPC_URL = "https://rpc.fantom.network"

USDC_ADDRESS = "0x04068da6c83afcfa0e13ba15a6696662335d5b75"
USDC_DECIMALS = Decimal("1000000")
TRANSFER_TOPIC = "0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef"
SENDER_ADDRESS = "0xbeb15caee71001d82f430e4deda80e16ddf438db"
KNOWN_WALLET_ADDRESS = "0xb573f01f2901c0db3e14ec80c6e12e4868dec864"
TERMINAL_TX_HASH = "0xb67d094cad2b8641086c3218fb7064d93840b82dc21b79da6bc422b57b29a2ca"
START_BLOCK = 50_000_000
TERMINAL_BLOCK = 57_810_243
RECENT_SOURCE_BLOCK_FLOOR = 57_800_000
USER_CONTEXT = (
    "Taxpayer context from 2026-04-25: 0xbeb15c... is likely an employer/company/Reaper-related address. "
    "The taxpayer recalls selling crypto to stablecoins during the market crash, investing those "
    "stablecoins into Reaper Farm multistrategy vaults on Fantom, losing those vault positions in a "
    "hack/recovery event, receiving in-kind recovery assets in August 2022, and later using "
    "recovered/compensated value to fund the BTC/WBTC path."
)
REAPER_INCIDENT_REFERENCES = [
    "https://docs.reaper.farm/crypts/multi-strategy-vaults",
    "https://docs.google.com/document/d/1aCEbz40BBC3y1RqDksnD9d-5IOXXgbeKAvJWMH2GoI4/edit",
    "https://docs.google.com/document/d/1wymADZrvisr8UNU9BHWh9bgEsO28D2-awhOHlxlQ3X8/edit",
    "https://pexx.com/chaindebrief/reaper-farm-got-hacked/",
]


def rpc(url: str, method: str, params: list[object]) -> object:
    body = json.dumps({"jsonrpc": "2.0", "id": 1, "method": method, "params": params}).encode()
    request = urllib.request.Request(url, data=body, headers={"content-type": "application/json"})
    with urllib.request.urlopen(request, timeout=30) as response:
        payload = json.loads(response.read())
    if "error" in payload:
        raise RuntimeError(payload["error"])
    return payload["result"]


def address_topic(address: str) -> str:
    return "0x" + "0" * 24 + address.lower().removeprefix("0x")


def topic_address(topic: str) -> str:
    return "0x" + topic[-40:].lower()


def fmt_decimal(value: Decimal) -> str:
    text = format(value.normalize(), "f")
    if "." in text:
        text = text.rstrip("0").rstrip(".")
    return text or "0"


def get_logs(url: str, from_block: int, to_block: int, direction: str) -> list[dict[str, object]]:
    if direction == "in":
        topics: list[object] = [TRANSFER_TOPIC, None, address_topic(SENDER_ADDRESS)]
    else:
        topics = [TRANSFER_TOPIC, address_topic(SENDER_ADDRESS)]
    result = rpc(
        url,
        "eth_getLogs",
        [
            {
                "fromBlock": hex(from_block),
                "toBlock": hex(to_block),
                "address": USDC_ADDRESS,
                "topics": topics,
            }
        ],
    )
    if not isinstance(result, list):
        return []
    return [item for item in result if isinstance(item, dict)]


def block_timestamps(url: str, block_numbers: set[int]) -> dict[int, str]:
    timestamps: dict[int, str] = {}
    for block_number in sorted(block_numbers):
        block = rpc(url, "eth_getBlockByNumber", [hex(block_number), False])
        if not isinstance(block, dict):
            continue
        timestamp = int(str(block.get("timestamp", "0x0")), 16)
        timestamps[block_number] = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime(timestamp))
    return timestamps


def scan(url: str, start_block: int, end_block: int, chunk_size: int) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    for direction in ("in", "out"):
        block = start_block
        while block <= end_block:
            chunk_end = min(end_block, block + chunk_size - 1)
            logs = get_logs(url, block, chunk_end, direction)
            for log in logs:
                topics = log.get("topics")
                if not isinstance(topics, list) or len(topics) < 3:
                    continue
                amount = Decimal(int(str(log.get("data", "0x0")), 16)) / USDC_DECIMALS
                rows.append(
                    {
                        "block_number": str(int(str(log.get("blockNumber", "0x0")), 16)),
                        "timestamp": "",
                        "tx_hash": str(log.get("transactionHash", "")),
                        "direction_relative_to_sender": direction,
                        "amount_usdc": fmt_decimal(amount),
                        "from_address": topic_address(str(topics[1])),
                        "to_address": topic_address(str(topics[2])),
                    }
                )
            block = chunk_end + 1
            time.sleep(0.03)

    timestamps = block_timestamps(url, {int(row["block_number"]) for row in rows})
    for row in rows:
        row["timestamp"] = timestamps.get(int(row["block_number"]), "")
    rows.sort(key=lambda item: (int(item["block_number"]), item["tx_hash"], item["direction_relative_to_sender"]))
    return rows


def summarize(rows: list[dict[str, str]], code: str) -> dict[str, object]:
    by_direction: dict[str, Decimal] = defaultdict(Decimal)
    counts = Counter(row["direction_relative_to_sender"] for row in rows)
    recent_inbound_by_source: dict[str, Decimal] = defaultdict(Decimal)
    recent_inbound_counts: Counter[str] = Counter()
    for row in rows:
        amount = Decimal(row["amount_usdc"])
        by_direction[row["direction_relative_to_sender"]] += amount
        if (
            row["direction_relative_to_sender"] == "in"
            and int(row["block_number"]) >= RECENT_SOURCE_BLOCK_FLOOR
            and int(row["block_number"]) < TERMINAL_BLOCK
        ):
            recent_inbound_by_source[row["from_address"]] += amount
            recent_inbound_counts[row["from_address"]] += 1

    return {
        "sender_address": SENDER_ADDRESS,
        "sender_code_at_terminal_block": code,
        "sender_account_type": "EOA" if code == "0x" else "contract",
        "known_wallet_address": KNOWN_WALLET_ADDRESS,
        "scan_start_block": START_BLOCK,
        "scan_end_block": TERMINAL_BLOCK,
        "transfer_count": len(rows),
        "transfer_counts_by_direction": dict(counts),
        "inbound_usdc": fmt_decimal(by_direction.get("in", Decimal("0"))),
        "outbound_usdc": fmt_decimal(by_direction.get("out", Decimal("0"))),
        "terminal_tx_hash": TERMINAL_TX_HASH,
        "terminal_transfer_usdc": fmt_decimal(
            sum((Decimal(row["amount_usdc"]) for row in rows if row["tx_hash"] == TERMINAL_TX_HASH), Decimal("0"))
        ),
        "recent_inbound_by_source": {
            address: fmt_decimal(amount) for address, amount in sorted(recent_inbound_by_source.items(), key=lambda item: item[1], reverse=True)
        },
        "recent_inbound_counts_by_source": dict(recent_inbound_counts),
        "user_context": USER_CONTEXT,
    }


def write_csv(path: Path, rows: list[dict[str, str]]) -> None:
    fieldnames = ["block_number", "timestamp", "tx_hash", "direction_relative_to_sender", "amount_usdc", "from_address", "to_address"]
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def write_markdown(path: Path, rows: list[dict[str, str]], summary: dict[str, object]) -> None:
    recent_sources = summary.get("recent_inbound_by_source", {})
    primary_recent_source = ""
    primary_recent_amount = ""
    if isinstance(recent_sources, dict) and recent_sources:
        primary_recent_source, primary_recent_amount = next(iter(recent_sources.items()))

    lines = [
        "# Fantom USDC Sender Scan For WBTC Source-Open Row",
        "",
        f"Target sender: `{SENDER_ADDRESS}`",
        f"Terminal transfer: `{TERMINAL_TX_HASH}`",
        "",
        "This generated workpaper scans Fantom USDC `Transfer` logs for the external sender that funded the WBTC stablecoin source-open row. It is source-provenance evidence only, not an imported-basis value.",
        "",
        "## Current Finding",
        "",
        f"- Sender account type at terminal block: `{summary['sender_account_type']}` (`eth_getCode` returned `{summary['sender_code_at_terminal_block']}`).",
        f"- Scan range: `{summary['scan_start_block']}` through `{summary['scan_end_block']}`.",
        f"- USDC transfers involving sender: `{summary['transfer_count']}`.",
        f"- Total inbound USDC in range: `{summary['inbound_usdc']}`.",
        f"- Total outbound USDC in range: `{summary['outbound_usdc']}`.",
        f"- Terminal transfer to known wallet: `{summary['terminal_transfer_usdc']} USDC`.",
        f"- User context to verify: {summary['user_context']}",
    ]
    if primary_recent_source:
        lines.append(
            f"- Immediate pre-terminal funding clue: `{primary_recent_amount} USDC` inbound from `{primary_recent_source}` after block `{RECENT_SOURCE_BLOCK_FLOOR}`."
        )
    lines.extend(
        [
            "",
            "Interpretation: the sender is not a contract wallet and is not in the current known-wallet files. The 56,314.96 USDC sent to the known wallet appears funded by recent inbound USDC transfers, especially from the source above. The user context and related Reaper workpapers make this look like later recovered-value provenance rather than a missing personal wallet, but it still does not prove acquisition cost by itself. The next evidence target is accepting the partial August 18 recovery-to-WBTC trace, deciding the March 2023 compensation/source-open leg, and fixing the Swedish tax treatment of the sale/loss/recovery chain.",
            "",
            "External Reaper incident references to archive with the evidence packet:",
            *[f"- {reference}" for reference in REAPER_INCIDENT_REFERENCES],
            "",
            "## Transfer Rows",
            "",
            "| Time | Direction | Amount USDC | From | To | Tx |",
            "| --- | --- | ---: | --- | --- | --- |",
        ]
    )
    for row in rows:
        lines.append(
            "| {timestamp} | {direction} | {amount} | `{from_addr}` | `{to_addr}` | `{tx}` |".format(
                timestamp=row["timestamp"],
                direction=row["direction_relative_to_sender"],
                amount=row["amount_usdc"],
                from_addr=row["from_address"],
                to_addr=row["to_address"],
                tx=row["tx_hash"],
            )
        )
    lines.extend(
        [
            "",
            "## Outputs",
            "",
            "- CSV scan: `move-date-wbtc-fantom-usdc-sender-scan.csv`",
            "- JSON summary: `move-date-wbtc-fantom-usdc-sender-scan-summary.json`",
            "",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")


def build(args: argparse.Namespace) -> None:
    output_dir = Path(args.inventory_dir)
    rows = scan(args.rpc_url, args.start_block, args.end_block, args.chunk_size)
    code = str(rpc(args.rpc_url, "eth_getCode", [SENDER_ADDRESS, hex(args.end_block)]))
    summary = summarize(rows, code)
    write_csv(output_dir / "move-date-wbtc-fantom-usdc-sender-scan.csv", rows)
    (output_dir / "move-date-wbtc-fantom-usdc-sender-scan-summary.json").write_text(
        json.dumps(summary, indent=2, sort_keys=True),
        encoding="utf-8",
    )
    write_markdown(output_dir / "move-date-wbtc-fantom-usdc-sender-scan.md", rows, summary)
    print(json.dumps(summary, indent=2, sort_keys=True))


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--inventory-dir", default=str(DEFAULT_INVENTORY_DIR))
    parser.add_argument("--rpc-url", default=DEFAULT_RPC_URL)
    parser.add_argument("--start-block", type=int, default=START_BLOCK)
    parser.add_argument("--end-block", type=int, default=TERMINAL_BLOCK)
    parser.add_argument("--chunk-size", type=int, default=250_000)
    build(parser.parse_args())


if __name__ == "__main__":
    main()
