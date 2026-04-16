"""Price resolution: NBP -> stablecoin -> CoinGecko -> unresolved."""
from __future__ import annotations

import json
import os
import time
import urllib.request
from decimal import Decimal
from typing import Optional, Tuple

from tax_calc.constants import COINGECKO_ID_MAP, FIAT, STABLECOINS, is_fiat, is_stablecoin
from tax_calc.nbp import NBPClient


class PriceResolver:
    """Resolves PLN values for transactions using multiple data sources."""

    def __init__(self, nbp: NBPClient, cg_cache_path: str = "data/coingecko_cache.json"):
        self.nbp = nbp
        self._cg_cache_path = cg_cache_path
        self._cg_cache: dict[str, Optional[str]] = {}
        self._load_cg_cache()

    def _load_cg_cache(self) -> None:
        if os.path.exists(self._cg_cache_path):
            with open(self._cg_cache_path, "r") as f:
                self._cg_cache = json.load(f)

    def _save_cg_cache(self) -> None:
        os.makedirs(os.path.dirname(self._cg_cache_path) or ".", exist_ok=True)
        with open(self._cg_cache_path, "w") as f:
            json.dump(self._cg_cache, f, indent=2, sort_keys=True)

    def _get_coingecko_price(self, asset: str, date_str: str) -> Optional[Decimal]:
        """Get PLN price from CoinGecko historical API."""
        cache_key = f"{asset.upper()}/{date_str}"
        if cache_key in self._cg_cache:
            v = self._cg_cache[cache_key]
            return Decimal(v) if v is not None else None

        cg_id = COINGECKO_ID_MAP.get(asset.upper())
        if not cg_id:
            self._cg_cache[cache_key] = None
            return None

        parts = date_str.split("-")
        cg_date = f"{parts[2]}-{parts[1]}-{parts[0]}"

        url = f"https://api.coingecko.com/api/v3/coins/{cg_id}/history?date={cg_date}&localization=false"
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "tax-calc/1.0"})
            with urllib.request.urlopen(req, timeout=15) as resp:
                data = json.loads(resp.read().decode("utf-8"))
                price_pln = data.get("market_data", {}).get("current_price", {}).get("pln")
                if price_pln is not None:
                    result = Decimal(str(price_pln))
                    self._cg_cache[cache_key] = str(result)
                    self._save_cg_cache()
                    time.sleep(0.5)
                    return result
        except Exception:
            pass

        self._cg_cache[cache_key] = None
        self._save_cg_cache()
        return None

    def resolve(
        self,
        asset: str,
        amount: Decimal,
        counterparty_asset: str,
        counterparty_amount: Decimal,
        date_str: str,
    ) -> Tuple[Decimal, str]:
        """
        Resolve PLN value of a transaction.

        Priority:
        1. Counterparty is PLN -> direct
        2. Counterparty is fiat -> counterparty_amount * NBP rate
        3. Counterparty is stablecoin -> counterparty_amount * NBP USD rate
        4. Asset is stablecoin -> amount * NBP USD rate (for salary/deposit valuation)
        5. CoinGecko historical price
        6. Unresolved (return 0 + warning)
        """
        cp = counterparty_asset.upper() if counterparty_asset else ""
        cp_amt = counterparty_amount.copy_abs() if counterparty_amount else Decimal("0")

        # 1. Direct PLN
        if cp == "PLN" and cp_amt > 0:
            return cp_amt, "direct_pln"

        # 2. Counterparty is fiat -> NBP rate
        if cp in FIAT and cp_amt > 0:
            rate = self.nbp.get_rate(cp, date_str)
            if rate:
                return cp_amt * rate, f"nbp_{cp.lower()}"

        # 3. Counterparty is stablecoin -> treat as USD
        if cp in STABLECOINS and cp_amt > 0:
            usd_rate = self.nbp.get_rate("USD", date_str)
            if usd_rate:
                return cp_amt * usd_rate, f"nbp_usd_via_{cp.lower()}"

        # 4. Asset itself is stablecoin -> amount * USD rate
        if is_stablecoin(asset) and amount > 0:
            usd_rate = self.nbp.get_rate("USD", date_str)
            if usd_rate:
                return amount.copy_abs() * usd_rate, f"nbp_usd_stablecoin_{asset.lower()}"

        # 5. CoinGecko
        if asset.upper() not in FIAT and asset.upper() not in STABLECOINS:
            price = self._get_coingecko_price(asset, date_str)
            if price:
                return amount.copy_abs() * price, "coingecko_pln"

        # 6. Unresolved
        return Decimal("0"), "unresolved"

    def resolve_with_rate(
        self,
        asset: str,
        amount: Decimal,
        counterparty_asset: str,
        counterparty_amount: Decimal,
        date_str: str,
    ) -> Tuple[Decimal, str, Optional[Decimal], str, str]:
        """Like resolve() but also returns the NBP rate, rate date, and currency used.

        Returns:
            (pln_value, method, nbp_rate, nbp_rate_date, nbp_currency)
        """
        cp = counterparty_asset.upper() if counterparty_asset else ""
        cp_amt = counterparty_amount.copy_abs() if counterparty_amount else Decimal("0")

        # 1. Direct PLN
        if cp == "PLN" and cp_amt > 0:
            return cp_amt, "direct_pln", Decimal("1"), date_str, "PLN"

        # 2. Counterparty is fiat -> NBP rate
        if cp in FIAT and cp_amt > 0:
            rate, rate_date = self.nbp.get_rate_with_date(cp, date_str)
            if rate:
                return cp_amt * rate, f"nbp_{cp.lower()}", rate, rate_date, cp

        # 3. Counterparty is stablecoin -> treat as USD
        if cp in STABLECOINS and cp_amt > 0:
            rate, rate_date = self.nbp.get_rate_with_date("USD", date_str)
            if rate:
                return cp_amt * rate, f"nbp_usd_via_{cp.lower()}", rate, rate_date, "USD"

        # 4. Asset itself is stablecoin -> amount * USD rate
        if is_stablecoin(asset) and amount > 0:
            rate, rate_date = self.nbp.get_rate_with_date("USD", date_str)
            if rate:
                return amount.copy_abs() * rate, f"nbp_usd_stablecoin_{asset.lower()}", rate, rate_date, "USD"

        # 5. CoinGecko
        if asset.upper() not in FIAT and asset.upper() not in STABLECOINS:
            price = self._get_coingecko_price(asset, date_str)
            if price:
                return amount.copy_abs() * price, "coingecko_pln", price, date_str, asset

        # 6. Unresolved
        return Decimal("0"), "unresolved", None, "", ""

    def stablecoin_pln_value(self, amount: Decimal, date_str: str) -> Tuple[Decimal, str]:
        """Value a stablecoin amount in PLN using NBP USD rate."""
        usd_rate = self.nbp.get_rate("USD", date_str)
        if usd_rate:
            return amount.copy_abs() * usd_rate, "nbp_usd_stablecoin"
        return Decimal("0"), "unresolved"

    def stablecoin_pln_value_with_rate(self, amount: Decimal, date_str: str) -> Tuple[Decimal, str, Optional[Decimal], str]:
        """Like stablecoin_pln_value but also returns the rate and rate date."""
        rate, rate_date = self.nbp.get_rate_with_date("USD", date_str)
        if rate:
            return amount.copy_abs() * rate, "nbp_usd_stablecoin", rate, rate_date
        return Decimal("0"), "unresolved", None, ""
