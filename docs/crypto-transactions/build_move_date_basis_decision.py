#!/usr/bin/env python3
"""Build a move-date imported-basis decision workpaper.

This report sits after ``build_move_date_inventory.py`` and
``build_move_date_cost_provenance.py``. It does not create final PIT-38 filing
values. It answers the narrower question: which move-date positions are strong
enough to focus on, and how far the current evidence is from the minimum
imported-basis threshold needed to keep the split-year PIT-38 chain at zero.
"""

from __future__ import annotations

import argparse
import csv
import json
import sys
from collections import Counter, defaultdict, deque
from dataclasses import dataclass
from datetime import datetime, timezone
from decimal import Decimal, InvalidOperation, ROUND_HALF_UP
from pathlib import Path
from typing import Iterable


REPO_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO_ROOT / "src"))

from tax_calc.nbp import NBPClient  # noqa: E402


DEFAULT_INVENTORY_DIR = REPO_ROOT / "private/evidence/onchain/move-date-inventory-2023-04-12"
DEFAULT_KOINLY_2022_EOY = (
    REPO_ROOT / "private/evidence/koinly/2022/koinly_2022_end_of_year_holdings_report_e7abrLJ2nY_1777113106.csv"
)
MOVE_CUTOFF = datetime(2023, 4, 12, tzinfo=timezone.utc)
MOVE_CUTOFF_TEXT = "2023-04-12T00:00:00Z"
THRESHOLD_PLN = Decimal("134579.93")

GTRAIN_GRAIN_STABLECOIN_SOURCES = [
    {
        "source_chain": "optimism",
        "source_symbol": "USDC",
        "source_amount": Decimal("5996.4"),
        "source_tx_hash": "0xc32bfc5ecdf3c559ec86811c84a887e67d62965ddd16f8b80b98ca34e5e55abb",
        "buy_tx_hash": "0xd31238f19d947764044999d348d2c0892c0497051f3e7d2a78611321b7590916",
        "grain_amount": Decimal("88427.81951728909758089"),
        "date": "2023-04-02",
        "note": "Optimism direct swap into GRAIN used in the 2023-04-10 BPT-GTRAIN join.",
    },
    {
        "source_chain": "arbitrum",
        "source_symbol": "USDC.e",
        "source_amount": Decimal("17415.915677"),
        "source_tx_hash": "0x73d04beb6eab662d2201ec6c492b04518f7599705453873fa8d0bb2ed0a28d2f",
        "buy_tx_hash": "0x73d04beb6eab662d2201ec6c492b04518f7599705453873fa8d0bb2ed0a28d2f",
        "bridge_tx_hash": "0x16685f5022ff7bb83d03c67837ff74fbed4b565f87140e4c71d391f2ad6a70b7",
        "receipt_tx_hash": "0x8a76f322f7bb4f8fc577f9452d02e94ccc8b63376b4fcb427118857914c0b2d4",
        "grain_amount": Decimal("255597.147"),
        "date": "2023-04-02",
        "note": "Arbitrum GRAIN buy bridged to Optimism before the 2023-04-10 BPT-GTRAIN join.",
    },
]

STABLE_USD_SYMBOLS = {
    "BUSD",
    "DAI",
    "DAI+",
    "DOLA",
    "ERN",
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
    "ETH.E": "ETH",
    "FUSDT": "USDT",
    "USDC.E": "USDC",
    "WBTC": "BTC",
    "WETH": "ETH",
    "WFTM": "FTM",
    "WMATIC": "MATIC",
}

TARGETS = [
    {
        "id": "arbitrum_moo_gmx_glp",
        "chain": "arbitrum",
        "wallet_address": "0xb573f01f2901c0db3e14ec80c6e12e4868dec864",
        "contract_address": "0x9dbbbaecacedf53d5caa295b8293c1def2055adc",
        "symbol": "mooGmxGLP",
        "classification": "supportable_candidate_if_usdc_source_proven",
        "decision": "High-priority Layer C candidate. It unwraps to a 2023-03-18 GLP mint funded by 9,985.6 USDC.e, but the USDC.e source still needs a Swedish replacement-basis trace and no-double-counting check.",
    },
    {
        "id": "optimism_rf_soweth",
        "chain": "optimism",
        "wallet_address": "0x8ca0c27a7a868a4069967709b5592995a69ae006",
        "contract_address": "0x932b30b2bc3f00b77affce8d0ff70b536f658462",
        "symbol": "rf-soWETH",
        "classification": "supportable_candidate_if_eth_basis_traced",
        "decision": "Good Layer C candidate. It unwraps directly to WETH deposits and can be tied to the ETH/WETH Koinly cost pool if the Swedish acquisition/replacement-basis trace supports it.",
    },
    {
        "id": "optimism_bpt_gtrain_gauge",
        "chain": "optimism",
        "wallet_address": "0xb573f01f2901c0db3e14ec80c6e12e4868dec864",
        "contract_address": "0xefba6c3d81737bc6641b848345f497268d2807ca",
        "symbol": "BPT-GTRAIN-gauge",
        "classification": "mixed_candidate_count_only_non_debt_parts",
        "decision": "Mixed Layer C candidate. The BPT join used ETH, GRAIN, and ERN. Count the documented non-debt ETH and stablecoin-funded GRAIN inputs by default; quarantine ERN unless adviser/KIS accepts borrowed stablecoin basis.",
    },
    {
        "id": "optimism_bpt_reserve_gauge",
        "chain": "optimism",
        "wallet_address": "0xb573f01f2901c0db3e14ec80c6e12e4868dec864",
        "contract_address": "0xf496794778d49e6ce1af5cdbd3231ee3bd293ec0",
        "symbol": "BPT-RESERVE-gauge",
        "classification": "quarantine_debt_sourced",
        "decision": "Quarantine by default. The visible joins are funded by ERN and appear debt/CDP-sourced, so this should not be used as imported basis without specialist advice.",
    },
    {
        "id": "arbitrum_nead_weth_oath",
        "chain": "arbitrum",
        "wallet_address": "0xb573f01f2901c0db3e14ec80c6e12e4868dec864",
        "contract_address": "0x7e70d4034cd0c6003d2ae8f4594f70135687ce10",
        "symbol": "nead-vrAMM-WETH/OATH",
        "classification": "complex_candidate",
        "decision": "High-value Layer C expansion bucket. The current selected path includes the WETH-linked component plus the distinct DOLA-funded OATH component from the OATH provenance workpaper; OATH-native bridge/reward/TGE buckets remain excluded pending Swedish-source review.",
    },
    {
        "id": "optimism_rf_grain_op",
        "chain": "optimism",
        "wallet_address": "0x8ca0c27a7a868a4069967709b5592995a69ae006",
        "contract_address": "0x229ecbb1d76463e761535dd0e591c34317396131",
        "symbol": "rf-grain-OP",
        "classification": "lower_priority_complex_candidate",
        "decision": "Lower-priority Layer C candidate. It is traceable, but current visible size is not the main threshold driver.",
    },
    {
        "id": "arbitrum_reaper_usdc",
        "chain": "arbitrum",
        "wallet_address": "0x01c1a8d062b29dd2ac3ae49b717c02c99bade52a",
        "contract_address": "0xae321792046a4606ab5965793a61c0a7a703ed7a",
        "symbol": "USDC",
        "classification": "unresolved_stablecoin_source",
        "decision": "Do not treat as clean salary/fiat USDC yet. The receipt appears to come from an Arbitrum DeFi unwind and needs predecessor-LP tracing.",
    },
]


@dataclass
class HoldingEvidence:
    symbol: str
    quantity: Decimal
    cost_sek: Decimal
    source_file: str


@dataclass
class Lot:
    key: tuple[str, str, str, str, str, str]
    amount: Decimal
    timestamp: str
    tx_hash: str
    symbol: str
    row: dict[str, str]


@dataclass
class Consumption:
    tx_hash: str
    timestamp: str
    chain: str
    wallet_address: str
    out_symbol: str
    out_amount: Decimal
    out_direction: str
    source_key: tuple[str, str, str, str, str, str]
    source_symbol: str
    source_amount: Decimal
    source_timestamp: str
    source_tx_hash: str


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


def q2(value: Decimal) -> Decimal:
    return value.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)


def fmt_decimal(value: Decimal | str | None, places: str | None = None) -> str:
    if value is None:
        return ""
    if not isinstance(value, Decimal):
        value = parse_decimal(str(value))
    if places:
        value = value.quantize(Decimal(places), rounding=ROUND_HALF_UP)
    text = format(value.normalize(), "f")
    if "." in text:
        text = text.rstrip("0").rstrip(".")
    return text or "0"


def parse_iso(value: str) -> datetime | None:
    try:
        return datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return None


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def read_csv_after_title(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        return []
    lines = path.read_text(encoding="utf-8-sig", errors="replace").splitlines()
    while lines and not lines[0].startswith("Asset,"):
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
            quantity=parse_decimal(row.get("Quantity")),
            cost_sek=parse_decimal(row.get("Cost (SEK)")),
            source_file=str(path),
        )
    return holdings


def asset_key(row: dict[str, str]) -> tuple[str, str, str, str, str, str]:
    return (
        row.get("chain", ""),
        row.get("wallet_address", "").lower(),
        row.get("asset_type", ""),
        row.get("contract_address", "").lower(),
        row.get("token_id", ""),
        row.get("symbol", ""),
    )


def target_key(target: dict[str, str]) -> tuple[str, str, str, str, str, str]:
    return (
        target["chain"],
        target["wallet_address"].lower(),
        "ERC-20",
        target["contract_address"].lower(),
        "",
        target["symbol"],
    )


def tx_group_key(row: dict[str, str]) -> tuple[str, str, str]:
    return (row.get("chain", ""), row.get("wallet_address", "").lower(), row.get("tx_hash", ""))


def sort_movements(movements: Iterable[dict[str, str]]) -> list[dict[str, str]]:
    indexed = list(enumerate(movements))
    indexed.sort(key=lambda item: (item[1].get("timestamp", ""), item[0]))
    return [item[1] for item in indexed]


def build_fifo(
    movements: list[dict[str, str]],
) -> tuple[
    dict[tuple[str, str, str, str, str, str], deque[Lot]],
    dict[tuple[str, str, str], list[Consumption]],
    dict[tuple[str, str, str], list[dict[str, str]]],
]:
    lots: dict[tuple[str, str, str, str, str, str], deque[Lot]] = defaultdict(deque)
    consumed_by_tx: dict[tuple[str, str, str], list[Consumption]] = defaultdict(list)
    tx_rows: dict[tuple[str, str, str], list[dict[str, str]]] = defaultdict(list)

    for movement in sort_movements(movements):
        timestamp = parse_iso(movement.get("timestamp", ""))
        if timestamp and timestamp >= MOVE_CUTOFF:
            continue
        tx_rows[tx_group_key(movement)].append(movement)

        key = asset_key(movement)
        amount = parse_decimal(movement.get("amount"))
        direction = movement.get("direction", "")
        if direction == "in" and amount > 0:
            lots[key].append(
                Lot(
                    key=key,
                    amount=amount,
                    timestamp=movement.get("timestamp", ""),
                    tx_hash=movement.get("tx_hash", ""),
                    symbol=movement.get("symbol", ""),
                    row=movement,
                )
            )
            continue

        if direction not in {"out", "fee"} or amount >= 0:
            continue

        remaining = -amount
        while remaining > 0 and lots[key]:
            lot = lots[key][0]
            consumed = min(remaining, lot.amount)
            consumed_by_tx[tx_group_key(movement)].append(
                Consumption(
                    tx_hash=movement.get("tx_hash", ""),
                    timestamp=movement.get("timestamp", ""),
                    chain=movement.get("chain", ""),
                    wallet_address=movement.get("wallet_address", "").lower(),
                    out_symbol=movement.get("symbol", ""),
                    out_amount=-amount,
                    out_direction=direction,
                    source_key=lot.key,
                    source_symbol=lot.symbol,
                    source_amount=consumed,
                    source_timestamp=lot.timestamp,
                    source_tx_hash=lot.tx_hash,
                )
            )
            lot.amount -= consumed
            remaining -= consumed
            if lot.amount <= 0:
                lots[key].popleft()

        if remaining > 0:
            consumed_by_tx[tx_group_key(movement)].append(
                Consumption(
                    tx_hash=movement.get("tx_hash", ""),
                    timestamp=movement.get("timestamp", ""),
                    chain=movement.get("chain", ""),
                    wallet_address=movement.get("wallet_address", "").lower(),
                    out_symbol=movement.get("symbol", ""),
                    out_amount=-amount,
                    out_direction=direction,
                    source_key=key,
                    source_symbol=movement.get("symbol", ""),
                    source_amount=remaining,
                    source_timestamp="",
                    source_tx_hash="ARCHIVE_GAP_OR_PREHISTORY",
                )
            )

    return lots, consumed_by_tx, tx_rows


def summarize_tx(rows: list[dict[str, str]]) -> str:
    pieces: list[str] = []
    for row in rows:
        if row.get("direction") == "fee":
            continue
        amount = parse_decimal(row.get("amount"))
        if amount == 0:
            continue
        sign = "+" if amount > 0 else ""
        pieces.append(f"{row.get('symbol', '')} {sign}{fmt_decimal(amount)}")
    return "; ".join(pieces[:12])


def koinly_avg_cost_sek(symbol: str, holdings: dict[str, HoldingEvidence]) -> Decimal:
    holding = holdings.get(evidence_symbol(symbol))
    if not holding or holding.quantity <= 0 or holding.cost_sek <= 0:
        return Decimal("0")
    return holding.cost_sek / holding.quantity


def estimate_source_pln(
    consumption: Consumption,
    holdings: dict[str, HoldingEvidence],
    nbp: NBPClient,
    sek_rate: Decimal,
) -> tuple[Decimal, str, str]:
    symbol = normalize_symbol(consumption.source_symbol)
    amount = abs(consumption.source_amount)
    tx_date = (consumption.timestamp or "")[:10]

    if symbol in STABLE_USD_SYMBOLS and tx_date:
        usd_rate, usd_rate_date = nbp.get_rate_with_date("USD", tx_date)
        if usd_rate:
            return amount * usd_rate, "stablecoin_usd_value_proxy", f"USD NBP {usd_rate} from {usd_rate_date}"

    avg_sek = koinly_avg_cost_sek(symbol, holdings)
    if avg_sek > 0:
        cost_sek = amount * avg_sek
        return cost_sek * sek_rate, "koinly_2022_cost_pool_proxy", f"{fmt_decimal(cost_sek, '0.01')} SEK x SEK/PLN {sek_rate}"

    return Decimal("0"), "unpriced_or_no_cost_pool", "No 2022 Koinly cost-pool match or stablecoin proxy"


def trace_target(
    target: dict[str, str],
    lots: dict[tuple[str, str, str, str, str, str], deque[Lot]],
    consumed_by_tx: dict[tuple[str, str, str], list[Consumption]],
    tx_rows: dict[tuple[str, str, str], list[dict[str, str]]],
    holdings: dict[str, HoldingEvidence],
    nbp: NBPClient,
    sek_rate: Decimal,
    max_depth: int = 4,
) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    key = target_key(target)
    remaining_lots = sorted(
        [lot for lot in lots.get(key, []) if lot.amount > 0],
        key=lambda lot: lot.amount,
        reverse=True,
    )

    def walk(lot: Lot, depth: int, path: set[tuple[str, str, str]]) -> None:
        group_key = (lot.key[0], lot.key[1], lot.tx_hash)
        if depth > max_depth or group_key in path:
            return
        path = set(path)
        path.add(group_key)
        flow = summarize_tx(tx_rows.get(group_key, []))
        consumptions = [
            item
            for item in consumed_by_tx.get(group_key, [])
            if item.out_direction == "out"
            and item.source_tx_hash != item.tx_hash
            and item.source_symbol
        ]
        consumptions.sort(key=lambda item: abs(item.source_amount), reverse=True)

        if not consumptions:
            rows.append(
                {
                    "target_id": target["id"],
                    "target_symbol": target["symbol"],
                    "target_classification": target["classification"],
                    "depth": str(depth),
                    "lot_symbol": lot.symbol,
                    "lot_amount": fmt_decimal(lot.amount),
                    "tx_timestamp": lot.timestamp,
                    "tx_hash": lot.tx_hash,
                    "tx_flow": flow,
                    "source_symbol": "",
                    "source_amount": "",
                    "source_timestamp": "",
                    "source_tx_hash": "",
                    "estimate_pln": "",
                    "estimate_type": "leaf_or_untraced_external_receipt",
                    "estimate_note": "No external predecessor source found in this tx group",
                    "decision": target["decision"],
                }
            )
            return

        for consumption in consumptions[:8]:
            estimate_pln, estimate_type, estimate_note = estimate_source_pln(consumption, holdings, nbp, sek_rate)
            rows.append(
                {
                    "target_id": target["id"],
                    "target_symbol": target["symbol"],
                    "target_classification": target["classification"],
                    "depth": str(depth),
                    "lot_symbol": lot.symbol,
                    "lot_amount": fmt_decimal(lot.amount),
                    "tx_timestamp": lot.timestamp,
                    "tx_hash": lot.tx_hash,
                    "tx_flow": flow,
                    "source_symbol": consumption.source_symbol,
                    "source_amount": fmt_decimal(consumption.source_amount),
                    "source_timestamp": consumption.source_timestamp,
                    "source_tx_hash": consumption.source_tx_hash,
                    "estimate_pln": fmt_decimal(estimate_pln, "0.01") if estimate_pln > 0 else "",
                    "estimate_type": estimate_type,
                    "estimate_note": estimate_note,
                    "decision": target["decision"],
                }
            )
            if consumption.source_tx_hash and consumption.source_tx_hash != "ARCHIVE_GAP_OR_PREHISTORY":
                walk(
                    Lot(
                        key=consumption.source_key,
                        amount=consumption.source_amount,
                        timestamp=consumption.source_timestamp,
                        tx_hash=consumption.source_tx_hash,
                        symbol=consumption.source_symbol,
                        row={},
                    ),
                    depth + 1,
                    path,
                )

    for lot in remaining_lots[:8]:
        walk(lot, 0, set())

    if not rows:
        rows.append(
            {
                "target_id": target["id"],
                "target_symbol": target["symbol"],
                "target_classification": target["classification"],
                "depth": "",
                "lot_symbol": "",
                "lot_amount": "",
                "tx_timestamp": "",
                "tx_hash": "",
                "tx_flow": "",
                "source_symbol": "",
                "source_amount": "",
                "source_timestamp": "",
                "source_tx_hash": "",
                "estimate_pln": "",
                "estimate_type": "no_remaining_lot_found",
                "estimate_note": "Target row not found in remaining FIFO lots",
                "decision": target["decision"],
            }
        )

    return rows


def direct_target_estimates(trace_rows: list[dict[str, str]]) -> dict[str, Decimal]:
    """Return deliberately narrow non-debt estimates for the report summary."""
    totals: dict[str, Decimal] = defaultdict(Decimal)
    for row in trace_rows:
        target_id = row["target_id"]
        symbol = normalize_symbol(row.get("source_symbol", ""))
        depth = row.get("depth", "")
        estimate = parse_decimal(row.get("estimate_pln"))
        if estimate <= 0:
            continue

        if target_id == "arbitrum_moo_gmx_glp" and depth == "1" and symbol in {"USDC", "USDC.E"}:
            totals[target_id] += estimate
        elif target_id == "optimism_rf_soweth" and depth == "0" and symbol in {"ETH", "WETH"}:
            totals[target_id] += estimate
        elif target_id == "optimism_bpt_gtrain_gauge" and depth == "1" and symbol in {"ETH", "WETH"}:
            totals[target_id] += estimate
        elif target_id == "optimism_bpt_reserve_gauge":
            continue
    return totals


def gtrain_grain_stablecoin_basis(nbp: NBPClient) -> tuple[Decimal, list[dict[str, str]]]:
    total = Decimal("0")
    rows: list[dict[str, str]] = []
    for source in GTRAIN_GRAIN_STABLECOIN_SOURCES:
        rate, rate_date = nbp.get_rate_with_date("USD", str(source["date"]))
        if not rate:
            raise RuntimeError(f"Could not fetch USD/PLN NBP rate for {source['date']}")
        source_amount = source["source_amount"]
        estimate = source_amount * rate
        total += estimate
        rows.append(
            {
                "source_chain": str(source["source_chain"]),
                "source_symbol": str(source["source_symbol"]),
                "source_amount": fmt_decimal(source_amount),
                "source_tx_hash": str(source["source_tx_hash"]),
                "buy_tx_hash": str(source["buy_tx_hash"]),
                "bridge_tx_hash": str(source.get("bridge_tx_hash", "")),
                "receipt_tx_hash": str(source.get("receipt_tx_hash", "")),
                "grain_amount": fmt_decimal(source["grain_amount"]),
                "date": str(source["date"]),
                "usd_pln_rate": str(rate),
                "nbp_rate_date": rate_date,
                "estimate_pln": fmt_decimal(estimate, "0.01"),
                "note": str(source["note"]),
            }
        )
    return q2(total), rows


def load_wbtc_rollforward_summary(inventory_dir: Path) -> dict[str, object]:
    summary_path = inventory_dir / "move-date-wbtc-basis-rollforward-summary.json"
    if not summary_path.exists():
        return {}
    try:
        payload = json.loads(summary_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return {}
    return payload if isinstance(payload, dict) else {}


def load_cdp_candidates(
    inventory_dir: Path,
    holdings: dict[str, HoldingEvidence],
    sek_rate: Decimal,
) -> list[dict[str, str]]:
    summary_path = inventory_dir / "move-date-cdp-positions-summary.json"
    if not summary_path.exists():
        return []

    try:
        payload = json.loads(summary_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return []

    rows = payload.get("collaterals", [])
    if not isinstance(rows, list):
        return []

    candidates: list[dict[str, str]] = []
    for row in rows:
        if not isinstance(row, dict):
            continue
        symbol = str(row.get("collateral_symbol") or "")
        if symbol != "WBTC" or str(row.get("move_status")) != "1":
            continue

        collateral_qty = parse_decimal(str(row.get("move_collateral_quantity", "0")))
        debt_ern = parse_decimal(str(row.get("move_debt_ern", "0")))
        avg_sek = koinly_avg_cost_sek("WBTC", holdings)
        avg_cost_sek = collateral_qty * avg_sek if avg_sek > 0 else Decimal("0")
        avg_cost_pln = avg_cost_sek * sek_rate
        rollforward_summary = load_wbtc_rollforward_summary(inventory_dir)
        rollforward_pln = parse_decimal(str(rollforward_summary.get("current_supported_plus_proxy_pln", "")))
        exact_anchor_pln = parse_decimal(str(rollforward_summary.get("exact_koinly_anchor_pln", "")))
        stable_proxy_pln = parse_decimal(str(rollforward_summary.get("stablecoin_proxy_open_pln", "")))
        cost_pln = rollforward_pln if rollforward_pln > 0 else avg_cost_pln

        if exact_anchor_pln > 0:
            candidates.append(
                {
                    "candidate_id": "optimism_ethos_wbtc_exact_koinly_anchors",
                    "candidate_label": "Ethos WBTC exact Koinly anchor subset",
                    "candidate_group": "primary_cdp_collateral_lower_bound",
                    "basis_layer": "C",
                    "quantity": fmt_decimal(collateral_qty),
                    "quantity_symbol": "WBTC",
                    "estimate_pln": fmt_decimal(exact_anchor_pln, "0.01"),
                    "estimate_type": "scaled_exact_koinly_transaction_history_anchors",
                    "estimate_note": "Exact Koinly transaction-history rows from the scaled WBTC basis roll-forward; excludes source-open stablecoin and unresolved legs.",
                    "supportable_status": "partial_lower_bound_pending_final_review",
                    "include_supportable": "pending",
                    "source_workpaper": "move-date-wbtc-basis-rollforward.md",
                    "anti_double_count_note": "Subset of the full WBTC roll-forward. Do not add this on top of the full WBTC candidate.",
                    "filing_note": "Lower-bound scenario only; exact anchors alone do not currently clear the imported-basis threshold.",
                }
            )

        candidates.append(
            {
                "candidate_id": "optimism_ethos_wbtc_trove_collateral",
                "candidate_label": "Ethos WBTC trove collateral",
                "candidate_group": "primary_cdp_collateral",
                "basis_layer": "C",
                "quantity": fmt_decimal(collateral_qty),
                "quantity_symbol": "WBTC",
                "estimate_pln": fmt_decimal(cost_pln, "0.01") if cost_pln > 0 else "",
                "estimate_type": "scaled_koinly_and_stablecoin_rollforward_proxy"
                if rollforward_pln > 0
                else "koinly_2022_btc_cost_pool_proxy",
                "estimate_note": (
                    f"Scaled WBTC roll-forward: {fmt_decimal(exact_anchor_pln, '0.01')} PLN exact Koinly anchors "
                    f"+ {fmt_decimal(stable_proxy_pln, '0.01')} PLN stablecoin source-open proxy; excludes unresolved ETH/anyWETH leg"
                )
                if rollforward_pln > 0
                else (
                    f"{fmt_decimal(avg_cost_sek, '0.01')} SEK x SEK/PLN {sek_rate}; "
                    "WBTC aliased to BTC for Koinly 2022 cost-pool proxy"
                )
                if cost_pln > 0
                else "No Koinly BTC/WBTC cost-pool proxy found",
                "supportable_status": "primary_supportable_pending_stablecoin_source_and_swedish_review"
                if rollforward_pln > 0
                else "primary_supportable_pending_swedish_replacement_basis_trace",
                "include_supportable": "pending",
                "source_workpaper": "move-date-wbtc-basis-rollforward.md"
                if rollforward_pln > 0
                else "move-date-wbtc-cdp-basis-trace.md",
                "anti_double_count_note": (
                    "Count the collateral basis only once. Do not also count ERN-funded BPT/LP/gauge positions "
                    "as separate acquisition cost unless a separate non-debt source is proved."
                ),
                "filing_note": (
                    "Primary candidate only if the exact Koinly anchors and stablecoin source-open legs in the scaled "
                    "roll-forward are accepted, with no double count."
                )
                if rollforward_pln > 0
                else (
                    "Primary candidate if Swedish K4/Koinly evidence ties the traced WBTC/BTC bridge, wrapper, "
                    "and swap path to documented acquisition or replacement basis, with no double count."
                ),
            }
        )
        candidates.append(
            {
                "candidate_id": "optimism_ethos_ern_debt",
                "candidate_label": "Ethos ERN protocol debt",
                "candidate_group": "excluded_debt_proceeds",
                "basis_layer": "excluded",
                "quantity": fmt_decimal(debt_ern),
                "quantity_symbol": "ERN",
                "estimate_pln": "0",
                "estimate_type": "debt_proceeds_not_acquisition_cost",
                "estimate_note": "Borrowed ERN is liability/debt-proceeds state, not out-of-pocket acquisition cost.",
                "supportable_status": "excluded_by_default",
                "include_supportable": "no",
                "source_workpaper": "move-date-cdp-positions.md",
                "anti_double_count_note": "Do not add borrowed ERN and WBTC collateral as two independent cost bases.",
                "filing_note": "Track for liability/economic explanation, not as imported PIT-38 acquisition cost.",
            }
        )

    return candidates


def load_oath_weth_linked_candidate(inventory_dir: Path) -> tuple[Decimal, dict[str, str] | None]:
    summary_path = inventory_dir / "move-date-oath-provenance-summary.json"
    if not summary_path.exists():
        return Decimal("0"), None

    try:
        payload = json.loads(summary_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return Decimal("0"), None
    if not isinstance(payload, dict):
        return Decimal("0"), None

    estimate = q2(parse_decimal(str(payload.get("weth_linked_proxy_pln", ""))))
    quantity = parse_decimal(str(payload.get("weth_linked_total", "")))
    direct_weth = parse_decimal(str(payload.get("direct_weth_input", "")))
    swap_weth = parse_decimal(str(payload.get("weth_from_oath_swaps", "")))
    if estimate <= 0 or quantity <= 0:
        return Decimal("0"), None

    return estimate, {
        "candidate_id": "arbitrum_nead_weth_oath_weth_linked",
        "candidate_label": "WETH/OATH LP WETH-linked component",
        "candidate_group": "independent_non_debt_oath_lp_weth_linked",
        "basis_layer": "C",
        "quantity": fmt_decimal(quantity),
        "quantity_symbol": "WETH-equivalent",
        "estimate_pln": fmt_decimal(estimate, "0.01"),
        "estimate_type": "koinly_2022_eth_cost_pool_proxy",
        "estimate_note": (
            f"Move-date nead-vrAMM-WETH/OATH LP workpaper allocates {fmt_decimal(direct_weth)} direct WETH "
            f"plus {fmt_decimal(swap_weth)} WETH spent into OATH swaps to this WETH-linked component."
        ),
        "supportable_status": "supportable_weth_linked_part_pending_eth_basis_and_no_double_count_review",
        "include_supportable": "pending",
        "source_workpaper": "move-date-oath-provenance.md",
        "anti_double_count_note": (
            "Count only this WETH-linked component. Do not also count the OATH-native bridge/reward/TGE buckets "
            "or the same ETH/WETH basis elsewhere."
        ),
        "filing_note": (
            "Selected as an urgent higher-support expansion bucket because it is tied to ETH/WETH cost evidence; "
            "OATH-native bridge/reward/TGE buckets remain excluded."
        ),
    }


def load_oath_dola_funded_candidate(
    inventory_dir: Path,
    nbp: NBPClient,
) -> tuple[Decimal, dict[str, str] | None]:
    summary_path = inventory_dir / "move-date-oath-provenance-summary.json"
    if not summary_path.exists():
        return Decimal("0"), None

    try:
        payload = json.loads(summary_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return Decimal("0"), None
    if not isinstance(payload, dict):
        return Decimal("0"), None

    quantity = parse_decimal(str(payload.get("dola_from_oath_swaps", "")))
    if quantity <= 0:
        return Decimal("0"), None

    usd_rate, usd_rate_date = nbp.get_rate_with_date("USD", "2023-04-10")
    if not usd_rate:
        return Decimal("0"), None

    estimate = q2(quantity * usd_rate)
    return estimate, {
        "candidate_id": "arbitrum_nead_weth_oath_dola_funded_oath",
        "candidate_label": "WETH/OATH LP DOLA-funded OATH component",
        "candidate_group": "independent_non_debt_oath_lp_dola_funded",
        "basis_layer": "C",
        "quantity": fmt_decimal(quantity),
        "quantity_symbol": "DOLA",
        "estimate_pln": fmt_decimal(estimate, "0.01"),
        "estimate_type": "stablecoin_usd_value_proxy",
        "estimate_note": (
            f"Move-date nead-vrAMM-WETH/OATH LP workpaper allocates {fmt_decimal(quantity)} DOLA "
            f"spent into OATH swaps; valued as a stablecoin source at USD/PLN {usd_rate} from {usd_rate_date}."
        ),
        "supportable_status": "supportable_distinct_dola_branch_pending_cramm_source_review",
        "include_supportable": "pending",
        "source_workpaper": "move-date-oath-provenance.md",
        "anti_double_count_note": (
            "Count only the DOLA spent into OATH swaps. Do not also add the same April 10 DOLA branch spent into WBTC, "
            "or the separate DOLA-to-WETH branch already represented in the WETH-linked LP component."
        ),
        "filing_note": (
            "Selected as a distinct source-open expansion bucket because the DOLA was spent directly into OATH before "
            "the move-date LP; keep the crAMM-FRAX/DOLA predecessor and no-double-counting chain in the evidence file."
        ),
    }


def build_supportable_candidates(
    *,
    base: Decimal,
    cdp_candidates: list[dict[str, str]],
    glp: Decimal,
    rf_soweth: Decimal,
    gtrain_eth: Decimal,
    gtrain_grain: Decimal,
    oath_weth_linked_candidate: dict[str, str] | None,
    oath_dola_funded_candidate: dict[str, str] | None,
) -> list[dict[str, str]]:
    rows = [
        {
            "candidate_id": "reviewable_koinly_matched_rows",
            "candidate_label": "Koinly-matched reviewable move-date rows",
            "candidate_group": "base_reviewable_rows",
            "basis_layer": "A/B/C aggregate",
            "quantity": "",
            "quantity_symbol": "",
            "estimate_pln": fmt_decimal(base, "0.01"),
            "estimate_type": "reviewable_rows_cross_check",
            "estimate_note": "Aggregate of generated provenance rows excluding Layer D/E; still requires row-level final proof.",
            "supportable_status": "supportable_pending_final_row_review",
            "include_supportable": "pending",
            "source_workpaper": "move-date-cost-provenance.md",
            "anti_double_count_note": "Aggregate cross-check only; final filing should use row-level accepted amounts.",
            "filing_note": "Base supportable pool after row-level Swedish replacement-basis trace and final PLN conversion are confirmed.",
        }
    ]
    rows.extend(cdp_candidates)

    rows.extend(
        [
            {
                "candidate_id": "arbitrum_moo_gmx_glp_usdc_e_source",
                "candidate_label": "GLP USDC.e predecessor",
                "candidate_group": "independent_non_debt_backup",
                "basis_layer": "C",
                "quantity": "9985.6",
                "quantity_symbol": "USDC.e",
                "estimate_pln": fmt_decimal(glp, "0.01") if glp > 0 else "",
                "estimate_type": "stablecoin_usd_value_proxy",
                "estimate_note": "Trace shows GLP mint funded by 9,985.6 USDC.e; source/replacement-basis proof still needed.",
                "supportable_status": "supportable_pending_source_proof",
                "include_supportable": "pending",
                "source_workpaper": "move-date-basis-decision.md",
                "anti_double_count_note": "Use only if independent from already-counted CDP debt proceeds and the same Swedish replacement-basis chain.",
                "filing_note": "Backup/additional candidate if USDC.e predecessor is proved.",
            },
            {
                "candidate_id": "optimism_rf_soweth_weth_inputs",
                "candidate_label": "rf-soWETH WETH inputs",
                "candidate_group": "independent_non_debt_backup",
                "basis_layer": "C",
                "quantity": "",
                "quantity_symbol": "WETH",
                "estimate_pln": fmt_decimal(rf_soweth, "0.01") if rf_soweth > 0 else "",
                "estimate_type": "koinly_2022_eth_cost_pool_proxy",
                "estimate_note": "Trace unwraps rf-soWETH to WETH inputs; ETH/WETH Swedish replacement-basis trace still needed.",
                "supportable_status": "supportable_pending_eth_basis_proof",
                "include_supportable": "pending",
                "source_workpaper": "move-date-basis-decision.md",
                "anti_double_count_note": "Use only for the WETH inputs actually represented by the move-date receipt token.",
                "filing_note": "Small backup/additional candidate.",
            },
            {
                "candidate_id": "optimism_bpt_gtrain_eth_only",
                "candidate_label": "BPT-GTRAIN ETH-only input",
                "candidate_group": "independent_non_debt_backup",
                "basis_layer": "C",
                "quantity": "2.835333729957595637",
                "quantity_symbol": "ETH",
                "estimate_pln": fmt_decimal(gtrain_eth, "0.01") if gtrain_eth > 0 else "",
                "estimate_type": "koinly_2022_eth_cost_pool_proxy",
                "estimate_note": "ETH leg only; add stablecoin-funded GRAIN in the separate row. ERN remains excluded/pending.",
                "supportable_status": "mixed_supportable_eth_only",
                "include_supportable": "pending",
                "source_workpaper": "move-date-basis-decision.md",
                "anti_double_count_note": "Do not include ERN/debt-funded BPT-GTRAIN legs in the supportable amount.",
                "filing_note": "Backup/additional candidate if ETH basis can be traced through Swedish acquisition/replacement records.",
            },
            {
                "candidate_id": "optimism_bpt_gtrain_stablecoin_funded_grain",
                "candidate_label": "BPT-GTRAIN stablecoin-funded GRAIN input",
                "candidate_group": "independent_non_debt_backup",
                "basis_layer": "C",
                "quantity": "344024.96651728909758089",
                "quantity_symbol": "GRAIN",
                "estimate_pln": fmt_decimal(gtrain_grain, "0.01") if gtrain_grain > 0 else "",
                "estimate_type": "stablecoin_usd_value_proxy",
                "estimate_note": "GRAIN used in the BPT-GTRAIN join came from 5,996.4 USDC Optimism buy plus 17,415.915677 USDC.e Arbitrum buy bridged to Optimism.",
                "supportable_status": "supportable_non_debt_stablecoin_sources",
                "include_supportable": "pending",
                "source_workpaper": "move-date-gtrain-grain-provenance.md",
                "anti_double_count_note": "Do not also count ERN/debt leg or the same GRAIN cost elsewhere.",
                "filing_note": "Additional candidate because the GRAIN leg is directly tied to stablecoin outflows before the move-date join.",
            },
            {
                "candidate_id": "optimism_bpt_reserve_ern_funded",
                "candidate_label": "BPT-RESERVE ERN-funded position",
                "candidate_group": "excluded_debt_sourced_by_default",
                "basis_layer": "excluded/adviser-only",
                "quantity": "",
                "quantity_symbol": "BPT-RESERVE",
                "estimate_pln": "0",
                "estimate_type": "excluded_debt_sourced_by_default",
                "estimate_note": "The holding was real, but visible joins are ERN/CDP-funded.",
                "supportable_status": "excluded_by_default",
                "include_supportable": "no",
                "source_workpaper": "move-date-unwind-workpaper.md",
                "anti_double_count_note": "Counting this on top of WBTC collateral would likely double-count borrowed ERN proceeds.",
                "filing_note": "Keep documented for adviser/KIS discussion, not in the default supportable pool.",
            },
        ]
    )
    if oath_weth_linked_candidate:
        rows.append(oath_weth_linked_candidate)
    if oath_dola_funded_candidate:
        rows.append(oath_dola_funded_candidate)
    return rows


def write_supportable_candidates_csv(path: Path, rows: list[dict[str, str]]) -> None:
    fieldnames = [
        "candidate_id",
        "candidate_label",
        "candidate_group",
        "basis_layer",
        "quantity",
        "quantity_symbol",
        "estimate_pln",
        "estimate_type",
        "estimate_note",
        "supportable_status",
        "include_supportable",
        "source_workpaper",
        "anti_double_count_note",
        "filing_note",
    ]
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def write_csv(path: Path, rows: list[dict[str, str]]) -> None:
    fieldnames = [
        "target_id",
        "target_symbol",
        "target_classification",
        "depth",
        "lot_symbol",
        "lot_amount",
        "tx_timestamp",
        "tx_hash",
        "tx_flow",
        "source_symbol",
        "source_amount",
        "source_timestamp",
        "source_tx_hash",
        "estimate_pln",
        "estimate_type",
        "estimate_note",
        "decision",
    ]
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)


def display_path(path: Path) -> str:
    try:
        return str(path.relative_to(REPO_ROOT))
    except ValueError:
        return str(path)


def write_markdown(
    path: Path,
    summary: dict[str, object],
    layer_rows: list[dict[str, str]],
    trace_rows: list[dict[str, str]],
) -> None:
    trace_by_target: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in trace_rows:
        trace_by_target[row["target_id"]].append(row)

    cdp_rows: list[dict[str, str]] = []
    cdp_summary_path = path.parent / "move-date-cdp-positions-summary.json"
    if cdp_summary_path.exists():
        try:
            cdp_payload = json.loads(cdp_summary_path.read_text(encoding="utf-8"))
            raw_cdp_rows = cdp_payload.get("collaterals", [])
            if isinstance(raw_cdp_rows, list):
                cdp_rows = [row for row in raw_cdp_rows if isinstance(row, dict)]
        except json.JSONDecodeError:
            cdp_rows = []
    active_cdp_rows = [
        row
        for row in cdp_rows
        if row.get("move_status") == "1" and parse_decimal(str(row.get("move_collateral_quantity", "0"))) != 0
    ]

    lines: list[str] = [
        "# Move-Date Imported Basis Decision Workpaper",
        "",
        f"Cut-off: `{MOVE_CUTOFF_TEXT}`",
        "",
        "This generated workpaper is a decision aid, not a PIT-38 filing attachment and not final tax advice. It quantifies the current evidence gap and highlights the move-date Layer C positions most likely to matter.",
        "",
        "## Threshold Status",
        "",
        f"- Imported-basis threshold needed under the current split-year zero-tax model: `{summary['threshold_pln']}` PLN.",
        f"- Reviewable Koinly 2022 cost-pool cross-check: `{summary['reviewable_koinly_2022_cost_sek']}` SEK.",
        f"- SEK/PLN proxy used for the cross-check: `{summary['sek_rate']}` from NBP table date `{summary['sek_rate_date']}`.",
        f"- Reviewable Koinly cross-check in PLN: `{summary['reviewable_koinly_2022_cost_pln']}` PLN.",
        f"- Gap before tracing additional Layer C positions: `{summary['gap_after_koinly_cross_check_pln']}` PLN.",
        "",
        "Interpretation: direct/Koinly-matched positions alone do not clear the threshold. The filing decision now depends on whether the CDP collateral and specific replacement-asset positions can be tied back to documented pre-residency acquisition basis after any Swedish-taxable transformations, without double counting the same economic cost.",
        "",
        "## Reviewable Cross-Check By Layer",
        "",
        "| Layer | SEK proxy | PLN proxy |",
        "| --- | ---: | ---: |",
    ]

    if active_cdp_rows:
        cdp = active_cdp_rows[0]
        insert_at = lines.index("## Reviewable Cross-Check By Layer")
        lines[insert_at:insert_at] = [
            "Important CDP caveat: `move-date-cdp-positions.md` now shows protocol-state collateral that this token-transfer threshold table did not include.",
            f"The active move-date Ethos trove is `{cdp.get('move_collateral_quantity')} {cdp.get('collateral_symbol')}` with `{cdp.get('move_debt_ern')} ERN` protocol debt. The scenarios below now include that collateral as the primary supportable candidate and keep borrowed ERN/debt-funded positions out by default.",
            "",
        ]

    for row in layer_rows:
        lines.append(f"| `{row['basis_layer']}` | {row['cost_sek']} | {row['cost_pln']} |")

    lines.extend(
        [
            "",
            "## Highest-Impact Layer C Candidates",
            "",
            "| Target | Narrow estimate | Current decision |",
            "| --- | ---: | --- |",
        ]
    )
    target_estimates = summary["target_estimates_pln"]  # type: ignore[index]
    for target in TARGETS:
        estimate = target_estimates.get(target["id"], "") if isinstance(target_estimates, dict) else ""
        lines.append(f"| `{target['symbol']}` | {estimate or ''} | {target['decision']} |")

    supportable_candidates = summary.get("supportable_candidates", [])
    if isinstance(supportable_candidates, list) and supportable_candidates:
        lines.extend(
            [
                "",
                "## Supportable Candidate Ledger",
                "",
                "| Candidate | Group | Estimate | Source workpaper | Supportable status | Filing note |",
                "| --- | --- | ---: | --- | --- | --- |",
            ]
        )
        for candidate in supportable_candidates:
            if not isinstance(candidate, dict):
                continue
            amount = candidate.get("estimate_pln", "")
            if amount and amount != "0":
                amount = f"{amount} PLN"
            lines.append(
                "| {label} | {group} | {amount} | {source} | {status} | {note} |".format(
                    label=candidate.get("candidate_label", ""),
                    group=candidate.get("candidate_group", ""),
                    amount=amount or "",
                    source=candidate.get("source_workpaper", ""),
                    status=candidate.get("supportable_status", ""),
                    note=(candidate.get("filing_note", "") or "").replace("|", "/"),
                )
            )

    lines.extend(
        [
            "",
            "## Threshold Scenarios",
            "",
            "| Scenario | Imported-basis proxy | Gap / surplus vs threshold | Use for filing? |",
            "| --- | ---: | ---: | --- |",
        ]
    )
    for scenario in summary["scenarios"]:  # type: ignore[index]
        lines.append(
            "| {name} | {basis} | {gap} | {use} |".format(
                name=scenario["name"],
                basis=scenario["basis_pln"],
                gap=scenario["gap_or_surplus_pln"],
                use=scenario["filing_use"],
            )
        )

    gtrain_sources = summary.get("gtrain_grain_stablecoin_sources", [])
    if isinstance(gtrain_sources, list) and gtrain_sources:
        lines.extend(
            [
                "",
                "## BPT-GTRAIN GRAIN Stablecoin Sources",
                "",
                f"Total stablecoin-funded GRAIN source included in the no-debt GTRAIN candidate: `{summary.get('gtrain_grain_stablecoin_source_total_pln')}` PLN.",
                "",
                "| Chain | Date | Stablecoin source | GRAIN received / bridged | NBP rate | Estimate | Evidence |",
                "| --- | --- | ---: | ---: | ---: | ---: | --- |",
            ]
        )
        for source in gtrain_sources:
            if not isinstance(source, dict):
                continue
            evidence = f"buy `{source.get('buy_tx_hash', '')}`"
            if source.get("bridge_tx_hash"):
                evidence += f"; bridge `{source.get('bridge_tx_hash')}`; receipt `{source.get('receipt_tx_hash')}`"
            lines.append(
                "| {chain} | {date} | {amount} {symbol} | {grain} GRAIN | {rate} ({rate_date}) | {estimate} PLN | {evidence} |".format(
                    chain=source.get("source_chain", ""),
                    date=source.get("date", ""),
                    amount=source.get("source_amount", ""),
                    symbol=source.get("source_symbol", ""),
                    grain=source.get("grain_amount", ""),
                    rate=source.get("usd_pln_rate", ""),
                    rate_date=source.get("nbp_rate_date", ""),
                    estimate=source.get("estimate_pln", ""),
                    evidence=evidence,
                )
            )

    lines.extend(
        [
            "",
            "## Trace Highlights",
            "",
        ]
    )
    for target in TARGETS:
        rows = trace_by_target.get(target["id"], [])
        lines.extend(
            [
                f"### {target['symbol']}",
                "",
                target["decision"],
                "",
                "| Depth | Tx date | Tx | Flow | External source | Estimate |",
                "| ---: | --- | --- | --- | --- | ---: |",
            ]
        )
        for row in rows[:12]:
            source = ""
            if row.get("source_symbol"):
                source = f"{row['source_symbol']} {row['source_amount']} from `{row['source_tx_hash']}`"
            lines.append(
                "| {depth} | {date} | `{tx}` | {flow} | {source} | {estimate} |".format(
                    depth=row.get("depth", ""),
                    date=(row.get("tx_timestamp", "") or "")[:10],
                    tx=row.get("tx_hash", ""),
                    flow=(row.get("tx_flow", "") or "").replace("|", "/"),
                    source=source.replace("|", "/"),
                    estimate=row.get("estimate_pln", ""),
                )
            )
        lines.append("")

    lines.extend(
        [
            "## Filing Implication",
            "",
            "- Do not use Layer D or E rows as imported basis unless new evidence changes their classification.",
            "- Do not count ERN/debt-sourced LP inputs by default. Treat them as adviser/KIS-only positions.",
            "- The CDP protocol-state workpaper must be handled before final PIT-38 filing inputs. If the Ethos WBTC collateral can be tied to a Swedish K4/Koinly acquisition/replacement-basis trace, it is likely a primary imported-basis candidate.",
            "- The GLP `USDC.e 9,985.6`, `rf-soWETH`, and BPT-GTRAIN ETH plus stablecoin-funded GRAIN traces remain useful backup evidence if the CDP collateral basis is not enough or is not accepted.",
            "- The numbers above are threshold proxies. Final PIT-38 inputs still require transaction-level basis amounts and PLN translation under the selected filing policy.",
            "",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")


def build(args: argparse.Namespace) -> None:
    inventory_dir = Path(args.inventory_dir)
    provenance_path = inventory_dir / "move-date-cost-provenance.csv"
    movements_path = inventory_dir / "move-date-movements.csv"
    trace_csv_path = inventory_dir / "move-date-replacement-traces.csv"
    candidates_csv_path = inventory_dir / "move-date-supportable-basis-candidates.csv"
    summary_json_path = inventory_dir / "move-date-basis-decision-summary.json"
    markdown_path = inventory_dir / "move-date-basis-decision.md"

    provenance_rows = read_csv(provenance_path)
    movement_rows = read_csv(movements_path)
    holdings = load_holdings(Path(args.koinly_2022_eoy))
    nbp = NBPClient(args.nbp_cache)

    sek_rate, sek_rate_date = nbp.get_rate_with_date("SEK", "2023-04-12")
    if not sek_rate:
        raise RuntimeError("Could not fetch SEK/PLN NBP rate for 2023-04-12")

    reviewable_rows = [
        row
        for row in provenance_rows
        if row.get("basis_layer") not in {"D", "E"}
        and parse_decimal(row.get("provisional_2022_eoy_prorata_cost_sek")) > 0
    ]
    by_layer: dict[str, Decimal] = defaultdict(Decimal)
    for row in reviewable_rows:
        by_layer[row.get("basis_layer", "")] += parse_decimal(row.get("provisional_2022_eoy_prorata_cost_sek"))
    total_reviewable_sek = sum(by_layer.values(), Decimal("0"))
    total_reviewable_pln = total_reviewable_sek * sek_rate

    lots, consumed_by_tx, tx_rows = build_fifo(movement_rows)
    trace_rows: list[dict[str, str]] = []
    for target in TARGETS:
        trace_rows.extend(trace_target(target, lots, consumed_by_tx, tx_rows, holdings, nbp, sek_rate))

    target_estimates = direct_target_estimates(trace_rows)
    base = q2(total_reviewable_pln)
    glp = q2(target_estimates.get("arbitrum_moo_gmx_glp", Decimal("0")))
    rf_soweth = q2(target_estimates.get("optimism_rf_soweth", Decimal("0")))
    gtrain_eth = q2(target_estimates.get("optimism_bpt_gtrain_gauge", Decimal("0")))
    gtrain_grain, gtrain_grain_sources = gtrain_grain_stablecoin_basis(nbp)
    target_estimates["optimism_bpt_gtrain_gauge"] = gtrain_eth + gtrain_grain
    cdp_candidates = load_cdp_candidates(inventory_dir, holdings, sek_rate)
    cdp_wbtc = q2(
        sum(
            parse_decimal(row.get("estimate_pln"))
            for row in cdp_candidates
            if row.get("candidate_id") == "optimism_ethos_wbtc_trove_collateral"
        )
    )
    cdp_wbtc_exact = q2(
        sum(
            parse_decimal(row.get("estimate_pln"))
            for row in cdp_candidates
            if row.get("candidate_id") == "optimism_ethos_wbtc_exact_koinly_anchors"
        )
    )
    gtrain_total = q2(gtrain_eth + gtrain_grain)
    max_supportable_no_debt = q2(base + cdp_wbtc + glp + rf_soweth + gtrain_total)
    oath_weth_linked, oath_weth_linked_candidate = load_oath_weth_linked_candidate(inventory_dir)
    oath_dola_funded, oath_dola_funded_candidate = load_oath_dola_funded_candidate(inventory_dir, nbp)
    max_supportable_no_debt_plus_oath_weth = q2(max_supportable_no_debt + oath_weth_linked)
    max_supportable_no_debt_plus_oath_weth_dola = q2(
        max_supportable_no_debt_plus_oath_weth + oath_dola_funded
    )

    scenarios = [
        {
            "name": "Koinly-matched reviewable rows only",
            "basis_pln": fmt_decimal(base, "0.01"),
            "gap_or_surplus_pln": fmt_decimal(base - THRESHOLD_PLN, "0.01"),
            "filing_use": "Not enough; base cross-check only",
        },
        {
            "name": "Add Ethos WBTC exact Koinly anchors only",
            "basis_pln": fmt_decimal(base + cdp_wbtc_exact, "0.01"),
            "gap_or_surplus_pln": fmt_decimal(base + cdp_wbtc_exact - THRESHOLD_PLN, "0.01"),
            "filing_use": "Lower-bound WBTC path; exact anchors alone are not enough",
        },
        {
            "name": "Add Ethos WBTC scaled roll-forward",
            "basis_pln": fmt_decimal(base + cdp_wbtc, "0.01"),
            "gap_or_surplus_pln": fmt_decimal(base + cdp_wbtc - THRESHOLD_PLN, "0.01"),
            "filing_use": "Primary supportable path only if stablecoin source-open legs are accepted",
        },
        {
            "name": "Add Ethos WBTC scaled roll-forward plus GLP USDC.e predecessor",
            "basis_pln": fmt_decimal(base + cdp_wbtc + glp, "0.01"),
            "gap_or_surplus_pln": fmt_decimal(base + cdp_wbtc + glp - THRESHOLD_PLN, "0.01"),
            "filing_use": "Supportable wider path if GLP source proof is also accepted",
        },
        {
            "name": "Max supportable no-debt path",
            "basis_pln": fmt_decimal(max_supportable_no_debt, "0.01"),
            "gap_or_surplus_pln": fmt_decimal(max_supportable_no_debt - THRESHOLD_PLN, "0.01"),
            "filing_use": "Adds WBTC collateral + independent GLP/rf-soWETH/BPT-GTRAIN ETH+stablecoin-funded GRAIN; excludes debt proceeds",
        },
        {
            "name": "Max supportable no-debt path plus WETH-linked WETH/OATH LP",
            "basis_pln": fmt_decimal(max_supportable_no_debt_plus_oath_weth, "0.01"),
            "gap_or_surplus_pln": fmt_decimal(max_supportable_no_debt_plus_oath_weth - THRESHOLD_PLN, "0.01"),
            "filing_use": "Comparison scenario; adds only the WETH-linked OATH LP component and keeps OATH-native/DOLA/debt buckets excluded",
        },
        {
            "name": "Max supportable no-debt path plus WETH-linked and DOLA-funded WETH/OATH LP",
            "basis_pln": fmt_decimal(max_supportable_no_debt_plus_oath_weth_dola, "0.01"),
            "gap_or_surplus_pln": fmt_decimal(
                max_supportable_no_debt_plus_oath_weth_dola - THRESHOLD_PLN,
                "0.01",
            ),
            "filing_use": "Selected urgent expansion; adds WETH-linked and distinct DOLA-funded OATH LP components while keeping OATH-native/debt buckets excluded",
        },
        {
            "name": "Old token-transfer backup path without CDP",
            "basis_pln": fmt_decimal(base + glp + rf_soweth + gtrain_total, "0.01"),
            "gap_or_surplus_pln": fmt_decimal(base + glp + rf_soweth + gtrain_total - THRESHOLD_PLN, "0.01"),
            "filing_use": "Historical comparison only; omitted protocol-state CDP collateral",
        },
    ]
    supportable_candidates = build_supportable_candidates(
        base=base,
        cdp_candidates=cdp_candidates,
        glp=glp,
        rf_soweth=rf_soweth,
        gtrain_eth=gtrain_eth,
        gtrain_grain=gtrain_grain,
        oath_weth_linked_candidate=oath_weth_linked_candidate,
        oath_dola_funded_candidate=oath_dola_funded_candidate,
    )

    layer_rows = [
        {
            "basis_layer": layer,
            "cost_sek": fmt_decimal(cost, "0.01"),
            "cost_pln": fmt_decimal(cost * sek_rate, "0.01"),
        }
        for layer, cost in sorted(by_layer.items())
    ]

    summary = {
        "cutoff": MOVE_CUTOFF_TEXT,
        "threshold_pln": fmt_decimal(THRESHOLD_PLN, "0.01"),
        "sek_rate": str(sek_rate),
        "sek_rate_date": sek_rate_date,
        "reviewable_koinly_2022_cost_sek": fmt_decimal(total_reviewable_sek, "0.01"),
        "reviewable_koinly_2022_cost_pln": fmt_decimal(total_reviewable_pln, "0.01"),
        "gap_after_koinly_cross_check_pln": fmt_decimal(total_reviewable_pln - THRESHOLD_PLN, "0.01"),
        "reviewable_rows_by_layer": dict(Counter(row.get("basis_layer", "") for row in reviewable_rows)),
        "reviewable_cost_by_layer": layer_rows,
        "target_estimates_pln": {key: fmt_decimal(value, "0.01") for key, value in sorted(target_estimates.items())},
        "gtrain_grain_stablecoin_sources": gtrain_grain_sources,
        "gtrain_grain_stablecoin_source_total_pln": fmt_decimal(gtrain_grain, "0.01"),
        "gtrain_total_no_debt_pln": fmt_decimal(gtrain_total, "0.01"),
        "oath_weth_linked_pln": fmt_decimal(oath_weth_linked, "0.01"),
        "oath_dola_funded_pln": fmt_decimal(oath_dola_funded, "0.01"),
        "cdp_estimates_pln": {
            row["candidate_id"]: row["estimate_pln"]
            for row in cdp_candidates
            if row.get("estimate_pln") not in {"", "0"}
        },
        "max_supportable_no_debt_pln": fmt_decimal(max_supportable_no_debt, "0.01"),
        "max_supportable_no_debt_plus_oath_weth_pln": fmt_decimal(
            max_supportable_no_debt_plus_oath_weth,
            "0.01",
        ),
        "max_supportable_no_debt_plus_oath_weth_dola_pln": fmt_decimal(
            max_supportable_no_debt_plus_oath_weth_dola,
            "0.01",
        ),
        "supportable_candidates": supportable_candidates,
        "scenarios": scenarios,
        "outputs": {
            "trace_csv": display_path(trace_csv_path),
            "supportable_candidates_csv": display_path(candidates_csv_path),
            "summary_json": display_path(summary_json_path),
            "markdown": display_path(markdown_path),
        },
    }

    write_csv(trace_csv_path, trace_rows)
    write_supportable_candidates_csv(candidates_csv_path, supportable_candidates)
    summary_json_path.write_text(json.dumps(summary, indent=2, sort_keys=True), encoding="utf-8")
    write_markdown(markdown_path, summary, layer_rows, trace_rows)

    print(f"Wrote {display_path(trace_csv_path)}")
    print(f"Wrote {display_path(candidates_csv_path)}")
    print(f"Wrote {display_path(summary_json_path)}")
    print(f"Wrote {display_path(markdown_path)}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--inventory-dir", default=str(DEFAULT_INVENTORY_DIR))
    parser.add_argument("--koinly-2022-eoy", default=str(DEFAULT_KOINLY_2022_EOY))
    parser.add_argument("--nbp-cache", default=str(REPO_ROOT / "data/nbp_cache.json"))
    return parser.parse_args()


if __name__ == "__main__":
    build(parse_args())
