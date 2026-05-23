# Research: Pre-Residency USDC Salary Basis and Split-Year PIT-38

## Objective

We need focused external legal research on one high-impact Polish PIT-38 issue:

**When a taxpayer moves from Sweden to Poland during 2023, can pre-residency USDC salary / compensation become Polish PIT-38 acquisition cost, and should pre-residency crypto disposals be excluded entirely rather than run through a synthetic Polish annual cost pool?**

This is not a generic crypto-tax memo. The goal is to resolve a concrete filing-method dispute that could materially change 2023-2025 PIT-38 corrections.

Treat this as an adversarial review. If the current working policy is wrong, say so clearly.

## External Agent Instructions

Do not assume access to any local filesystem, code repository, CSVs, PDFs, or markdown files unless they are pasted or attached separately. Work from the facts in this prompt and from your own legal research.

Use primary and high-authority sources where possible:

- Polish PIT Act provisions,
- Polish Ministry of Finance / podatki.gov.pl guidance,
- KIS individual interpretations,
- Polish administrative court judgments,
- Poland-Sweden double tax treaty,
- Swedish tax law only where it changes whether costs were already deducted / consumed before the Polish move.

Clearly separate:

- black-letter law,
- published authority / KIS practice,
- inference,
- practical filing recommendation.

## Taxpayer Facts

- Swedish citizen.
- Lived in Sweden before moving to Poland.
- Moved to Poland on `2023-04-12` according to the rental-agreement fact record.
- PESEL / Polish registration date: `2023-05-04`.
- Sold Swedish apartment on `2023-09-07`.
- First Polish tax filing year under review: 2023.
- Crypto trading and liquidation happened mainly on Binance and Kraken.
- Some fiat-to-crypto purchases happened before Polish residency through Kraken, Binance, Coinbase, Celsius/Simplex, and FTX.
- Pre-JDG work was paid in USDC on-chain, including before Polish residency.
- Post-residency USDC remuneration was or should be reported as Polish income, and then treated as PIT-38 acquisition cost when disposed.
- Pre-residency salary / compensation paid in USDC may have been reported and taxed in Sweden. Assume evidence can include contracts, on-chain transfer history, invoices/payment records, and Swedish tax returns.

## Why This Is Urgent

The current tax calculator has two possible frames:

1. **Synthetic full-history Polish pool**
   - Run 2020-2022 and Jan-Mar 2023 through Polish-style annual PIT-38 pooling even though the taxpayer was not Polish resident.
   - Then carry the remaining pool into 2023.

2. **Split-year / imported-cost model**
   - Exclude all pre-residency disposals from Polish PIT-38 revenue.
   - Start Polish PIT-38 revenue from the Polish residency date.
   - Import only eligible pre-residency acquisition costs that were documented and not deducted/consumed abroad.

The second model appears more coherent, but we need external confirmation.

## Existing Research Baseline

Prior internal/external research reached these working conclusions. Re-open them only if this topic depends on a nuance that was previously missed.

- Polish tax residency begins prospectively from the actual move / centre-of-life transfer, not retroactively from January 1.
- Poland-Sweden DTT tie-breaker rules should allocate post-move crypto gains to Poland, assuming Polish residence from the move date.
- Native crypto should generally fall under the residual capital-gains article, not real estate / PE rules.
- Poland has no general immigration step-up for crypto basis.
- Documented pre-residency fiat-to-crypto purchase costs may be imported into Polish PIT-38 if not already deducted abroad.
- Post-residency Poland-taxed crypto remuneration can become PIT-38 acquisition cost when later disposed.
- Stablecoin deposits are transfer/reconciliation events and should not create cost basis by themselves.

## Preliminary Source Anchors

Please verify these sources independently and look for better / newer authorities.

### Official Polish crypto guidance

MF guidance states that PIT-38 virtual-currency costs are documented expenses directly incurred to acquire virtual currency plus disposal-related costs, and that excess costs carry forward:

- https://www.podatki.gov.pl/podatki-osobiste/pit/informacje-podstawowe/co-jest-opodatkowane/zbycie-kryptowalut/
- https://www.podatki.gov.pl/twoj-e-pit/pit-38-za-2025-rok/

### Official Polish residency guidance

MF residency guidance says tax residence can change during a tax year and describes the consequences prospectively:

- https://www.podatki.gov.pl/pit/wyjasnienia-pit/objasnienia-rezydencja/

### KIS on importing pre-residency purchase costs

KIS interpretation `0113-KDIPT2-3.4011.205.2025.2.NM` accepts that documented costs incurred before becoming Polish resident can be shown in the first Polish PIT-38 year after the residency change if not deducted abroad:

- https://www.inforlex.pl/dok/tresc%2CFOB0000000000006932617%2CInterpretacja-indywidualna-z-dnia-30-kwietnia-2025-r-Dyrektor-Krajowej-Informacji-Skarbowej-sygn-0113-KDIPT2-3-4011-205-2025-2-NM.html

Key point to test: this case is about costs for purchase of virtual currencies, not salary-paid crypto.

### KIS on crypto remuneration becoming PIT-38 cost basis

KIS interpretation `0112-KDIL2-2.4011.651.2023.1.WS` accepts that virtual currency received for services is an "odpłatne nabycie"; the settled receivable for services is the directly incurred expense for acquiring the virtual currency:

- https://www.interpretacje.pl/pit/9353007%2Cskutki-podatkowe-zaplaty-za-usluge-kryptowaluta-interpretacja-011.html

KIS interpretation `0115-KDIT1.4011.22.2025.1.MR` accepts similar treatment for a crypto bonus already included in Polish PIT-36 employment income:

- https://www.inforlex.pl/dok/tresc%2CFOB0000000000006885875%2CInterpretacja-indywidualna-z-dnia-4-marca-2025-r-Dyrektor-Krajowej-Informacji-Skarbowej-sygn-0115-KDIT1-4011-22-2025-1-MR.html

Key point to test: these authorities involve Polish-taxed remuneration. They do not directly answer whether foreign-taxed, pre-residency remuneration has the same Polish PIT-38 basis effect.

## Current Numbers Showing The Problem

The local calculator currently produces an all-history Polish-style pool. These numbers are provided to help quantify the stakes, not as a request to audit every transaction.

### Current all-year engine output

| Year | Revenue | Current-year costs | Prior costs | Carry-forward |
|---|---:|---:|---:|---:|
| 2020 | 3,640.46 | 278,039.85 | 0.00 | 274,399.39 |
| 2021 | 413,682.55 | 735,213.28 | 274,399.39 | 595,930.12 |
| 2022 | 437,946.26 | 510,774.07 | 595,930.12 | 668,757.92 |
| 2023 | 411,143.91 | 703,072.73 | 668,757.92 | 960,686.74 |

### 2022 tension

2022 revenue includes stablecoin disposals:

| Asset | 2022 revenue |
|---|---:|
| BUSD | 78,229.59 |
| USDC | 51,855.83 |
| USDT | 63,144.46 |
| Stablecoin total | 193,229.88 |

2022 cost events include pre-residency salary / compensation in USDC:

| Source | 2022 cost |
|---|---:|
| `fantom_salary` | 365,103.07 |
| `polygon_salary` | 138,798.60 |
| Salary total | 503,901.67 |

The current safe-default policy excludes the 2022 salary-cost bucket because Poland did not tax the receipt. But if the taxpayer was not Polish resident in 2022, should those 2022 stablecoin disposals be in the Polish pool at all?

### 2023 move-date split

The taxpayer moved to Poland on `2023-04-12`.

| 2023 period | Revenue | Costs |
|---|---:|---:|
| Before 2023-04-12 | 147,030.09 | 202,150.16 |
| On/after 2023-04-12 | 264,113.82 | 500,922.55 |

Pre-move 2023 revenue is all MATIC disposal revenue. If Polish residence begins on 2023-04-12, should that revenue be excluded from Polish PIT-38?

### Scenario impact under post-move-only revenue

If Polish PIT-38 starts with post-move 2023 revenue and current-year costs only:

| Opening imported pre-residency cost | 2023 carry | 2024 PIT-38 income | 2024 PIT-38 tax | 2025 PIT-38 income | 2025 PIT-38 tax | 2025 carry |
|---:|---:|---:|---:|---:|---:|---:|
| 0.00 | 236,808.73 | 60,634.23 | 11,520.50 | 73,945.70 | 14,049.68 | 0.00 |
| 294,073.39 | 530,882.12 | 0.00 | 0.00 | 0.00 | 0.00 | 159,493.46 |

The `294,073.39 PLN` opening cost is the current topic 16 "safe-default" amount after excluding pre-residency salary but still running the pre-residency synthetic Polish annual pool. It may be too low, too high, or methodologically wrong.

Approximate threshold: if at least `134,579.93 PLN` of opening imported pre-residency cost is valid, then 2024 and 2025 PIT-38 tax stays at zero under this simplified post-move-only model, assuming the 2024 and 2025 figures are otherwise correct.

## Research Questions

### A. Split-year PIT-38 revenue

1. For a taxpayer who becomes Polish tax resident on `2023-04-12`, should Polish PIT-38 for 2023 include crypto-to-fiat disposals from January through April 11, 2023?
2. Should Polish PIT-38 include any revenue from 2020-2022 disposals when the taxpayer was Swedish resident and not Polish resident?
3. Does the answer change if the disposed assets were held on exchanges also accessible after the move, or if the proceeds were later brought to Poland?
4. Under the Poland-Sweden DTT, are pre-move native crypto gains taxable only in Sweden, only in Poland, or potentially both with relief?

### B. Method for importing pre-residency costs

5. When KIS says pre-residency costs not deducted before the residency change can be shown in the first Polish PIT-38 year, how should "not deducted" or "not consumed" be measured?
6. Is the right method transaction-level tracing to assets still held at the move date?
7. Is it acceptable to run a Polish-style annual aggregate pool for foreign-residency years and import the remainder?
8. Should pre-residency sales reduce the importable pool only if the costs were actually deducted in Sweden / used in Swedish K4 calculations?
9. How do Swedish crypto rules affect this? Sweden generally taxes crypto-to-crypto swaps, unlike Poland. Does that mean Swedish K4 / Swedish cost-basis records are the controlling evidence for what costs were consumed before the move?

### C. Pre-residency salary-paid USDC

10. Can USDC received as salary / compensation before Polish residency become Polish PIT-38 acquisition cost if the taxpayer later sells it while Polish resident?
11. Does it matter that the USDC compensation was reported and taxed in Sweden?
12. Does foreign tax recognition play the same anti-double-taxation role as Polish PIT-36 / PIT-28 recognition in KIS interpretations?
13. Does the answer differ between:
    - pre-residency salary USDC sold before moving to Poland,
    - pre-residency salary USDC still held on the move date and sold after becoming Polish resident,
    - pre-residency salary USDC swapped into another crypto before the move and sold after the move,
    - pre-residency salary USDC deposited to an exchange after the move?
14. If this bucket is allowed, what PLN value should be used:
    - Swedish taxed SEK value converted to PLN,
    - historical USD/USDC value using Polish NBP USD rate from day before receipt,
    - actual fiat amount under contract/invoice,
    - or another method?
15. If this bucket is not safe as a default, is it still a defensible aggressive position with an individual interpretation request?

### D. Evidence and filing posture

16. What evidence should be retained for each bucket:
    - exchange / card fiat purchases,
    - salary / compensation USDC,
    - Swedish tax reporting,
    - wallet-chain provenance,
    - exchange disposals?
17. What does the taxpayer need from Swedish filings or K4-style records to prove costs were not already used?
18. Should the taxpayer file now with a conservative position and later amend if an individual interpretation confirms the aggressive basis?
19. What exact individual-interpretation question should be submitted to KIS if the salary-USDC bucket matters?

## Required Output

Please produce:

1. **Bottom-line recommendation**: which model should be used for 2023-2025 PIT-38 filings.
2. **Authority table**: source, holding, relevance, and confidence.
3. **Bucket table** with treatment and confidence for:
   - pre-residency fiat-to-crypto purchases,
   - pre-residency salary / compensation USDC taxed in Sweden and still held at move,
   - pre-residency salary / compensation USDC sold before move,
   - post-residency Poland-taxed USDC remuneration,
   - deposit-only stablecoin transfers,
   - pre-move 2023 disposals.
4. **Calculation-method recommendation**: whether to use synthetic Polish annual pooling for 2020-2022, transaction-level tracing, Swedish K4 consumption, or another method.
5. **Filing risk assessment**:
   - conservative,
   - supportable,
   - aggressive but arguable,
   - not recommended.
6. **Practical next steps** for finishing the actual Polish filing before the deadline.
7. **Draft KIS interpretation questions** focused on the pre-residency salary-USDC facts.

Do not just restate that "costs must be documented." The central issue is whether pre-residency foreign-taxed compensation paid in crypto is a cost at all for Polish PIT-38, and whether pre-residency sales should be excluded rather than consuming the Polish pool.

