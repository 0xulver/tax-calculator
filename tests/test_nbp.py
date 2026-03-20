"""Tests for the NBP rate client."""
from decimal import Decimal
from unittest.mock import MagicMock, patch

import pytest

from tax_calc.nbp import NBPClient


def test_pln_returns_one():
    """PLN -> PLN rate is always 1."""
    client = NBPClient(cache_path="/tmp/nonexistent_cache.json")
    assert client.get_rate("PLN", "2025-01-15") == Decimal("1")


def test_cache_hit(tmp_path):
    """Cached rates are returned without API calls."""
    import json
    cache_path = str(tmp_path / "cache.json")
    with open(cache_path, "w") as f:
        json.dump({"EUR/2025-01-15": "4.2567"}, f)

    client = NBPClient(cache_path=cache_path)
    rate = client.get_rate("EUR", "2025-01-15")
    assert rate == Decimal("4.2567")


def test_starts_at_day_before():
    """NBP rate should be fetched for day BEFORE transaction, not transaction day."""
    client = NBPClient(cache_path="/tmp/nonexistent_cache.json")

    calls = []
    original_urlopen = None

    def mock_urlopen(req, timeout=None):
        url = req.full_url if hasattr(req, 'full_url') else str(req)
        calls.append(url)
        raise Exception("mock 404")

    with patch("tax_calc.nbp.urllib.request.urlopen", side_effect=mock_urlopen):
        result = client.get_rate("EUR", "2025-01-16")

    # Should NOT contain the transaction date itself
    assert not any("2025-01-16" in c for c in calls), \
        f"Should not fetch transaction date itself, but called: {calls}"
    # Should start with day before
    assert any("2025-01-15" in c for c in calls), \
        f"Should start at day before, called: {calls}"
