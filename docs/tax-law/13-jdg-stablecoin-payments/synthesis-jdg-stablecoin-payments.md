# Synthesis: JDG Stablecoin Payments vs EUR Bank Transfers

**Sources**: ChatGPT 5.4 Pro, ChatGPT Deep Research, Perplexity, Gemini 3.1 Deep Research
**Topic**: Tax implications of receiving USDC vs EUR for a JDG on ryczałt 12% (PKD 62.01.B)

---

## Key Findings — Full Agreement (4/4 Models)

### 1. Two-Track Tax Structure Is Mandatory

All models confirm that receiving USDC creates **two independent tax layers**:

- **PIT-28 (ryczałt 12%)**: Business revenue from the service, recognized the same way as EUR
- **PIT-38 (19% capital gains)**: Triggered later when USDC is disposed of (sold for fiat, used to pay for goods/services)

This is "double reporting" but **not double taxation**, because the cost basis mechanism neutralizes the PIT-38 layer when values don't move.

### 2. Cost Basis = Receivable Value

The PLN value recognized as ryczałt revenue **becomes the PIT-38 acquisition cost**. All models cite KIS interpretation **0114-KDIP3-1.4011.51.2025.1.AK** as the key ruling. This means:

- Immediate USDC→EUR conversion → PIT-38 gain ≈ 0 (only spread/fees)
- Holding USDC → USD/PLN FX movement becomes the PIT-38 gain/loss

### 3. No Różnice Kursowe for Crypto

USDC is **not a foreign currency** (waluta obca) under Polish law — it's a virtual currency (waluta wirtualna). Therefore **Art. 24c FX differences do not apply** to crypto settlements. All models cite KIS interpretation **0115-KDIT1.4011.25.2024.1.MR**.

This is actually a **simplification for ryczałt**: the ryczałt base is locked at the revenue date NBP rate. No invoice-to-payment FX reconciliation needed. Under EUR (Option A), negative FX differences are a **non-deductible sunk cost** on ryczałt, making this structurally asymmetric and punitive.

### 4. Invoice Should Be Denominated in USD/EUR, Not USDC

All models agree: invoice in **fiat currency** with a clause allowing USDC settlement is far cleaner than invoicing directly in USDC units. Fiat denomination:
- Anchors the ryczałt base to NBP foreign-currency conversion (simple, unambiguous)
- Avoids the need for crypto market-price valuation methodology
- Reduces audit risk

Recommended wording: *"Payable in USD; settlement may be made in USDC at market equivalent"*

### 5. Crypto-to-Crypto Swaps Are Non-Taxable

USDC → ETH (or any other crypto) is **not a disposal event** for PIT-38. The cost basis carries over. This enables:
- Tax-deferred portfolio building from business income
- Only the final fiat exit triggers PIT-38

### 6. No VASP Registration Required

Accepting USDC as payment for your own software services does **not** trigger the VASP/AML registry requirement. The registry applies only to entities providing exchange/custody/brokerage services to third parties.

### 7. Bank Withdrawal Is Not a Tax Event

The USDC→EUR exchange on Binance/Kraken is the taxable disposal. The subsequent EUR transfer from exchange to business bank is just fiat movement — no additional tax event.

### 8. The 319K PLN Cost Pool Is Highly Relevant

The existing cost carry-forward shields all foreseeable PIT-38 exposure from USDC disposals. Under Art. 22 ust. 16, crypto costs carry forward **indefinitely** with no percentage caps.

### 9. PIT-38 Must Be Filed Even in Zero-Gain Years

If USDC is acquired in a year, PIT-38 costs must be declared to preserve the carry-forward chain. Missing a filing risks losing carry-forward rights.

---

## Disagreements and Differences

### Revenue Recognition Date

| Model | Position |
|---|---|
| ChatGPT 5.4 Pro | Revenue date follows Art. 14 ust. 1e — typically **last day of billing period**. NOT the USDC receipt date. |
| ChatGPT Deep Research | Same — **service completion / end of billing period**, not the crypto receipt timestamp. |
| Perplexity | Revenue date is whichever occurs **first**: service completion, invoice issuance, or payment receipt (Art. 14(1c)). |
| Gemini | Revenue is recognized at the **moment USDC arrives in the wallet** — the moment the taxpayer gains "uninhibited disposition" over the crypto. |

> **Assessment**: ChatGPT 5.4 Pro and Deep Research align on the standard business-revenue rule (billing period). Perplexity uses the "whichever is first" formulation. Gemini uniquely argues the revenue date is the crypto receipt date, which contradicts the other 3 and the KIS interpretation that payment medium does not change the business income date. **The majority view (billing period / service completion) is more defensible.**

### VAT Exemption Threshold for 2026

| Model | Position |
|---|---|
| ChatGPT 5.4 Pro | **240,000 PLN** (explicitly corrects the user's 200K figure) |
| ChatGPT Deep Research | **240,000 PLN** |
| Perplexity | **200,000 PLN** (uses the old figure) |
| Gemini | **200,000 PLN** (uses the old figure) |

> **Assessment**: The threshold increased to 240,000 PLN from 1 Jan 2026. ChatGPT models provide the updated figure.

### VAT Risk from Crypto Sales

| Model | Position |
|---|---|
| ChatGPT 5.4 Pro | Does not raise the VAT limit aggregation issue. |
| ChatGPT Deep Research | Does not raise it. |
| Perplexity | Does not raise it — states B2B services to foreign clients are outside Polish VAT regardless. |
| Gemini | **Raises a significant warning**: crypto→fiat sales are VAT-exempt financial services under Art. 43(1)(7), but their value **may count toward the VAT exemption threshold** under Art. 113(2)(2). Cites KIS ruling 0112-KDIL1-3.4012.298.2024.2.MR showing "ancillary transaction" exception can protect against this, but warns it's subjective and audit-risky. |

> **Assessment**: Gemini uniquely raises a non-trivial VAT risk that others miss entirely. Even if B2B services go to a foreign client, the domestic VAT exemption threshold calculation could be affected by crypto sales. This deserves further investigation, though the "ancillary transaction" exception should apply in our case.

### Overall Recommendation

| Model | Recommended Option | Reasoning |
|---|---|---|
| ChatGPT 5.4 Pro | **EUR (Option A)** | Lowest compliance burden. USDC workable but not inherently better. Cost pool is a buffer, not a reason to switch. |
| ChatGPT Deep Research | **EUR (Option A)** | Structurally simpler. USDC can work if you want on-chain optionality. |
| Perplexity | **Neutral / slight USDC edge** | With 319K cost pool, USDC is "tax-neutral or even marginally advantageous." Depends on whether you prioritize simplicity or flexibility. |
| Gemini | **USDC (Option B)** | "Profoundly superior architecture for wealth accumulation and tax optimization." The 319K pool is the "definitive economic variable." Strongly advocates switching. |

> **Assessment**: The models split 2-1-1. ChatGPT models are conservative (EUR default), Perplexity is balanced, Gemini is aggressively pro-USDC. The truth likely sits in between — **USDC is workable and not disadvantageous given the cost pool, but adds significant compliance overhead**.

---

## Unique Insights Per Model

### ChatGPT 5.4 Pro
- Identified 3 specific KIS interpretation sygnaturas with keywords confirming ryczałt + crypto coverage
- Warned that spending USDC directly on goods/services is a PIT-38 disposal — "especially clumsy on ryczałt" where business costs don't reduce the tax base
- Recommended getting own KIS interpretation before scaling

### ChatGPT Deep Research
- Most thorough on the FX-differences distinction — explained that ryczałt explicitly imports Art. 24c via Art. 6(1c), and negative differences reduce revenue
- Provided formal "tax burden formula": Option B total ≈ 0.12 × R_PLN + 0.19 × max(0, D_PLN − C_PLN)
- Noted that Art. 23(1)(38d) restricts deductibility of crypto-to-crypto swap expenses

### Perplexity
- Most comprehensive table of KIS interpretations (8 sygnaturas with dates and topics)
- Cited a **March 2026 KIS confirmation** that USDC/USDT remain "waluta wirtualna" despite MiCA's e-money token classification
- Noted that crypto exchanges only retain data 1–3 years, requiring proactive archiving
- Flagged that DeFi yield/staking rewards may create separate PIT-38 income at receipt

### Gemini
- Only model to discuss **datio in solutum** (Art. 453 Civil Code) vs pure barter (Art. 603) distinction
- Only model to raise the **VAT threshold aggregation risk** with detailed analysis of "ancillary transaction" exception
- Required a **dowód wewnętrzny** (internal accounting document) for each USDC receipt — most specific on documentation
- Most detailed on the **asymmetric ryczałt FX problem**: positive FX differences are taxed at 12%, negative ones are non-deductible sunk costs — USDC eliminates this asymmetry entirely

---

## Actions Relevant to Us

### Immediate (if switching to USDC)

1. **Amend the client contract/invoice** to read "payable in USD, settlement accepted in USDC at market rate" with a defined rate source and timestamp
2. **Use a dedicated business wallet** — separate from personal crypto holdings
3. **Set up a PIT-38 acquisition log** tracking: USDC quantity, receipt date, PLN cost basis (= ryczałt value), source invoice number, blockchain tx hash

### Before Scaling

4. **Request interpretacja indywidualna** (40 PLN, ~3 months) covering:
   - PLN valuation method for fiat-denominated invoice settled in USDC
   - Confirmation that the satisfied receivable is the Art. 22 ust. 14 acquisition cost for PIT-38
   - Whether USDC sales count toward the VAT exemption threshold (the Gemini VAT risk)

### Ongoing Compliance

5. **File PIT-38 every year** — even in zero-gain years, to preserve cost carry-forward chain
6. **Archive exchange data proactively** — platforms retain data only 1–3 years
7. **Keep crypto→fiat conversions clean and infrequent** — avoid anything that looks like trading activity (protects "ancillary transaction" VAT classification)
8. **Prepare AML documentation package** for the bank: contract → invoice → blockchain receipt → exchange conversion → EUR SEPA transfer

### Decision: EUR vs USDC?

For **our specific situation** (large cost pool, crypto-native, already tracking PIT-38):

- The **tax burden is identical** between EUR and USDC in practice
- USDC **eliminates the asymmetric ryczałt FX problem** (where negative FX differences are non-deductible)
- USDC gives **optionality**: can route into other crypto tax-free, defer PIT-38 indefinitely
- The 319K PLN cost pool absorbs years of potential PIT-38 exposure
- **But**: adds PIT-38 filing complexity, documentation requirements, and banking friction

**Bottom line**: If we have a non-tax reason to want USDC (on-chain treasury, DeFi optionality, faster settlement), the compliance overhead is manageable and the tax outcome is neutral-to-slightly-better. If we don't care about those benefits, EUR is simpler. Either way, get the KIS interpretation first.
