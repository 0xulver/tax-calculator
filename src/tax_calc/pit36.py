"""PIT-36 personal income calculator for pre-JDG USDC salary payments.

Calculates tax on USDC salary received before JDG establishment,
classified as personal services income (Art. 13 pkt 8 ustawy o PIT).

Progressive tax scale (2025):
  - 12% on income up to 120,000 PLN
  - 32% on income above 120,000 PLN
  - 30,000 PLN kwota wolna (tax-free amount)
"""
from __future__ import annotations

import os
from dataclasses import dataclass, field
from datetime import datetime
from decimal import Decimal, ROUND_HALF_UP

from tax_calc.models import FIFOLot


# 2024-2025 tax scale constants
KWOTA_WOLNA = Decimal("30000")
BRACKET_THRESHOLD = Decimal("120000")
RATE_LOW = Decimal("0.12")
RATE_HIGH = Decimal("0.32")
COST_DEDUCTION_RATE = Decimal("0.20")  # 20% koszty uzyskania for umowa zlecenie


def _fmt(v) -> str:
    d = Decimal(str(v))
    return f"{d:,.2f}"


def _fmt_rate(v) -> str:
    if v is None:
        return "—"
    d = Decimal(str(v))
    return str(d.quantize(Decimal("0.0001"), rounding=ROUND_HALF_UP))


@dataclass
class SalaryPayment:
    """A single USDC salary payment with full traceability."""
    date: str
    usdc_amount: Decimal
    nbp_usd_rate: Decimal
    nbp_rate_date: str
    pln_value: Decimal
    tx_hash: str = ""


@dataclass
class PIT36Result:
    """Complete PIT-36 calculation for pre-JDG USDC salary income."""
    year: int
    payments: list[SalaryPayment]
    total_usdc: Decimal
    gross_income_pln: Decimal          # przychod
    cost_deduction_pln: Decimal        # koszty uzyskania (20%)
    taxable_income_pln: Decimal        # dochod (przychod - koszty)
    tax_base_pln: Decimal              # podstawa obliczenia (dochod - kwota wolna)
    tax_due_pln: Decimal               # podatek nalezny
    kwota_wolna_used: Decimal           # how much kwota wolna was applied
    monthly_advances_due: list[dict]    # zaliczki miesięczne


def calculate_pit36(
    salary_lots: list[FIFOLot],
    year: int = 2025,
) -> PIT36Result:
    """Calculate PIT-36 tax on USDC salary payments.

    Args:
        salary_lots: FIFOLot objects from parse_salary_payments() for the given year
        year: Tax year
    """
    # Filter to the requested year
    year_lots = [lot for lot in salary_lots if lot.date.startswith(str(year))]

    # Build payment details
    payments: list[SalaryPayment] = []
    for lot in year_lots:
        # Reconstruct rate from lot data
        rate = lot.cost_pln / lot.amount if lot.amount else Decimal("0")
        payments.append(SalaryPayment(
            date=lot.date,
            usdc_amount=lot.amount,
            nbp_usd_rate=rate,
            nbp_rate_date="",  # filled from NBP cache if available
            pln_value=lot.cost_pln,
            tx_hash=getattr(lot, 'source_tx_id', ''),
        ))

    payments.sort(key=lambda p: p.date)

    total_usdc = sum(p.usdc_amount for p in payments)
    gross_income = sum(p.pln_value for p in payments)

    # 20% cost deduction (Art. 22 ust. 9 pkt 4)
    cost_deduction = (gross_income * COST_DEDUCTION_RATE).quantize(
        Decimal("0.01"), rounding=ROUND_HALF_UP)

    taxable_income = gross_income - cost_deduction

    # Apply kwota wolna (tax-free amount)
    kwota_wolna_used = min(KWOTA_WOLNA, taxable_income)
    tax_base = max(Decimal("0"), taxable_income - kwota_wolna_used)
    # Round down to full PLN (Art. 27 ust. 1)
    tax_base = tax_base.quantize(Decimal("1"), rounding=ROUND_HALF_UP)

    # Progressive tax calculation
    if tax_base <= BRACKET_THRESHOLD - KWOTA_WOLNA:
        tax_due = (tax_base * RATE_LOW).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
    else:
        low_portion = BRACKET_THRESHOLD - KWOTA_WOLNA
        high_portion = tax_base - low_portion
        tax_due = (
            low_portion * RATE_LOW + high_portion * RATE_HIGH
        ).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

    # Round to full PLN
    tax_due = tax_due.quantize(Decimal("1"), rounding=ROUND_HALF_UP)

    # Monthly advance payments (zaliczki)
    monthly_advances = _calculate_monthly_advances(payments)

    return PIT36Result(
        year=year,
        payments=payments,
        total_usdc=total_usdc,
        gross_income_pln=gross_income,
        cost_deduction_pln=cost_deduction,
        taxable_income_pln=taxable_income,
        tax_base_pln=tax_base,
        tax_due_pln=tax_due,
        kwota_wolna_used=kwota_wolna_used,
        monthly_advances_due=monthly_advances,
    )


def _calculate_monthly_advances(payments: list[SalaryPayment]) -> list[dict]:
    """Calculate monthly advance tax payments (zaliczki).

    Under Art. 44 ust. 1a, taxpayers receiving income from foreign payers
    must pay monthly advances by the 20th of the following month.
    """
    # Group payments by month
    monthly_income: dict[str, Decimal] = {}
    for p in payments:
        month_key = p.date[:7]  # "2025-01"
        monthly_income.setdefault(month_key, Decimal("0"))
        monthly_income[month_key] += p.pln_value

    advances = []
    cumulative_income = Decimal("0")
    cumulative_tax = Decimal("0")

    for month in sorted(monthly_income.keys()):
        income = monthly_income[month]
        cumulative_income += income

        # Cumulative cost deduction
        cum_cost = (cumulative_income * COST_DEDUCTION_RATE).quantize(
            Decimal("0.01"), rounding=ROUND_HALF_UP)
        cum_taxable = cumulative_income - cum_cost

        # Apply kwota wolna
        cum_base = max(Decimal("0"), cum_taxable - KWOTA_WOLNA)
        cum_base = cum_base.quantize(Decimal("1"), rounding=ROUND_HALF_UP)

        # Progressive tax on cumulative base
        if cum_base <= BRACKET_THRESHOLD - KWOTA_WOLNA:
            cum_tax_total = (cum_base * RATE_LOW).quantize(Decimal("1"), rounding=ROUND_HALF_UP)
        else:
            low_portion = BRACKET_THRESHOLD - KWOTA_WOLNA
            high_portion = cum_base - low_portion
            cum_tax_total = (
                low_portion * RATE_LOW + high_portion * RATE_HIGH
            ).quantize(Decimal("1"), rounding=ROUND_HALF_UP)

        # This month's advance = cumulative tax - previously paid
        advance = cum_tax_total - cumulative_tax
        cumulative_tax = cum_tax_total

        # Parse month for due date
        year_str, month_str = month.split("-")
        month_num = int(month_str)
        if month_num == 12:
            due_date = f"{int(year_str) + 1}-01-20"
        else:
            due_date = f"{year_str}-{month_num + 1:02d}-20"

        advances.append({
            "month": month,
            "income_pln": income,
            "cumulative_income_pln": cumulative_income,
            "advance_pln": advance,
            "due_date": due_date,
        })

    return advances


def generate_pit36_report(result: PIT36Result, output_path: str | None = None) -> str:
    """Generate a PIT-36 markdown report for pre-JDG USDC salary income."""

    lines: list[str] = []
    lines.append(f"# PIT-36 Personal Income Report -- {result.year}")
    lines.append("")
    lines.append(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    lines.append(f"Income type: **Personal services (Art. 13 pkt 8 ustawy o PIT)**")
    lines.append(f"Source: USDC salary payments on Polygon blockchain (pre-JDG)")
    lines.append("")

    # Summary
    lines.append("## Tax Calculation Summary")
    lines.append("")
    lines.append("| Item | Amount |")
    lines.append("| --- | ---: |")
    lines.append(f"| Total USDC received | {_fmt(result.total_usdc)} USDC |")
    lines.append(f"| **Gross income (przychod)** | **{_fmt(result.gross_income_pln)} PLN** |")
    lines.append(f"| Cost deduction 20% (koszty uzyskania) | -{_fmt(result.cost_deduction_pln)} PLN |")
    lines.append(f"| **Taxable income (dochod)** | **{_fmt(result.taxable_income_pln)} PLN** |")
    lines.append(f"| Kwota wolna (tax-free amount) | -{_fmt(result.kwota_wolna_used)} PLN |")
    lines.append(f"| **Tax base (podstawa obliczenia)** | **{_fmt(result.tax_base_pln)} PLN** |")
    lines.append(f"| Tax rate | 12% (up to 120K) / 32% (above 120K) |")
    lines.append(f"| **Tax due (podatek nalezny)** | **{_fmt(result.tax_due_pln)} PLN** |")
    lines.append("")

    # Tax calculation detail
    lines.append("## Tax Calculation Detail")
    lines.append("")
    if result.tax_base_pln <= BRACKET_THRESHOLD - KWOTA_WOLNA:
        tax_12 = result.tax_base_pln * RATE_LOW
        lines.append(f"- Entire tax base ({_fmt(result.tax_base_pln)} PLN) falls within the 12% bracket")
        lines.append(f"- Tax: {_fmt(result.tax_base_pln)} x 12% = **{_fmt(result.tax_due_pln)} PLN**")
    else:
        low_portion = BRACKET_THRESHOLD - KWOTA_WOLNA
        high_portion = result.tax_base_pln - low_portion
        tax_12 = low_portion * RATE_LOW
        tax_32 = high_portion * RATE_HIGH
        lines.append(f"- First {_fmt(low_portion)} PLN at 12% = {_fmt(tax_12)} PLN")
        lines.append(f"- Remaining {_fmt(high_portion)} PLN at 32% = {_fmt(tax_32)} PLN")
        lines.append(f"- Total: **{_fmt(result.tax_due_pln)} PLN**")
    lines.append("")

    # Note about JDG separation
    lines.append("> **Note**: JDG ryczalt income (PIT-28) is completely separate from PIT-36.")
    lines.append("> The two tax systems do not interact. JDG income does NOT push this")
    lines.append("> income into a higher bracket. (Art. 9 ust. 1a, Art. 30c ustawy o PIT)")
    lines.append("")

    # Payment details with traceability
    lines.append("---")
    lines.append("")
    lines.append("## Payment Details")
    lines.append("")
    lines.append("| # | Date | USDC Amount | NBP USD/PLN Rate | PLN Value | Polygon Tx |")
    lines.append("| ---: | --- | ---: | ---: | ---: | --- |")
    for i, p in enumerate(result.payments, 1):
        tx_short = p.tx_hash[:16] + "..." if p.tx_hash else "—"
        lines.append(
            f"| {i} | {p.date} | {_fmt(p.usdc_amount)} | {_fmt_rate(p.nbp_usd_rate)} | "
            f"{_fmt(p.pln_value)} | {tx_short} |"
        )
    lines.append(f"| | **TOTAL** | **{_fmt(result.total_usdc)}** | | **{_fmt(result.gross_income_pln)}** | |")
    lines.append("")

    # Verification
    lines.append("## Verification")
    lines.append("")
    payment_sum = sum(p.pln_value for p in result.payments)
    match = "YES" if payment_sum == result.gross_income_pln else "**NO**"
    lines.append(f"- Sum of payments = gross income: {_fmt(payment_sum)} = {_fmt(result.gross_income_pln)} -- {match}")
    lines.append(f"- Gross income x 20% = cost deduction: {_fmt(result.gross_income_pln)} x 0.20 = {_fmt(result.cost_deduction_pln)}")
    lines.append(f"- Gross - costs = taxable: {_fmt(result.gross_income_pln)} - {_fmt(result.cost_deduction_pln)} = {_fmt(result.taxable_income_pln)}")
    lines.append(f"- Taxable - kwota wolna = tax base: {_fmt(result.taxable_income_pln)} - {_fmt(result.kwota_wolna_used)} = {_fmt(result.tax_base_pln)}")
    lines.append("")
    lines.append("Each payment's PLN value = USDC amount x NBP USD mid-rate from last business day before payment date.")
    lines.append("Verify any rate at: `https://api.nbp.pl/api/exchangerates/rates/a/USD/{RATE_DATE}/?format=json`")
    lines.append("")

    # Monthly advance payments
    lines.append("---")
    lines.append("")
    lines.append("## Monthly Advance Payments (Zaliczki)")
    lines.append("")
    lines.append("Under Art. 44 ust. 1a, income from a foreign payer requires self-paid monthly advances by the 20th of the following month.")
    lines.append("")
    lines.append("| Month | Income (PLN) | Cumulative Income | Advance Due (PLN) | Due Date |")
    lines.append("| --- | ---: | ---: | ---: | --- |")
    total_advances = Decimal("0")
    for adv in result.monthly_advances_due:
        total_advances += adv["advance_pln"]
        lines.append(
            f"| {adv['month']} | {_fmt(adv['income_pln'])} | "
            f"{_fmt(adv['cumulative_income_pln'])} | "
            f"{_fmt(adv['advance_pln'])} | {adv['due_date']} |"
        )
    lines.append(f"| **TOTAL** | | | **{_fmt(total_advances)}** | |")
    lines.append("")

    if total_advances != result.tax_due_pln:
        diff = result.tax_due_pln - total_advances
        lines.append(f"Difference between total advances and annual tax: {_fmt(diff)} PLN")
        lines.append(f"(due to rounding in monthly vs annual calculation)")
        lines.append("")

    lines.append("**If advances were not paid monthly, interest accrues from each due date at ~14.5% annual rate.**")
    lines.append("")

    # Cross-reference to PIT-38
    lines.append("---")
    lines.append("")
    lines.append("## Cross-Reference: PIT-38 Cost Basis")
    lines.append("")
    lines.append(f"The same {_fmt(result.gross_income_pln)} PLN appears as **cost basis** on PIT-38")
    lines.append(f"(salary USDC acquisition costs). This is the barter doctrine: income taxed at")
    lines.append(f"receipt becomes the cost basis for later crypto disposal. When USDC is sold for")
    lines.append(f"EUR, the PIT-38 gain/loss is only the difference between the sale PLN value and")
    lines.append(f"this {_fmt(result.gross_income_pln)} PLN cost basis -- typically near zero.")
    lines.append("")

    report = "\n".join(lines)

    if output_path:
        os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(report)

    return report
