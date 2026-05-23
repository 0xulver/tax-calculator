#!/usr/bin/env python3
"""Archive EVM `Transfer` logs by indexed wallet address.

This is useful when a chain has a working public RPC but no usable address
explorer export. It captures ERC-20 and ERC-721 compatible `Transfer` events
where a known wallet is indexed as sender or recipient. It does not capture
native-token transfers or contract calls without a token `Transfer` log.

Example:
  python3 docs/crypto-transactions/archive_evm_transfer_logs.py \
    --wallets-file docs/crypto-transactions/wallets.txt \
    --config docs/crypto-transactions/config.json \
    --chain-filter fantom \
    --start-date 2020-04-24 \
    --output-dir private/evidence/onchain/raw/rpc-transfer-logs
"""

from __future__ import annotations

import argparse
import csv
import json
import re
import time
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


EVM_ADDRESS_RE = re.compile(r"^0x[a-fA-F0-9]{40}$")
TRANSFER_TOPIC = "0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef"


def compact(value: str) -> str:
    return " ".join(str(value or "").split())


def read_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def read_evm_wallets(path: Path, wallet_filters: set[str]) -> list[dict[str, str]]:
    wallets: list[dict[str, str]] = []
    for raw in path.read_text(encoding="utf-8", errors="replace").splitlines():
        line = compact(raw)
        if not line or line.startswith("#") or " " not in line:
            continue
        label, address = line.rsplit(" ", 1)
        if not EVM_ADDRESS_RE.match(address):
            continue
        if wallet_filters and label.lower() not in wallet_filters and address.lower() not in wallet_filters:
            continue
        wallets.append({"label": label, "address": address})
    return wallets


def rpc_chains(config: dict[str, Any], chain_filters: set[str]) -> list[dict[str, Any]]:
    chains = []
    for chain in config.get("chains", []):
        if chain.get("family") != "evm" or not chain.get("rpc_url"):
            continue
        if chain_filters and str(chain.get("name", "")).lower() not in chain_filters:
            continue
        chains.append(chain)
    return chains


def rpc_call(rpc_url: str, method: str, params: list[Any], timeout: int) -> Any:
    request = urllib.request.Request(
        rpc_url,
        data=json.dumps({"jsonrpc": "2.0", "id": 1, "method": method, "params": params}).encode("utf-8"),
        headers={
            "Content-Type": "application/json",
            "User-Agent": "tax-calculator-evm-transfer-log-archive/1.0",
        },
    )
    with urllib.request.urlopen(request, timeout=timeout) as response:
        payload = json.loads(response.read().decode("utf-8"))
    if "error" in payload:
        raise RuntimeError(payload["error"])
    return payload.get("result")


def block_timestamp(rpc_url: str, block_number: int, timeout: int) -> int:
    block = rpc_call(rpc_url, "eth_getBlockByNumber", [hex(block_number), False], timeout)
    if not isinstance(block, dict):
        raise RuntimeError(f"missing block {block_number}")
    return int(block["timestamp"], 16)


def latest_block(rpc_url: str, timeout: int) -> int:
    return int(rpc_call(rpc_url, "eth_blockNumber", [], timeout), 16)


def find_block_at_or_after(rpc_url: str, target_ts: int, high: int, timeout: int) -> int:
    low = 0
    while low < high:
        mid = (low + high) // 2
        if block_timestamp(rpc_url, mid, timeout) < target_ts:
            low = mid + 1
        else:
            high = mid
    return low


def parse_date(value: str | None) -> datetime | None:
    if not value:
        return None
    return datetime.fromisoformat(value).replace(tzinfo=timezone.utc)


def address_topic(address: str) -> str:
    return "0x" + "0" * 24 + address.lower()[2:]


def fetch_logs(
    rpc_url: str,
    wallet: dict[str, str],
    direction: str,
    from_block: int,
    to_block: int,
    timeout: int,
) -> list[dict[str, Any]]:
    topic = address_topic(wallet["address"])
    if direction == "in":
        topics: list[str | None] = [TRANSFER_TOPIC, None, topic]
    elif direction == "out":
        topics = [TRANSFER_TOPIC, topic]
    else:
        raise ValueError(direction)
    params = {
        "fromBlock": hex(from_block),
        "toBlock": hex(to_block),
        "topics": topics,
    }
    result = rpc_call(rpc_url, "eth_getLogs", [params], timeout)
    return result if isinstance(result, list) else []


def archive_wallet_direction(
    chain: dict[str, Any],
    wallet: dict[str, str],
    direction: str,
    start_block: int,
    end_block: int,
    output_dir: Path,
    chunk_size: int,
    request_delay: float,
    timeout: int,
) -> tuple[list[dict[str, str]], set[int]]:
    rows: list[dict[str, str]] = []
    blocks_with_logs: set[int] = set()
    chain_name = str(chain["name"])
    wallet_dir = output_dir / chain_name / wallet["address"].lower()
    wallet_dir.mkdir(parents=True, exist_ok=True)

    chunk_index = 0
    for chunk_start in range(start_block, end_block + 1, chunk_size):
        chunk_end = min(chunk_start + chunk_size - 1, end_block)
        chunk_index += 1
        captured_at = datetime.now(timezone.utc).isoformat()
        file_path = wallet_dir / f"transfer_{direction}_chunk_{chunk_index:05d}_{chunk_start}_{chunk_end}.json"
        error = ""
        try:
            logs = fetch_logs(str(chain["rpc_url"]), wallet, direction, chunk_start, chunk_end, timeout)
            payload: dict[str, Any] = {"logs": logs}
        except Exception as exc:
            payload = {"logs": [], "error": type(exc).__name__, "message": str(exc)}
            error = f"{type(exc).__name__}: {exc}"

        payload.update(
            {
                "captured_at": captured_at,
                "chain": chain_name,
                "wallet_label": wallet["label"],
                "wallet_address": wallet["address"],
                "direction": direction,
                "from_block": chunk_start,
                "to_block": chunk_end,
                "transfer_topic": TRANSFER_TOPIC,
            }
        )
        file_written = ""
        if payload["logs"] or error:
            file_path.write_text(json.dumps(payload, indent=2, sort_keys=True), encoding="utf-8")
            file_written = str(file_path)

        for log in payload["logs"]:
            try:
                blocks_with_logs.add(int(log["blockNumber"], 16))
            except Exception:
                pass

        rows.append(
            {
                "captured_at": captured_at,
                "chain": chain_name,
                "wallet_label": wallet["label"],
                "wallet_address": wallet["address"],
                "direction": direction,
                "chunk": str(chunk_index),
                "from_block": str(chunk_start),
                "to_block": str(chunk_end),
                "result_count": str(len(payload["logs"])),
                "error": error,
                "file": file_written,
            }
        )
        time.sleep(request_delay)

    return rows, blocks_with_logs


def write_manifest(path: Path, rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=[
                "captured_at",
                "chain",
                "wallet_label",
                "wallet_address",
                "direction",
                "chunk",
                "from_block",
                "to_block",
                "result_count",
                "error",
                "file",
            ],
        )
        writer.writeheader()
        writer.writerows(rows)


def retry_failed_manifest_rows(args: argparse.Namespace, config: dict[str, Any]) -> int:
    if not args.retry_errors_from_manifest:
        return 0

    chain_by_name = {str(chain["name"]): chain for chain in rpc_chains(config, set())}
    source_rows = list(csv.DictReader(args.retry_errors_from_manifest.open(encoding="utf-8")))
    failed_rows = [row for row in source_rows if row.get("error")]

    manifest_rows: list[dict[str, str]] = []
    blocks_by_chain: dict[str, set[int]] = {}
    for row in failed_rows:
        chain = chain_by_name.get(str(row["chain"]))
        if not chain:
            continue
        wallet = {"label": row["wallet_label"], "address": row["wallet_address"]}
        rows, blocks = archive_wallet_direction(
            chain=chain,
            wallet=wallet,
            direction=row["direction"],
            start_block=int(row["from_block"]),
            end_block=int(row["to_block"]),
            output_dir=args.output_dir,
            chunk_size=args.chunk_size,
            request_delay=args.request_delay,
            timeout=args.timeout,
        )
        manifest_rows.extend(rows)
        blocks_by_chain.setdefault(str(chain["name"]), set()).update(blocks)

    for chain_name, block_numbers in blocks_by_chain.items():
        chain = chain_by_name[chain_name]
        rpc_url = str(chain["rpc_url"])
        timestamp_path = args.output_dir / chain_name / "block_timestamps.json"
        timestamps: dict[str, str] = {}
        if timestamp_path.exists():
            timestamps = json.loads(timestamp_path.read_text(encoding="utf-8"))
        for block_number in sorted(block_numbers):
            key = str(block_number)
            if key in timestamps:
                continue
            timestamps[key] = str(block_timestamp(rpc_url, block_number, args.timeout))
            time.sleep(args.request_delay)
        timestamp_path.parent.mkdir(parents=True, exist_ok=True)
        timestamp_path.write_text(json.dumps(timestamps, indent=2, sort_keys=True), encoding="utf-8")

    manifest_path = args.output_dir / "retry_manifest.csv"
    write_manifest(manifest_path, manifest_rows)
    print(f"retry source rows: {len(failed_rows)}")
    print(f"retry manifest rows: {len(manifest_rows)}")
    print(f"retry manifest: {manifest_path}")
    return 0


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--wallets-file", type=Path, default=Path("docs/crypto-transactions/wallets.txt"))
    parser.add_argument("--config", type=Path, default=Path("docs/crypto-transactions/config.json"))
    parser.add_argument("--output-dir", type=Path, default=Path("private/evidence/onchain/raw/rpc-transfer-logs"))
    parser.add_argument("--wallet-filter", action="append", default=[], help="Wallet label or address filter.")
    parser.add_argument("--chain-filter", action="append", default=[], help="Chain name filter.")
    parser.add_argument("--start-date", help="UTC date, e.g. 2020-04-24. Defaults to config history_start.")
    parser.add_argument("--end-date", help="UTC date. Defaults to latest chain block.")
    parser.add_argument("--chunk-size", type=int, default=500_000)
    parser.add_argument("--request-delay", type=float, default=0.05)
    parser.add_argument("--timeout", type=int, default=60)
    parser.add_argument(
        "--retry-errors-from-manifest",
        type=Path,
        help="Retry only errored rows from an existing manifest, split by --chunk-size.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    config = read_json(args.config)
    if args.retry_errors_from_manifest:
        return retry_failed_manifest_rows(args, config)

    wallet_filters = {value.lower() for value in args.wallet_filter}
    chain_filters = {value.lower() for value in args.chain_filter}
    wallets = read_evm_wallets(args.wallets_file, wallet_filters)
    chains = rpc_chains(config, chain_filters)
    start_dt = parse_date(args.start_date or config.get("history_start"))
    end_dt = parse_date(args.end_date)

    manifest_rows: list[dict[str, str]] = []
    for chain in chains:
        rpc_url = str(chain["rpc_url"])
        high = latest_block(rpc_url, args.timeout)
        start_block = 0
        if start_dt:
            start_block = find_block_at_or_after(rpc_url, int(start_dt.timestamp()), high, args.timeout)
        end_block = high
        if end_dt:
            end_block = find_block_at_or_after(rpc_url, int(end_dt.timestamp()), high, args.timeout)

        chain_blocks: set[int] = set()
        for wallet in wallets:
            for direction in ("in", "out"):
                rows, blocks = archive_wallet_direction(
                    chain=chain,
                    wallet=wallet,
                    direction=direction,
                    start_block=start_block,
                    end_block=end_block,
                    output_dir=args.output_dir,
                    chunk_size=args.chunk_size,
                    request_delay=args.request_delay,
                    timeout=args.timeout,
                )
                manifest_rows.extend(rows)
                chain_blocks.update(blocks)

        timestamps: dict[str, str] = {}
        for block_number in sorted(chain_blocks):
            timestamps[str(block_number)] = str(block_timestamp(rpc_url, block_number, args.timeout))
            time.sleep(args.request_delay)
        timestamp_path = args.output_dir / str(chain["name"]) / "block_timestamps.json"
        timestamp_path.parent.mkdir(parents=True, exist_ok=True)
        timestamp_path.write_text(json.dumps(timestamps, indent=2, sort_keys=True), encoding="utf-8")

    manifest_path = args.output_dir / "manifest.csv"
    write_manifest(manifest_path, manifest_rows)
    print(f"wallets: {len(wallets)}")
    print(f"chains: {len(chains)}")
    print(f"manifest rows: {len(manifest_rows)}")
    print(f"manifest: {manifest_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
