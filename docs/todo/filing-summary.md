# Tax Filing Summary -- Provisional Working Plan

**Date**: April 26, 2026
**Deadline**: April 30, 2026
**Filing posture**: PIT-36 and PIT-28 ready; PIT-38 uses the split-year max no-debt plus WETH-linked, DOLA-funded, TGE-WFTM OATH and `rf-grain-OP` imported-basis pool.

Important update: the topic 16 PIT-38 chain in this file is no longer final.
Topic 17 research and the calculator rewrite now use a split-year model starting
on `2023-04-12`. The old synthetic pre-residency pool and `294,073.39 PLN`
prior-cost figure are historical comparison values, not filing-source values.

April 25 on-chain update: Ethereum, Polygon, Optimism, Arbitrum, Mantle, Mode,
and Scroll were added to the evidence scan. Ethereum, Polygon, Optimism, and
Arbitrum have pre-residency activity before `2023-04-12`; Fantom token-transfer
logs are now archived through public RPC and also have pre-residency activity.
OKLink is still useful for native/internal Fantom address history. Mantle, Mode, and
Scroll activity found so far is post-residency but still missing from final
PIT-38 normalization.

Move-date inventory update: the repo now has a reproducible asset snapshot at
`private/evidence/onchain/move-date-inventory-2023-04-12/`. It contains 6,530
movement rows and 245 non-zero balance rows at `2023-04-12T00:00:00Z`. It is
not a filing value by itself; the selected filing posture uses specific
documented no-debt rows from the later basis workpapers.

Cost-provenance update: the first generated workpaper is now in the same
folder: `move-date-cost-provenance.csv`, `move-date-cost-provenance-summary.json`,
and `move-date-cost-provenance.md`. It classifies the 245 rows as 28 direct
Layer A candidates, 3 unresolved stablecoin rows (`A/B/C`), 8 direct-or-
replacement rows (`A/C`), 80 Layer C DeFi / replacement rows, 106 excluded
Layer D rows, and 20 quarantined Layer E rows. It is not the full filing value
by itself; it supports the selected imported-basis package together with the
CDP, WBTC, GTRAIN, unwind, and OATH workpapers.

Basis-decision update: the same folder now also contains
`move-date-basis-decision.md`, `move-date-basis-decision-summary.json`, and
`move-date-replacement-traces.csv`, plus the new
`move-date-supportable-basis-candidates.csv`. The current reviewable Koinly
2022 cost-pool cross-check is only about `77,955.80 PLN`, leaving a
`38,830.71 PLN` gap versus the `116,786.51 PLN` imported-basis threshold before
CDP collateral is added. The generated scenarios now also include the selected
urgent WETH/OATH partial-add path with WETH-linked, DOLA-funded, and TGE-WFTM
components plus `rf-grain-OP`.

Unwind update: `move-date-unwind-workpaper.md`,
`move-date-unwind-summary.json`, and `move-date-unwind-traces.csv` now verify
that the six reviewed Layer C positions reconcile to the `2023-04-12`
move-date balances and currently have zero wrapper/gauge/receipt token balances.
This makes `BPT-RESERVE` a documented real holding, but not a default filing
cost: its problem is ERN/CDP-style cost provenance.

CDP protocol-state update: `move-date-cdp-positions.md`,
`move-date-cdp-positions.csv`, `move-date-cdp-transactions.csv`, and
`move-date-cdp-positions-summary.json` now show the Optimism Ethos Reserve
trove at the move-date block. The active move-date collateral is
`1.77696328 WBTC` with `26,341 ERN` protocol debt. WETH collateral is
zero/non-existent at the move date and first appears only on `2023-06-29`.
This WBTC trove is included in the selected imported-basis posture,
and ERN-funded LP/gauge positions are not double-counted as separate
acquisition cost.

WBTC basis-trace update: `move-date-wbtc-cdp-basis-trace.md`,
`move-date-wbtc-cdp-basis-trace.csv`, and
`move-date-wbtc-cdp-basis-trace-summary.json` now reconcile four successful
pre-move WBTC trove top-ups to the exact `1.77696328 WBTC` move-date
collateral and identify four relevant cross-chain bridge hops, including the
Arbitrum `anyUSDC` receipt back to the Fantom USDC bridge-out. The trace maps
visible predecessor transactions through BTC/WBTC, USDC, DOLA, and
wrapper/receipt-token steps. This supports the WBTC candidate used in the
selected filing posture.

Swedish/Koinly evidence update: `move-date-wbtc-swedish-evidence-checklist.md`,
`move-date-wbtc-swedish-evidence-checklist.csv`, and
`move-date-wbtc-swedish-evidence-checklist-summary.json` compare the WBTC trace
to available Koinly transaction-history exports. Current result: 9 exact Koinly
2022 transaction-hash matches, 45 Jan-Apr 2023 pre-move on-chain rows with no
2023 Koinly export in the repo, and 1 archive-gap/prehistory bucket. Further
self-calculation can improve audit support after filing.

WBTC roll-forward update: `move-date-wbtc-basis-rollforward.md`,
`move-date-wbtc-basis-rollforward.csv`, and
`move-date-wbtc-basis-rollforward-summary.json` now scale the WBTC trace to the
actual collateral top-ups. Current split: `41,086.89 PLN` exact Koinly anchors,
`101,493.55 PLN` stablecoin source-open proxy, and an unresolved ETH/anyWETH
leg for the `0.38977903 WBTC` top-up.

WBTC stablecoin source-open update:
`move-date-wbtc-stablecoin-source-open.md` now narrows the source-open proxy to
two terminal transactions: `10,000 USDC` on Fantom worth `44,202.01 PLN` and
`13,344.71795066 DOLA` from Arbitrum `crAMM-FRAX/DOLA` removal worth
`57,291.54 PLN`. The Fantom USDC sender
`0xbeb15caee71001d82f430e4deda80e16ddf438db` is not in the current known-wallet
files and is now believed to be an employer/company/Reaper-related address that
paid hack/loss compensation after a pre-move Reaper Farm multistrategy vault
loss on Fantom.
The direct Reaper hack/recovery event is now supported on-chain, and the new
Reaper-to-WBTC link workpaper ties part of the August 18 recovery directly into
the WBTC predecessor path. Deeper stablecoin trace rows are fallback provenance
context, not additive filing values.

Reaper multi-strategy hack/compensation update:
`move-date-reaper-multistrategy-hack-thread.md` now gives concrete on-chain
support for the Reaper explanation. The known wallet lost `rfETH`, `rfUSDC`,
`rfDAI`, `rfUSDT`, `rfBTC`, and `rfWFTM` receipt tokens on
2022-08-02/2022-08-03; `rfUSDC` + `rfDAI` + `rfUSDT` alone total
`96,955.481433717843` stable receipt units. Four loss transactions match the
attacker address named in Reaper's post-mortem. The loss-to-recovery match now
covers every lost receipt family: `rfUSDC->USDC`, `rfDAI->DAI`,
`rfUSDT->fUSDT`, `rfETH->ETH`, `rfBTC->BTC`, and `rfWFTM->WFTM`. Same-family
stable direct recovery is `41,002.05546` tokens, a `0.422896` ratio against the
stable receipt face loss. The same workpaper also finds six direct 2022-08-18
recovery rows to the known wallet: `20,000 USDC`, `20,000 DAI`,
`4.52241375895353 ETH`, `0.04636763 BTC`, `1,002.05546 fUSDT`, and
`103.128665223373 WFTM`; all six share recovery caller
`0x60bc5e0440c867eeb4cbce84bb1123fad2b262b1` and target
`0xd152f549545093347a162dce210e7293f1452150`. The later
`56,314.96 USDC` receipt on 2023-03-18 is WBTC-source provenance, but it is no
longer the main evidence that Reaper repayment occurred. The remaining issue is
the legal treatment and the partial transaction-level tie from recovered assets
into the WBTC path.

Reaper-to-WBTC link update:
`move-date-wbtc-reaper-recovery-link.md` now identifies the directly linked
recovery subchain. The WBTC trace explicitly consumes `9,000 DAI` from the
2022-08-18 Reaper DAI recovery and `0.04636763 BTC` from the 2022-08-18 Reaper
BTC recovery, with a combined trace proxy of `45,930.36 PLN`. The August 18
USDC and ETH recovery rows now have indirect forward-trace provenance into the
Arbitrum DOLA/source-open branch, but those forward links are not additive
filing amounts. The August 18 fUSDT and WFTM recovery rows remain unlinked to
the WBTC path. The March 18 2023 compensation/source-open leg remains separate:
`10,000 USDC` is allocated to the scaled WBTC roll-forward for `44,202.01 PLN`,
but it is not itself an August 2022 recovery transaction.

Max-supportable update: the current PIT-38 filing path uses the max supportable
no-debt pool plus the WETH-linked, DOLA-funded, and TGE-WFTM components of the WETH/OATH LP and `rf-grain-OP`. It includes the Ethos
`1.77696328 WBTC` trove collateral at a scaled roll-forward proxy
`142,580.44 PLN`. Exact WBTC anchors alone bring the threshold pool to
`119,042.69 PLN`, now `2,256.18 PLN` above the threshold. The full WBTC roll-forward
brings the threshold pool to `220,536.24 PLN`, a `103,749.73 PLN` surplus if
the stablecoin source-open rows and no-double-counting review are accepted. The
supportable no-debt scenario before OATH is `396,449.97 PLN`, adding independent
GLP / `rf-soWETH` / BPT-GTRAIN ETH plus stablecoin-funded GRAIN candidates
while excluding ERN debt proceeds and BPT-RESERVE by default. The selected
urgent filing scenario adds the WETH-linked part of WETH/OATH
(`159,526.15 PLN`) plus the distinct DOLA-funded OATH component
(`17,172.86 PLN`), the OATH TGE/LGE WFTM payment-side proof
(`15,596.93 PLN`), and `rf-grain-OP` (`102.25 PLN`), and uses total imported
basis of `588,848.16 PLN`. The remaining OATH-native bridge/reward/vesting
buckets remain excluded. The new OATH vesting
trace improves those excluded buckets by tying `114,148` OATH to the early
2022 distributor and `145,833.3333333332` OATH to recurring batch
vesting/distributor transfers through April 2023; valuation and tax-basis
treatment are still unresolved for filing.

DOLA-source clarification: `move-date-dola-oath-source-check.md` and
`move-date-frax-dola-lp-source-check.md` confirm the DOLA-funded OATH branch is
not visibly ERN/CDP debt and is separately allocated from the WBTC DOLA leg. The
deeper FRAX/DOLA LP source is now partially stronger: one large Fantom
bridge-source branch traces through the `2022-08-18` Reaper DAI recovery row
with exact 2022 Koinly transaction-history evidence, then through
`sDAI -> DIGI #90 -> DAI -> USDC -> Arbitrum USDC.e`. This supports provenance
for part of the LP source pool. It is still stablecoin/LP replacement evidence,
not bank-grade fiat-source proof for the full branch, so this remains a Layer
C/source-open posture.

Basis-trace clarification: if the same WBTC was held through the move date,
holding it was not itself a Swedish taxable disposal. The issue is whether its
move-date acquisition cost can be traced through Swedish K4/Koinly records,
including any taxable pre-move swaps, wraps, bridges, or receipt-token steps,
without counting the same economic basis twice.

---

## Current Bottom Line

| Form | Year | Type | Tax Due | Already Paid | Net Effect |
| --- | --- | --- | ---: | ---: | ---: |
| PIT-38 korekta | 2023 | Crypto capital gains | 0 PLN | 0 PLN | Carry-forward `825,656.90 PLN` |
| PIT-38 korekta / zalegle zeznanie | 2024 | Crypto capital gains | 0 PLN | 0 PLN | Carry-forward `528,067.97 PLN` |
| PIT-38 | 2025 | Crypto capital gains | 0 PLN | 0 PLN | Carry-forward `472,061.65 PLN` |
| PIT-36 | 2025 | Pre-JDG USDC service income | 14,060 PLN | 0 PLN | 14,060 PLN due |
| PIT-28 | 2025 | JDG ryczalt | 31,784 PLN | 32,288.14 PLN | 504.14 PLN overpayment |

Practical cash position:

| Item | Amount |
| --- | ---: |
| PIT-36 tax to pay | 14,060 PLN |
| Estimated interest on late PIT-36 advances if no advances were paid | ~1,800 PLN |
| PIT-28 overpayment/refund | -504.14 PLN |
| PIT-38 tax | 0 PLN |
| **Net economic cost after PIT-28 refund** | **~15,356 PLN** |

Operationally, pay the PIT-36 tax and interest by the deadline. Treat the PIT-28 overpayment as a refund or separately request offset; do not assume it automatically reduces the PIT-36 payment. File PIT-38 using the split-year max no-debt plus WETH-linked, DOLA-funded, TGE-WFTM OATH and `rf-grain-OP` generated reports in `outputs/pit38_max_no_debt_plus_oath_weth_dola_tge_rfgrain/`.

---

## Why This Changed

The old `docs/personal-tax/2025/tax-correction-plan.md` is superseded. It used March estimates and an aggressive PIT-38 pool that included pre-residency salary-paid USDC.

The old topic 16 safe-default policy kept:

- documented pre-residency fiat-to-crypto purchases,
- post-residency USDC remuneration taxed by Poland on receipt,
- taxable buy/sell/disposal fees.

The old topic 16 safe-default policy excluded:

- pre-residency salary / compensation paid in USDC,
- stablecoin deposits treated as standalone cost creation,
- funding or withdrawal fees,
- manual proxy rows that cannot be backed by primary evidence.

Topic 17 changes the frame: pre-residency disposals are excluded entirely, and
pre-residency costs are imported through a move-date basis ledger. The selected
max no-debt plus WETH-linked, DOLA-funded, TGE-WFTM OATH and `rf-grain-OP` imported-basis pool results in 0 PLN PIT-38
tax for 2023-2025.

---

## Documents To Submit

PIT-36 and PIT-28 below are usable working values. The PIT-38 subsections below
use the current topic 17 split-year max no-debt plus WETH-linked, DOLA-funded,
TGE-WFTM OATH and `rf-grain-OP` run generated in
`outputs/pit38_max_no_debt_plus_oath_weth_dola_tge_rfgrain/`.

### 1. PIT-38 korekta for 2023

| PIT-38 Field | Amount (PLN) |
| --- | ---: |
| Poz. 34 -- Revenue | 264,113.82 |
| Poz. 35 -- Costs incurred in 2023 | 500,922.56 |
| Poz. 36 -- Costs from prior years | 588,848.16 |
| Poz. 37 -- Income | 0.00 |
| Poz. 38 -- Carry-forward to 2024 | 825,656.90 |
| **Tax due** | **0 PLN** |

Reasoning: split-year PIT-38 starts from Polish residency on `2023-04-12` and imports `588,848.16 PLN` of documented no-debt plus WETH-linked, DOLA-funded, TGE-WFTM OATH and `rf-grain-OP` pre-residency basis. This correction is needed because the filed 2023 PIT-38 has the wrong carry-forward.

### 2. PIT-38 for 2024

Use **korekta** if e-Urzad shows an auto-accepted zero PIT-38 for 2024. Use **zalegle zeznanie** if no 2024 PIT-38 exists.

| PIT-38 Field | Amount (PLN) |
| --- | ---: |
| Poz. 34 -- Revenue | 785,654.54 |
| Poz. 35 -- Costs incurred in 2024 | 488,065.61 |
| Poz. 36 -- Costs from prior years | 825,656.90 |
| Poz. 37 -- Income | 0.00 |
| Poz. 38 -- Carry-forward to 2025 | 528,067.97 |
| **Tax due** | **0 PLN** |

Reasoning: this preserves the chain from corrected 2023 into 2025. The 2024 PIT-38 was not manually filed, and the prior-year cost field must match the corrected 2023 carry-forward.

### 3. PIT-38 for 2025

| PIT-38 Field | Amount (PLN) |
| --- | ---: |
| Poz. 36 -- Revenue | 271,316.95 |
| Poz. 37 -- Costs incurred in 2025 | 215,310.63 |
| Poz. 38 -- Costs from prior years | 528,067.97 |
| Poz. 39 -- Income | 0.00 |
| Poz. 40 -- Carry-forward to 2026 | 472,061.65 |
| **Tax due** | **0 PLN** |

Reasoning: current-year 2025 costs plus corrected prior-year carry-forward exceed 2025 crypto disposal revenue, so no crypto tax is due.

### 4. PIT-36 for 2025

Report pre-JDG USDC service income from January-April 2025.

| Item | Amount |
| --- | ---: |
| Gross income | 162,735.75 PLN |
| Cost deduction, 20% | -32,547.15 PLN |
| Taxable income | 130,188.60 PLN |
| Kwota wolna applied | -30,000.00 PLN |
| Tax base | 100,189.00 PLN |
| **Tax due** | **14,060 PLN** |

Reasoning: the working classification is Art. 13 pkt 8 personal services, using 20% standard costs. This remains plausible, not risk-free. The same 162,735.75 PLN is also included as 2025 PIT-38 cost basis because it was taxed by Poland on receipt.

Include PIT/ZG only if you choose the conservative disclosure route for foreign-source income. The research is split on whether it is mandatory when work was performed from Poland for a foreign payer, but attaching it is the safer procedural posture.

### 5. PIT-28 for 2025

Report JDG ryczalt income from the Clearstar EUR invoices.

| Item | Amount |
| --- | ---: |
| Total invoiced | 62,956.56 EUR |
| Revenue before health deduction | 267,794.30 PLN |
| Health insurance paid | 5,847.67 PLN |
| Revenue deduction: 50% health insurance | -2,923.84 PLN |
| Taxable ryczalt revenue | 264,870.46 PLN |
| Ryczałt rate | 12% |
| **Tax due** | **31,784 PLN** |
| Monthly payments already made | 32,288.14 PLN |
| **Expected overpayment / refund** | **504.14 PLN** |

Reasoning: official guidance says a ryczalt taxpayer deducts 50% of paid health insurance from revenue, not directly from tax. The previous local report deducted it from tax and understated PIT-28 by about 2,573 PLN.

---

## Evidence Behind The Calculations

### PIT-38

- Current legal policy: `docs/tax-law/17-pre-residency-usdc-basis/synthesis-pre-residency-usdc-basis.md`
- Calculator policy modes: `src/tax_calc/cost_pool.py`
- Current generated reports use the selected split-year max no-debt plus WETH-linked, DOLA-funded, TGE-WFTM OATH and `rf-grain-OP` imported-basis posture.
- Move-date inventory snapshot:
  `private/evidence/onchain/move-date-inventory-2023-04-12/`
- Move-date basis decision:
  `private/evidence/onchain/move-date-inventory-2023-04-12/move-date-basis-decision.md`
- Move-date supportable candidates:
  `private/evidence/onchain/move-date-inventory-2023-04-12/move-date-supportable-basis-candidates.csv`
- Move-date BPT-GTRAIN GRAIN provenance:
  `private/evidence/onchain/move-date-inventory-2023-04-12/move-date-gtrain-grain-provenance.md`
- Move-date unwind workpaper:
  `private/evidence/onchain/move-date-inventory-2023-04-12/move-date-unwind-workpaper.md`
- Move-date CDP protocol-state workpaper:
  `private/evidence/onchain/move-date-inventory-2023-04-12/move-date-cdp-positions.md`
- Move-date WBTC CDP basis trace:
  `private/evidence/onchain/move-date-inventory-2023-04-12/move-date-wbtc-cdp-basis-trace.md`
- Move-date WBTC Swedish/Koinly evidence checklist:
  `private/evidence/onchain/move-date-inventory-2023-04-12/move-date-wbtc-swedish-evidence-checklist.md`
- Move-date WBTC scaled basis roll-forward:
  `private/evidence/onchain/move-date-inventory-2023-04-12/move-date-wbtc-basis-rollforward.md`
- Move-date WBTC stablecoin source-open workpaper:
  `private/evidence/onchain/move-date-inventory-2023-04-12/move-date-wbtc-stablecoin-source-open.md`
- Reaper multi-strategy hack/compensation thread:
  `private/evidence/onchain/move-date-inventory-2023-04-12/move-date-reaper-multistrategy-hack-thread.md`
- Reaper-to-WBTC recovery link:
  `private/evidence/onchain/move-date-inventory-2023-04-12/move-date-wbtc-reaper-recovery-link.md`
- Move-date OATH/WETH provenance:
  `private/evidence/onchain/move-date-inventory-2023-04-12/move-date-oath-provenance.md`
- Move-date OATH vesting/distributor trace:
  `private/evidence/onchain/move-date-inventory-2023-04-12/move-date-oath-vesting-trace.md`
- Move-date Avalanche frxETH/sfrxETH check:
  `private/evidence/onchain/move-date-inventory-2023-04-12/move-date-avalanche-fraxeth-check.md`
- Current threshold conclusion: Koinly-matched rows alone are short
  (`77,955.80 PLN` vs `116,786.51 PLN`). Adding only the Ethos WBTC exact
  Koinly anchors gives `119,042.69 PLN`, which now clears the threshold
  slightly; adding the full source-open WBTC roll-forward gives
  `220,536.24 PLN` if the two source-open terminal
  transactions are accepted. The max supportable no-debt path before OATH gives
  `396,449.97 PLN`; the selected urgent path adds the WETH-linked WETH/OATH
  component plus the DOLA-funded OATH component, OATH TGE/LGE WFTM
  payment-side proof, and `rf-grain-OP`, and gives `588,848.16 PLN`.
- Current unwind conclusion: all six reviewed wrapper/gauge/receipt positions
  reconcile to the move-date quantities and have current zero balances. The
  workpaper supports GLP, `rf-soWETH`, and BPT-GTRAIN tracing; the GTRAIN GRAIN
  provenance adds `100,518.44 PLN` from stablecoin-funded GRAIN and it confirms
  `BPT-RESERVE` existed but leaves it quarantined by default.
- Current selected PIT-38 generated reports are in
  `outputs/pit38_max_no_debt_plus_oath_weth_dola_tge_rfgrain/`. They do not yet include future
  normalization changes for post-residency
  Mantle, Mode, and Scroll activity if those later prove to have taxable
  crypto-to-fiat disposals.
- Avalanche `frxETH` / `sfrxETH` was checked after the user noticed a current
  balance. It first appears in the archived Avalanche history on `2023-06-03`,
  after Polish residency started, so it is not added to the move-date imported
  basis pool.
- Crypto method: annual cost pooling, not FIFO; crypto-to-crypto swaps are not taxable; excess costs carry forward as undeducted costs.
- Official support: podatki.gov.pl PIT-38 guidance says PIT-38 is required when crypto revenue or acquisition costs exist, and unused costs carry into later years.

### PIT-36

- Calculation report: `outputs/pit36_report_2025.md`
- Underlying payments: 7 USDC payments, 40,500 USDC total, valued at NBP USD/PLN from the last business day before receipt.
- Working classification: Art. 13 pkt 8 with 20% standard costs.

### PIT-28

- Calculation report: `outputs/pit28_report_2025.md`
- Underlying invoices: `docs/invoices/2025/invoices-clearstar/`
- Health insurance evidence: ZUS DRA monthly health contributions for May-December 2025.
- Official support: podatki.gov.pl says ryczalt taxpayers may deduct 50% of paid health insurance from revenue and settle it finally in PIT-28.

---

## Filing Sequence

1. Use the selected split-year max no-debt plus WETH-linked, DOLA-funded, TGE-WFTM OATH and `rf-grain-OP` PIT-38 values if you accept the current evidence posture: WBTC roll-forward, GLP, `rf-soWETH`, BPT-GTRAIN ETH plus stablecoin-funded GRAIN, the WETH-linked plus DOLA-funded parts of WETH/OATH, OATH TGE/LGE WFTM payment-side proof, and `rf-grain-OP`; ERN/debt legs, BPT-RESERVE, remaining OATH-native bridge/reward/vesting buckets, and unsupported LP/vault balances remain excluded.
2. Keep the evidence packet together: `move-date-cdp-positions.md`, `move-date-wbtc-cdp-basis-trace.md`, `move-date-wbtc-swedish-evidence-checklist.md`, `move-date-wbtc-basis-rollforward.md`, `move-date-wbtc-stablecoin-source-open.md`, `move-date-frax-dola-lp-source-check.md`, `move-date-reaper-multistrategy-hack-thread.md`, `move-date-wbtc-reaper-recovery-link.md`, `move-date-gtrain-grain-provenance.md`, `move-date-oath-provenance.md`, `move-date-oath-vesting-trace.md`, `move-date-basis-decision.md`, and `move-date-supportable-basis-candidates.csv`.
3. Check e-Urzad `Zlozone dokumenty` for 2023 and 2024 PIT-38 status.
4. File 2023 PIT-38 korekta, 2024 PIT-38 korekta/late filing, and 2025 PIT-38.
5. File 2025 PIT-36 and pay 14,060 PLN plus exact interest on missed advances.
6. File 2025 PIT-28 and claim / leave the 504.14 PLN overpayment.
7. Save UPO confirmations for every submission.

---

## After April 30

| Action | Priority | Expected tax impact |
| --- | --- | ---: |
| Correct 2023 PIT-37 -> PIT-36 + optional PIT/ZG | High, after deadline | 0 PLN expected |
| Correct 2024 PIT-37 -> PIT-36 + optional PIT/ZG | High, after deadline | 0 PLN expected |
| Consult ZUS specialist on 2023-2025 pre-JDG service income | High | Unknown, potentially material |
| Prepare individual interpretation for excluded pre-residency salary-USDC if preserving larger PIT-38 pool matters | Medium | Protects optional aggressive bucket |
| Swedish residency notice / report | Done | Submitted by taxpayer; keep confirmation and any Skatteverket response |
