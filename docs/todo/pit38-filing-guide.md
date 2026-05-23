# PIT-38 Filing Guide -- Current Split-Year Max No-Debt Plus WETH-Linked, DOLA-Funded, TGE-WFTM OATH And rf-grain-OP Values

Status: **current selected PIT-38 posture as of April 27, 2026**.

This guide uses the topic 17 split-year imported-basis model. The older topic
16 safe-default chain is superseded for PIT-38 mechanics:

- Polish PIT-38 revenue should start from `2023-04-12`, not from January 1 or
  prior Swedish-residency years.
- Pre-residency costs must be imported as explicit Layer A/B/C amounts, not via
  the old synthetic 2020-2022 Polish pool.
- The old `294,073.39 PLN` prior-cost figure is no longer a filing-source value.

Current calculator command:

```bash
PYTHONPATH=src python3 -m tax_calc pit38 \
  --policy split_year_high_risk \
  --primary-policy split_year_high_risk \
  --imported-fiat-costs 77955.80 \
  --imported-successor-costs 510892.36 \
  --output-dir outputs/pit38_max_no_debt_plus_oath_weth_dola_tge_rfgrain
```

The selected imported-basis pool is `588,848.16 PLN`: Koinly-matched reviewable
rows `77,955.80 PLN` plus Layer C successor basis `510,892.36 PLN`. Layer C
contains WBTC `142,580.44 PLN`, GLP `44,138.35 PLN`, `rf-soWETH`
`5,292.90 PLN`, BPT-GTRAIN ETH-only `25,964.04 PLN`, and BPT-GTRAIN
stablecoin-funded GRAIN `100,518.44 PLN`, plus the WETH-linked component of
the WETH/OATH LP `159,526.15 PLN`, plus the DOLA-funded OATH component
`17,172.86 PLN`, plus the OATH TGE/LGE WFTM payment-side proof
`15,596.93 PLN`, plus `rf-grain-OP` `102.25 PLN`. It excludes ERN debt
proceeds, BPT-RESERVE, the remaining OATH-native bridge/reward/vesting
buckets, and unsupported LP/vault balances.

April 25 on-chain update: activity on Ethereum, Polygon, Optimism, and
Arbitrum was found before `2023-04-12` for known wallets, so the move-date
basis rebuild must include those chains. Fantom token-transfer logs are also
now archived through public RPC and show pre-residency activity; OKLink is
still useful for native/internal Fantom address history. Mantle, Mode, and
Scroll activity found so far is post-residency and must be normalized before
final 2024-2025 PIT-38 values.

Move-date inventory output:
- `private/evidence/onchain/move-date-inventory-2023-04-12/move-date-inventory-2023-04-12.md`
- `private/evidence/onchain/move-date-inventory-2023-04-12/move-date-token-balances.csv`
- `private/evidence/onchain/move-date-inventory-2023-04-12/move-date-reconciliation-exceptions.csv`
- `private/evidence/onchain/move-date-inventory-2023-04-12/move-date-cost-provenance.csv`
- `private/evidence/onchain/move-date-inventory-2023-04-12/move-date-cost-provenance.md`
- `private/evidence/onchain/move-date-inventory-2023-04-12/move-date-basis-decision.md`
- `private/evidence/onchain/move-date-inventory-2023-04-12/move-date-replacement-traces.csv`
- `private/evidence/onchain/move-date-inventory-2023-04-12/move-date-supportable-basis-candidates.csv`
- `private/evidence/onchain/move-date-inventory-2023-04-12/move-date-unwind-workpaper.md`
- `private/evidence/onchain/move-date-inventory-2023-04-12/move-date-unwind-traces.csv`
- `private/evidence/onchain/move-date-inventory-2023-04-12/move-date-cdp-positions.md`
- `private/evidence/onchain/move-date-inventory-2023-04-12/move-date-cdp-positions.csv`
- `private/evidence/onchain/move-date-inventory-2023-04-12/move-date-cdp-transactions.csv`
- `private/evidence/onchain/move-date-inventory-2023-04-12/move-date-wbtc-cdp-basis-trace.md`
- `private/evidence/onchain/move-date-inventory-2023-04-12/move-date-wbtc-cdp-basis-trace.csv`
- `private/evidence/onchain/move-date-inventory-2023-04-12/move-date-wbtc-swedish-evidence-checklist.md`
- `private/evidence/onchain/move-date-inventory-2023-04-12/move-date-wbtc-swedish-evidence-checklist.csv`
- `private/evidence/onchain/move-date-inventory-2023-04-12/move-date-wbtc-basis-rollforward.md`
- `private/evidence/onchain/move-date-inventory-2023-04-12/move-date-wbtc-basis-rollforward.csv`
- `private/evidence/onchain/move-date-inventory-2023-04-12/move-date-wbtc-stablecoin-source-open.md`
- `private/evidence/onchain/move-date-inventory-2023-04-12/move-date-wbtc-stablecoin-source-open-rollforward.csv`
- `private/evidence/onchain/move-date-inventory-2023-04-12/move-date-reaper-multistrategy-hack-thread.md`
- `private/evidence/onchain/move-date-inventory-2023-04-12/move-date-wbtc-reaper-recovery-link.md`
- `private/evidence/onchain/move-date-inventory-2023-04-12/move-date-oath-provenance.md`
- `private/evidence/onchain/move-date-inventory-2023-04-12/move-date-oath-vesting-trace.md`
- `private/evidence/onchain/move-date-inventory-2023-04-12/move-date-oath-tge-payment-scan.md`
- `private/evidence/onchain/move-date-inventory-2023-04-12/move-date-oath-tge-wftm-payment-candidates.csv`
- `private/evidence/onchain/move-date-inventory-2023-04-12/move-date-avalanche-fraxeth-check.md`

The snapshot has 6,530 movement rows and 245 non-zero balance rows. It is an
asset-position input, not a cost-basis value. The provenance workpaper
classifies those rows as 28 `A`, 3 `A/B/C`, 8 `A/C`, 80 `C`, 106 `D`, and
20 `E`; only rows with final documented basis should feed PIT-38.

Current threshold finding: Koinly-matched reviewable rows alone are about
`77,955.80 PLN`, below the `116,786.51 PLN` imported-basis threshold by
`38,830.71 PLN`. The selected filing posture clears the threshold by adding the
Ethos WBTC roll-forward, GLP, `rf-soWETH`, BPT-GTRAIN ETH plus
stablecoin-funded GRAIN, and the WETH-linked plus DOLA-funded components of
WETH/OATH, while excluding ERN debt proceeds and OATH-native buckets.

Current max-supportable finding: exact WBTC Koinly anchors alone give a
`119,042.69 PLN` imported-basis pool, now `2,256.18 PLN` above the
threshold. Adding the full Ethos WBTC scaled roll-forward gives a
`220,536.24 PLN` imported-basis pool, a `103,749.73 PLN` surplus if the
stablecoin source-open rows and no-double-counting review are accepted. The max
supportable no-debt path before OATH is `396,449.97 PLN`, adding independent GLP /
`rf-soWETH` / BPT-GTRAIN ETH plus stablecoin-funded GRAIN candidates and excluding
ERN debt proceeds by default. The selected urgent filing path adds the
WETH-linked component and the distinct DOLA-funded OATH component of the
WETH/OATH LP, the OATH TGE/LGE WFTM payment-side proof, and `rf-grain-OP`,
bringing imported basis to `588,848.16 PLN`.

Current OATH source finding: `move-date-oath-vesting-trace.md` now traces the
OATH-native bucket much further back. It identifies `114,148` OATH from early
distributor `0x8b4441...` in 2022 and `145,833.3333333332` OATH from recurring
batch vesting/distributor `0xd152...` from November 2022 through April 2023.
The excluded OATH-native bucket is therefore source-traced, but valuation and
tax-basis treatment remain unresolved, especially for the 2023 pre-move vesting
receipts without a Koinly 2023 export.

Current unwind finding: the six reviewed wrapper/gauge/receipt positions match
their `2023-04-12` balances and all have latest `balanceOf = 0`. The exit
workpaper confirms GLP unwound to `USDC.e 10539.680018`, `rf-soWETH` unwound
to `WETH 0.603672288028468693`, and BPT-GTRAIN/BPT-RESERVE were real positions
that exited shortly after the move. This proves existence and unwind timing; it
does not make ERN/debt-sourced cost importable and does not permit the same
economic basis to be counted twice.

Current CDP finding: at Optimism block `89200417`
(`2023-04-11T23:59:55Z`), the Ethos WBTC trove is active with
`1.77696328 WBTC` collateral. The Ethos WETH trove is zero/non-existent at the
move date and first appears on `2023-06-29`, after Polish residency began.
Do not count both the WBTC collateral and ERN-funded LP/gauge positions as
independent acquisition cost.

Current WBTC basis-trace finding: the dedicated WBTC workpaper reconciles four
successful pre-move WBTC top-ups to the exact `1.77696328 WBTC` move-date
collateral, identifies four relevant cross-chain bridge hops including the
Arbitrum `anyUSDC` receipt back to Fantom USDC, and traces visible predecessor
rows through BTC/WBTC, USDC, DOLA, and wrapper/receipt-token steps. This is the
main evidence map for the WBTC candidate used in the selected filing posture.

Current Swedish/Koinly checklist finding: the WBTC trace has 9 exact Koinly
2022 transaction-history matches. The remaining unmatched non-archive hashes
are 45 Jan-Apr 2023 pre-move on-chain rows, and no 2023 Koinly export is in the
repo. The practical next step is to self-calculate those 2023 replacement-basis
rows from on-chain evidence.

Current WBTC roll-forward finding:
`move-date-wbtc-basis-rollforward.md` scales the trace to the actual top-up
quantities. Current split: `41,086.89 PLN` exact Koinly anchors,
`101,493.55 PLN` stablecoin source-open proxy, and an unresolved ETH/anyWETH
leg for the `0.38977903 WBTC` top-up. The selected filing posture uses the full
WBTC roll-forward and keeps the ETH/anyWETH leg excluded.

Current WBTC stablecoin source-open finding:
`move-date-wbtc-stablecoin-source-open.md` narrows the source-open proxy to two
terminal transactions: `10,000 USDC` on Fantom worth `44,202.01 PLN` and
`13,344.71795066 DOLA` from Arbitrum `crAMM-FRAX/DOLA` removal worth
`57,291.54 PLN`. The Fantom USDC sender
`0xbeb15caee71001d82f430e4deda80e16ddf438db` is not in the current known-wallet
files and is now believed to be an employer/company/Reaper-related address that
paid hack/loss compensation after a pre-move Reaper Farm multistrategy vault
loss on Fantom.
The direct Reaper hack/recovery event is now supported on-chain, and the
Reaper-to-WBTC link workpaper ties part of the August 18 recovery directly into
the WBTC predecessor path. The deeper stablecoin rows in that workpaper are
provenance context, not additional costs. The follow-up FRAX/DOLA LP source
check traces the DOLA branch to pre-move stablecoin and LP unwinds, and now
ties one large Fantom bridge-source branch to the `2022-08-18` Reaper DAI
recovery row with exact 2022 Koinly transaction-history evidence. The path runs
through `sDAI -> DIGI #90 -> DAI -> USDC -> Arbitrum USDC.e`. This strengthens
part of the source pool, but it is not bank-grade fiat-source proof for the
full branch; it remains Layer C/source-open evidence.

Current Reaper multi-strategy hack/compensation finding:
`move-date-reaper-multistrategy-hack-thread.md` supports the Reaper explanation
with on-chain rows across `rfETH`, `rfUSDC`, `rfDAI`, `rfUSDT`, `rfBTC`, and
`rfWFTM`. The known-wallet stable receipt face loss (`rfUSDC` + `rfDAI` +
`rfUSDT`) is `96,955.481433717843` receipt units; four loss transactions match
the attacker address named in Reaper's post-mortem. The loss-to-recovery match
covers every lost receipt family: `rfUSDC->USDC`, `rfDAI->DAI`,
`rfUSDT->fUSDT`, `rfETH->ETH`, `rfBTC->BTC`, and `rfWFTM->WFTM`; same-family
stable direct recovery is `41,002.05546` tokens, a `0.422896` ratio against the
stable receipt face loss. It also finds six direct 2022-08-18 recovery rows to
the known wallet: `20,000 USDC`, `20,000 DAI`, `4.52241375895353 ETH`,
`0.04636763 BTC`, `1,002.05546 fUSDT`, and `103.128665223373 WFTM`, all with a
common recovery caller/target. The later
`56,314.96 USDC` receipt on 2023-03-18 is WBTC-source provenance, but it is no
longer the main evidence that Reaper repayment occurred. Treat this as strong
provenance context, not final accepted basis, until the partial recovered-asset
trace and Swedish/Polish treatment are accepted.

Current Reaper-to-WBTC link finding:
`move-date-wbtc-reaper-recovery-link.md` directly links `9,000 DAI` from the
2022-08-18 Reaper DAI recovery and `0.04636763 BTC` from the 2022-08-18 Reaper
BTC recovery into the WBTC predecessor trace, with a combined trace proxy of
`45,930.36 PLN`. The August 18 USDC and ETH recovery rows now have indirect
forward-trace provenance into the Arbitrum DOLA/source-open branch, but those
forward links are not additive filing amounts. The August 18 fUSDT and WFTM
rows remain unlinked to the WBTC path. The March 18 2023 source-open leg is
separate: the scaled roll-forward allocates `10,000 USDC` / `44,202.01 PLN` to
the WBTC path, but that tx is not itself an August 2022 recovery transaction.

Basis-trace clarification: still holding WBTC at the move date means the WBTC
itself was not taxed merely because it was held. The evidence task is to trace
its acquisition cost through any Swedish-taxable pre-move swaps, wraps, bridges,
or receipt-token steps; those steps may create replacement acquisition values,
not make the cost disappear.

Source of truth:
- `docs/tax-law/17-pre-residency-usdc-basis/synthesis-pre-residency-usdc-basis.md`
- `src/tax_calc/cost_pool.py`

The values below are retained only for historical comparison with the old topic
16 policy.

---

## Before You Start

1. Keep the selected imported-basis posture together: Ethos `1.77696328 WBTC`, GLP, `rf-soWETH`, BPT-GTRAIN ETH plus stablecoin-funded GRAIN, the WETH-linked plus DOLA-funded WETH/OATH LP components, OATH TGE/LGE WFTM payment-side proof, and `rf-grain-OP`, using `move-date-cdp-positions.md`, `move-date-wbtc-cdp-basis-trace.md`, `move-date-wbtc-swedish-evidence-checklist.md`, `move-date-wbtc-basis-rollforward.md`, `move-date-wbtc-stablecoin-source-open.md`, `move-date-frax-dola-lp-source-check.md`, `move-date-reaper-multistrategy-hack-thread.md`, `move-date-wbtc-reaper-recovery-link.md`, `move-date-gtrain-grain-provenance.md`, `move-date-oath-provenance.md`, `move-date-oath-tge-payment-scan.md`, and `move-date-supportable-basis-candidates.csv`.
2. Use the generated `outputs/pit38_max_no_debt_plus_oath_weth_dola_tge_rfgrain/` values consistently across 2023, 2024, and 2025; refinements to WBTC/OATH/other unresolved rows can be handled after filing if needed.
3. Log into e-Urzad Skarbowy and check `Zlozone dokumenty`.
4. Confirm whether PIT-38 already exists for 2023 and 2024.
5. Choose filing mode:
   - **2023**: korekta of the already-filed PIT-38.
   - **2024**: korekta if a zero PIT-38 was auto-accepted; otherwise late first filing / zalegle zeznanie.
   - **2025**: normal annual PIT-38 for 2025.
6. File in order: **2023 -> 2024 -> 2025**.

---

## PIT-38 For 2023

Use the PIT-38 form for tax year 2023. In the crypto section (`Waluty wirtualne`, Section E), enter:

| Field | Value |
| --- | ---: |
| Poz. 34 | 264,113.82 |
| Poz. 35 | 500,922.56 |
| Poz. 36 | 588,848.16 |
| Poz. 37 | 0.00 |
| Poz. 38 | 825,656.90 |

Meaning:
- `Poz. 34`: revenue from post-residency crypto-to-fiat disposals.
- `Poz. 35`: 2023 acquisition/disposal costs.
- `Poz. 36`: imported pre-residency basis selected under this posture.
- `Poz. 37`: income, zero because costs exceed revenue.
- `Poz. 38`: undeducted costs carried to 2024.

Expected outcome: **0 PLN tax due**.

---

## PIT-38 For 2024

Use the PIT-38 form for tax year 2024. In the crypto section (`Waluty wirtualne`, Section E), enter:

| Field | Value |
| --- | ---: |
| Poz. 34 | 785,654.54 |
| Poz. 35 | 488,065.61 |
| Poz. 36 | 825,656.90 |
| Poz. 37 | 0.00 |
| Poz. 38 | 528,067.97 |

Meaning:
- `Poz. 36` must match 2023 `Poz. 38`.
- `Poz. 38` becomes the prior-year cost figure for 2025.

Expected outcome: **0 PLN tax due**.

---

## PIT-38 For 2025

Use the PIT-38 form for tax year 2025. In the crypto section (`Waluty wirtualne`, Section E), enter:

| Field | Value |
| --- | ---: |
| Poz. 36 | 271,316.95 |
| Poz. 37 | 215,310.63 |
| Poz. 38 | 528,067.97 |
| Poz. 39 | 0.00 |
| Poz. 40 | 472,061.65 |

Meaning:
- `Poz. 38` must match 2024 `Poz. 38`.
- `Poz. 40` is the selected cost amount carried into 2026.

Expected outcome: **0 PLN tax due**.

---

## Quick Cross-Checks

Use these checks before submitting:

| Year | Check |
| --- | --- |
| 2023 | `500,922.56 + 588,848.16 - 264,113.82 = 825,656.90` |
| 2024 | `488,065.61 + 825,656.90 - 785,654.54 = 528,067.97` |
| 2025 | `215,310.63 + 528,067.97 - 271,316.95 = 472,061.65` |

Use the generated policy values consistently in each carry-forward and prior-year-cost field.

---

## Why These Are Selected Values

The selected filing posture excludes pre-residency salary-paid USDC merely because it was salary. It includes the currently documented no-debt move-date asset basis: fiat/direct Koinly rows, WBTC roll-forward, GLP, `rf-soWETH`, BPT-GTRAIN ETH plus stablecoin-funded GRAIN, the WETH-linked plus DOLA-funded components of WETH/OATH, the OATH TGE/LGE WFTM payment-side proof, and `rf-grain-OP`.

ERN/debt-funded positions, BPT-RESERVE, remaining OATH-native bridge/reward/vesting buckets, and unsupported LP/vault balances remain documented separately but are not in the current filing values.

---

## Submission Notes

- Save the UPO / confirmation after each submission.
- File all three PIT-38 forms before finalizing 2025 PIT-38, because the carry-forward fields depend on prior-year submissions.
- These PIT-38 forms all show **0 PLN tax due**. The cash payment this week comes from PIT-36 plus late-advance interest; PIT-28 shows a small overpayment.
