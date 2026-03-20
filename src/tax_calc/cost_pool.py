"""Polish PIT-38 cost pool engine.

Poland does NOT use FIFO for crypto. Instead it uses annual cost pooling:
- Sum ALL fiat spent acquiring crypto in the year = costs (Art. 22 ust. 14-16)
- Sum ALL fiat received from crypto disposals in the year = revenue (Art. 17 ust. 1 pkt 11)
- If costs > revenue: income = 0, excess costs carry forward (Art. 22 ust. 15-16)
- If revenue > costs: income = revenue - costs, taxed at 19% (Art. 30b ust. 1a)

No per-transaction gain/loss matching. No lot tracking. Just annual aggregates.
"""
from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass, field
from decimal import Decimal, ROUND_HALF_UP
from typing import Any

from tax_calc.constants import FIAT, IGNORED_TX_TYPES, is_fiat, is_stablecoin
from tax_calc.models import FIFOLot, fmt, fmt_full
from tax_calc.prices import PriceResolver


@dataclass
class CostPoolEvent:
    """A single revenue or cost event for the cost pool."""
    date: str
    event_type: str  # "revenue" or "cost"
    asset: str
    amount: Decimal
    pln_value: Decimal
    price_method: str
    source: str
    counterparty_asset: str = ""
    counterparty_amount: Decimal = Decimal("0")
    notes: str = ""

    def to_dict(self) -> dict[str, str]:
        return {
            "date": self.date,
            "event_type": self.event_type,
            "asset": self.asset,
            "amount": fmt_full(self.amount),
            "pln_value": fmt(self.pln_value),
            "price_method": self.price_method,
            "source": self.source,
            "counterparty_asset": self.counterparty_asset,
            "counterparty_amount": fmt_full(self.counterparty_amount),
            "notes": self.notes,
        }


@dataclass
class YearlyPool:
    """Annual cost pool for PIT-38 Section E."""
    year: int
    revenue_events: list[CostPoolEvent] = field(default_factory=list)
    cost_events: list[CostPoolEvent] = field(default_factory=list)
    fee_costs: list[CostPoolEvent] = field(default_factory=list)

    @property
    def total_revenue(self) -> Decimal:
        return sum(e.pln_value for e in self.revenue_events)

    @property
    def total_costs(self) -> Decimal:
        return sum(e.pln_value for e in self.cost_events) + sum(e.pln_value for e in self.fee_costs)

    @property
    def disposal_count(self) -> int:
        return len(self.revenue_events)


@dataclass
class PIT38Result:
    """Complete PIT-38 Section E result for one year."""
    year: int
    # Poz. 34/36: revenue from crypto disposals
    revenue_pln: Decimal
    # Poz. 35/37: costs incurred in this year
    costs_current_year_pln: Decimal
    # Poz. 36/38: costs carried forward from prior years
    costs_prior_years_pln: Decimal
    # Poz. 37/39: income (revenue - total costs, min 0)
    income_pln: Decimal
    # Poz. 38/40: undeducted costs to carry forward
    carry_forward_pln: Decimal
    # Tax at 19%
    tax_due_pln: Decimal
    # Detail
    disposal_count: int
    revenue_events: list[CostPoolEvent]
    cost_events: list[CostPoolEvent]
    warnings: list[str]

    def to_dict(self) -> dict:
        return {
            "year": self.year,
            "revenue_pln": fmt(self.revenue_pln),
            "costs_current_year_pln": fmt(self.costs_current_year_pln),
            "costs_prior_years_pln": fmt(self.costs_prior_years_pln),
            "income_pln": fmt(self.income_pln),
            "carry_forward_pln": fmt(self.carry_forward_pln),
            "tax_due_pln": fmt(self.tax_due_pln),
            "disposal_count": self.disposal_count,
            "revenue_events": [e.to_dict() for e in self.revenue_events],
            "cost_events": [e.to_dict() for e in self.cost_events],
        }


def process_cost_pool(
    rows: list[dict[str, str]],
    prices: PriceResolver,
    salary_lots: list[FIFOLot] | None = None,
    pre_residency_costs: Decimal = Decimal("0"),
    first_polish_year: int = 2023,
) -> dict[str, Any]:
    """Process the normalized ledger using Polish annual cost pooling.

    Args:
        rows: Normalized transaction dicts
        prices: PriceResolver for PLN conversions
        salary_lots: Salary USDC payments (become costs in the year received)
        pre_residency_costs: Total PLN value of crypto purchased before Polish residency
        first_polish_year: First year of Polish tax residency (for pre-residency costs)
    """
    pools: dict[int, YearlyPool] = defaultdict(lambda: YearlyPool(year=0))
    warnings: list[str] = []

    # Inject salary USDC as cost events (valued at receipt = already taxed as income)
    if salary_lots:
        for lot in salary_lots:
            year = int(lot.date[:4])
            if pools[year].year == 0:
                pools[year].year = year
            pools[year].cost_events.append(CostPoolEvent(
                date=lot.date, event_type="cost", asset="USDC",
                amount=lot.amount, pln_value=lot.cost_pln,
                price_method="nbp_usd_salary", source="polygon_salary",
                notes=f"Salary USDC {lot.amount} @ {fmt(lot.cost_pln)} PLN",
            ))

    for row in rows:
        tx_type = row["tx_type"]
        asset = row["asset"]
        amount = _dec(row["amount"])
        fee = _dec(row.get("fee", "0"))
        fee_asset = row.get("fee_asset", "")
        cp_asset = row.get("counterparty_asset", "")
        cp_amount = _dec(row.get("counterparty_amount", "0"))
        date_iso = row["date"]
        date_str = date_iso[:10]
        year = int(date_str[:4])
        source = row.get("source", "")

        if pools[year].year == 0:
            pools[year].year = year

        if tx_type in IGNORED_TX_TYPES:
            continue

        # === REVENUE EVENTS (crypto -> fiat) ===
        if tx_type == "sell" and not is_fiat(asset):
            revenue_pln, method = prices.resolve(
                asset, amount, cp_asset, cp_amount, date_str)
            pools[year].revenue_events.append(CostPoolEvent(
                date=date_str, event_type="revenue", asset=asset,
                amount=amount, pln_value=revenue_pln, price_method=method,
                source=source, counterparty_asset=cp_asset,
                counterparty_amount=cp_amount,
            ))
            # Sale fees are deductible disposal costs
            if fee and fee_asset and is_fiat(fee_asset):
                fee_pln_rate = prices.nbp.get_rate(fee_asset, date_str)
                if fee_pln_rate:
                    pools[year].fee_costs.append(CostPoolEvent(
                        date=date_str, event_type="cost", asset=fee_asset,
                        amount=fee, pln_value=fee * fee_pln_rate,
                        price_method=f"nbp_{fee_asset.lower()}_fee", source=source,
                        notes=f"Trading fee {fee} {fee_asset}",
                    ))

        # === COST EVENTS (fiat -> crypto purchases) ===
        elif tx_type == "buy":
            # Fiat spent to buy crypto = deductible cost
            if cp_asset and is_fiat(cp_asset) and cp_amount > 0:
                cost_pln, method = prices.resolve(
                    asset, amount, cp_asset, cp_amount, date_str)
                pools[year].cost_events.append(CostPoolEvent(
                    date=date_str, event_type="cost", asset=asset,
                    amount=amount, pln_value=cost_pln, price_method=method,
                    source=source, counterparty_asset=cp_asset,
                    counterparty_amount=cp_amount,
                    notes=f"Buy {amount} {asset} for {cp_amount} {cp_asset}",
                ))
                # Purchase fees
                if fee and fee_asset and is_fiat(fee_asset):
                    fee_pln_rate = prices.nbp.get_rate(fee_asset, date_str)
                    if fee_pln_rate:
                        pools[year].fee_costs.append(CostPoolEvent(
                            date=date_str, event_type="cost", asset=fee_asset,
                            amount=fee, pln_value=fee * fee_pln_rate,
                            price_method=f"nbp_{fee_asset.lower()}_fee", source=source,
                            notes=f"Trading fee {fee} {fee_asset}",
                        ))

        # === STABLECOIN DEPOSIT = cost (valued at NBP USD rate) ===
        elif tx_type == "deposit" and is_stablecoin(asset):
            pln_value, method = prices.stablecoin_pln_value(amount, date_str)
            pools[year].cost_events.append(CostPoolEvent(
                date=date_str, event_type="cost", asset=asset,
                amount=amount, pln_value=pln_value, price_method=method,
                source=source,
                notes=f"Stablecoin deposit {amount} {asset}",
            ))

        # === NON-TAXABLE EVENTS (crypto-to-crypto, transfers, etc.) ===
        # swap_in, swap_out, withdrawal, deposit (non-stablecoin),
        # staking_reward, earn_reward, interest, airdrop, token_swap,
        # conversion, fee — all non-taxable at this stage.
        # Crypto-to-crypto swap fees are NOT deductible (Art. 23 ust. 1 pkt 38d).

    # Build PIT-38 results year by year
    carry_forward = pre_residency_costs
    results: dict[int, PIT38Result] = {}

    for year in sorted(pools.keys()):
        pool = pools[year]
        revenue = pool.total_revenue
        costs_current = pool.total_costs

        # For the first Polish year, add pre-residency costs
        costs_prior = carry_forward

        total_costs = costs_current + costs_prior
        if revenue > total_costs:
            income = revenue - total_costs
            new_carry = Decimal("0")
        else:
            income = Decimal("0")
            new_carry = total_costs - revenue

        tax = income * Decimal("0.19")

        results[year] = PIT38Result(
            year=year,
            revenue_pln=revenue,
            costs_current_year_pln=costs_current,
            costs_prior_years_pln=costs_prior,
            income_pln=income,
            carry_forward_pln=new_carry,
            tax_due_pln=tax,
            disposal_count=pool.disposal_count,
            revenue_events=pool.revenue_events,
            cost_events=pool.cost_events + pool.fee_costs,
            warnings=warnings,
        )

        carry_forward = new_carry

    return {
        "yearly_results": results,
        "warnings": warnings,
    }


def _dec(v: str) -> Decimal:
    try:
        return Decimal(v.strip())
    except Exception:
        return Decimal("0")
