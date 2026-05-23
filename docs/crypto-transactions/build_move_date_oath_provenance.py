#!/usr/bin/env python3
"""Build the move-date OATH/WETH LP provenance workpaper.

This is a targeted follow-up to the move-date inventory. It traces the
``nead-vrAMM-WETH/OATH`` receipt held on 2023-04-12 back to the immediate
``vrAMM-WETH/OATH`` LP mints, then classifies the OATH inputs by visible source
bucket.

The output is an evidence workpaper, not a final PIT-38 value. It separates the
real asset/value question from the harder legal question: which OATH/WETH input
costs are importable as pre-residency Polish PIT-38 basis.
"""

from __future__ import annotations

import argparse
import csv
import json
from collections import defaultdict, deque
from dataclasses import dataclass
from datetime import datetime, timezone
from decimal import Decimal, InvalidOperation, ROUND_HALF_UP
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_INVENTORY_DIR = REPO_ROOT / "private/evidence/onchain/move-date-inventory-2023-04-12"
DEFAULT_KOINLY_2022_TX = (
    REPO_ROOT / "private/evidence/koinly/2022/koinly_2022_transaction_history_krYwagtox4_1777112970.csv"
)
DEFAULT_KOINLY_2022_INCOME = (
    REPO_ROOT / "private/evidence/koinly/2022/koinly_2022_income_report_mn8SY4MFM9_1777113144.csv"
)
DEFAULT_KOINLY_2022_EOY = (
    REPO_ROOT / "private/evidence/koinly/2022/koinly_2022_end_of_year_holdings_report_e7abrLJ2nY_1777113106.csv"
)

MOVE_CUTOFF = datetime(2023, 4, 12, tzinfo=timezone.utc)
MOVE_CUTOFF_TEXT = "2023-04-12T00:00:00Z"
WALLET = "0xb573f01f2901c0db3e14ec80c6e12e4868dec864"
CHAIN = "arbitrum"

# Valuation proxies used only to size the position. Basis must come from the
# actual source buckets, not from a move-date fair-market-value step-up.
ETH_USD_2023_04_12 = Decimal("1892.69")
OATH_USD_USER_2023_04_12 = Decimal("0.2036")
USD_PLN_2023_04_12 = Decimal("4.2713")

# From move-date-basis-decision.md: 13.677446 WETH -> 125,248.69 PLN.
WETH_PROXY_PLN_PER_WETH = Decimal("125248.69") / Decimal("13.677446")

AVALANCHE_BIG_BRIDGE_TRACE = [
    {
        "timestamp": "2023-03-31T16:34:01Z",
        "chain": "avalanche",
        "tx_hash": "0x0dd832c6d3440386b57bbb89370d406e3ca3d4aa60a14306b02144a5130411ba",
        "flow": "OATH +50832.2169",
        "note": "Avalanche anySwapInAuto from Ethereum chainID 1, source tx 0xe29b11ea1717d1163cc3cd3bc4c5ea64aff0a9b308fe226f58298534e2a131bb.",
    },
    {
        "timestamp": "2023-04-06T22:35:42Z",
        "chain": "avalanche",
        "tx_hash": "0x55deed10897c6aa323537350a2db37affe6d5f06b94a4d083989c447c2bd9408",
        "flow": "OATH +55326.1185",
        "note": "Avalanche anySwapInAuto from Arbitrum chainID 42161, source tx 0x38a74ae875fc95951fc1aa4fafb4cd7c018912dbe2b5d192fdc218e1adb27fea.",
    },
    {
        "timestamp": "2023-04-06T22:53:42Z",
        "chain": "avalanche",
        "tx_hash": "0xd873e4d0af3189aa42ce71e4770ed14e0ce9136d2d10697bd4cffcd9df18a9e9",
        "flow": "OATH -55210.307972558138831081; WETH.e -6.944090877608349585; vAMM-OATH/WETH.e +619.181230288990992974",
        "note": "Adds the second large OATH bridge receipt into Avalanche OATH/WETH.e LP.",
    },
    {
        "timestamp": "2023-04-07T22:16:46Z",
        "chain": "avalanche",
        "tx_hash": "0x2ac9236cdff2d19f42384b09de5ec805e606432bd1e84ee8ae285a78fd14cad2",
        "flow": "vAMM-OATH/WETH.e -1241.934930584579298112; OATH +110374.466585288208452027; WETH.e +13.974267958199223167",
        "note": "Unwinds the Avalanche OATH/WETH.e LP immediately before the large bridge back to Arbitrum.",
    },
    {
        "timestamp": "2023-04-07T22:20:35Z",
        "chain": "avalanche",
        "tx_hash": "0x2438125ab490e737bdf56352da494c5d1539920c05f880f0c7ceac4c60906488",
        "flow": "OATH -110490",
        "note": "Avalanche anySwapOut to Arbitrum chainID 42161; this is the source tx embedded in the Arbitrum receipt 0xd45ce2727020117542372c73deb3879d073125380708981a4c378975ae5eb877.",
    },
    {
        "timestamp": "2023-04-07T22:22:21Z",
        "chain": "arbitrum",
        "tx_hash": "0xd45ce2727020117542372c73deb3879d073125380708981a4c378975ae5eb877",
        "flow": "OATH +110379.51",
        "note": "Arbitrum anySwapInAuto from Avalanche chainID 43114, source tx 0x2438125ab490e737bdf56352da494c5d1539920c05f880f0c7ceac4c60906488.",
    },
]

FANTOM_ORIGIN_TRACE = [
    {
        "route": "large_march16_fantom_to_arbitrum",
        "timestamp": "2023-03-16T15:21:39Z",
        "chain": "fantom",
        "tx_hash": "0x8e1b489c02f3f7ea1b2ef33ee271c079e5205cfa2934e72e5ceb790dfe2b1c64",
        "flow": "Reaper OATH -48000",
        "note": "Reaper/vesting OATH bridged out of Fantom to Arbitrum.",
    },
    {
        "route": "large_march16_fantom_to_arbitrum",
        "timestamp": "2023-03-16T15:22:07Z",
        "chain": "arbitrum",
        "tx_hash": "0x26ca6d38b00cf28157d55cd27a61597ec9b461a9f9e3ae8faed7de7a48b814ae",
        "flow": "Reaper OATH +47877.70576",
        "note": "Arbitrum receipt from the Fantom bridge-out.",
    },
    {
        "route": "large_march16_fantom_to_arbitrum",
        "timestamp": "2023-03-16T15:28:42Z",
        "chain": "arbitrum",
        "tx_hash": "0x8ba9c51006f2d730e55a40f77f6a775f4866778e42e996021a7548013796a53d",
        "flow": "Reaper OATH -47877.70576; Metamask3 OATH +47877.70576",
        "note": "Internal transfer from the Reaper wallet to Metamask3 before Arbitrum LP farming.",
    },
    {
        "route": "large_march16_fantom_to_arbitrum",
        "timestamp": "2023-03-16T15:36:35Z to 2023-03-18T13:01:04Z",
        "chain": "arbitrum",
        "tx_hash": "MULTIPLE",
        "flow": "OATH -46214.535833415366303507 into WETH/OATH LPs",
        "note": "Most of the March 16 Fantom bridge receipt was added to Arbitrum WETH/OATH LP positions.",
    },
    {
        "route": "large_march18_fantom_to_arbitrum",
        "timestamp": "2023-03-18T19:33:22Z",
        "chain": "fantom",
        "tx_hash": "0xeb381345564aaeefdc54154ff16b4dcfc4c008edce3e69dc1eb7594270394946",
        "flow": "Reaper OATH -35333.3333333332; Metamask3 OATH +35333.3333333332",
        "note": "Another Reaper/vesting OATH transfer to Metamask3 on Fantom.",
    },
    {
        "route": "large_march18_fantom_to_arbitrum",
        "timestamp": "2023-03-18T19:42:19Z",
        "chain": "fantom",
        "tx_hash": "0x4dc8c0c80bab837cae6b65a25bb9bc9dd487f7d3321bae0e3420a27415987465",
        "flow": "Metamask3 OATH -42319.4",
        "note": "Metamask3 bridges OATH out of Fantom to Arbitrum.",
    },
    {
        "route": "large_march18_fantom_to_arbitrum",
        "timestamp": "2023-03-18T19:42:42Z",
        "chain": "arbitrum",
        "tx_hash": "0x0be1b89b730ef8d88dc293eb594d921538a61e3ffcabc2f27536cf7ca146082c",
        "flow": "Metamask3 OATH +42197.10576",
        "note": "Arbitrum receipt from the Fantom bridge-out.",
    },
    {
        "route": "large_march18_fantom_to_arbitrum",
        "timestamp": "2023-03-18T19:52:43Z",
        "chain": "arbitrum",
        "tx_hash": "0xb9e3f0c9ca7152fdc247b630f315d1b084ce440e5d899e8fb7c897eb8a722f8e",
        "flow": "OATH -43860.275686584633696493 into WETH/OATH LP",
        "note": "This LP input equals the 42197.10576 Arbitrum bridge receipt plus 1663.169926584633696493 OATH left from the March 16 bridge receipt.",
    },
    {
        "route": "large_pooled_lp_to_avalanche",
        "timestamp": "2023-03-19T06:56:04Z to 2023-03-31T15:51:32Z",
        "chain": "arbitrum",
        "tx_hash": "MULTIPLE",
        "flow": "Small OATH swap/farming additions into the same WETH/OATH LP family",
        "note": "The later 1220.411022298644920249 LP withdrawal includes the March Fantom-sourced OATH plus smaller pre-move Arbitrum swap/farming additions.",
    },
    {
        "route": "large_pooled_lp_to_avalanche",
        "timestamp": "2023-03-31T16:07:15Z",
        "chain": "arbitrum",
        "tx_hash": "0x2d227a3419ba7aa817dc1ef920ec63876d36b4af673a5447d5cfef76a3f1b6d8",
        "flow": "vrAMM-WETH/OATH +1220.411022298644920249",
        "note": "Withdraws the accumulated March 16-31 Arbitrum WETH/OATH LP position.",
    },
    {
        "route": "large_pooled_lp_to_avalanche",
        "timestamp": "2023-03-31T16:08:04Z",
        "chain": "arbitrum",
        "tx_hash": "0x20ebf770ccb227b3d54a4febfa2592302826465f6f12c6466839925ab58ad324",
        "flow": "vrAMM-WETH/OATH -610.205511149322460125; OATH +51011.139246238993478277; WETH +7.30105672368520572",
        "note": "Unwinds half of the pooled LP; this OATH is then bridged toward Avalanche.",
    },
    {
        "route": "large_pooled_lp_to_avalanche",
        "timestamp": "2023-03-31T16:11:55Z",
        "chain": "arbitrum",
        "tx_hash": "0x5ef37766a149f33e26e265ffa0dae5a76e713d35f13bb3ecc02df4844b7f0e98",
        "flow": "OATH -51011.8",
        "note": "Bridges the first large pooled LP unwind branch from Arbitrum to Ethereum.",
    },
    {
        "route": "large_pooled_lp_to_avalanche",
        "timestamp": "2023-03-31T16:25:35Z",
        "chain": "ethereum",
        "tx_hash": "0x82eec4c67e50bacd80395554be85a15faaad42dbe3e6dff2cdbe4ab207962dbb",
        "flow": "OATH +50883.182637",
        "note": "Ethereum receipt from the Arbitrum bridge-out.",
    },
    {
        "route": "large_pooled_lp_to_avalanche",
        "timestamp": "2023-03-31T16:30:47Z",
        "chain": "ethereum",
        "tx_hash": "0xe29b11ea1717d1163cc3cd3bc4c5ea64aff0a9b308fe226f58298534e2a131bb",
        "flow": "OATH -50883.1",
        "note": "Bridges the first large branch from Ethereum to Avalanche.",
    },
    {
        "route": "large_pooled_lp_to_avalanche",
        "timestamp": "2023-03-31T16:34:01Z",
        "chain": "avalanche",
        "tx_hash": "0x0dd832c6d3440386b57bbb89370d406e3ca3d4aa60a14306b02144a5130411ba",
        "flow": "OATH +50832.2169",
        "note": "Avalanche receipt from Ethereum.",
    },
    {
        "route": "large_second_lp_branch_to_avalanche",
        "timestamp": "2023-04-06T22:13:57Z",
        "chain": "arbitrum",
        "tx_hash": "0xe208c15776b9ef96c1b7e4cf2aeb7d8be2eddb8d87d809296ca8049759cc5083",
        "flow": "vrAMM-WETH/OATH +615.406918038356559644",
        "note": "Withdraws the remaining March pooled LP half plus small April 1/4 LP additions.",
    },
    {
        "route": "large_second_lp_branch_to_avalanche",
        "timestamp": "2023-04-06T22:14:32Z",
        "chain": "arbitrum",
        "tx_hash": "0xcf7b994b374ca7f2945ac07769ed60e20d1e63e1b121c57ae188f87b7b6a09fb",
        "flow": "vrAMM-WETH/OATH -615.406918038356559644; OATH +55381.544787984097001435; WETH +6.840037285387213317",
        "note": "Unwinds the second large pooled LP branch before bridging to Avalanche.",
    },
    {
        "route": "large_second_lp_branch_to_avalanche",
        "timestamp": "2023-04-06T22:22:24Z",
        "chain": "arbitrum",
        "tx_hash": "0x38a74ae875fc95951fc1aa4fafb4cd7c018912dbe2b5d192fdc218e1adb27fea",
        "flow": "OATH -55381.5",
        "note": "Bridges the second large LP branch from Arbitrum to Avalanche.",
    },
    {
        "route": "large_second_lp_branch_to_avalanche",
        "timestamp": "2023-04-06T22:35:42Z",
        "chain": "avalanche",
        "tx_hash": "0x55deed10897c6aa323537350a2db37affe6d5f06b94a4d083989c447c2bd9408",
        "flow": "OATH +55326.1185",
        "note": "Avalanche receipt from Arbitrum.",
    },
    {
        "route": "large_avalanche_lp_back_to_arbitrum",
        "timestamp": "2023-04-06T22:53:42Z",
        "chain": "avalanche",
        "tx_hash": "0xd873e4d0af3189aa42ce71e4770ed14e0ce9136d2d10697bd4cffcd9df18a9e9",
        "flow": "OATH -55210.307972558138831081; WETH.e -6.944090877608349585; vAMM-OATH/WETH.e +619.181230288990992974",
        "note": "Adds the second large branch to Avalanche OATH/WETH.e LP.",
    },
    {
        "route": "large_avalanche_lp_back_to_arbitrum",
        "timestamp": "2023-04-07T22:16:46Z",
        "chain": "avalanche",
        "tx_hash": "0x2ac9236cdff2d19f42384b09de5ec805e606432bd1e84ee8ae285a78fd14cad2",
        "flow": "vAMM-OATH/WETH.e -1241.934930584579298112; OATH +110374.466585288208452027; WETH.e +13.974267958199223167",
        "note": "Unwinds the Avalanche LP immediately before the bridge back to Arbitrum.",
    },
    {
        "route": "large_avalanche_lp_back_to_arbitrum",
        "timestamp": "2023-04-07T22:20:35Z",
        "chain": "avalanche",
        "tx_hash": "0x2438125ab490e737bdf56352da494c5d1539920c05f880f0c7ceac4c60906488",
        "flow": "OATH -110490",
        "note": "Bridges the large Avalanche LP unwind back to Arbitrum.",
    },
    {
        "route": "large_avalanche_lp_back_to_arbitrum",
        "timestamp": "2023-04-07T22:22:21Z",
        "chain": "arbitrum",
        "tx_hash": "0xd45ce2727020117542372c73deb3879d073125380708981a4c378975ae5eb877",
        "flow": "OATH +110379.51",
        "note": "This is the large OATH bridge-in consumed into the move-date Arbitrum WETH/OATH LP.",
    },
    {
        "route": "smaller_april_fantom_optimism_arbitrum",
        "timestamp": "2023-04-01T16:07:06Z",
        "chain": "fantom",
        "tx_hash": "0xdf3f7f76fe3c0854564db35d4024200b9278d957ab14759811b45f22e2624a03",
        "flow": "Reaper OATH +20833.3333333333",
        "note": "Visible Fantom Reaper vesting/compensation receipt before the move.",
    },
    {
        "route": "smaller_april_fantom_optimism_arbitrum",
        "timestamp": "2023-04-06T21:59:37Z",
        "chain": "fantom",
        "tx_hash": "0x599458698118c645eb262ea449778329be5998a6cf98c4db021789eabc797bcc",
        "flow": "Reaper OATH -20833.3333333333; Metamask3 OATH +20833.3333333333",
        "note": "Transfers the April Reaper OATH receipt to Metamask3.",
    },
    {
        "route": "smaller_april_fantom_optimism_arbitrum",
        "timestamp": "2023-04-06T22:04:08Z",
        "chain": "fantom",
        "tx_hash": "0x9c8a7ca61d683a483571f5120ec5ef7b82186123cb4c4a3e892cb950898d5895",
        "flow": "OATH -20833.4",
        "note": "Bridges the April Reaper OATH from Fantom to Optimism.",
    },
    {
        "route": "smaller_april_fantom_optimism_arbitrum",
        "timestamp": "2023-04-06T22:05:50Z",
        "chain": "optimism",
        "tx_hash": "0x74541f7e8061bced939347c781c970469773df35f2103e64438184beec9e4e82",
        "flow": "OATH +20812.5666",
        "note": "Optimism receipt from Fantom.",
    },
    {
        "route": "smaller_april_fantom_optimism_arbitrum",
        "timestamp": "2023-04-06T22:29:01Z",
        "chain": "optimism",
        "tx_hash": "0x478adb4da5d122837ff7bd9f8788dc99176b7d7e81b0166f74f9c8729922c8aa",
        "flow": "OATH -20812.5666 into BPT-BOATH",
        "note": "Adds the bridged OATH to an Optimism Beethoven/Balancer pool.",
    },
    {
        "route": "smaller_april_fantom_optimism_arbitrum",
        "timestamp": "2023-04-08T20:27:36Z",
        "chain": "optimism",
        "tx_hash": "0xff1088389572c3f1d750e57ee6b7951f19eeaeae6f7c2fb665e8658e59c80513",
        "flow": "BPT-BOATH -4286.530262444379754122; OATH +17366.687747501314124732; WETH +0.516482693023296757",
        "note": "Exits the Optimism pool before bridging OATH to Arbitrum.",
    },
    {
        "route": "smaller_april_fantom_optimism_arbitrum",
        "timestamp": "2023-04-08T20:31:36Z",
        "chain": "optimism",
        "tx_hash": "0x7db615fe9b96a7c4de77f537ea94add9d0296b3b0409792a80fd5db3e2a0e1e6",
        "flow": "OATH -17366.6",
        "note": "Bridges the Optimism OATH to Arbitrum.",
    },
    {
        "route": "smaller_april_fantom_optimism_arbitrum",
        "timestamp": "2023-04-08T20:43:47Z",
        "chain": "arbitrum",
        "tx_hash": "0x037e9acac695b1391c1c755f736f209a4bf11ce254be541d09de93c72d6526ca",
        "flow": "OATH +17349.2334",
        "note": "Arbitrum receipt; 5518.155490623468125458 OATH from this lot is consumed into the move-date LP inputs.",
    },
]


@dataclass
class Lot:
    amount: Decimal
    timestamp: str
    tx_hash: str
    bucket: str
    note: str
    cost_assets: dict[str, Decimal]


def parse_decimal(value: Any) -> Decimal:
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


def parse_ts(value: str) -> datetime:
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


def fmt_decimal(value: Decimal | str | int, places: str | None = None) -> str:
    if not isinstance(value, Decimal):
        value = parse_decimal(value)
    if places:
        value = value.quantize(Decimal(places), rounding=ROUND_HALF_UP)
    text = format(value.normalize(), "f")
    if "." in text:
        text = text.rstrip("0").rstrip(".")
    return text or "0"


def q2(value: Decimal) -> Decimal:
    return value.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def read_csv_after_header(path: Path, header_prefixes: tuple[str, ...]) -> list[dict[str, str]]:
    lines = path.read_text(encoding="utf-8-sig", errors="replace").splitlines()
    while lines and not any(lines[0].startswith(prefix) for prefix in header_prefixes):
        lines.pop(0)
    if not lines:
        return []
    return list(csv.DictReader(lines))


def write_csv(path: Path, rows: list[dict[str, Any]], fieldnames: list[str]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)


def tx_rows(rows: list[dict[str, str]]) -> dict[str, list[dict[str, str]]]:
    grouped: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        grouped[row["tx_hash"]].append(row)
    return grouped


def token_amount_in_tx(grouped: dict[str, list[dict[str, str]]], tx_hash: str, symbol: str) -> Decimal:
    return sum(parse_decimal(row["amount"]) for row in grouped.get(tx_hash, []) if row["symbol"] == symbol)


def negative_cost_assets(grouped: dict[str, list[dict[str, str]]], tx_hash: str) -> dict[str, Decimal]:
    assets: dict[str, Decimal] = defaultdict(Decimal)
    for row in grouped.get(tx_hash, []):
        symbol = row["symbol"]
        if symbol == "OATH":
            continue
        if row["direction"] != "out":
            continue
        amount = -parse_decimal(row["amount"])
        if amount <= 0:
            continue
        # Gas is tracked separately and is not an acquisition-cost source for
        # the OATH amount in this workpaper.
        if symbol == "ETH" and row.get("asset_type") == "native" and "gas" in row.get("name", "").lower():
            continue
        assets[symbol] += amount
    return dict(assets)


def consume_lots(lots: deque[Lot], amount: Decimal) -> list[tuple[Lot, Decimal]]:
    remaining = amount
    consumed: list[tuple[Lot, Decimal]] = []
    while remaining > 0 and lots:
        lot = lots[0]
        original_amount = lot.amount
        take = min(lot.amount, remaining)
        ratio = take / original_amount if original_amount else Decimal("0")
        consumed_cost_assets = {
            symbol: cost_amount * ratio for symbol, cost_amount in lot.cost_assets.items()
        }
        consumed.append(
            (
                Lot(
                    amount=take,
                    timestamp=lot.timestamp,
                    tx_hash=lot.tx_hash,
                    bucket=lot.bucket,
                    note=lot.note,
                    cost_assets=consumed_cost_assets,
                ),
                take,
            )
        )
        lot.amount -= take
        for symbol, cost_amount in consumed_cost_assets.items():
            lot.cost_assets[symbol] -= cost_amount
        remaining -= take
        if lot.amount == 0:
            lots.popleft()
    if remaining > Decimal("0.000000000000000001"):
        consumed.append(
            (
                Lot(
                    amount=remaining,
                    timestamp="",
                    tx_hash="ARCHIVE_GAP_OR_PREHISTORY",
                    bucket="archive_gap",
                    note="OATH source not present in the archived movement file before this consumption.",
                    cost_assets={},
                ),
                remaining,
            )
        )
    return consumed


def classify_oath_inflow(row: dict[str, str], grouped: dict[str, list[dict[str, str]]]) -> Lot:
    amount = parse_decimal(row["amount"])
    method = row.get("method", "")
    note = ""
    bucket = "other_oath_inflow"
    if method.startswith("anySwapInAuto"):
        if row["tx_hash"] == "0xd45ce2727020117542372c73deb3879d073125380708981a4c378975ae5eb877":
            bucket = "bridge_in_avalanche_lp_unwind"
            note = "Large Arbitrum OATH bridge-in from Avalanche LP unwind; predecessor hops are pinned in the Fantom-origin trace section."
        else:
            bucket = "bridge_in_cross_chain"
            note = "Cross-chain OATH bridge-in. The April bridge path is linked to Fantom -> Optimism -> Arbitrum in the Fantom-origin trace section."
    elif method.startswith("swap"):
        costs = negative_cost_assets(grouped, row["tx_hash"])
        cost_symbols = ",".join(sorted(costs)) or "unknown"
        bucket = f"swap_purchase_{cost_symbols}"
        note = f"OATH acquired in a pre-move swap using {cost_symbols}."
    elif method.startswith("transfer") and any(
        tx_row.get("wallet_label") == "Reaper"
        and tx_row.get("direction") == "out"
        and tx_row.get("symbol") == "OATH"
        for tx_row in grouped.get(row["tx_hash"], [])
    ):
        bucket = "internal_transfer_from_reaper"
        note = "OATH transferred from the Reaper wallet after a cross-chain bridge or vesting flow."
    elif method.startswith("removeLiquidity"):
        bucket = "prior_lp_unwind"
        note = "OATH received by unwinding an earlier OATH LP position before the move."
    elif method.startswith("claimRewards"):
        bucket = "reward_claim"
        note = "OATH reward claim before the move."
    else:
        note = "OATH inflow with no stronger local source classification."
    return Lot(
        amount=amount,
        timestamp=row["timestamp"],
        tx_hash=row["tx_hash"],
        bucket=bucket,
        note=note,
        cost_assets=negative_cost_assets(grouped, row["tx_hash"]),
    )


def build_vramm_inputs(rows: list[dict[str, str]], grouped: dict[str, list[dict[str, str]]]) -> list[dict[str, Any]]:
    vramm_lots: deque[Lot] = deque()
    output: list[dict[str, Any]] = []

    relevant = [
        row
        for row in rows
        if row["chain"] == CHAIN
        and row["wallet_address"].lower() == WALLET
        and row["symbol"] == "vrAMM-WETH/OATH"
        and parse_ts(row["timestamp"]) < MOVE_CUTOFF
    ]

    for row in relevant:
        amount = parse_decimal(row["amount"])
        method = row.get("method", "")
        if row["direction"] == "in":
            vramm_lots.append(
                Lot(
                    amount=amount,
                    timestamp=row["timestamp"],
                    tx_hash=row["tx_hash"],
                    bucket="source_vramm_lp_mint",
                    note="vrAMM LP minted before the move.",
                    cost_assets={},
                )
            )
        elif row["direction"] == "out":
            nead_in = token_amount_in_tx(grouped, row["tx_hash"], "nead-vrAMM-WETH/OATH")
            consumed_lots = consume_lots(vramm_lots, -amount)
            if not method.startswith("deposit") or nead_in <= 0:
                continue
            for lot, consumed in consumed_lots:
                source_lp_amount = token_amount_in_tx(grouped, lot.tx_hash, "vrAMM-WETH/OATH")
                source_weth = -token_amount_in_tx(grouped, lot.tx_hash, "WETH")
                source_oath = -token_amount_in_tx(grouped, lot.tx_hash, "OATH")
                ratio = consumed / source_lp_amount if source_lp_amount else Decimal("0")
                output.append(
                    {
                        "deposit_timestamp": row["timestamp"],
                        "deposit_tx_hash": row["tx_hash"],
                        "nead_receipt_amount": fmt_decimal(consumed),
                        "source_lp_tx_hash": lot.tx_hash,
                        "source_lp_timestamp": lot.timestamp,
                        "source_lp_amount_consumed": fmt_decimal(consumed),
                        "source_lp_amount_total": fmt_decimal(source_lp_amount),
                        "proration_ratio": fmt_decimal(ratio),
                        "weth_input_amount": fmt_decimal(source_weth * ratio),
                        "oath_input_amount": fmt_decimal(source_oath * ratio),
                    }
                )
    return output


def build_oath_allocations(
    rows: list[dict[str, str]], grouped: dict[str, list[dict[str, str]]], lp_input_rows: list[dict[str, Any]]
) -> list[dict[str, Any]]:
    move_lp_txs = {row["source_lp_tx_hash"] for row in lp_input_rows}
    oath_lots: deque[Lot] = deque()
    output: list[dict[str, Any]] = []

    relevant = [
        row
        for row in rows
        if row["chain"] == CHAIN
        and row["wallet_address"].lower() == WALLET
        and row["symbol"] == "OATH"
        and parse_ts(row["timestamp"]) < MOVE_CUTOFF
    ]

    for row in relevant:
        amount = parse_decimal(row["amount"])
        if row["direction"] == "in":
            oath_lots.append(classify_oath_inflow(row, grouped))
            continue
        if row["direction"] != "out":
            continue

        consumed_lots = consume_lots(oath_lots, -amount)
        if row["tx_hash"] not in move_lp_txs:
            continue

        for lot, consumed in consumed_lots:
            output.append(
                {
                    "lp_tx_hash": row["tx_hash"],
                    "lp_timestamp": row["timestamp"],
                    "oath_consumed_in_move_lp": fmt_decimal(consumed),
                    "source_bucket": lot.bucket,
                    "source_tx_hash": lot.tx_hash,
                    "source_timestamp": lot.timestamp,
                    "source_note": lot.note,
                    "source_cost_asset_amounts": "; ".join(
                        f"{symbol} {fmt_decimal(amount)}" for symbol, amount in sorted(lot.cost_assets.items())
                    ),
                }
            )
    return output


def summarize_koinly_2022(tx_path: Path, income_path: Path, eoy_path: Path) -> dict[str, Any]:
    tx_rows_2022 = read_csv_after_header(tx_path, ("Date,",))
    received: dict[str, dict[str, Decimal | int]] = defaultdict(
        lambda: {"amount": Decimal("0"), "cost_basis_sek": Decimal("0"), "net_value_sek": Decimal("0"), "rows": 0}
    )
    sent: dict[str, dict[str, Decimal | int]] = defaultdict(
        lambda: {"amount": Decimal("0"), "cost_basis_sek": Decimal("0"), "net_value_sek": Decimal("0"), "rows": 0}
    )
    for row in tx_rows_2022:
        tag = row.get("Tag", "").strip() or "(blank)"
        row_type = row.get("Type", "").strip()
        key = f"{row_type}/{tag}"
        if row.get("Received Currency", "").upper() == "OATH":
            received[key]["amount"] += parse_decimal(row.get("Received Amount"))
            received[key]["cost_basis_sek"] += parse_decimal(row.get("Received Cost Basis"))
            received[key]["net_value_sek"] += parse_decimal(row.get("Net Value (SEK)"))
            received[key]["rows"] += 1
        if row.get("Sent Currency", "").upper() == "OATH":
            sent[key]["amount"] += parse_decimal(row.get("Sent Amount"))
            sent[key]["cost_basis_sek"] += parse_decimal(row.get("Sent Cost Basis"))
            sent[key]["net_value_sek"] += parse_decimal(row.get("Net Value (SEK)"))
            sent[key]["rows"] += 1

    income_rows = read_csv_after_header(income_path, ("Date,",))
    income_oath_amount = Decimal("0")
    income_oath_value = Decimal("0")
    income_oath_rows = 0
    for row in income_rows:
        if row.get("Asset", "").upper() == "OATH":
            income_oath_amount += parse_decimal(row.get("Amount"))
            income_oath_value += parse_decimal(row.get("Value (SEK)"))
            income_oath_rows += 1

    eoy_rows = read_csv_after_header(eoy_path, ("Asset,",))
    eoy_oath = []
    for row in eoy_rows:
        asset = row.get("Asset", "")
        if asset.startswith("OATH"):
            quantity = row.get("Quantity", row.get("Amount", ""))
            cost = row.get("Cost (SEK)", row.get("Cost Basis (SEK)", ""))
            value = row.get("Value (SEK)", row.get("Market Value (SEK)", ""))
            eoy_oath.append(
                {
                    "asset": asset,
                    "amount": fmt_decimal(parse_decimal(quantity)),
                    "cost_sek": fmt_decimal(parse_decimal(cost), "0.01"),
                    "market_value_sek": fmt_decimal(parse_decimal(value), "0.01"),
                }
            )

    return {
        "received": {
            key: {
                "amount": fmt_decimal(value["amount"]),
                "cost_basis_sek": fmt_decimal(value["cost_basis_sek"], "0.01"),
                "net_value_sek": fmt_decimal(value["net_value_sek"], "0.01"),
                "rows": value["rows"],
            }
            for key, value in sorted(received.items())
        },
        "sent": {
            key: {
                "amount": fmt_decimal(value["amount"]),
                "cost_basis_sek": fmt_decimal(value["cost_basis_sek"], "0.01"),
                "net_value_sek": fmt_decimal(value["net_value_sek"], "0.01"),
                "rows": value["rows"],
            }
            for key, value in sorted(sent.items())
        },
        "income_report_oath_rewards": {
            "amount": fmt_decimal(income_oath_amount),
            "value_sek": fmt_decimal(income_oath_value, "0.01"),
            "rows": income_oath_rows,
        },
        "end_of_year_oath_rows": eoy_oath,
    }


def summarize_2023_oath_receipts(rows: list[dict[str, str]]) -> list[dict[str, Any]]:
    receipts = []
    for row in rows:
        if row["symbol"] != "OATH" or row["direction"] != "in":
            continue
        if row["chain"] != "fantom" or row["wallet_label"] != "Reaper":
            continue
        ts = parse_ts(row["timestamp"])
        if datetime(2023, 1, 1, tzinfo=timezone.utc) <= ts < MOVE_CUTOFF:
            amount = parse_decimal(row["amount"])
            if amount >= Decimal("10000"):
                receipts.append(
                    {
                        "timestamp": row["timestamp"],
                        "amount": fmt_decimal(amount),
                        "tx_hash": row["tx_hash"],
                    }
                )
    return receipts


def bucket_status(bucket: str) -> str:
    if bucket.startswith("swap_purchase_WETH"):
        return "Potentially supportable if the ETH/WETH source basis is accepted and not double counted."
    if bucket.startswith("swap_purchase_DOLA"):
        return "Selected as a distinct source-open bucket if the DOLA/crAMM-FRAX/DOLA predecessor and no-double-counting trace are accepted."
    if bucket == "bridge_in_cross_chain":
        return "Reviewable. April bridge path is visible back to Fantom/Reaper via Optimism and the companion vesting trace links the source to recurring distributor/vesting receipts, but valuation/tax-basis treatment remains unresolved."
    if bucket == "bridge_in_avalanche_lp_unwind":
        return "Reviewable. Source is traced through Avalanche/Ethereum/Arbitrum bridge loops back to Fantom-linked Reaper/LP flows, and the companion vesting trace links the Fantom source to distributor/vesting receipts; valuation/tax-basis treatment remains unresolved."
    if bucket == "bridge_in_unresolved_large":
        return "Not filing-ready. The OATH amount is real, but the predecessor bridge/source is not pinned in this archive."
    if bucket == "internal_transfer_from_reaper":
        return "Reviewable. Internal transfer from Reaper; link to Fantom vesting/bridge and Swedish treatment before using."
    if bucket == "prior_lp_unwind":
        return "Tiny carryover from an earlier LP unwind; not material by itself."
    return "Pending source review."


def make_markdown(
    path: Path,
    lp_inputs: list[dict[str, Any]],
    allocations: list[dict[str, Any]],
    koinly: dict[str, Any],
    receipts_2023: list[dict[str, Any]],
    summary: dict[str, Any],
) -> None:
    lines: list[str] = []
    lines.append("# Move-Date OATH/WETH LP Provenance Workpaper")
    lines.append("")
    lines.append(f"Cut-off: `{MOVE_CUTOFF_TEXT}`")
    lines.append("")
    lines.append(
        "This workpaper traces the `nead-vrAMM-WETH/OATH` position held at the Poland move date. "
        "It is evidence for position existence, value, and source buckets. It does not by itself create a final PIT-38 filing value."
    )
    lines.append("")
    lines.append("## Bottom Line")
    lines.append("")
    lines.append(
        f"- Move-date receipt balance traced: `{summary['move_date_nead_receipt']}` `nead-vrAMM-WETH/OATH`."
    )
    lines.append(
        f"- Immediate pre-move LP inputs: `{summary['direct_weth_input']}` WETH and `{summary['oath_input']}` OATH."
    )
    lines.append(
        f"- Source-input value proxy at move-date prices: `{summary['source_input_value_usd']}` USD / `{summary['source_input_value_pln']}` PLN."
    )
    lines.append(
        f"- WETH-linked component, including WETH swapped into OATH, is `{summary['weth_linked_total']}` WETH, with a provisional existing-workpaper cost proxy of `{summary['weth_linked_proxy_pln']}` PLN."
    )
    lines.append(
        "- The largest OATH bridge bucket is now traced through the Avalanche/Ethereum/Arbitrum loop back to Fantom-linked Reaper and LP flows; the smaller April bridge bucket is traced Fantom -> Optimism -> Arbitrum."
    )
    lines.append(
        "- Current selected PIT-38 input adds the WETH-linked component and the distinct DOLA-funded OATH component. OATH-native bridge/reward/TGE buckets remain excluded pending valuation and tax-basis review."
    )
    lines.append("")
    lines.append("## Immediate LP Inputs")
    lines.append("")
    lines.append("| Deposit date | nead receipt | Source LP tx | WETH input | OATH input |")
    lines.append("| --- | ---: | --- | ---: | ---: |")
    for row in lp_inputs:
        lines.append(
            f"| {row['deposit_timestamp']} | `{row['nead_receipt_amount']}` | `{row['source_lp_tx_hash']}` | `{row['weth_input_amount']}` | `{row['oath_input_amount']}` |"
        )
    lines.append("")
    lines.append("## OATH Source Buckets")
    lines.append("")
    lines.append("| Source bucket | OATH consumed | Visible cost asset | Status |")
    lines.append("| --- | ---: | --- | --- |")
    for bucket, values in summary["oath_source_buckets"].items():
        cost_assets = "; ".join(f"{k} {v}" for k, v in values["cost_assets"].items()) or ""
        lines.append(
            f"| `{bucket}` | `{values['oath']}` | {cost_assets} | {bucket_status(bucket)} |"
        )
    lines.append("")
    lines.append("## Fantom-Origin Bridge Trace")
    lines.append("")
    lines.append(
        "The high-value OATH source is not just an unexplained Avalanche receipt. "
        "The predecessor rows show repeated Fantom-origin OATH moving through Arbitrum, Ethereum, Avalanche, and Optimism farming routes before the move-date Arbitrum WETH/OATH LP. "
        "This strengthens the factual provenance. The companion OATH vesting trace links the Fantom source rows to distributor/vesting receipts, but still does not decide the taxable-value/acquisition-basis treatment for those original OATH receipts."
    )
    lines.append("")
    lines.append("| Route | Timestamp | Chain | Tx | Flow | Note |")
    lines.append("| --- | --- | --- | --- | --- | --- |")
    for row in FANTOM_ORIGIN_TRACE:
        lines.append(
            f"| {row['route']} | {row['timestamp']} | {row['chain']} | `{row['tx_hash']}` | {row['flow']} | {row['note']} |"
        )
    lines.append("")
    lines.append("## Avalanche Bridge Trace")
    lines.append("")
    lines.append("This is the compact Avalanche sub-trace for the largest final Arbitrum bridge-in. The fuller predecessor route is in the Fantom-origin trace above.")
    lines.append("")
    lines.append("| Timestamp | Chain | Tx | Flow | Note |")
    lines.append("| --- | --- | --- | --- | --- |")
    for row in AVALANCHE_BIG_BRIDGE_TRACE:
        lines.append(f"| {row['timestamp']} | {row['chain']} | `{row['tx_hash']}` | {row['flow']} | {row['note']} |")
    lines.append("")
    lines.append("## Allocation Detail")
    lines.append("")
    lines.append("| LP tx | OATH used | Source bucket | Source tx | Cost asset |")
    lines.append("| --- | ---: | --- | --- | --- |")
    for row in allocations:
        lines.append(
            f"| `{row['lp_tx_hash']}` | `{row['oath_consumed_in_move_lp']}` | `{row['source_bucket']}` | `{row['source_tx_hash']}` | {row['source_cost_asset_amounts']} |"
        )
    lines.append("")
    lines.append("## Koinly 2022 OATH Evidence")
    lines.append("")
    lines.append("Koinly 2022 is useful because it shows OATH was not an imaginary zero-history token: it had reported rewards, deposits, disposals, and year-end holdings. It is still not enough by itself to prove every 2023 OATH lot used in the Arbitrum LP.")
    lines.append("")
    lines.append("| 2022 received category | Amount | Cost basis SEK | Net value SEK | Rows |")
    lines.append("| --- | ---: | ---: | ---: | ---: |")
    for key, values in koinly["received"].items():
        lines.append(
            f"| `{key}` | `{values['amount']}` | `{values['cost_basis_sek']}` | `{values['net_value_sek']}` | {values['rows']} |"
        )
    lines.append("")
    lines.append("| 2022 sent category | Amount | Sent cost basis SEK | Net value SEK | Rows |")
    lines.append("| --- | ---: | ---: | ---: | ---: |")
    for key, values in koinly["sent"].items():
        lines.append(
            f"| `{key}` | `{values['amount']}` | `{values['cost_basis_sek']}` | `{values['net_value_sek']}` | {values['rows']} |"
        )
    lines.append("")
    rewards = koinly["income_report_oath_rewards"]
    lines.append(
        f"Income report OATH reward rows: `{rewards['amount']}` OATH, `{rewards['value_sek']}` SEK across `{rewards['rows']}` rows."
    )
    lines.append("")
    lines.append("| 2022 end-of-year asset | Amount | Cost SEK | Market SEK |")
    lines.append("| --- | ---: | ---: | ---: |")
    for row in koinly["end_of_year_oath_rows"]:
        lines.append(f"| `{row['asset']}` | `{row['amount']}` | `{row['cost_sek']}` | `{row['market_value_sek']}` |")
    lines.append("")
    lines.append("## 2023 Pre-Move OATH Receipts")
    lines.append("")
    lines.append("These visible Fantom Reaper receipts are now tied by `move-date-oath-vesting-trace.md` to recurring distributor/vesting flows. They need valuation and tax-basis support before they can be counted as importable PIT-38 basis.")
    lines.append("")
    lines.append("| Timestamp | Amount | Tx |")
    lines.append("| --- | ---: | --- |")
    for row in receipts_2023:
        lines.append(f"| {row['timestamp']} | `{row['amount']}` | `{row['tx_hash']}` |")
    lines.append("")
    lines.append("## Filing Implication")
    lines.append("")
    lines.append("- The WETH/OATH LP is a high-value real move-date asset, not a spam or dust row.")
    lines.append("- The directly traceable WETH side is the strongest part of this position.")
    lines.append("- OATH bought with WETH can ride on the same ETH/WETH evidence if no double counting is found.")
    lines.append("- OATH bought with DOLA is now treated as a distinct source-open bucket; do not double count the adjacent DOLA-to-WETH or DOLA-to-WBTC branches.")
    lines.append("- The large `110,379.51` OATH bridge-in is now traced through Avalanche/Ethereum/Arbitrum back to Fantom-linked Reaper/LP flows; the companion vesting trace links those Fantom rows to distributor/vesting receipts, but valuation/tax-basis treatment remains unresolved.")
    lines.append("- The smaller `5,518.155490623468125458` OATH bridge bucket is traced to the April Fantom -> Optimism -> Arbitrum path.")
    lines.append("- For the urgent filing, this workpaper supports adding the WETH-linked component plus the DOLA-funded OATH component while preserving OATH-native bridge/reward/TGE buckets as future amendment / interpretation / adviser-review items.")
    lines.append("")
    lines.append("## Outputs")
    lines.append("")
    lines.append("- LP inputs CSV: `move-date-oath-provenance-lp-inputs.csv`")
    lines.append("- OATH allocation CSV: `move-date-oath-provenance-source-allocations.csv`")
    lines.append("- Fantom-origin trace CSV: `move-date-oath-fantom-origin-trace.csv`")
    lines.append("- Avalanche bridge trace CSV: `move-date-oath-avalanche-bridge-trace.csv`")
    lines.append("- Related vesting/distributor trace: `move-date-oath-vesting-trace.md`")
    lines.append("- Summary JSON: `move-date-oath-provenance-summary.json`")
    lines.append("")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--inventory-dir", type=Path, default=DEFAULT_INVENTORY_DIR)
    parser.add_argument("--koinly-2022-tx", type=Path, default=DEFAULT_KOINLY_2022_TX)
    parser.add_argument("--koinly-2022-income", type=Path, default=DEFAULT_KOINLY_2022_INCOME)
    parser.add_argument("--koinly-2022-eoy", type=Path, default=DEFAULT_KOINLY_2022_EOY)
    args = parser.parse_args()

    movements_path = args.inventory_dir / "move-date-movements.csv"
    rows = read_csv(movements_path)
    grouped = tx_rows(rows)

    lp_inputs = build_vramm_inputs(rows, grouped)
    allocations = build_oath_allocations(rows, grouped, lp_inputs)
    koinly = summarize_koinly_2022(args.koinly_2022_tx, args.koinly_2022_income, args.koinly_2022_eoy)
    receipts_2023 = summarize_2023_oath_receipts(rows)

    direct_weth = sum(parse_decimal(row["weth_input_amount"]) for row in lp_inputs)
    oath_input = sum(parse_decimal(row["oath_input_amount"]) for row in lp_inputs)
    nead_receipt = sum(parse_decimal(row["nead_receipt_amount"]) for row in lp_inputs)

    bucket_values: dict[str, dict[str, Any]] = {}
    for row in allocations:
        bucket = row["source_bucket"]
        values = bucket_values.setdefault(bucket, {"oath": Decimal("0"), "cost_assets": defaultdict(Decimal)})
        values["oath"] += parse_decimal(row["oath_consumed_in_move_lp"])
        for part in row["source_cost_asset_amounts"].split("; "):
            if not part:
                continue
            symbol, amount_text = part.split(" ", 1)
            values["cost_assets"][symbol] += parse_decimal(amount_text)

    weth_from_oath_swaps = sum(
        values["cost_assets"].get("WETH", Decimal("0")) for values in bucket_values.values()
    )
    dola_from_oath_swaps = sum(
        values["cost_assets"].get("DOLA", Decimal("0")) for values in bucket_values.values()
    )
    weth_linked_total = direct_weth + weth_from_oath_swaps

    source_input_value_usd = direct_weth * ETH_USD_2023_04_12 + oath_input * OATH_USD_USER_2023_04_12
    source_input_value_pln = source_input_value_usd * USD_PLN_2023_04_12
    weth_linked_proxy_pln = weth_linked_total * WETH_PROXY_PLN_PER_WETH
    dola_proxy_pln = dola_from_oath_swaps * USD_PLN_2023_04_12

    summary = {
        "cutoff": MOVE_CUTOFF_TEXT,
        "move_date_nead_receipt": fmt_decimal(nead_receipt),
        "direct_weth_input": fmt_decimal(direct_weth),
        "oath_input": fmt_decimal(oath_input),
        "source_input_value_usd": fmt_decimal(q2(source_input_value_usd), "0.01"),
        "source_input_value_pln": fmt_decimal(q2(source_input_value_pln), "0.01"),
        "weth_from_oath_swaps": fmt_decimal(weth_from_oath_swaps),
        "dola_from_oath_swaps": fmt_decimal(dola_from_oath_swaps),
        "weth_linked_total": fmt_decimal(weth_linked_total),
        "weth_linked_proxy_pln": fmt_decimal(q2(weth_linked_proxy_pln), "0.01"),
        "dola_proxy_pln_at_move_usdpln": fmt_decimal(q2(dola_proxy_pln), "0.01"),
        "oath_source_buckets": {
            bucket: {
                "oath": fmt_decimal(values["oath"]),
                "cost_assets": {
                    symbol: fmt_decimal(amount)
                    for symbol, amount in sorted(values["cost_assets"].items())
                },
                "status": bucket_status(bucket),
            }
            for bucket, values in sorted(bucket_values.items())
        },
        "koinly_2022": koinly,
        "visible_2023_reaper_oath_receipts": receipts_2023,
        "fantom_origin_trace": FANTOM_ORIGIN_TRACE,
        "avalanche_big_bridge_trace": AVALANCHE_BIG_BRIDGE_TRACE,
        "notes": [
            "Move-date source-input value uses ETH 1892.69 USD, user-provided OATH 0.2036 USD, and NBP USD/PLN 4.2713.",
            "WETH-linked proxy uses the existing move-date-basis-decision WETH trace ratio 125248.69 PLN / 13.677446 WETH.",
            "The large OATH bucket is now traced back to Fantom-linked Reaper/LP flows through documented bridge and LP hops, and a companion vesting trace links those Fantom rows to distributor/vesting receipts; this does not decide taxable-value/acquisition-basis treatment.",
            "The current selected PIT-38 filing input includes the WETH-linked component and distinct DOLA-funded OATH component; OATH-native bridge/reward/TGE buckets remain excluded pending valuation and tax-basis review.",
        ],
    }

    write_csv(
        args.inventory_dir / "move-date-oath-provenance-lp-inputs.csv",
        lp_inputs,
        [
            "deposit_timestamp",
            "deposit_tx_hash",
            "nead_receipt_amount",
            "source_lp_tx_hash",
            "source_lp_timestamp",
            "source_lp_amount_consumed",
            "source_lp_amount_total",
            "proration_ratio",
            "weth_input_amount",
            "oath_input_amount",
        ],
    )
    write_csv(
        args.inventory_dir / "move-date-oath-provenance-source-allocations.csv",
        allocations,
        [
            "lp_tx_hash",
            "lp_timestamp",
            "oath_consumed_in_move_lp",
            "source_bucket",
            "source_tx_hash",
            "source_timestamp",
            "source_note",
            "source_cost_asset_amounts",
        ],
    )
    write_csv(
        args.inventory_dir / "move-date-oath-fantom-origin-trace.csv",
        FANTOM_ORIGIN_TRACE,
        ["route", "timestamp", "chain", "tx_hash", "flow", "note"],
    )
    write_csv(
        args.inventory_dir / "move-date-oath-avalanche-bridge-trace.csv",
        AVALANCHE_BIG_BRIDGE_TRACE,
        ["timestamp", "chain", "tx_hash", "flow", "note"],
    )
    (args.inventory_dir / "move-date-oath-provenance-summary.json").write_text(
        json.dumps(summary, indent=2) + "\n", encoding="utf-8"
    )
    make_markdown(
        args.inventory_dir / "move-date-oath-provenance.md",
        lp_inputs,
        allocations,
        koinly,
        receipts_2023,
        summary,
    )


if __name__ == "__main__":
    main()
