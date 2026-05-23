# External Research Prompt: PIT-38 Filing Audit Before Submission

Date prepared: 2026-04-27  
Jurisdiction: Poland  
Return type: PIT-38, virtual currency section  
Urgency: Filing deadline is 2026-04-30. Please prioritize errors that would
change the submitted PIT-38 values or materially change audit risk.

## Task For External Research Agent

You are reviewing a proposed Polish PIT-38 filing package before submission.
Please perform an independent legal, arithmetic, and evidence audit. Do not
assume the current filing posture is correct. Challenge the interpretation,
field mapping, carry-forward chain, and evidence sufficiency.

Please use primary Polish sources where possible:

- Polish PIT Act provisions on virtual currencies, income, costs, and
  carry-forward of virtual-currency costs.
- Official Ministry of Finance / e-Deklaracje / e-Urzad guidance for PIT-38
  fields for 2023, 2024, and 2025.
- KIS interpretations or administrative-court decisions if relevant to
  pre-residency cost basis, crypto-to-crypto transactions, DeFi wrappers,
  borrowed/debt-funded tokens, receipt tokens, and salary/remuneration paid in
  crypto.

If you cannot access a cited local file, say exactly which file you need and why.
Do not invent missing evidence.

## Factual Background

The taxpayer moved tax residence from Sweden to Poland during 2023. The working
Polish residency start date for PIT-38 is:

```text
2023-04-12
```

The proposed PIT-38 model is a split-year model:

- Polish PIT-38 revenue starts from `2023-04-12`.
- Pre-residency crypto disposals are excluded from Polish PIT-38.
- Pre-residency costs are not reconstructed using a synthetic full-history
  Polish pool.
- Instead, pre-residency acquisition/replacement basis is imported only through
  a documented move-date asset/basis ledger.
- Polish crypto reporting uses annual cost pooling, not FIFO.
- Crypto-to-crypto swaps are treated as non-taxable for Polish PIT-38, but they
  may matter for tracing replacement basis into move-date assets.

The selected posture is called:

```text
split_year_high_risk
```

The name means the package includes Layer C replacement/successor basis through
pre-move DeFi and crypto-to-crypto transformations. It does not mean the package
is knowingly unsupported. The request is to audit whether this filing posture is
legally and evidentially defensible enough to submit now.

## Proposed Forms To Submit

The taxpayer intends to submit:

1. PIT-38 correction for 2023.
2. PIT-38 for 2024. Use a correction only if e-Urzad shows an auto-accepted
   PIT-38; otherwise submit as a first/late PIT-38 for 2024.
3. PIT-38 for 2025.

All proposed PIT-38 returns have `0 PLN` tax due, but the carry-forward chain is
important.

## Proposed PIT-38 Values

### 2023 PIT-38 Correction

Use the PIT-38 form for tax year 2023. In the virtual-currency section:

| Field | Proposed value PLN |
| --- | ---: |
| Poz. 34 - Revenue | 264,113.82 |
| Poz. 35 - Costs incurred in 2023 | 500,922.56 |
| Poz. 36 - Costs from prior years / imported basis | 588,848.16 |
| Poz. 37 - Income | 0.00 |
| Poz. 38 - Costs carried forward to 2024 | 825,656.90 |

Check:

```text
500,922.56 + 588,848.16 - 264,113.82 = 825,656.90
```

### 2024 PIT-38

Use the PIT-38 form for tax year 2024. In the virtual-currency section:

| Field | Proposed value PLN |
| --- | ---: |
| Poz. 34 - Revenue | 785,654.54 |
| Poz. 35 - Costs incurred in 2024 | 488,065.61 |
| Poz. 36 - Costs from prior years | 825,656.90 |
| Poz. 37 - Income | 0.00 |
| Poz. 38 - Costs carried forward to 2025 | 528,067.97 |

Check:

```text
488,065.61 + 825,656.90 - 785,654.54 = 528,067.97
```

### 2025 PIT-38

Use the PIT-38 form for tax year 2025. In the virtual-currency section:

| Field | Proposed value PLN |
| --- | ---: |
| Poz. 36 - Revenue | 271,316.95 |
| Poz. 37 - Costs incurred in 2025 | 215,310.63 |
| Poz. 38 - Costs from prior years | 528,067.97 |
| Poz. 39 - Income | 0.00 |
| Poz. 40 - Costs carried forward to 2026 | 472,061.65 |

Check:

```text
215,310.63 + 528,067.97 - 271,316.95 = 472,061.65
```

## Generated Reports To Audit

Use only this selected output folder:

```text
outputs/pit38_max_no_debt_plus_oath_weth_dola_tge_rfgrain/
```

Important files:

- `pit38_policy_summary.md`
- `pit38_results.json`
- `pit38_detail.json`
- `pit38_report_2023.md`
- `pit38_report_2024.md`
- `pit38_report_2025.md`

Do not use root-level `outputs/pit38_report_*.md`; those may be stale.

The selected output currently says:

| Year | Revenue PLN | Current costs PLN | Prior/imported costs PLN | Income PLN | Tax PLN | Carry-forward PLN |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 2023 | 264,113.82 | 500,922.56 | 588,848.16 | 0.00 | 0.00 | 825,656.90 |
| 2024 | 785,654.54 | 488,065.61 | 825,656.90 | 0.00 | 0.00 | 528,067.97 |
| 2025 | 271,316.95 | 215,310.63 | 528,067.97 | 0.00 | 0.00 | 472,061.65 |

The generated reports include revenue-event tables, cost-event tables, NBP rates,
and verification checksum rows. Please audit whether the event tables match the
field totals.

## Current-Year Revenue And Cost Evidence

The current-year revenue/cost event tables are in:

- `outputs/pit38_max_no_debt_plus_oath_weth_dola_tge_rfgrain/pit38_report_2023.md`
- `outputs/pit38_max_no_debt_plus_oath_weth_dola_tge_rfgrain/pit38_report_2024.md`
- `outputs/pit38_max_no_debt_plus_oath_weth_dola_tge_rfgrain/pit38_report_2025.md`

The normalized transaction ledger behind the reports is:

```text
outputs/normalized_all_exchanges.csv
```

Relevant exchange/input sources include:

- `docs/crypto-cex-transactions/binance/binance_all_transactions_2020_2025.csv`
- `docs/crypto-cex-transactions/binance/binance_fiat_counterparty_overrides.csv`
- Kraken normalized/export files under `docs/crypto-cex-transactions/kraken/`
- FTX normalized/export files under `docs/crypto-cex-transactions/ftx/`
- Manual salary/purchase input files under `docs/crypto-transactions/`

Please audit especially:

1. Whether each post-residency crypto-to-fiat disposal is included as revenue.
2. Whether each post-residency fiat-to-crypto purchase, taxed crypto
   remuneration, or supported purchase is included as current-year cost only
   once.
3. Whether crypto-to-crypto swaps are correctly excluded from direct PIT-38
   revenue/cost totals, while still preserved for basis tracing.
4. Whether NBP rates appear to use the correct business-day-before rule.
5. Whether the two June 2025 Binance Paymonade USDC purchases and one small
   November 2024 Binance Paymonade ETH sale are correctly repaired by manual
   fiat-counterparty evidence:
   - 2025-06-20: 2,000 EUR -> 2,275.36649 USDC, 8,543.40 PLN cost.
   - 2025-06-22: 2,200 EUR -> 2,499.60415945 USDC, 9,395.98 PLN cost.
   - 2024-11-04: 0.015 ETH -> estimated 33.53231693 EUR, 145.97 PLN revenue.

Private reconciliation notes for these repairs:

- `private/evidence/fiat/2025-06-harmoniie-paymonade-binance-reconciliation.md`
- `private/evidence/fiat/fiat-counterparty-normalization-audit-2026-04-27.md`

## Imported Pre-Residency Basis

The proposed imported pre-residency basis for 2023 is:

```text
588,848.16 PLN
```

Breakdown in the calculator:

| Imported layer | Amount PLN |
| --- | ---: |
| Layer A fiat/direct/reviewable purchase costs | 77,955.80 |
| Layer C pre-move successor / replacement basis | 510,892.36 |
| Total imported basis | 588,848.16 |

The selected imported basis is built from these components:

| Candidate | Proposed amount PLN | Evidence file / workpaper | Included? |
| --- | ---: | --- | --- |
| Koinly-matched reviewable move-date rows | 77,955.80 | `move-date-cost-provenance.md` | Yes, as Layer A/base reviewable pool |
| Ethos WBTC trove collateral, full roll-forward | 142,580.44 | `move-date-wbtc-basis-rollforward.md`, `move-date-wbtc-cdp-basis-trace.md`, `move-date-cdp-positions.md` | Yes |
| GLP USDC.e predecessor | 44,138.35 | `move-date-basis-decision.md` | Yes |
| `rf-soWETH` WETH inputs | 5,292.90 | `move-date-basis-decision.md`, `move-date-unwind-workpaper.md` | Yes |
| BPT-GTRAIN ETH-only input | 25,964.04 | `move-date-basis-decision.md`, `move-date-unwind-workpaper.md` | Yes |
| BPT-GTRAIN stablecoin-funded GRAIN input | 100,518.44 | `move-date-gtrain-grain-provenance.md` | Yes |
| WETH/OATH LP WETH-linked component | 159,526.15 | `move-date-oath-provenance.md` | Yes |
| WETH/OATH LP DOLA-funded OATH component | 17,172.86 | `move-date-oath-provenance.md` | Yes |
| OATH TGE/LGE WFTM payment-side proof | 15,596.93 | `move-date-oath-tge-payment-scan.md` | Yes |
| `rf-grain-OP` surviving OP-funded receipt basis | 102.25 | `move-date-basis-decision.md` | Yes |

Arithmetic check:

```text
77,955.80
+ 142,580.44
+ 44,138.35
+ 5,292.90
+ 25,964.04
+ 100,518.44
+ 159,526.15
+ 17,172.86
+ 15,596.93
+ 102.25
= 588,848.16 PLN
```

Core imported-basis evidence folder:

```text
private/evidence/onchain/move-date-inventory-2023-04-12/
```

Key private workpapers:

- `move-date-inventory-2023-04-12.md`
- `move-date-token-balances.csv`
- `move-date-reconciliation-exceptions.csv`
- `move-date-cost-provenance.md`
- `move-date-cost-provenance.csv`
- `move-date-basis-decision.md`
- `move-date-supportable-basis-candidates.csv`
- `move-date-unwind-workpaper.md`
- `move-date-unwind-traces.csv`
- `move-date-cdp-positions.md`
- `move-date-cdp-positions.csv`
- `move-date-cdp-transactions.csv`
- `move-date-wbtc-cdp-basis-trace.md`
- `move-date-wbtc-cdp-basis-trace.csv`
- `move-date-wbtc-swedish-evidence-checklist.md`
- `move-date-wbtc-swedish-evidence-checklist.csv`
- `move-date-wbtc-basis-rollforward.md`
- `move-date-wbtc-basis-rollforward.csv`
- `move-date-wbtc-stablecoin-source-open.md`
- `move-date-wbtc-stablecoin-source-open-rollforward.csv`
- `move-date-reaper-multistrategy-hack-thread.md`
- `move-date-wbtc-reaper-recovery-link.md`
- `move-date-gtrain-grain-provenance.md`
- `move-date-oath-provenance.md`
- `move-date-oath-tge-payment-scan.md`
- `move-date-oath-tge-wftm-payment-candidates.csv`
- `move-date-oath-vesting-trace.md`
- `move-date-avalanche-fraxeth-check.md`

Please audit whether each included candidate has enough evidence to be counted
as Polish imported PIT-38 cost basis, and whether any candidate duplicates the
same economic basis already counted elsewhere.

## Included And Excluded Buckets

### Included

The current selected filing posture includes:

- Koinly-matched reviewable/direct move-date rows.
- Ethos `1.77696328 WBTC` trove collateral using the selected full WBTC
  roll-forward.
- GLP USDC.e predecessor.
- `rf-soWETH` WETH inputs.
- BPT-GTRAIN ETH-only input.
- BPT-GTRAIN stablecoin-funded GRAIN input.
- WETH/OATH LP WETH-linked component.
- WETH/OATH LP DOLA-funded OATH component.
- OATH TGE/LGE WFTM payment-side proof.
- Small `rf-grain-OP` survivor.
- Post-residency USDC/crypto remuneration or purchases where the income was
  taxed or the fiat purchase is evidenced; these appear as current-year costs,
  not as imported pre-residency basis.

### Excluded

The current selected filing posture excludes:

- ERN debt proceeds and ERN-funded legs by default.
- BPT-RESERVE, even though it existed at the move date, because current evidence
  suggests ERN/CDP debt-sourced provenance and potential double-counting with
  WBTC collateral.
- Remaining OATH-native bridge/reward/vesting/distributor buckets. These are
  now better source-traced but still excluded because valuation and legal
  tax-basis treatment are unresolved.
- Unsupported LP/vault balances without a clear cost source.
- Avalanche `frxETH` / `sfrxETH` as move-date imported basis, because current
  evidence shows the Avalanche position starts after Polish residency.
- Pre-residency salary-paid USDC as an imported cost merely because it was
  salary. This was researched separately in topic 17; the filing posture does
  not rely on it unless same-token/surviving-basis evidence applies.

Please audit whether any excluded item actually must be included, should be
included, or creates a risk by being omitted.

## Legal Questions To Answer

Please answer these directly:

1. Is the split-year approach correct for a taxpayer who became Polish tax
   resident on `2023-04-12`?
2. Can Polish PIT-38 include pre-residency acquisition/replacement basis for
   crypto assets held at the move date and later disposed while Polish resident?
3. If yes, what proof standard is needed for pre-residency basis imported into
   PIT-38?
4. Is it legally acceptable to import Layer C successor/replacement basis through
   pre-move crypto-to-crypto swaps, bridges, wrappers, LP tokens, receipt tokens,
   and DeFi positions?
5. Are there reasons to disallow or haircut any of the selected Layer C buckets?
6. Are borrowed/debt-sourced tokens, especially ERN/CDP debt proceeds, correctly
   excluded?
7. Is BPT-RESERVE correctly excluded by default despite being a real move-date
   holding?
8. Is the OATH treatment reasonable: include WETH-linked, DOLA-funded, and WFTM
   payment-side proof, but exclude remaining OATH-native/vesting/reward buckets?
9. Is post-residency crypto remuneration taxed in Poland on receipt properly
   counted as PIT-38 acquisition cost when later disposed?
10. Are the PIT-38 field mappings for 2023, 2024, and 2025 correct, including
    the shift from poz. 34-38 to poz. 36-40 in 2025?
11. Should the 2024 return be a correction or first/late filing if e-Urzad shows
    no manually submitted PIT-38?
12. Are there filing-order or czynny-zal implications for correcting/submitting
    2023, 2024, and 2025 PIT-38 now?

## Arithmetic Questions To Answer

Please verify:

1. The annual revenue totals match the event tables.
2. The annual current-year cost totals match the event tables.
3. The imported basis total is exactly `588,848.16 PLN`.
4. The carry-forward chain is arithmetically correct:
   - 2023 carry-forward: `825,656.90 PLN`
   - 2024 carry-forward: `528,067.97 PLN`
   - 2025 carry-forward: `472,061.65 PLN`
5. No current-year revenue or cost is duplicated across exchange rows, manual
   purchase rows, salary/remuneration rows, and override rows.
6. Manual Binance fiat-counterparty overrides are reasonable and not duplicated.
7. NBP rates and PLN conversions look correct for the material rows.

## Evidence Questions To Answer

Please review whether the filing package is supportable if challenged. For each
material bucket, classify evidence as:

```text
Strong / adequate for filing now / weak but defensible / not defensible
```

Please pay special attention to:

- WBTC roll-forward and Reaper recovery/source-open evidence.
- Whether WBTC collateral and ERN-funded LP/gauge positions are safely separated
  to avoid double-counting.
- GTRAIN GRAIN purchases and whether the GRAIN source really supports the
  BPT-GTRAIN basis.
- WETH/OATH LP components and whether WETH-linked vs OATH-native split is
  reasonable.
- DOLA-funded OATH component and whether it overlaps with any WBTC DOLA branch.
- OATH TGE/LGE WFTM payment-side proof and whether it should create cost basis.
- `rf-grain-OP` small survivor.
- 2025 Binance Paymonade EUR payments and 2024 small Paymonade ETH sale.
- Whether Swedish/Koinly records are enough, or whether the filing should mark
  some imported basis as provisional.

## Desired External-Audit Output

Please return a concise but rigorous audit memo with this structure:

1. **Verdict**
   - Ready to file / file with changes / do not file yet.
2. **Critical corrections before filing**
   - Exact fields and values to change, if any.
3. **Legal-risk findings**
   - Ranked high/medium/low.
4. **Arithmetic findings**
   - Any mismatch in totals, carry-forward, NBP rates, or field mapping.
5. **Evidence findings**
   - For each included imported-basis bucket, say whether it is supportable.
6. **Double-counting findings**
   - Identify any duplicated economic basis.
7. **Excluded-item findings**
   - Say whether any excluded item should be added now or left for later.
8. **Questions that must be answered by the taxpayer**
   - Only list questions that are genuinely blocking or materially reduce risk.
9. **Recommended filing wording**
   - If corrections or explanations are needed, suggest concise Polish/English
     wording for czynny zal, correction explanations, or audit notes.

If you disagree with a value, provide the corrected value and show the arithmetic.
If you disagree with a legal interpretation, cite the source and explain the
practical filing impact.

