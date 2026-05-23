#!/usr/bin/env python3
"""Build a focused OATH TGE/LGE payment scan workpaper."""

from __future__ import annotations

import csv
import json
from collections import defaultdict
from decimal import Decimal, InvalidOperation
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_INVENTORY_DIR = REPO_ROOT / "private/evidence/onchain/move-date-inventory-2023-04-12"
DEFAULT_KOINLY_2022_TX = (
    REPO_ROOT / "private/evidence/koinly/2022/koinly_2022_transaction_history_krYwagtox4_1777112970.csv"
)

OATH_DISTRIBUTOR = "0x8b4441e79151e3fc5264733a3c5da4ff8eac16c1"
OATH_CLAIM_OR_MINTER = "0x96662f375a9734654cb57bbfeb31db9dd7784a7f"
OATH_PAYMENT_RECEIVER = "0x111731a388743a75cf60cca7b140c58e41d83635"
OATH_OWNERSHIP_NFT = "0x0eaa652ac0503602923de4190ff8a97d658575fd"
OATH_TOKEN = "0x21ada0d2ac28c3a5fa3cd2ee30882da8812279b6"
LIKELY_LGE_START = "2022-04-10"
LIKELY_LGE_END = "2022-04-18"
WFTM_PAYMENT_SCAN_START = "2022-02-01"
BROADER_SCAN_START = "2022-03-01"
BROADER_SCAN_END = "2022-04-19"
STABLE_SYMBOLS = {"USDC", "USDT", "FUSDT", "DAI", "MIM", "FRAX", "DOLA", "UST", "TUSD"}
WFTM_PAYMENT_SYMBOLS = {"WFTM", "FTM"}


def parse_decimal(value: str | None) -> Decimal:
    text = str(value or "").strip().replace("\u00a0", " ").replace(" ", "")
    if not text:
        return Decimal("0")
    if "," in text and "." in text:
        text = text.replace(",", "")
    elif "," in text:
        text = text.replace(",", ".")
    try:
        return Decimal(text)
    except InvalidOperation:
        return Decimal("0")


def fmt(value: Decimal) -> str:
    text = format(value.normalize(), "f")
    return text.rstrip("0").rstrip(".") if "." in text else text


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def read_koinly(path: Path) -> list[dict[str, str]]:
    lines = path.read_text(encoding="utf-8-sig", errors="replace").splitlines()
    while lines and not lines[0].startswith("Date,"):
        lines.pop(0)
    if not lines:
        return []
    return list(csv.DictReader(lines))


def transfer_recipient(row: dict[str, str]) -> str:
    source_file = row.get("source_file", "")
    if not source_file:
        return ""
    path = REPO_ROOT / source_file
    if not path.exists():
        return ""
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return ""
    for log in payload.get("logs", []):
        if str(log.get("transactionHash", "")).lower() != row.get("tx_hash", "").lower():
            continue
        if str(log.get("address", "")).lower() != row.get("contract_address", "").lower():
            continue
        topics = log.get("topics") or []
        if len(topics) >= 3:
            return "0x" + str(topics[2])[-40:]
    return ""


def movement_flow(rows: list[dict[str, str]]) -> str:
    pieces: list[str] = []
    for row in rows:
        if row.get("direction") == "fee":
            continue
        amount = parse_decimal(row.get("amount"))
        if amount == 0:
            continue
        pieces.append(f"{row.get('symbol', '')} {fmt(amount)}")
    return "; ".join(pieces)


def build() -> None:
    inventory_dir = DEFAULT_INVENTORY_DIR
    movement_rows = read_csv(inventory_dir / "move-date-movements.csv")
    koinly_rows = read_koinly(DEFAULT_KOINLY_2022_TX)

    movements_by_tx: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in movement_rows:
        if row.get("chain") == "fantom":
            movements_by_tx[row.get("tx_hash", "")].append(row)

    stable_out_rows: list[dict[str, str]] = []
    outgoing_to_oath_distributor = 0
    for row in movement_rows:
        if row.get("chain") != "fantom" or row.get("direction") != "out":
            continue
        symbol = (row.get("symbol") or "").upper()
        amount = -parse_decimal(row.get("amount"))
        if symbol not in STABLE_SYMBOLS or amount < Decimal("1000"):
            continue
        timestamp = row.get("timestamp", "")
        if not (BROADER_SCAN_START <= timestamp[:10] < BROADER_SCAN_END):
            continue
        recipient = transfer_recipient(row)
        if recipient.lower() == OATH_DISTRIBUTOR:
            outgoing_to_oath_distributor += 1
        tx_rows = movements_by_tx.get(row.get("tx_hash", ""), [])
        inflows = [item for item in tx_rows if item.get("direction") == "in" and parse_decimal(item.get("amount")) > 0]
        stable_out_rows.append(
            {
                "timestamp": timestamp,
                "wallet_label": row.get("wallet_label", ""),
                "wallet_address": row.get("wallet_address", ""),
                "symbol": symbol,
                "amount": fmt(amount),
                "recipient": recipient,
                "tx_hash": row.get("tx_hash", ""),
                "flow": movement_flow(tx_rows),
                "has_same_tx_inflow": "yes" if inflows else "no",
            }
        )

    oath_rows: list[dict[str, str]] = []
    wftm_payment_rows: list[dict[str, str]] = []
    for row in koinly_rows:
        date = row.get("Date", "")
        tx_src = row.get("TxSrc", "")
        tx_dest = row.get("TxDest", "")
        sent_currency = row.get("Sent Currency", "").upper()
        sent_amount = parse_decimal(row.get("Sent Amount"))
        if (
            WFTM_PAYMENT_SCAN_START <= date[:10] < BROADER_SCAN_END
            and sent_currency in WFTM_PAYMENT_SYMBOLS
            and sent_amount >= Decimal("100")
            and tx_dest.lower() in {OATH_CLAIM_OR_MINTER, OATH_PAYMENT_RECEIVER}
        ):
            net_value = parse_decimal(row.get("Net Value (SEK)"))
            implied = net_value / sent_amount if sent_amount else Decimal("0")
            wftm_payment_rows.append(
                {
                    "date": date,
                    "type": row.get("Type", ""),
                    "tag": row.get("Tag", ""),
                    "sending_wallet": row.get("Sending Wallet", ""),
                    "sent_amount": row.get("Sent Amount", ""),
                    "sent_currency": row.get("Sent Currency", ""),
                    "net_value_sek": row.get("Net Value (SEK)", ""),
                    "implied_sek_per_token": fmt(implied),
                    "tx_src": tx_src,
                    "tx_dest": tx_dest,
                    "tx_hash": row.get("TxHash", ""),
                }
            )

        if not (LIKELY_LGE_START <= date[:10] < LIKELY_LGE_END):
            continue
        currencies = {row.get("Sent Currency", "").upper(), row.get("Received Currency", "").upper()}
        if "OATH" not in currencies and "USDC" not in currencies and "FTM" not in currencies:
            continue
        include = (
            "OATH" in currencies
            or tx_src.lower() in {OATH_DISTRIBUTOR, OATH_CLAIM_OR_MINTER}
            or tx_dest.lower() in {OATH_DISTRIBUTOR, OATH_CLAIM_OR_MINTER}
        )
        if not include:
            continue
        oath_rows.append(
            {
                "date": date,
                "type": row.get("Type", ""),
                "tag": row.get("Tag", ""),
                "sending_wallet": row.get("Sending Wallet", ""),
                "sent_amount": row.get("Sent Amount", ""),
                "sent_currency": row.get("Sent Currency", ""),
                "receiving_wallet": row.get("Receiving Wallet", ""),
                "received_amount": row.get("Received Amount", ""),
                "received_currency": row.get("Received Currency", ""),
                "net_value_sek": row.get("Net Value (SEK)", ""),
                "tx_src": tx_src,
                "tx_dest": tx_dest,
                "tx_hash": row.get("TxHash", ""),
            }
        )

    stable_csv = inventory_dir / "move-date-oath-tge-stable-outflow-candidates.csv"
    oath_csv = inventory_dir / "move-date-oath-tge-koinly-oath-window.csv"
    wftm_payment_csv = inventory_dir / "move-date-oath-tge-wftm-payment-candidates.csv"
    markdown = inventory_dir / "move-date-oath-tge-payment-scan.md"

    for path, rows in [
        (stable_csv, stable_out_rows),
        (oath_csv, oath_rows),
        (wftm_payment_csv, wftm_payment_rows),
    ]:
        fieldnames = list(rows[0].keys()) if rows else ["empty"]
        with path.open("w", encoding="utf-8", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)

    direct_oath = [
        row
        for row in oath_rows
        if row["received_currency"].upper() == "OATH"
        and row["tx_src"].lower() in {OATH_DISTRIBUTOR, OATH_CLAIM_OR_MINTER}
    ]
    claim_call_hashes = {
        row["tx_hash"]
        for row in oath_rows
        if row["tx_dest"].lower() == OATH_CLAIM_OR_MINTER
    }
    claim_mint_oath = [
        row
        for row in oath_rows
        if row["received_currency"].upper() == "OATH" and row["tx_hash"] in claim_call_hashes
    ]
    distributor_oath = [
        row for row in direct_oath if row["tx_src"].lower() == OATH_DISTRIBUTOR
    ]
    distributor_usdc = [
        row
        for row in oath_rows
        if row["received_currency"].upper() == "USDC" and row["tx_src"].lower() == OATH_DISTRIBUTOR
    ]

    lines = [
        "# OATH TGE/LGE Payment Scan",
        "",
        f"Window: `{LIKELY_LGE_START}` to `{LIKELY_LGE_END}` for OATH rows; `{BROADER_SCAN_START}` to `{BROADER_SCAN_END}` for large Fantom stablecoin outflows.",
        "",
        "This is a focused evidence scan for the remembered OATH TGE/LGE payment. It is not a final PIT-38 basis decision.",
        "",
        "## Current Finding",
        "",
        "- I did not find a large USDC/stablecoin payment from the known Fantom wallets to the OATH distributor or claim contracts in the likely OATH launch window.",
        f"- Large stablecoin outflows in the broader scan: `{len(stable_out_rows)}`. Stablecoin outflows to the OATH distributor `{OATH_DISTRIBUTOR}`: `{outgoing_to_oath_distributor}`.",
        "- Public launch documentation says the OATH LGE sold shares for `1 wFTM` each, not USDC/stablecoin. Source: https://blockbytes.com/2022/04/14/everything-you-need-to-know-about-oath/",
        f"- A strong WFTM payment candidate was found before the April OATH distribution window: `{len(wftm_payment_rows)}` Koinly row(s) from `{WFTM_PAYMENT_SCAN_START}` to `{BROADER_SCAN_END}` sent WFTM/FTM to OATH payment/claim contracts.",
        f"- The key row is transaction `7cd7689d05bdc844d5f8fcb14722e771b32b74f398520a05a1c710152c1614c2`: `2,877.7 WFTM` to `{OATH_PAYMENT_RECEIVER}`, Koinly net value `37,976.46 SEK`.",
        f"- The archived trace for that transaction calls `{OATH_CLAIM_OR_MINTER}`, checks `ownerOf(13)` on `{OATH_OWNERSHIP_NFT}`, then calls WFTM `transferFrom` from the wallet to `{OATH_PAYMENT_RECEIVER}`. This is payment-side evidence, not merely a later OATH receipt.",
        f"- The April 16 OATH rows are direct OATH transfers from `{OATH_DISTRIBUTOR}` to the wallet, not wallet-paid purchase calls.",
        f"- The April 17 small OATH row is a claim/mint-style call from `{OATH_CLAIM_OR_MINTER}` with only gas paid in the same transaction.",
        "",
        "## WFTM Payment Candidates",
        "",
        "| Date | Type | Sent | Net value SEK | Implied SEK/token | Tx source | Tx dest | Tx |",
        "| --- | --- | ---: | ---: | ---: | --- | --- | --- |",
    ]
    for row in wftm_payment_rows:
        sent = f"{row['sent_amount']} {row['sent_currency']}".strip()
        lines.append(
            f"| {row['date']} | {row['type']} | {sent} | {row['net_value_sek']} | {row['implied_sek_per_token']} | `{row['tx_src']}` | `{row['tx_dest']}` | `{row['tx_hash']}` |"
        )

    lines.extend(
        [
            "",
            "## Koinly OATH / Related Rows",
            "",
            "| Date | Type | Tag | Sent | Received | Tx source | Tx dest | Tx |",
            "| --- | --- | --- | ---: | ---: | --- | --- | --- |",
        ]
    )
    for row in oath_rows:
        sent = f"{row['sent_amount']} {row['sent_currency']}".strip()
        received = f"{row['received_amount']} {row['received_currency']}".strip()
        lines.append(
            f"| {row['date']} | {row['type']} | {row['tag']} | {sent} | {received} | `{row['tx_src']}` | `{row['tx_dest']}` | `{row['tx_hash']}` |"
        )

    lines.extend(
        [
            "",
            "## Direct OATH Rows In Window",
            "",
            f"- OATH transfers from distributor `{OATH_DISTRIBUTOR}`: `{len(distributor_oath)}` rows.",
            f"- OATH claim/mint receipts paired with calls to `{OATH_CLAIM_OR_MINTER}`: `{len(claim_mint_oath)}` rows.",
            f"- USDC transfers from the same distributor to the Reaper wallet in this window: `{len(distributor_usdc)}` rows.",
            "",
            "## Large Stablecoin Outflow Candidates",
            "",
            "| Timestamp | Wallet | Stable out | Recipient | Same-tx inflow | Flow | Tx |",
            "| --- | --- | ---: | --- | --- | --- | --- |",
        ]
    )
    for row in stable_out_rows:
        lines.append(
            f"| {row['timestamp']} | {row['wallet_label']} | {row['amount']} {row['symbol']} | `{row['recipient']}` | {row['has_same_tx_inflow']} | {row['flow']} | `{row['tx_hash']}` |"
        )
    lines.extend(
        [
            "",
            "## Filing Impact",
            "",
            "- The Feb 24 WFTM payment candidate should be considered for OATH-native TGE/LGE basis, subject to tracing it into OATH received and avoiding double counting against later OATH rows already valued by Koinly.",
            "- The direct OATH distributor rows may still support a later OATH-native basis analysis using Koinly-reported SEK values, but they are not evidence of a large wallet-paid USDC/stablecoin TGE purchase.",
            "- If this needs to be pushed further, the next target is address-level reconstruction for `0x6539519e69343535a2af6583d9bae3ad74c6a293`, which appears in Koinly as a recurring recipient from MetaMask1 and may be another user-controlled wallet, not an OATH sale contract.",
            "",
            "## Outputs",
            "",
            "- Stable outflow candidates CSV: `move-date-oath-tge-stable-outflow-candidates.csv`",
            "- Koinly OATH window CSV: `move-date-oath-tge-koinly-oath-window.csv`",
            "- WFTM payment candidates CSV: `move-date-oath-tge-wftm-payment-candidates.csv`",
            "",
        ]
    )
    markdown.write_text("\n".join(lines), encoding="utf-8")

    print(f"Wrote {stable_csv.relative_to(REPO_ROOT)}")
    print(f"Wrote {oath_csv.relative_to(REPO_ROOT)}")
    print(f"Wrote {wftm_payment_csv.relative_to(REPO_ROOT)}")
    print(f"Wrote {markdown.relative_to(REPO_ROOT)}")


if __name__ == "__main__":
    build()
