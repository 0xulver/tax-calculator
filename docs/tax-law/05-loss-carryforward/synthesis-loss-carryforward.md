# Synthesis: Crypto Loss Carry-Forward Rules in Poland

Sources: ChatGPT 5.4 Pro, ChatGPT Deep Research, Perplexity, Gemini 3.1 Deep Research

---

## Complete Consensus (All 4 sources agree on everything)

This is the most unanimous topic across all research — **zero disagreements** on any substantive point.

### The fundamental rule: Crypto does NOT use Art. 9 ust. 3 loss carry-forward

Art. 9 ust. 3a pkt 2 PIT **explicitly excludes** crypto from the standard loss carry-forward mechanism. The 50% annual cap and the 5,000,000 PLN one-shot rule do **not apply** to crypto. There is no "strata podatkowa" (tax loss) for crypto — only "nadwyzka kosztow" (excess of costs over revenues).

### What crypto uses instead: Art. 22 ust. 16 cost rollover

When crypto costs exceed revenue in a year, the excess carries forward to the next year as additional costs. This mechanism is:
- **No time limit** — costs carry forward indefinitely (confirmed by KIS interpretations)
- **No annual cap** — the full excess can offset revenue in the very next year (no 50% restriction)
- **No maximum amount** — no 5M PLN one-shot limit
- **Ring-fenced** — can only offset future crypto revenue, not stocks, business income, or anything else

### How it works on PIT-38

| PIT-38 Field (2023-2024) | PIT-38 Field (2025) | Description |
|---|---|---|
| Poz. 34 | Poz. 36 | Revenue from crypto disposals |
| Poz. 35 | Poz. 37 | Costs incurred in current year |
| Poz. 36 | Poz. 38 | Costs from prior years (carry-forward from last year's poz. 38/40) |
| Poz. 37 | Poz. 39 | Income = revenue - (current costs + prior costs), min 0 |
| Poz. 38 | Poz. 40 | Excess costs to carry forward = (current + prior costs) - revenue |

### Comparison with standard loss rules

| Feature | Art. 9 ust. 3 (stocks etc.) | Art. 22 ust. 16 (crypto) |
|---|---|---|
| Applies to crypto? | **No** (excluded by Art. 9 ust. 3a pkt 2) | **Yes** |
| Time limit | 5 years | **None** (infinite) |
| Annual cap | 50% OR 5M PLN one-shot | **None** (full amount each year) |
| Legal term | "Strata podatkowa" (tax loss) | "Nadwyzka kosztow" (cost surplus) |
| Can offset other sources? | Same income source only | Crypto revenue only |

### Crypto cannot offset anything else (and vice versa)

Art. 30b ust. 5d: crypto income is NOT combined with:
- Stock/bond/derivative gains (even though both are on PIT-38, they're separate sections)
- Business income (JDG, ryczalt, liniowy, skala)
- Employment income
- Rental income
- Any other income source

### Must file PIT-38 even with zero revenue

Art. 30b ust. 6a requires filing PIT-38 to declare costs even in years with no crypto sales. Failure to file breaks the carry-forward chain — KIS/sources warn that omitting a cost-only year may forfeit the right to carry those costs forward. The fix is a korekta (correction).

### Cross-border: Sweden to Poland

All 4 sources agree on the same framework:

**Swedish-year realized losses (2020-2022) = dead.** These were finalized under Swedish jurisdiction. They cannot be imported into the Polish system. The ~461 PLN loss from 2020 is permanently extinguished.

**Swedish-year unrealized costs = alive.** Fiat-to-crypto purchase costs incurred while in Sweden, for crypto that was NOT sold in Sweden, CAN be used in Polish PIT-38. Conditions:
- Must be documented (exchange records, bank transfers)
- Must NOT have been already deducted in Sweden
- Enter as costs in the first Polish PIT-38 (2023)
- Convert to PLN using NBP rate from the original purchase date

Supported by WSA Warsaw ruling III SA/Wa 1290/24 (Aug 29, 2024) and multiple KIS interpretations for UK/Germany residency changes.

**Double-counting prohibition:** If a cost was already used to reduce Swedish tax, it cannot also appear in Polish PIT-38.

### Corrections (korekta) can establish or increase carry-forward

If a prior PIT-38 omitted costs:
1. File korekta for the earliest affected year
2. The corrected poz. 38/40 creates or increases the carry-forward
3. Cascade corrections to subsequent years (each year's poz. 36/38 depends on the prior year)
4. Include czynny zal explaining the correction

Statute of limitations: 5 years from end of year the tax was due. For 2020: expires Dec 31, 2026. For 2023: expires Dec 31, 2029.

---

## No Disagreements

Remarkably, all 4 sources agree on every point. There are no conflicting positions on:
- The Art. 9 ust. 3a exclusion
- The Art. 22 ust. 16 mechanism
- The unlimited time/amount nature of the carry-forward
- The ring-fencing
- The cross-border treatment
- The filing requirements
- The correction mechanics

The only variation is emphasis — Gemini provides the most detailed cross-border analysis, Perplexity cites the most KIS interpretations and the WSA ruling, ChatGPT 5.4 Pro is the most concise with direct legal references, and ChatGPT Deep Research gives the best procedural guidance.

---

## What This Means for You

### Your carry-forward chain is working correctly

Our cost pool calculator shows costs exceeding revenue every year, with the excess rolling forward:

| Year | Revenue | Total Costs | Income | Carry Forward |
|---|---|---|---|---|
| 2020 | 3,640 | 271,378 | 0 | 267,738 |
| 2021 | 265,133 | 797,855 | 0 | 532,722 |
| 2022 | 437,946 | 668,811 | 0 | 230,865 |
| 2023 | 411,144 | 539,917 | 0 | 128,773 |
| 2024 | 785,509 | 906,955 | 0 | 121,446 |
| 2025 | 271,317 | 589,925 | 0 | 318,608 |

**Zero tax in every year.** The ~319K PLN carry-forward into 2026 shields future gains indefinitely.

### The old PIT-38 report was wrong about loss carry-forward

Our original pit38.py used the Art. 9 ust. 3 rules (50% cap, 5-year limit). This was incorrect — crypto uses the simpler, more favorable Art. 22 ust. 16 mechanism. The rewritten cost_pool.py already implements the correct rule (unlimited carry-forward, no cap).

### Pre-residency costs are free money

Any fiat-to-crypto purchases you made in Sweden (2020-2022) that were NOT sold in Sweden and NOT deducted on Swedish tax returns can be added to the Polish cost pool. This could be significant — worth calculating from Binance/Kraken records.

---

## Action Items

### 1. Calculate pre-residency costs (potentially significant)

Extract all fiat->crypto purchases from Binance/Kraken for 2020-2022. Verify which were NOT deducted in Swedish K4/Inkomstdeklaration. Convert to PLN at historical NBP rates. Add to the `--pre-residency-costs` parameter when running the calculator.

### 2. Verify Swedish tax returns for double-counting

Check your Swedish K4 forms for 2020-2022 to confirm which crypto costs were already claimed there. Only costs NOT used in Sweden can appear in Polish PIT-38.

### 3. File PIT-38 for every year from 2023 onward

Even if costs > revenue, the filing establishes the carry-forward chain. The missing 2024 PIT-38 breaks the chain — filing it is the top priority (as already identified in the correction plan).

### 4. The 2020 statute of limitations window closes Dec 31, 2026

If any 2020 corrections are needed (unlikely since you were Swedish resident), they must be filed before end of 2026. This is low priority since 2020 was a Swedish year.

### 5. No changes needed to the calculator

The cost pool calculator already correctly implements Art. 22 ust. 16 — unlimited carry-forward, no cap, full amount each year. This matches all 4 research sources.
