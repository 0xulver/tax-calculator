# PIT-38 External Audit Response Synthesis

Date: 2026-04-27  
Folder: `docs/tax-law/19-pit38-filing-external-audit/`  
Subject: Proposed PIT-38 filings/corrections for 2023, 2024, and 2025

## Source Responses Reviewed

- `PIT-38 Filing Audit - ChatGPT 5.5 Pro.md`
- `Crypto Tax Filing Audit_ Poland - Gemini 3.1 Deep Research.pdf`
- Original request: `external-audit-prompt.md`

This document synthesizes the two external responses. It is not a new primary
legal opinion. Both responses appear to be based on the prompt package rather
than direct access to all private evidence and generated repo files, so their
findings are most useful as a legal/evidence risk review, not as complete
certification of every ledger row.

## Bottom Line

The two responses agree that the proposed PIT-38 arithmetic and form-field
mapping are internally consistent. They also agree that the split-year approach
is defensible if `2023-04-12` is the correct Polish tax-residence start date,
and that documented pre-residency acquisition costs can be imported into Polish
PIT-38 where they relate to crypto assets held when Polish residency began.

The main unresolved risk is not arithmetic. It is the legal and evidentiary
strength of Layer C imported basis: historical cost traced through DeFi
wrappers, LP tokens, receipt tokens, CDPs, bridge flows, and crypto-to-crypto
transformations. ChatGPT frames Layer C as high-risk and says to file only with
clear risk disclosures. Gemini is more supportive and treats the package as
ready if the double-counting and evidence checks hold. Where they conflict, the
safer filing posture is to weight ChatGPT's risk framing more heavily and use
Gemini's analysis as supporting rationale.

No external response requires a change to the proposed PLN values solely on
arithmetic grounds. The proposed selected chain remains:

| Year | Revenue PLN | Current costs PLN | Prior/imported costs PLN | Income PLN | Tax PLN | Carry-forward PLN |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 2023 | 264,113.82 | 500,922.56 | 588,848.16 | 0.00 | 0.00 | 825,656.90 |
| 2024 | 785,654.54 | 488,065.61 | 825,656.90 | 0.00 | 0.00 | 528,067.97 |
| 2025 | 271,316.95 | 215,310.63 | 528,067.97 | 0.00 | 0.00 | 472,061.65 |

## Shared Findings

Both responses support these points:

- Polish PIT-38 crypto reporting uses annual cost pooling and carry-forward,
  not FIFO.
- Crypto-to-crypto exchanges should not be treated as direct PIT-38 taxable
  revenue events.
- Pre-residency disposals before Polish residence should not be included in
  Polish PIT-38 unless there is a separate Polish-source issue.
- Documented pre-residency fiat/direct acquisition costs are supportable as
  imported basis when the assets survived into Polish residency and are later
  relevant to Polish taxable disposals.
- Debt proceeds and minted/borrowed stablecoins should not create new cost
  basis. Excluding ERN debt proceeds and BPT-RESERVE by default is correct.
- Rewards, airdrops, vesting allocations, and unsupported native-token buckets
  should not be given cost basis unless there is a separate paid-acquisition or
  taxed-income analysis.
- Post-residency crypto remuneration can become PIT-38 acquisition cost if the
  remuneration was taxed on receipt and the value is documented.
- Filing order should preserve the carry-forward chain: 2023 correction first,
  then 2024, then 2025.

## Main Disagreement

The important disagreement is how strong Layer C is.

ChatGPT's view:

- Layer C is the main high-risk item.
- The package should not describe DeFi swaps or LP deposits as creating new
  tax costs.
- Only original documented fiat/direct/taxed-remuneration expenditure should be
  claimed, with crypto-to-crypto and DeFi transactions used only as factual
  tracing links.
- If Layer C is excluded and only the 77,955.80 PLN Layer A imported basis is
  used, the conservative chain would produce about 7,378 PLN of PIT-38 tax for
  2025 and no carry-forward.

Gemini's view:

- Layer C is aggressive but strategically and legally defensible if it is framed
  as historical cost rolling forward through tax-neutral virtual-currency
  transformations.
- Wrapped tokens such as WETH/WBTC are highly defensible.
- LP/receipt tokens such as GLP and BPT-GTRAIN are gray but can be defended as
  virtual-currency-like digital representations if freely transferable and
  exchangeable.
- Excluding debt-funded branches and native/reward buckets makes the posture
  much more defensible.

Synthesis:

The selected filing posture is defensible only if the explanation is narrow:
`original documented acquisition expenditure traced through successor assets`.
It should not be presented as claiming cost for crypto-to-crypto swap value,
DeFi receipt-token fair market value, swap fees, CDP/stability fees, debt
principal, or valuation uplift.

## Imported Basis Classification

| Candidate | Amount PLN | Synthesis classification |
| --- | ---: | --- |
| Koinly-matched reviewable move-date rows | 77,955.80 | Strongest imported-basis layer if backed by exchange/bank records and move-date holdings. |
| Ethos WBTC trove collateral full roll-forward | 142,580.44 | Defensible but needs a cohesive trace showing original WBTC cost survived and was not duplicated into ERN/DOLA/debt branches. |
| GLP USDC.e predecessor | 44,138.35 | Defensible if it is original USDC.e/stablecoin acquisition cost traced into GLP, not a new FMV reset at LP deposit. Receipt-token classification remains a risk. |
| `rf-soWETH` WETH inputs | 5,292.90 | Defensible as wrapper/receipt tracing if WETH input cost is documented and not reused elsewhere. |
| BPT-GTRAIN ETH-only input | 25,964.04 | Defensible but receipt-token gray area; needs ETH input trace and no duplication. |
| BPT-GTRAIN stablecoin-funded GRAIN input | 100,518.44 | Weak but defensible; large enough to need a clean stablecoin-to-GRAIN-to-BPT trail and no overlap with other stablecoin-funded buckets. |
| WETH/OATH LP WETH-linked component | 159,526.15 | Weak but defensible; very large amount, so exact LP input split and WETH basis continuity are important. |
| WETH/OATH LP DOLA-funded OATH component | 17,172.86 | Conditional. Include only if the DOLA source is independent paid-for capital and not minted/borrowed against WBTC or another already-counted collateral branch. |
| OATH TGE/LGE WFTM payment-side proof | 15,596.93 | Defensible for the paid WFTM side only. Do not include reward, vesting, or distributor uplift beyond documented payment-side cost. |
| `rf-grain-OP` surviving OP-funded receipt basis | 102.25 | Immaterial and acceptable if the OP-funded trace is clean. |

Excluded items should stay excluded unless new evidence creates a clearly
separate paid-acquisition basis:

- ERN debt proceeds and ERN-funded legs.
- BPT-RESERVE.
- Remaining OATH-native bridge/reward/vesting/distributor buckets.
- Unsupported LP/vault balances.
- Avalanche `frxETH` / `sfrxETH` as move-date basis if acquired only after
  Polish residency.
- Pre-residency salary-paid USDC merely because it was salary, unless surviving
  units and taxed-value/cost provenance are separately documented.

## Specific Checks Before Submission

1. Confirm the 2024 PIT-38 procedural status in e-Urzad.
   - If a 2024 PIT-38 exists or was auto-accepted, submit a correction.
   - If no 2024 PIT-38 exists, submit a first/late PIT-38 and send a targeted
     czynny zal.

2. Confirm DOLA-funded OATH independence.
   - Follow-up local check `move-date-dola-oath-source-check.md` finds the
     direct DOLA source was an Arbitrum `crAMM-FRAX/DOLA` liquidity removal, not
     ERN/CDP debt.
   - The same removal produced `21,344.719438193822835596 DOLA`: `4,000 DOLA`
     went to WETH, `4,000 DOLA` went to OATH, and
     `13,344.719438193822835596 DOLA` went to WBTC, so the OATH and WBTC legs
     are separate units from the same removal.
   - Follow-up local check `move-date-frax-dola-lp-source-check.md` traces the
     FRAX/DOLA LP to pre-move stablecoin and LP unwinds. A further trace ties
     one large Fantom bridge-source branch to the `2022-08-18` Reaper DAI
     recovery row with exact 2022 Koinly evidence, through
     `sDAI -> DIGI #90 -> DAI -> USDC -> Arbitrum USDC.e`.
   - This improves provenance for part of the FRAX/DOLA source pool, but it is
     still not bank-grade fiat purchase proof for the full branch and does not
     by itself settle the cost treatment of pre-move DIGI/Scream uplift.
   - Remaining risk is Layer C / source-open stablecoin replacement basis, not
     immediate DOLA-vs-WBTC double counting.

3. Confirm no Layer C bucket uses a new FMV basis.
   - Every included amount should tie back to original paid acquisition cost,
     taxed remuneration, or another already documented acquisition expenditure.
   - Crypto-to-crypto and DeFi transactions should be tracing steps only.

4. Confirm whether any imported basis was incurred in 2023 before `2023-04-12`.
   - ChatGPT flags that same-year pre-residency acquisition costs may belong in
     2023 current-year cost field rather than prior-year/imported-cost field.
   - This does not change the 2023 total cost pool, but it may affect field
     presentation.

5. Keep the evidence packet local and organized.
   - Do not attach all private evidence unless requested.
   - Retain bank statements, exchange exports, transaction hashes, move-date
     holdings, and workpapers proving no double counting.

6. Check the displayed NBP rate dates in generated reports before using them as
   an audit packet.
   - The selected reports use the correct PLN values for the highlighted
     Paymonade repairs, but the displayed NBP rate date can be misleading when
     the prior weekday was a Polish holiday.
   - Example: the 2024-11-04 ETH sale shows `4.3530 EUR/PLN` but displays
     `2024-11-01`; a local NBP API spot-check shows `4.3530` is the
     `2024-10-31` table, because 2024-11-01 has no table.
   - Example: the 2025-06-20 USDC purchase shows `4.2717 EUR/PLN` and displays
     `2025-06-19`; a local NBP API spot-check shows `4.2717` is the
     `2025-06-18` table, because 2025-06-19 has no table.

## Filing Narrative To Use

The correction explanation should be conservative and fact-based:

- The 2023 correction adds virtual-currency revenue and costs omitted or
  incorrectly carried in the prior filing.
- Imported basis consists of documented acquisition costs for assets held when
  Polish tax residence began.
- The imported basis is not a synthetic full-history Polish crypto pool.
- Crypto-to-crypto transactions are not treated as direct PIT-38 revenue or cost
  events.
- DeFi and bridge transactions are used only to trace original documented cost
  into successor assets.
- Debt-funded branches, native rewards, unsupported receipt tokens, and
  duplicate branches have been excluded.

For 2024, use czynny zal only if the portal requires a late first filing rather
than a correction. If submitting only a correction, a concise explanatory pismo
may still be useful, but the penal-fiscal posture is different from a late first
return.

## Practical Recommendation

The selected zero-tax, 472,061.65 PLN carry-forward chain can be submitted if
the taxpayer accepts the Layer C audit risk and the final DOLA/WBTC and
same-year field checks pass.

Do not submit it as a "clean, no-risk" position. Submit it as a documented,
good-faith reconstruction with a clear audit note and preserved evidence.

If the taxpayer wants the lowest legal-risk filing instead, use the Layer-A-only
conservative variant described in the ChatGPT response. That variant gives up
most imported basis and creates an estimated 2025 PIT-38 tax of about 7,378 PLN.
