#!/usr/bin/env python3
"""Archive EVM address traces through `trace_filter`.

This captures call/create/selfdestruct traces where a known wallet appears as
`action.from` or `action.to`. For Fantom this fills the native/internal value
movement gap left by token `Transfer` logs.

Example:
  python3 docs/crypto-transactions/archive_evm_traces.py \
    --wallets-file docs/crypto-transactions/wallets.txt \
    --config docs/crypto-transactions/config.json \
    --chain-filter fantom \
    --start-date 2020-04-24 \
    --output-dir private/evidence/onchain/raw/rpc-traces
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


def trace_chains(config: dict[str, Any], chain_filters: set[str]) -> list[dict[str, Any]]:
    chains = []
    for chain in config.get("chains", []):
        if chain.get("family") != "evm":
            continue
        if not (chain.get("trace_rpc_url") or chain.get("rpc_url")):
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
            "User-Agent": "tax-calculator-evm-trace-archive/1.0",
        },
    )
    with urllib.request.urlopen(request, timeout=timeout) as response:
        payload = json.loads(response.read().decode("utf-8"))
    if "error" in payload:
        raise RuntimeError(payload["error"])
    return payload.get("result")


def latest_block(rpc_url: str, timeout: int) -> int:
    return int(rpc_call(rpc_url, "eth_blockNumber", [], timeout), 16)


def block_timestamp(rpc_url: str, block_number: int, timeout: int) -> int:
    block = rpc_call(rpc_url, "eth_getBlockByNumber", [hex(block_number), False], timeout)
    if not isinstance(block, dict):
        raise RuntimeError(f"missing block {block_number}")
    return int(block["timestamp"], 16)


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


def fetch_trace_filter(
    rpc_url: str,
    wallet: dict[str, str],
    direction: str,
    from_block: int,
    to_block: int,
    count: int,
    after: int,
    timeout: int,
) -> list[dict[str, Any]]:
    key = "fromAddress" if direction == "from" else "toAddress"
    params = {
        "fromBlock": hex(from_block),
        "toBlock": hex(to_block),
        key: [wallet["address"].lower()],
        "count": count,
    }
    if after:
        params["after"] = after
    result = rpc_call(rpc_url, "trace_filter", [params], timeout)
    return result if isinstance(result, list) else []


def archive_trace_range(
    chain: dict[str, Any],
    wallet: dict[str, str],
    direction: str,
    range_label: str,
    chunk_start: int,
    chunk_end: int,
    output_dir: Path,
    page_size: int,
    min_split_size: int,
    request_delay: float,
    timeout: int,
) -> tuple[list[dict[str, str]], set[int]]:
    rows: list[dict[str, str]] = []
    blocks_with_traces: set[int] = set()
    chain_name = str(chain["name"])
    rpc_url = str(chain.get("trace_rpc_url") or chain.get("rpc_url"))
    wallet_dir = output_dir / chain_name / wallet["address"].lower()
    wallet_dir.mkdir(parents=True, exist_ok=True)

    after = 0
    page = 1

    while True:
        captured_at = datetime.now(timezone.utc).isoformat()
        file_path = (
            wallet_dir
            / f"trace_{direction}_range_{range_label}_page_{page:04d}_{chunk_start}_{chunk_end}.json"
        )
        error = ""
        try:
            traces = fetch_trace_filter(
                rpc_url=rpc_url,
                wallet=wallet,
                direction=direction,
                from_block=chunk_start,
                to_block=chunk_end,
                count=page_size,
                after=after,
                timeout=timeout,
            )
            payload: dict[str, Any] = {"traces": traces}
        except Exception as exc:
            if chunk_end > chunk_start and (chunk_end - chunk_start + 1) > min_split_size:
                mid = (chunk_start + chunk_end) // 2
                left_rows, left_blocks = archive_trace_range(
                    chain=chain,
                    wallet=wallet,
                    direction=direction,
                    range_label=f"{range_label}a",
                    chunk_start=chunk_start,
                    chunk_end=mid,
                    output_dir=output_dir,
                    page_size=page_size,
                    min_split_size=min_split_size,
                    request_delay=request_delay,
                    timeout=timeout,
                )
                right_rows, right_blocks = archive_trace_range(
                    chain=chain,
                    wallet=wallet,
                    direction=direction,
                    range_label=f"{range_label}b",
                    chunk_start=mid + 1,
                    chunk_end=chunk_end,
                    output_dir=output_dir,
                    page_size=page_size,
                    min_split_size=min_split_size,
                    request_delay=request_delay,
                    timeout=timeout,
                )
                return left_rows + right_rows, left_blocks | right_blocks
            payload = {"traces": [], "error": type(exc).__name__, "message": str(exc)}
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
                "page": page,
                "after": after,
                "page_size": page_size,
            }
        )

        file_written = ""
        if payload["traces"] or error:
            file_path.write_text(json.dumps(payload, indent=2, sort_keys=True), encoding="utf-8")
            file_written = str(file_path)

        for trace in payload["traces"]:
            try:
                blocks_with_traces.add(int(trace["blockNumber"]))
            except Exception:
                pass

        rows.append(
            {
                "captured_at": captured_at,
                "chain": chain_name,
                "wallet_label": wallet["label"],
                "wallet_address": wallet["address"],
                "direction": direction,
                "chunk": range_label,
                "page": str(page),
                "from_block": str(chunk_start),
                "to_block": str(chunk_end),
                "after": str(after),
                "result_count": str(len(payload["traces"])),
                "error": error,
                "file": file_written,
            }
        )

        if error or len(payload["traces"]) < page_size:
            break
        after += page_size
        page += 1
        time.sleep(request_delay)

    return rows, blocks_with_traces


def archive_wallet_direction(
    chain: dict[str, Any],
    wallet: dict[str, str],
    direction: str,
    start_block: int,
    end_block: int,
    output_dir: Path,
    chunk_size: int,
    page_size: int,
    min_split_size: int,
    request_delay: float,
    timeout: int,
) -> tuple[list[dict[str, str]], set[int]]:
    rows: list[dict[str, str]] = []
    blocks_with_traces: set[int] = set()

    chunk_index = 0
    for chunk_start in range(start_block, end_block + 1, chunk_size):
        chunk_end = min(chunk_start + chunk_size - 1, end_block)
        chunk_index += 1
        chunk_rows, chunk_blocks = archive_trace_range(
            chain=chain,
            wallet=wallet,
            direction=direction,
            range_label=f"{chunk_index:05d}",
            chunk_start=chunk_start,
            chunk_end=chunk_end,
            output_dir=output_dir,
            page_size=page_size,
            min_split_size=min_split_size,
            request_delay=request_delay,
            timeout=timeout,
        )
        rows.extend(chunk_rows)
        blocks_with_traces.update(chunk_blocks)
        time.sleep(request_delay)

    return rows, blocks_with_traces


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
                "page",
                "from_block",
                "to_block",
                "after",
                "result_count",
                "error",
                "file",
            ],
        )
        writer.writeheader()
        writer.writerows(rows)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--wallets-file", type=Path, default=Path("docs/crypto-transactions/wallets.txt"))
    parser.add_argument("--config", type=Path, default=Path("docs/crypto-transactions/config.json"))
    parser.add_argument("--output-dir", type=Path, default=Path("private/evidence/onchain/raw/rpc-traces"))
    parser.add_argument("--wallet-filter", action="append", default=[], help="Wallet label or address filter.")
    parser.add_argument("--chain-filter", action="append", default=[], help="Chain name filter.")
    parser.add_argument("--start-date", help="UTC date, e.g. 2020-04-24. Defaults to config history_start.")
    parser.add_argument("--end-date", help="UTC date. Defaults to latest chain block.")
    parser.add_argument("--chunk-size", type=int, default=500_000)
    parser.add_argument("--page-size", type=int, default=1000)
    parser.add_argument("--min-split-size", type=int, default=100)
    parser.add_argument("--request-delay", type=float, default=0.05)
    parser.add_argument("--timeout", type=int, default=60)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    config = read_json(args.config)
    wallet_filters = {value.lower() for value in args.wallet_filter}
    chain_filters = {value.lower() for value in args.chain_filter}
    wallets = read_evm_wallets(args.wallets_file, wallet_filters)
    chains = trace_chains(config, chain_filters)
    start_dt = parse_date(args.start_date or config.get("history_start"))
    end_dt = parse_date(args.end_date)

    manifest_rows: list[dict[str, str]] = []
    for chain in chains:
        rpc_url = str(chain.get("trace_rpc_url") or chain.get("rpc_url"))
        block_lookup_url = str(chain.get("rpc_url") or rpc_url)
        high = latest_block(block_lookup_url, args.timeout)
        start_block = 0
        if start_dt:
            start_block = find_block_at_or_after(block_lookup_url, int(start_dt.timestamp()), high, args.timeout)
        end_block = high
        if end_dt:
            end_block = find_block_at_or_after(block_lookup_url, int(end_dt.timestamp()), high, args.timeout)

        chain_blocks: set[int] = set()
        for wallet in wallets:
            for direction in ("from", "to"):
                rows, blocks = archive_wallet_direction(
                    chain=chain,
                    wallet=wallet,
                    direction=direction,
                    start_block=start_block,
                    end_block=end_block,
                    output_dir=args.output_dir,
                    chunk_size=args.chunk_size,
                    page_size=args.page_size,
                    min_split_size=args.min_split_size,
                    request_delay=args.request_delay,
                    timeout=args.timeout,
                )
                manifest_rows.extend(rows)
                chain_blocks.update(blocks)

        timestamps: dict[str, str] = {}
        timestamp_path = args.output_dir / str(chain["name"]) / "block_timestamps.json"
        if timestamp_path.exists():
            timestamps = json.loads(timestamp_path.read_text(encoding="utf-8"))
        for block_number in sorted(chain_blocks):
            key = str(block_number)
            if key in timestamps:
                continue
            timestamps[key] = str(block_timestamp(block_lookup_url, block_number, args.timeout))
            time.sleep(args.request_delay)
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
