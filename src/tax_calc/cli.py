"""Unified CLI entry point for the tax calculator."""
from __future__ import annotations

import argparse
import csv
import json
import os
import sys
from collections import Counter
from decimal import Decimal

from tax_calc.cost_pool import process_cost_pool
from tax_calc.models import fmt, fmt_full
from tax_calc.nbp import NBPClient
from tax_calc.normalizers.base import UNIFIED_COLUMNS, write_csv
from tax_calc.normalizers.binance import normalize_binance
from tax_calc.normalizers.ftx import normalize_ftx
from tax_calc.normalizers.coinbase import normalize_coinbase
from tax_calc.normalizers.kraken import normalize_kraken
from tax_calc.normalizers.salary import parse_salary_payments
from tax_calc.pit38 import generate_pit38_report
from tax_calc.prices import PriceResolver

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(SCRIPT_DIR, "..", ".."))


def _default_path(*parts: str) -> str:
    return os.path.join(PROJECT_ROOT, *parts)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="tax-calc",
        description="Polish PIT-38 crypto tax calculator (cost pool method)",
    )
    sub = parser.add_subparsers(dest="command")

    # normalize
    norm = sub.add_parser("normalize", help="Normalize exchange + salary data")
    norm.add_argument("--binance-dir",
                      default=_default_path("docs", "crypto-cex-transactions", "binance"))
    norm.add_argument("--ftx-dir",
                      default=_default_path("docs", "crypto-cex-transactions", "ftx"))
    norm.add_argument("--coinbase-dir",
                      default=_default_path("docs", "crypto-cex-transactions", "coinbase"))
    norm.add_argument("--kraken-dir",
                      default=_default_path("docs", "crypto-cex-transactions", "kraken"))
    norm.add_argument("--output-dir", default=_default_path("outputs"))

    # pit38
    pit38 = sub.add_parser("pit38", help="Calculate PIT-38 using cost pool method")
    pit38.add_argument("--input", default=_default_path("outputs", "normalized_all_exchanges.csv"))
    pit38.add_argument("--salary", nargs="*", default=[
        _default_path("docs", "crypto-transactions", "2022-fantom-salary.txt"),
        _default_path("docs", "crypto-transactions", "2022-2023-pre-poland-salary.txt"),
        _default_path("docs", "crypto-transactions", "2023-salary-invoices.txt"),
        _default_path("docs", "crypto-transactions", "2024-salary-invoices.txt"),
        _default_path("docs", "crypto-transactions", "2025-polygon-payments.txt"),
        _default_path("docs", "crypto-transactions", "coinbase-purchases.txt"),
        _default_path("docs", "crypto-transactions", "celsius-simplex-purchases.txt"),
    ])
    pit38.add_argument("--output-dir", default=_default_path("outputs"))
    pit38.add_argument("--cache-dir", default=_default_path("data"))
    pit38.add_argument("--pre-residency-costs", type=Decimal, default=Decimal("0"),
                       help="Total PLN value of crypto purchased before Polish residency (2020-2022)")
    pit38.add_argument("--first-polish-year", type=int, default=2023)

    # report
    rep = sub.add_parser("report", help="Generate PIT-38 reports from saved results")
    rep.add_argument("--results", default=_default_path("outputs", "pit38_results.json"))
    rep.add_argument("--output-dir", default=_default_path("outputs"))
    rep.add_argument("--year", type=int, nargs="*", default=[2023, 2024, 2025])

    # full
    full = sub.add_parser("full", help="Run normalize + pit38 + report")
    full.add_argument("--binance-dir",
                      default=_default_path("docs", "crypto-cex-transactions", "binance"))
    full.add_argument("--ftx-dir",
                      default=_default_path("docs", "crypto-cex-transactions", "ftx"))
    full.add_argument("--coinbase-dir",
                      default=_default_path("docs", "crypto-cex-transactions", "coinbase"))
    full.add_argument("--kraken-dir",
                      default=_default_path("docs", "crypto-cex-transactions", "kraken"))
    full.add_argument("--salary", nargs="*", default=[
        _default_path("docs", "crypto-transactions", "2022-fantom-salary.txt"),
        _default_path("docs", "crypto-transactions", "2022-2023-pre-poland-salary.txt"),
        _default_path("docs", "crypto-transactions", "2023-salary-invoices.txt"),
        _default_path("docs", "crypto-transactions", "2024-salary-invoices.txt"),
        _default_path("docs", "crypto-transactions", "2025-polygon-payments.txt"),
        _default_path("docs", "crypto-transactions", "coinbase-purchases.txt"),
        _default_path("docs", "crypto-transactions", "celsius-simplex-purchases.txt"),
    ])
    full.add_argument("--output-dir", default=_default_path("outputs"))
    full.add_argument("--cache-dir", default=_default_path("data"))
    full.add_argument("--pre-residency-costs", type=Decimal, default=Decimal("0"),
                       help="Total PLN value of crypto purchased before Polish residency")
    full.add_argument("--first-polish-year", type=int, default=2023)
    full.add_argument("--year", type=int, nargs="*", default=[2023, 2024, 2025])

    return parser.parse_args()


def cmd_normalize(args: argparse.Namespace) -> int:
    print("Normalizing Binance exports...")
    binance_txns = normalize_binance(args.binance_dir)
    print(f"  Binance: {len(binance_txns)} records")

    print("Normalizing Coinbase exports...")
    coinbase_txns = normalize_coinbase(args.coinbase_dir)
    print(f"  Coinbase: {len(coinbase_txns)} records")

    print("Normalizing FTX exports...")
    ftx_txns = normalize_ftx(args.ftx_dir)
    print(f"  FTX: {len(ftx_txns)} records")

    print("Normalizing Kraken exports...")
    kraken_txns = normalize_kraken(args.kraken_dir)
    print(f"  Kraken: {len(kraken_txns)} records")

    binance_rows = [t.to_dict() for t in binance_txns]
    ftx_rows = [t.to_dict() for t in ftx_txns]
    coinbase_rows = [t.to_dict() for t in coinbase_txns]
    kraken_rows = [t.to_dict() for t in kraken_txns]
    all_rows = binance_rows + coinbase_rows + ftx_rows + kraken_rows
    all_rows.sort(key=lambda r: r["date"])

    os.makedirs(args.output_dir, exist_ok=True)
    write_csv(os.path.join(args.output_dir, "normalized_binance.csv"), binance_rows)
    write_csv(os.path.join(args.output_dir, "normalized_ftx.csv"), ftx_rows)
    write_csv(os.path.join(args.output_dir, "normalized_coinbase.csv"), coinbase_rows)
    write_csv(os.path.join(args.output_dir, "normalized_kraken.csv"), kraken_rows)
    write_csv(os.path.join(args.output_dir, "normalized_all_exchanges.csv"), all_rows)

    type_counts = Counter(r["tx_type"] for r in all_rows)
    print(f"\nTotal: {len(all_rows)} normalized records")
    print("By type:")
    for t, c in type_counts.most_common():
        print(f"  {t}: {c}")

    year_counts = Counter(r["date"][:4] for r in all_rows)
    print("By year:")
    for y, c in sorted(year_counts.items()):
        print(f"  {y}: {c}")

    print(f"\nOutput written to {args.output_dir}/")
    return 0


def cmd_pit38(args: argparse.Namespace) -> int:
    cache_dir = getattr(args, "cache_dir", _default_path("data"))
    nbp = NBPClient(cache_path=os.path.join(cache_dir, "nbp_cache.json"))
    prices = PriceResolver(nbp, cg_cache_path=os.path.join(cache_dir, "coingecko_cache.json"))

    input_path = getattr(args, "input", _default_path("outputs", "normalized_all_exchanges.csv"))
    with open(input_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = list(reader)
    print(f"\nLoaded {len(rows)} records from {input_path}")
    ledger_sources = {row.get("source", "") for row in rows}

    # Load salary lots from all salary files
    salary_paths = getattr(args, "salary", []) or []
    if isinstance(salary_paths, str):
        salary_paths = [salary_paths]
    salary_lots = []
    for salary_path in salary_paths:
        if salary_path and os.path.exists(salary_path):
            basename = os.path.basename(salary_path)
            if "coinbase" in basename and "coinbase" in ledger_sources:
                print(f"Skipping {basename} because Coinbase exchange CSV data is already normalized.")
                continue
            # Derive source name from filename
            if "ftx" in basename:
                source_name = "ftx_purchase"
            elif "coinbase" in basename:
                source_name = "coinbase_purchase"
            elif "celsius" in basename:
                source_name = "celsius_purchase"
            elif "fantom" in basename:
                source_name = "fantom_salary"
            else:
                source_name = "polygon_salary"
            print(f"Parsing payments from {basename}...")
            lots = parse_salary_payments(salary_path, nbp, source_name=source_name)
            salary_lots.extend(lots)
            total_pln = sum(l.cost_pln for l in lots)
            print(f"  {len(lots)} payments, total {fmt(total_pln)} PLN")
    if salary_lots:
        salary_lots.sort(key=lambda l: l.date)
        print(f"  Total salary lots: {len(salary_lots)}")


    pre_residency = getattr(args, "pre_residency_costs", Decimal("0"))
    first_year = getattr(args, "first_polish_year", 2023)

    result = process_cost_pool(rows, prices, salary_lots, pre_residency, first_year)
    yearly_results = result["yearly_results"]
    warnings = result["warnings"]

    output_dir = getattr(args, "output_dir", _default_path("outputs"))
    os.makedirs(output_dir, exist_ok=True)

    # Save results as JSON for the report command
    json_data = {}
    for year, r in sorted(yearly_results.items()):
        json_data[str(year)] = {
            "revenue_pln": str(r.revenue_pln),
            "costs_current_year_pln": str(r.costs_current_year_pln),
            "costs_prior_years_pln": str(r.costs_prior_years_pln),
            "income_pln": str(r.income_pln),
            "carry_forward_pln": str(r.carry_forward_pln),
            "tax_due_pln": str(r.tax_due_pln),
            "disposal_count": r.disposal_count,
        }

    results_path = os.path.join(output_dir, "pit38_results.json")
    with open(results_path, "w", encoding="utf-8") as f:
        json.dump({"yearly_results": json_data, "warnings": warnings}, f, indent=2)

    # Export enriched detail JSON for the frontend dashboard
    detail_data = {}
    for year, r in sorted(yearly_results.items()):
        detail_data[str(year)] = r.to_dict()
    detail_path = os.path.join(output_dir, "pit38_detail.json")
    with open(detail_path, "w", encoding="utf-8") as f:
        json.dump({"yearly_results": detail_data, "warnings": warnings}, f, indent=2)

    # Print summary
    print("\n" + "=" * 70)
    print("PIT-38 COST POOL SUMMARY (Polish method)")
    print("=" * 70)

    for year in sorted(yearly_results.keys()):
        r = yearly_results[year]
        total_costs = r.costs_current_year_pln + r.costs_prior_years_pln
        print(f"\n  {year}:")
        print(f"    Revenue (przychod):          {fmt(r.revenue_pln):>15} PLN  ({r.disposal_count} disposals)")
        print(f"    Costs this year:             {fmt(r.costs_current_year_pln):>15} PLN")
        print(f"    Costs from prior years:      {fmt(r.costs_prior_years_pln):>15} PLN")
        print(f"    Total costs:                 {fmt(total_costs):>15} PLN")
        if r.income_pln > 0:
            print(f"    Income (dochod):             {fmt(r.income_pln):>15} PLN")
            print(f"    Tax due (19%):               {fmt(r.tax_due_pln):>15} PLN")
        else:
            print(f"    Income (dochod):                        0.00 PLN")
            print(f"    Carry forward to {year+1}:       {fmt(r.carry_forward_pln):>15} PLN")

    # Print revenue events for each year
    for year in sorted(yearly_results.keys()):
        r = yearly_results[year]
        if r.revenue_events:
            print(f"\n  {year} disposals ({len(r.revenue_events)} events):")
            for e in sorted(r.revenue_events, key=lambda x: x.date):
                print(f"    {e.date} {e.asset:6s} {str(e.amount.normalize()):>16s} -> "
                      f"{e.counterparty_asset:4s} {str(e.counterparty_amount.normalize()):>12s}  "
                      f"= {fmt(e.pln_value):>12s} PLN  [{e.price_method}]")

    if warnings:
        print(f"\n  {len(warnings)} warnings:")
        for w in warnings[:20]:
            print(f"    - {w}")

    # Generate markdown reports
    for year, r in sorted(yearly_results.items()):
        out_path = os.path.join(output_dir, f"pit38_report_{year}.md")
        generate_pit38_report(r, out_path)
        print(f"\n  Report: {out_path}")

    print(f"\n  Results: {results_path}")
    return 0


def cmd_report(args: argparse.Namespace) -> int:
    results_path = getattr(args, "results", _default_path("outputs", "pit38_results.json"))
    output_dir = getattr(args, "output_dir", _default_path("outputs"))
    years = getattr(args, "year", [2023, 2024, 2025])

    with open(results_path, "r") as f:
        data = json.load(f)

    from tax_calc.cost_pool import PIT38Result
    for year in years:
        y_data = data.get("yearly_results", {}).get(str(year))
        if not y_data:
            print(f"No data for {year}")
            continue

        r = PIT38Result(
            year=year,
            revenue_pln=Decimal(y_data["revenue_pln"]),
            costs_current_year_pln=Decimal(y_data["costs_current_year_pln"]),
            costs_prior_years_pln=Decimal(y_data["costs_prior_years_pln"]),
            income_pln=Decimal(y_data["income_pln"]),
            carry_forward_pln=Decimal(y_data["carry_forward_pln"]),
            tax_due_pln=Decimal(y_data["tax_due_pln"]),
            disposal_count=y_data["disposal_count"],
            revenue_events=[], cost_events=[],
            warnings=data.get("warnings", []),
        )

        out_path = os.path.join(output_dir, f"pit38_report_{year}.md")
        generate_pit38_report(r, out_path)
        print(f"Report: {out_path}")

        print(f"\n=== PIT-38 {year} ===")
        print(f"Revenue:         {fmt(r.revenue_pln)} PLN")
        print(f"Costs (current): {fmt(r.costs_current_year_pln)} PLN")
        print(f"Costs (prior):   {fmt(r.costs_prior_years_pln)} PLN")
        print(f"Income:          {fmt(r.income_pln)} PLN")
        print(f"Tax due:         {fmt(r.tax_due_pln)} PLN")
        if r.carry_forward_pln > 0:
            print(f"Carry forward:   {fmt(r.carry_forward_pln)} PLN")

    return 0


def cmd_full(args: argparse.Namespace) -> int:
    print("=== Step 1: Normalize ===\n")
    rc = cmd_normalize(args)
    if rc != 0:
        return rc

    print("\n=== Step 2: PIT-38 Cost Pool ===\n")
    args.input = os.path.join(args.output_dir, "normalized_all_exchanges.csv")
    rc = cmd_pit38(args)
    if rc != 0:
        return rc

    return 0


def main() -> int:
    args = parse_args()
    if not args.command:
        print("Usage: python -m tax_calc {normalize|pit38|report|full}", file=sys.stderr)
        return 1

    commands = {
        "normalize": cmd_normalize,
        "pit38": cmd_pit38,
        "report": cmd_report,
        "full": cmd_full,
    }
    return commands[args.command](args)
