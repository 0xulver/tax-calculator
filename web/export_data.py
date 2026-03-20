#!/usr/bin/env python3
"""Export enriched tax data for the frontend dashboard.

Runs the cost pool calculation and exports:
- public/data/pit38_detail.json  (yearly results + all events)
- public/data/transactions.json  (normalized ledger as JSON)
"""
import csv
import json
import os
import sys

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from decimal import Decimal
from tax_calc.cost_pool import process_cost_pool
from tax_calc.models import FIFOLot, fmt, fmt_full
from tax_calc.nbp import NBPClient
from tax_calc.normalizers.salary import parse_salary_payments
from tax_calc.prices import PriceResolver

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))


def main():
    cache_dir = os.path.join(PROJECT_ROOT, "data")
    nbp = NBPClient(cache_path=os.path.join(cache_dir, "nbp_cache.json"))
    prices = PriceResolver(nbp, cg_cache_path=os.path.join(cache_dir, "coingecko_cache.json"))

    # Load salary payments
    salary_path = os.path.join(PROJECT_ROOT, "docs", "crypto-transactions", "2025-polygon-payments.txt")
    salary_lots = []
    if os.path.exists(salary_path):
        salary_lots = parse_salary_payments(salary_path, nbp)
        print(f"Loaded {len(salary_lots)} salary payments")

    # Load normalized ledger
    ledger_path = os.path.join(PROJECT_ROOT, "outputs", "normalized_all_exchanges.csv")
    with open(ledger_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = list(reader)
    print(f"Loaded {len(rows)} ledger rows")

    # Run cost pool
    result = process_cost_pool(rows, prices, salary_lots)
    yearly_results = result["yearly_results"]

    # Export detail JSON
    out_dir = os.path.join(os.path.dirname(__file__), "public", "data")
    os.makedirs(out_dir, exist_ok=True)

    detail = {}
    for year, r in sorted(yearly_results.items()):
        detail[str(year)] = r.to_dict()

    detail_path = os.path.join(out_dir, "pit38_detail.json")
    with open(detail_path, "w", encoding="utf-8") as f:
        json.dump({"yearly_results": detail, "warnings": result["warnings"]}, f, indent=2)
    print(f"Wrote {detail_path}")

    # Export transactions as JSON (for frontend cross-reference)
    tx_path = os.path.join(out_dir, "transactions.json")
    with open(tx_path, "w", encoding="utf-8") as f:
        json.dump(rows, f, indent=2)
    print(f"Wrote {tx_path}")

    print("Done!")


if __name__ == "__main__":
    main()
