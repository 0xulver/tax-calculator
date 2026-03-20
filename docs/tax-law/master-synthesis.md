# Master Synthesis: Polish Tax Research — All 14 Topics

**Date**: March 2026
**Sources**: 54 research documents across 14 topics from ChatGPT 5.4 Pro, ChatGPT Deep Research, Perplexity, and Gemini 3.1 Deep Research

---

## The Big Picture

You are a Swedish national who moved to Poland ~2023, works as a software engineer paid in USDC (and now EUR via JDG), and has been actively investing in crypto since 2020. Your tax situation spans three jurisdictions (Sweden pre-2023, US company as payer, Poland as current residence) and involves salary income, crypto trading, DeFi, staking, platform collapses, and a pending JDG ryczalt business.

**The good news**: Under the correct Polish cost pool method, you owe **0 PLN in crypto tax** for every year (2020-2025). Your salary USDC costs and pre-residency acquisition costs create a massive cost shield that exceeds all disposal revenue. The carry-forward into 2026 is ~319K PLN.

**The urgent items**: Missing 2024 PIT-38, corrections to 2023/2024 PIT-37->PIT-36, and filing 2025 PIT-38 + PIT-28 + PIT-36 by April 30, 2026.

---

## Settled Law (All Sources Agree — Zero Disagreements)

### How crypto is taxed
- **19% flat tax** on "odplatne zbycie walut wirtualnych" (Art. 30b ust. 1a)
- Taxable = crypto -> fiat, goods, services, property rights, or settling liabilities
- **NOT taxable** = crypto-to-crypto swaps, wallet transfers, holding
- Reported on **PIT-38 Section E** — completely ring-fenced from all other income
- Annual **cost pooling** (not FIFO) — sum all revenues vs sum all costs per year
- Excess costs carry forward **indefinitely** (no time limit, no annual cap)
- Must file PIT-38 even with zero revenue (to preserve carry-forward chain)
- No "loss" in the traditional sense — only "nadwyzka kosztow" (cost surplus)

### NBP exchange rates
- Revenue: NBP mid-rate from **last business day BEFORE** revenue date (Art. 11a ust. 1)
- Costs: NBP mid-rate from **last business day BEFORE** cost date (Art. 11a ust. 2)
- Weekend trades use Friday's rate

### Stablecoins
- USDC and USDT are "waluta wirtualna" under current Polish law and KIS practice
- USDC has a theoretical post-MiCA risk (EMT/e-money classification) but KIS continues treating it as crypto
- Stablecoin-to-stablecoin swaps are non-taxable
- Stablecoin-to-fiat IS the taxable event

### USDC salary (barter doctrine)
- Receiving USDC for services = income taxed at receipt (PIT-36, progressive rates)
- That PLN value becomes the cost basis for later PIT-38 disposal
- Makes USDC->EUR conversion nearly tax-neutral (only FX movement)
- Confirmed by multiple KIS interpretations (2024-2025)

### Pre-residency costs (Sweden -> Poland)
- Original fiat-to-crypto purchases from 2020-2022 ARE deductible in Poland
- Use **original purchase price** (no market-value step-up at move date)
- Convert to PLN at NBP rate from day before **original** purchase date
- Condition: costs NOT already deducted in Swedish K4
- WSA Warsaw III SA/Wa 1290/24 (Aug 2024) confirms this

### Sweden transition
- Polish residency starts from actual move date (prospective, not Jan 1)
- Pre-move gains = Sweden only. Post-move gains = Poland only.
- Swedish realized losses do NOT transfer to Poland
- Sweden's 10-year rule doesn't reach native crypto (only Swedish shares)
- DTT Art. 13(4): crypto gains taxed exclusively in country of residence at time of sale

### Platform collapses (Celsius, BlockFi)
- Bankruptcy is NOT a taxable event — no "odplatne zbycie" occurred
- No "loss deduction" available for platform failures
- Original acquisition costs remain in the cost pool
- Do NOT book a fictitious "sale at 0"
- Crypto distributions = non-taxable at receipt; fiat/equity distributions = taxable

### Loss carry-forward
- Art. 9 ust. 3 (standard 5-year/50% cap) does NOT apply to crypto
- Art. 22 ust. 16 applies instead: unlimited time, no annual cap, full amount each year
- Must file PIT-38 each year to maintain the carry-forward chain

### JDG and crypto
- JDG trading own crypto = PIT-38 (capital gains), NOT business income
- Crypto and ryczalt are completely separate — no cross-offsetting
- 50% of health insurance deductible from ryczalt revenue

### JDG stablecoin payments (Topic 13)
- Receiving USDC as B2B payment creates **two tax layers**: PIT-28 ryczalt (12%) + PIT-38 (19% at disposal)
- Double reporting, NOT double taxation — cost basis = receivable value recognized as revenue
- Invoice in fiat (USD/EUR) with USDC settlement clause is strongly recommended
- No różnice kursowe for crypto — USDC eliminates the asymmetric ryczalt FX problem (positive FX taxed, negative FX non-deductible)
- Crypto-to-crypto swaps from received USDC remain tax-neutral
- No VASP registration required for receiving USDC as payment
- The 319K PLN cost pool shields all foreseeable PIT-38 exposure from USDC disposals
- Confirmed by KIS 0114-KDIP3-1.4011.51.2025.1.AK

### Automated bot trading (Topic 14)
- Liquidation/arbitrage bots on own account = **PIT-38 (19%)**, not business income
- Art. 17 ust. 1g overrides business definition — volume and automation are irrelevant
- AML Art. 2 ust. 1 pkt 12 exception requires providing services to **third parties** — own-account trading doesn't qualify
- JDG ryczalt 12% completely unaffected — the two income streams never interact
- No ZUS on PIT-38 capital gains
- No VASP registration for own-account algorithmic trading regardless of volume
- Gas fees on crypto-to-crypto are non-deductible (Art. 23 ust. 1 pkt 38d)
- Server hosting, flash loan fees, bot development time: all non-deductible under PIT-38
- Server location (Germany/Japan) doesn't create PE for private capital gains
- Smart contract "location" on blockchain is legally irrelevant for tax jurisdiction
- Confirmed by KIS 0115-KDIT1.4011.582.2025.1.MR and 0112-KDIL2-2.4011.234.2025.3.AA

### DAC8 (coming fast)
- Signed into Polish law March 9, 2026
- Exchanges begin collecting data January 1, 2026
- First data to KAS: June 2027
- Up to 75% punitive tax on audit-discovered unreported crypto
- File past returns BEFORE the data flows

---

## Active Disputes (Sources Disagree or Law Is Unsettled)

### 1. Staking/airdrop taxation timing
- **KIS**: Tax at receipt (PIT-36, 12%/32%). Receipt value = later cost basis.
- **Courts (WSA)**: Tax only at disposal (PIT-38, 19%). Cost basis = 0.
- Pending legislation would codify disposal-only approach
- **Impact for you**: Minimal — cost pool absorbs everything regardless

### 2. FIFO vs cost pool
- **3 of 4 sources**: Poland does NOT use FIFO; annual cost pooling is the statutory method
- **Gemini**: Claims FIFO is strictly mandated via Art. 30b(7a)
- **Practical impact**: Both produce the same PIT-38 annual totals. FIFO only matters for per-transaction detail.

### 3. DeFi LP/vault tokens
- Likely NOT "waluta wirtualna" — more like claims/rights
- Depositing crypto into AMM/vault could be a taxable disposal
- Biggest unresolved DeFi risk area — no KIS guidance
- **Relevant for your Ironclad Finance loss** (ETH -> ic-ETH conversion)

### 4. ZUS obligations for pre-JDG USDC income
- All sources flag this as a real issue but disagree on magnitude
- Perplexity estimates ~180-190K PLN for 2024 alone (worst case)
- Depends on umowa zlecenie vs business activity classification
- US-Poland Totalization Agreement may provide protection
- **Needs specialist consultation — too fact-dependent for desk research**

### 5. PIT/ZG with PIT-38
- Perplexity/Gemini: mandatory for foreign exchanges
- ChatGPT sources: only when foreign tax methods apply
- Safe approach: include it (harmless if no foreign tax paid)

### 6. Liquidation bonus classification (Topic 14)
- **Gemini**: Not taxable at receipt. Autonomous protocol has no legal personhood for service contract. Zero cost basis. Tax only at fiat exit.
- **ChatGPT models**: Defensible as crypto-to-crypto exchange mechanism, but KIS staking/airdrop rulings create receipt-time risk.
- **Perplexity**: KIS will likely tax as progressive income at receipt (12%/32%), creating dual taxation risk.
- **All agree**: #1 priority for individual KIS interpretation (interpretacja indywidualna)

### 7. Gas fees as taxable disposal (Topic 14)
- **ChatGPT 5.4 Pro uniquely flags**: paying gas in ETH = using crypto to settle an obligation = potentially a separate taxable disposal for each gas payment
- This would make gas simultaneously non-deductible AND a micro-taxable event across 365K+ trades/year
- Other 3 models treat gas purely as a non-deductible cost without raising the disposal angle
- No KIS ruling exists on this point

### 8. Revenue recognition date for USDC payments (Topic 13)
- **ChatGPT models**: Service completion / end of billing period (standard Art. 14 rule)
- **Perplexity**: Whichever is first: service completion, invoice, or payment (Art. 14(1c))
- **Gemini**: USDC arrival in wallet (when taxpayer gains "uninhibited disposition")
- Majority view (billing period) is more defensible

### 9. VAT threshold risk from crypto sales (Topic 13)
- **Only Gemini raises**: crypto→fiat sales are VAT-exempt financial services, but their value may count toward VAT exemption threshold under Art. 113(2)(2)
- "Ancillary transaction" exception likely applies but is subjective and audit-risky
- Other 3 models do not flag this risk

---

## Your Tax Filings: What's Needed

### Already filed (by tax company)
| Year | Form | Status | Issues |
|---|---|---|---|
| 2023 | PIT-37 | Filed late (June 2024) with czynny zal | Wrong form (should be PIT-36) |
| 2023 | PIT-38 | Filed late (June 2024) with czynny zal | Only salary USDC conversions reported |
| 2024 | PIT-37 | Filed | Wrong form, no advance payments, no PIT/ZG |

### Missing (needs filing)
| Year | Form | Priority | Notes |
|---|---|---|---|
| **2024** | **PIT-38** | **CRITICAL** | Protects ~701K PLN cost carry-forward chain |
| 2025 | PIT-38 | Due Apr 30 | 15 fiat-exit events, 0 tax (costs >> revenue) |
| 2025 | PIT-28 | Due Apr 30 | JDG ryczalt income (must be actively filed) |
| 2025 | PIT-36 | Due Apr 30 | Pre-JDG USDC salary income (Jan-Apr) |

### Lower priority corrections
| Year | Form | Priority | Notes |
|---|---|---|---|
| 2023 | PIT-37 -> PIT-36 korekta | Medium | Wrong form, add PIT/ZG |
| 2024 | PIT-37 -> PIT-36 korekta | Medium | Wrong form, add PIT/ZG |

---

## Financial Summary

### Tax owed: likely 0 PLN across all years

| Year | Revenue | Costs (current + prior) | Income | Tax | Carry Forward |
|---|---|---|---|---|---|
| 2020 | 3,640 | 271,378 | 0 | 0 | 267,738 |
| 2021 | 265,133 | 797,855 | 0 | 0 | 532,722 |
| 2022 | 437,946 | 668,811 | 0 | 0 | 230,865 |
| 2023 | 411,144 | 539,917 | 0 | 0 | 128,773 |
| 2024 | 785,509 | 906,955 | 0 | 0 | 121,446 |
| 2025 | 271,317 | 589,925 | 0 | 0 | 318,608 |

The salary USDC creates massive annual costs that exceed all disposal revenue. The ~319K PLN carry-forward shields future gains indefinitely.

### Potential additional liabilities
| Item | Estimated | Status |
|---|---|---|
| Late advance payments (zaliczki) interest 2023-2024 | ~6-12K PLN | Already accrued, payable regardless |
| ZUS for pre-JDG income | 0 to 190K PLN | Unknown — needs specialist |
| Additional crypto tax | 0 PLN | Cost pool absorbs everything |

---

## Action Plan (Prioritized)

### THIS WEEK
1. **Check e-Urzad Skarbowy** for auto-accepted PIT-38s (2023, 2024)
2. **File 2024 PIT-38** (korekta or first filing) + czynny zal — protects cost chain
3. **Calculate and pay interest** on late advance payments for 2023-2024

### BEFORE APRIL 30, 2026
4. **File 2025 PIT-38** — 15 disposal events, 0 tax, cost carry-forward
5. **File 2025 PIT-28** — JDG ryczalt (must be actively filed, NOT auto-accepted)
6. **File 2025 PIT-36** — pre-JDG USDC salary income (Jan-Apr 2025)
7. **Calculate pre-residency costs** from Swedish-period fiat->crypto purchases (2020-2022)

### AFTER APRIL 30 (lower priority)
8. **Correct 2023 PIT-37 -> PIT-36** + PIT/ZG
9. **Correct 2024 PIT-37 -> PIT-36** + PIT/ZG
10. **Consult ZUS specialist** for pre-JDG USDC income obligations
11. **Consider interpretacja indywidualna** (40 PLN) for USDC salary classification
12. **Sell worthless LUNA/UST dust** to crystallize indefinite cost carry-forward
13. **Request KIS interpretation for bot trading** covering: liquidation bonus classification, gas fee as taxable disposal, flash loan fee treatment
14. **If switching to USDC payments**: amend contract to "payable in USD, settlement accepted in USDC", set up dedicated business wallet, establish PIT-38 acquisition log

### DOCUMENTATION TO PREPARE
- Binance/Kraken CSV exports for all years
- Swedish K4 returns (to verify no double-counting of costs)
- Salary payment records (USDC receipts with dates and amounts)
- Bank statements showing fiat->crypto purchases
- Wallet tx hashes for Celsius/BlockFi/Ironclad deposits
- NBP rate records for each transaction
- Czynny zal letter (Polish template in synthesis 06)

---

## Key Legal References

| Topic | Primary Law | Key Articles |
|---|---|---|
| Crypto disposal | PIT Act | Art. 17 ust. 1 pkt 11, Art. 17 ust. 1f |
| 19% rate | PIT Act | Art. 30b ust. 1a |
| Cost basis | PIT Act | Art. 22 ust. 14-16 |
| Cost carry-forward | PIT Act | Art. 22 ust. 16 |
| No loss for crypto | PIT Act | Art. 9 ust. 3a pkt 2 |
| Ring-fencing | PIT Act | Art. 30b ust. 5d |
| NBP rate | PIT Act | Art. 11a ust. 1-2 |
| Waluta wirtualna def. | AML Act | Art. 2 ust. 2 pkt 26 |
| Annual filing | PIT Act | Art. 30b ust. 6, 6a |
| Czynny zal | KKS | Art. 16 |
| Correction | Ordynacja | Art. 81 |
| Statute of limitations | Ordynacja | Art. 70 §1 |
| Pre-residency costs | WSA ruling | III SA/Wa 1290/24 (Aug 2024) |
| Crypto stays PIT-38 in business | PIT Act | Art. 17 ust. 1g |
| AML crypto service exception | AML Act | Art. 2 ust. 1 pkt 12 |
| Crypto-to-crypto cost exclusion | PIT Act | Art. 23 ust. 1 pkt 38d |
| Barter / datio in solutum | Civil Code | Art. 453, Art. 603 |
| VAT ancillary transaction | VAT Act | Art. 113 ust. 2 pkt 2 |
| No FX differences for crypto | PIT Act | Art. 24c (inapplicable) |
| USDC as business payment | KIS ruling | 0114-KDIP3-1.4011.51.2025.1.AK |
| No FX for crypto | KIS ruling | 0115-KDIT1.4011.25.2024.1.MR |
| Bot trading stays PIT-38 | KIS ruling | 0115-KDIT1.4011.582.2025.1.MR |
| Volume irrelevant for classification | KIS ruling | 0112-KDIL2-2.4011.234.2025.3.AA |

---

## Summary of All 14 Syntheses

| # | Topic | Key Finding | Disagreements |
|---|---|---|---|
| 01 | JDG ryczalt | 12% on gross revenue, no costs, PIT-28 by Apr 30 | JPK_V7 for VAT-exempt (Gemini says yes, others no) |
| 02 | USDC salary | Barter doctrine: income at receipt + cost basis for PIT-38 | ZUS liability (0 to 190K PLN depending on facts) |
| 03 | PIT-38 crypto | Annual cost pooling, NOT FIFO. 19% on disposal only. | FIFO question (statutory text vs MF guidance) |
| 04 | Stablecoins | USDC/USDT = waluta wirtualna. Post-MiCA risk for USDC low. | Cost basis for salary USDC (one source flags "wydatki" risk) |
| 05 | Loss carry-forward | Art. 22 ust. 16: no time limit, no cap. Not Art. 9 ust. 3. | None — unanimous |
| 06 | Late filing | Czynny zal + late PIT-38 + pay immediately. All electronic. | Whether actual tax is owed (0 under cost pool) |
| 07 | Filing checklist | 2025 = 3 forms (PIT-38 + PIT-28 + PIT-36). DAC8 coming. | PIT/ZG requirement, health insurance deductibility |
| 08 | Cost basis/valuation | NBP rate from day before. Narrow cost deductibility. | FIFO question (same as 03) |
| 09 | Sweden->Poland | Split-year residency. No step-up. Pre-residency costs usable. | DTT relief method (exemption vs credit) |
| 10 | General framework | 2019 regime still in force. DAC8 = biggest change. | None substantive |
| 11 | Platform losses | No loss deduction. Costs stay in pool. Don't book fake sale. | Deposit = disposal? (for Celsius Earn type products) |
| 12 | DeFi/staking/airdrops | KIS vs courts actively fighting. LP tokens = biggest risk. | Staking timing (receipt vs disposal) — the core dispute |
| 13 | JDG stablecoin payments | Dual PIT-28+PIT-38 layers. Cost basis = receivable. No FX risk. 319K pool shields all. | Revenue date (4-way split), VAT threshold risk (only Gemini), recommendation split (EUR vs USDC) |
| 14 | Bot trading | PIT-38 at 19% regardless of volume/automation. Crypto-to-crypto neutral. Massive cost trap. | Liquidation bonus (3-way split), gas as taxable disposal (ChatGPT Pro only), server PE risk level |
