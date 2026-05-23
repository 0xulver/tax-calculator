# Synthesis: Pre-Residency USDC Basis and Split-Year PIT-38

Status: research synthesis for filing work, prepared 2026-04-25.

This document synthesizes the four external research outputs in this folder:

- `PIT-38 Pre-Residency Crypto Issue - ChatGPT 5.5 Pro.md`
- `Polish Crypto Tax Residency Split - Gemini 3.1 Deep Research.pdf`
- `Pre-Residency USDC PIT-38 Query - ChatGPT Deep Research.md`
- `Pre-Residency USDC Salary Basis and Split-Year PIT-38  Polish Tax Analysis - Perplexity.md`

Weighting used here follows the requested hierarchy:

1. ChatGPT 5.5 Pro - highest weight.
2. Gemini 3.1 Deep Research and ChatGPT Deep Research - second highest weight.
3. Perplexity - preliminary, lowest weight.

This is not a legal opinion. It is a working synthesis for deciding how to update the calculator outputs, filing guides, and evidence package.

## Bottom Line

The existing full-history Polish PIT-38 pool is outdated and should not be used as the filing model.

The four sources converge on the same core correction:

1. Polish PIT-38 should start from the Polish residency date, currently `2023-04-12`.
2. Crypto disposals before that date should be excluded from Polish PIT-38 revenue.
3. Pre-residency acquisition costs should not be imported through a synthetic Polish annual pool for 2020-2022.
4. The opening Polish cost basis should be rebuilt from assets actually held at the move date and costs not already consumed in Sweden.
5. Pre-residency salary-paid USDC is not a "definitely excluded" bucket. It is a supportable but KIS-dependent bucket if it was taxed in Sweden, documented, still held at the move date, and later disposed while Polish resident.

The newest ChatGPT Deep Research output adds one material nuance: if salary-paid USDC was swapped into another crypto before the move, the better frame is not a generic Polish "successor basis" claim. Sweden taxes crypto-to-crypto swaps and creates a Swedish acquisition cost in the replacement asset. The possible Polish import is therefore the Swedish surviving acquisition cost of the replacement asset held at the move date, not the old USDC as if the Swedish swap had never happened.

The key filing consequence is that the old question "how do we balance 2022 stablecoin sales against 2022 salary USDC in a Polish pool?" is probably the wrong question. The better answer is:

- 2022 stablecoin sales are not Polish PIT-38 revenue at all.
- 2022 salary USDC sold before the move is not a Polish cost or revenue item at all.
- 2022 salary USDC still held at the move date may become imported Polish PIT-38 basis when sold after the move, but that bucket needs strong evidence and preferably an individual interpretation if material.

## Consensus Findings

### 1. Exclude pre-residency disposals from Polish PIT-38 revenue

All four sources support split-year treatment.

For this taxpayer, Polish residency starts on `2023-04-12` based on the current fact record. Pre-move disposals belong outside Polish PIT-38 because the taxpayer was not yet subject to Polish unlimited tax liability.

Numerical impact from current data:

| Item | Existing broad engine | Split-year model |
|---|---:|---:|
| 2023 PIT-38 revenue | 411,143.91 PLN | 264,113.82 PLN |
| Pre-move 2023 revenue to remove | 147,030.09 PLN | excluded |

The excluded 2023 pre-move revenue is all MATIC disposal revenue from `2023-01-01` through `2023-04-11`.

The same logic applies more strongly to 2020-2022, when the taxpayer was Swedish resident.

### 2. Do not use the synthetic 2020-2022 Polish cost-pool chain

The external outputs agree that the old method is not just conservative or imperfect. It mixes incompatible systems:

- It includes pre-residency foreign disposals as if they were Polish PIT-38 revenue.
- It applies Polish annual pooling to years that were not Polish PIT-38 years.
- It creates a carry-forward amount that cannot be proven to represent only costs of assets still held when Polish residency began.

The current `294,073.39 PLN` opening imported cost figure is therefore not a reliable legal figure. It may be too low, too high, or accidentally close, but it must be rebuilt from transaction-level evidence.

### 3. Imported basis should be built from move-date inventory and Swedish surviving basis

The best-supported method is transaction-level tracing with Swedish K4 reconciliation:

1. Freeze crypto holdings at the start of Polish residency, using `2023-04-12` as the move date.
2. Identify assets actually held at the move date.
3. Trace each held asset back to its acquisition event or Swedish replacement-asset acquisition after a pre-move swap.
4. Import only acquisition costs that are legally recognized under Polish PIT-38 and not already deducted or consumed in Sweden.
5. Use Swedish K4 or equivalent Swedish tax records to show which costs were consumed by pre-move Swedish-taxed disposals and swaps.

This method replaces the old annual fake-pool carry-forward.

### 4. Fiat-to-crypto purchases are the strongest imported-cost bucket

Pre-residency fiat-to-crypto purchases are the cleanest imported costs if all conditions are met:

- documented purchase,
- asset or traceable successor still held at the move date,
- cost not already used in Swedish K4,
- NBP conversion support available.

This is the low-risk bucket to compute first.

### 5. Post-residency Poland-taxed USDC remuneration remains valid cost basis

The sources continue to support the existing policy for post-residency remuneration:

- USDC received after Polish residency as salary, services, or JDG remuneration should first be reported as Polish income where applicable.
- When later sold for fiat, the already-taxed remuneration value can be PIT-38 acquisition cost.

This is not the disputed bucket.

### 6. Pre-residency Sweden-taxed salary USDC is supportable but not a safe default without evidence

This is the main issue.

The old topic 16 safe-default logic was too blunt if it said pre-residency salary USDC must be excluded because Poland did not tax the receipt. The better synthesis is:

- If the taxpayer received USDC as compensation before Polish residency,
- and Sweden taxed that compensation as income,
- and the USDC was still held at the Polish move date,
- and the same USDC was later sold while Polish resident,
- then treating the settled salary or service receivable value as imported PIT-38 acquisition cost is supportable.

But this is not as safe as fiat purchase costs. There is no direct KIS ruling squarely confirming Swedish-taxed pre-residency salary USDC as Polish imported PIT-38 basis. It depends on extending two accepted lines of authority:

- pre-residency costs not consumed abroad can be imported into Polish PIT-38,
- crypto received for services or employment can be acquired for consideration because the receivable was settled by the crypto transfer.

The evidence burden is high.

### 7. Pre-move crypto-to-crypto replacement-asset basis is the main conflict

The sources diverge on salary USDC swapped into another crypto before the move and sold after the move.

Gemini is more favorable. It suggests the labor-cost basis can carry through a pre-move crypto-to-crypto swap because Poland treats crypto-to-crypto swaps as neutral.

ChatGPT 5.5 Pro and Perplexity are more cautious. They treat this as high-risk because Polish PIT-38 does not recognize crypto-to-crypto swaps as taxable events or cost-generating events, while Swedish K4 may already have consumed cost through the swap.

ChatGPT Deep Research gives the best practical reconciliation: because Sweden taxes the pre-move swap, the USDC basis is normally consumed in Sweden and the replacement token receives a Swedish acquisition cost. The possible importable cost is then the surviving Swedish acquisition cost of the replacement asset actually held on `2023-04-12`, if it was not later consumed before the move. This is still disputed for Polish purposes, but it is stronger than an unsupported "USDC basis carries forever" theory.

Following the requested source weighting, this synthesis treats the buckets as follows:

| Bucket | Working treatment |
|---|---|
| Pre-residency salary USDC sold before move | Exclude entirely from Polish PIT-38. |
| Pre-residency salary USDC still held at move and sold after move | Supportable imported cost, evidence-heavy, KIS-dependent. |
| Pre-residency salary USDC deposited to exchange after move, same token still owned | Deposit is neutral; original basis analysis remains. |
| Pre-residency salary USDC swapped before move into another crypto | Separate replacement-asset basis bucket. Potentially supportable if Swedish K4/tax records show the replacement asset's surviving cost at move date, but still KIS-dependent and not safe-default. |

## Calculation Impact

Under the split-year model, current known 2023 figures become:

| 2023 period | Revenue | Costs |
|---|---:|---:|
| Before `2023-04-12` | 147,030.09 PLN | 202,150.16 PLN |
| On/after `2023-04-12` | 264,113.82 PLN | 500,922.55 PLN |

The pre-move row should not enter Polish PIT-38 revenue.

The post-move 2023 costs of `500,922.55 PLN` remain in the Polish period, subject to normal evidence and source classification.

The opening imported basis is the variable. The simplified scenario table is:

| Opening imported pre-residency cost | 2023 carry | 2024 PIT-38 income | 2024 PIT-38 tax | 2025 PIT-38 income | 2025 PIT-38 tax | 2025 carry |
|---:|---:|---:|---:|---:|---:|---:|
| 0.00 PLN | 236,808.73 PLN | 60,634.23 PLN | 11,520.50 PLN | 73,945.70 PLN | 14,049.68 PLN | 0.00 PLN |
| 60,634.23 PLN | 297,442.96 PLN | 0.00 PLN | 0.00 PLN | 73,945.70 PLN | 14,049.68 PLN | 0.00 PLN |
| 134,579.93 PLN | 371,388.66 PLN | 0.00 PLN | 0.00 PLN | 0.00 PLN | 0.00 PLN | 0.00 PLN |
| 294,073.39 PLN old placeholder | 530,882.12 PLN | 0.00 PLN | 0.00 PLN | 0.00 PLN | 0.00 PLN | 159,493.46 PLN |

Interpretation:

- If valid imported basis is at least about `134,579.93 PLN`, 2024 and 2025 PIT-38 tax remain zero under the simplified split-year model.
- If valid imported basis is zero, 2024 and 2025 PIT-38 tax appears.
- The old `294,073.39 PLN` amount should not be used as proof. It is only a placeholder showing sensitivity.

## Evidence Needed

### Move-date inventory

Required:

- complete holdings at `2023-04-12`,
- wallet and exchange balances,
- token quantities,
- chain and exchange provenance,
- disposal history after the move.

This is the foundation of the new calculation.

### Swedish K4 / Swedish reporting

Required:

- Swedish K4 or equivalent disposal schedules for 2020, 2021, 2022, and the pre-move part of 2023,
- Swedish tax assessment or submitted report records,
- evidence that pre-move disposal costs were already consumed in Sweden,
- evidence that claimed imported costs were not consumed in Sweden.

For the salary-USDC bucket, the Swedish records should distinguish income taxation at receipt from capital-gain cost deductions on later disposal.

For pre-move swaps, the Swedish records need to show the sale of USDC, the Swedish acquisition cost assigned to the replacement token, and whether that replacement-token basis survived to `2023-04-12`.

### Fiat purchase costs

Required:

- exchange CSVs,
- bank and card records,
- purchase confirmations,
- NBP rate evidence for PLN conversion,
- proof that the purchased assets or eligible traced assets were still held at move date.

### Salary / compensation USDC

Required:

- contracts or service agreements,
- invoices or compensation statements,
- on-chain receipt hashes,
- wallet ownership evidence,
- Swedish income reporting showing the compensation was taxed in Sweden,
- proof the same USDC was held at move date if relying on the stronger same-token theory,
- if the USDC was swapped before the move, Swedish K4 or workpapers showing the replacement asset and surviving Swedish basis,
- the Swedish-taxed remuneration value or invoice/contract value at receipt, then PLN conversion using the relevant NBP day-before rate.

## Filing Posture Options

### Conservative

Use split-year revenue. Import only documented pre-residency fiat-to-crypto purchase costs for assets held at move date. Exclude pre-residency salary USDC.

This has the lowest legal risk but may overstate tax if salary USDC is a valid cost.

### Supportable

Use split-year revenue. Import documented fiat purchase costs plus documented Sweden-taxed pre-residency salary USDC that was still held at the move date and sold after Polish residency began.

This reflects the main ChatGPT 5.5, Gemini, and ChatGPT Deep Research economic/legal theory, but it is KIS-dependent.

This posture can also include a replacement-asset basis bucket where salary USDC was swapped before the move, but only if Swedish records cleanly show the replacement asset, its Swedish acquisition cost, and that the basis survived to the Polish move date.

### High-risk

Use split-year revenue and also import salary-USDC basis through pre-move crypto-to-crypto swaps without a clean Swedish replacement-asset basis computation or without KIS protection.

This is not recommended as a default. It should be separated from the main filing numbers unless an individual interpretation or adviser explicitly supports it.

### Not Recommended

Run 2020-2022 and pre-move 2023 through a synthetic Polish PIT-38 annual pool.

This is the outdated method.

## Recommended Working Plan

1. Stop using the old full-history PIT-38 carry-forward as the filing source.
2. Rebuild `2023-04-12` move-date inventory.
3. Reconcile Swedish K4/reporting against all pre-move disposals.
4. Compute imported basis in three separate layers:
   - Layer A: documented fiat-to-crypto costs, not consumed in Sweden.
   - Layer B: documented Sweden-taxed salary USDC still held at move date.
   - Layer C: documented replacement-asset basis from salary USDC swapped before the move, using Swedish K4/tax survival records.
5. First test whether Layer A alone reaches `134,579.93 PLN`.
6. If Layer A reaches the threshold, file PIT-38 using the low-risk imported-cost position and keep salary-USDC as backup / interpretation topic.
7. If Layer A does not reach the threshold, test Layer B and decide whether the tax difference justifies using the supportable salary-USDC position now.
8. Keep Layer C out of default numbers unless the Swedish replacement-asset computation is strong and the posture is explicitly chosen.
9. Prepare an ORD-IN individual interpretation request if Layer B or Layer C materially changes tax due.

## KIS Interpretation Focus

If an individual interpretation is submitted, the main question should not be the whole PIT-38 calculation. It should focus on the hard unresolved point:

Whether USDC received before Polish residency as compensation for services, taxed as income in Sweden, documented by invoices/contracts and on-chain receipts, and still held when Polish residency began, can be treated as a documented expense directly incurred to acquire virtual currency for Polish PIT-38 when that USDC is sold after becoming Polish resident.

The new ChatGPT Deep Research memo also supports asking a separate replacement-asset question:

Whether, if the Sweden-taxed salary USDC was exchanged before Polish residency for another virtual currency and that replacement asset remained held on `2023-04-12`, the importable Polish cost is the Swedish acquisition cost / surviving basis of the replacement asset, provided it was not deducted or consumed before the residency change.

Secondary questions:

- whether Swedish income taxation satisfies the anti-double-taxation logic that Polish PIT-36/PIT-28 recognition provides in domestic KIS crypto-remuneration cases,
- whether the same-token salary-USDC cost should be valued using the Swedish-taxed remuneration value or invoice/contract amount at receipt, translated to PLN using the relevant NBP day-before rate,
- whether replacement-asset basis after a pre-move swap should be valued from Swedish K4 / Swedish acquisition-cost records, then translated to PLN under Article 11a day-before logic,
- whether excess cost may carry forward under the normal PIT-38 crypto rules.

Do not bury this issue inside a broad filing-policy request. The broader split-year exclusion is much more certain; the salary-USDC bridge is the issue that needs protection.

## What Changes In Current Filing Docs

The current docs should be updated so that:

- `docs/todo/filing-summary.md` no longer treats the topic 16 PIT-38 numbers as final.
- `docs/todo/pit38-filing-guide.md` is marked provisional until move-date imported basis is rebuilt.
- `docs/tax-law/16-implementation-audit/filing-policy.md` is superseded for PIT-38 split-year/imported-cost mechanics by this topic 17 synthesis.
- the PIT-38 calculator/report should show a separate split-year model and should not silently import the old synthetic carry-forward.

## Current Decision

Use the split-year / imported-cost model as the new working policy.

Do not conclude that pre-residency salary USDC is unusable. Instead, classify it:

- same-token, Sweden-taxed, held at move date: supportable, evidence-heavy, KIS-dependent;
- sold before move: excluded entirely;
- deposited after move: neutral custody movement;
- swapped before move into other crypto: separate replacement-asset basis bucket; potentially supportable with Swedish K4/surviving-basis proof, but still KIS-dependent and not safe-default.

The immediate practical task is not more generic research. It is reconstructing the April 12, 2023 inventory and Swedish-consumed cost ledger. More legal work is useful only if targeted at the salary-USDC individual interpretation question.
