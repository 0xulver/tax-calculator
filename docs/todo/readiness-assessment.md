# Tax Calculator System -- Readiness Assessment

**Date**: April 13, 2026
**Overall Completeness**: ~70% for Polish taxes, ~0% for Swedish taxes

> Snapshot from April 13, 2026. Parts of this assessment were superseded by
> later work, especially the PIT-36 / PIT-28 modules and the updated PIT-38
> filing chain. For current filing numbers, use `docs/todo/filing-summary.md`
> and the generated reports in `outputs/`.

---

## What's DONE and Working Well

### PIT-38 (Crypto Capital Gains) -- ~90% complete

- Cost pool engine correctly implements Polish annual cost pooling (not FIFO) per Art. 22 ust. 14-16
- Binance + Kraken normalizers parse exchange CSVs into unified format (1,842 transactions)
- Polygon USDC salary payments parsed and injected as cost basis
- NBP exchange rates fetched correctly (business-day-before rule)
- CoinGecko fallback for crypto prices
- Carry-forward chain tracked across 2020-2025
- Markdown reports generated with PIT-38 Section E field numbers (poz. 34-40)
- Interactive web dashboard with drill-down, waterfall charts, timeline
- All years show 0 tax due (costs exceed revenue), ~318K PLN carry-forward to 2026
- Test suite covers normalizers, cost pool, NBP, salary parsing

### Tax Law Research -- Thorough

- 14 topics researched across 4 AI models (54 documents) in `docs/tax-law/`
- Covers: cost pooling, carry-forward, stablecoin treatment, USDC salary barter doctrine, residency transition, bot trading, platform losses, late filing, and more

### Verification/Traceability -- Good

- Every revenue and cost event in reports shows: date, asset, amount, counterparty, PLN value, and pricing method used
- Dashboard lets you drill down from year totals to individual events
- Normalized CSVs preserve source exchange and transaction IDs

---

## What STILL NEEDS to be Done

### URGENT -- Before April 30, 2026

#### 1. File 2024 PIT-38 korekta

The system has the numbers ready:

| PIT-38 Field | Amount (PLN) |
|---:|---:|
| Poz. 34 -- Revenue | 785,508.57 |
| Poz. 35 -- Costs (2024) | 778,181.67 |
| Poz. 36 -- Costs (prior years) | 128,772.86 |
| Poz. 38 -- Carry-forward to 2025 | 121,445.96 |

**Without this filing, the carry-forward chain breaks and 2025 would show ~51K PLN phantom tax.**

#### 2. File 2025 PIT-38

Numbers are computed: 271K revenue, 468K+121K costs, 0 tax due. Ready to file.

#### 3. Build PIT-28 ryczalt calculator (NOT in this system)

The system does not calculate ryczalt. Needed:

- Parse Clearstar XML invoices for amounts/dates (7 invoices, ~63K EUR in 2025)
- Parse Conclave PDF invoices (7 invoices in `docs/invoices/2025/invoices-conclave/`)
- Calculate PLN revenue per NBP rates (day before invoice/settlement date)
- 12% tax calculation
- Track FX differences (roznice kursowe) if payment date differs from invoice date
- Verify monthly payments already made match
- Generate PIT-28 form field values

#### 4. Build PIT-36 module for pre-JDG USDC salary (NOT in this system)

The Conclave USDC payments (Jan-Apr 2025, ~40,500 USDC) need to be reported as personal income on PIT-36. The system currently tracks these as PIT-38 *costs* only -- it does not generate the PIT-36 income side.

#### 5. Extract Conclave invoice amounts

The 7 Conclave PDFs in `docs/invoices/2025/invoices-conclave/` haven't been parsed. Need to extract amounts and dates to cross-reference with salary payments.

### IMPORTANT -- Soon After Filing Deadline

#### 6. File 2023 & 2024 PIT-37 -> PIT-36 korekta

Wrong form used for both years (PIT-37 requires a Polish payer with PIT-11). Should be PIT-36 with PIT/ZG foreign income annex. Same numbers, different form.

#### 7. Investigate unresolved price in 2024

One event in the 2024 report (2024-11-04, ETH 0.015) shows "unresolved" pricing method and 0.00 PLN revenue. Small amount but should be investigated and fixed.

### NOT STARTED

#### 8. Swedish tax reporting

Nothing exists for this. Needs:

- Research on Swedish rules for non-residents (Skatteverket obligations for people who moved abroad)
- Determine which forms are needed (K4 for crypto? Inkomstdeklaration 1?)
- Income conversion to SEK (NBP already supports SEK rates, but may need Riksbanken rates)
- Generate a report/summary that Sweden can accept
- Determine whether Sweden still considers you tax resident (10-year rule for shares -- does it apply to crypto?)

#### 9. PIT-28 ryczalt calculation module

No code exists. Would need to:

- Parse Clearstar XML invoices for amounts/dates
- Parse Conclave PDF invoices
- Calculate PLN revenue per NBP rates
- Track FX differences (roznice kursowe)
- Compare with monthly tax payments made
- Generate PIT-28 form field values

#### 10. PIT-36 income calculation module

No code for pre-JDG USDC salary income tax calculation (the personal income side of the barter doctrine).

---

## Verification Gaps

- **No cross-check between invoice amounts and exchange deposits** -- The system processes exchange data independently of invoices. A verification report matching "USDC received on Polygon" to "corresponding invoice" would build confidence.
- **No reconciliation report** -- A summary showing "total USDC received as salary" vs "total USDC sold on exchanges" vs "remaining USDC balance" would help verify nothing is missing.
- **2024 cost figure context** -- The tax-correction-plan.md estimated ~479K PLN costs for 2024 salary, but the computed report shows 778K PLN total costs (which includes all stablecoin deposits + trading fees, not just salary). This is correct behavior (cost pool includes ALL acquisitions), but worth understanding when cross-referencing.

---

## Recommended Next Steps (Priority Order)

| Priority | Action | Deadline |
|---|---|---|
| 1 | File 2024 PIT-38 korekta using generated numbers | ASAP (before Apr 30) |
| 2 | Build PIT-28 ryczalt calculator for Clearstar/Conclave invoices | Before Apr 30 |
| 3 | Build PIT-36 module for pre-JDG USDC salary (2025 Jan-Apr) | Before Apr 30 |
| 4 | Extract Conclave invoice amounts from PDFs | Before Apr 30 |
| 5 | File PIT-28, PIT-36, PIT-38 for 2025 | Apr 30, 2026 |
| 6 | Research Swedish tax obligations | May 2026 |
| 7 | Build Swedish tax report generator | May-Jun 2026 |
| 8 | File PIT-37 -> PIT-36 corrections for 2023/2024 | After deadline |
| 9 | Fix unresolved ETH price (2024-11-04) | After deadline |
| 10 | Add invoice-to-deposit reconciliation report | After deadline |

---

## Current System Output Summary

### PIT-38 Carry-Forward Chain

```
2023 PIT-38 (filed):
  Revenue:        226,115.71 PLN
  Costs (2023):   448,108.20 PLN
  Carry-forward:  221,992.49 PLN ────┐
                                      |
2024 PIT-38 (NEEDS FILING):          |
  Prior costs:    128,772.86 PLN  <───┘  (note: differs from 2023 PIT-38 filed
  Costs (2024):   778,181.67 PLN         carry-forward due to pre-residency cost
  Revenue:        785,508.57 PLN         adjustments in the calculator)
  Carry-forward:  121,445.96 PLN ────┐
                                      |
2025 PIT-38 (to be filed):           |
  Prior costs:    121,445.96 PLN  <───┘
  Costs (2025):   468,478.72 PLN
  Revenue:        271,316.95 PLN
  Carry-forward:  318,607.72 PLN ──── to 2026
```

### Forms Needed for 2025

| Form | Covers | Status |
|---|---|---|
| PIT-28 | JDG ryczalt income (Clearstar EUR invoices, May-Dec 2025) | Not started -- no code |
| PIT-36 | Pre-JDG USDC salary income (Conclave, Jan-Apr 2025) | Not started -- no code |
| PIT-38 | Crypto disposals (15 events, 0 tax due) | Numbers ready |

### Forms Needed as Corrections

| Form | Year | Issue |
|---|---|---|
| PIT-38 korekta | 2024 | Never filed -- protects ~700K PLN cost basis |
| PIT-36 korekta | 2023 | Replace PIT-37 (wrong form) + add PIT/ZG |
| PIT-36 korekta | 2024 | Replace PIT-37 (wrong form) + add PIT/ZG |
