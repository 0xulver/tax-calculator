# Synthesis: Tax Treatment of USDC Salary Payments in Poland

Sources: ChatGPT 5.4 Pro, ChatGPT Deep Research, Perplexity, Gemini 3.1 Deep Research

---

## Full Consensus (All 4 sources agree)

### 1. PIT-37 was the wrong form — should be PIT-36

Unanimous and unambiguous. PIT-37 is exclusively for income processed by a Polish platnik (payer) who issued PIT-11/PIT-11A/PIT-40A/PIT-R/IFT-1R. A US company with no Polish presence cannot issue any of these. PIT-36 is the correct form for self-reported income without a Polish payer. This applies to both 2023 and 2024.

### 2. USDC salary = service income taxed at receipt (the "barter doctrine")

All sources confirm: receiving USDC as payment for services is treated as a **barter transaction** (transakcja barterowa). The taxable event occurs **at the moment USDC is received in the wallet**, not when it's later converted to fiat. This aligns with the Swedish Skatteverket precedent.

Multiple KIS interpretations cited across sources confirm this:
- KIS 0113-KDIPT2-3.4011.549.2019.3.PR (Jan 2020): crypto for IT services = income at receipt
- KIS 0111-KDIB1-1.4010.303.2023.1.MF (Jul 2023): crypto as IT payment = barter, cost basis = invoice value
- KIS 0115-KDIT1.4011.25.2024.1.MR (Feb 2024): service receivable settled in crypto, acquisition cost = remuneration value

### 3. The "double-reporting" approach is correct and avoids double taxation

All sources agree on the two-step mechanism:
1. **PIT-36**: USDC received as salary = service income, taxed at progressive rates (12%/32%)
2. **PIT-38**: When USDC is later sold for EUR = crypto disposal, but cost basis equals the PLN value already declared as income

This makes the USDC->EUR conversion **nearly tax-neutral** (only FX movement between receipt and conversion is taxed at 19%). The cost basis neutralization is explicitly endorsed by KIS interpretations.

### 4. Monthly advance tax payments (zaliczki) were required and missing

Art. 44 ust. 1a PIT Act: taxpayers receiving Art. 13 income without a Polish payer must self-calculate and pay monthly advances by the 20th of the following month. This was not done for 2023 or 2024. Interest on late payments accrues from each missed monthly deadline. Paying the full annual tax at filing does NOT extinguish the interest.

### 5. PIT/ZG (foreign income annex) should have been attached

All sources agree PIT/ZG is required when income comes from a foreign source. However, two sources note this is less critical than other errors because no US tax was paid (so the annex would show zero foreign tax credit). Still a formal compliance error.

### 6. Missing 2024 PIT-38 is a significant omission

If any USDC was converted to fiat in 2024 (which it was), PIT-38 should have been filed — even though the tax would be near-zero due to the high cost basis. Additionally, PIT-38 should declare all crypto acquisition costs (the salary USDC) to establish the carry-forward chain.

### 7. Pre-JDG 2025 income (Jan-Apr) cannot be retroactively put into the JDG

All sources agree: the JDG's ryczalt regime starts from the JDG registration date. Income earned before that date must be reported separately on PIT-36 as personal income. You cannot retroactively pull earlier income into the JDG.

### 8. PLN valuation method for USDC

USDC should be valued using the **NBP USD mid-rate from the last business day before receipt**. Since USDC ≈ 1 USD, this effectively means: USDC amount x NBP USD rate (day before).

### 9. Poland has exclusive taxing rights under the 1974 US-Poland treaty

Work performed from Poland for a US company = taxable only in Poland (no US fixed base/PE). No US tax was paid. The treaty's independent personal services article supports Poland-only taxation.

---

## Disagreements Between Sources

### 1. Is Art. 13 pkt 8 classification defensible, or is this de facto business activity?

| Source | Position | Risk Level |
|---|---|---|
| ChatGPT 5.4 Pro | "Arguable but plausible" — Art. 13 is one plausible reading, but the facts increase business risk | Medium |
| ChatGPT Deep Research | Art. 13 pkt 8 is "legally defensible" — supported by KIS precedent for US company contractor | Low-Medium |
| Perplexity | "Probably correct" — cites specific KIS ruling confirming Art. 13 pkt 8 for foreign US company contractor | Low-Medium |
| **Gemini** | **"Highly precarious"** — the pattern overwhelmingly resembles business activity (Art. 5a pkt 6), reclassification risk is severe, could lose the 20% deduction and trigger ~30K PLN additional tax | **High** |

**Assessment**: Gemini takes the most alarming view. The other three acknowledge the risk but cite KIS precedent specifically supporting Art. 13 pkt 8 for a foreign US company paying a Polish contractor. The key KIS ruling (cited by Perplexity and ChatGPT Deep Research) confirmed that income from a US company as "niezalezny kontraktor" is Art. 13 pkt 8. However, Gemini's concern about the continuous, organized nature of the work is valid — this is the grey zone.

### 2. Is PIT/ZG mandatory or just advisable?

| Source | Position |
|---|---|
| ChatGPT 5.4 Pro | "Probably not the main problem" — PIT/ZG is for work performed abroad; work done from Poland for a US client is not obviously "foreign work income" |
| ChatGPT Deep Research | Safe compliance posture is to include it, but strongest official guidance ties PIT/ZG to Art. 27 treaty methods |
| Perplexity | **Mandatory** — foreign-sourced income requires PIT/ZG regardless |
| Gemini | **Mandatory** — failure to attach is a "material disclosure violation" |

**Assessment**: Split. The practical impact is small (PIT/ZG would show USA as source country, zero foreign tax paid, proporcjonalne odliczenie method with zero credit). Filing it is harmless; not filing it is a procedural gap.

### 3. ZUS liability: How severe is it?

This is where the sources diverge most dramatically.

| Source | Position | Estimated Liability |
|---|---|---|
| ChatGPT 5.4 Pro | "Real issue" — ZUS has a foreign payer mechanism, nonpayment creates exposure | Not quantified |
| ChatGPT Deep Research | "Genuine exposure point" — ZUS provides foreign-payer registration, can't assume nil | Not quantified |
| Perplexity | **"Single largest financial risk"** — full ZUS at ~38-40% of gross = **~180-190K PLN for 2024 alone** | **~180-190K PLN** |
| Gemini | **"Most severe and unaddressed liability"** — classifying as umowa zlecenie triggers mandatory ZUS on full gross, ~30% = **~140K+ PLN for 2024** | **~140K+ PLN** |

**Assessment**: All four agree ZUS is a real issue. Perplexity and Gemini provide alarming numbers (140-190K PLN for 2024). However, there are important nuances the sources acknowledge:
- Whether the umowa zlecenie classification actually requires ZUS registration depends on the specific facts
- The US-Poland Totalization Agreement may affect which country's social security applies
- If the activity is reclassified as business (not zlecenie), the ZUS calculation changes entirely (JDG preferential rates would apply instead of full zlecenie rates)
- No source has verified whether any US Social Security was paid

**This needs a specialized ZUS advisor — the numbers are too large and fact-dependent for desk research alone.**

### 4. The "irreconcilable dilemma" (Gemini's framing)

Gemini uniquely identifies a structural paradox:
- **Keep umowa zlecenie** → preserve 20% cost deduction → but admit to massive ZUS liability (~140K+ PLN)
- **Reclassify as business** → escape zlecenie ZUS → but lose 20% deduction, gain ~30K PLN additional income tax, and admit to operating an unregistered business (KKS penalty risk)

The other sources don't frame it as starkly, but they all acknowledge the tension between the classification choice and its ZUS consequences.

### 5. USDC valuation: NBP USD rate vs market price

| Source | Position |
|---|---|
| ChatGPT 5.4 Pro | NBP USD rate is a **proxy** — technically USDC is not USD, so market value is the cleaner legal route. But NBP USD is practical if USDC tracked $1 closely |
| ChatGPT Deep Research | KIS practice: determine crypto market value in USD, then convert to PLN via Art. 11a (NBP rate). NBP USD is acceptable for USDC |
| Perplexity | NBP USD rate is correct — Art. 11a ust. 1 PIT applies, USDC = 1 USD for this purpose |
| Gemini | NBP USD rate from last business day before receipt — straightforward |

**Assessment**: Minor disagreement. ChatGPT 5.4 Pro is technically correct that USDC isn't legally USD, but all sources agree the practical approach (using NBP USD rate) is acceptable and is what KIS interpretations effectively endorse.

---

## Key Takeaways

### What the tax company got right
- The **income amount** (448K/479K PLN) is reasonable based on invoices
- The **Art. 13 pkt 8 classification** is plausible and supported by KIS precedent
- The **20% cost deduction** is correct for Art. 13 pkt 8
- The **barter doctrine** (income at receipt, cost basis for PIT-38) is the correct approach
- The **progressive tax calculations** are arithmetically correct

### What the tax company got wrong
- **PIT-37 instead of PIT-36** (all 4 sources agree)
- **No monthly advance payments** (all 4 sources agree — creates interest liability)
- **No PIT/ZG attachment** (3 of 4 say mandatory)
- **No PIT-38 for 2024** (all 4 sources agree this is needed)
- **ZUS completely ignored** (all 4 sources flag this as a real issue)

### What remains genuinely uncertain
- **Art. 13 vs business activity**: KIS precedent supports Art. 13, but the facts push toward business
- **ZUS liability magnitude**: Could be 0 (if the classification can be defended differently) or 140-190K PLN per year
- **Whether an individual KIS interpretation (interpretacja indywidualna) should be obtained**: Perplexity recommends it (40 PLN fee) to bind the tax authority going forward

---

## Action Items

### URGENT (before April 30, 2026)

1. **File 2024 PIT-38** — declare USDC acquisition costs (479K PLN) + carry-forward from 2023 (222K PLN). Even if tax = 0, this preserves the cost basis chain for 2025.

2. **File 2025 PIT-36** for pre-JDG income (Jan-Apr 2025, 40,500 USDC) — separate from JDG PIT-28. Include PIT/ZG.

3. **File 2025 PIT-38** — 15 fiat-exit events, with cost basis from salary + carry-forward.

4. **Calculate and pay overdue 2025 advance payments** for Jan-Apr pre-JDG income. Consider accompanying with czynny zal.

### HIGH PRIORITY (within weeks)

5. **Consult a ZUS specialist** — this is the single biggest financial risk. The zlecenie classification implies mandatory ZUS at ~30-40% of gross income. A specialist can assess:
   - Whether the US-Poland Totalization Agreement provides protection
   - Whether reclassification changes the picture
   - What the realistic enforcement risk is
   - Whether a payment plan (uklad ratalny) is available

6. **File korekta for 2024**: PIT-37 -> PIT-36 + PIT/ZG attachment. Consider including czynny zal for the advance payment issue.

### MEDIUM PRIORITY (after April deadline)

7. **File korekta for 2023**: same PIT-37 -> PIT-36 correction + PIT/ZG.

8. **Calculate advance payment interest** for both 2023 and 2024 — estimated 5-12K PLN total. Pay proactively.

9. **Consider applying for interpretacja indywidualna from KIS** (40 PLN) to get a binding ruling on:
   - USDC classification as waluta wirtualna post-MiCA
   - Barter doctrine applicability for Art. 13 non-business income
   - This would provide forward-looking protection

### STRATEGIC DECISION NEEDED

10. **Resolve the classification question**: Art. 13 (umowa zlecenie) vs business activity (dzialalnosc gospodarcza). This decision affects:
    - 20% cost deduction (Art. 13 only)
    - ZUS liability (dramatically different between zlecenie and JDG)
    - Whether retroactive JDG registration is needed
    - Potential KKS penalty risk for unregistered business

    **This cannot be resolved without professional advice.** The financial stakes are too high (potentially 100K+ PLN difference depending on the path chosen).
