# Tax Implications of Automated Crypto Bot Trading Under Polish JDG (2025–2026)

## Executive Summary

Under current Polish tax law, automated liquidation and DEX arbitrage bots operated for one's own account almost certainly remain in the **PIT-38 capital gains regime at 19%**, regardless of transaction volume or automation level. The critical structural protection is **Art. 17 ust. 1g PIT**, which locks virtually all crypto disposal income into the capital gains source even within a JDG, and **Art. 17 ust. 1f PIT**, which defines "disposal" as exchange-to-fiat only — meaning the overwhelming majority of bot transactions are simply **non-events for tax purposes**. Server location in Germany or elsewhere creates no material tax risk for a Polish resident. The existing ryczałt 12% JDG is unaffected. However, the regime contains critical traps: liquidation bonuses may be taxed as "other income" at progressive rates at receipt, gas fees on crypto-to-crypto swaps are explicitly non-deductible, and infrastructure costs (servers) cannot be deducted under PIT-38. DAC8 reporting starting January 2026 will dramatically increase KAS visibility into CEX transactions, making compliance now more urgent than ever.

***

## Part 1: Legal Classification — PIT-38 vs. Business Income

### The Statutory Default: Art. 17 ust. 1g PIT

The cornerstone of Polish crypto taxation since January 2019 is **Art. 17 ust. 1 pkt 11** read together with **Art. 17 ust. 1g** of the PIT Act. The former classifies income from disposal of virtual currency as "capital gains" (kapitały pieniężne), a separate source of income under Art. 10 ust. 1 pkt 7. The latter explicitly provides that this classification applies **even when the disposal is conducted within the framework of a JDG** (sole proprietorship). This is a statutory override — the normal rule that business income is taxed as business income does not apply to crypto disposal.[^1][^2][^3]

The consequence is categorical: a developer running arbitrage or liquidation bots **under a JDG** still reports all crypto disposal income on **PIT-38** at a flat 19%, not PIT-36/PIT-36L as business income. There is no progressive scale; there is no ryczałt; there is no kwota wolna. The tax is simply 19% of: (revenues from disposal) minus (documented acquisition costs).[^2][^4][^5][^6]

Crucially, **Art. 30b ust. 5b PIT** prohibits combining crypto capital gains with any other income — they are always taxed separately at 19% regardless of other income sources or tax forms.[^3]

### The AML Exception: Can Bot Activity Become Business Income?

Art. 17 ust. 1g contains a single exception: activities classified under **AML Art. 2 ust. 1 pkt 12** — which defines "obligated entities" in the virtual currency business — are treated as business income, not capital gains. These four regulated activities are:[^7][^3]

1. Exchange between virtual currencies and payment means (fiat↔crypto)
2. Exchange between virtual currencies (crypto↔crypto)
3. Intermediation in the above exchanges
4. Maintaining virtual currency accounts (wallets/custody)

At first glance, categories (1) and (2) appear to encompass DEX arbitrage (buying low/selling high) or even liquidation mechanics. However, the decisive legal qualifier is that AML Art. 2 ust. 1 pkt 12 refers specifically to **"prowadzenie działalności gospodarczej polegającej na świadczeniu USŁUG"** — conducting business activity consisting of **providing services to third parties**. A bot that trades exclusively for its own account, using its own capital, earning profit for itself, does **not** provide exchange services to third parties. It is not a crypto exchange (giełda), not a cantor (kantor), not a custodian. The legislative intent is to bring regulated VASP/CASP-type businesses within the business income regime, not to reclassify private algorithmic traders.[^8][^9][^10][^11]

**Conclusion on AML exception**: Liquidation and arbitrage bots operated for one's own account do **not** fall under AML Art. 2 ust. 1 pkt 12. The income remains in the PIT-38 capital gains regime.

### High-Volume Trading and Business Reclassification Risk

Polish law defines business activity (pozarolnicza działalność gospodarcza) as "gainful activity conducted in an organized and continuous manner" (Art. 5a pkt 6 PIT). Automated bots running 24/7 technically satisfy the "organized and continuous" test. However, the **PIT statute explicitly resolves this tension**: Art. 17 ust. 1g acts as a *lex specialis* override, keeping crypto disposal in capital gains regardless of how organized or continuous the trading is.[^1][^3]

Critically, a **KIS individual interpretation dated 15 July 2025** (sygn. 0114-KDIP3-1.4011.470.2025.2.EC) confirmed that a taxpayer executing approximately **400 P2P crypto transactions per month** could still be taxed under the personal capital gains regime (PIT-38), not as a business. The KIS focused on whether the taxpayer provided services to others, had employees, had professional infrastructure operating for clients, or raised external capital — not simply on transaction volume or use of automated tools. Volume alone does not trigger reclassification.[^12]

### PKD Code Implications and Ryczałt 12% Protection

The existing JDG with PKD 62.01.Z at ryczałt 12% covers software development services. Crypto trading income does not flow through this JDG for tax purposes at all — it goes directly to PIT-38 as a separate income source. There is no interaction or contamination between the two regimes.[^4][^13][^14][^3]

If the developer chose to register a separate PKD for crypto-related trading activity (e.g., PKD 64.19.Z "Remaining monetary intermediation," which NSA has associated with crypto exchange via internet), this would be purely for CEIDG classification purposes and would not affect the ryczałt 12% on the software PKD. The two income streams are legally separate. However, adding PKD 64.19.Z could attract AML scrutiny if it implies provision of exchange services to third parties — this is generally unnecessary and inadvisable for a developer trading only for their own account.[^15][^10]

***

## Part 2: The Crypto-to-Crypto Neutrality Principle

### Statutory Definition of "Disposal" (Art. 17 ust. 1f PIT)

**Art. 17 ust. 1f PIT** defines "odpłatne zbycie waluty wirtualnej" (taxable disposal) as:

> Exchange of virtual currency for: **legal tender**, goods, services, or property rights **other than virtual currency**, or settling obligations with virtual currency.

The explicit exclusion of virtual currency-to-virtual currency exchange from this definition means that **crypto-to-crypto swaps do not constitute a taxable disposal**. This is confirmed by NSA jurisprudence (II FSK 1688/19, 22 March 2022), which established that even pre-2019, crypto-to-crypto exchange was not taxable.[^16][^17][^18][^19][^1]

### Implications for High-Frequency Bot Trading

For a bot executing 1,000 DEX arbitrage trades per day (all crypto-to-crypto):
- **None of those trades is a taxable event** — zero tax liability accrues during trading[^17][^20][^16]
- The entire cost basis of funds used to start the bot (ETH, WBTC, USDC — purchased with fiat) builds up as "pending" deductible costs carried in the annual cost pool
- **Tax only arises when accumulated crypto is converted to fiat** (EUR/PLN/USD)
- The cost pool uses the **annual pool method** (not FIFO) — all acquisition costs in a given year form a single pool, matched against disposal revenues in that year, with excess costs carrying forward indefinitely to future years[^21][^22]

### Practical Timing: The "Trigger" Events

For the bot developer, the following are the **only taxable events** (triggering PIT-38 reporting):

| Event | Taxable? | Basis |
|---|---|---|
| Buy ETH with EUR on Kraken | No (fiat→crypto acquisition) | Creates cost |
| Bot swaps ETH→USDC on DEX | No | Art. 17 ust. 1f |
| Bot swaps USDC→WBTC on DEX | No | Art. 17 ust. 1f |
| Bot executes liquidation, receives ETH bonus | **Disputed — see Part 3** | Complex |
| Bot gas fees paid in ETH (for crypto-to-crypto) | No taxable event; also **non-deductible** | Art. 23 ust. 1 pkt 38d |
| Swap 500 USDC → EUR on Kraken | **YES — taxable disposal** | Art. 17 ust. 1f |
| Pay for Hetzner VPS with EUR (from bank account) | N/A (server cost) | Indirect cost — see Part 4 |

### Cost Pool Construction for Annual Reporting

At the end of the tax year, the developer calculates:
- **Revenue** = sum of all fiat (PLN/EUR/USD/other fiat) received from crypto disposals, converted to PLN at NBP mid-rate from the last business day preceding each disposal
- **Costs** = sum of all documented direct acquisition costs (fiat paid for crypto, CEX trading commissions on fiat-to-crypto trades) incurred in the current year, plus any cost excess carried forward from prior years
- **Taxable income** = Revenue − Costs (if positive, taxed at 19%; if negative, carried forward)

PIT-38 requires only **aggregate annual figures** — no per-transaction breakdown is filed in the form itself. However, documentation of each transaction must be retained to support the aggregates, since KAS can audit.[^22][^23][^24]

***

## Part 3: Liquidation Bonuses — The Most Complex Question

### What Is a Liquidation Bonus?

In DeFi lending (Aave, Compound, Morpho), a liquidator repays a portion of an under-collateralized borrower's debt and receives in exchange the borrower's collateral at a discount (the "liquidation bonus" or "incentive," typically 5–15%). The bot effectively performs a service (market stabilization) and receives cryptocurrency as the reward.

### Three Possible Tax Characterizations

**Scenario A — Treated as crypto acquisition at market value (cost basis = market value at receipt)**
Under this approach, receiving the ETH liquidation bonus is treated as acquiring ETH at zero additional fiat cost (since no fiat was paid), but the prior flash loan repayment and collateral handover constitute the real cost. The bonus ETH sits in the cost pool at its fiat-equivalent value at date of receipt and is taxed only when ultimately disposed for fiat. This is the most taxpayer-favorable reading.

**Scenario B — Treated as "free receipt" analogous to staking reward (taxed at receipt as "other income")**
KIS has consistently held, including in interpretation **0112-KDIL2-2.4011.146.2024.2.IM** (April 2024), that receiving crypto rewards through staking or airdrops constitutes income ("przychód z praw majątkowych" under Art. 18 PIT) at the moment of receipt, valued at market prices. If KIS analogizes a liquidation bonus to a staking reward, it would be taxed as "other income" (Art. 20 ust. 1 PIT) or "rights income" (Art. 18 PIT) at **progressive rates (12%/32%)** at the time of receipt — not at disposal. KIS extended this logic to airdrops in June 2025 (interpretation 0113-KDIPT2-3.4011.186.2025.4.JŚ). The cost basis of the ETH upon later disposal would be the value recognized as income at receipt.[^25][^26][^27][^28]

**Scenario C — Treated as JDG service income (most aggressive)**
If a liquidation is viewed as performing a DeFi "service" (executing a smart contract function on behalf of the protocol), the crypto received could arguably be JDG business income taxed as ryczałt. One KIS interpretation (0113-KDIPT2-1.4011.572.2022.2.MGR, October 2022) addressed an IT contractor receiving a bonus in crypto tokens, treating it as business income subject to ryczałt. A separate interpretation found that receiving crypto as compensation for performing IT services creates a business income event at receipt.[^29][^30]

### Most Likely KIS Position and Risk Assessment

Given the current KIS interpretive trajectory, a liquidation bonus received in ETH for executing a bot liquidation call is most likely to be characterized as **Scenario B** — income from rights at receipt — because:
- The bot receives crypto without paying fiat for it (pure "gain")
- KIS consistently taxes "gratuitous" crypto receipts at receipt, not at disposal
- The liquidation bonus is not a pure market trade (no fiat changing hands); it is a protocol-mediated reward

**Dual taxation risk**: If taxed at receipt as progressive income AND later taxed again at disposal as capital gains (minus the cost basis established at receipt), this creates an effective double-taxation structure. KIS has not published a definitive interpretation specifically on DeFi liquidation bonuses, but the analogy to staking rewards is strong in the current interpretive climate.

**Risk level**: **HIGH** uncertainty. A dedicated individual tax interpretation (interpretacja indywidualna) from KIS is strongly recommended before operating liquidation bots at scale.

### Flash Loans

Flash loans are borrowed and repaid within a single atomic transaction. The net economic effect is zero (no acquisition of capital). Polish law has no specific provision for flash loans. The most defensible analysis is:
- The flash loan "acquisition" and "repayment" occur in the same transaction block with no net economic gain from the loan itself — only the arbitrage/liquidation profit (in crypto) represents actual gain
- Flash loan fees (paid in crypto to the lending protocol) are costs associated with a crypto-to-crypto operation and thus **non-deductible** under Art. 23 ust. 1 pkt 38d[^31]
- No KIS interpretation exists specifically on flash loans (as of March 2026)

***

## Part 4: Deductibility of Gas Fees and Operational Costs

### The Legal Framework for Deductible Costs

Under **Art. 22 ust. 14 PIT**, deductible costs for virtual currency disposal income are limited to:
1. **Documented expenses directly incurred on acquisition** of virtual currency
2. **Costs related to disposal** of virtual currency, including fees paid to entities under AML Art. 2 ust. 1 pkt 12 (i.e., regulated exchanges)[^21][^1]

**Art. 23 ust. 1 pkt 38d PIT** explicitly excludes: "expenses connected with the exchange of virtual currency for another virtual currency".[^31]

### Gas Fees — Detailed Analysis

| Gas Fee Type | Deductible? | Reasoning |
|---|---|---|
| Gas on fiat→crypto acquisition (e.g., buying ETH on CEX) | **YES** | Direct cost of acquisition |
| Gas on crypto-to-crypto swap (DEX arbitrage) | **NO** | Art. 23 ust. 1 pkt 38d explicit exclusion |
| Gas on crypto-to-fiat conversion (Kraken sell) | **YES** | Cost related to disposal |
| Gas on liquidation transaction (receiving ETH bonus) | **Ambiguous** | If bonus = acquisition, gas may be direct cost; if bonus = "free receipt," gas may be excluded |
| Gas on failed/reverted transactions | **NO** | No acquisition or disposal occurred; purely wasted expenditure |
| CEX trading commissions on fiat↔crypto | **YES** | Expressly included as "costs related to disposal" |

The net result for a pure DEX arbitrage bot (all crypto-to-crypto operations) is that essentially **all gas fees are non-deductible** — they constitute costs of crypto-to-crypto exchanges. This is a significant economic drag that cannot be offset in the PIT-38 calculation.[^32][^31]

### Server Hosting Costs

Server hosting costs (Hetzner VPS, AWS, etc.) are **indirect costs** analogous to mining equipment and electricity. The NSA and KIS have consistently ruled that indirect costs cannot be deducted under Art. 22 ust. 14 PIT:[^33][^34][^35]
- Mining equipment and electricity = non-deductible (NSA confirmed)
- Exchange account maintenance fees = non-deductible[^36]
- Server costs for bots = by analogy, non-deductible under PIT-38 capital gains

**However**, if the activity were reclassified as JDG business income (which is unlikely, but see Part 1), server costs would become fully deductible as business expenses under the general Art. 22 ust. 1 PIT cost deduction regime.

**Alternative deduction path**: The server costs are incurred by the JDG as infrastructure. If the developer characterizes a portion of the server costs as expenses related to the JDG's software development activity (PKD 62.01.Z), these costs could potentially be deducted against the ryczałt income — but this is only valid if the server genuinely supports the software development work, not solely the trading bots.

### Bot Development Costs

Time spent developing the trading bot software cannot be deducted against PIT-38 income (no provision for labor value of self-employment under the crypto gains rules). However, if the bot development constitutes work performed **within the JDG** as software development, the JDG income associated with that work is taxed at ryczałt 12%, and costs incurred in that development (hardware, software licenses, tools) are deductible through the JDG's cost framework — but note that ryczałt does not allow cost deduction by definition. Only under podatek liniowy (19%) or skala podatkowa would JDG development costs be deductible.

***

## Part 5: Multi-Jurisdiction Analysis — Server Location and PE Risk

### Polish Resident's Worldwide Tax Obligation

A Polish tax resident (Art. 3 ust. 1 PIT) is subject to **unlimited tax liability** — worldwide income is taxed in Poland regardless of where assets are located, transactions executed, or infrastructure hosted. The location of the Hetzner server in Germany, AWS in Japan, or smart contracts on Ethereum mainnet is irrelevant to the fundamental tax obligation in Poland.[^37][^2]

### Permanent Establishment (Zagraniczny Zakład) Analysis

A "foreign permanent establishment" (zagraniczny zakład) under Art. 5a pkt 22 PIT requires three cumulative elements:[^38]
1. A **fixed place of business** (stała placówka)
2. **Stable/permanent** character (stały charakter)
3. Conducting **business activity** through it

For a Hetzner VPS in Germany:

**Element 1 — Fixed place**: OECD Commentary on Art. 5 (as clarified through multiple updates including 2025) confirms that a **server can constitute a PE** if the enterprise has it "at its disposal" and it performs important/essential functions — not merely preparatory or auxiliary ones. Human presence is not required. However, a critical distinction exists: OECD Commentary paragraph 42.2 distinguishes between:[^39][^40]
- A server **owned or exclusively leased** by the enterprise (PE possible) 
- A server at an **ISP/hosting provider** where the enterprise merely has a contractual right to use resources (generally NOT a PE for the client)[^41]

A standard Hetzner VPS or dedicated server involves the **developer having exclusive disposal** of that server — they control it entirely, it runs only their code, and it is effectively "at their disposal" in the legal sense. This is distinguishable from shared ISP hosting. **WSA Gliwice (I SA/Gl 175/24, November 2024)** held that rented servers in Poland created a PE for a foreign company because those servers were "an essential element of the company's core business".[^42]

**Element 3 — Business activity**: The trading bot performs the enterprise's core economic function (arbitrage, liquidations) continuously and autonomously. This is not preparatory/auxiliary activity. If a German court found an automated oil pipeline to be a PE for Dutch operators, an algorithmic trading bot generating all profits through its autonomous operations likely exceeds the preparatory/auxiliary threshold.[^41]

**PE Risk Assessment**:

| Scenario | PE Risk Level | Analysis |
|---|---|---|
| Hetzner dedicated server (exclusive control, core bot operations) | **MEDIUM** | Server at disposal, core functions, but: Polish resident = all income taxed in PL anyway |
| Hetzner VPS (shared resources, root access) | **LOW-MEDIUM** | Arguments both ways; standard VPS has limited "fixity" in legal sense |
| AWS Tokyo region (cloud, shared infrastructure) | **LOW** | Cloud = hyperscaler model; no exclusive disposal of specific hardware |
| Smart contract "location" on Ethereum | **NONE** | Protocol has no physical location; no tax jurisdiction |

### The Critical Practical Point: PE Has Minimal Impact for Polish Residents

Even **if** a foreign PE were found to exist in Germany under the Poland-Germany DTT (signed 14.05.2003, in force 01.01.2005):[^43]
- Germany would gain the right to tax profits **attributable to the German PE** under DTT Art. 7
- But under the PL-DE DTT, Poland typically applies the **exemption method** — German PE income is exempt from Polish tax but used for progression purposes
- Since PIT-38 crypto capital gains use a flat 19% rate (no progression), exempting the PE portion from Poland would merely shift where 19% is paid — with Germany also taxing at its rates

**More practically**: Germany does not currently have crypto-specific regulations treating crypto disposal gains from automated bots as business income attributable to a server PE. The administrative complexity of a German tax registration, filing, and audit far outweighs the marginal risk. The conservative practical approach is to treat all income as Polish-source personal capital gains and report on PIT-38.

**Japan server**: The Poland-Japan DTT provides similar business profits allocation rules. A Japanese AWS Tokyo instance, running shared cloud infrastructure not "exclusively at the developer's disposal," creates negligible PE risk — and even if it did, Japanese tax authorities have shown no inclination to pursue PE claims against foreign personal crypto traders using Japanese cloud services.

### Smart Contract Location: Legally Irrelevant

The location of a smart contract (Uniswap on Ethereum, Aave on Polygon) has no tax jurisdiction significance. Smart contracts are code deployed on a distributed blockchain with no physical location. No jurisdiction has successfully asserted taxing rights based on smart contract "location." Polish tax obligations are determined solely by the **developer's residency**, not the protocol's blockchain or smart contract address.[^44]

***

## Part 6: Volume, Documentation, and PIT-38 Reporting Methodology

### How PIT-38 Works for High-Volume Bots

PIT-38 is filed once per year (February 15 – April 30) and **requires only annual aggregate figures**:[^4][^22]
- Box: Total revenues (przychody) from virtual currency disposal in the tax year
- Box: Total costs (koszty) of virtual currency acquisition and disposal in the tax year + carried-forward costs from prior years
- Box: Net income (dochód) or excess costs to carry forward

There is **no per-transaction reporting requirement** in PIT-38. For a bot executing 365,000 transactions per year, the taxpayer enters a single revenue figure and a single cost figure.[^23][^24]

### Documentation Requirements

While PIT-38 only requires aggregates, **KAS can audit**. The developer must retain documentation sufficient to reconstruct the calculation:

**Required records** (no statutory format, but must be reconstructable):
- Complete transaction history from all chains (on-chain records are permanent; DEX transactions are on-chain)
- Fiat-to-crypto purchase records with prices and commissions (CEX exports, bank statements)
- Crypto-to-fiat sale records with prices (CEX exports, fiat receipt records)
- All fiat amounts must be convertible to PLN using NBP mid-rate from the last business day preceding each transaction
- Flash loan and gas fee records (for cost basis and non-deductibility documentation)

**Tools**: Specialized crypto tax software (Divly, Koinly, etc.) can process on-chain transaction data across Ethereum, Arbitrum, Polygon, etc., and generate PIT-38-compatible aggregates. For a developer building custom bots, maintaining a SQL database or structured log of all transactions is straightforward and advisable.[^12]

**The DAC8 Factor**: From January 1, 2026, EU-licensed CEXes (Kraken, Binance, Coinbase, etc.) are required to report user transaction data to national tax authorities under DAC8. Polish KAS will receive detailed reports on CEX transactions starting in 2027 (for 2026 data). This makes accurate PIT-38 filing for CEX-side disposals (the "profit taking" step) a compliance imperative, not just a best practice. DeFi bot operations (on-chain, non-custodial) are not captured by DAC8, as on-chain DEX activity does not go through a reporting CASP.[^45][^46][^47]

### AML Registration Obligation

Since the bot operates for its own account and does not provide exchange, intermediation, or wallet services to third parties, **no registration in the VASP registry** (Rejestr działalności w zakresie walut wirtualnych, administered by Dyrektor Izby Administracji Skarbowej in Katowice) is required. Registration is required only for entities providing regulated crypto services to others; personal trading — regardless of scale — does not trigger this obligation. Failure to register when required carries fines up to PLN 100,000.[^11]

### ZUS and Health Insurance

Income reported on PIT-38 as capital gains (kapitały pieniężne) does **not** constitute a base for ZUS social security contributions or the health insurance premium (składka zdrowotna). This is a significant advantage over business income: there are no ZUS obligations on any amount of crypto capital gains, regardless of scale. The developer's ZUS obligations arise solely from the JDG software development activity (ryczałt-based health insurance contribution formula).[^3]

***

## Part 7: Practical Walk-Through Examples

### Example 1: Arbitrage Bot Annual Reporting

**Scenario**: Bot starts with 10 ETH purchased for 25,000 EUR. Over 12 months, executes 50,000 crypto-to-crypto DEX trades. Year-end holding: 12 ETH + 500 USDC. Developer converts 500 USDC to EUR on Kraken (receives 490 EUR net after fees).

**Tax analysis**:

| Item | Tax Treatment |
|---|---|
| 50,000 DEX arbitrage swaps (all crypto-to-crypto) | Non-taxable events — zero PIT-38 entries for these[^16][^1] |
| 2 ETH "gained" from arbitrage (held as ETH) | Non-taxable until disposed; no current-year tax |
| 500 USDC → EUR conversion on Kraken | **TAXABLE DISPOSAL** — triggers PIT-38[^16][^4] |
| Revenue from USDC disposal | 490 EUR × NBP PLN rate on prior business day |
| Deductible cost (USDC cost basis) | Attributable portion of total cost pool (original 25,000 EUR equivalent in PLN) |
| Cost pool method | Annual pool: all 2025 acquisition costs ÷ prorated by disposal[^21] |
| Kraken commission on USDC→EUR | YES, deductible as disposal cost[^48][^49] |
| Gas fees on DEX swaps | **NON-DEDUCTIBLE** — Art. 23 ust. 1 pkt 38d[^31] |
| Server costs (Hetzner) | **NON-DEDUCTIBLE** — indirect costs[^33][^34] |
| Filing: PIT-38 | One form, annual aggregates, deadline April 30 |
| PIT-28 (ryczałt) | Separate, unaffected by crypto activity |
| ZUS | No crypto-related ZUS obligations[^3] |

**Realistic PIT-38 entry**: If the cost pool shows that the 500 USDC disposal carries proportional acquisition costs nearly equal to the disposal proceeds (which is likely given the bot "earned" the USDC through many zero-cost crypto-to-crypto trades — the cost basis depends on how USDC was acquired, potentially at near-zero additional fiat cost), the taxable income could be close to the full 490 EUR equivalent — or zero if the cost pool absorbs it.

### Example 2: Liquidation Bot — Receiving ETH Bonus

**Scenario**: Bot liquidates a position, receives 0.1 ETH (value at receipt: 300 EUR). This ETH is later swapped to USDC (crypto-to-crypto, non-taxable). USDC is later converted to EUR on Kraken.

**Conservative (pro-compliance) treatment**:

1. **Receipt of 0.1 ETH** as liquidation bonus — likely taxed as "income from other sources" (Art. 20 ust. 1) or "income from property rights" (Art. 18) at progressive rates (12%/32%), valued at 300 EUR equivalent in PLN at date of receipt. This income is reported in PIT-36/PIT (not PIT-38).[^26][^50][^25]

2. **ETH → USDC swap**: Non-taxable disposal event. The USDC acquires cost basis equal to the ETH's recognized value at receipt (300 EUR equivalent in PLN).[^16]

3. **USDC → EUR on Kraken**: Taxable disposal under PIT-38. Revenue = EUR received in PLN. Cost = 300 EUR equivalent allocated to this USDC (the value recognized at step 1). Net income = EUR received minus cost basis minus Kraken commissions.

**Result**: Double reporting — once at receipt on PIT (progressive), once at disposal on PIT-38 (19%). The cost basis established at receipt prevents triple taxation.

**More favorable (aggressive) treatment**: Argue the 0.1 ETH received is a crypto acquisition at cost = the value of debt repaid via flash loan plus gas (which creates traceable cost). Under this view, no income arises at receipt; everything is deferred to the fiat disposal event on PIT-38. This is more tax-efficient but carries interpretation risk.

**Recommendation**: File a dedicated interpretacja indywidualna (individual tax ruling) with KIS before scaling liquidation bot operations. The fee is PLN 40 per question. KIS is bound by favorable rulings issued to the same taxpayer.

***

## Part 8: Existing KIS Interpretations and Court Rulings

### Directly Relevant KIS Interpretations

No KIS interpretation as of March 2026 has specifically addressed **automated bot trading**, **DEX arbitrage**, **DeFi liquidation bonuses**, **MEV strategies**, or **flash loan taxation**. This is a significant gap in the interpretive landscape.

The closest analogous rulings:

| Interpretation | Sygn. | Date | Ruling |
|---|---|---|---|
| High-volume P2P trading (400 trades/month) | 0114-KDIP3-1.4011.470.2025.2.EC | July 2025 | Still PIT-38, not business[^12] |
| Staking and airdrop rewards | 0112-KDIL2-2.4011.146.2024.2.IM | April 2024 | Income at receipt, not at disposal[^25][^26] |
| Airdrop tokens | 0113-KDIPT2-3.4011.186.2025.4.JŚ | June 2025 | Income at receipt[^27] |
| Crypto bonus in business (IT) | 0113-KDIPT2-1.4011.572.2022.2.MGR | Oct 2022 | Complex analysis — ryczałt 3%?[^29] |
| Mining equipment/electricity non-deductible | Multiple NSA rulings 2022-2024 | Various | Indirect costs, non-deductible[^33][^34] |
| Receiving crypto for services | 0111-KDIB1-3.4010.301.2024.2.JKU | 2024 | Business income at receipt[^51] |
| WSA Gdańsk — cantor commissions | (WSA Gdańsk) | March 2025 | VASP commissions taxed only at fiat conversion[^52] |

### NSA and WSA Court Rulings of Relevance

- **NSA II FSK 1688/19** (22 March 2022): Crypto-to-crypto exchange confirmed as non-taxable even before 2019[^18][^19]
- **NSA** (2022): Crypto trading with traditional accounts may generate progressive-rate income — but this was under pre-2019 law[^53]
- **WSA Gliwice I SA/Gl 175/24** (November 2024): Rented servers in Poland can create PE for foreign company when servers are core to business[^42]
- **WSA Gdańsk** (March 2025): Crypto exchange service companies' commissions not taxed until fiat conversion[^52]

***

## Part 9: Risk Matrix and Strategic Recommendations

### Risk Summary

| Issue | Risk Level | Key Risk | Mitigation |
|---|---|---|---|
| PIT-38 (not business) classification | LOW | Volume/automation triggers business reclassification | KIS Jul 2025 ruling supports PIT-38 for own-account trading |
| Liquidation bonus taxation at receipt | HIGH | Progressive tax triggered on receipt, not just disposal | Get individual KIS interpretation; document carefully |
| Gas fee non-deductibility | MEDIUM | Most bot operating costs unrecoverable from taxes | Accept as structural; optimize fiat withdrawal strategy |
| Server PE in Germany | LOW | German tax registration requirement | Standard VPS model; PE threshold not met in practice |
| AML registration obligation | LOW-MEDIUM | If activity reclassified as "service provision" | Ensure bot clearly trades for own account only |
| DAC8 CEX reporting (from 2026) | HIGH | KAS will see all Kraken/Binance withdrawals | File accurate PIT-38 — non-compliance risk now higher |
| Documentation insufficiency | MEDIUM | Cost basis challenges during KAS audit | Maintain structured transaction logs; export on-chain data |
| Danina solidarnościowa (4% surcharge) | LOW-MEDIUM | Applies if total income >1M PLN | Track total income across all sources |

### Strategic Recommendations

1. **File PIT-38 annually** covering all fiat disposals (crypto→fiat) from bot profits. Include carried-forward costs from prior years. Maintain complete transaction logs.[^24][^23]

2. **Do not register as AML-regulated entity** unless the business model shifts to providing crypto exchange services to third parties. Operating purely for own account with own capital does not require VASP registration.[^11]

3. **Obtain individual KIS interpretations** (interpretacje indywidualne) on: (a) liquidation bonus taxation at receipt; (b) characterization of flash loan fees; (c) server cost deductibility if the activity were ever challenged as business. Each interpretation costs PLN 40 and provides legal protection.

4. **The ryczałt 12% JDG is fully protected**. Crypto income goes to PIT-38; software development goes to PIT-28. These never interact.[^14][^3][^4]

5. **No ZUS obligations** on any crypto capital gains income — a structural advantage of the PIT-38 route versus business income.[^3]

6. **Prepare for DAC8 scrutiny**: Starting 2027 (for 2026 transactions), KAS will receive automatic CEX reports. Ensure all CEX-side fiat withdrawals are properly reported in PIT-38 with matching cost documentation.[^47][^45]

7. **Server location**: Use standard VPS/cloud hosting and do not register local businesses in Germany or Japan. Polish worldwide tax obligation covers all income. The PE risk from a standard Hetzner VPS does not materially affect total tax burden (same 19% rate applies).[^38][^39]

8. **Timing optimization**: Since only fiat conversions trigger tax, consider concentrating fiat withdrawals in tax years with high accumulated costs (carried-forward from prior low-income years) to minimize net taxable income.[^22][^21]

9. **Above PLN 1 million total income**: The 4% danina solidarnościowa applies to total income exceeding PLN 1M annually (including crypto capital gains). At scale, this becomes a planning consideration.

---

## References

1. [Kryptowaluty i podatki (6) Obrót kryptowalutą dokonywany ...](https://www.podatki.biz/artykuly/kryptowaluty-i-podatki-6-obrot-kryptowaluta-dokonywany-przez-przedsiebiorce-i-podatek-pit_65_55986.htm) - Zgodnie z art. 17 ust. 1 pkt 11 ustawy PIT przychody z odpłatnego zbycia waluty wirtualnej uważa się...

2. [Cryptocurrency tax in Poland in 2025 – rules and settlement](https://getsix.eu/getsix-blog/accounting-hr-payroll-tax-and-legal-alerts-poland/taxes-and-law-in-poland/cryptocurrency-tax-in-poland-in-2025-rules-and-settlement/) - Cryptocurrency tax in Poland is 19% – learn about settlement rules, deductible costs and when the ta...

3. [Działalność w zakresie obrotu kryptowalutami a składka ...](https://akademialtca.pl/blog/dzialalnosc-w-zakresie-obrotu-kryptowalutami-a-skladka-zdrowotna) - Od 01 stycznia 2019 r., przychody z obrotu kryptowalutami zaliczane są do źródła kapitałów pieniężny...

4. [Cryptocurrency Tax in Poland in 2025](https://www.rebellpay.com/en/cryptocurrency-tax-in-poland-in-2025/) - In Poland, there is a dedicated form for reporting crypto profits — PIT-38. You must declare all inc...

5. [Crypto Tax in Poland: 2025 Guide](https://www.dudkowiak.com/blog/crypto-tax-in-poland-2025-guide/) - Income from the sale of virtual currencies is taxed at a flat rate of 19%. There are no applicable d...

6. [Krypto, fiskus i 19 procent. Co polski inwestor naprawdę musi ...](https://is.rzeszow.pl/krypto-fiskus-i-19-procent-co-polski-inwestor-naprawde-musi-wiedziec-o-podatkach-od-kryptowalut/) - Przepisy nie każą Ci płacić podatku za samo trzymanie kryptowalut na portfelu. Kluczowe pojęcie to „...

7. [Kradzież kryptowalut – jakie skutki podatkowe w PIT?](https://poradnikprzedsiebiorcy.pl/-kradziez-kryptowalut-jakie-skutki-podatkowe-w-pit) - Kradzież kryptowalut to pomimo straty musisz wykazać koszty ich nabycia w rocznym PIT-38. Sprawdź, j...

8. [Giełda kryptowalut, a wpis do rejestru](https://mentzen.pl/blog/inne/kryptowaluty/gielda-kryptowalut-a-wpis-do-rejestru/) - Wniosek o wpis można złożyć w formie elektronicznej, prowadzony jest przez Izbę Administracji Skarbo...

9. [Nowy rejestr – działalność w branży walut wirtualnych tylko ...](https://kryptoprawo.pl/nowy-rejestr-dzialalnosc-w-branzy-walut-wirtualnych-tylko-po-uzyskaniu-wpisu/) - Rejestr będzie dotyczył przede wszystkim podmiotów świadczące usługi wymiany pomiędzy walutami fiduc...

10. [PKD dla kantorów kryptowalut](https://kryptoprawo.pl/pkd-dla-kantorow-kryptowalut/) - NSA wyjaśnia również kwestię związaną z kodem PKD dla kantorów kryptowalut. Zgodnie z treścią dokume...

11. [Kto musi wpisać się do rejestru działalności w zakresie ...](https://sawaryn.com/publikacje/kto-musi-wpisac-sie-do-rejestru-dzialalnosci-w-zakresie-walut-wirtualnych/) - Pamiętaj o tym, że podmiot, który wykonuje działalność z zakresu walut wirtualnych bez wymaganej rej...

12. [Czy sprzedaż krypto w bitomacie i P2P trzeba wykazać w ...](https://divly.com/pl/przewodniki/bitomat-p2p-pit-38-kryptowaluty) - Najważniejsze: Sprzedaż krypto za PLN w bitomacie, kantorze lokalnym lub P2P traktuj jak normalną sp...

13. [Wykaz PKD a ryczałt – jak należy określać stawkę podatku?](https://firmove.pl/aktualnosci/finanse/podatki/ryczalt-a-wykaz-pkd-i-kody-pkwiu) - Na ryczałcie wykaz PKD i kody PKWiU są wykorzystywane do określenia stawki. Dowiedz się, w jaki spos...

14. [Kody PKD w IT a stawka ryczałtu 8,5% lub 12%](https://poradnikprzedsiebiorcy.pl/-kody-pkd-w-it-i-ich-wplyw-na-stawke-ryczaltu) - Programista, który zdecydował się na ryczałt, może korzystać ze stawki 12% ryczałtu w przypadku, gdy...

15. [Jakie PKD dla kantoru kryptowalut?](https://kryptoprawo.pl/jakie-pkd-dla-kantoru-kryptowalut/) - Po rozpoczęciu działalności gospodarczej zmiana lub dodanie PKD jest możliwe. W tej kwestii wystarcz...

16. [Poland crypto tax guide 2025 - Latest KAS updates](https://www.kraken.com/it/learn/poland-crypto-tax-guide) - Profits from disposing of crypto for PLN or spending crypto are taxed at 19%. Taxpayers report aggre...

17. [Rozliczanie kryptowalut - wszystko co musisz wiedzieć | Blog](https://solidnaksiegowa.com/rozliczanie-kryptowalut-wszystko-co-musisz-wiedziec/) - Czy muszę uwzględniać w PIT-38 wymianę jednej kryptowaluty na inną? ... Nie, wymiana jednej kryptowa...

18. [Kryptowaluty a podatek. Jest korzystny wyrok NSA dla ...](https://www.bankier.pl/wiadomosc/Kryptowaluty-a-podatek-Jest-korzystny-wyrok-NSA-dla-inwestorow-8321252.html) - W korzystnym dla inwestorów wyroku Naczelny Sąd Administracyjny potwierdził, że zamiana jednej krypt...

19. [Zamiana kryptowaluty na inną bez podatku PIT również ...](https://www.nexiaadvicero.eu/zamiana-kryptowaluty-na-inna-bez-podatku-pit-rowniez-przed-2019-r/) - Wyrok ten jest ponownym potwierdzeniem tego, że wymiana w relacji kryptowaluty na inną kryptowalutę ...

20. [NFT and Defi Taxes in Poland: A Comprehensive Guide ...](https://kryptos.io/blog/nft-and-defi-taxes-in-poland-a-comprehensive-guide) - Curious about NFT and Defi taxes in Poland for 2024? Explore our guide to navigate tax implications ...

21. [Korzystne interpretacje Dyrektora KIS dotyczące obrotu ...](https://bieluk.pl/blog/2022/07/21/korzystne-interpretacje-dyrektora-kis-dotyczace-obrotu-walutami-wirtualnymi/) - Z najnowszych interpretacji Dyrektora KIS dotyczących obrotu kryptowalutami wynika również, że podat...

22. [Jak rozliczyć kryptowaluty w PIT-38 za 2025 r.](https://www.pitax.pl/wiedza/poradnik-rozliczenia/jak-rozliczyc-kryptowaluty-w-pit-38/) - Przeczytaj to! ✅ Inwestowanie w waluty wirtualne (tzw. kryptowaluty) z każdym kolejnym rokiem zyskuj...

23. [Jak rozliczyć PIT 38 dla kryptowalut?](https://fakturownia.pl/firma-w-praktyce/jak-rozliczyc-pit-38-dla-kryptowalut) - Przy rozliczaniu PIT 38 kryptowaluty kluczowe jest precyzyjne dokumentowanie każdej transakcji. Błąd...

24. [Podatek od kryptowalut – co musi znaleźć się w PIT-38?](https://openprofit.pl/aktualnosci/podatek-od-kryptowalut-co-musi-znalezc-sie-w-pit-38/) - Rozliczenie PIT: kryptowaluty – kiedy musisz rozliczyć PIT? Zeznanie PIT-38 składa się do 30 kwietni...

25. [0112-KDIL2-2.4011.146.2024.2.IM | Interpretacje podatkowe MF](https://anylawyer.com/interpretacje-podatkowe/otrzymanie-nagrody-w-postaci-dodatkowych-jednostek-waluty-wirtualnej-w-ramach-stakingu-i-airdropu--0112-kdil2-2-4011-146-2024-2-im) - Interpretacja indywidualna dotyczy opodatkowania przychodów z nagród w postaci kryptowalut otrzymany...

26. [Otrzymanie nagrody w postaci dodatkowych jednostek waluty wirtualnej w ramach stakingu i airdropu. - Interpretacja - 0112-KDIL2-2.4011.146.2024.2.IM](https://www.interpretacje.pl/pit/9497679,otrzymanie-nagrody-w-postaci-dodatkowych-jednostek-waluty-wirtualnej-w.html) - Interpretacja indywidualna z dnia 19 kwietnia 2024 r., Dyrektor Krajowej Informacji Skarbowej, sygn....

27. [KIS zmienia zasady opodatkowania airdropów kryptowalutowych](https://pro.rp.pl/nawigator-prawny-poradnik/art43224001-kis-zmienia-zasady-opodatkowania-airdropow-kryptowalutowych) - Krajowa Informacja Skarbowa przełamuje dotychczasową praktykę w opodatkowaniu kryptowalut.

28. [DeFi, Staking, Airdrops - Jak rozliczyć w Polsce 2025 | KryptoTax.pl](https://cryptotax.pl/blog/defi-staking-airdrops-podatki.html) - Kompleksowy przewodnik: jak opodatkować staking rewards, yield farming, liquidity mining, airdrops i...

29. [Opodatkowanie bonusu dla przedsiębiorcy - MDDP](https://www.mddp.pl/opodatkowanie-bonusu-dla-przedsiebiorcy/) - W wielu krajach pracodawcy, aby wyjść naprzeciw oczekiwaniom rynku pracy już teraz często decydują s...

30. [Przegląd interpretacji podatkowych – kryptowaluty pod lupą](https://kryptokancelaria.pl/przeglad-interpretacji-podatkowych-kryptowaluty-pod-lupa/) - Jeśli świadczysz usługę i otrzymujesz kryptowalutę, to masz przychód. KIS uznała to za transakcję ba...

31. [Rozliczenie sprzedaży kryptowalut a podstawa ...](https://poradnikprzedsiebiorcy.pl/-rozliczenie-sprzedazy-kryptowalut-jak-ustalic-podstawe-opodatkowania) - Rozliczenie sprzedaży kryptowalut wiąże się z koniecznością opodatkowania dochodu. Jak prawidłowo ob...

32. [Cryptocurrency tax in Poland in 2025 – rules and settlement](https://poland-accounting.eu/2025/09/cryptocurrency-tax-in-poland-in-2025-rules-and-settlement/) - Cryptocurrency tax in Poland is 19% – learn about settlement rules, deductible costs and when the ta...

33. [Cryptocurrency mining costs: are expenses for electricity and ...](https://atl-law.pl/en/koszty-kopania-kryptowalut-czy-wydatki-na-prad-i-zakup-koparek-to-koszty-uzyskania-przychodu-english/) - The tax authority's position – electricity and mining equipment costs are not deductible expenses. T...

34. [Koparka wirtualnych walut a koszt podatkowy](https://poradnikprzedsiebiorcy.pl/-koparka-wirtualnych-walut-a-rozliczenie-zakupu-w-kosztach-podatkowych) - Wyroki NSA wskazują, że wydatki na zakup koparek do wydobywania waluty wirtualnej nie mogą być uznan...

35. [Your Complete Crypto Tax Guide for Poland](https://nexo.com/pl/blog/a-crypto-tax-guide-for-poland) - Similarly, if you acquire virtual currencies through mining, expenses for mining equipment and elect...

36. [Kompletny przewodnik po rozliczaniu kryptowalut](https://www.infakt.pl/blog/kompletny-przewodnik-po-rozliczaniu-kryptowalut/) - Do kosztów nie zaliczysz jednak kosztów finansowania zakupu kryptowalut, takich jak kredyty czy poży...

37. [Wyrok NSA: handel bitcoinem nawet z 32-procentowym ...](https://www.rp.pl/podatki/art2081141-wyrok-nsa-handel-bitcoinem-nawet-z-32-procentowym-podatkiem) - Kto obraca kryptowalutami, uzyskuje przychód z praw majątkowych. Czyli podatek dochodowy musi rozlic...

38. [Zagraniczny zakład jako serwer - skutki podatkowe](https://poradnikprzedsiebiorcy.pl/-zagraniczny-zaklad-jako-serwer-skutki-podatkowe) - Jeżeli przedsiębiorstwo wykonuje działalność w ten sposób, to zyski przedsiębiorstwa mogą być opodat...

39. [Are Your Server's Activities Creating a Taxable Presence ...](https://www.alvarezandmarsal.com/insights/server-permanent-establishment-are-your-servers-activities-creating-taxable-presence-you) - A foreign company's server constitutes a permanent establishment, or PE, for tax purposes, and the p...

40. [CHANGES TO THE COMMENTARY ON ARTICLE](https://www.rashminsanghvi.com/downloads/taxation/electronic_commerce/OECD_Report_Commentary_on_article_5.pdf) - The Committee wishes to stress that the changes included in this document deal exclusively with the ...

41. [When Does E-Commerce Result in a Permanent ...](https://www.robertsandholland.com/news-and-insights/when-does-e-commerce-result-in-a-permanent-establishment-the-oecds-initial-response/) - 1 Article 5 of the OECD Model Tax Convention provides that the “term 'permanent establishment' means...

42. [Serwery w Polsce mogą tworzyć zakład podatkowy ...](https://www.ey.com/pl_pl/insights/tax/podatki-miedzynarodowe/serwery-w-polsce-zaklad-podatkowy-zagranicznej-spolki) - Uznano, że serwery te, stanowiące istotny element podstawowej działalności spółki, spełniają kryteri...

43. [Wykaz umów o unikaniu podwójnego opodatkowania](https://www.podatki.gov.pl/podatkowa-wspolpraca-miedzynarodowa/wykaz-umow-o-unikaniu-podwojnego-opodatkowania/) - Tabela zawiera listę zawartych przez Polskę umów o unikaniu podwójnego opodatkowania. ... Niemcy. Um...

44. [Cryptocurrencies In Poland | Intertax](https://polishtax.com/cryptocurrencies-in-poland/) - In Poland, crypto trading and mining are legal, with profits taxed at a 19% rate (PIT-38) only when ...

45. [DAC-8: Jak rozliczyć kryptowaluty i uniknąć sankcji dzięki czynnemu ...](https://rpms.pl/dac-8-jak-rozliczyc-kryptowaluty-i-uniknac-sankcji-dzieki-czynnemu-zalowi/) - Jeszcze niedawno handel kryptowalutami uchodził za obszar względnej anonimowości. Transakcje na zagr...

46. [DAC8: nowe obowiązki podatkowe dla CASP w 2026](https://dudkowiak.pl/blog/dac8-nowe-obowiazki-podatkowe-dla-casp-od-2026-r-i-automatyczna-blokada-transakcji-po-60-dniach) - Poznaj DAC8: nowe obowiązki podatkowe dla CASP od 2026 roku i zasady automatycznej blokady transakcj...

47. [DAC8 - Fiskus dowie się o Twoich transakcjach krypto](https://kancelaria-skarbiec.pl/dac8/) - Nowelizacja ustawy o wymianie informacji podatkowych z innymi państwami

48. [Rozliczenie kryptowaluty w PIT-38: obowiązki, koszty i ...](https://kurdynowski.com.pl/rozliczenie-kryptowaluty-w-pit-38-obowiazki-koszty-i-przychody/) - Rozliczenie kryptowalut w PIT-38 to kluczowy element odpowiedzialnego inwestowania. Dowiedz się, jak...

49. [Jak samodzielnie rozliczyć podatek od kryptowalut w 2025?](https://kancelariamw.pl/jak-rozliczyc-podatek-od-kryptowalut/) - Podatek będzie zatem mniejszy, jeżeli będzie więcej kosztów. W koszty uzyskania przychodów z transak...

50. [Skutki podatkowe otrzymania nagrody w formie kryptowaluty - KIP](https://izbapodatkowa.pl/baza-wiedzy/skutki-podatkowe-otrzymania-nagrody-w-formie-kryptowaluty/) - Kryptowaluty spełniają definicję waluty wirtualnej, o której mowa w art. 5a pkt 33a ustawy o podatku...

51. [Wirtualny napiwek i opodatkowanie kryptowalut CIT ...](https://lexplorers.pl/opodatkowanie-kryptowalut-cit/) - Dyrektor KIS uznał stanowisko spółki za nieprawidłowe. Zdaniem organu otrzymanie waluty wirtualnej n...

52. [Korzystny wyrok dla branży kryptowalutowej. Pośrednicy ...](https://kancelaria-skarbiec.pl/korzystny-wyrok-dla-branzy-kryptowalutowej-posrednicy-nie-musza-placic-podatku-od-prowizji/) - W wyroku z 25 marca 2025 r. WSA w Gdańsku orzekł, że firmy oferujące wymianę kryptowalut nie muszą p...

53. [NSA: handel kryptowalutą opodatkowany. Nawet 32% podatku](https://www.pit.pl/aktualnosci/nsa-handel-kryptowaluta-opodatkowany-nawet-32-podatku-915262) - Zakup i sprzedaż kryptowalut stanowi transakcje na prawach majątkowych – uznał Naczelny Sąd Administ...

