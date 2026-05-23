#!/usr/bin/env python3
"""Archive raw Blockscout v2 address activity for known EVM wallets.

Mode's explorer exposes Blockscout v2 endpoints that are more reliable for
token transfers than its Etherscan-compatible `tokentx` endpoint.

Example:
  python3 docs/crypto-transactions/archive_blockscout_v2_transactions.py \
    --wallets-file docs/crypto-transactions/wallets.txt \
    --chain mode \
    --api-base https://explorer.mode.network/api/v2 \
    --output-dir private/evidence/onchain/raw/blockscout-v2
"""

from __future__ import annotations

import argparse
import csv
import json
import re
import time
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


EVM_ADDRESS_RE = re.compile(r"^0x[a-fA-F0-9]{40}$")
DEFAULT_ENDPOINTS = ["transactions", "token-transfers", "internal-transactions"]


def compact(value: str) -> str:
    return " ".join(str(value or "").split())


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


def fetch_json(url: str, timeout: int) -> dict[str, Any]:
    request = urllib.request.Request(
        url,
        headers={
            "Accept": "application/json",
            "User-Agent": "tax-calculator-blockscout-archive/1.0",
        },
    )
    with urllib.request.urlopen(request, timeout=timeout) as response:
        return json.loads(response.read().decode("utf-8"))


def build_url(api_base: str, address: str, endpoint: str, params: dict[str, Any] | None) -> str:
    base = f"{api_base.rstrip('/')}/addresses/{address}/{endpoint}"
    if not params:
        return base
    return f"{base}?{urllib.parse.urlencode(params)}"


def item_count(payload: dict[str, Any]) -> int:
    items = payload.get("items")
    return len(items) if isinstance(items, list) else 0


def archive_endpoint(
    chain: str,
    api_base: str,
    wallet: dict[str, str],
    endpoint: str,
    output_dir: Path,
    max_pages: int,
    request_delay: float,
    timeout: int,
) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    wallet_dir = output_dir / chain / wallet["address"].lower()
    wallet_dir.mkdir(parents=True, exist_ok=True)
    params: dict[str, Any] | None = None

    for page in range(1, max_pages + 1):
        url = build_url(api_base, wallet["address"], endpoint, params)
        captured_at = datetime.now(timezone.utc).isoformat()
        file_path = wallet_dir / f"{endpoint}_page_{page:04d}.json"
        error = ""
        try:
            payload = fetch_json(url, timeout)
        except Exception as exc:
            payload = {
                "items": [],
                "error": type(exc).__name__,
                "message": str(exc),
                "captured_at": captured_at,
            }
            error = f"{type(exc).__name__}: {exc}"

        payload.setdefault("captured_at", captured_at)
        payload.setdefault("chain", chain)
        payload.setdefault("wallet_label", wallet["label"])
        payload.setdefault("wallet_address", wallet["address"])
        payload.setdefault("endpoint", endpoint)
        payload.setdefault("page", page)
        file_path.write_text(json.dumps(payload, indent=2, sort_keys=True), encoding="utf-8")

        rows.append(
            {
                "captured_at": captured_at,
                "chain": chain,
                "wallet_label": wallet["label"],
                "wallet_address": wallet["address"],
                "endpoint": endpoint,
                "page": str(page),
                "result_count": str(item_count(payload)),
                "error": error or compact(str(payload.get("message", ""))),
                "file": str(file_path),
            }
        )

        next_params = payload.get("next_page_params")
        if error or not isinstance(next_params, dict) or not next_params:
            break
        params = next_params
        time.sleep(request_delay)

    return rows


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
                "endpoint",
                "page",
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
    parser.add_argument("--chain", required=True)
    parser.add_argument("--api-base", required=True)
    parser.add_argument("--output-dir", type=Path, default=Path("private/evidence/onchain/raw/blockscout-v2"))
    parser.add_argument("--wallet-filter", action="append", default=[], help="Wallet label or address filter.")
    parser.add_argument("--endpoint", action="append", choices=DEFAULT_ENDPOINTS, default=[])
    parser.add_argument("--max-pages", type=int, default=200)
    parser.add_argument("--request-delay", type=float, default=0.25)
    parser.add_argument("--timeout", type=int, default=60)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    wallet_filters = {value.lower() for value in args.wallet_filter}
    wallets = read_evm_wallets(args.wallets_file, wallet_filters)
    endpoints = args.endpoint or DEFAULT_ENDPOINTS

    rows: list[dict[str, str]] = []
    for wallet in wallets:
        for endpoint in endpoints:
            rows.extend(
                archive_endpoint(
                    chain=args.chain,
                    api_base=args.api_base,
                    wallet=wallet,
                    endpoint=endpoint,
                    output_dir=args.output_dir,
                    max_pages=args.max_pages,
                    request_delay=args.request_delay,
                    timeout=args.timeout,
                )
            )

    manifest_path = args.output_dir / args.chain / "manifest.csv"
    write_manifest(manifest_path, rows)
    print(f"wallets: {len(wallets)}")
    print(f"endpoints: {len(endpoints)}")
    print(f"manifest rows: {len(rows)}")
    print(f"manifest: {manifest_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
