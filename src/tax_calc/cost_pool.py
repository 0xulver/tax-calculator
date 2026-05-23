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

from tax_calc.constants import IGNORED_TX_TYPES, is_fiat, is_stablecoin
from tax_calc.models import FIFOLot, fmt, fmt_full
from tax_calc.prices import PriceResolver


def _fmt_plain(v: Decimal) -> str:
    """Format Decimal values for human-readable event notes."""
    if not isinstance(v, Decimal):
        v = Decimal(str(v))
    normalized = v.normalize()
    if normalized == normalized.to_integral():
        return format(normalized, "f")
    return format(normalized, "f").rstrip("0").rstrip(".")


POLICY_LEGACY_FULL_HISTORY = "legacy_full_history"
POLICY_SPLIT_YEAR_CONSERVATIVE = "split_year_conservative"
POLICY_SPLIT_YEAR_SUPPORTABLE = "split_year_supportable"
POLICY_SPLIT_YEAR_HIGH_RISK = "split_year_high_risk"

PIT38_POLICIES = (
    POLICY_LEGACY_FULL_HISTORY,
    POLICY_SPLIT_YEAR_CONSERVATIVE,
    POLICY_SPLIT_YEAR_SUPPORTABLE,
    POLICY_SPLIT_YEAR_HIGH_RISK,
)

POLICY_LABELS = {
    POLICY_LEGACY_FULL_HISTORY: "Legacy full-history Polish pool (audit/debug only)",
    POLICY_SPLIT_YEAR_CONSERVATIVE: "Split-year conservative: Layer A imported fiat costs only",
    POLICY_SPLIT_YEAR_SUPPORTABLE: "Split-year supportable: Layer A + Layer B same-token salary USDC",
    POLICY_SPLIT_YEAR_HIGH_RISK: "Split-year high-risk: Layers A + B + C successor basis",
}


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
    source_tx_id: str = ""
    nbp_rate: Decimal | None = None
    nbp_rate_date: str = ""
    nbp_currency: str = ""

    def to_dict(self) -> dict[str, str]:
        d = {
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
            "source_tx_id": self.source_tx_id,
        }
        if self.nbp_rate is not None:
            d["nbp_rate"] = fmt_full(self.nbp_rate)
            d["nbp_rate_date"] = self.nbp_rate_date
            d["nbp_currency"] = self.nbp_currency
        return d


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
    policy_name: str = POLICY_LEGACY_FULL_HISTORY
    policy_label: str = POLICY_LABELS[POLICY_LEGACY_FULL_HISTORY]
    polish_residency_start: str = ""
    costs_prior_breakdown: dict[str, Decimal] = field(default_factory=dict)

    def to_dict(self) -> dict:
        return {
            "year": self.year,
            "policy_name": self.policy_name,
            "policy_label": self.policy_label,
            "polish_residency_start": self.polish_residency_start,
            "revenue_pln": fmt(self.revenue_pln),
            "costs_current_year_pln": fmt(self.costs_current_year_pln),
            "costs_prior_years_pln": fmt(self.costs_prior_years_pln),
            "costs_prior_breakdown": {k: fmt(v) for k, v in self.costs_prior_breakdown.items()},
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
    *,
    policy: str = POLICY_LEGACY_FULL_HISTORY,
    polish_residency_start: str = "2023-04-12",
    imported_salary_usdc_costs: Decimal = Decimal("0"),
    imported_successor_costs: Decimal = Decimal("0"),
) -> dict[str, Any]:
    """Process the normalized ledger using Polish annual cost pooling.

    Args:
        rows: Normalized transaction dicts
        prices: PriceResolver for PLN conversions
        salary_lots: Salary USDC payments (become costs in the year received)
        pre_residency_costs: Layer A imported pre-residency fiat-purchase costs
        first_polish_year: First year of Polish tax residency (for imported costs)
        policy: Filing policy. Legacy includes all years; split-year policies start
            from polish_residency_start and import explicit Layer A/B/C costs.
        polish_residency_start: First day of Polish tax residency, YYYY-MM-DD.
        imported_salary_usdc_costs: Layer B imported same-token salary USDC basis.
        imported_successor_costs: Layer C imported successor basis through pre-move swaps.
    """
    if policy not in PIT38_POLICIES:
        raise ValueError(f"Unknown PIT-38 policy: {policy}")

    pools: dict[int, YearlyPool] = defaultdict(lambda: YearlyPool(year=0))
    warnings: list[str] = []
    excluded_counts: dict[str, int] = defaultdict(int)
    split_year = policy != POLICY_LEGACY_FULL_HISTORY
    start_year = int(polish_residency_start[:4]) if split_year else first_polish_year
    imported_prior_breakdown = _imported_prior_breakdown(
        policy=policy,
        imported_fiat_costs=pre_residency_costs,
        imported_salary_usdc_costs=imported_salary_usdc_costs,
        imported_successor_costs=imported_successor_costs,
    )
    imported_prior_total = sum(imported_prior_breakdown.values(), Decimal("0"))

    if split_year:
        warnings.append(
            f"Split-year policy active: rows before {polish_residency_start} are excluded "
            "from Polish PIT-38 revenue and current-year costs."
        )
        if imported_prior_total == 0:
            warnings.append(
                "No imported pre-residency costs supplied. This is conservative but may "
                "overstate PIT-38 tax until the move-date inventory is rebuilt."
            )
        if imported_salary_usdc_costs > 0 and policy in (
            POLICY_SPLIT_YEAR_SUPPORTABLE,
            POLICY_SPLIT_YEAR_HIGH_RISK,
        ):
            warnings.append(
                "Layer B salary-USDC imported cost is KIS-dependent and requires Swedish "
                "income-tax evidence plus same-token move-date provenance."
            )
        if imported_successor_costs > 0 and policy == POLICY_SPLIT_YEAR_HIGH_RISK:
            warnings.append(
                "Layer C successor-basis cost through pre-move crypto-to-crypto swaps is "
                "high risk and should remain separate from default filing numbers."
            )

    # Track which years have salary data -- stablecoin deposits in those years
    # should NOT be counted as costs (to avoid double-counting with salary lots)
    salary_years: set[int] = set()

    # Inject external lots (salary USDC, fiat purchases) as cost events
    if salary_lots:
        for lot in salary_lots:
            year = int(lot.date[:4])
            if split_year and lot.date < polish_residency_start:
                excluded_counts["pre_residency_salary_or_purchase_lots"] += 1
                continue
            if pools[year].year == 0:
                pools[year].year = year
            currency = getattr(lot, "fiat_currency", "USD")
            asset = getattr(lot, "asset", "USDC")
            rate, rate_date = prices.nbp.get_rate_with_date(currency, lot.date)
            # Only salary sources trigger stablecoin deposit dedup
            if "salary" in lot.source:
                salary_years.add(year)
            is_salary = "salary" in lot.source
            method = f"nbp_{currency.lower()}_salary" if is_salary else f"nbp_{currency.lower()}_purchase"
            label = f"Salary {asset} {lot.amount} @ {fmt(lot.cost_pln)} PLN" if is_salary else f"Purchase {lot.amount} {asset} = {fmt(lot.cost_pln)} PLN"
            pools[year].cost_events.append(CostPoolEvent(
                date=lot.date, event_type="cost", asset=asset,
                amount=lot.amount, pln_value=lot.cost_pln,
                price_method=method, source=lot.source,
                notes=label,
                nbp_rate=rate, nbp_rate_date=rate_date, nbp_currency=currency,
            ))

    for row in rows:
        date_iso = row["date"]
        date_str = date_iso[:10]
        year = int(date_str[:4])
        if split_year and date_str < polish_residency_start:
            excluded_counts[f"pre_residency_{row['tx_type']}"] += 1
            continue

        tx_type = row["tx_type"]
        asset = row["asset"]
        amount = _dec(row["amount"])
        fee = _dec(row.get("fee", "0"))
        fee_asset = row.get("fee_asset", "")
        cp_asset = row.get("counterparty_asset", "")
        cp_amount = _dec(row.get("counterparty_amount", "0"))
        source = row.get("source", "")
        source_tx_id = row.get("source_tx_id", "")

        if pools[year].year == 0:
            pools[year].year = year

        if tx_type in IGNORED_TX_TYPES:
            continue

        # === REVENUE EVENTS (crypto -> fiat) ===
        if tx_type == "sell" and not is_fiat(asset):
            revenue_pln, method, nbp_rate, nbp_date, nbp_cur = prices.resolve_with_rate(
                asset, amount, cp_asset, cp_amount, date_str)
            pools[year].revenue_events.append(CostPoolEvent(
                date=date_str, event_type="revenue", asset=asset,
                amount=amount, pln_value=revenue_pln, price_method=method,
                source=source, counterparty_asset=cp_asset,
                counterparty_amount=cp_amount,
                source_tx_id=source_tx_id,
                nbp_rate=nbp_rate, nbp_rate_date=nbp_date, nbp_currency=nbp_cur,
            ))
            # Sale fees are deductible disposal costs
            _append_fee_cost(
                pools[year], prices,
                date_str=date_str,
                fee_asset=fee_asset,
                fee_amount=fee,
                source=source,
                source_tx_id=source_tx_id,
                notes=f"Trading fee {fee} {fee_asset}",
                trade_asset=asset,
                trade_amount=amount,
                trade_pln_value=revenue_pln,
                trade_nbp_rate=nbp_rate,
                trade_nbp_date=nbp_date,
                trade_nbp_currency=nbp_cur,
            )

        # === COST EVENTS (fiat -> crypto purchases) ===
        elif tx_type == "buy":
            # Fiat spent to buy crypto = deductible cost
            if cp_asset and is_fiat(cp_asset) and cp_amount > 0:
                cost_pln, method, nbp_rate, nbp_date, nbp_cur = prices.resolve_with_rate(
                    asset, amount, cp_asset, cp_amount, date_str)
                pools[year].cost_events.append(CostPoolEvent(
                    date=date_str, event_type="cost", asset=asset,
                    amount=amount, pln_value=cost_pln, price_method=method,
                    source=source, counterparty_asset=cp_asset,
                    counterparty_amount=cp_amount,
                    notes=f"Buy {_fmt_plain(amount)} {asset} for {_fmt_plain(cp_amount)} {cp_asset}",
                    source_tx_id=source_tx_id,
                    nbp_rate=nbp_rate, nbp_rate_date=nbp_date, nbp_currency=nbp_cur,
                ))
                # Purchase fees
                _append_fee_cost(
                    pools[year], prices,
                    date_str=date_str,
                    fee_asset=fee_asset,
                    fee_amount=fee,
                    source=source,
                    source_tx_id=source_tx_id,
                    notes=f"Trading fee {fee} {fee_asset}",
                    trade_asset=asset,
                    trade_amount=amount,
                    trade_pln_value=cost_pln,
                    trade_nbp_rate=nbp_rate,
                    trade_nbp_date=nbp_date,
                    trade_nbp_currency=nbp_cur,
                )

        # === STABLECOIN DEPOSIT = cost (valued at NBP USD rate) ===
        # Skip if salary data covers this year (salary lots already count the
        # acquisition cost at receipt time; the exchange deposit is just a
        # transfer and should not be double-counted)
        elif tx_type == "deposit" and is_stablecoin(asset):
            if year in salary_years:
                continue  # salary lots already cover this cost
            pln_value, method, nbp_rate, nbp_date = prices.stablecoin_pln_value_with_rate(amount, date_str)
            pools[year].cost_events.append(CostPoolEvent(
                date=date_str, event_type="cost", asset=asset,
                amount=amount, pln_value=pln_value, price_method=method,
                source=source,
                notes=f"Stablecoin deposit {amount} {asset}",
                source_tx_id=source_tx_id,
                nbp_rate=nbp_rate, nbp_rate_date=nbp_date, nbp_currency="USD",
            ))

        # === STANDALONE FEES ===
        elif tx_type == "fee":
            _append_fee_cost(
                pools[year], prices,
                date_str=date_str,
                fee_asset=asset,
                fee_amount=amount,
                source=source,
                source_tx_id=source_tx_id,
                notes=row.get("notes", "") or f"Fee {amount} {asset}",
            )

        # === NON-TAXABLE EVENTS (crypto-to-crypto, transfers, etc.) ===
        # swap_in, swap_out, withdrawal, deposit (non-stablecoin),
        # staking_reward, earn_reward, interest, airdrop, token_swap,
        # conversion, funding_fee — all non-taxable at this stage.
        # Crypto-to-crypto swap fees and withdrawal/funding fees are excluded.

    # Build PIT-38 results year by year
    if imported_prior_total > 0 and pools[start_year].year == 0:
        pools[start_year].year = start_year

    carry_forward = Decimal("0")
    results: dict[int, PIT38Result] = {}

    for year in sorted(pools.keys()):
        pool = pools[year]
        revenue = pool.total_revenue
        costs_current = pool.total_costs

        costs_prior = carry_forward
        prior_breakdown: dict[str, Decimal] = {}
        if year == start_year and imported_prior_total > 0:
            costs_prior += imported_prior_total
            prior_breakdown = dict(imported_prior_breakdown)

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
            policy_name=policy,
            policy_label=POLICY_LABELS[policy],
            polish_residency_start=polish_residency_start if split_year else "",
            costs_prior_breakdown=prior_breakdown,
        )

        carry_forward = new_carry

    for key, count in sorted(excluded_counts.items()):
        warnings.append(f"Excluded {count} {key.replace('_', ' ')} events/lots under {policy}.")

    return {
        "yearly_results": results,
        "warnings": warnings,
        "policy_name": policy,
        "policy_label": POLICY_LABELS[policy],
        "polish_residency_start": polish_residency_start if split_year else "",
        "imported_prior_breakdown": {k: fmt(v) for k, v in imported_prior_breakdown.items()},
    }


def _imported_prior_breakdown(
    *,
    policy: str,
    imported_fiat_costs: Decimal,
    imported_salary_usdc_costs: Decimal,
    imported_successor_costs: Decimal,
) -> dict[str, Decimal]:
    """Return the imported prior-year cost layers included by a policy."""
    breakdown: dict[str, Decimal] = {}

    if policy == POLICY_LEGACY_FULL_HISTORY:
        if imported_fiat_costs > 0:
            breakdown["legacy_pre_residency_costs"] = imported_fiat_costs
        return breakdown

    if imported_fiat_costs > 0:
        breakdown["layer_a_fiat_purchase_costs"] = imported_fiat_costs

    if policy in (POLICY_SPLIT_YEAR_SUPPORTABLE, POLICY_SPLIT_YEAR_HIGH_RISK):
        if imported_salary_usdc_costs > 0:
            breakdown["layer_b_same_token_salary_usdc_costs"] = imported_salary_usdc_costs

    if policy == POLICY_SPLIT_YEAR_HIGH_RISK and imported_successor_costs > 0:
        breakdown["layer_c_pre_move_swap_successor_costs"] = imported_successor_costs

    return breakdown


def _dec(v: str) -> Decimal:
    try:
        return Decimal(v.strip())
    except Exception:
        return Decimal("0")


def _append_fee_cost(
    pool: YearlyPool,
    prices: PriceResolver,
    *,
    date_str: str,
    fee_asset: str,
    fee_amount: Decimal,
    source: str,
    source_tx_id: str,
    notes: str,
    trade_asset: str = "",
    trade_amount: Decimal = Decimal("0"),
    trade_pln_value: Decimal = Decimal("0"),
    trade_nbp_rate: Decimal | None = None,
    trade_nbp_date: str = "",
    trade_nbp_currency: str = "",
) -> None:
    """Append a deductible fee cost event when it can be valued in PLN."""
    if fee_amount <= 0 or not fee_asset:
        return

    # If the fee is charged in the traded asset itself, value it using the
    # trade's implied PLN-per-unit instead of a separate price lookup.
    if trade_asset and fee_asset.upper() == trade_asset.upper() and trade_amount > 0 and trade_pln_value > 0:
        unit_pln = trade_pln_value / trade_amount
        pool.fee_costs.append(CostPoolEvent(
            date=date_str,
            event_type="cost",
            asset=fee_asset,
            amount=fee_amount,
            pln_value=fee_amount * unit_pln,
            price_method="trade_implied_fee",
            source=source,
            notes=notes,
            source_tx_id=source_tx_id,
            nbp_rate=trade_nbp_rate,
            nbp_rate_date=trade_nbp_date,
            nbp_currency=trade_nbp_currency,
        ))
        return

    fee_pln, method, nbp_rate, nbp_date, nbp_cur = prices.asset_pln_value_with_rate(
        fee_asset, fee_amount, date_str)
    if fee_pln <= 0:
        return

    pool.fee_costs.append(CostPoolEvent(
        date=date_str,
        event_type="cost",
        asset=fee_asset,
        amount=fee_amount,
        pln_value=fee_pln,
        price_method=method,
        source=source,
        notes=notes,
        source_tx_id=source_tx_id,
        nbp_rate=nbp_rate,
        nbp_rate_date=nbp_date,
        nbp_currency=nbp_cur,
    ))
