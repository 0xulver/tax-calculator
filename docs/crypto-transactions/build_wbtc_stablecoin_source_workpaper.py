#!/usr/bin/env python3
"""Build a focused workpaper for WBTC source-open stablecoin rows.

This sits after ``build_wbtc_basis_rollforward.py``. The goal is to make the
remaining filing judgment narrow: which stablecoin replacement-basis rows are
being relied on, what on-chain evidence exists, and what proof remains open.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from collections import defaultdict
from decimal import Decimal
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]
SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO_ROOT / "src"))
sys.path.insert(0, str(SCRIPT_DIR))

import build_move_date_basis_decision as basis  # noqa: E402


DEFAULT_INVENTORY_DIR = REPO_ROOT / "private/evidence/onchain/move-date-inventory-2023-04-12"
MOVE_CUTOFF_TEXT = "2023-04-12T00:00:00Z"
ZERO_ADDRESS = "0x0000000000000000000000000000000000000000"
ADDRESS_RE = re.compile(r"0x[a-fA-F0-9]{40}")
FANTOM_USDC_TX = "0xb67d094cad2b8641086c3218fb7064d93840b82dc21b79da6bc422b57b29a2ca"
WALLET_ADDRESS = "0xb573f01f2901c0db3e14ec80c6e12e4868dec864"
FANTOM_USDC_USER_CONTEXT = (
    "Taxpayer context from 2026-04-25: sender 0xbeb15c... is likely an employer/company/Reaper-related address. "
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


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def fmt(value: Decimal, quantum: str = "0.01") -> str:
    return basis.fmt_decimal(value, quantum)


def norm_hash(value: str | None) -> str:
    return (value or "").strip().lower()


def short_hash(value: str) -> str:
    text = norm_hash(value)
    return text[:10] + "..." if len(text) > 13 else text


def group_by_tx(rows: list[dict[str, str]]) -> dict[str, list[dict[str, str]]]:
    grouped: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        grouped[norm_hash(row.get("tx_hash"))].append(row)
    return grouped


def summarize_flow(rows: list[dict[str, str]]) -> str:
    return basis.summarize_tx(rows).replace("|", "/")


def movement_source_files(rows: list[dict[str, str]]) -> list[str]:
    files = sorted({row.get("source_file", "") for row in rows if row.get("source_file")})
    return [file for file in files if file]


def load_json(path_text: str) -> object | None:
    path = Path(path_text)
    if not path.is_absolute():
        path = REPO_ROOT / path
    if not path.exists():
        return None
    return json.loads(path.read_text(encoding="utf-8", errors="replace"))


def load_known_addresses() -> set[str]:
    files = [
        REPO_ROOT / "docs/crypto-transactions/wallets.txt",
        REPO_ROOT / "private/evidence/wallets/koinly_high_confidence_wallets_new.txt",
        REPO_ROOT / "private/evidence/wallets/koinly_wallets_new.txt",
        REPO_ROOT / "private/evidence/koinly/wallets/koinly-wallets-page-2026-04-25.txt",
    ]
    addresses: set[str] = set()
    for path in files:
        if not path.exists():
            continue
        for match in ADDRESS_RE.finditer(path.read_text(encoding="utf-8", errors="replace")):
            addresses.add(norm_hash(match.group(0)))
    return addresses


def amount_from_raw(raw_value: str | None, decimals: str | None) -> Decimal:
    value = basis.parse_decimal(raw_value)
    scale = basis.parse_decimal(decimals)
    if scale <= 0:
        return value
    return value / (Decimal(10) ** int(scale))


def decode_topic_address(topic: str | None) -> str:
    text = (topic or "").lower()
    if text.startswith("0x") and len(text) == 66:
        return "0x" + text[-40:]
    return ""


def decode_transfer_call(input_text: str | None) -> tuple[str, int] | None:
    text = (input_text or "").lower()
    if not text.startswith("0xa9059cbb") or len(text) < 8 + 64 + 64 + 2:
        return None
    body = text[10:]
    to_address = "0x" + body[24:64]
    amount = int(body[64:128], 16)
    return to_address, amount


def token_parties_from_source_files(tx_hash: str, tx_rows: list[dict[str, str]]) -> list[dict[str, str]]:
    """Extract token transfer parties from the raw files referenced by movements."""
    parties: list[dict[str, str]] = []
    seen: set[tuple[str, str, str, str, str]] = set()

    for source_file in movement_source_files(tx_rows):
        payload = load_json(source_file)
        if payload is None:
            continue

        if isinstance(payload, dict) and isinstance(payload.get("result"), list):
            for item in payload["result"]:
                if not isinstance(item, dict):
                    continue
                item_hash = norm_hash(item.get("hash") or item.get("transactionHash"))
                if item_hash != norm_hash(tx_hash):
                    continue

                # Etherscan-compatible token-transfer rows.
                if item.get("tokenSymbol") or item.get("tokenName"):
                    decimals = item.get("tokenDecimal") or "0"
                    amount = amount_from_raw(item.get("value"), decimals)
                    party = {
                        "source": source_file,
                        "symbol": item.get("tokenSymbol", ""),
                        "amount": fmt(amount, "0.00000001"),
                        "from": norm_hash(item.get("from")),
                        "to": norm_hash(item.get("to")),
                    }
                    key = tuple(party.get(field, "") for field in ("symbol", "amount", "from", "to", "source"))
                    if key not in seen:
                        seen.add(key)
                        parties.append(party)
                    continue

                # Raw Transfer logs from archive_evm_transfer_logs.py.
                topics = item.get("topics")
                if isinstance(topics, list) and len(topics) >= 3:
                    decimals = ""
                    symbol = ""
                    for row in tx_rows:
                        if norm_hash(row.get("contract_address")) == norm_hash(item.get("address")):
                            decimals = row.get("decimals", "")
                            symbol = row.get("symbol", "")
                            break
                    amount = amount_from_raw(item.get("data"), decimals or "0")
                    party = {
                        "source": source_file,
                        "symbol": symbol,
                        "amount": fmt(amount, "0.00000001"),
                        "from": decode_topic_address(topics[1]),
                        "to": decode_topic_address(topics[2]),
                    }
                    key = tuple(party.get(field, "") for field in ("symbol", "amount", "from", "to", "source"))
                    if key not in seen:
                        seen.add(key)
                        parties.append(party)

    return parties


def trace_transfer_parties(tx_hash: str, chain: str) -> list[dict[str, str]]:
    """Extract simple ERC-20 transfer() calls from archived transaction traces."""
    trace_path = REPO_ROOT / f"private/evidence/onchain/raw/rpc-transaction-traces/{chain}/{norm_hash(tx_hash)}.json"
    payload = load_json(str(trace_path))
    if not isinstance(payload, dict):
        return []
    traces = payload.get("traces")
    if not isinstance(traces, list):
        return []

    parties: list[dict[str, str]] = []
    for item in traces:
        if not isinstance(item, dict):
            continue
        action = item.get("action")
        if not isinstance(action, dict):
            continue
        decoded = decode_transfer_call(action.get("input"))
        if decoded is None:
            continue
        to_address, raw_amount = decoded
        parties.append(
            {
                "source": str(trace_path.relative_to(REPO_ROOT)),
                "symbol": "",
                "amount_raw": str(raw_amount),
                "from": norm_hash(action.get("from")),
                "to": norm_hash(to_address),
                "token_contract": norm_hash(action.get("to")),
            }
        )
    return parties


def aggregate_rollforward_stables(rows: list[dict[str, str]]) -> list[dict[str, str]]:
    grouped: dict[tuple[str, str], dict[str, object]] = {}
    for row in rows:
        if row.get("terminal_status") != "stablecoin_usd_value_proxy_source_open":
            continue
        key = (norm_hash(row.get("terminal_tx_hash")), row.get("terminal_symbol", ""))
        if key not in grouped:
            grouped[key] = {
                "terminal_tx_hash": norm_hash(row.get("terminal_tx_hash")),
                "terminal_timestamp": row.get("terminal_timestamp", ""),
                "terminal_symbol": row.get("terminal_symbol", ""),
                "allocated_amount": Decimal("0"),
                "cost_pln": Decimal("0"),
                "root_topups": set(),
                "paths": [],
                "notes": set(),
            }
        bucket = grouped[key]
        bucket["allocated_amount"] = bucket["allocated_amount"] + basis.parse_decimal(row.get("terminal_amount"))  # type: ignore[operator]
        bucket["cost_pln"] = bucket["cost_pln"] + basis.parse_decimal(row.get("cost_pln"))  # type: ignore[operator]
        bucket["root_topups"].add(row.get("root_tx_hash", ""))  # type: ignore[union-attr]
        bucket["paths"].append(row.get("path", ""))  # type: ignore[union-attr]
        if row.get("terminal_note"):
            bucket["notes"].add(row["terminal_note"])  # type: ignore[union-attr]

    output: list[dict[str, str]] = []
    for bucket in grouped.values():
        output.append(
            {
                "terminal_tx_hash": str(bucket["terminal_tx_hash"]),
                "terminal_timestamp": str(bucket["terminal_timestamp"]),
                "terminal_symbol": str(bucket["terminal_symbol"]),
                "allocated_amount": fmt(bucket["allocated_amount"], "0.00000001"),  # type: ignore[arg-type]
                "cost_pln": fmt(bucket["cost_pln"], "0.01"),  # type: ignore[arg-type]
                "root_topups": "; ".join(sorted(bucket["root_topups"])),  # type: ignore[arg-type]
                "path_count": str(len(bucket["paths"])),  # type: ignore[arg-type]
                "notes": "; ".join(sorted(bucket["notes"])),  # type: ignore[arg-type]
            }
        )
    output.sort(key=lambda row: (row["terminal_timestamp"], row["terminal_tx_hash"], row["terminal_symbol"]))
    return output


def trace_stable_sources(trace_rows: list[dict[str, str]]) -> list[dict[str, str]]:
    """Aggregate unscaled stable source rows found in the deeper WBTC trace."""
    grouped: dict[tuple[str, str], dict[str, object]] = {}
    for row in trace_rows:
        if row.get("estimate_type") != "stablecoin_usd_value_proxy":
            continue
        if not norm_hash(row.get("source_tx_hash")).startswith("0x"):
            continue
        key = (norm_hash(row.get("source_tx_hash")), row.get("source_symbol", ""))
        if key not in grouped:
            grouped[key] = {
                "source_tx_hash": norm_hash(row.get("source_tx_hash")),
                "source_timestamp": row.get("source_timestamp", ""),
                "source_symbol": row.get("source_symbol", ""),
                "trace_amount": Decimal("0"),
                "estimate_pln": Decimal("0"),
                "depths": set(),
                "trace_tx_hashes": set(),
            }
        bucket = grouped[key]
        bucket["trace_amount"] = bucket["trace_amount"] + abs(basis.parse_decimal(row.get("source_amount")))  # type: ignore[operator]
        bucket["estimate_pln"] = bucket["estimate_pln"] + basis.parse_decimal(row.get("estimate_pln"))  # type: ignore[operator]
        bucket["depths"].add(row.get("depth", ""))  # type: ignore[union-attr]
        bucket["trace_tx_hashes"].add(row.get("tx_hash", ""))  # type: ignore[union-attr]

    output: list[dict[str, str]] = []
    for bucket in grouped.values():
        output.append(
            {
                "source_tx_hash": str(bucket["source_tx_hash"]),
                "source_timestamp": str(bucket["source_timestamp"]),
                "source_symbol": str(bucket["source_symbol"]),
                "trace_amount": fmt(bucket["trace_amount"], "0.00000001"),  # type: ignore[arg-type]
                "estimate_pln": fmt(bucket["estimate_pln"], "0.01"),  # type: ignore[arg-type]
                "depths": "; ".join(sorted(bucket["depths"])),  # type: ignore[arg-type]
                "trace_tx_hashes": "; ".join(sorted(bucket["trace_tx_hashes"])),  # type: ignore[arg-type]
            }
        )
    output.sort(key=lambda row: (row["source_timestamp"], row["source_tx_hash"], row["source_symbol"]))
    return output


def build_transaction_evidence(
    source_rows: list[dict[str, str]],
    movements_by_tx: dict[str, list[dict[str, str]]],
) -> list[dict[str, str]]:
    output: list[dict[str, str]] = []
    relevant_tx_hashes = sorted(
        {
            tx_hash
            for row in source_rows
            for tx_hash in (row.get("terminal_tx_hash"), row.get("source_tx_hash"))
            if tx_hash and norm_hash(tx_hash).startswith("0x")
        }
    )

    for tx_hash in relevant_tx_hashes:
        tx_rows = movements_by_tx.get(tx_hash, [])
        chains = sorted({row.get("chain", "") for row in tx_rows if row.get("chain")})
        wallet_addresses = {norm_hash(row.get("wallet_address")) for row in tx_rows if row.get("wallet_address")}
        token_parties = token_parties_from_source_files(tx_hash, tx_rows)
        trace_parties: list[dict[str, str]] = []
        for chain in chains:
            trace_parties.extend(
                party
                for party in trace_transfer_parties(tx_hash, chain)
                if party.get("from") in wallet_addresses or party.get("to") in wallet_addresses
            )

        party_bits: list[str] = []
        for party in token_parties:
            symbol = party.get("symbol") or "token"
            party_bits.append(
                f"{party.get('amount', '')} {symbol}: {party.get('from', '')} -> {party.get('to', '')}"
            )
        for party in trace_parties:
            party_bits.append(
                "trace transfer call: {amount_raw} raw units from {from_addr} to {to_addr} via {token}".format(
                    amount_raw=party.get("amount_raw", ""),
                    from_addr=party.get("from", ""),
                    to_addr=party.get("to", ""),
                    token=party.get("token_contract", ""),
                )
            )

        output.append(
            {
                "tx_hash": tx_hash,
                "timestamp": min((row.get("timestamp", "") for row in tx_rows if row.get("timestamp")), default=""),
                "chain": "; ".join(chains),
                "flow": summarize_flow(tx_rows) if tx_rows else "",
                "movement_count": str(len(tx_rows)),
                "raw_parties": " | ".join(party_bits),
                "source_files": "; ".join(movement_source_files(tx_rows)),
            }
        )
    return output


def inbound_sender(tx_rows: list[dict[str, str]], tx_hash: str, wallet_address: str) -> str:
    for row in tx_rows:
        if row.get("tx_hash") != tx_hash:
            continue
        for match in re.finditer(r"from (0x[a-f0-9]{40}) to (0x[a-f0-9]{40})", row.get("raw_parties", "")):
            source, target = match.groups()
            if norm_hash(target) == norm_hash(wallet_address) and norm_hash(source) != ZERO_ADDRESS:
                return norm_hash(source)
    return ""


def write_csv(path: Path, rows: list[dict[str, str]], fieldnames: list[str]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def write_markdown(
    path: Path,
    *,
    rollforward_rows: list[dict[str, str]],
    trace_rows: list[dict[str, str]],
    tx_rows: list[dict[str, str]],
    summary: dict[str, object],
) -> None:
    lines = [
        "# WBTC Stablecoin Source-Open Workpaper",
        "",
        f"Cut-off: `{MOVE_CUTOFF_TEXT}`",
        "",
        "This generated workpaper isolates the stablecoin source-open rows inside the Ethos WBTC collateral roll-forward. It is a review aid for the imported-basis decision, not a final PIT-38 attachment.",
        "",
        "## Current Finding",
        "",
        f"- Roll-forward stablecoin source-open value: `{summary['rollforward_source_open_pln']} PLN`.",
        f"- Roll-forward source-open terminal transactions: `{summary['rollforward_terminal_tx_count']}`.",
        f"- The Fantom USDC terminal row contributes `{summary['fantom_usdc_pln']} PLN` and is backed by an inbound USDC transfer from an external contract/address.",
        f"- The Arbitrum DOLA terminal row contributes `{summary['arbitrum_dola_pln']} PLN` and comes from pre-move removal of the `crAMM-FRAX/DOLA` LP position.",
        f"- Fantom USDC sender `{summary['fantom_usdc_source_address'] or 'unknown'}` known-wallet check: `{summary['fantom_usdc_source_known_wallet']}`.",
        f"- User context to verify: {summary['fantom_usdc_user_context']}",
        "",
        "Interpretation: the WBTC path clears the PIT-38 threshold only if these source-open stablecoin rows are accepted as pre-residency replacement basis. The stronger position is to support them with Swedish/Koinly evidence or a self-calculated Swedish-style pre-move disposal trail. The exact Koinly anchors alone are still short.",
        "",
        "For the Fantom USDC row, the direct Reaper hack/recovery event is now supported by the related local workpapers. The Reaper-to-WBTC link workpaper directly ties the August 18 DAI and BTC recovery rows into the WBTC predecessor trace, and forward tracing adds provenance links for August 18 USDC and ETH into the Arbitrum DOLA/source-open branch. Those forward links are not additive filing amounts. The March 2023 USDC transfer remains a separate compensation/source-open leg. Remaining useful evidence is final Swedish tax/K4 treatment of the original stablecoin sale, vault loss, and recovery chain. A Reaper UI/export, claim page, Discord/support record, or allocation record would be helpful if available, but the local on-chain recovery rows are now the core taxpayer-specific repayment evidence.",
        "",
        "Related local workpapers: `move-date-reaper-multistrategy-hack-thread.md` isolates the Reaper multi-strategy vault loss/compensation path behind this Fantom USDC row, and `move-date-wbtc-reaper-recovery-link.md` identifies which recovery assets are visible in the WBTC path.",
        "",
        "External Reaper incident references to archive with the evidence packet:",
        *[f"- {reference}" for reference in REAPER_INCIDENT_REFERENCES],
        "",
        "## Roll-Forward Rows In Filing Scope",
        "",
        "| Terminal tx | Date | Symbol | Allocated amount | Cost PLN | Root top-ups | Notes |",
        "| --- | --- | --- | ---: | ---: | --- | --- |",
    ]
    for row in rollforward_rows:
        lines.append(
            "| `{tx}` | {date} | {symbol} | {amount} | {cost} | {roots} | {notes} |".format(
                tx=row["terminal_tx_hash"],
                date=row["terminal_timestamp"][:10],
                symbol=row["terminal_symbol"],
                amount=row["allocated_amount"],
                cost=row["cost_pln"],
                roots=", ".join(short_hash(item) for item in row["root_topups"].split("; ") if item),
                notes=row["notes"].replace("|", "/"),
            )
        )

    lines.extend(
        [
            "",
            "## On-Chain Evidence For Those Transactions",
            "",
            "| Tx | Chain | Flow | Raw parties / trace |",
            "| --- | --- | --- | --- |",
        ]
    )
    for row in tx_rows:
        lines.append(
            "| `{tx}` | {chain} | {flow} | {parties} |".format(
                tx=row["tx_hash"],
                chain=row["chain"],
                flow=row["flow"].replace("|", "/"),
                parties=(row["raw_parties"] or "").replace("|", "/"),
            )
        )

    lines.extend(
        [
            "",
            "## Deeper Stablecoin Receipts In The WBTC Trace",
            "",
            "These rows are from the unscaled evidence trace, so they are source-trail context rather than additive filing values. They matter mainly if the DOLA replacement-basis shortcut is rejected and the LP path must be traced deeper.",
            "",
            "| Source tx | Date | Symbol | Trace amount | Unscaled estimate PLN | Depths |",
            "| --- | --- | --- | ---: | ---: | --- |",
        ]
    )
    for row in trace_rows:
        lines.append(
            "| `{tx}` | {date} | {symbol} | {amount} | {pln} | {depths} |".format(
                tx=row["source_tx_hash"],
                date=row["source_timestamp"][:10],
                symbol=row["source_symbol"],
                amount=row["trace_amount"],
                pln=row["estimate_pln"],
                depths=row["depths"],
            )
        )

    lines.extend(
        [
            "",
            "## Filing Use",
            "",
            "- If using the full WBTC roll-forward, attach or retain this workpaper with `move-date-wbtc-basis-rollforward.md`.",
            "- Do not add the deeper stablecoin receipt rows to the roll-forward totals. They are fallback provenance context.",
            "- The open proof question is narrow: whether the March-April 2023 stablecoin receipts and LP removal can be treated as pre-residency replacement basis without a paid 2023 Koinly export.",
            "- The remaining unresolved ETH/anyWETH top-up is still excluded from the current WBTC basis number.",
            "",
            "## Outputs",
            "",
            "- Roll-forward CSV: `move-date-wbtc-stablecoin-source-open-rollforward.csv`",
            "- Deeper trace CSV: `move-date-wbtc-stablecoin-source-open-trace.csv`",
            "- Transaction evidence CSV: `move-date-wbtc-stablecoin-source-open-transactions.csv`",
            "- JSON summary: `move-date-wbtc-stablecoin-source-open-summary.json`",
            "",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")


def build(args: argparse.Namespace) -> None:
    inventory_dir = Path(args.inventory_dir)
    rollforward_path = inventory_dir / "move-date-wbtc-basis-rollforward.csv"
    trace_path = inventory_dir / "move-date-wbtc-cdp-basis-trace.csv"
    movements_path = inventory_dir / "move-date-movements.csv"

    rollforward_stables = aggregate_rollforward_stables(read_csv(rollforward_path))
    deeper_stables = trace_stable_sources(read_csv(trace_path))
    movements_by_tx = group_by_tx(read_csv(movements_path))

    relevant_trace_rows = [
        row
        for row in deeper_stables
        if row["source_tx_hash"] not in {item["terminal_tx_hash"] for item in rollforward_stables}
    ]
    tx_evidence = build_transaction_evidence(rollforward_stables + relevant_trace_rows, movements_by_tx)
    known_addresses = load_known_addresses()
    fantom_usdc_source = inbound_sender(tx_evidence, FANTOM_USDC_TX, WALLET_ADDRESS)

    total_pln = sum((basis.parse_decimal(row.get("cost_pln")) for row in rollforward_stables), Decimal("0"))
    fantom_usdc_pln = sum(
        (
            basis.parse_decimal(row.get("cost_pln"))
            for row in rollforward_stables
            if row.get("terminal_tx_hash") == "0xb67d094cad2b8641086c3218fb7064d93840b82dc21b79da6bc422b57b29a2ca"
        ),
        Decimal("0"),
    )
    arbitrum_dola_pln = sum(
        (
            basis.parse_decimal(row.get("cost_pln"))
            for row in rollforward_stables
            if row.get("terminal_tx_hash") == "0xecf9f6eb5bca8a5a1f3263676912f6cbe65d48569074385424ebc00967e59557"
        ),
        Decimal("0"),
    )
    summary = {
        "cutoff": MOVE_CUTOFF_TEXT,
        "rollforward_source_open_pln": fmt(total_pln),
        "rollforward_terminal_tx_count": len(rollforward_stables),
        "deeper_stable_source_tx_count": len(relevant_trace_rows),
        "fantom_usdc_pln": fmt(fantom_usdc_pln),
        "fantom_usdc_source_address": fantom_usdc_source,
        "fantom_usdc_source_known_wallet": "yes" if fantom_usdc_source in known_addresses else "no",
        "fantom_usdc_user_context": FANTOM_USDC_USER_CONTEXT,
        "arbitrum_dola_pln": fmt(arbitrum_dola_pln),
    }

    write_csv(
        inventory_dir / "move-date-wbtc-stablecoin-source-open-rollforward.csv",
        rollforward_stables,
        ["terminal_tx_hash", "terminal_timestamp", "terminal_symbol", "allocated_amount", "cost_pln", "root_topups", "path_count", "notes"],
    )
    write_csv(
        inventory_dir / "move-date-wbtc-stablecoin-source-open-trace.csv",
        relevant_trace_rows,
        ["source_tx_hash", "source_timestamp", "source_symbol", "trace_amount", "estimate_pln", "depths", "trace_tx_hashes"],
    )
    write_csv(
        inventory_dir / "move-date-wbtc-stablecoin-source-open-transactions.csv",
        tx_evidence,
        ["tx_hash", "timestamp", "chain", "flow", "movement_count", "raw_parties", "source_files"],
    )
    (inventory_dir / "move-date-wbtc-stablecoin-source-open-summary.json").write_text(
        json.dumps(summary, indent=2, sort_keys=True),
        encoding="utf-8",
    )
    write_markdown(
        inventory_dir / "move-date-wbtc-stablecoin-source-open.md",
        rollforward_rows=rollforward_stables,
        trace_rows=relevant_trace_rows,
        tx_rows=tx_evidence,
        summary=summary,
    )

    print(json.dumps(summary, indent=2, sort_keys=True))


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--inventory-dir", default=str(DEFAULT_INVENTORY_DIR))
    build(parser.parse_args())


if __name__ == "__main__":
    main()
