# Synthesis: Tax Residency Transition from Sweden to Poland

Sources: ChatGPT 5.4 Pro, Perplexity, Gemini 3.1 Deep Research (3 sources; ChatGPT Deep Research not available)

---

## Full Consensus (All 3 agree)

### Polish residency begins prospectively, not retroactively
If you moved in March 2023, Polish tax residency starts from the actual date your centre of vital interests transferred — NOT from January 1, 2023. MF official guidance and KIS interpretations explicitly confirm split-year residency (podzial roku podatkowego). Pre-move income belongs to Sweden; post-move income belongs to Poland.

### Two-test residency determination (Art. 3 ust. 1a PIT)
Either test is sufficient:
1. **Centre of vital interests** (centrum interesow zyciowych) — personal OR economic ties
2. **Physical presence** >183 days in the calendar year

All sources note the centre-of-interests test generally takes precedence in practice, with the 183-day rule as a subsidiary fallback.

### DTT tie-breaker for dual residency (Art. 4(2) Poland-Sweden DTT)
Sequential: permanent home -> centre of vital interests -> habitual abode -> nationality -> mutual agreement. For someone who moved family and established life in Poland, this resolves to Poland from the move date.

### Crypto gains fall under DTT Art. 13(4) — "any other property"
The treaty doesn't mention crypto, but Art. 13(4) is the residual provision covering gains from "any property." Crypto sold while Polish resident = taxable **exclusively** in Poland. Crypto sold while Swedish resident = taxable **exclusively** in Sweden.

### No Polish immigration step-up in basis
All 3 unanimously confirm: Poland does NOT reset crypto cost basis to market value on the date you become resident. The cost basis is the **original documented acquisition price**, converted to PLN at the NBP rate from the day before the original purchase date. This is confirmed by WSA Warsaw III SA/Wa 1290/24 and KIS interpretations.

### Pre-residency acquisition costs ARE deductible in Poland
Fiat-to-crypto purchases made while in Sweden (2020-2022) can be included in Polish PIT-38 as deductible costs — IF:
- They were documented (exchange records, bank statements)
- They were NOT already deducted in Swedish K4 returns
- They were fiat-to-crypto purchases (NOT crypto-to-crypto swap costs)

This is the WSA Warsaw 2024 ruling principle, confirmed across all 3 sources.

### Swedish realized losses do NOT transfer to Poland
A realized Swedish crypto loss (declared on K4) stays in Sweden. It cannot become a Polish PIT-38 carry-forward. Swedish crypto loss rules only allow offsetting 70% against same-year Swedish gains — no carry-forward even within Sweden.

### Sweden's 10-year rule likely doesn't reach crypto
The DTT Art. 13(5) gives Sweden a theoretical 10-year window to tax post-departure gains. BUT Sweden's domestic 10-year extended liability rule (Chapter 3, Section 19 Income Tax Act) only covers Swedish shares and comparable securities ("delagarratter"). Skatteverket classifies crypto as "andra tillgangar" (other assets), not equity. So in practice, Sweden cannot enforce the 10-year rule on native crypto (BTC, ETH, etc.).

**Exception**: If you held Swedish exchange-traded crypto products (XBT Provider ETNs traded on Nasdaq Stockholm), those ARE Swedish securities and could trigger the 10-year rule.

### Crypto-to-crypto swap asymmetry between Sweden and Poland
A critical point all sources flag: Sweden taxes crypto-to-crypto swaps (every swap is a taxable event). Poland does NOT. So a swap done before the move is taxable in Sweden; the same swap done after the move is non-taxable in Poland. This creates different cost basis histories depending on when transactions occurred.

### PIT/ZG generally not needed for crypto gains assigned to Poland
If the DTT assigns exclusive taxing rights to Poland (Art. 13(4)), and no Swedish tax was paid on the crypto gain, PIT/ZG is not required for those gains. PIT/ZG is only needed if foreign tax was actually paid and a credit/exemption method must be applied.

### DTT double-taxation elimination: exemption method for capital gains
Art. 22 of the Poland-Sweden DTT uses the **exemption method** (not credit) for capital gains. If Sweden taxes pre-move gains, Poland exempts them (with progression, which is moot at a flat 19%).

---

## Minor Disagreement: The DTT Art. 22 relief method

| Source | Position |
|---|---|
| ChatGPT 5.4 Pro | Art. 22 points to **exemption** for Swedish-taxable capital gains in Poland, not credit. Credit is only for Art. 10 (dividends) and Art. 12 (royalties). |
| Perplexity | Art. 22(1)(a) uses **exemption with progression** for capital gains. |
| Gemini | Claims Poland uses "proportional deduction method (metoda proporcjonalnego odliczenia)" — i.e., **credit method** for capital gains. |

**Assessment**: ChatGPT 5.4 Pro and Perplexity agree on exemption. Gemini claims credit. Looking at the treaty text, Art. 22(1)(a) provides exemption for income that "may be taxed in Sweden" (with certain exclusions for dividends/royalties which get credit instead). For capital gains under Art. 13, exemption appears to be the correct method. Gemini may be conflating the general Polish domestic method with the specific DTT provision. In practice, this distinction doesn't matter much for your case since post-move crypto gains are exclusively Polish and pre-move gains are exclusively Swedish.

---

## What This Means for You

### The 2023 split-year
- **Jan-Mar 2023** (before move): Swedish resident. Any crypto sold for fiat in this period = Swedish tax only. Poland has no claim.
- **Apr-Dec 2023** (after move): Polish resident. All crypto disposals = Polish PIT-38.
- The exact date matters: determine when your centre of vital interests actually shifted (when you moved, registered, opened bank accounts, etc.)

### Pre-Sweden costs are valuable
All fiat-to-crypto purchases from 2020-2022 that were NOT sold in Sweden (costs not consumed in a K4 gain/loss calculation) can enter your Polish cost pool. This could be a substantial amount.

### What to check against Swedish K4 returns
For each pre-Poland crypto purchase:
1. Was the crypto sold while in Sweden? If yes → cost already consumed in Sweden, cannot reuse in Poland
2. Was the crypto still held when you moved? If yes → cost is available for Polish PIT-38
3. Was a loss claimed in Sweden on this crypto? If yes → cost consumed, cannot reuse

### The FX angle matters
Pre-Poland purchases in EUR must be converted to PLN at the NBP rate from the **original purchase date** (not the move date). If EUR was stronger against PLN in 2020-2021 than now, your historical cost basis in PLN is actually higher than it would be at current rates — this works in your favor.

---

## Action Items

### 1. Determine the exact date of Polish residency
Document when your centre of vital interests shifted in 2023. Relevant evidence: lease/rental agreement, PESEL registration, bank account opening, address registration (zameldowanie), flight records.

### 2. Compile pre-Poland purchase records
Extract all fiat->crypto purchases from Binance/Kraken for 2020-2022. For each:
- Date of purchase
- EUR/USD amount spent
- Crypto received
- Was this sold while in Sweden? (check against K4 if filed)

### 3. Check Swedish K4 returns
If you filed Swedish K4 for 2020-2022:
- Which crypto disposals were reported?
- What costs were used in those calculations?
- Any losses claimed?

Costs already used in Swedish K4 calculations CANNOT be reused in Poland. Only costs for crypto that was never sold in Sweden are available.

### 4. Calculate pre-residency costs for the calculator
For each eligible pre-Poland purchase:
- Convert EUR amount to PLN using NBP EUR rate from day before the purchase date
- Sum all eligible costs
- Enter as `--pre-residency-costs` parameter

### 5. Consider an interpretacja indywidualna
The WSA Warsaw 2024 ruling addressed a UK->Poland transition. While the legal reasoning is the same for Sweden->Poland, it hasn't been directly tested. For large pre-residency cost claims, a binding KIS interpretation (40 PLN) provides legal certainty.

### 6. No Swedish exit tax risk for native crypto
Sweden does not impose exit tax on crypto departure. The 10-year rule targets Swedish shares, not crypto. You can safely ignore this for BTC, ETH, USDC, DOT etc. Only relevant if you held Swedish crypto ETNs.
