# Tax Implications of Automated DeFi Liquidations and DEX Arbitrage Under a Polish JDG on Ryczałt

## Legal framework that actually controls the classification

Polish personal income tax rules for “virtual currencies” (waluty wirtualne) are built around a **special-source regime**: (i) what counts as *taxable disposal*, (ii) which **tax return** is used, and (iii) which **costs** may be recognized. Two provisions effectively dominate most of your questions:

Polish PIT law defines *“odpłatne zbycie waluty wirtualnej”* (taxable disposal of a virtual currency) narrowly as: exchanging a virtual currency for (a) a legal means of payment, (b) a good, (c) a service, (d) a property right other than a virtual currency, or settling other liabilities with a virtual currency. citeturn40view0turn16view0turn17view0

Polish PIT law also says that the rule taxing disposal of virtual currencies as **capital gains** (in practice, PIT-38 / 19%) applies **even if the income is obtained “within business activity”**, **except** for activity described in the AML Act’s Art. 2(1)(12) (the “crypto-service activity” catalogue). citeturn40view0turn17view0turn11view0

The “crypto-service activity” exception is defined in the AML Act as providing services in the scope of: (a) exchange between virtual currencies and means of payment, (b) exchange between virtual currencies, (c) intermediation in such exchange, and (d) keeping accounts (as referenced by the AML Act). citeturn11view0

**Why this matters for bots**: even if a bot operation is “organized and continuous” (which matches the statutory definition of business activity), the PIT Act hard-codes that **disposal-of-virtual-currency income remains in the PIT-38 bucket** unless the taxpayer is performing AML Art. 2(1)(12)-type services. citeturn13view0turn40view0turn17view0

## Classification of liquidation and arbitrage bots: capital gains vs business vs AML-crypto services

### How “business activity” (działalność gospodarcza) interacts with crypto disposal rules

Under the PIT Act’s definition, business activity is a gainful activity carried out in one’s own name, in an organized and continuous manner. citeturn13view0

A 24/7 automated strategy with dedicated infrastructure and systematic execution (liquidations/arbitrage/MEV) fits the **factual hallmarks** of “organized and continuous” activity. citeturn13view0

However, **the critical point** is that—even if the facts look “business-like”—the PIT Act’s Art. 17(1g) directs that income from disposal of virtual currencies remains treated like capital gains (PIT-38) also when obtained in the course of business, **unless** the activity is the AML Art. 2(1)(12) activity. citeturn40view0turn17view0

That is why Polish official guidance explicitly states that you file PIT-38 even if disposal/acquisition occurs “within business activity,” with the AML activity as the stated exception. citeturn17view0turn16view0

### Does running liquidation and arbitrage bots match the AML Art. 2(1)(12) exception

The AML catalogue (exchange, intermediation, account-keeping) is constructed as **service provision** (świadczenie usług). citeturn11view0

A bot that trades **only for the owner’s own account** (own wallets, own capital/flash liquidity, own PnL) usually does **not** look like “exchange service”, “intermediation”, or “account-keeping for others.” It resembles proprietary trading rather than a crypto-asset service provider. citeturn11view0turn17view0

So, under a plain-language and functional reading, liquidation/arbitrage bots run for your own benefit normally would **not** fall into AML Art. 2(1)(12). If they do not, the statutory default remains: PIT-38 treatment for disposal-of-virtual-currency income even if the activity is business-like. citeturn40view0turn17view0turn11view0

Where the AML exception risk becomes real is if the operator is effectively **providing exchange/intermediation services for third parties** (e.g., custodying client funds, executing swaps on behalf of clients, operating a platform that matches third-party orders, or taking fees as a service provider). That is the fact pattern the AML catalogue is designed to capture. citeturn11view0turn17view0

### Can the activity be “registered under the existing JDG” and what does that change

From a “tax bucket” perspective, **adding PKD codes or operationally running the bots within the same JDG does not override** Art. 17(1g) for virtual currency disposal: PIT-38 remains the reporting channel unless AML-type crypto services are performed. citeturn40view0turn17view0turn16view0

From a “ryczałt eligibility” perspective, a separate risk exists only if you begin performing activities that are **excluded from ryczałt**. The ryczałt act lists exclusions, including, among others, activity in buying/selling foreign exchange values (“wartości dewizowe”). citeturn21view0

There is also Polish case law that treated certain crypto trading/intermediation patterns as “other monetary intermediation” and therefore outside ryczałt in that case’s fact pattern. citeturn38view0

The practical synthesis:
- If your bot activity stays legally characterized as **virtual-currency disposal taxable under PIT-38**, it is typically **outside** the ryczałt base for your software-development JDG and does not by itself force a change of your 12% software rate. citeturn17view0turn16view0turn40view0  
- If instead you begin providing exchange/intermediation services (AML Art. 2(1)(12)-type activity), you are moving into a different regulated and tax-relevant category, which can create **both AML registration duties and potential ryczałt eligibility issues** depending on the exact activity classification. citeturn11view0turn21view0turn38view0

## Transaction characterization: liquidation bonus, arbitrage, flash loans, and the “crypto-to-crypto neutrality” rule

image_group{"layout":"carousel","aspect_ratio":"16:9","query":["Aave liquidation process diagram","Uniswap arbitrage diagram","flash loan diagram DeFi"],"num_per_query":1}

### Crypto-to-crypto trades and why many bot actions do not create PIT revenue immediately

Polish tax administration guidance states plainly that exchanging one virtual currency for another—whether via an exchange or individually—**is not taxed**. citeturn17view0turn16view0

This aligns with the statutory definition of “odpłatne zbycie waluty wirtualnej,” which is framed around exchange into legal tender, goods/services, non-crypto property rights, or paying liabilities—not around swapping virtual currency for virtual currency. citeturn40view0turn16view0

So, if your bot performs only:
- DEX swap A → token B, then token B → token C,
- cross-DEX arbitrage where both legs settle in tokens, and
- atomic liquidation flows that ultimately “round-trip” through tokens,

then in the **core PIT-38 virtual-currency disposal regime**, these steps typically do not create “przychód” (revenue) at the moment of swapping, because the taxable disposal definition is not met. citeturn40view0turn17view0

Two important caveats emerge from the statutory definition:
- Using virtual currency to **pay for a service or settle liabilities** is itself a taxable disposal, even without fiat (e.g., paying a contractor in stablecoins, paying a debt in crypto). citeturn40view0turn16view0  
- The tax system is triggered not only by “cash-out to PLN/EUR,” but also by crypto payment for goods/services and similar settlement events. citeturn40view0turn16view0turn17view0

### Liquidation bonuses: “free receipt” vs “service remuneration” vs “embedded exchange rate”

On-chain liquidations (e.g., on entity["company","Aave","defi lending protocol"], entity["company","Compound","defi lending protocol"], or similar lending protocols) economically look like: the liquidator provides repayment (often via flash liquidity) and receives collateral at a discount (“liquidation bonus”). This is structurally close to acquiring collateral tokens at a favorable exchange rate, not receiving a gratuitous transfer. citeturn17view0turn40view0

Under the PIT “virtual currency disposal” framing, one defensible characterization is:
- the liquidator’s “bonus” is part of the consideration embedded in the swap rate (repay token → receive collateral token),
- thus it is still within crypto-to-crypto flows, and
- tax would arise only when a later statutory disposal occurs (fiat cash-out, paying for services, etc.). citeturn40view0turn17view0

That said, Polish practice shows a live controversy for **crypto received without a standard purchase price** (airdrops, grants, certain “rewards”). A 2025 individual ruling (Dyrektor entity["organization","Krajowa Informacja Skarbowa","polish tax authority"]) treated receipt of virtual currencies in an airdrop/grant context as taxable **at receipt**, not at later disposal, and allowed the value recognized as income to be treated as the “cost of acquisition” for later PIT-38 disposal. citeturn37view0

This matters because if a liquidation bonus were re-framed as “remuneration for a service performed” (liquidating as a service), a similar “tax at receipt” logic could be argued by a tax authority. The counter-argument is that liquidations involve consideration and resemble an exchange mechanism rather than a gratuitous in-kind benefit. citeturn40view0turn17view0turn37view0

Given the novelty of DeFi liquidations in Polish practice, the safest statement is: **there is no clear, DeFi-liquidation-specific public line that fully resolves this**, but the statutory structure strongly supports treating liquidation legs as crypto-to-crypto mechanics unless a non-crypto consideration (goods/services/liabilities/legal tender) is involved. citeturn40view0turn17view0turn16view0

### Flash loans and MEV-style flows

From a cash-flow standpoint, flash loans are borrowed and repaid in the same atomic transaction. They are typically a “financing” component of a token-to-token strategy. The Polish tax administration’s public guidance explicitly excludes from crypto PIT-38 costs items “related to financing the purchase of virtual currencies (loan/credit costs).” citeturn17view0turn16view0

This makes it difficult to treat flash loan fees as deductible PIT-38 “crypto disposal” costs unless the fact pattern supports treating them as direct disposal costs within the meaning of the statute (which is not how the official guidance frames financing). citeturn17view0turn40view1

In practice, MEV and atomic arbitrage are still generally composed of:
- crypto-to-crypto exchanges (not immediately taxable as disposal), plus
- transaction fees and financing-like costs (with restrictive deductibility rules). citeturn40view0turn17view0

## Costs and deductibility: gas, failed tx, hosting, flash fees, and software development

### The statutory cost pool rules and what they allow

For virtual currency disposal under PIT-38, recognized tax costs are limited to:
- documented expenditures directly incurred to acquire virtual currency, and
- costs related to the disposal of virtual currency (including documented expenditures paid to entities described in AML Art. 2(1)(12)). citeturn40view1turn16view0

These costs are deducted in the year incurred; any excess over that year’s virtual-currency disposal revenue is carried forward to the next year’s virtual-currency disposal costs. citeturn40view1turn17view0turn16view0

Separately, the PIT statute contains an explicit exclusion: expenses incurred in connection with exchanging one virtual currency into another virtual currency are not treated as tax deductible costs. citeturn4view2turn17view0

This is the critical barrier for high-frequency bots whose “edge” is obtained via token-to-token activity and whose transaction cost profile is dominated by gas and DEX fees.

### Gas fees on arbitrage (crypto-to-crypto) and liquidation transactions

Official tax administration guidance states you cannot include in costs expenses “related to exchanging virtual currency into another virtual currency.” citeturn17view0turn4view2

In a DEX-to-DEX arbitrage comprised only of token swaps, most gas/DEX fees are tightly connected to token-to-token exchange steps; that makes them vulnerable to being treated as **non-deductible** under the explicit exclusion. citeturn17view0turn4view2

Liquidations are more nuanced:
- If the liquidation is treated as a token-to-token exchange (repay token → receive collateral token), gas is again connected to token exchange and likely falls into the same exclusion risk. citeturn40view0turn17view0turn4view2  
- If a particular leg constitutes “odpłatne zbycie” (e.g., you pay a service or settle a liability using virtual currency inside your strategy), the gas directly tied to that specific taxable disposal may fit better into “costs related to disposal,” but the official guidance still warns that token-to-token exchange costs are excluded. citeturn40view0turn40view1turn17view0

Failed or reverted transactions: the public guidance does not provide a special carve-out. If the failed transaction did not result in acquisition or taxable disposal, gas spent is difficult to map to “direct acquisition” or “disposal” costs and is therefore high risk as non-deductible under the strict “direct/disposing” concept. citeturn40view1turn17view0turn4view2

### Flash loan fees and other “financing-like” costs

Public guidance explicitly lists as non-allowable costs those related to financing (loans/credits). citeturn17view0turn16view0

A flash loan fee is economically a borrowing cost. Absent a more specific DeFi interpretation, it is difficult to defend as a PIT-38 crypto disposal cost under the “direct acquisition / disposal costs” framework, especially in light of the explicit financing exclusion in guidance. citeturn17view0turn40view1

### Server/cloud hosting and other indirect overhead

PIT-38 crypto costs are constrained to direct acquisition and disposal costs. Public guidance illustrates non-deductible items as those not directly connected to acquisition/sale of virtual currencies (the guidance uses mining hardware and electricity as examples). citeturn17view0turn40view1

A monthly hosting bill (e.g., from entity["company","Hetzner","hosting provider"] or entity["company","Amazon Web Services","cloud provider"]) is functionally an **indirect operating expense**, not a direct acquisition or disposal cost. Under the PIT-38 regime, it is therefore high risk to claim as a deductible crypto cost. citeturn40view1turn17view0

If—contrary to the usual proprietary-trading framing—you were in a fact pattern that is taxed as business income (e.g., AML Art. 2(1)(12)-type services), the deductibility analysis would switch away from the narrow PIT-38 cost pool and toward general business expense rules; however, your described bot operation (own-account trading) does not naturally fall into that AML exception. citeturn11view0turn40view0turn17view0

### Cost of developing the bot software inside the JDG

Under the PIT-38 virtual currency disposal regime, the “cost pool” is not designed to capture the opportunity cost of your labor or general development overhead; it is restricted to direct acquisition/disposal expenses. citeturn40view1turn17view0

So the “time spent coding the bot” is not a PIT-38 cost. If you incur actual cash expenses (contractors, licenses) and try to connect them to PIT-38, you face the same “directness” barrier. citeturn40view1turn17view0

If the bot were a separate business line taxed as business income (especially if it were an AML Art. 2(1)(12) activity), then software development costs could be treated as business expenses under the general rule-set; but again, the PIT Act’s design pushes own-account disposal of virtual currencies into PIT-38. citeturn40view0turn11view0turn17view0

## High-volume reporting and documentation for hundreds of thousands of transactions

PIT-38 reporting for virtual currencies is **annual and aggregated**. The official PIT-38 brochure for year 2025 explains that the “virtual currency” section is completed by taxpayers who earned disposal revenue, or incurred costs related to disposal, even when no disposal revenue occurred that year. citeturn16view0turn17view0turn14view0

The same guidance clarifies what counts as “odpłatne zbycie” (taxable disposal) and reiterates that costs are those defined by the statute, including costs paid to intermediaries (AML Art. 2(1)(12) entities). citeturn16view0turn40view0turn11view0

The tax administration also notes that crypto exchanges/intermediaries generally do not have a statutory duty to provide PIT information forms (like PIT‑8C) to taxpayers, which makes taxpayer-side documentation the practical backbone. citeturn17view0

For a bot executing 365,000 swaps/year, a defensible documentation posture typically requires being able to reconstruct:
- fiat on-ramps and off-ramps (bank transfers, exchange statements, confirmation emails),
- all taxable disposals (virtual → legal tender; virtual used to buy goods/services; debt settlement),
- the PLN valuation used for those disposals (in practice, consistent use of NBP FX for foreign currency amounts is referenced in KIS practice and guidance contexts), and
- the annual cost pool: direct acquisition costs and allowable disposal costs, with carry-forward of unused costs. citeturn40view1turn17view0turn16view0turn14view0

The law’s structure (aggregated costs, carry-forward, annual PIT-38 lines) is what makes “many transactions per day” reportable without listing each trade on the return—yet the auditability burden shifts to your own records. citeturn40view1turn16view0turn17view0

## Cross-border hosting and double tax treaty analysis: Germany/Japan servers and PE risk

### Poland’s starting point: worldwide income

Polish PIT law provides that individuals with a place of residence in Poland are subject to tax on the totality of their income regardless of where the source is located (unlimited tax liability). citeturn39view1

So the default is global taxation in Poland, with treaty relief mechanisms if another state has a taxing right. citeturn39view1turn14view0

### When Germany or Japan could have a taxing right: business profits + permanent establishment

Under the Poland–Germany DTT, business profits are taxable only in the residence state unless the enterprise carries on business in the other state through a “zakład” (permanent establishment), in which case the other state may tax the profits attributable to that PE. citeturn29view2

The treaty defines “zakład” as a fixed place of business through which the business is wholly or partly carried on. citeturn29view0turn29view2

Under the Poland–Japan DTT text provided by the Polish government, the same core structure appears: Article 7 allocates “zyski przedsiębiorstwa” (business profits) primarily to the residence state unless there is a “zakład,” and Article 5 defines “zakład” similarly as a fixed place through which business is carried on. citeturn31view1turn31view2

### Does a foreign server create a “zakład” for a bot operator

Treaties do not explicitly name “servers,” so interpretation leans on OECD commentary practice. The OECD Model Tax Convention commentary has long discussed that:
- a **website** alone is not tangible property and does not by itself create a PE, but
- if the enterprise has a **server at its own disposal** (e.g., owns/leases and operates the server where the website is stored and used), the place where the server is located could constitute a PE if other conditions are met. citeturn32search0turn32search7

Applying that to server location:
- A dedicated server in Germany leased and operated in a manner that is central to the trading operation is a non-zero PE risk factor under OECD-style analysis, because “server at disposal” is a recognized pathway for PE. citeturn32search0turn29view0turn29view2  
- Pure cloud usage (elastic instances where you do not have a specific server “at your disposal” in the OECD sense) is generally closer to the “hosting arrangement” that does not itself constitute a PE. citeturn32search0turn32search7

Because your bot is run by an individual Polish tax resident (not a multinational group), and because the “source state” would still need a treaty-recognized PE to tax business profits, the practical PE risk is usually driven by: (i) how fixed and exclusive the foreign infrastructure is, (ii) whether it is a core business location rather than preparatory/auxiliary, and (iii) whether the activity is even taxed as “business profits” rather than PIT-38 capital gains. citeturn29view0turn29view2turn32search0turn40view0

### Does “smart contract location” matter

Neither the PIT statute’s taxable-disposal definition nor the DTT concept of PE relies on “where a smart contract lives.” They hinge on taxpayer residence, the existence of a fixed place of business, and the legal characterization of the income stream. A DeFi protocol’s deployment on a blockchain is not, by itself, a physical place of business under treaty definitions. citeturn29view0turn31view1turn39view1turn40view0

## Practical reporting walkthroughs under PIT-38 and interaction with a ryczałt JDG

### Example: pure crypto-to-crypto arbitrage year, then partial cash-out

Assume:
- Start capital: 10 ETH bought for 25,000 EUR (documented).
- During the year: 50,000 arbitrage trades, all token-to-token.
- End holdings: 12 ETH + 500 USDC.
- Cash-out: convert 500 USDC to EUR on entity["company","Kraken","crypto exchange"], then withdraw EUR.

Under the Polish statutory definition, the 50,000 token-to-token swaps do not inherently create “odpłatne zbycie” revenue (absent paying for goods/services or settling liabilities with crypto). citeturn40view0turn17view0

The taxable event occurs at the moment of exchanging virtual currency to legal tender (USDC → EUR if treated as virtual-to-fiat). This falls squarely within the statutory disposal definition used in PIT-38 reporting. citeturn40view0turn16view0turn17view0

What goes on PIT-38:
- In the “virtual currencies” section, you report the **sum of disposal revenues** for the year (here: EUR proceeds converted to PLN).
- You report allowable costs: (a) acquisition costs of virtual currencies incurred in the year, plus (b) allowable disposal costs, plus (c) carried-forward costs from prior years; unused costs carry forward again. citeturn40view1turn16view0turn17view0turn14view0

What does *not* go on PIT-28 (ryczałt return for the software JDG):
- Your proprietary trading disposal income is directed by statute into PIT-38 even if done “within business,” unless you are performing AML Art. 2(1)(12) services. citeturn40view0turn17view0  
- Your software development revenue remains reported under the ryczałt regime; PIT-38 virtual currency disposal is a separate reporting channel by design. citeturn17view0turn16view0

Documentation needed:
- Bank transfer and exchange statement proving the initial ETH purchase (basis for “direct acquisition cost”). citeturn40view1turn17view0
- Exchange trade confirmation for the USDC→EUR disposal (basis for revenue and disposal fee cost). citeturn40view0turn40view1turn16view0
- An internal ledger (or exported trade logs + blockchain tx mapping) sufficient to support the annual totals and prove which fees are disposal fees vs token-to-token swap costs (given the explicit exclusion for token-to-token swap costs). citeturn17view0turn4view2turn16view0

### Example: DeFi liquidation bonus, then swaps, then fiat cash-out

Assume:
- A liquidation executes and leaves you with +0.1 ETH “bonus” net.
- Later, ETH → USDC (token-to-token).
- Later, USDC → EUR on a centralized exchange.

If the liquidation is treated as an exchange mechanism (repay token → receive collateral token) and the “bonus” is simply the embedded discount, then the acquisition of the extra ETH is part of token-to-token flows and is not a taxable disposal event. citeturn40view0turn17view0

The later ETH → USDC remains token-to-token, also not a taxable disposal event in itself. citeturn17view0turn40view0

The taxable event occurs when USDC is exchanged to EUR (legal tender), which is “odpłatne zbycie” under the statutory definition. citeturn40view0turn16view0

Cost basis implications under the Polish cost-pool method:
- PIT-38 costs are pooled and carried forward; you do not report FIFO lot-by-lot matching for each token in the statute’s crypto cost mechanism. The statute describes annual cost deduction with carry-forward of excess rather than per-asset FIFO. citeturn40view1turn16view0turn17view0
- If the liquidation profit tokens are obtained in a way that the tax authority re-characterizes as “income at receipt” (like some airdrop/grant interpretations), then the published KIS approach is to tax at receipt but also allow the recognized value to become the acquisition cost for later disposal. citeturn37view0  
- Your liquidation fact pattern is arguably more “exchange-like” than “free receipt,” but a conservative risk view acknowledges that “token reward” interpretations exist and may be raised by analogy. citeturn37view0turn40view0

## What is known from KIS interpretations and court rulings about bots, arbitrage, and “rewards”

### KIS / administrative practice signals that matter for bot operators

A publicly available 2025 PIT interpretation involving a taxpayer on ryczałt with software PKD codes treated receipt of virtual currencies via airdrops/grants as taxable at the moment of receipt (not only at later disposal), while allowing that value to be treated as a crypto acquisition cost for later PIT-38 disposal. citeturn37view0

This is directly relevant to your “liquidation bonus” question because it shows **the interpretive path** under which “crypto received” can be treated as current income even before a fiat disposal, depending on why it is received and whether it is framed as a benefit in kind or remuneration. citeturn37view0

At the same time, Polish administrative and judicial outputs have recognized that crypto-related income-recognition can depend on valuation mechanics and on whether there is an objectively measurable “real economic benefit” at a given moment. For example, a 2025 WSA judgment (in a corporate-tax context) addressed the timing of taxation of crypto commissions and treated taxation as occurring upon later disposal when value becomes measurable in a way required for taxation. citeturn24search3turn24search20

These materials are not DeFi-liquidation-specific, but they show the contours of the dispute: **tax at receipt** (some KIS interpretations) vs **tax only at realization/disposal** (some court reasoning in crypto-value contexts). citeturn37view0turn24search3turn24search20

### High-frequency “looks like business” vs statutory assignment to PIT-38

Polish official guidance states that you file PIT-38 for virtual currency disposals even if the trades occur in the course of business, with the AML Art. 2(1)(12) activity as the stated exception. citeturn17view0turn16view0turn40view0

That means there is not a clear “transaction count threshold” in the law that flips PIT-38 into PIT-36/PIT-36L for ordinary proprietary trading disposals. The statute already anticipates “business activity involvement” and still routes the income to the PIT-38 regime (again, unless AML services). citeturn40view0turn17view0

### PKD/ryczałt litigation signals for crypto intermediation

There is an NSA judgment (2022) addressing crypto trade/intermediation classification in a way that led to exclusion from ryczałt in that fact pattern, emphasizing a classification as “other monetary intermediation.” citeturn38view0

This is most relevant where the activity resembles exchange/intermediation services, not where the activity is purely own-account token trading already routed to PIT-38 by Art. 17(1g). citeturn38view0turn40view0

## Risk assessment synthesis by approach

Treating bot activity as PIT-38 “virtual currency disposal” with crypto-to-crypto neutrality is strongly aligned with:
- the statutory definition of taxable disposal (which does not list token-to-token swaps), citeturn40view0turn16view0  
- official tax administration guidance on token-to-token neutrality, citeturn17view0turn16view0  
- and the statutory rule that routes virtual-currency-disposal income to PIT-38 even when arising in business (except AML activity). citeturn40view0turn17view0

Its main weaknesses are cost-related: the explicit exclusion of swap-related costs, plus the narrow “direct acquisition / disposal” cost regime, makes gas-heavy strategies potentially taxable on a base that does not reflect economic profit. citeturn17view0turn4view2turn40view1

Recharacterizing bot profits as business income under JDG rules would face the statutory barrier of Art. 17(1g): even if activity is business-like, pure disposal revenue is still treated under PIT-38, unless the activity is the AML Art. 2(1)(12) service catalogue. citeturn40view0turn11view0turn17view0

Attempting to fit the activity into the AML Art. 2(1)(12) exception is high-risk unless the factual reality involves providing exchange/intermediation/account services to others (i.e., a service provider model). That path also carries regulatory burdens (AML registration regime) and can affect ryczałt eligibility depending on activity classification. citeturn11view0turn21view0turn38view0

For multi-jurisdiction hosting, the main tax risk channel is permanent establishment if the activity were treated as business profits and if the foreign server is “at disposal” of the enterprise as contemplated in OECD commentary. Typical cloud hosting reduces (does not eliminate) that pathway, while dedicated server patterns can increase it. citeturn32search0turn29view0turn29view2turn31view1turn31view2