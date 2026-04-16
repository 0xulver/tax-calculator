"""PIT-28 ryczalt calculator for JDG income.

Calculates tax on JDG sole proprietorship income taxed under ryczalt
(flat-rate tax on gross revenue). For IT/software services: 12%.

Revenue recognition: Art. 14 ust. 1c -- earliest of service completion,
invoice date, or payment date. For monthly billing: Art. 14 ust. 1e
moves to last day of settlement period.

EUR to PLN: NBP mid-rate from last business day before revenue date
(Art. 11a ust. 1).
"""
from __future__ import annotations

import os
import re
import xml.etree.ElementTree as ET
from dataclasses import dataclass, field
from datetime import datetime
from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path
from typing import Optional

from tax_calc.nbp import NBPClient


RYCZALT_RATE = Decimal("0.12")  # 12% for IT services


@dataclass
class HealthInsuranceMonth:
    """Monthly health insurance contribution from ZUS DRA."""
    month: str           # YYYY-MM
    amount_pln: Decimal


def _fmt(v) -> str:
    d = Decimal(str(v))
    return f"{d:,.2f}"


def _fmt_rate(v) -> str:
    if v is None:
        return "—"
    d = Decimal(str(v))
    return str(d.quantize(Decimal("0.0001"), rounding=ROUND_HALF_UP))


@dataclass
class Invoice:
    """A single parsed invoice."""
    invoice_number: str
    issue_date: str          # YYYY-MM-DD
    amount_eur: Decimal
    currency: str = "EUR"
    file_path: str = ""


@dataclass
class RyczaltEntry:
    """An invoice with PLN conversion and tax calculation."""
    invoice: Invoice
    nbp_rate: Decimal
    nbp_rate_date: str
    amount_pln: Decimal
    month: str               # YYYY-MM for grouping


@dataclass
class PIT28Result:
    """Complete PIT-28 calculation for a tax year."""
    year: int
    entries: list[RyczaltEntry]
    total_eur: Decimal
    total_pln: Decimal
    tax_rate: Decimal
    tax_before_deduction_pln: Decimal
    health_insurance_paid: Decimal
    health_insurance_deduction: Decimal
    tax_due_pln: Decimal
    monthly_breakdown: list[dict]
    health_months: list[HealthInsuranceMonth] = field(default_factory=list)


def parse_clearstar_invoices(invoice_dir: str) -> list[Invoice]:
    """Parse Clearstar UBL XML invoices from a directory.

    Extracts IssueDate and PayableAmount from each XML file.
    """
    invoices: list[Invoice] = []
    invoice_path = Path(invoice_dir)

    if not invoice_path.exists():
        return invoices

    for xml_file in sorted(invoice_path.glob("*.xml")):
        try:
            tree = ET.parse(xml_file)
            root = tree.getroot()

            # Handle XML namespaces -- UBL uses namespaces heavily
            # Try to find elements with or without namespace
            ns = _detect_namespaces(root)

            issue_date = _find_text(root, "IssueDate", ns)
            payable_amount = _find_text(root, "PayableAmount", ns)

            if issue_date and payable_amount:
                # Extract invoice number from filename
                # Format: 2025-07-Jul_udr-20250602_2025-001_hash.xml
                inv_num = _extract_invoice_number(xml_file.name)

                invoices.append(Invoice(
                    invoice_number=inv_num,
                    issue_date=issue_date,
                    amount_eur=Decimal(payable_amount),
                    file_path=str(xml_file),
                ))
        except Exception as e:
            print(f"Warning: Could not parse {xml_file.name}: {e}")

    invoices.sort(key=lambda i: i.issue_date)
    return invoices


def _detect_namespaces(root: ET.Element) -> dict[str, str]:
    """Detect common UBL namespaces from root element."""
    ns = {}
    tag = root.tag
    if "{" in tag:
        default_ns = tag.split("}")[0] + "}"
        ns["default"] = default_ns
    return ns


def _find_text(root: ET.Element, local_name: str, ns: dict) -> Optional[str]:
    """Find element text by local name, handling namespaces."""
    # Try with namespace
    for elem in root.iter():
        tag = elem.tag
        if tag.endswith(local_name) or tag.endswith("}" + local_name):
            if elem.text:
                return elem.text.strip()
    return None


def _extract_invoice_number(filename: str) -> str:
    """Extract invoice number like '2025-001' from filename."""
    match = re.search(r"(\d{4}-\d{3})", filename)
    return match.group(1) if match else filename


def calculate_pit28(
    invoices: list[Invoice],
    nbp: NBPClient,
    year: int = 2025,
    health_insurance: list[HealthInsuranceMonth] | None = None,
) -> PIT28Result:
    """Calculate PIT-28 ryczalt tax for a given year.

    Args:
        invoices: Parsed invoices (will be filtered to the given year)
        nbp: NBP client for exchange rates
        year: Tax year
        health_insurance: Monthly health insurance contributions from ZUS DRA
    """
    entries: list[RyczaltEntry] = []

    for inv in invoices:
        inv_year = int(inv.issue_date[:4])
        if inv_year != year:
            continue

        rate, rate_date = nbp.get_rate_with_date("EUR", inv.issue_date)
        if rate is None:
            print(f"Warning: No NBP rate for {inv.issue_date}, skipping {inv.invoice_number}")
            continue

        amount_pln = (inv.amount_eur * rate).quantize(
            Decimal("0.01"), rounding=ROUND_HALF_UP)

        entries.append(RyczaltEntry(
            invoice=inv,
            nbp_rate=rate,
            nbp_rate_date=rate_date,
            amount_pln=amount_pln,
            month=inv.issue_date[:7],
        ))

    entries.sort(key=lambda e: e.invoice.issue_date)

    total_eur = sum(e.invoice.amount_eur for e in entries)
    total_pln = sum(e.amount_pln for e in entries)
    tax_before = (total_pln * RYCZALT_RATE).quantize(Decimal("1"), rounding=ROUND_HALF_UP)

    # Health insurance deduction (50% of paid skladka zdrowotna)
    health_months = health_insurance or []
    health_paid = sum(h.amount_pln for h in health_months)
    health_deduction = (health_paid * Decimal("0.5")).quantize(
        Decimal("0.01"), rounding=ROUND_HALF_UP)
    # Deduction cannot exceed tax
    health_deduction = min(health_deduction, tax_before)

    tax_due = tax_before - health_deduction
    tax_due = tax_due.quantize(Decimal("1"), rounding=ROUND_HALF_UP)

    # Monthly breakdown for advance payment verification
    monthly: dict[str, Decimal] = {}
    for e in entries:
        monthly.setdefault(e.month, Decimal("0"))
        monthly[e.month] += e.amount_pln

    monthly_breakdown = []
    for month in sorted(monthly.keys()):
        revenue = monthly[month]
        advance = (revenue * RYCZALT_RATE).quantize(Decimal("1"), rounding=ROUND_HALF_UP)
        # Due by 20th of following month
        year_str, month_str = month.split("-")
        month_num = int(month_str)
        if month_num == 12:
            due_date = f"{int(year_str) + 1}-01-20"
        else:
            due_date = f"{year_str}-{month_num + 1:02d}-20"

        monthly_breakdown.append({
            "month": month,
            "revenue_pln": revenue,
            "tax_advance": advance,
            "due_date": due_date,
        })

    return PIT28Result(
        year=year,
        entries=entries,
        total_eur=total_eur,
        total_pln=total_pln,
        tax_rate=RYCZALT_RATE,
        tax_before_deduction_pln=tax_before,
        health_insurance_paid=health_paid,
        health_insurance_deduction=health_deduction,
        tax_due_pln=tax_due,
        monthly_breakdown=monthly_breakdown,
        health_months=health_months,
    )


def generate_pit28_report(result: PIT28Result, output_path: str | None = None) -> str:
    """Generate a PIT-28 markdown report for JDG ryczalt income."""

    lines: list[str] = []
    lines.append(f"# PIT-28 Ryczalt Report -- {result.year}")
    lines.append("")
    lines.append(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    lines.append(f"Tax type: **Ryczalt od przychodow ewidencjonowanych (12% flat rate)**")
    lines.append(f"Activity: IT/software development services (PKWiU 62.01)")
    lines.append("")

    # Summary
    lines.append("## Tax Calculation Summary")
    lines.append("")
    lines.append("| Item | Amount |")
    lines.append("| --- | ---: |")
    lines.append(f"| Total invoiced (EUR) | {_fmt(result.total_eur)} EUR |")
    lines.append(f"| **Total revenue (PLN)** | **{_fmt(result.total_pln)} PLN** |")
    lines.append(f"| Ryczalt rate | {result.tax_rate * 100}% |")
    lines.append(f"| Tax before deduction | {_fmt(result.tax_before_deduction_pln)} PLN |")
    lines.append(f"| Health insurance paid (skladka zdrowotna) | {_fmt(result.health_insurance_paid)} PLN |")
    lines.append(f"| Health insurance deduction (50%) | -{_fmt(result.health_insurance_deduction)} PLN |")
    lines.append(f"| **Tax due (podatek nalezny)** | **{_fmt(result.tax_due_pln)} PLN** |")
    lines.append("")

    if result.health_months:
        lines.append("### Health Insurance Contributions (from ZUS DRA)")
        lines.append("")
        lines.append("| Month | Skladka zdrowotna |")
        lines.append("| --- | ---: |")
        for h in result.health_months:
            lines.append(f"| {h.month} | {_fmt(h.amount_pln)} |")
        lines.append(f"| **Total paid** | **{_fmt(result.health_insurance_paid)}** |")
        lines.append(f"| **50% deductible** | **{_fmt(result.health_insurance_deduction)}** |")
        lines.append("")
        lines.append("Source: ZUS DRA declarations, Section VI field 02")
        lines.append("")

    # Invoice details
    lines.append("---")
    lines.append("")
    lines.append("## Invoice Details")
    lines.append("")
    lines.append("| # | Invoice | Issue Date | EUR Amount | NBP EUR/PLN Rate | Rate Date | PLN Revenue |")
    lines.append("| ---: | --- | --- | ---: | ---: | --- | ---: |")
    for i, e in enumerate(result.entries, 1):
        lines.append(
            f"| {i} | {e.invoice.invoice_number} | {e.invoice.issue_date} | "
            f"{_fmt(e.invoice.amount_eur)} | {_fmt_rate(e.nbp_rate)} | "
            f"{e.nbp_rate_date} | {_fmt(e.amount_pln)} |"
        )
    lines.append(f"| | **TOTAL** | | **{_fmt(result.total_eur)}** | | | **{_fmt(result.total_pln)}** |")
    lines.append("")

    # Verification
    lines.append("## Verification")
    lines.append("")
    entry_sum = sum(e.amount_pln for e in result.entries)
    match = "YES" if entry_sum == result.total_pln else "**NO**"
    lines.append(f"- Sum of invoice PLN values = total revenue: {_fmt(entry_sum)} = {_fmt(result.total_pln)} -- {match}")
    lines.append(f"- Total revenue x {result.tax_rate * 100}% = tax before deduction: {_fmt(result.total_pln)} x {result.tax_rate} = {_fmt(result.tax_before_deduction_pln)}")
    lines.append(f"- Tax before deduction - health insurance deduction = tax due: {_fmt(result.tax_before_deduction_pln)} - {_fmt(result.health_insurance_deduction)} = {_fmt(result.tax_due_pln)}")
    lines.append("")
    lines.append("Each EUR amount is converted using the NBP mid-rate from the last business day before the invoice issue date.")
    lines.append("Verify any rate at: `https://api.nbp.pl/api/exchangerates/rates/a/EUR/{RATE_DATE}/?format=json`")
    lines.append("")

    # Monthly breakdown
    lines.append("---")
    lines.append("")
    lines.append("## Monthly Tax Advances (Zaliczki)")
    lines.append("")
    lines.append("Under ryczalt, monthly advance tax is due by the 20th of the following month.")
    lines.append("")
    lines.append("| Month | Revenue (PLN) | Tax Advance (12%) | Due Date |")
    lines.append("| --- | ---: | ---: | --- |")
    total_advances = Decimal("0")
    for m in result.monthly_breakdown:
        total_advances += m["tax_advance"]
        lines.append(
            f"| {m['month']} | {_fmt(m['revenue_pln'])} | "
            f"{_fmt(m['tax_advance'])} | {m['due_date']} |"
        )
    lines.append(f"| **TOTAL** | **{_fmt(result.total_pln)}** | **{_fmt(total_advances)}** | |")
    lines.append("")

    if total_advances != result.tax_due_pln:
        diff = result.tax_due_pln - total_advances
        lines.append(f"Rounding difference between monthly sum and annual total: {_fmt(diff)} PLN")
        lines.append("")

    lines.append("Compare these monthly amounts against your actual payments to determine any remaining balance.")
    lines.append("")

    # Legal basis
    lines.append("---")
    lines.append("")
    lines.append("## Legal Basis")
    lines.append("")
    lines.append("- **Tax type**: Ryczalt od przychodow ewidencjonowanych (Art. 2 ust. 1 ustawy o zryczaltowanym podatku dochodowym)")
    lines.append("- **Rate**: 12% for IT services (Art. 12 ust. 1 pkt 2b lit. b)")
    lines.append("- **Revenue recognition**: Art. 14 ust. 1c ustawy o PIT (earliest of service completion, invoice date, payment date)")
    lines.append("- **EUR conversion**: NBP mid-rate from last business day before revenue date (Art. 11a ust. 1)")
    lines.append("- **No cost deductions**: Ryczalt is on gross revenue (Art. 12 ust. 2)")
    lines.append("- **Health insurance**: 50% of paid contributions deductible (Art. 11 ust. 1a) -- not included in this report")
    lines.append("- **Monthly advances**: Due by 20th of following month (Art. 21 ust. 1)")
    lines.append("- **Annual filing**: PIT-28, due by April 30 of following year")
    lines.append("")

    report = "\n".join(lines)

    if output_path:
        os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(report)

    return report
