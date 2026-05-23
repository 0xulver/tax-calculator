#!/usr/bin/env python3
"""Extract wallet candidates from Koinly page/network dumps.

Example:
  python3 docs/crypto-transactions/extract_koinly_wallets.py \
    private/evidence/koinly/wallets/*.json \
    --existing docs/crypto-transactions/wallets.txt \
    --out-csv private/evidence/wallets/koinly_wallet_candidates.csv \
    --out-txt private/evidence/wallets/koinly_wallets_new.txt
"""

from __future__ import annotations

import argparse
import csv
import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable


ADDRESS_PATTERNS = [
    ("sui", re.compile(r"\b0x[a-fA-F0-9]{64}\b")),
    ("evm", re.compile(r"\b0x[a-fA-F0-9]{40}\b")),
    ("btc", re.compile(r"\bbc1[ac-hj-np-z02-9]{11,71}\b", re.IGNORECASE)),
    ("btc", re.compile(r"\b[13][a-km-zA-HJ-NP-Z1-9]{25,34}\b")),
    (
        "cosmos",
        re.compile(
            r"\b(?:cosmos|terra|osmo|juno|akash|secret|kujira|stride|celestia)1[0-9a-z]{38,80}\b",
            re.IGNORECASE,
        ),
    ),
    ("substrate", re.compile(r"\b[1-9A-HJ-NP-Za-km-z]{45,60}\b")),
    ("solana", re.compile(r"\b[1-9A-HJ-NP-Za-km-z]{32,44}\b")),
]

NAME_KEYS = {
    "name",
    "label",
    "title",
    "display_name",
    "displayName",
    "wallet_name",
    "walletName",
    "account_name",
    "accountName",
    "slug",
}
CHAIN_KEYS = {
    "chain",
    "chain_name",
    "chainName",
    "network",
    "blockchain",
    "blockchain_name",
    "blockchainName",
    "platform",
    "provider",
    "service",
    "exchange",
    "integration",
    "type",
}


@dataclass(frozen=True)
class Candidate:
    label: str
    address: str
    family: str
    chain: str
    source_file: str
    source_path: str
    raw_context: str


def compact(value: Any, max_len: int = 300) -> str:
    text = " ".join(str(value or "").split())
    if len(text) <= max_len:
        return text
    return text[: max_len - 1] + "…"


def extract_addresses(text: str) -> list[tuple[str, str]]:
    found: dict[str, str] = {}
    for family, pattern in ADDRESS_PATTERNS:
        for match in pattern.finditer(text):
            address = match.group(0)
            found.setdefault(address, family)
    return [(address, family) for address, family in found.items()]


def best_field(obj: dict[str, Any], keys: set[str]) -> str:
    for key in keys:
        if key in obj and isinstance(obj[key], (str, int, float)):
            value = compact(obj[key], 120)
            if value:
                return value
    return ""


def label_from_text(text: str, address: str) -> str:
    before = text.split(address, 1)[0]
    before = re.sub(r"https?://\S+", " ", before)
    before = re.sub(r"[/|,:;()\[\]{}]+", " ", before)
    before = compact(before, 80)
    return before or "Koinly wallet"


def candidates_from_text(
    text: str,
    source_file: str,
    source_path: str,
    label_hint: str = "",
    chain_hint: str = "",
) -> Iterable[Candidate]:
    for address, family in extract_addresses(text):
        label = label_hint or label_from_text(text, address)
        yield Candidate(
            label=label,
            address=address,
            family=family,
            chain=chain_hint,
            source_file=source_file,
            source_path=source_path,
            raw_context=compact(text, 500),
        )


def walk_json(value: Any, source_file: str, source_path: str = "$") -> Iterable[Candidate]:
    if isinstance(value, dict):
        label_hint = best_field(value, NAME_KEYS)
        chain_hint = best_field(value, CHAIN_KEYS)
        scalar_text = " ".join(
            compact(v, 500)
            for v in value.values()
            if isinstance(v, (str, int, float))
        )
        if scalar_text:
            yield from candidates_from_text(
                scalar_text,
                source_file,
                source_path,
                label_hint=label_hint,
                chain_hint=chain_hint,
            )

        for key, child in value.items():
            yield from walk_json(child, source_file, f"{source_path}.{key}")
        return

    if isinstance(value, list):
        for idx, child in enumerate(value):
            yield from walk_json(child, source_file, f"{source_path}[{idx}]")
        return

    if isinstance(value, str):
        yield from candidates_from_text(value, source_file, source_path)


def load_dump(path: Path) -> Any:
    text = path.read_text(encoding="utf-8", errors="replace")
    if path.suffix.lower() == ".json":
        return json.loads(text)
    return text


def read_existing_addresses(path: Path | None) -> set[str]:
    if not path or not path.exists():
        return set()
    addresses: set[str] = set()
    for raw in path.read_text(encoding="utf-8", errors="replace").splitlines():
        line = compact(raw)
        if not line or line.startswith("#") or " " not in line:
            continue
        addresses.add(line.rsplit(" ", 1)[-1].lower())
    return addresses


def dedupe(candidates: Iterable[Candidate]) -> list[Candidate]:
    selected: dict[str, Candidate] = {}
    for candidate in candidates:
        key = candidate.address.lower()
        current = selected.get(key)
        if current is None:
            selected[key] = candidate
            continue
        if current.label == "Koinly wallet" and candidate.label != "Koinly wallet":
            selected[key] = candidate
    return sorted(selected.values(), key=lambda row: (row.family, row.label.lower(), row.address.lower()))


def write_csv(path: Path, rows: list[Candidate], existing: set[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=[
                "status",
                "label",
                "address",
                "family",
                "chain",
                "source_file",
                "source_path",
                "raw_context",
            ],
        )
        writer.writeheader()
        for row in rows:
            writer.writerow(
                {
                    "status": "existing" if row.address.lower() in existing else "new",
                    "label": row.label,
                    "address": row.address,
                    "family": row.family,
                    "chain": row.chain,
                    "source_file": row.source_file,
                    "source_path": row.source_path,
                    "raw_context": row.raw_context,
                }
            )


def write_txt(path: Path, rows: list[Candidate], existing: set[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = []
    for row in rows:
        if row.address.lower() in existing:
            continue
        label = re.sub(r"\s+", " ", row.label).strip() or "Koinly wallet"
        lines.append(f"{label} {row.address}")
    path.write_text("\n".join(lines) + ("\n" if lines else ""), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("inputs", nargs="+", help="Koinly JSON/HTML/text dumps to parse.")
    parser.add_argument(
        "--existing",
        type=Path,
        default=Path("docs/crypto-transactions/wallets.txt"),
        help="Existing wallet list used to mark duplicates.",
    )
    parser.add_argument(
        "--out-csv",
        type=Path,
        default=Path("private/evidence/wallets/koinly_wallet_candidates.csv"),
        help="CSV output path.",
    )
    parser.add_argument(
        "--out-txt",
        type=Path,
        default=Path("private/evidence/wallets/koinly_wallets_new.txt"),
        help="wallets.txt-format output path for new addresses only.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    all_candidates: list[Candidate] = []
    for input_glob in args.inputs:
        paths = sorted(Path().glob(input_glob)) if any(ch in input_glob for ch in "*?[") else [Path(input_glob)]
        for path in paths:
            if not path.exists():
                raise FileNotFoundError(path)
            dump = load_dump(path)
            if isinstance(dump, str):
                all_candidates.extend(candidates_from_text(dump, str(path), "$"))
            else:
                all_candidates.extend(walk_json(dump, str(path)))

    rows = dedupe(all_candidates)
    existing = read_existing_addresses(args.existing)
    write_csv(args.out_csv, rows, existing)
    write_txt(args.out_txt, rows, existing)

    new_count = sum(1 for row in rows if row.address.lower() not in existing)
    print(f"wallet candidates: {len(rows)}")
    print(f"new addresses: {new_count}")
    print(f"csv: {args.out_csv}")
    print(f"txt: {args.out_txt}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
