#!/usr/bin/env python3
"""Extract likely wallet addresses from Koinly transaction-history CSV exports.

This intentionally parses TxSrc/TxDest columns instead of regexing whole files,
because transaction hashes and contract addresses are easy to misclassify.

Example:
  python3 docs/crypto-transactions/extract_koinly_transaction_wallets.py \
    private/evidence/koinly/*/koinly_*_transaction_history_*.csv \
    --existing docs/crypto-transactions/wallets.txt \
    --out-csv private/evidence/wallets/koinly_transaction_wallet_candidates.csv \
    --out-txt private/evidence/wallets/koinly_high_confidence_wallets_new.txt
"""

from __future__ import annotations

import argparse
import csv
import re
from collections import Counter
from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterable


ADDRESS_PATTERNS = [
    ("sui", re.compile(r"^0x[a-fA-F0-9]{64}$")),
    ("evm", re.compile(r"^0x[a-fA-F0-9]{40}$")),
    ("btc", re.compile(r"^(?:bc1[ac-hj-np-z02-9]{11,71}|[13][a-km-zA-HJ-NP-Z1-9]{25,34})$", re.I)),
    (
        "cosmos",
        re.compile(
            r"^(?:cosmos|terra|osmo|juno|akash|secret|kujira|stride|celestia)1[0-9a-z]{38,80}$",
            re.I,
        ),
    ),
    ("substrate", re.compile(r"^[1-9A-HJ-NP-Za-km-z]{45,60}$")),
    ("solana", re.compile(r"^[1-9A-HJ-NP-Za-km-z]{32,44}$")),
]

EXCLUDED_LABEL_RE = re.compile(
    r"\b(?:binance|kraken|coinbase|ftx|celsius|blockfi|simplex|paypal|revolut)\b",
    re.I,
)
SELF_CUSTODY_LABEL_RE = re.compile(
    r"\b(?:metamask|reaper|terra|terrastation|osmosis|cosmos|polkadot|kusama|dot|ksm|solana|sui|electrum|fearless)\b",
    re.I,
)


@dataclass
class Candidate:
    label: str
    address: str
    family: str
    source_count: int = 0
    destination_count: int = 0
    first_seen: str = ""
    last_seen: str = ""
    currencies: Counter[str] = field(default_factory=Counter)
    examples: list[str] = field(default_factory=list)

    @property
    def total_count(self) -> int:
        return self.source_count + self.destination_count


def address_family(value: str) -> str:
    for family, pattern in ADDRESS_PATTERNS:
        if pattern.match(value):
            return family
    return ""


def compact(value: str, max_len: int = 160) -> str:
    text = " ".join(str(value or "").split())
    if len(text) <= max_len:
        return text
    return text[: max_len - 1] + "…"


def read_existing_addresses(path: Path) -> set[str]:
    existing: set[str] = set()
    if not path.exists():
        return existing
    for raw in path.read_text(encoding="utf-8", errors="replace").splitlines():
        line = compact(raw)
        if not line or line.startswith("#") or " " not in line:
            continue
        existing.add(line.rsplit(" ", 1)[-1].lower())
    return existing


def headered_koinly_rows(path: Path) -> Iterable[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as f:
        header = None
        for line in f:
            if line.startswith("Date,"):
                header = next(csv.reader([line]))
                break
        if header is None:
            return
        yield from csv.DictReader(f, fieldnames=header)


def add_observation(
    candidates: dict[tuple[str, str], Candidate],
    label: str,
    address: str,
    side: str,
    row: dict[str, str],
) -> None:
    if not label or EXCLUDED_LABEL_RE.search(label):
        return
    family = address_family(address)
    if not family:
        return

    key = (label, address)
    candidate = candidates.get(key)
    if candidate is None:
        candidate = Candidate(label=label, address=address, family=family)
        candidates[key] = candidate

    if side == "source":
        candidate.source_count += 1
    else:
        candidate.destination_count += 1

    date = (row.get("Date") or "")[:10]
    if date:
        candidate.first_seen = min(candidate.first_seen, date) if candidate.first_seen else date
        candidate.last_seen = max(candidate.last_seen, date) if candidate.last_seen else date

    for key_name in ("Sent Currency", "Received Currency"):
        currency = compact(row.get(key_name, ""), 40)
        if currency:
            candidate.currencies[currency] += 1

    if len(candidate.examples) < 3:
        candidate.examples.append(
            compact(
                " | ".join(
                    [
                        row.get("Date", ""),
                        row.get("Type", ""),
                        row.get("Sending Wallet", ""),
                        row.get("Receiving Wallet", ""),
                        row.get("Sent Currency", ""),
                        row.get("Received Currency", ""),
                        row.get("Description", ""),
                    ]
                ),
                300,
            )
        )


def classify(candidate: Candidate, existing: set[str]) -> str:
    if candidate.address.lower() in existing:
        return "known"
    if not SELF_CUSTODY_LABEL_RE.search(candidate.label):
        return "not_self_custody_label"
    if candidate.address == "0x0000000000000000000000000000000000000000":
        return "contract_or_protocol"

    # Same address acting both as source and destination under a self-custody
    # Koinly wallet label is the strongest signal.
    if candidate.source_count > 0 and candidate.destination_count > 0:
        return "high_confidence_wallet"

    # EVM destination-only entries under MetaMask/Reaper labels are normally
    # routers, LP contracts, token contracts, or vaults. Do not import them as
    # owned wallets without manual confirmation.
    if candidate.family == "evm" and candidate.destination_count > 0 and candidate.source_count == 0:
        return "contract_or_protocol"

    # A recurring source address under MetaMask/Reaper is usually the actual
    # externally-owned account, even if the CSV only has outgoing DeFi rows.
    if candidate.family == "evm" and candidate.source_count >= 2:
        return "high_confidence_wallet"

    if candidate.family in {"cosmos", "substrate", "solana", "btc", "sui"} and candidate.total_count >= 2:
        return "likely_wallet_or_chain_account"

    return "needs_manual_review"


def parse_inputs(paths: list[Path]) -> dict[tuple[str, str], Candidate]:
    candidates: dict[tuple[str, str], Candidate] = {}
    for path in paths:
        for row in headered_koinly_rows(path):
            sending_wallet = compact(row.get("Sending Wallet", ""), 120)
            receiving_wallet = compact(row.get("Receiving Wallet", ""), 120)
            tx_src = compact(row.get("TxSrc", ""), 120)
            tx_dest = compact(row.get("TxDest", ""), 120)
            add_observation(candidates, sending_wallet, tx_src, "source", row)
            add_observation(candidates, receiving_wallet, tx_dest, "destination", row)
    return candidates


def write_csv(path: Path, candidates: list[Candidate], existing: set[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=[
                "classification",
                "label",
                "address",
                "family",
                "first_seen",
                "last_seen",
                "source_count",
                "destination_count",
                "total_count",
                "top_currencies",
                "examples",
            ],
        )
        writer.writeheader()
        for candidate in candidates:
            writer.writerow(
                {
                    "classification": classify(candidate, existing),
                    "label": candidate.label,
                    "address": candidate.address,
                    "family": candidate.family,
                    "first_seen": candidate.first_seen,
                    "last_seen": candidate.last_seen,
                    "source_count": candidate.source_count,
                    "destination_count": candidate.destination_count,
                    "total_count": candidate.total_count,
                    "top_currencies": "; ".join(
                        currency for currency, _ in candidate.currencies.most_common(8)
                    ),
                    "examples": " || ".join(candidate.examples),
                }
            )


def wallet_line(candidate: Candidate) -> str:
    label = re.sub(r"\s+", " ", candidate.label).strip()
    if candidate.family == "cosmos" and candidate.address.startswith("terra"):
        label = f"{label} main"
    elif candidate.family == "cosmos" and candidate.address.startswith("osmo"):
        label = f"{label} main"
    elif candidate.family == "cosmos" and candidate.address.startswith("cosmos"):
        label = f"{label} main"
    elif label.lower() == "metamask":
        label = "Old MetaMask"
    return f"{label} {candidate.address}"


def write_txt(path: Path, candidates: list[Candidate], existing: set[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        wallet_line(candidate)
        for candidate in candidates
        if classify(candidate, existing) == "high_confidence_wallet"
        and candidate.address.lower() not in existing
    ]
    path.write_text("\n".join(lines) + ("\n" if lines else ""), encoding="utf-8")


def expand_inputs(values: list[str]) -> list[Path]:
    paths: list[Path] = []
    for value in values:
        if any(char in value for char in "*?["):
            paths.extend(sorted(Path().glob(value)))
        else:
            paths.append(Path(value))
    return paths


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("inputs", nargs="+", help="Koinly transaction-history CSV exports.")
    parser.add_argument(
        "--existing",
        type=Path,
        default=Path("docs/crypto-transactions/wallets.txt"),
        help="Existing wallet list used to mark known addresses.",
    )
    parser.add_argument(
        "--out-csv",
        type=Path,
        default=Path("private/evidence/wallets/koinly_transaction_wallet_candidates.csv"),
    )
    parser.add_argument(
        "--out-txt",
        type=Path,
        default=Path("private/evidence/wallets/koinly_high_confidence_wallets_new.txt"),
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    paths = expand_inputs(args.inputs)
    missing = [path for path in paths if not path.exists()]
    if missing:
        raise FileNotFoundError(", ".join(str(path) for path in missing))

    existing = read_existing_addresses(args.existing)
    candidates = sorted(
        parse_inputs(paths).values(),
        key=lambda candidate: (
            classify(candidate, existing),
            candidate.label.lower(),
            candidate.last_seen,
            -candidate.total_count,
            candidate.address.lower(),
        ),
    )
    write_csv(args.out_csv, candidates, existing)
    write_txt(args.out_txt, candidates, existing)

    counts = Counter(classify(candidate, existing) for candidate in candidates)
    print(f"inputs: {len(paths)}")
    print(f"candidates: {len(candidates)}")
    for key, count in sorted(counts.items()):
        print(f"{key}: {count}")
    print(f"csv: {args.out_csv}")
    print(f"txt: {args.out_txt}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
