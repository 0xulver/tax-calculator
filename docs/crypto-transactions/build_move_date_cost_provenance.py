#!/usr/bin/env python3
"""Build a move-date cost-provenance workpaper.

This script does not create final PIT-38 values. It converts the move-date
asset inventory into a reviewable imported-basis ledger with explicit legal /
evidence layers:

- A: documented pre-residency fiat/direct purchase basis candidate
- B: same-token Sweden-taxed salary USDC candidate
- C: replacement-asset / DeFi receipt basis candidate
- D: unknown, spam, airdrop, NFT, or no-basis pending proof
- E: reconciliation exception / debt / incomplete native-flow row

The output deliberately separates "candidate source evidence" from "importable
PLN basis". A row is not filing-ready until the Swedish acquisition or
replacement-basis trace and PLN translation are filled.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
from collections import Counter, defaultdict
from dataclasses import dataclass
from datetime import datetime, timezone
from decimal import Decimal, InvalidOperation
from pathlib import Path
from typing import Iterable


DEFAULT_INVENTORY_DIR = Path("private/evidence/onchain/move-date-inventory-2023-04-12")
DEFAULT_KOINLY_2022_EOY = Path(
    "private/evidence/koinly/2022/koinly_2022_end_of_year_holdings_report_e7abrLJ2nY_1777113106.csv"
)
DEFAULT_KOINLY_2020_EOY = Path(
    "private/evidence/koinly/2020/koinly_2020_end_of_year_holdings_report_YZt3yZnR3Z_1777112647.csv"
)
DEFAULT_KOINLY_2022_TX = Path(
    "private/evidence/koinly/2022/koinly_2022_transaction_history_krYwagtox4_1777112970.csv"
)

MOVE_CUTOFF = "2023-04-12T00:00:00Z"
PREMOVE_2023_START = datetime(2023, 1, 1, tzinfo=timezone.utc)

SPAM_HINTS = (
    "visit",
    "claim",
    "airdrop",
    "casino",
    "gambling",
    "reward.xyz",
    "rewards",
    "free",
    ".com",
    ".net",
    ".org",
    "2xcoin",
    "2xbnb",
    "minereum",
    "quick-v2",
    "errornotice",
    ".io",
)

DIRECT_ASSET_SYMBOLS = {
    "AAVE",
    "ATOM",
    "BTC",
    "CEL",
    "CRV",
    "DAI",
    "DOT",
    "ETH",
    "FTM",
    "FXS",
    "GRAIN",
    "KSM",
    "LINK",
    "MATIC",
    "MIM",
    "OATH",
    "OP",
    "OXD",
    "SNX",
    "SOL",
    "SUSD",
    "USDC",
    "USDT",
    "WBTC",
    "WETH",
    "WFTM",
}

STABLECOIN_SYMBOLS = {
    "BUSD",
    "DAI",
    "DAI+",
    "FRAX",
    "FUSDT",
    "GDAI",
    "GUSDC",
    "MAI",
    "MIM",
    "SUSD",
    "USDC",
    "USDC.E",
    "USDT",
}

WRAPPED_ALIASES = {
    "WETH": "ETH",
    "ETH.E": "ETH",
    "WFTM": "FTM",
    "WMATIC": "MATIC",
    "WBTC": "BTC",
    "USDC.E": "USDC",
    "FUSDT": "USDT",
}

DEFI_HINTS = (
    " aave ",
    " amm",
    " balancer",
    " borrow",
    " ctoken",
    " crypt",
    " deposit",
    " dforce",
    " gauge",
    " geist",
    " granary",
    " interest bearing",
    " lp",
    " moo",
    " pool",
    " receipt",
    " reaper",
    " scream wrapped",
    " solidly",
    " sonne",
    " tarot",
    " vault",
    " wrapped usdc",
    " wrapped dai",
    " wrapped weth",
    " yvault",
)

DEFI_SYMBOL_PREFIXES = (
    "A",
    "AYV",
    "BB-",
    "BH",
    "BPT",
    "BTAROT",
    "CTAROT",
    "FX-",
    "G",
    "I",
    "MOO",
    "NEAD-",
    "RF",
    "SC",
    "SW",
    "YV",
)


@dataclass
class HoldingEvidence:
    symbol: str
    asset: str
    quantity: Decimal
    cost_sek: Decimal
    value_sek: Decimal
    source_file: str


def parse_decimal(value: str | None) -> Decimal:
    text = str(value or "").strip().strip('"')
    if not text:
        return Decimal("0")
    text = text.replace("\u00a0", " ").replace(" ", "")
    if "," in text and "." in text:
        text = text.replace(",", "")
    elif "," in text:
        text = text.replace(",", ".")
    try:
        return Decimal(text)
    except InvalidOperation:
        return Decimal("0")


def fmt_decimal(value: Decimal | str | None) -> str:
    if value is None:
        return ""
    if not isinstance(value, Decimal):
        value = parse_decimal(str(value))
    text = format(value.normalize(), "f")
    if "." in text:
        text = text.rstrip("0").rstrip(".")
    return text or "0"


def read_csv_after_title(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        return []
    lines = path.read_text(encoding="utf-8-sig", errors="replace").splitlines()
    while lines and not lines[0].startswith("Asset,") and not lines[0].startswith("Date,"):
        lines.pop(0)
    if not lines:
        return []
    return list(csv.DictReader(lines))


def symbol_from_asset(asset: str) -> str:
    return asset.split(" (", 1)[0].strip().upper()


def normalize_symbol(symbol: str) -> str:
    return (symbol or "").strip().upper()


def evidence_symbol(symbol: str) -> str:
    normalized = normalize_symbol(symbol)
    return WRAPPED_ALIASES.get(normalized, normalized)


def load_holdings(path: Path) -> dict[str, HoldingEvidence]:
    holdings: dict[str, HoldingEvidence] = {}
    for row in read_csv_after_title(path):
        asset = row.get("Asset", "")
        symbol = symbol_from_asset(asset)
        if not symbol or symbol == "TOTAL":
            continue
        holdings[symbol] = HoldingEvidence(
            symbol=symbol,
            asset=asset,
            quantity=parse_decimal(row.get("Quantity")),
            cost_sek=parse_decimal(row.get("Cost (SEK)")),
            value_sek=parse_decimal(row.get("Value (SEK)")),
            source_file=str(path),
        )
    return holdings


def load_koinly_tx_hashes(path: Path) -> set[str]:
    hashes: set[str] = set()
    for row in read_csv_after_title(path):
        tx_hash = str(row.get("TxHash", "") or "").lower()
        if tx_hash:
            hashes.add(tx_hash)
    return hashes


def parse_iso(value: str) -> datetime | None:
    if not value:
        return None
    try:
        return datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return None


def row_key(row: dict[str, str]) -> tuple[str, str, str, str, str, str]:
    return (
        row.get("chain", ""),
        row.get("wallet_address", "").lower(),
        row.get("asset_type", ""),
        row.get("contract_address", "").lower(),
        row.get("token_id", ""),
        row.get("symbol", ""),
    )


def text_blob(row: dict[str, str]) -> str:
    return f" {row.get('symbol', '')} {row.get('name', '')} {row.get('basis_status', '')} ".lower()


def looks_like_spam(row: dict[str, str]) -> bool:
    text = text_blob(row)
    return any(hint in text for hint in SPAM_HINTS)


def looks_like_debt_or_exception(row: dict[str, str]) -> bool:
    text = text_blob(row)
    amount = parse_decimal(row.get("amount"))
    return (
        amount < 0
        or "reconciliation exception" in text
        or "partial native-flow estimate" in text
        or "variabledebt" in text
        or "debt token" in text
    )


def looks_like_defi_receipt(row: dict[str, str]) -> bool:
    symbol = normalize_symbol(row.get("symbol", ""))
    text = text_blob(row)
    if symbol in STABLECOIN_SYMBOLS and "wrapped" not in text and "crypt" not in text:
        return False
    if symbol in {"WETH", "WBTC", "WFTM", "ETH", "FTM", "MATIC", "BTC"}:
        return False
    padded = f" {text} "
    if any(hint in padded for hint in DEFI_HINTS):
        return True
    return any(symbol.startswith(prefix) for prefix in DEFI_SYMBOL_PREFIXES)


def latest_movements(movements: Iterable[dict[str, str]], direction: str, limit: int = 4) -> list[dict[str, str]]:
    selected = [m for m in movements if m.get("direction") == direction]
    selected.sort(key=lambda m: m.get("timestamp", ""), reverse=True)
    return selected[:limit]


def tx_list(rows: Iterable[dict[str, str]], limit: int = 4) -> str:
    hashes: list[str] = []
    for row in rows:
        tx_hash = row.get("tx_hash", "")
        if tx_hash and tx_hash not in hashes:
            hashes.append(tx_hash)
        if len(hashes) >= limit:
            break
    return ";".join(hashes)


def has_2023_premove_activity(movements: Iterable[dict[str, str]]) -> bool:
    for row in movements:
        timestamp = parse_iso(row.get("timestamp", ""))
        if timestamp and timestamp >= PREMOVE_2023_START:
            return True
    return False


def classify_row(
    row: dict[str, str],
    movements: list[dict[str, str]],
    koinly_2022: dict[str, HoldingEvidence],
    koinly_2020: dict[str, HoldingEvidence],
) -> tuple[str, str, str, str, str, str]:
    symbol = normalize_symbol(row.get("symbol", ""))
    evidence_sym = evidence_symbol(symbol)
    status = "manual_review"
    conservative = "no"
    supportable = "no"
    candidate_layers = ""
    next_action = "manual source review"

    if looks_like_debt_or_exception(row):
        return (
            "E",
            "reconciliation exception / debt / incomplete native flow",
            status,
            conservative,
            supportable,
            "exclude; resolve archive gap only if asset is economically material",
        )

    if looks_like_spam(row):
        return (
            "D",
            "spam, airdrop, or no-basis token",
            "excluded_pending_contrary_proof",
            conservative,
            supportable,
            "exclude unless independent purchase or taxable-income evidence exists",
        )

    if row.get("asset_type") in {"ERC-721", "ERC-1155"}:
        return (
            "D",
            "NFT / non-fungible item, no basis proven",
            "excluded_pending_contrary_proof",
            conservative,
            supportable,
            "exclude unless a purchase invoice or Koinly basis row is found",
        )

    latest_in = latest_movements(movements, "in", 1)
    latest_method = (latest_in[0].get("method", "") if latest_in else "").lower()
    if looks_like_defi_receipt(row):
        return (
            "C",
            "replacement asset / DeFi receipt basis candidate",
            status,
            "no",
            "pending",
            "unwrap protocol position and trace Swedish acquisition/replacement basis of the asset",
        )

    if symbol == "USDC":
        if any(word in latest_method for word in ("remove", "swap", "deposit", "withdraw")):
            return (
                "C",
                "stablecoin received from pre-move DeFi unwind / replacement asset",
                status,
                "no",
                "pending",
                "trace immediate DeFi unwind and prove Swedish acquisition/replacement basis of the predecessor position",
            )
        return (
            "A/B/C",
            "USDC source unresolved: fiat purchase, salary, or replacement asset",
            status,
            "pending",
            "pending",
            "match USDC receipts to fiat purchase, Sweden-taxed salary, or predecessor DeFi position",
        )

    if symbol in STABLECOIN_SYMBOLS:
        return (
            "A/C",
            "stablecoin direct-purchase or replacement basis candidate",
            status,
            "pending",
            "pending",
            "match to Koinly/Swedish stablecoin pool and pre-move swap history",
        )

    has_positive_koinly_pool = any(
        holding and holding.cost_sek > 0
        for holding in (
            koinly_2022.get(evidence_sym),
            koinly_2022.get(symbol),
            koinly_2020.get(evidence_sym),
            koinly_2020.get(symbol),
        )
    )
    if symbol in DIRECT_ASSET_SYMBOLS or has_positive_koinly_pool:
        candidate_layers = "A"
        if symbol != evidence_sym:
            candidate_layers = "A/C"
            next_action = "prove wrap/bridge link from Swedish basis asset to move-date wrapped asset"
        else:
            next_action = "reconcile Swedish 2022 year-end pool through 2023-04-11 disposals and transfers"
        return (
            candidate_layers,
            "direct asset with Koinly/Swedish pool candidate",
            status,
            "pending",
            "pending",
            next_action,
        )

    return (
        "D",
        "unknown token with no cost evidence matched yet",
        "excluded_pending_contrary_proof",
        "no",
        "no",
        "find source transaction and purchase/tax-income evidence or exclude",
    )


def prorata_cost(quantity: Decimal, holding: HoldingEvidence | None) -> Decimal:
    if not holding or holding.quantity <= 0 or holding.cost_sek <= 0 or quantity <= 0:
        return Decimal("0")
    return quantity * holding.cost_sek / holding.quantity


def write_markdown(
    path: Path,
    rows: list[dict[str, str]],
    summary: dict[str, object],
) -> None:
    layer_counts = Counter(row["basis_layer"] for row in rows)
    status_counts = Counter(row["evidence_status"] for row in rows)
    koinly_candidates = [
        row
        for row in rows
        if row["basis_layer"] not in {"D", "E"}
        and parse_decimal(row.get("provisional_2022_eoy_prorata_cost_sek")) > 0
    ]
    koinly_candidates.sort(
        key=lambda row: parse_decimal(row.get("provisional_2022_eoy_prorata_cost_sek")),
        reverse=True,
    )
    review_rows = [
        row
        for row in rows
        if row["basis_layer"] not in {"D", "E"}
        and row["evidence_status"] == "manual_review"
    ]
    review_rows.sort(
        key=lambda row: (
            row["basis_layer"] not in {"A", "A/C"},
            -float(parse_decimal(row.get("provisional_2022_eoy_prorata_cost_sek"))),
            row["chain"],
            row["symbol"],
        )
    )

    lines: list[str] = [
        "# Move-Date Cost Provenance Workpaper",
        "",
        f"Cut-off: `{MOVE_CUTOFF}`",
        "",
        "This is a generated review ledger for imported PIT-38 basis. It is not a filing number.",
        "",
        "## Summary",
        "",
        f"- Inventory rows reviewed: `{summary['row_count']}`",
        f"- Reviewable rows with 2022 Koinly year-end cost-pool match: `{summary['reviewable_koinly_2022_cost_match_rows']}`",
        f"- Provisional 2022 year-end SEK cost cross-check: `{summary['provisional_2022_eoy_prorata_cost_sek']}` SEK",
        f"- Rows requiring 2023 pre-move reconciliation: `{summary['requires_2023_premove_reconciliation_rows']}`",
        "",
        "## Rows By Layer",
        "",
        "| Layer | Rows | Meaning |",
        "| --- | ---: | --- |",
    ]
    meanings = {
        "A": "direct fiat/purchase basis candidate",
        "A/B/C": "stablecoin source unresolved",
        "A/C": "direct or replacement basis candidate",
        "B": "same-token Sweden-taxed salary USDC candidate",
        "C": "replacement asset / DeFi receipt basis candidate",
        "D": "unknown, spam, airdrop, NFT, or no-basis pending proof",
        "E": "reconciliation exception / debt / incomplete native-flow row",
    }
    for layer, count in sorted(layer_counts.items()):
        lines.append(f"| `{layer}` | {count} | {meanings.get(layer, '')} |")

    lines.extend(
        [
            "",
            "## Rows By Evidence Status",
            "",
            "| Status | Rows |",
            "| --- | ---: |",
        ]
    )
    for status, count in sorted(status_counts.items()):
        lines.append(f"| `{status}` | {count} |")

    lines.extend(
        [
            "",
            "## Largest Koinly 2022 Cost-Pool Matches",
            "",
            "These are not final imported PLN costs. They only show where the move-date asset has a 2022 Koinly year-end cost-pool candidate.",
            "",
            "| Layer | Chain | Wallet | Asset | Move qty | Koinly symbol | Provisional SEK cost | 2023 pre-move activity | Next action |",
            "| --- | --- | --- | --- | ---: | --- | ---: | --- | --- |",
        ]
    )
    for row in koinly_candidates[:25]:
        lines.append(
            "| {layer} | {chain} | {wallet} | {asset} | {qty} | {ksym} | {cost} | {activity} | {next_action} |".format(
                layer=row["basis_layer"],
                chain=row["chain"],
                wallet=row["wallet_label"],
                asset=row["symbol"],
                qty=row["move_quantity"],
                ksym=row["koinly_2022_match_symbol"],
                cost=row["provisional_2022_eoy_prorata_cost_sek"],
                activity=row["requires_2023_premove_reconciliation"],
                next_action=row["next_action"],
            )
        )

    lines.extend(
        [
            "",
            "## Manual Review Queue",
            "",
            "| Layer | Chain | Wallet | Asset | Move qty | Last in tx | Next action |",
            "| --- | --- | --- | --- | ---: | --- | --- |",
        ]
    )
    for row in review_rows[:35]:
        lines.append(
            "| {layer} | {chain} | {wallet} | {asset} | {qty} | `{tx}` | {next_action} |".format(
                layer=row["basis_layer"],
                chain=row["chain"],
                wallet=row["wallet_label"],
                asset=row["symbol"],
                qty=row["move_quantity"],
                tx=row["last_in_tx_hashes"].split(";")[0],
                next_action=row["next_action"],
            )
        )

    lines.extend(
        [
            "",
            "## Filing Use",
            "",
            "- Conservative PIT-38 can only use rows whose final `basis_pln` is supported by Layer A evidence and a no-double-counting Swedish basis trace.",
            "- Supportable PIT-38 may add proven salary-USDC rows from `A/B/C` and carefully proven Layer C rows, but those remain KIS-dependent.",
            "- Rows in Layer D or E should not be imported unless the underlying evidence changes.",
            "- `provisional_2022_eoy_prorata_cost_sek` is a triage cross-check, not a filing value; final PLN basis needs transaction-date valuation and NBP translation.",
            "",
        ]
    )

    path.write_text("\n".join(lines), encoding="utf-8")


def build(args: argparse.Namespace) -> None:
    inventory_dir = Path(args.inventory_dir)
    balances_path = inventory_dir / "move-date-token-balances.csv"
    movements_path = inventory_dir / "move-date-movements.csv"
    output_csv = inventory_dir / "move-date-cost-provenance.csv"
    output_json = inventory_dir / "move-date-cost-provenance-summary.json"
    output_md = inventory_dir / "move-date-cost-provenance.md"

    koinly_2022 = load_holdings(Path(args.koinly_2022_eoy))
    koinly_2020 = load_holdings(Path(args.koinly_2020_eoy))
    koinly_2022_tx_hashes = load_koinly_tx_hashes(Path(args.koinly_2022_tx))

    with balances_path.open(encoding="utf-8", newline="") as handle:
        balance_rows = list(csv.DictReader(handle))
    with movements_path.open(encoding="utf-8", newline="") as handle:
        movement_rows = list(csv.DictReader(handle))

    movement_index: dict[tuple[str, str, str, str, str, str], list[dict[str, str]]] = defaultdict(list)
    for movement in movement_rows:
        movement_index[row_key(movement)].append(movement)

    output_rows: list[dict[str, str]] = []
    for row in balance_rows:
        movements = movement_index.get(row_key(row), [])
        symbol = normalize_symbol(row.get("symbol", ""))
        evidence_sym = evidence_symbol(symbol)
        k2022 = koinly_2022.get(evidence_sym) or koinly_2022.get(symbol)
        k2020 = koinly_2020.get(evidence_sym) or koinly_2020.get(symbol)
        amount = parse_decimal(row.get("amount"))
        layer, label, evidence_status, conservative, supportable, next_action = classify_row(
            row, movements, koinly_2022, koinly_2020
        )
        latest_in = latest_movements(movements, "in")
        latest_out = latest_movements(movements, "out")
        koinly_tx_matches = sorted(
            {movement.get("tx_hash", "").lower() for movement in movements}
            & koinly_2022_tx_hashes
        )
        premove_2023 = has_2023_premove_activity(movements)
        prorata_2022 = prorata_cost(amount, k2022)

        notes: list[str] = []
        if symbol != evidence_sym:
            notes.append(f"symbol aliased to {evidence_sym} for Koinly matching")
        if k2022 and k2022.cost_sek > 0:
            notes.append("2022 Koinly year-end cost pool exists; reconcile Jan-Apr 2023 before importing")
        if k2020 and k2020.cost_sek > 0:
            notes.append("2020 Koinly year-end pool also exists")
        if premove_2023:
            notes.append("known 2023 pre-move movements exist")
        if layer in {"D", "E"}:
            notes.append(row.get("basis_status", ""))

        output_rows.append(
            {
                "chain": row.get("chain", ""),
                "wallet_label": row.get("wallet_label", ""),
                "wallet_address": row.get("wallet_address", ""),
                "asset_type": row.get("asset_type", ""),
                "contract_address": row.get("contract_address", ""),
                "token_id": row.get("token_id", ""),
                "symbol": row.get("symbol", ""),
                "name": row.get("name", ""),
                "move_quantity": row.get("amount", ""),
                "basis_layer": layer,
                "basis_layer_label": label,
                "evidence_status": evidence_status,
                "include_conservative": conservative,
                "include_supportable": supportable,
                "final_basis_pln": "",
                "final_basis_currency": "",
                "final_basis_original_amount": "",
                "basis_valuation_date": "",
                "source_type": "",
                "source_document": "",
                "swedish_k4_years": "",
                "swedish_consumption_status": "",
                "koinly_2022_match_symbol": k2022.symbol if k2022 else "",
                "koinly_2022_quantity": fmt_decimal(k2022.quantity) if k2022 else "",
                "koinly_2022_cost_sek": fmt_decimal(k2022.cost_sek) if k2022 else "",
                "provisional_2022_eoy_prorata_cost_sek": fmt_decimal(prorata_2022),
                "koinly_2020_match_symbol": k2020.symbol if k2020 else "",
                "koinly_2020_quantity": fmt_decimal(k2020.quantity) if k2020 else "",
                "koinly_2020_cost_sek": fmt_decimal(k2020.cost_sek) if k2020 else "",
                "movement_count": str(len(movements)),
                "requires_2023_premove_reconciliation": "yes" if premove_2023 else "no",
                "last_in_tx_hashes": tx_list(latest_in),
                "last_out_tx_hashes": tx_list(latest_out),
                "koinly_2022_tx_hash_matches": ";".join(koinly_tx_matches[:8]),
                "next_action": next_action,
                "notes": "; ".join(note for note in notes if note),
            }
        )

    fieldnames = list(output_rows[0].keys()) if output_rows else []
    with output_csv.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(output_rows)

    summary = {
        "cutoff": MOVE_CUTOFF,
        "row_count": len(output_rows),
        "rows_by_layer": dict(sorted(Counter(row["basis_layer"] for row in output_rows).items())),
        "rows_by_evidence_status": dict(
            sorted(Counter(row["evidence_status"] for row in output_rows).items())
        ),
        "rows_by_conservative_inclusion": dict(
            sorted(Counter(row["include_conservative"] for row in output_rows).items())
        ),
        "rows_by_supportable_inclusion": dict(
            sorted(Counter(row["include_supportable"] for row in output_rows).items())
        ),
        "koinly_2022_cost_match_rows": sum(
            1 for row in output_rows if parse_decimal(row["koinly_2022_cost_sek"]) > 0
        ),
        "reviewable_koinly_2022_cost_match_rows": sum(
            1
            for row in output_rows
            if row["basis_layer"] not in {"D", "E"}
            and parse_decimal(row["koinly_2022_cost_sek"]) > 0
        ),
        "requires_2023_premove_reconciliation_rows": sum(
            1 for row in output_rows if row["requires_2023_premove_reconciliation"] == "yes"
        ),
        "provisional_2022_eoy_prorata_cost_sek": fmt_decimal(
            sum(
                (
                    parse_decimal(row["provisional_2022_eoy_prorata_cost_sek"])
                    for row in output_rows
                    if row["basis_layer"] not in {"D", "E"}
                ),
                Decimal("0"),
            )
        ),
        "outputs": {
            "csv": str(output_csv),
            "json": str(output_json),
            "markdown": str(output_md),
        },
    }
    output_json.write_text(json.dumps(summary, indent=2, sort_keys=True), encoding="utf-8")
    write_markdown(output_md, output_rows, summary)

    print(json.dumps(summary, indent=2, sort_keys=True))


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--inventory-dir", default=str(DEFAULT_INVENTORY_DIR))
    parser.add_argument("--koinly-2022-eoy", default=str(DEFAULT_KOINLY_2022_EOY))
    parser.add_argument("--koinly-2020-eoy", default=str(DEFAULT_KOINLY_2020_EOY))
    parser.add_argument("--koinly-2022-tx", default=str(DEFAULT_KOINLY_2022_TX))
    build(parser.parse_args())


if __name__ == "__main__":
    main()
