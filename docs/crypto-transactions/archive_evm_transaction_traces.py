#!/usr/bin/env python3
"""Archive per-transaction EVM traces for transactions already discovered.

For Fantom, broad `trace_filter` ranges can fail or be slow on historical
blocks. This script takes transaction hashes from an existing transfer-log
archive and calls `trace_transaction` for each hash, producing deterministic
raw trace evidence for token-movement transactions.

Example:
  python3 docs/crypto-transactions/archive_evm_transaction_traces.py \
    --config docs/crypto-transactions/config.json \
    --chain fantom \
    --source-dir private/evidence/onchain/raw/rpc-transfer-logs/fantom \
    --output-dir private/evidence/onchain/raw/rpc-transaction-traces \
    --before-date 2023-04-12
"""

from __future__ import annotations

import argparse
import csv
import json
import time
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


def read_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def parse_date(value: str | None) -> datetime | None:
    if not value:
        return None
    return datetime.fromisoformat(value).replace(tzinfo=timezone.utc)


def rpc_call(rpc_url: str, method: str, params: list[Any], timeout: int) -> Any:
    request = urllib.request.Request(
        rpc_url,
        data=json.dumps({"jsonrpc": "2.0", "id": 1, "method": method, "params": params}).encode("utf-8"),
        headers={
            "Content-Type": "application/json",
            "User-Agent": "tax-calculator-evm-transaction-trace-archive/1.0",
        },
    )
    with urllib.request.urlopen(request, timeout=timeout) as response:
        payload = json.loads(response.read().decode("utf-8"))
    if "error" in payload:
        raise RuntimeError(payload["error"])
    return payload.get("result")


def chain_config(config: dict[str, Any], chain_name: str) -> dict[str, Any]:
    for chain in config.get("chains", []):
        if str(chain.get("name", "")).lower() == chain_name.lower():
            return chain
    raise ValueError(f"chain not found in config: {chain_name}")


def collect_hashes(source_dir: Path, before_dt: datetime | None, after_dt: datetime | None) -> dict[str, dict[str, str]]:
    timestamps: dict[int, int] = {}
    timestamp_path = source_dir / "block_timestamps.json"
    if timestamp_path.exists():
        timestamps = {int(k): int(v) for k, v in read_json(timestamp_path).items()}

    hashes: dict[str, dict[str, str]] = {}
    for path in source_dir.glob("0x*/transfer_*_chunk_*.json"):
        payload = read_json(path)
        for log in payload.get("logs", []):
            tx_hash = str(log.get("transactionHash", "")).lower()
            if not tx_hash:
                continue
            block_number = int(str(log["blockNumber"]), 16)
            block_ts = timestamps.get(block_number)
            if block_ts is not None:
                dt = datetime.fromtimestamp(block_ts, timezone.utc)
                if before_dt and dt >= before_dt:
                    continue
                if after_dt and dt < after_dt:
                    continue
            hashes.setdefault(
                tx_hash,
                {
                    "first_seen_file": str(path),
                    "block_number": str(block_number),
                    "block_timestamp": str(block_ts or ""),
                },
            )
    return hashes


def write_manifest(path: Path, rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=[
                "captured_at",
                "chain",
                "tx_hash",
                "block_number",
                "block_timestamp",
                "result_count",
                "error",
                "file",
                "first_seen_file",
            ],
        )
        writer.writeheader()
        writer.writerows(rows)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", type=Path, default=Path("docs/crypto-transactions/config.json"))
    parser.add_argument("--chain", required=True)
    parser.add_argument("--source-dir", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, default=Path("private/evidence/onchain/raw/rpc-transaction-traces"))
    parser.add_argument("--before-date", help="Only include tx hashes before this UTC date.")
    parser.add_argument("--after-date", help="Only include tx hashes at or after this UTC date.")
    parser.add_argument("--limit", type=int, help="Optional cap for test runs.")
    parser.add_argument("--request-delay", type=float, default=0.03)
    parser.add_argument("--timeout", type=int, default=60)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    config = read_json(args.config)
    chain = chain_config(config, args.chain)
    rpc_url = str(chain.get("trace_rpc_url") or chain.get("rpc_url"))
    before_dt = parse_date(args.before_date)
    after_dt = parse_date(args.after_date)
    tx_hashes = collect_hashes(args.source_dir, before_dt, after_dt)
    selected = sorted(tx_hashes.items())
    if args.limit:
        selected = selected[: args.limit]

    chain_dir = args.output_dir / str(chain["name"])
    chain_dir.mkdir(parents=True, exist_ok=True)
    rows: list[dict[str, str]] = []
    for tx_hash, meta in selected:
        captured_at = datetime.now(timezone.utc).isoformat()
        file_path = chain_dir / f"{tx_hash}.json"
        error = ""
        result_count = 0
        if file_path.exists():
            payload = read_json(file_path)
            traces = payload.get("traces")
            result_count = len(traces) if isinstance(traces, list) else 0
        else:
            try:
                traces = rpc_call(rpc_url, "trace_transaction", [tx_hash], args.timeout)
                if not isinstance(traces, list):
                    traces = []
                result_count = len(traces)
                payload = {
                    "captured_at": captured_at,
                    "chain": chain["name"],
                    "tx_hash": tx_hash,
                    "block_number": meta["block_number"],
                    "block_timestamp": meta["block_timestamp"],
                    "traces": traces,
                }
            except Exception as exc:
                payload = {
                    "captured_at": captured_at,
                    "chain": chain["name"],
                    "tx_hash": tx_hash,
                    "block_number": meta["block_number"],
                    "block_timestamp": meta["block_timestamp"],
                    "traces": [],
                    "error": type(exc).__name__,
                    "message": str(exc),
                }
                error = f"{type(exc).__name__}: {exc}"
            file_path.write_text(json.dumps(payload, indent=2, sort_keys=True), encoding="utf-8")
            time.sleep(args.request_delay)

        rows.append(
            {
                "captured_at": captured_at,
                "chain": str(chain["name"]),
                "tx_hash": tx_hash,
                "block_number": meta["block_number"],
                "block_timestamp": meta["block_timestamp"],
                "result_count": str(result_count),
                "error": error,
                "file": str(file_path),
                "first_seen_file": meta["first_seen_file"],
            }
        )

    suffix = "all"
    if args.before_date:
        suffix = f"before_{args.before_date}"
    if args.after_date:
        suffix = f"after_{args.after_date}"
    manifest_path = args.output_dir / f"manifest_{args.chain}_{suffix}.csv"
    write_manifest(manifest_path, rows)
    print(f"chain: {chain['name']}")
    print(f"tx hashes: {len(selected)}")
    print(f"manifest rows: {len(rows)}")
    print(f"manifest: {manifest_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
