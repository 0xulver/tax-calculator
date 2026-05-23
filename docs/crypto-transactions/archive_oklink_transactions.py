#!/usr/bin/env python3
"""Archive raw OKLink address activity for known wallets.

Fantom is no longer reliably available through the Etherscan v2 account API,
but OKLink exposes Fantom as chain short name `FTM`.

Example:
  OKLINK_API_KEY=... python3 docs/crypto-transactions/archive_oklink_transactions.py \
    --wallets-file docs/crypto-transactions/wallets.txt \
    --config docs/crypto-transactions/config.json \
    --chain-filter fantom \
    --output-dir private/evidence/onchain/raw/oklink
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
DEFAULT_ACTIONS = ["normal", "internal", "token_20", "token_721", "token_1155"]
ACTION_ENDPOINTS = {
    "normal": ("normal-transaction-list", ""),
    "internal": ("internal-transaction-list", ""),
    "token_20": ("token-transaction-list", "token_20"),
    "token_721": ("token-transaction-list", "token_721"),
    "token_1155": ("token-transaction-list", "token_1155"),
}


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


def oklink_chains(config: dict[str, Any], chain_filters: set[str]) -> list[dict[str, Any]]:
    chains = []
    for chain in config.get("chains", []):
        if chain.get("type") != "oklink_explorer":
            continue
        if chain_filters and str(chain.get("name", "")).lower() not in chain_filters:
            continue
        chains.append(chain)
    return chains


def fetch_json(url: str, api_key: str, timeout: int) -> dict[str, Any]:
    request = urllib.request.Request(
        url,
        headers={
            "Accept": "application/json",
            "Ok-Access-Key": api_key,
            "User-Agent": "tax-calculator-oklink-archive/1.0",
        },
    )
    with urllib.request.urlopen(request, timeout=timeout) as response:
        return json.loads(response.read().decode("utf-8"))


def build_url(
    chain: dict[str, Any],
    wallet: dict[str, str],
    action: str,
    page: int,
    limit: int,
    start_block_height: int | None,
    end_block_height: int | None,
) -> str:
    endpoint, protocol_type = ACTION_ENDPOINTS[action]
    api_url = str(chain.get("api_url") or "https://www.oklink.com").rstrip("/")
    params: dict[str, Any] = {
        "chainShortName": chain.get("chain_short_name") or chain.get("chainShortName"),
        "address": wallet["address"],
        "page": page,
        "limit": limit,
    }
    if protocol_type:
        params["protocolType"] = protocol_type
    if start_block_height is not None:
        params["startBlockHeight"] = start_block_height
    if end_block_height is not None:
        params["endBlockHeight"] = end_block_height
    return f"{api_url}/api/v5/explorer/address/{endpoint}?{urllib.parse.urlencode(params)}"


def first_data_page(payload: dict[str, Any]) -> dict[str, Any]:
    data = payload.get("data")
    if isinstance(data, list) and data and isinstance(data[0], dict):
        return data[0]
    if isinstance(data, dict):
        return data
    return {}


def transaction_rows(payload: dict[str, Any]) -> list[Any]:
    page = first_data_page(payload)
    for key in ("transactionList", "transactionLists"):
        value = page.get(key)
        if isinstance(value, list):
            return value
    return []


def total_page(payload: dict[str, Any]) -> int:
    page = first_data_page(payload)
    try:
        return int(page.get("totalPage") or 1)
    except (TypeError, ValueError):
        return 1


def response_error(payload: dict[str, Any]) -> str:
    code = str(payload.get("code", ""))
    if code in ("", "0"):
        return ""
    return compact(str(payload.get("msg") or payload.get("detailMsg") or payload.get("message") or code))


def archive_action(
    chain: dict[str, Any],
    wallet: dict[str, str],
    action: str,
    output_dir: Path,
    api_key: str,
    page_size: int,
    max_pages: int,
    request_delay: float,
    timeout: int,
    start_block_height: int | None,
    end_block_height: int | None,
) -> list[dict[str, str]]:
    manifest_rows: list[dict[str, str]] = []
    chain_name = str(chain["name"])
    endpoint, protocol_type = ACTION_ENDPOINTS[action]
    wallet_dir = output_dir / chain_name / wallet["address"].lower()
    wallet_dir.mkdir(parents=True, exist_ok=True)

    for page in range(1, max_pages + 1):
        url = build_url(chain, wallet, action, page, page_size, start_block_height, end_block_height)
        file_path = wallet_dir / f"{action}_page_{page:04d}.json"
        captured_at = datetime.now(timezone.utc).isoformat()
        error = ""
        try:
            payload = fetch_json(url, api_key, timeout)
        except Exception as exc:
            payload = {
                "code": "error",
                "msg": type(exc).__name__,
                "detailMsg": str(exc),
                "data": [],
                "captured_at": captured_at,
            }
            error = f"{type(exc).__name__}: {exc}"

        payload.setdefault("captured_at", captured_at)
        payload.setdefault("chain", chain_name)
        payload.setdefault("chain_short_name", chain.get("chain_short_name") or chain.get("chainShortName"))
        payload.setdefault("wallet_label", wallet["label"])
        payload.setdefault("wallet_address", wallet["address"])
        payload.setdefault("action", action)
        payload.setdefault("endpoint", endpoint)
        payload.setdefault("protocol_type", protocol_type)
        payload.setdefault("page", page)
        file_path.write_text(json.dumps(payload, indent=2, sort_keys=True), encoding="utf-8")

        count = len(transaction_rows(payload))
        error = error or response_error(payload)
        manifest_rows.append(
            {
                "captured_at": captured_at,
                "chain": chain_name,
                "chain_short_name": str(chain.get("chain_short_name") or chain.get("chainShortName") or ""),
                "wallet_label": wallet["label"],
                "wallet_address": wallet["address"],
                "action": action,
                "endpoint": endpoint,
                "protocol_type": protocol_type,
                "page": str(page),
                "result_count": str(count),
                "error": error,
                "file": str(file_path),
            }
        )

        if error or count == 0 or page >= total_page(payload):
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
                "chain_short_name",
                "wallet_label",
                "wallet_address",
                "action",
                "endpoint",
                "protocol_type",
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
    parser.add_argument("--output-dir", type=Path, default=Path("private/evidence/onchain/raw/oklink"))
    parser.add_argument("--wallet-filter", action="append", default=[], help="Wallet label or address filter.")
    parser.add_argument("--chain-filter", action="append", default=[], help="Chain name filter.")
    parser.add_argument("--action", action="append", choices=DEFAULT_ACTIONS, default=[])
    parser.add_argument("--page-size", type=int, default=100)
    parser.add_argument("--max-pages", type=int, default=1000)
    parser.add_argument("--request-delay", type=float, default=0.25)
    parser.add_argument("--timeout", type=int, default=60)
    parser.add_argument("--start-block-height", type=int)
    parser.add_argument("--end-block-height", type=int)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    load_env_file()
    api_key = os.getenv("OKLINK_API_KEY", "")
    if not api_key:
        print("OKLINK_API_KEY is not set. Add it to .env to archive OKLink/Fantom history.")
        return 2

    config = read_json(args.config)
    wallet_filters = {value.lower() for value in args.wallet_filter}
    chain_filters = {value.lower() for value in args.chain_filter}
    actions = args.action or DEFAULT_ACTIONS
    wallets = read_evm_wallets(args.wallets_file, wallet_filters)
    chains = oklink_chains(config, chain_filters)

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
                        api_key=api_key,
                        page_size=args.page_size,
                        max_pages=args.max_pages,
                        request_delay=args.request_delay,
                        timeout=args.timeout,
                        start_block_height=args.start_block_height,
                        end_block_height=args.end_block_height,
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
