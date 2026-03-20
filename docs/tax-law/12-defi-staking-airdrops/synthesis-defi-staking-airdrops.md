# Synthesis: DeFi, Staking, and Airdrops Taxation in Poland

Sources: ChatGPT 5.4 Pro, ChatGPT Deep Research, Perplexity (3 sources; Gemini not available)

---

## The Central Conflict: KIS vs Courts

This is the most disputed area in Polish crypto tax. All 3 sources agree that there are **two legitimate, mutually exclusive approaches** — and neither is definitively settled:

### Track A: KIS (tax authority) — Tax at receipt
- Staking rewards, airdrops, and earn/lending rewards are **taxable upon receipt**
- Classified as "przychod z praw majatkowych" (property rights income, Art. 18)
- Valued at market price on receipt date
- Reported on **PIT-36** at progressive rates (12%/32%)
- The receipt value becomes the **cost basis** for later PIT-38 disposal
- Confirmed in KIS interpretations: 0112-KDIL2-2.4011.146.2024.2.IM (Apr 2024), 0112-KDIL2-2.4011.234.2025.3.AA (Jun 2025), 0115-KDIT1.4011.558.2025.2.MK (Oct 2025)

### Track B: Courts (WSA) — Tax only at disposal
- Receipt of rewards is NOT a taxable event
- Tax arises only when tokens are sold for fiat (odplatne zbycie)
- Reported on **PIT-38** at 19% flat rate
- Cost basis = **0 PLN** (no "wydatki" = no acquisition expenditure)
- Confirmed by WSA Wroclaw I SA/Wr 413/23 (Dec 2023), WSA Poznan I SA/Po 434/24 (Dec 2024), WSA Wroclaw I SA/Wr 559/25 (Dec 2025)

### Key insight from ChatGPT 5.4 Pro
ChatGPT 5.4 Pro adds important 2025 court developments: WSA Wroclaw's December 2025 ruling went further than prior courts, stating that "virtual currencies cannot be equated with property rights to the extent assumed by KIS." This strengthens the disposal-only position.

### Pending legislation
ChatGPT 5.4 Pro also notes a pending Sejm crypto-assets bill that would **codify the disposal-only approach** for staking — saying receipt of virtual currency from staking does NOT create revenue. This hasn't passed yet but signals legislative intent.

---

## Consensus Across All 3 Sources

### Crypto-to-crypto swaps remain non-taxable
All agree: DeFi swaps (token A -> token B), wrapping (ETH -> wBTC), stablecoin conversions (BUSD -> USDC) are tax-neutral if both sides are waluta wirtualna. Fees on these swaps are NOT deductible (Art. 23 ust. 1 pkt 38d).

### Each staking reward = separate lot
Under either approach, each reward receipt creates a new lot with its own date, quantity, and cost basis (either FMV at receipt under KIS, or 0 under court approach). For DOT weekly staking on Kraken, that's ~52 lots per year.

### No de minimis threshold
There is NO materiality exemption for small staking rewards. Every micro-reward must in principle be tracked and valued. The practical relief: PIT-38 requires only **annual aggregates**, not per-transaction filing.

### Earn/lending programs = same as staking
Binance Simple Earn, Kraken Earn treated identically to staking under both approaches.

### Crowdloans (Kusama/Polkadot)
- **Locking KSM**: NOT a disposal (no exchange for fiat/goods/rights). Non-taxable.
- **KSM returned after lease**: Non-taxable. Original cost basis preserved.
- **Project tokens received**: Treated like airdrops — disputed (KIS: tax at receipt; courts: tax at disposal).

### Token swaps/migrations (LUNA -> LUNA2, BUSD -> FDUSD -> USDC)
- BUSD -> FDUSD -> USDC: **Definitively non-taxable** (confirmed by KIS). Cost basis carries through.
- LUNA -> LUNA2: If treated as a migration/replacement — non-taxable continuation, cost carries through. If treated as an airdrop — disputed (KIS vs courts).

### Terra/Anchor collapse
- Price going to zero is NOT a taxable event — no disposal occurred
- Original acquisition costs remain in the cost pool
- **Pro tip from Perplexity**: Consider selling worthless LUNA/UST dust for minimal proceeds to formally crystallize the excess cost carry-forward in PIT-38. The carry-forward is indefinite within the crypto bucket.

### Liquid staking tokens (stETH, cbETH, DOT.S)
- ETH -> stETH conversion: **Non-taxable** crypto-to-crypto swap (if stETH qualifies as waluta wirtualna — KIS confirmed cbETH does in Oct 2024)
- Ongoing rebase rewards (stETH balance increases): Disputed, same as staking
- DOT.S: No direct KIS interpretation found

### DeFi LP tokens — highest risk
All sources flag LP tokens as the biggest classification risk:
- If LP token = waluta wirtualna → depositing crypto to AMM is non-taxable swap
- If LP token = property right (claim/receipt) → depositing crypto IS a taxable disposal
- KIS tends to classify LP tokens as claims/rights, NOT waluta wirtualna
- This makes depositing crypto into Uniswap/Aave potentially taxable — the single riskiest DeFi action

### Smart contract exploits / rug pulls
- NOT a taxable event (no disposal occurred)
- No loss deduction available (2025 KIS theft interpretation)
- Original acquisition costs remain in the pool
- Same treatment as Celsius/BlockFi from synthesis 11

---

## Minor Disagreement: KIS Earn/Lending Interpretation

ChatGPT 5.4 Pro provides a unique KIS interpretation from December 2025 (0115-KDIT1.4011.847.2025.1.MR) that distinguishes between:
- **Fiat savings account paying crypto reward** → treated as "interest" (Art. 17 ust. 1 pkt 2)
- **Crypto deposit paying crypto reward** → treated as "property rights income" (Art. 18)

The other sources don't cite this distinction. It's relevant for Kraken Earn / Binance Simple Earn where the deposit is in crypto (second category).

---

## What This Means for Your Situation

### Your staking activities (DOT, ETH, SOL on Kraken)
These are modest amounts relative to your salary USDC income. Under either approach:
- **KIS approach**: Each weekly reward taxed at receipt on PIT-36 (12%/32%). Receipt value becomes cost basis for later PIT-38. Higher compliance burden but provides cost basis.
- **Court approach**: Ignore until sold. Zero cost basis. Simpler but if audited, KIS may reassess.

**Recommendation**: Given your large cost pool carry-forward (costs >> revenue every year), the choice between approaches has minimal practical tax impact. The cost pool absorbs everything regardless. Choose one approach consistently and document your reasoning.

### Your airdrops (Binance)
Same analysis. Small amounts, absorbed by cost pool. Keep records of receipt dates and values regardless of which approach you choose.

### The Ironclad Finance DeFi loss
As analyzed separately: the ETH -> ic-ETH conversion is the riskiest transaction (LP/vault token classification). The hack itself is non-taxable. Original costs remain in the pool.

### LUNA/UST
If you still hold LUNA Classic (LUNC) dust, consider selling it for minimal proceeds to crystallize the excess cost. The carry-forward is indefinite.

---

## Action Items

### 1. Pick an approach and stick with it
Choose KIS (receipt-tax) or court (disposal-only) for ALL staking/airdrop/earn rewards. Don't cherry-pick between them for different assets — all sources warn that inconsistent treatment across similar rewards is the highest audit risk.

### 2. For conservative (KIS) approach
- Export Kraken staking reward history (dates, amounts)
- Value each receipt in PLN using market price + NBP rate
- Report total on PIT-36 as property rights income
- Use the same values as cost basis when tokens are sold on PIT-38

### 3. For taxpayer-friendly (court) approach
- Track reward receipts for documentation only
- Report nothing until disposal
- At disposal, cost basis = 0 for reward tokens (full proceeds taxable, but absorbed by cost pool)
- Document your legal basis (cite WSA Wroclaw 2023, WSA Poznan 2024 rulings)

### 4. Consider interpretacja indywidualna (40 PLN)
For your highest-value staking position (DOT), a binding KIS interpretation provides legal protection against reassessment regardless of which approach you choose. Takes ~3 months.

### 5. Sell worthless LUNA/UST dust
If holding, sell for any amount to crystallize excess costs in PIT-38. The indefinite carry-forward makes this free future tax protection.
