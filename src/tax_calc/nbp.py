"""NBP (National Bank of Poland) exchange rate client with JSON disk cache."""
from __future__ import annotations

import json
import os
import time
import urllib.request
from datetime import datetime, timedelta
from decimal import Decimal
from typing import Optional


class NBPClient:
    """Fetches PLN mid-rates from api.nbp.pl with local disk cache."""

    def __init__(self, cache_path: str = "data/nbp_cache.json"):
        self._cache_path = cache_path
        self._cache: dict[str, str] = {}  # "CUR/YYYY-MM-DD" -> rate string
        self._load_cache()

    def _load_cache(self) -> None:
        if os.path.exists(self._cache_path):
            with open(self._cache_path, "r") as f:
                self._cache = json.load(f)

    def _save_cache(self) -> None:
        os.makedirs(os.path.dirname(self._cache_path) or ".", exist_ok=True)
        with open(self._cache_path, "w") as f:
            json.dump(self._cache, f, indent=2, sort_keys=True)

    def get_rate(self, currency: str, date_str: str) -> Optional[Decimal]:
        """
        Get PLN mid-rate for currency on the last business day BEFORE date_str.

        Polish tax law requires the NBP mid-rate from the last business day
        before the transaction date (not the transaction date itself).

        Args:
            currency: ISO currency code (e.g. "EUR", "USD")
            date_str: Transaction date as "YYYY-MM-DD"

        Returns:
            PLN value of 1 unit of currency, or None if unavailable.
        """
        if currency.upper() == "PLN":
            return Decimal("1")

        currency = currency.upper()
        cache_key = f"{currency}/{date_str}"
        if cache_key in self._cache:
            return Decimal(self._cache[cache_key])

        base_date = datetime.strptime(date_str, "%Y-%m-%d")
        # Start at delta=1: day BEFORE the transaction date (Polish tax law)
        for delta in range(1, 10):
            d = base_date - timedelta(days=delta)
            ds = d.strftime("%Y-%m-%d")

            url = f"https://api.nbp.pl/api/exchangerates/rates/a/{currency}/{ds}/?format=json"
            try:
                req = urllib.request.Request(url, headers={"User-Agent": "tax-calc/1.0"})
                with urllib.request.urlopen(req, timeout=10) as resp:
                    data = json.loads(resp.read().decode("utf-8"))
                    rate = Decimal(str(data["rates"][0]["mid"]))
                    self._cache[cache_key] = str(rate)
                    self._save_cache()
                    time.sleep(0.2)
                    return rate
            except Exception:
                continue

        return None
