# PIT-38 Max No-Debt Plus WETH-Linked, DOLA-Funded, TGE-WFTM OATH And rf-grain-OP Filing Position

Status: working file-now position, updated 2026-04-27.

This is the current pragmatic filing posture for the April 2026 deadline. It
does not try to reconstruct every Swedish K4 row, every LP token, or every vault
token. It uses the largest currently documented no-debt subset of the move-date
portfolio that can be argued as Polish PIT-38 imported basis today.

## Position

Use split-year Polish residency from `2023-04-12`.

Exclude pre-residency Polish revenue/cost rows before `2023-04-12`.

Use this imported pre-residency basis package:

| Component | Amount |
| --- | ---: |
| Koinly-matched reviewable move-date rows | `77,955.80 PLN` |
| Ethos WBTC full roll-forward | `142,580.44 PLN` |
| GLP `USDC.e` predecessor | `44,138.35 PLN` |
| `rf-soWETH` WETH inputs | `5,292.90 PLN` |
| BPT-GTRAIN ETH-only input | `25,964.04 PLN` |
| BPT-GTRAIN stablecoin-funded GRAIN input | `100,518.44 PLN` |
| WETH/OATH LP WETH-linked component | `159,526.15 PLN` |
| WETH/OATH LP DOLA-funded OATH component | `17,172.86 PLN` |
| OATH TGE/LGE WFTM payment-side proof | `15,596.93 PLN` |
| `rf-grain-OP` surviving OP-funded receipt basis | `102.25 PLN` |
| **Total imported basis used** | **`588,848.16 PLN`** |

The Layer C successor-basis amount passed to the calculator is
`510,892.36 PLN`: WBTC `142,580.44` + GLP `44,138.35` + `rf-soWETH`
`5,292.90` + BPT-GTRAIN ETH-only `25,964.04` + BPT-GTRAIN stablecoin-funded
GRAIN `100,518.44` + WETH/OATH LP WETH-linked component `159,526.15` +
WETH/OATH LP DOLA-funded OATH component `17,172.86` + OATH TGE/LGE WFTM
payment-side proof `15,596.93` + `rf-grain-OP` `102.25`.

Exclude BPT-RESERVE, ERN/debt legs, the remaining OATH-native bridge/reward/
vesting buckets, and unsupported LP/vault balances from the current filed
numbers.

## Why The WETH/OATH Partial Add Is Included

The full `nead-vrAMM-WETH/OATH` move-date source-input value proxy is
`256,851.44 PLN`, but the current filed value does not use that full amount.
It uses the ETH/WETH-linked part and the distinct DOLA-funded OATH purchase:

| OATH/WETH part | Quantity | Current treatment |
| --- | ---: | --- |
| Direct WETH deposited into the LP | `16.916502906487040914 WETH` | Included |
| WETH spent to buy OATH that entered the LP | `0.504120886 WETH` | Included |
| **Total WETH-linked component** | **`17.420623792487040914 WETH-equivalent`** | **`159,526.15 PLN` included** |
| DOLA spent to buy OATH that entered the LP | `4,000.013743178546457040667047 DOLA` | **`17,172.86 PLN` included** |
| OATH TGE/LGE WFTM payment-side proof | `2,877.7 WFTM` | **`15,596.93 PLN` included** |
| Remaining OATH-native bridge/reward/vesting buckets | `115,897.665490623468125458 OATH` plus tiny carryover | Excluded for now |

Reasoning: the WETH-linked piece can ride on the same ETH/WETH acquisition or
replacement-basis evidence used elsewhere in the move-date workpapers. The DOLA
piece is a separate visible stablecoin spend into OATH, valued with the NBP
USD/PLN rate for the source date. The FRAX/DOLA LP source check confirms the
direct path is not visible ERN/CDP debt and is separately allocated from the
WBTC DOLA leg. It now also ties one large Fantom bridge-source branch to the
`2022-08-18` Reaper DAI recovery row with exact 2022 Koinly evidence, via
`sDAI -> DIGI #90 -> DAI -> USDC -> Arbitrum USDC.e`. That improves provenance
for part of the DOLA/FRAX pool, but it remains source-open Layer C evidence
rather than bank-grade fiat-source proof for the full branch. The WFTM payment
is also included because the
trace shows `2,877.7 WFTM` spent from the claiming wallet into the OATH
TGE/LGE contract path on `2022-02-24`, and Koinly has that outflow at
`37,976.46 SEK`, converted at `0.4107 SEK/PLN` to `15,596.93 PLN`. The
remaining OATH-native pieces have a different evidentiary path because the
user's history mixes TGE purchase, rewards/bonus, and farming receipts. Those
are preserved for later amendment or adviser review, but they are not in this
urgent filing run.

## OATH TGE / LGE Scan Status

The focused Fantom/Koinly scan did not find a large USDC/stablecoin payment
from a known Fantom wallet to the OATH distributor or claim contracts in the
likely launch window. It found two April 16 direct OATH transfers from
`0x8b4441e79151e3fc5264733a3c5da4ff8eac16c1`, one April 17 claim/mint-style
receipt paired with a wallet call to `0x96662f375a9734654cb57bbfeb31db9dd7784a7f`,
and zero large stablecoin outflows to the OATH distributor.

The later source trace materially improves the OATH-native bucket: it shows
`114,148` OATH from early distributor `0x8b4441e79151e3fc5264733a3c5da4ff8eac16c1`
in 2022 and `145,833.3333333332` OATH from recurring batch vesting/distributor
`0xd152f549545093347a162dce210e7293f1452150` from November 2022 through April
2023. The move-date OATH-native LP bucket is therefore no longer an unexplained
token source. The unresolved question is valuation and tax-basis treatment,
especially for 2023 pre-move vesting/distributor receipts where no Koinly 2023
export is in the repo.

The current result is therefore: include the documented WFTM payment-side proof,
but do not add the remaining OATH-native TGE/vesting/reward quantity as a
separate market-value cost. The remaining OATH-native rows remain preserved as a
possible later basis analysis using Koinly SEK values, source contracts, and
self-calculated 2023 pre-move receipt values.

## Threshold

Current split-year sensitivity says imported basis of about `116,786.51 PLN` is
enough to keep 2024 and 2025 PIT-38 tax at zero.

This selected package uses `588,848.16 PLN`, giving `472,061.65 PLN` surplus
over the threshold. That surplus becomes the 2025 cost carry-forward, rounded by
the PIT-38 engine to `472,061.65 PLN`.

## Avalanche frxETH / sfrxETH Check

The newly noticed Avalanche `frxETH` / `sfrxETH` position is not added to the
move-date imported-basis pool. The full Routescan Avalanche token-transfer
archive shows the first `frxETH` / `sfrxETH` rows on Metamask3 on
`2023-06-03`, after Polish residency started. The actual Avalanche Frax token
contracts found in the archive had no deployed code and no wallet balance at
the `2023-04-11T23:59:59Z` move-date block. This can still matter for
post-residency normalization, but it is not a pre-residency move-date asset.

## Evidence Package

Use these as the audit file:

- `private/evidence/onchain/move-date-inventory-2023-04-12/move-date-inventory-2023-04-12.md`
- `private/evidence/onchain/move-date-inventory-2023-04-12/move-date-cost-provenance.md`
- `private/evidence/onchain/move-date-inventory-2023-04-12/move-date-basis-decision.md`
- `private/evidence/onchain/move-date-inventory-2023-04-12/move-date-supportable-basis-candidates.csv`
- `private/evidence/onchain/move-date-inventory-2023-04-12/move-date-gtrain-grain-provenance.md`
- `private/evidence/onchain/move-date-inventory-2023-04-12/move-date-unwind-workpaper.md`
- `private/evidence/onchain/move-date-inventory-2023-04-12/move-date-wbtc-basis-rollforward.md`
- `private/evidence/onchain/move-date-inventory-2023-04-12/move-date-wbtc-cdp-basis-trace.md`
- `private/evidence/onchain/move-date-inventory-2023-04-12/move-date-wbtc-stablecoin-source-open.md`
- `private/evidence/onchain/move-date-inventory-2023-04-12/move-date-reaper-multistrategy-hack-thread.md`
- `private/evidence/onchain/move-date-inventory-2023-04-12/move-date-reaper-multistrategy-loss-recovery-match.csv`
- `private/evidence/onchain/move-date-inventory-2023-04-12/move-date-wbtc-reaper-recovery-link.md`
- `private/evidence/onchain/move-date-inventory-2023-04-12/move-date-oath-provenance.md`
- `private/evidence/onchain/move-date-inventory-2023-04-12/move-date-oath-fantom-origin-trace.csv`
- `private/evidence/onchain/move-date-inventory-2023-04-12/move-date-oath-tge-payment-scan.md`
- `private/evidence/onchain/move-date-inventory-2023-04-12/move-date-oath-tge-stable-outflow-candidates.csv`
- `private/evidence/onchain/move-date-inventory-2023-04-12/move-date-oath-tge-wftm-payment-candidates.csv`
- `private/evidence/onchain/move-date-inventory-2023-04-12/move-date-oath-tge-koinly-oath-window.csv`
- `private/evidence/onchain/move-date-inventory-2023-04-12/move-date-oath-vesting-trace.md`
- `private/evidence/onchain/move-date-inventory-2023-04-12/move-date-oath-vesting-source-transfers.csv`
- `private/evidence/onchain/move-date-inventory-2023-04-12/move-date-avalanche-fraxeth-check.md`

The Reaper evidence covers all six lost receipt families:

`rfUSDC->USDC`, `rfDAI->DAI`, `rfUSDT->fUSDT`, `rfETH->ETH`, `rfBTC->BTC`,
and `rfWFTM->WFTM`.

## Generated PIT-38 Outputs

Generated with:

```bash
PYTHONPATH=src python3 -m tax_calc pit38 \
  --policy split_year_high_risk \
  --primary-policy split_year_high_risk \
  --imported-fiat-costs 77955.80 \
  --imported-successor-costs 510892.36 \
  --output-dir outputs/pit38_max_no_debt_plus_oath_weth_dola_tge_rfgrain
```

Output folder: `outputs/pit38_max_no_debt_plus_oath_weth_dola_tge_rfgrain/`

| Year | Revenue | Current-year costs | Prior-year/imported costs | Income | Carry-forward |
| --- | ---: | ---: | ---: | ---: | ---: |
| 2023 | `264,113.82 PLN` | `500,922.56 PLN` | `588,848.16 PLN` | `0.00 PLN` | `825,656.90 PLN` |
| 2024 | `785,654.54 PLN` | `488,065.61 PLN` | `825,656.90 PLN` | `0.00 PLN` | `528,067.97 PLN` |
| 2025 | `271,316.95 PLN` | `215,310.63 PLN` | `528,067.97 PLN` | `0.00 PLN` | `472,061.65 PLN` |

## Important Caveat

The calculator calls this `split_year_high_risk` because part of the basis is
Layer C replacement/source-open basis through pre-move DeFi and crypto-to-crypto
transformations. That label does not mean "unsupported"; it means it is not the
ultra-conservative fiat-purchase-only position.

The practical explanation is:

- Swedish K4 records are messy and incomplete for DeFi.
- The taxpayer made a good-faith attempt to report Sweden.
- The Polish filing uses a limited subset of assets actually held or represented
  at the Poland move date.
- The subset is supported by on-chain traces, Koinly exports where available,
  and Reaper loss/recovery workpapers.
- The filing claims WBTC, GLP, `rf-soWETH`, BPT-GTRAIN ETH plus stablecoin-
  funded GRAIN, the WETH-linked plus DOLA-funded parts of WETH/OATH, the
  documented OATH TGE/LGE WFTM payment, and the small `rf-grain-OP` survivor.
- The filing does not claim ERN/debt legs, BPT-RESERVE, OATH-native
  bridge/reward/vesting buckets beyond the WFTM payment-side proof, spam
  tokens, or unsupported LP/vault balances.

## Source Anchors

- Polish MF guidance states that crypto-to-crypto exchange is not taxed in
  Poland, and PIT-38 is used for crypto disposal reporting:
  https://www.podatki.gov.pl/podatki-osobiste/pit/informacje-podstawowe/co-jest-opodatkowane/zbycie-kryptowalut/
- PIT Act Article 22(14)-(16) frames crypto costs as documented expenses
  directly incurred to acquire virtual currency and carries excess costs
  forward:
  https://isap.sejm.gov.pl/isap.nsf/download.xsp/WDU20250000163/T/D20250163L.pdf
