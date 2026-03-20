"""PIT-38 report generator using Polish annual cost pooling (not FIFO)."""
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


def generate_pit38_report(
    result: PIT38Result,
    output_path: str | None = None,
) -> str:
    """Generate a PIT-38 markdown report for one tax year using cost pool data."""

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

    # Revenue detail
    lines.append("## Revenue Events (Crypto -> Fiat Disposals)")
    lines.append("")
    if result.revenue_events:
        lines.append("| Date | Asset | Amount | Counterparty | CP Amount | Revenue (PLN) | Method |")
        lines.append("| --- | --- | ---: | --- | ---: | ---: | --- |")
        for e in sorted(result.revenue_events, key=lambda x: x.date):
            lines.append(
                f"| {e.date} | {e.asset} | {e.amount.normalize()} | "
                f"{e.counterparty_asset} | {e.counterparty_amount.normalize()} | "
                f"{_fmt(e.pln_value)} | {e.price_method} |"
            )
        lines.append("")
    else:
        lines.append("No taxable disposals in this year.")
        lines.append("")

    # Cost detail
    lines.append("## Cost Events (Crypto Acquisitions)")
    lines.append("")
    if result.cost_events:
        lines.append("| Date | Type | Asset | Amount | Cost (PLN) | Method | Notes |")
        lines.append("| --- | --- | --- | ---: | ---: | --- | --- |")
        for e in sorted(result.cost_events, key=lambda x: x.date):
            lines.append(
                f"| {e.date} | {e.source} | {e.asset} | {e.amount.normalize()} | "
                f"{_fmt(e.pln_value)} | {e.price_method} | {e.notes} |"
            )
        lines.append("")
    else:
        lines.append("No acquisition costs in this year.")
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

    report = "\n".join(lines)

    if output_path:
        os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(report)

    return report
