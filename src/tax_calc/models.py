from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal, ROUND_HALF_UP
from typing import Optional


def fmt(v: Decimal) -> str:
    return str(v.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP))


def fmt_full(v: Decimal) -> str:
    if not isinstance(v, Decimal):
        v = Decimal(str(v))
    return str(v.normalize())


@dataclass
class Transaction:
    date: str  # ISO format
    source: str
    source_tx_id: str
    tx_type: str
    asset: str
    amount: Decimal
    fee: Decimal = Decimal("0")
    fee_asset: str = ""
    counterparty_asset: str = ""
    counterparty_amount: Decimal = Decimal("0")
    notes: str = ""

    def to_dict(self) -> dict[str, str]:
        return {
            "date": self.date,
            "source": self.source,
            "source_tx_id": self.source_tx_id,
            "tx_type": self.tx_type,
            "asset": self.asset,
            "amount": fmt_full(self.amount),
            "fee": fmt_full(self.fee),
            "fee_asset": self.fee_asset,
            "counterparty_asset": self.counterparty_asset,
            "counterparty_amount": fmt_full(self.counterparty_amount),
            "notes": self.notes,
        }


@dataclass
class FIFOLot:
    date: str  # YYYY-MM-DD
    amount: Decimal
    cost_pln: Decimal
    source: str = ""
    source_tx_id: str = ""
    asset: str = "USDC"  # crypto asset received/purchased
    fiat_currency: str = "USD"  # fiat currency used for NBP rate

    @property
    def cost_per_unit(self) -> Decimal:
        if self.amount == 0:
            return Decimal("0")
        return self.cost_pln / self.amount

    def __repr__(self) -> str:
        return f"Lot({self.date}, {self.amount}, {fmt(self.cost_pln)} PLN, {self.source})"


@dataclass
class TaxEvent:
    date: str
    asset: str
    amount: Decimal
    revenue_pln: Decimal
    cost_basis_pln: Decimal
    gain_loss_pln: Decimal
    price_method: str
    source: str
    counterparty_asset: str = ""
    counterparty_amount: Decimal = Decimal("0")
    lots_consumed: int = 0
    year: int = 0
    lot_details: list = field(default_factory=list)

    def to_dict(self) -> dict[str, str]:
        return {
            "date": self.date,
            "asset": self.asset,
            "amount": fmt_full(self.amount),
            "revenue_pln": fmt(self.revenue_pln),
            "cost_basis_pln": fmt(self.cost_basis_pln),
            "gain_loss_pln": fmt(self.gain_loss_pln),
            "price_method": self.price_method,
            "source": self.source,
            "counterparty_asset": self.counterparty_asset,
            "counterparty_amount": fmt_full(self.counterparty_amount),
            "lots_consumed": str(self.lots_consumed),
            "year": str(self.year),
        }
