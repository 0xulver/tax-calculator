# Response to Summons — Czynności Sprawdzające PIT 2023 (Poz. 36 PIT-38)

**Summons received:** Wednesday 2026-06-03 (e-mail)
**Issuing office:** Trzeci Urząd Skarbowy Warszawa-Śródmieście, Pierwszy Dział
Czynności Analitycznych i Sprawdzających
**Case officer:** Sylwia Kurzydłowska-Buczko, starszy referent
**Legal basis cited:** Art. 155 § 1, art. 272, art. 274 Ordynacji podatkowej
**Response deadline:** 7 days from receipt → **Wednesday 2026-06-10**

## What they are asking about

Documents/explanations for **Poz. 36 of the 2023 PIT-38 korekta**
(submitted 2026-04-27, document nr `cff427bb38a5e8fc6fb37a0a85cccf1d`):
**588,848.16 PLN** of "koszty uzyskania przychodu poniesione w latach
ubiegłych z odpłatnego zbycia walut wirtualnych".

The figure looks anomalous to the office because no 2022 PIT-38 exists. It is
in fact imported pre-residency basis under the topic 17 split-year policy
(`docs/tax-law/17-pre-residency-usdc-basis/`), composed per
`docs/todo/pit38-simplified-filing-position.md`.

## Strategy: minimal submission package

Decision (taxpayer, 2026-06-07): submit a **minimal, readable package** —
answer exactly what was asked, attach only what carries the story, keep deep
evidence in reserve. Everything not attached is explicitly offered "na
żądanie Organu" in the letter (sections III, IV, VI, VII), so the posture is
cooperative, not evasive. Rationale: raw exchange ledgers show ALL activity
(disposals, transfers), and 80 pages of English DeFi traces invite questions
a desk-check clerk cannot evaluate.

### What gets submitted — e-mail with 3 PDF attachments

Submission form chosen 2026-06-07: **e-mail reply to the case officer's
summons e-mail** (explicitly allowed by the summons). Ready-made files:

| What | File |
| --- | --- |
| E-mail subject + body (copy-paste into Gmail) | `EMAIL-READY-copy-paste.md` — content identical to `SEND-1-the-letter-POLISH.md`, reformatted for plain-text e-mail |
| Attachment 1 | `Zalacznik-1-Specyfikacja.pdf` (generated from `SEND-2-annex1-cost-breakdown-POLISH.md`) |
| Attachment 2 | `Zalacznik-2-Rejestr-zakupow.pdf` (landscape; generated from `SEND-3-annex2-purchase-register-POLISH.md`) |
| Attachment 3 | `Zalacznik-3-Umowa-zakwaterowania.pdf` (copy of the Vonder agreement) |

`MagnusBwezwanie (1).pdf` in this folder is a DIFFERENT summons (PIT-36 2025,
part L→Q advances, case 1449-SKA-1.4031.1099.2026.1, officer Aleksandra
Kalinowska) — answered separately by the taxpayer; not part of this package.

The corrected PIT-38 + UPO are NOT attached — the office already has the
korekta (it triggered this summons); the letter cites its document number
`cff427bb38a5e8fc6fb37a0a85cccf1d`, which is sufficient to identify it.

**Do NOT send:** `FOR-YOU-ONLY-letter-translation-ENGLISH.md` — that is the
English translation of PDF 1 so the taxpayer knows what he is signing.

### Held in reserve — provide ONLY if the office asks

| Reserve item | Source |
| --- | --- |
| Official exchange exports (Kraken/Binance/FTX) | `docs/crypto-cex-transactions/` |
| Move-date holdings inventory 2023-04-12 | `private/evidence/onchain/move-date-inventory-2023-04-12/` |
| WBTC trace + roll-forward | `move-date-wbtc-cdp-basis-trace.md`, `move-date-wbtc-basis-rollforward.md` |
| Component provenance (GLP / BPT-GTRAIN / WETH-OATH / OATH TGE / rf-grain-OP) | same folder workpapers |
| Reaper hack loss/recovery thread | `move-date-reaper-multistrategy-hack-thread.md`, `move-date-wbtc-reaper-recovery-link.md` |
| NBP rate schedule | regenerate from `data/nbp_cache.json` |
| Coinbase full export | taxpayer to request from Coinbase if asked |
| Celsius bank statements (Simplex-Elastum charges, 6 txns) | taxpayer's bank if asked |
| Optional residency strengtheners | Vonder deposit/fee bank transfers; Skatteverket flyttanmälan |

## Submission plan

1. **Sun–Mon:** finalize the 4-annex package; convert letter + annexes 1–2 to
   PDF.
2. **Mon–Tue:** review by a doradca podatkowy (strongly recommended — the
   posture is the repo's `split_year_high_risk` Layer C package and ~589k PLN
   of costs / up to ~112k PLN of 19% tax across 2023–2025 ride on it).
3. **By Wed 2026-06-10:** submit via **e-Urząd Skarbowy (pismo ogólne)** for a
   UPO timestamp **and** send a courtesy copy by e-mail to the case officer.

## Correction-history narrative (letter section III — keep consistent everywhere)

- Original 2023 PIT-37 + PIT-38 filed late on **2024-06-07** by a tax firm,
  with czynny żal (reason given then: unawareness of the April 30 deadline —
  consistent with the "new arrival" narrative).
- Original PIT-38: revenue 226,115.71 / costs 448,108.20 / poz. 36 = 0 /
  carry-forward 221,992.49 / tax 0 (see
  `docs/personal-tax/2023/analysis-2023-filing.md`).
- The firm never asked about pre-residency crypto purchases/holdings; the
  taxpayer discovered their relevance through own research in 2026.
- Korekta 2026-04-27 **raised revenue by 37,998.11** (added the missed FTM
  disposal etc.) and added poz. 36 — strongest good-faith point; the letter
  leads with it in section III pt 4.
- If the office asks for the tax firm's identity/engagement papers, that is a
  normal follow-up — have them ready.

## Risk notes (do not include in the letter)

- The deductibility of pre-residency acquisition costs is supportable but not
  squarely confirmed by KIS; topic 17 synthesis flags it as KIS-dependent.
- **WSA Warszawa 29.08.2024, III SA/Wa 1290/24** (cited in the letter, verified
  via web search 2026-06-07; advisor should pull the full text from
  orzeczenia.nsa.gov.pl): pre-residency costs deductible if not deducted
  abroad — but the court accepted only **fiat-for-crypto** purchase costs and
  denied crypto-to-crypto exchange values. This supports the headline position
  and Annex 2 (purchase register), but cuts against the swap-valued Layer C
  components if the office digs in. If escalated, consider reframing Layer C
  valuations toward original fiat cost (Annex 2 chain) rather than swap-time
  values.
- Some components are Layer C replacement/successor basis through pre-move
  DeFi steps — the letter presents them honestly as on-chain-documented
  acquisition costs of assets held at the move date.
- Part of the amount in Poz. 36 was incurred Jan–Apr 2023 (pre-move, same tax
  year). The letter discloses this and notes the Poz. 35/36 allocation has no
  effect on income or tax.
- If the office rejects the position, the fallback ladder is: exact-anchor
  subset (119,042.69 PLN) → Layer A only (77,955.80 PLN) → korekta with tax.
  Do not volunteer fallbacks now.
- Pre-residency Sweden-taxed salary USDC (154,317 USDC ≈ 687,583.27 PLN
  received 2022–2023) is NOT claimed as a separate bucket and the letter says
  so (conservatism signal + source-of-funds support). Only ~1,674.68 plain
  USDC remained at the move date; the rest was consumed pre-move or
  transformed into the Layer C positions whose swap-time values are already in
  the claim — adding a salary-valued bucket would double-count. Do NOT ask the
  verification clerk for a position on it (no binding effect); if the
  carry-forward beyond 2026 matters, file an ORD-IN individual interpretation
  with KIS per the topic 17 "KIS Interpretation Focus" question, then korekta.
