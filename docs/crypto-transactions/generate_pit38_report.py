#!/usr/bin/env python3
"""
generate_pit38_report.py
Generate human-readable PIT-38 crypto tax report from FIFO calculator output.

Usage:
  python3 generate_pit38_report.py --summary outputs/pit38_summary_all.json --events outputs/tax_events_all.csv --year 2025
"""

from __future__ import annotations

import argparse
import csv
import json
import os
import sys
from collections import defaultdict
from datetime import datetime
from decimal import Decimal, ROUND_HALF_UP


def fmt(v) -> str:
    d = Decimal(str(v))
    return f"{d:,.2f}"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate PIT-38 report.")
    parser.add_argument("--summary", required=True, help="Path to pit38_summary JSON.")
    parser.add_argument("--events", required=True, help="Path to tax_events CSV.")
    parser.add_argument("--year", type=int, required=True, help="Tax year to report.")
    parser.add_argument("--output", default=None, help="Output markdown file path.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()

    with open(args.summary, "r") as f:
        summary_data = json.load(f)

    yearly = summary_data.get("yearly_summary", {})
    lot_inventory = summary_data.get("lot_inventory", {})
    warnings = summary_data.get("warnings", [])

    year_str = str(args.year)
    year_data = yearly.get(year_str)
    if not year_data:
        print(f"No data for year {args.year}", file=sys.stderr)
        return 1

    # Load tax events for the year
    events = []
    with open(args.events, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row.get("year") == year_str:
                events.append(row)

    # Group events by asset
    by_asset = defaultdict(list)
    for e in events:
        by_asset[e["asset"]].append(e)

    # Build loss carry-forward info
    prior_losses = Decimal("0")
    for y in sorted(yearly.keys()):
        if int(y) >= args.year:
            break
        net = Decimal(yearly[y]["net_income_pln"])
        if net < 0:
            prior_losses += net.copy_abs()

    net_income = Decimal(year_data["net_income_pln"])
    applied_loss = min(prior_losses, max(net_income, Decimal("0")))
    adjusted_income = net_income - applied_loss
    tax_due = max(adjusted_income * Decimal("0.19"), Decimal("0"))

    # Generate report
    lines = []
    lines.append(f"# PIT-38 Crypto Tax Report — {args.year}")
    lines.append("")
    lines.append(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    lines.append("")
    lines.append("## Summary")
    lines.append("")
    lines.append("| Item | Amount (PLN) |")
    lines.append("| --- | ---: |")
    lines.append(f"| **Revenue (przychód)** | {fmt(year_data['revenue_pln'])} |")
    lines.append(f"| **Deductible costs (koszty)** | {fmt(year_data['cost_pln'])} |")
    lines.append(f"| Gains | {fmt(year_data['gain_pln'])} |")
    lines.append(f"| Losses | {fmt(year_data['loss_pln'])} |")
    lines.append(f"| **Net income (dochód)** | {fmt(net_income)} |")
    if prior_losses > 0:
        lines.append(f"| Loss carry-forward (prior years) | {fmt(prior_losses)} |")
        lines.append(f"| Applied loss deduction | {fmt(applied_loss)} |")
        lines.append(f"| **Adjusted income** | {fmt(adjusted_income)} |")
    lines.append(f"| **Tax rate** | 19% |")
    lines.append(f"| **Tax due (podatek)** | **{fmt(tax_due)}** |")
    lines.append("")

    if prior_losses > 0 and applied_loss > 0:
        remaining_loss = prior_losses - applied_loss
        lines.append(f"> [!NOTE]")
        lines.append(f"> Loss carry-forward of {fmt(prior_losses)} PLN from prior years reduces taxable income.")
        if remaining_loss > 0:
            lines.append(f"> Remaining carry-forward for future years: {fmt(remaining_loss)} PLN (valid up to 5 years from loss year).")
        lines.append("")

    # Breakdown by asset
    lines.append("## Breakdown by Asset")
    lines.append("")
    lines.append("| Asset | # Events | Revenue (PLN) | Cost Basis (PLN) | Net Gain/Loss (PLN) |")
    lines.append("| --- | ---: | ---: | ---: | ---: |")

    for asset in sorted(by_asset.keys()):
        asset_events = by_asset[asset]
        total_rev = sum(Decimal(e["revenue_pln"]) for e in asset_events)
        total_cost = sum(Decimal(e["cost_basis_pln"]) for e in asset_events)
        total_gl = sum(Decimal(e["gain_loss_pln"]) for e in asset_events)
        lines.append(f"| {asset} | {len(asset_events)} | {fmt(total_rev)} | {fmt(total_cost)} | {fmt(total_gl)} |")

    lines.append("")

    # Detailed events
    lines.append("## Detailed Tax Events")
    lines.append("")
    lines.append("| Date | Asset | Amount | Revenue (PLN) | Cost (PLN) | Gain/Loss (PLN) | Method |")
    lines.append("| --- | --- | ---: | ---: | ---: | ---: | --- |")

    for e in events:
        gain_loss = Decimal(e["gain_loss_pln"])
        gl_indicator = "✅" if gain_loss >= 0 else "🔻"
        lines.append(
            f"| {e['date']} | {e['asset']} | {e['amount']} | "
            f"{fmt(e['revenue_pln'])} | {fmt(e['cost_basis_pln'])} | "
            f"{gl_indicator} {fmt(gain_loss)} | {e['price_method']} |"
        )

    lines.append("")

    # Remaining inventory
    if lot_inventory:
        lines.append("## Remaining Holdings (FIFO Lots)")
        lines.append("")
        lines.append("| Asset | Amount | Cost Basis (PLN) | # Lots |")
        lines.append("| --- | ---: | ---: | ---: |")
        for asset in sorted(lot_inventory.keys()):
            info = lot_inventory[asset]
            lines.append(f"| {asset} | {info['total_amount']} | {fmt(info['total_cost_pln'])} | {info['lot_count']} |")
        lines.append("")

    # Warnings
    year_warnings = [w for w in warnings if f"[{args.year}" in w or f"[{year_str}" in w]
    if year_warnings:
        lines.append("## Warnings")
        lines.append("")
        for w in year_warnings:
            lines.append(f"- ⚠ {w}")
        lines.append("")

    # Notes
    lines.append("## Notes")
    lines.append("")
    lines.append("- All values in PLN using approximate EUR/USD exchange rates (static fallback).")
    lines.append("- For final filing, re-run with `--use-api` flag to use live NBP exchange rates.")
    lines.append("- Crypto-to-crypto swaps are NOT included as taxable events (per Polish law).")
    lines.append("- Staking rewards, airdrops, and earn rewards are tracked with 0 PLN cost basis. They become taxable at disposal.")
    lines.append("- Loss carry-forward calculation is simplified; verify specific year-of-loss limits with your tax advisor.")
    lines.append("")

    report = "\n".join(lines)

    # Output
    if args.output:
        os.makedirs(os.path.dirname(args.output) or ".", exist_ok=True)
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(report)
        print(f"Report written to {args.output}")
    else:
        output_path = os.path.join(os.path.dirname(args.events), f"pit38_report_{args.year}.md")
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(report)
        print(f"Report written to {output_path}")

    # Print summary to stdout
    print(f"\n=== PIT-38 {args.year} ===")
    print(f"Revenue:    {fmt(year_data['revenue_pln'])} PLN")
    print(f"Costs:      {fmt(year_data['cost_pln'])} PLN")
    print(f"Net income: {fmt(net_income)} PLN")
    if applied_loss > 0:
        print(f"Loss applied: -{fmt(applied_loss)} PLN")
        print(f"Adjusted:   {fmt(adjusted_income)} PLN")
    print(f"Tax due:    {fmt(tax_due)} PLN (19%)")
    print(f"Events:     {len(events)} taxable disposals")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
