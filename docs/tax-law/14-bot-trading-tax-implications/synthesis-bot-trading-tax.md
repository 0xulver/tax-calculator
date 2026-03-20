# Synthesis: Tax Implications of Automated Crypto Bot Trading Under Polish JDG

**Sources**: ChatGPT 5.4 Pro, ChatGPT Deep Research, Perplexity, Gemini 3.1 Deep Research
**Topic**: Liquidation bots, DEX arbitrage, MEV — classification, taxation, deductibility, multi-jurisdiction

---

## Key Findings — Full Agreement (4/4 Models)

### 1. Bot Trading Stays in PIT-38 (19% Capital Gains)

All models confirm: despite the organized, continuous, 24/7 nature of automated bot trading, the income remains in **PIT-38 capital gains** — not business income. The mechanism is Art. 17 ust. 1g PIT, which **overrides the business activity definition** for crypto disposals, keeping them in the capital gains bucket regardless of volume or automation.

There is **no transaction-count threshold** that flips PIT-38 into PIT-36. KIS has explicitly confirmed this in recent rulings.

### 2. AML Exception Does Not Apply to Own-Account Bots

The Art. 17 ust. 1g exception (which would reclassify crypto income as business income) only triggers for activities defined in **AML Art. 2 ust. 1 pkt 12** — providing exchange, intermediation, or custody services **to third parties**. A bot trading exclusively with the operator's own capital on permissionless protocols is not providing services to anyone, so the exception does not apply.

All models emphasize: the moment the developer accepts external capital or manages third-party funds, the entire structure collapses into business income with AML registration, ZUS, and potential progressive taxation.

### 3. Crypto-to-Crypto Is Absolutely Tax-Neutral

Under Art. 17 ust. 1f, "odpłatne zbycie" (taxable disposal) is **exhaustively defined** as exchange for legal tender, goods, services, or non-crypto property rights. Swapping one virtual currency for another is explicitly **not** a taxable event. This applies uniformly to:
- DEX arbitrage (ETH→USDC→WBTC→ETH loops)
- Flash loan round-trips
- Cross-chain bridge hops
- Stablecoin parking (ETH→USDC is not a disposal)

Tax **only** arises when crypto is converted to fiat or used to pay for goods/services.

### 4. JDG Ryczałt 12% Is Completely Unaffected

Bot trading income flows to PIT-38 as a separate income source. The software development JDG continues on PIT-28 at 12% ryczałt. There is **no interaction** between the two — adding bot trading does not contaminate, risk, or alter the JDG's tax status.

### 5. Annual Cost Pool Method (Not FIFO)

PIT-38 uses an **annual aggregate cost pool**: total acquisition costs vs. total disposal revenues. Excess costs carry forward **indefinitely**. No per-token, per-lot, or FIFO tracking is required. PIT-38 only needs annual aggregate figures — there is no per-transaction reporting requirement on the form itself.

### 6. Server/Infrastructure Costs Are Not Deductible Under PIT-38

Server hosting (Hetzner, AWS), RPC endpoints, software tools, and development time are **indirect costs** — similar to mining equipment and electricity. All models cite KIS/NSA precedent that mining hardware is non-deductible under PIT-38's "direct acquisition/disposal costs" framework. By analogy, bot infrastructure costs are non-deductible.

### 7. Polish Worldwide Taxation Applies — Server Location Doesn't Move Income

Polish tax residents pay tax on worldwide income under unlimited tax liability (Art. 3 ust. 1 PIT). Running the bot on foreign infrastructure does not shift the tax obligation away from Poland. Smart contract "location" on a blockchain is irrelevant — there is no physical location to create tax nexus.

### 8. No VASP/AML Registration Required for Own-Account Trading

Operating bots for one's own account does not trigger the VASP registry requirement. Registration is required only for entities providing crypto exchange/intermediation/custody services to third parties. Trading volume is irrelevant.

### 9. No ZUS Obligations on PIT-38 Income

Capital gains income from crypto (PIT-38) does **not** form a base for ZUS social security or health insurance contributions. ZUS obligations arise only from the JDG software activity.

### 10. DAC8 Reporting Starting 2026

From January 2026, EU-licensed centralized exchanges will automatically report user transactions to national tax authorities (Polish KAS receives data starting 2027). This makes accurate PIT-38 filing imperative. On-chain DEX activity is not captured by DAC8.

---

## Disagreements and Differences

### Liquidation Bonus Treatment — The Biggest Split

This is the **most contested question** across all 4 models, with a genuine 3-way split:

| Model | Position | Tax Consequence |
|---|---|---|
| ChatGPT 5.4 Pro | Best argument: crypto-to-crypto exchange at favorable rate. **Not a free receipt**. Defensible but not de-risked — KIS has been aggressive on reward-like receipts. | Tax deferred to fiat exit. Zero cost basis in pool. |
| ChatGPT Deep Research | Also favors crypto-to-crypto mechanism. But acknowledges a live controversy: KIS treated airdrops as income at receipt (2025 ruling). | Structurally supports tax deferral but flags receipt-time risk. |
| Perplexity | **Most pessimistic**: KIS will likely classify as income at receipt (Scenario B — progressive rates 12%/32%), analogizing to staking rewards and airdrops. **Dual taxation risk**: taxed at receipt as progressive income AND at disposal as PIT-38 19%. | Income at receipt (PIT-36 progressive) + later PIT-38 at disposal. Cost basis = value at receipt. |
| Gemini | **Most optimistic**: Liquidation is a "unilateral programmatic acquisition" — no service contract because decentralized protocol has no legal personhood. Receipt is **not taxable**. Cost basis is zero. Tax only at fiat exit. | Tax deferred. Zero cost basis. Full 19% on disposal. |

> **Assessment**: This is genuinely unsettled. The core tension is:
> - **Pro-deferral argument**: Liquidation involves consideration (repaying debt → receiving collateral). It's an exchange mechanism, not a gratuitous receipt. No bilateral service contract exists with an autonomous protocol.
> - **Anti-deferral argument**: KIS has consistently taxed "free" crypto receipts (airdrops, staking) at receipt moment. A bonus received without fiat expenditure looks like a reward.
>
> **Recommendation**: All 4 models agree this is the #1 priority for an individual KIS interpretation (interpretacja indywidualna, PLN 40).

### Gas Fees — Disposal vs Non-Deductible vs Taxable Event

All models agree gas on crypto-to-crypto swaps is non-deductible (Art. 23 ust. 1 pkt 38d). But there's a subtle additional layer:

| Model | Position on Gas Being a Taxable Disposal |
|---|---|
| ChatGPT 5.4 Pro | **Uniquely raises**: paying gas (ETH for a service) is itself a **taxable disposal** under the statutory definition. Gas = using crypto to settle an obligation. So gas is simultaneously (a) non-deductible as a cost AND (b) potentially a separate taxable event. "The fee paid in crypto may be a realization event, while still not being an easy PIT-38 cost." |
| ChatGPT Deep Research | Similar concern: "Using virtual currency to pay for a service or settle liabilities is itself a taxable disposal." But doesn't develop the dual-bind as explicitly. |
| Perplexity | **Does not raise** this issue. Treats gas purely as a non-deductible cost. |
| Gemini | **Does not raise** this issue. Treats gas purely as a non-deductible cost. |

> **Assessment**: ChatGPT 5.4 Pro identifies a genuinely alarming logical consequence of the statute. If paying gas is "settling an obligation with crypto," then every single gas payment across 365,000 trades could theoretically be a separate taxable disposal — while also being non-deductible. This creates a nightmare "cost trap" where the effective tax rate far exceeds 19%. No KIS ruling directly addresses this. High uncertainty.

### Flash Loan Treatment

| Model | Position |
|---|---|
| ChatGPT 5.4 Pro | Flash loans should be argued as tax-neutral (borrow + repay in same atomic tx, no durable enrichment). But "repaying a liability in crypto" falls within taxable disposal definition — statutory wording is awkward. Fees are non-deductible. |
| ChatGPT Deep Research | Flash loan fees = financing costs, explicitly excluded by MF guidance. Non-deductible. |
| Perplexity | Flash loans create zero net economic effect. Fees non-deductible under Art. 23 ust. 1 pkt 38d. No KIS interpretation exists. |
| Gemini | Flash loan premiums are "dead capital" — non-deductible sunk costs. Financing exclusion applies. |

> **Assessment**: All agree flash loan fees are non-deductible. The nuance is whether the flash loan repayment itself constitutes a "taxable disposal" (settling a liability with crypto). All note no KIS ruling exists. Low practical risk in atomic transactions but theoretically vulnerable.

### Server PE Risk Assessment

| Model | PE Risk for Dedicated Hetzner Server |
|---|---|
| ChatGPT 5.4 Pro | Low — but rises if activity is recharacterized as business. If stays PIT-38, PE analysis becomes "much less central." |
| ChatGPT Deep Research | Non-zero — "server at disposal" is a recognized OECD pathway. Dedicated server > Cloud. But practical PE risk is usually driven by whether income is "business profits" (Article 7 DTT). |
| Perplexity | **Most aggressive on PE risk**: "MEDIUM" for dedicated Hetzner server. Cites **WSA Gliwice I SA/Gl 175/24** (Nov 2024) where rented servers created PE. But notes that for Polish residents, PE has minimal practical impact (same 19% rate). |
| Gemini | **Lowest risk**: Two defenses — (1) PIT-38 capital gains = no "enterprise" capable of forming PE, (2) rented VPS = no "fixed place of business." Negligible PE risk. |

> **Assessment**: In practice, PE risk is moot because: (a) the activity is PIT-38 not business income, so DTT Article 7 (business profits) doesn't apply; and (b) even if PE existed, the tax rate wouldn't change materially. Use standard VPS/cloud hosting and don't overthink this.

### Cost Basis of Liquidation Bonus

| Model | Cost Basis |
|---|---|
| ChatGPT 5.4 Pro | No new direct acquisition expenditure in cost pool. Later disposal creates revenue; cost side comes from annual global pool. |
| ChatGPT Deep Research | If treated as exchange mechanism: no cost created. If treated as "income at receipt" (airdrop analogy): recognized income value becomes acquisition cost. |
| Perplexity | If Scenario B (income at receipt): cost basis = value at receipt. If Scenario A (favorable exchange): sits in pool at fiat-equivalent at date of receipt. |
| Gemini | **Explicitly zero**: "acquired without an associated, documented fiat expenditure — tax cost basis is mathematically zero." |

> **Assessment**: This directly depends on the liquidation bonus characterization above. If KIS treats it as a "free receipt" taxed at receipt, the recognized income becomes the cost basis (prevents triple taxation). If treated as exchange mechanism, the cost comes from the global pool.

---

## Unique Insights Per Model

### ChatGPT 5.4 Pro
- **Only model to identify the gas fee "dual bind"**: gas on crypto-to-crypto is both non-deductible AND potentially a separate taxable disposal (using crypto to settle an obligation). This is the most important novel insight across all 4 responses.
- Most cautious and precise about what it did and didn't find. Explicitly states when no precedent exists rather than inferring from analogies.
- Cites **KIS 0113-KDIPT2-3.4011.709.2025.2.SJ** (Nov 2025) — very active own-account crypto trading confirmed as PIT-38.
- Cites **KIS 0115-KDIT1.4011.591.2024.2.MR** (Oct 2024) — automated stablecoin mechanics, restrictive view on protocol fees.

### ChatGPT Deep Research
- Most thorough statutory walkthrough — traces every claim back to specific PIT Act articles and official guidance.
- Highlights the **ryczałt exclusion risk**: if bot trading were reclassified as AML-type business, ryczałt act excludes "buying/selling foreign exchange values" (wartości dewizowe), which could affect the JDG's ryczałt eligibility.
- Notes an NSA judgment (2022) that classified crypto intermediation as "other monetary intermediation" — excluded from ryczałt.
- Best explanation of the "service to others" vs "own-account" distinction for AML applicability.

### Perplexity
- Most comprehensive **KIS interpretation table** (12+ sygnaturas with dates and sygnatury).
- **Only model to cite a specific 2025 KIS ruling on high-volume P2P trading**: sygn. 0114-KDIP3-1.4011.470.2025.2.EC (July 2025) — 400 trades/month confirmed as PIT-38.
- Most detailed analysis of the **WSA Gliwice server PE case** (I SA/Gl 175/24, Nov 2024) — rented servers creating PE for foreign company.
- Unique mention of **danina solidarnościowa** (4% surcharge on income > 1M PLN) — relevant at scale.
- Most detailed on DAC8 reporting timeline and implications.
- Provides the "conservative" and "aggressive" treatment options for each scenario with clear risk labels.

### Gemini 3.1 Deep Research
- **"Chinese Wall" principle**: Most emphatic about strict separation between JDG and private bot operations. Bot capital must come from personal accounts, infrastructure billed to individual not JDG, bot code cannot be capitalized within JDG.
- **Stablecoin safe harbor analysis**: Explicitly addresses MiCA risk that EMT-classified stablecoins could lose crypto-to-crypto tax neutrality in future if Polish PIT Act harmonizes with MiCA definitions.
- Most detailed on **KIS 0115-KDIT1.4011.582.2025.1.MR** — the "landmark" ruling where KIS confirmed automated 24/7 bot trading with private funds stays PIT-38.
- Cites **0112-KDIL2-2.4011.234.2025.3.AA** — KIS stating "intensity and volume of transactions do not prejudge the change of qualification."
- Most aggressive cost trap quantification: "$365,000/year in gas fees, all legally invisible."
- Rejects liquidation bonus as "service provision" — no bilateral legal entity exists when interacting with autonomous smart contracts.

---

## KIS Interpretations Cited Across All Models

| Sygnatura | Date | Topic | Cited By |
|---|---|---|---|
| 0113-KDIPT2-3.4011.709.2025.2.SJ | Nov 2025 | Active own-account crypto trading → PIT-38 | ChatGPT Pro, Gemini |
| 0115-KDIT1.4011.582.2025.1.MR | Late 2025 | Automated 24/7 bot trading with private funds → PIT-38 | Gemini, ChatGPT DR |
| 0112-KDIL2-2.4011.234.2025.3.AA | Jun 2025 | Volume doesn't change classification; airdrop treatment | Gemini |
| 0114-KDIP3-1.4011.470.2025.2.EC | Jul 2025 | 400 P2P trades/month still PIT-38 | Perplexity |
| 0115-KDIT1.4011.591.2024.2.MR | Oct 2024 | Automated smart contract/stablecoin mechanics | ChatGPT Pro |
| 0112-KDIL2-2.4011.146.2024.2.IM | Apr 2024 | Staking/airdrop rewards → income at receipt | Perplexity, ChatGPT DR |
| 0113-KDIPT2-3.4011.186.2025.4.JŚ | Jun 2025 | Airdrop tokens → income at receipt | Perplexity |
| NSA II FSK 1688/19 | Mar 2022 | Crypto-to-crypto non-taxable (confirmed even pre-2019) | Perplexity |
| WSA Gliwice I SA/Gl 175/24 | Nov 2024 | Rented servers can create PE | Perplexity |

**Notable gap**: No KIS interpretation exists specifically on DeFi liquidation bots, flash loans, DEX arbitrage, MEV, or gas fee treatment in DeFi context. All models confirm this gap.

---

## Actions Relevant to Us

### Immediate

1. **Keep bot operations strictly in PIT-38** — do not register as AML entity, do not accept third-party funds
2. **Enforce "Chinese Wall"** between JDG and bot: fund bot from personal accounts, bill server costs to individual, keep separate wallets
3. **File PIT-38 annually** even in zero-gain years (to preserve cost carry-forward chain)
4. **Begin structured transaction logging** now — wallet exports, tx hashes, chain/block timestamps, protocol call traces, reconciliation to PIT-38 aggregates

### Before Scaling

5. **Request interpretacja indywidualna (PLN 40)** covering:
   - Classification of DeFi liquidation bonuses (free receipt vs exchange mechanism vs service)
   - Gas fee treatment: is paying gas a taxable disposal (settling obligation with crypto)?
   - Flash loan fee deductibility
   - Whether automated bot trading with private funds remains PIT-38

6. **Set up crypto tax software** (Koinly, Divly, or custom SQL) configured for Polish law — essential for 365K+ annual transactions

### Ongoing Compliance

7. **Prepare for DAC8**: from 2027, KAS will automatically receive CEX transaction data. Ensure PIT-38 fiat off-ramps match exchange records exactly
8. **Monitor MiCA implementation** in Polish law — risk that EMT-classified stablecoins (USDC) could lose crypto-to-crypto tax neutrality if PIT Act harmonizes with MiCA definitions
9. **Track total income across all sources** — danina solidarnościowa (4% surcharge) applies above 1M PLN total annual income
10. **Archive exchange data proactively** — platforms retain data only 1-3 years

### The Cost Trap Reality

The structural weakness of PIT-38 for bot operators is the **non-deductibility of operational costs**:
- Gas fees on all crypto-to-crypto trades: **non-deductible**
- Flash loan premiums: **non-deductible**
- Server hosting: **non-deductible**
- Failed transaction gas: **non-deductible**
- Bot development time: **non-deductible**

This means the **effective tax rate on real economic profit** is substantially higher than 19%, because the tax base includes gross disposal proceeds minus only fiat acquisition costs — ignoring the massive friction costs that actually determine profitability. This is the price of PIT-38's structural advantages (no ZUS, no progressive rates, no JDG contamination).

**Only deductible**: initial fiat→crypto purchases, CEX trading commissions on fiat↔crypto, and gas directly tied to fiat disposal transactions.
