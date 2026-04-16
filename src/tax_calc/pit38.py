"""PIT-38 report generator using Polish annual cost pooling (not FIFO).

Enhanced with full traceability: NBP rates, source transaction IDs,
subtotals by category, and verification checksums.
"""
from __future__ import annotations

import os
from collections import defaultdict
from datetime import datetime
from decimal import Decimal, ROUND_HALF_UP

from tax_calc.cost_pool import CostPoolEvent, PIT38Result


def _fmt(v) -> str:
    d = Decimal(str(v))
    return f"{d:,.2f}"


def _fmt2(v) -> str:
    """Format for PIT-38 form fields (2 decimal places, no thousands separator)."""
    d = Decimal(str(v))
    return str(d.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP))


def _fmt_rate(v) -> str:
    """Format NBP rate (4 decimal places)."""
    if v is None:
        return "—"
    d = Decimal(str(v))
    return str(d.quantize(Decimal("0.0001"), rounding=ROUND_HALF_UP))


def _categorize_cost(event: CostPoolEvent) -> str:
    """Assign a human-readable category to a cost event."""
    if "salary" in event.source:
        return "Salary (USDC)"
    if "purchase" in event.source:
        exchange = event.source.split("_")[0].upper()
        return f"Fiat purchases ({exchange})"
    if event.price_method.endswith("_fee"):
        return "Trading fees"
    if "deposit" in event.notes.lower() if event.notes else False:
        return "Stablecoin deposits"
    if "buy" in event.notes.lower() if event.notes else False:
        return "Crypto purchases"
    return "Other"


def generate_pit38_report(
    result: PIT38Result,
    output_path: str | None = None,
) -> str:
    """Generate a PIT-38 markdown report for one tax year with full traceability."""

    year = result.year
    lines: list[str] = []
    lines.append(f"# PIT-38 Crypto Tax Report -- {year}")
    lines.append("")
    lines.append(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    lines.append(f"Method: **Polish annual cost pooling** (Art. 22 ust. 14-16, Art. 30b ust. 1a-1b)")
    lines.append("")

    # PIT-38 Section E fields
    # Field numbers differ by year: 2023-2024 use poz. 34-38, 2025 uses poz. 36-40
    if year <= 2024:
        poz_rev, poz_cost, poz_prior, poz_income, poz_carry = 34, 35, 36, 37, 38
    else:
        poz_rev, poz_cost, poz_prior, poz_income, poz_carry = 36, 37, 38, 39, 40

    lines.append("## PIT-38 Section E -- Virtual Currency (waluta wirtualna)")
    lines.append("")
    lines.append("| PIT-38 Field | Description | Amount (PLN) |")
    lines.append("| ---: | --- | ---: |")
    lines.append(f"| **Poz. {poz_rev}** | Revenue from crypto disposals (przychody z odplatnego zbycia walut wirtualnych) | **{_fmt(result.revenue_pln)}** |")
    lines.append(f"| **Poz. {poz_cost}** | Costs incurred in {year} (koszty uzyskania przychodow poniesione w roku podatkowym) | **{_fmt(result.costs_current_year_pln)}** |")
    lines.append(f"| **Poz. {poz_prior}** | Costs from prior years (koszty z lat ubieglych nieodliczone) | **{_fmt(result.costs_prior_years_pln)}** |")

    total_costs = result.costs_current_year_pln + result.costs_prior_years_pln
    if result.income_pln > 0:
        lines.append(f"| **Poz. {poz_income}** | Income / dochod (poz.{poz_rev} - poz.{poz_cost} - poz.{poz_prior}) | **{_fmt(result.income_pln)}** |")
        lines.append(f"| Poz. {poz_carry} | Undeducted costs (carry forward) | 0.00 |")
    else:
        lines.append(f"| Poz. {poz_income} | Income / dochod | 0.00 |")
        lines.append(f"| **Poz. {poz_carry}** | **Undeducted costs to carry forward** (koszty nieodliczone) | **{_fmt(result.carry_forward_pln)}** |")
    lines.append("")

    # Tax calculation
    lines.append("## Tax Calculation")
    lines.append("")
    lines.append("| Item | Amount |")
    lines.append("| --- | ---: |")
    lines.append(f"| Tax base (podstawa obliczenia podatku) | {_fmt(result.income_pln)} PLN |")
    lines.append(f"| Tax rate (stawka podatku) | 19% |")
    lines.append(f"| **Tax due (podatek nalezny)** | **{_fmt(result.tax_due_pln)} PLN** |")
    lines.append("")

    # Summary explanation
    lines.append("## How This Was Calculated")
    lines.append("")
    lines.append(f"- **{result.disposal_count}** taxable disposal events (crypto -> fiat)")
    lines.append(f"- Revenue: all fiat received from selling crypto = **{_fmt(result.revenue_pln)} PLN**")
    lines.append(f"- Costs this year: all fiat spent acquiring crypto (incl. salary USDC) = **{_fmt(result.costs_current_year_pln)} PLN**")
    lines.append(f"- Costs from prior years: undeducted carry-forward = **{_fmt(result.costs_prior_years_pln)} PLN**")
    lines.append(f"- Total costs: {_fmt(total_costs)} PLN")
    if result.income_pln > 0:
        lines.append(f"- Income: {_fmt(result.revenue_pln)} - {_fmt(total_costs)} = **{_fmt(result.income_pln)} PLN**")
        lines.append(f"- Tax: {_fmt(result.income_pln)} x 19% = **{_fmt(result.tax_due_pln)} PLN**")
    else:
        lines.append(f"- Costs exceed revenue: income = 0, no tax due")
        lines.append(f"- Excess costs of **{_fmt(result.carry_forward_pln)} PLN** carry forward to {year + 1}")
    lines.append("")

    # === VERIFICATION SECTION ===
    lines.append("---")
    lines.append("")
    lines.append("## Verification: Cost Breakdown by Category")
    lines.append("")

    # Categorize costs
    category_totals: dict[str, Decimal] = defaultdict(Decimal)
    category_counts: dict[str, int] = defaultdict(int)
    for e in result.cost_events:
        cat = _categorize_cost(e)
        category_totals[cat] += e.pln_value
        category_counts[cat] += 1

    lines.append("| Category | Count | Total (PLN) |")
    lines.append("| --- | ---: | ---: |")
    for cat in sorted(category_totals.keys()):
        lines.append(f"| {cat} | {category_counts[cat]} | {_fmt(category_totals[cat])} |")
    lines.append(f"| **TOTAL (= Poz. {poz_cost})** | **{sum(category_counts.values())}** | **{_fmt(result.costs_current_year_pln)}** |")
    lines.append("")

    # Revenue breakdown by source
    lines.append("## Verification: Revenue Breakdown by Source")
    lines.append("")
    source_rev: dict[str, Decimal] = defaultdict(Decimal)
    source_rev_count: dict[str, int] = defaultdict(int)
    for e in result.revenue_events:
        source_rev[e.source] += e.pln_value
        source_rev_count[e.source] += 1
    lines.append("| Source | Count | Total (PLN) |")
    lines.append("| --- | ---: | ---: |")
    for src in sorted(source_rev.keys()):
        lines.append(f"| {src} | {source_rev_count[src]} | {_fmt(source_rev[src])} |")
    lines.append(f"| **TOTAL (= Poz. {poz_rev})** | **{sum(source_rev_count.values())}** | **{_fmt(result.revenue_pln)}** |")
    lines.append("")

    # Revenue breakdown by asset
    asset_rev: dict[str, Decimal] = defaultdict(Decimal)
    asset_rev_count: dict[str, int] = defaultdict(int)
    for e in result.revenue_events:
        asset_rev[e.asset] += e.pln_value
        asset_rev_count[e.asset] += 1
    if len(asset_rev) > 1:
        lines.append("## Verification: Revenue Breakdown by Asset")
        lines.append("")
        lines.append("| Asset | Count | Total (PLN) |")
        lines.append("| --- | ---: | ---: |")
        for asset in sorted(asset_rev.keys()):
            lines.append(f"| {asset} | {asset_rev_count[asset]} | {_fmt(asset_rev[asset])} |")
        lines.append(f"| **TOTAL** | **{sum(asset_rev_count.values())}** | **{_fmt(result.revenue_pln)}** |")
        lines.append("")

    # === DETAILED REVENUE EVENTS ===
    lines.append("---")
    lines.append("")
    lines.append("## Revenue Events (Crypto -> Fiat Disposals)")
    lines.append("")
    if result.revenue_events:
        lines.append("| # | Date | Source | Tx ID | Asset | Amount | Counterparty | CP Amount | NBP Rate | Rate Date | Revenue (PLN) |")
        lines.append("| ---: | --- | --- | --- | --- | ---: | --- | ---: | ---: | --- | ---: |")
        for i, e in enumerate(sorted(result.revenue_events, key=lambda x: x.date), 1):
            tx_id_short = e.source_tx_id[:16] if e.source_tx_id else "—"
            lines.append(
                f"| {i} | {e.date} | {e.source} | {tx_id_short} | {e.asset} | {e.amount.normalize()} | "
                f"{e.counterparty_asset} | {e.counterparty_amount.normalize()} | "
                f"{_fmt_rate(e.nbp_rate)} {e.nbp_currency}/PLN | {e.nbp_rate_date} | "
                f"{_fmt(e.pln_value)} |"
            )
        lines.append("")
        lines.append(f"**Revenue total: {_fmt(result.revenue_pln)} PLN** (sum of all rows above)")
        lines.append("")
    else:
        lines.append("No taxable disposals in this year.")
        lines.append("")

    # === DETAILED COST EVENTS ===
    lines.append("## Cost Events (Crypto Acquisitions)")
    lines.append("")
    if result.cost_events:
        lines.append("| # | Date | Source | Tx ID | Category | Asset | Amount | NBP Rate | Rate Date | Cost (PLN) | Notes |")
        lines.append("| ---: | --- | --- | --- | --- | --- | ---: | ---: | --- | ---: | --- |")
        for i, e in enumerate(sorted(result.cost_events, key=lambda x: x.date), 1):
            tx_id_short = e.source_tx_id[:16] if e.source_tx_id else "—"
            cat = _categorize_cost(e)
            lines.append(
                f"| {i} | {e.date} | {e.source} | {tx_id_short} | {cat} | {e.asset} | {e.amount.normalize()} | "
                f"{_fmt_rate(e.nbp_rate)} {e.nbp_currency}/PLN | {e.nbp_rate_date} | "
                f"{_fmt(e.pln_value)} | {e.notes} |"
            )
        lines.append("")
        lines.append(f"**Cost total: {_fmt(result.costs_current_year_pln)} PLN** (sum of all rows above)")
        lines.append("")
    else:
        lines.append("No acquisition costs in this year.")
        lines.append("")

    # === VERIFICATION CHECKSUM ===
    lines.append("---")
    lines.append("")
    lines.append("## Verification Checksum")
    lines.append("")
    revenue_sum = sum(e.pln_value for e in result.revenue_events)
    cost_sum = sum(e.pln_value for e in result.cost_events)
    lines.append("| Check | Expected | Computed | Match |")
    lines.append("| --- | ---: | ---: | --- |")
    rev_match = "YES" if revenue_sum == result.revenue_pln else "**NO**"
    cost_match = "YES" if cost_sum == result.costs_current_year_pln else "**NO**"
    lines.append(f"| Sum of revenue events = Poz. {poz_rev} | {_fmt(result.revenue_pln)} | {_fmt(revenue_sum)} | {rev_match} |")
    lines.append(f"| Sum of cost events = Poz. {poz_cost} | {_fmt(result.costs_current_year_pln)} | {_fmt(cost_sum)} | {cost_match} |")
    if result.income_pln > 0:
        expected_income = result.revenue_pln - result.costs_current_year_pln - result.costs_prior_years_pln
        income_match = "YES" if expected_income == result.income_pln else "**NO**"
        lines.append(f"| Poz. {poz_rev} - Poz. {poz_cost} - Poz. {poz_prior} = Poz. {poz_income} | {_fmt(result.income_pln)} | {_fmt(expected_income)} | {income_match} |")
    else:
        expected_carry = result.costs_current_year_pln + result.costs_prior_years_pln - result.revenue_pln
        carry_match = "YES" if expected_carry == result.carry_forward_pln else "**NO**"
        lines.append(f"| Poz. {poz_cost} + Poz. {poz_prior} - Poz. {poz_rev} = Poz. {poz_carry} | {_fmt(result.carry_forward_pln)} | {_fmt(expected_carry)} | {carry_match} |")
    lines.append("")

    # Notes
    lines.append("## Legal Basis")
    lines.append("")
    lines.append("- **Method**: Annual cost pooling per Art. 22 ust. 14-16, Art. 30b ust. 1a-1b ustawy o PIT")
    lines.append("- **No FIFO**: Polish law does not require FIFO matching for crypto (Art. 30b ust. 7-7a does not apply to Art. 30b ust. 1a)")
    lines.append("- **Crypto-to-crypto swaps**: NOT taxable (Art. 17 ust. 1f excludes exchange between virtual currencies)")
    lines.append("- **Cost carry-forward**: Unlimited duration, no 50% annual cap (Art. 22 ust. 15-16)")
    lines.append("- **Rate**: NBP mid-rate from last business day before transaction (Art. 11a ust. 1-2)")
    lines.append("- **Stablecoins (USDC/USDT)**: Treated as waluta wirtualna (KIS interpretation, confirmed post-MiCA)")
    lines.append("")

    # How to verify
    lines.append("## How to Verify This Report")
    lines.append("")
    lines.append("1. **Revenue events**: Each row shows the exchange transaction. Find the Tx ID in your Kraken/Binance export CSV to confirm the asset, amount, and counterparty.")
    lines.append("2. **NBP rates**: Each row shows the exact rate used and the date it's from (last business day before transaction). Verify at https://api.nbp.pl/api/exchangerates/rates/a/{CURRENCY}/{RATE_DATE}/?format=json")
    lines.append("3. **PLN calculation**: Counterparty Amount x NBP Rate = PLN Value (check any row)")
    lines.append("4. **Salary costs**: Cross-reference with Polygon payment records in docs/crypto-transactions/2025-polygon-payments.txt")
    lines.append("5. **Stablecoin deposits**: These are USDC/USDT deposited to exchanges before selling. The cost basis is the NBP USD rate at deposit time.")
    lines.append("6. **Checksums**: The verification table above confirms that individual events sum to the PIT-38 field totals.")
    lines.append("")

    report = "\n".join(lines)

    if output_path:
        os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(report)

    return report
