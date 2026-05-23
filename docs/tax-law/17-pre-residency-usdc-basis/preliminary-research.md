# Preliminary Research: Pre-Residency USDC Salary Basis

Status: preliminary internal research note, prepared 2026-04-25.

This note records the issue for topic 17 before sending the question to external research agents. It is not a final filing policy.

## Why This Needs New Research

The current safe-default PIT-38 policy excludes pre-residency salary-paid USDC from the Polish cost pool, but it still uses a pseudo-Polish annual cost-pool chain for 2020-2022. That creates a fairness and correctness problem:

- pre-residency 2022 stablecoin disposals are being allowed to consume cost pool value,
- but pre-residency salary-paid stablecoins are excluded from costs,
- and the taxpayer was not yet Polish resident in 2022.

This may be the wrong frame. The better legal question may be:

1. Should Poland ignore pre-residency disposals entirely and start PIT-38 revenue only from the Polish residency date?
2. Which pre-residency acquisition costs can be imported into the first Polish PIT-38 year?
3. Can Sweden-taxed or foreign-taxed USDC compensation be imported as acquisition cost in the same way as Poland-taxed crypto remuneration?

## Existing Research Read

Relevant existing local sources:

- `docs/tax-law/09-residency-sweden-poland/synthesis-residency-transition.md`
- `docs/tax-law/03-crypto-capital-gains-pit38/synthesis-pit38-crypto-tax.md`
- `docs/tax-law/13-jdg-stablecoin-payments/synthesis-jdg-stablecoin-payments.md`
- `docs/tax-law/16-implementation-audit/synthesis-implementation-audit.md`
- `docs/tax-law/16-implementation-audit/filing-policy.md`
- `docs/todo/filing-summary.md`
- `docs/todo/pit38-filing-guide.md`

The strongest existing conclusions are:

- Polish tax residency starts prospectively from the actual move / centre-of-life transfer, not retroactively from January 1.
- Pre-residency fiat-to-crypto purchase costs are plausibly importable into Polish PIT-38 if documented and not already deducted abroad.
- Post-residency Poland-taxed crypto remuneration can plausibly become PIT-38 acquisition cost when later disposed.
- Pre-residency salary-paid USDC is not yet supported by the same direct authority and should not be merged silently into the default pool.

## Preliminary Source Checks

### 1. Polish residency can change during the year

Official MF residency explanations say a change of tax residence can occur during a tax year. Before the change, a person is taxed under the old residence / limited obligation framework; after the change, the new residence framework applies. The guidance also says lack of Polish residence means Poland taxes only Polish-source income.

Source: https://www.podatki.gov.pl/pit/wyjasnienia-pit/objasnienia-rezydencja/

Important lines checked:

- Polish residents are taxed on worldwide income.
- Non-residents are taxed only on Polish-source income.
- Change of residence can happen during the year.
- The example applies the change prospectively from the date the centre of life moved.

### 2. PIT-38 crypto costs are narrow

Official MF crypto guidance and PIT-38 guidance tie deductible costs to:

- documented expenses directly incurred to acquire virtual currency,
- and documented costs connected with disposing of virtual currency.

They also say excess costs are carried forward to the next year.

Sources:

- https://www.podatki.gov.pl/podatki-osobiste/pit/informacje-podstawowe/co-jest-opodatkowane/zbycie-kryptowalut/
- https://www.podatki.gov.pl/twoj-e-pit/pit-38-za-2025-rok/

### 3. KIS supports importing documented pre-residency purchase costs

KIS interpretation `0113-KDIPT2-3.4011.205.2025.2.NM` supports importing documented costs incurred before Polish residency into the first PIT-38 year after becoming Polish resident, where the costs were not deducted abroad.

Important nuance: the case describes costs "na zakup walut wirtualnych" and says costs incurred and not deducted before the residency change are first shown in the PIT-38 for the year the taxpayer became Polish resident. It does not directly address salary-paid crypto.

Source:

- https://www.inforlex.pl/dok/tresc%2CFOB0000000000006932617%2CInterpretacja-indywidualna-z-dnia-30-kwietnia-2025-r-Dyrektor-Krajowej-Informacji-Skarbowej-sygn-0113-KDIPT2-3-4011-205-2025-2-NM.html

### 4. KIS supports crypto remuneration basis when the receipt is taxed as Polish income

KIS interpretation `0112-KDIL2-2.4011.651.2023.1.WS` supports the view that when a Polish taxpayer receives virtual currency as payment for services, the receivable settled by the virtual currency is an expense directly incurred to acquire the virtual currency for later PIT-38 purposes.

Source:

- https://www.interpretacje.pl/pit/9353007%2Cskutki-podatkowe-zaplaty-za-usluge-kryptowaluta-interpretacja-011.html

KIS interpretation `0115-KDIT1.4011.22.2025.1.MR` similarly accepts that a crypto bonus included in PIT-36 employment income can be PIT-38 cost basis when later sold.

Source:

- https://www.inforlex.pl/dok/tresc%2CFOB0000000000006885875%2CInterpretacja-indywidualna-z-dnia-4-marca-2025-r-Dyrektor-Krajowej-Informacji-Skarbowej-sygn-0115-KDIT1-4011-22-2025-1-MR.html

### 5. Missing bridge

I did not find direct authority squarely combining these two rules:

- imported pre-residency costs after a residence change,
- plus compensation / salary paid in virtual currency before Polish residency and taxed in Sweden.

That is the exact topic for external research.

## Local Numerical Evidence

The current generated PIT-38 detail shows the issue.

### Current all-year engine output

| Year | Revenue | Current-year costs | Prior costs | Carry-forward |
|---|---:|---:|---:|---:|
| 2020 | 3,640.46 | 278,039.85 | 0.00 | 274,399.39 |
| 2021 | 413,682.55 | 735,213.28 | 274,399.39 | 595,930.12 |
| 2022 | 437,946.26 | 510,774.07 | 595,930.12 | 668,757.92 |
| 2023 | 411,143.91 | 703,072.73 | 668,757.92 | 960,686.74 |

This is not a filing recommendation. It shows what the current broad engine does.

### 2022 stablecoin revenue and excluded salary-cost tension

2022 revenue includes stablecoin disposals:

| Asset | 2022 revenue |
|---|---:|
| BUSD | 78,229.59 |
| USDC | 51,855.83 |
| USDT | 63,144.46 |
| Stablecoin total | 193,229.88 |

2022 cost events include salary USDC:

| Source | 2022 cost |
|---|---:|
| `fantom_salary` | 365,103.07 |
| `polygon_salary` | 138,798.60 |
| Salary total | 503,901.67 |

If the salary side is excluded because Poland did not tax the receipt, it may be incoherent to let the pre-residency stablecoin sales consume the importable Polish pool as if 2022 were a Polish PIT year.

### 2023 move-date split

The taxpayer moved to Poland on `2023-04-12` according to the rental-agreement fact record.

Current 2023 events split as:

| 2023 period | Revenue | Costs |
|---|---:|---:|
| Before 2023-04-12 | 147,030.09 | 202,150.16 |
| On/after 2023-04-12 | 264,113.82 | 500,922.55 |

Pre-move 2023 revenue is all MATIC disposal revenue. If residence starts on 2023-04-12, that revenue may not belong in Polish PIT-38.

### Simple scenario impact

If Polish PIT-38 starts with post-move 2023 revenue and current-year costs only:

| Opening imported pre-residency cost | 2023 carry | 2024 PIT-38 income | 2024 PIT-38 tax | 2025 PIT-38 income | 2025 PIT-38 tax | 2025 carry |
|---:|---:|---:|---:|---:|---:|---:|
| 0.00 | 236,808.73 | 60,634.23 | 11,520.50 | 73,945.70 | 14,049.68 | 0.00 |
| 294,073.39 | 530,882.12 | 0.00 | 0.00 | 0.00 | 0.00 | 159,493.46 |

The `294,073.39 PLN` opening cost is the current topic 16 "safe-default" carry amount produced by excluding pre-residency salary but still running the old pre-residency annual pool. That number itself needs review.

Approximate threshold: an opening imported cost of about `134,579.93 PLN` is enough to keep 2024 and 2025 PIT-38 tax at zero under the post-move-only model, assuming the current 2024 and 2025 figures are otherwise correct.

## Preliminary Working View

Do not file from this note alone.

My preliminary view is:

1. The synthetic 2020-2022 Polish cost-pool chain is legally suspect because those were not Polish PIT years.
2. Pre-residency disposals probably should not be Polish PIT-38 revenue.
3. Imported pre-residency costs should be based on documented costs not deducted/consumed abroad, not on a fake Polish annual pool unless research confirms that method.
4. Pre-residency salary-paid USDC remains the hardest point: evidence that it was taxed in Sweden helps the equity / double-taxation argument, but I have not found authority that makes it a safe default.
5. The external prompt should ask agents to challenge or confirm this directly, not repeat general crypto-cost rules.

