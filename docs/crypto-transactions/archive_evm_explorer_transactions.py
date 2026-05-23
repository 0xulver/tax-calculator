#!/usr/bin/env python3
"""Archive raw EVM explorer account responses for known wallets.

This stores source JSON pages under private evidence so later tax calculations
can be reproduced without refetching explorer APIs.

Example:
  ETHERSCAN_API_KEY=... python3 docs/crypto-transactions/archive_evm_explorer_transactions.py \
    --wallets-file docs/crypto-transactions/wallets.txt \
    --config docs/crypto-transactions/config.json \
    --output-dir private/evidence/onchain/raw/evm-explorer \
    --chain-filter ethereum --chain-filter polygon --chain-filter fantom
"""

from __future__ import annotations

import argparse
import csv
import json
import os
import re
import time
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


EVM_ADDRESS_RE = re.compile(r"^0x[a-fA-F0-9]{40}$")
DEFAULT_ACTIONS = ["txlist", "tokentx", "tokennfttx", "token1155tx", "txlistinternal"]


def compact(value: str) -> str:
    return " ".join(str(value or "").split())


def read_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def load_env_file(path: Path = Path(".env")) -> None:
    if not path.exists():
        return
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        os.environ.setdefault(key.strip(), value.strip().strip('"').strip("'"))


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


def evm_chains(config: dict[str, Any], chain_filters: set[str]) -> list[dict[str, Any]]:
    chains = []
    for chain in config.get("chains", []):
        if chain.get("type") != "evm_explorer":
            continue
        if chain_filters and str(chain.get("name", "")).lower() not in chain_filters:
            continue
        chains.append(chain)
    return chains


def fetch_json(url: str, timeout: int) -> dict[str, Any]:
    request = urllib.request.Request(
        url,
        headers={
            "Accept": "application/json",
            "User-Agent": "tax-calculator-evm-archive/1.0",
        },
    )
    with urllib.request.urlopen(request, timeout=timeout) as response:
        return json.loads(response.read().decode("utf-8"))


def build_url(
    chain: dict[str, Any],
    wallet: dict[str, str],
    action: str,
    page: int,
    offset: int,
) -> str:
    params = {
        "module": "account",
        "action": action,
        "address": wallet["address"],
        "startblock": 0,
        "endblock": 99999999,
        "page": page,
        "offset": offset,
        "sort": "asc",
    }
    chainid = str(chain.get("chainid", "")).strip()
    if chainid:
        params["chainid"] = chainid
    api_key_name = chain.get("api_key_env", "")
    api_key = os.getenv(api_key_name, "") if api_key_name else ""
    if api_key:
        params["apikey"] = api_key
    return f"{chain.get('api_url') or chain.get('base_url')}?{urllib.parse.urlencode(params)}"


def page_result_count(payload: dict[str, Any]) -> int:
    result = payload.get("result")
    return len(result) if isinstance(result, list) else 0


def response_error(payload: dict[str, Any]) -> str:
    status = str(payload.get("status", ""))
    result = payload.get("result")
    if status == "1" or result in (None, [], "No transactions found"):
        return ""
    return compact(str(result or payload.get("message", "")))


def archive_action(
    chain: dict[str, Any],
    wallet: dict[str, str],
    action: str,
    output_dir: Path,
    page_size: int,
    max_pages: int,
    request_delay: float,
    timeout: int,
) -> list[dict[str, str]]:
    manifest_rows: list[dict[str, str]] = []
    chain_name = str(chain["name"])
    wallet_dir = output_dir / chain_name / wallet["address"].lower()
    wallet_dir.mkdir(parents=True, exist_ok=True)

    for page in range(1, max_pages + 1):
        url = build_url(chain, wallet, action, page, page_size)
        file_path = wallet_dir / f"{action}_page_{page:04d}.json"
        captured_at = datetime.now(timezone.utc).isoformat()
        try:
            payload = fetch_json(url, timeout)
        except Exception as exc:
            payload = {
                "status": "error",
                "message": type(exc).__name__,
                "result": str(exc),
                "captured_at": captured_at,
            }
        payload.setdefault("captured_at", captured_at)
        payload.setdefault("chain", chain_name)
        payload.setdefault("wallet_label", wallet["label"])
        payload.setdefault("wallet_address", wallet["address"])
        payload.setdefault("action", action)
        payload.setdefault("page", page)

        file_path.write_text(json.dumps(payload, indent=2, sort_keys=True), encoding="utf-8")

        count = page_result_count(payload)
        error = response_error(payload)
        manifest_rows.append(
            {
                "captured_at": captured_at,
                "chain": chain_name,
                "wallet_label": wallet["label"],
                "wallet_address": wallet["address"],
                "action": action,
                "page": str(page),
                "result_count": str(count),
                "error": error,
                "file": str(file_path),
            }
        )

        if error or count < page_size:
            break
        time.sleep(request_delay)

    return manifest_rows


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
                "action",
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
    parser.add_argument("--config", type=Path, default=Path("docs/crypto-transactions/config.json"))
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("private/evidence/onchain/raw/evm-explorer"),
    )
    parser.add_argument("--wallet-filter", action="append", default=[], help="Wallet label or address filter.")
    parser.add_argument("--chain-filter", action="append", default=[], help="Chain name filter.")
    parser.add_argument("--action", action="append", choices=DEFAULT_ACTIONS, default=[])
    parser.add_argument("--page-size", type=int, default=1000)
    parser.add_argument("--max-pages", type=int, default=1000)
    parser.add_argument("--request-delay", type=float, default=0.25)
    parser.add_argument("--timeout", type=int, default=60)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    load_env_file()
    config = read_json(args.config)
    wallet_filters = {value.lower() for value in args.wallet_filter}
    chain_filters = {value.lower() for value in args.chain_filter}
    actions = args.action or DEFAULT_ACTIONS
    wallets = read_evm_wallets(args.wallets_file, wallet_filters)
    chains = evm_chains(config, chain_filters)

    manifest_rows: list[dict[str, str]] = []
    for wallet in wallets:
        for chain in chains:
            for action in actions:
                manifest_rows.extend(
                    archive_action(
                        chain=chain,
                        wallet=wallet,
                        action=action,
                        output_dir=args.output_dir,
                        page_size=args.page_size,
                        max_pages=args.max_pages,
                        request_delay=args.request_delay,
                        timeout=args.timeout,
                    )
                )

    manifest_path = args.output_dir / "manifest.csv"
    write_manifest(manifest_path, manifest_rows)
    print(f"wallets: {len(wallets)}")
    print(f"chains: {len(chains)}")
    print(f"actions: {len(actions)}")
    print(f"manifest rows: {len(manifest_rows)}")
    print(f"manifest: {manifest_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
