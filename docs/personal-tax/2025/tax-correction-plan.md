# Tax Correction & 2025 Filing Plan

**Date**: March 2026
**Status**: Research phase — gathering information before engaging accountant

---

## Current Situation

### What has been filed

| Year | Form | Status | Tax Paid |
|---|---|---|---|
| 2023 | PIT-37 | Filed late (June 2024) with czynny zal | 87,116 PLN |
| 2023 | PIT-38 | Filed late (June 2024) with czynny zal | 0 PLN |
| 2024 | PIT-37 | Filed (by tax company) | 95,048 PLN |
| 2024 | PIT-38 | **NOT FILED** | — |
| 2025 | PIT-28 | Not yet due (deadline Apr 30, 2026) | Monthly payments in progress |
| 2025 | PIT-37 or PIT-36 | Not yet due | — |
| 2025 | PIT-38 | Not yet due | — |

### What we know is wrong

1. **PIT-37 used for both 2023 and 2024** — should be PIT-36 (no PIT-11/IFT-1R from foreign payer)
2. **No monthly advance tax payments (zaliczki)** for 2023 or 2024 — interest liability accrued
3. **No PIT/ZG foreign income annex** attached to either year
4. **No PIT-38 for 2024** — 222K PLN cost carry-forward from 2023 is stranded, 479K PLN of 2024 USDC acquisition costs undeclared
5. **Personal crypto trading unreported** — Binance/Kraken activity beyond salary USDC conversions not included in any PIT-38
6. **Umowa zlecenie classification** may be wrong — could be dzialalnosc gospodarcza given regularity, multiple clients, and amounts

### What is NOT wrong (tax amounts are broadly correct)

- The income amounts (448K PLN for 2023, 479K PLN for 2024) appear reasonable based on invoices
- The 20% cost deduction is standard for the chosen classification
- The progressive tax calculations are arithmetically correct
- The 2023 PIT-38 approach (USDC salary value = crypto cost basis) is internally consistent
- The czynny zal for 2023 was properly filed

---

## Financial Exposure

### Additional tax owed: likely minimal

| Item | Estimated Additional Tax |
|---|---|
| PIT-37 -> PIT-36 form correction | 0 PLN (same calculation, different form) |
| Missing 2024 PIT-38 | 0 PLN (costs far exceed revenue — would show no tax) |
| Unreported personal crypto (2023-2024) | Likely small — depends on non-salary crypto->fiat events |

### Interest on late advance payments

Monthly zaliczki should have been paid by the 20th of each following month. Instead, full tax was paid at filing. Interest at ~14.5% annual rate:

| Year | Tax Due | Est. Avg Delay | Est. Interest |
|---|---|---|---|
| 2023 | 87,116 PLN | ~6-12 months | ~3,000-6,000 PLN |
| 2024 | 95,048 PLN | ~6-12 months | ~3,000-6,000 PLN |
| **Total** | | | **~6,000-12,000 PLN** |

This interest is already accrued — it exists whether or not we file corrections. The corrections themselves don't create new interest.

### Cost basis at risk if NOT corrected

Without a 2024 PIT-38, the following cost basis is undeclared:

| Source | Amount |
|---|---|
| 2023 carry-forward (poz. 38) | 221,992.49 PLN |
| 2024 USDC salary acquisition costs | ~479,092.64 PLN |
| **Total at risk** | **~701,085 PLN** |

If this cost basis is lost, future USDC->EUR conversions (including all of 2025) would appear as nearly 100% profit, potentially triggering ~133K PLN in phantom crypto tax (19% of ~701K). **Filing the correction protects this.**

---

## Correction Plan

### Priority 1 (HIGH): File 2024 PIT-38 correction — before Apr 30, 2026

**Why**: Protects ~701K PLN of cost basis. Without it, the 2025 PIT-38 cannot reference prior-year undeducted costs.

**What to file**:
- Korekta (correction) for 2024 adding PIT-38
- Poz. 34: Revenue from 2024 crypto disposals (USDC->EUR + ETH->EUR events)
- Poz. 35: 2024 USDC acquisition costs (~479K PLN)
- Poz. 36: 2023 carry-forward (221,992.49 PLN)
- Result: 0 tax due, large carry-forward to 2025
- Consider including personal crypto trading disposals from 2024 (Binance ETH->EUR "Sell Crypto To Fiat" events)

**Timing**: Must be filed BEFORE the 2025 PIT-38 so the carry-forward chain is intact. Ideally by March 2026.

### Priority 2 (MEDIUM): Correct 2023 & 2024 PIT-37 -> PIT-36

**Why**: PIT-37 is technically the wrong form. Correcting to PIT-36 eliminates a procedural vulnerability if the tax office audits.

**What to file**:
- Korekta PIT-37 for 2023 (zeroing it out) + new PIT-36 for 2023
- Same for 2024
- Same numbers, just moved to the correct form
- Add PIT/ZG annex for foreign income
- Include czynny zal explaining the correction

**Risk of NOT doing this**: Low-medium. The tax office may never notice, since the tax amount is correct. But if they audit, the wrong form could trigger questions.

### Priority 3 (MEDIUM): Determine if personal crypto trading needs reporting

**Why**: Our tax calculator shows crypto disposals (selling BTC, ETH, DOT for EUR/fiat) in 2023-2024 beyond the salary USDC conversions. If these exist, they should be on PIT-38.

**Action items**:
- Review our calculator output for 2023 and 2024 non-salary crypto->fiat events
- Cross-reference with Binance/Kraken exports
- If material amounts exist, include them in the PIT-38 corrections
- These would likely have cost basis from earlier acquisitions, so net tax impact could be small

### Priority 4 (STANDARD): File 2025 taxes correctly the first time

**Forms needed for 2025**:

| Form | Covers | Deadline |
|---|---|---|
| **PIT-28** | JDG ryczalt income (EUR invoicing after JDG established) | Apr 30, 2026 |
| **PIT-36** | Pre-JDG USDC salary income (Jan-Apr 2025) | Apr 30, 2026 |
| **PIT-38** | Crypto disposals (USDC->EUR, DOT->EUR conversions) | Apr 30, 2026 |

**PIT-28 (JDG ryczalt)**:
- Revenue from EUR invoices after JDG establishment
- 12% flat tax on gross revenue
- Monthly payments already being made

**PIT-36 (pre-JDG income)**:
- USDC salary received Jan-Apr 2025 (40,500 USDC ≈ 162K PLN)
- Classification: TBD (depends on research outcome — umowa zlecenie vs other)
- Need to determine correct approach: same as tax company's 2023/2024 method, or different?

**PIT-38 (crypto)**:
- 15 fiat-exit events (13 Binance + 2 Kraken) — our calculator has these
- Revenue: ~271K PLN
- Cost basis: ~287K PLN (including salary USDC at NBP rates + carry-forward from 2024)
- Net: ~-15K PLN (loss, no tax due)
- The carry-forward from 2024 PIT-38 correction feeds directly into this

### Priority 5 (LOW): Resolve classification question

**Why**: The umowa zlecenie (Art. 13 pkt 8) classification used by the tax company may not be optimal. Research prompt 02 explores whether this should be:
- Dzialalnosc gospodarcza (requiring JDG registration earlier)
- Inne zrodla (other sources)
- Or if the current classification is actually fine

**Action**: Wait for research responses on prompt 02 before deciding whether to change the classification in corrections. If the classification changes, the tax amount might change (e.g., liniowy 19% vs progressive 12%/32%).

**Important**: Changing classification retroactively could increase or decrease tax. Progressive rates produced ~87-95K PLN per year. Linear 19% on the same dochod would be ~68-73K PLN (lower!). But switching to JDG/liniowy retroactively requires having been registered. This needs careful analysis.

---

## Recommended Sequence of Actions

```
March 2026 (NOW)
  ├── Complete tax law research (prompts in docs/tax-law/)
  ├── Compute 2024 PIT-38 numbers using our calculator
  ├── File korekta: 2024 PIT-38 (protects cost basis)
  │
April 2026 (before Apr 30 deadline)
  ├── File PIT-28 for 2025 (JDG ryczalt)
  ├── File PIT-36 for 2025 (pre-JDG USDC income)
  ├── File PIT-38 for 2025 (crypto disposals)
  │
After April 2026 (lower priority)
  ├── File korekta: 2023 PIT-37 -> PIT-36 + PIT/ZG
  ├── File korekta: 2024 PIT-37 -> PIT-36 + PIT/ZG
  ├── Review personal crypto trading for 2023-2024
  └── Consider engaging doradca podatkowy for classification question
```

---

## Open Questions (Pending Research)

1. **USDC salary classification**: Is umowa zlecenie correct? Or should it be something else? (Research prompt 02)
2. **Double-reporting approach**: Is the PIT-37 income + PIT-38 cost basis approach endorsed by KIS? (Research prompt 02)
3. **Advance tax interest**: Exact calculation of interest owed for missing monthly zaliczki (Research prompt 06)
4. **Can PIT-37 -> PIT-36 korekta be filed electronically?** Or must it be paper?
5. **Pre-JDG 2025 income**: Should it follow the same approach as 2023/2024, or be handled differently now that JDG exists?
6. **ZUS obligations**: Were there ZUS obligations on the 2023/2024 umowa zlecenie income from a foreign payer? (Research prompt 02)
7. **Stablecoin classification**: Does MiCA reclassification of USDC affect anything? (Research prompt 04)

---

## Cost Basis Chain (Critical)

The FIFO/cost-basis chain across years must be unbroken:

```
2023 PIT-38 (filed):
  Costs declared: 448,108.20 PLN
  Revenue: 226,115.71 PLN
  Carry-forward: 221,992.49 PLN ──┐
                                    │
2024 PIT-38 (NEEDS FILING):        │
  Prior-year costs: 221,992.49 ◄───┘
  2024 costs: ~479,092.64 PLN (salary USDC)
  Revenue: TBD (small)
  Carry-forward: ~700K PLN ──────┐
                                  │
2025 PIT-38 (to be filed):       │
  Prior-year costs: ~700K ◄──────┘
  2025 costs: ~162K PLN (Jan-Apr salary USDC)
  Revenue: ~271K PLN (15 fiat-exit events)
  Result: costs >> revenue → 0 tax, large carry-forward
```

**If the 2024 PIT-38 is not filed, this chain breaks and the 2025 PIT-38 would show ~271K PLN revenue with minimal cost basis = ~51K PLN in tax that shouldn't be owed.**
