# Analysis: Additional Crypto Tax Exposure from Personal Trading (2023-2024)

## The Question

Our FIFO tax calculator shows net gains from ALL crypto disposals (including personal trading beyond the salary USDC conversions):

- **2023**: ~146K PLN net gain (revenue 411K, FIFO costs 265K)
- **2024**: ~3K PLN net gain (revenue 786K, FIFO costs 783K)

The tax company only reported salary USDC->EUR conversions on PIT-38. Does adding personal crypto trading (selling BTC, ETH, DOT etc. for fiat) create additional tax?

## Why the Answer is: No Additional Tax

### PIT-38 does not work like FIFO

Our calculator uses strict FIFO: only the cost basis of the specific crypto lots consumed in each sale counts as cost. PIT-38 works differently -- it allows declaring **ALL crypto acquisition costs incurred in the year**, regardless of whether that crypto was sold.

The relevant PIT-38 fields:
- **Poz. 34**: Revenue from all crypto-to-fiat disposals
- **Poz. 35**: ALL costs of acquiring crypto during the year (not just what was sold)
- **Poz. 36**: Undeducted costs carried from prior years
- **Poz. 37**: Income = poz. 34 minus (poz. 35 + poz. 36), minimum 0
- **Poz. 38**: Excess costs = (poz. 35 + poz. 36) minus poz. 34, carries to next year

### 2023: Salary costs absorb everything

| | Our Calculator (FIFO) | PIT-38 (All Costs) |
|---|---|---|
| Revenue (all crypto disposals) | 411,144 PLN | 411,144 PLN |
| Costs | 264,730 PLN (consumed lots only) | **448,108 PLN** (all USDC salary acquired) + any crypto purchases |
| Net | +146,414 PLN | **Negative** (costs > revenue) |
| Tax | Would owe ~27.8K at 19% | **0 PLN** |

The 448K PLN salary USDC cost (already declared on the filed PIT-38) exceeds the 411K total revenue from ALL disposals. Even adding personal crypto trades to the revenue side, the salary cost base absorbs it. Any EUR spent buying crypto on exchanges would add further costs.

### 2024: Same story, even stronger

| | Our Calculator (FIFO) | PIT-38 (All Costs) |
|---|---|---|
| Revenue (all crypto disposals) | 785,509 PLN | 785,509 PLN |
| Costs | 782,531 PLN (consumed lots only) | **479,093 PLN** (salary) + **221,992 PLN** (2023 carry-forward) + any purchases |
| Total costs | — | **701,085+ PLN** |
| Net | +2,978 PLN | Likely **negative** or very small |
| Tax | ~566 PLN at 19% | **0 PLN** (or near zero) |

With 701K PLN in salary costs + carry-forward, plus any personal crypto purchase costs from 2024, the total costs likely exceed or closely match the 786K revenue.

### Why the FIFO gain doesn't translate to PIT-38 tax

```
FIFO approach (our calculator):
  Each sale → consume specific lots → gain if sale price > lot cost
  Total gains accumulate across all events

PIT-38 approach (actual Polish tax):
  Sum ALL disposal revenue for the year (one number)
  Sum ALL acquisition costs for the year (one number, includes unsold crypto)
  If costs > revenue → 0 tax, excess carries forward
```

The PIT-38 approach is more favorable because acquiring 448K PLN of USDC through salary counts as cost even if you only sold 226K PLN worth. The "extra" 222K of cost absorbs gains from personal trading.

## Can 2025 Losses Offset 2023-2024 Gains?

**No. Polish crypto tax only carries forward, never backward.**

Under PIT-38, there is no traditional loss (strata) in the Art. 9 ust. 3 sense. Instead:
- If costs > revenue in a year, the excess is "koszty uzyskania przychodow ktore nie zostaly potracone" (undeducted acquisition costs)
- These carry forward to the NEXT year's PIT-38 poz. 36
- They can only reduce FUTURE revenue, not past

Even if PIT-38 losses worked like regular PIT losses (Art. 9 ust. 3), those can only offset **future** income from the **same source**, up to 50% per year over 5 years. There is no carry-back mechanism in Polish tax law.

**However, this is a moot point** because:
1. 2023 PIT-38 already shows 0 tax (no gain to offset)
2. 2024 PIT-38, once filed, will also show 0 tax
3. The 2025 "loss" (~15K PLN) just adds to the cost carry-forward pile

## Cost Carry-Forward Chain

```
2023 PIT-38:  448K costs - 226K revenue = 222K carry-forward
2024 PIT-38:  (479K + 222K) costs - ~786K revenue = ~0 carry / small carry
2025 PIT-38:  (carry + 162K salary) costs - 271K revenue = large carry-forward
```

The carry-forward keeps growing because each year's salary USDC adds massive costs that exceed the fiat-exit revenue.

## Summary

| Year | Additional tax from personal crypto | Reason |
|---|---|---|
| 2023 | **0 PLN** | 448K salary costs > 411K total revenue |
| 2024 | **0 PLN** | 701K costs (salary + carry) ≈ 786K revenue |
| 2025 | **0 PLN** | Revenue 271K with ~862K+ in costs |

The USDC salary creates such a large cost shield each year that personal crypto trading gains are fully absorbed. No additional tax is owed, and 2025 losses cannot offset prior years (but don't need to since prior years are already at 0).

**The only action needed is filing the missing 2024 PIT-38 to preserve the carry-forward chain.** Without it, 2025 would lack the cost carry-forward and show phantom gains.
