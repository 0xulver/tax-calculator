Bottom line

For an own-account bot that liquidates DeFi positions and does DEX arbitrage using your own wallets and capital, the strongest current Polish reading is still PIT-38 / kapitały pieniężne, not JDG operating income, even if the activity is organized, continuous, automated, and very high-frequency. The reason is specific: the PIT Act keeps odpłatne zbycie walut wirtualnych in the crypto/capital-gains bucket even when connected with business activity, except for businesses that actually provide the AML-defined virtual-currency services. A November 2025 KIS interpretation on very active own-account crypto trading points the same way.

The biggest correction to your prior premise is this: Polish law does not tax only crypto→fiat. Taxable “odpłatne zbycie” also includes using crypto for a good, service, property right, or other obligation. So pure crypto↔crypto swap legs remain neutral, but gas, bridge fees, flash-loan fees, builder tips/private-orderflow fees, and similar amounts paid in crypto may themselves be taxable disposals. I did not find an open DeFi-specific ruling on gas, so that second sentence is a statutory inference rather than a settled KIS line.

1. Classification: PIT-38 or business income

Art. 5a pkt 6 PIT defines business broadly, but it gives way where the Act allocates a receipt to a different source. For virtual currencies, that specific rule is art. 17 ust. 1 pkt 11 plus ust. 1g. In practice, that means volume, automation, scripts, colocation, and 24/7 operation do not by themselves move own-account crypto disposals into PIT-36/PIT-36L. On the materials I reviewed, there is no practical transaction-count threshold where self-trading automatically flips into JDG income; the 2025 KIS ruling kept heavy own-account trading in PIT-38 despite organized, continuous activity.

So, on your facts, the default answer to question 1 is:

1a: most likely yes for the disposal side — own-account crypto trading reported in PIT-38 at 19%.

1b: the activity can be “business-like” in an economic sense, but that does not by itself move crypto disposals out of PIT-38 because of art. 17 ust. 1g.

1c: only if you actually enter the AML-listed virtual-currency service business does the exception move receipts into pozarolnicza działalność gospodarcza.

2. Does AML art. 2 ust. 1 pkt 12 catch liquidation/arbitrage bots?

The AML list is narrow. It covers businesses providing services of: exchange VC↔fiat, exchange VC↔VC, intermediation in those exchanges, and maintaining crypto accounts/wallet records. That is a service-to-others concept. A bot trading only the operator’s own assets is usually not providing exchange, brokerage, or wallet services to anyone else, so it usually does not fit the AML exception. If it did fit — for example, you were executing exchanges for clients, brokering deals, or operating a client-facing wallet/account service — then the activity would be a regulated virtual-currency business and art. 17 ust. 1g would move those receipts into business income.

A liquidation bot is, if anything, even less naturally an AML service than exchange brokerage: economically it is your own market operation against a protocol, not intermediation for a client. DEX arbitrage on your own wallets is the same. That conclusion is an inference from the statutory categories; among the open materials I reviewed, I did not find a published Polish interpretation specifically on Aave-style liquidation bots or MEV searcher bots.

If you ever did cross into the AML exception, the mechanics change materially: the crypto receipts stop being reported in PIT-38 and instead follow the business tax form for your chosen method of taxation, and entry in the register of virtual-currency business becomes mandatory before starting that service activity. On general rules or liniówka, ordinary business costs become potentially deductible; on ryczałt they still do not matter.

3. Existing JDG, PKD, ryczałt 12%, ZUS

If you wanted to record the activity inside the existing sole proprietorship, it would normally be done by amending the same CEIDG/JDG entry, not by creating a second sole proprietorship under your own name. On PKD 2025, the closest official own-account analogue is 64.99.Z, because the classification places own-account market activity in division 64, while division 66 is mainly for acting on behalf of others. PKD is only an administrative classification, though; it does not decide whether PIT goes to PIT-38 or business income.

Adding another line of activity does not by itself change the 12% ryczałt rate on your software-development revenue. The ryczałt rules require applying the proper rate to each revenue type and keeping records that separate them. What is not clear from the sources I reviewed is whether a hypothetical crypto-service line would itself be ryczałt-eligible and, if yes, at what rate. In any case, ryczałt is economically unattractive for bot trading because it ignores costs.

If the bot stays in PIT-38, nothing from those crypto disposals goes into PIT-28; PIT-28 remains for the software business. If the bot ever became actual JDG income, then the return would follow the business tax form instead.

On ZUS, if the bot activity really became JDG income, the issue is mainly the tax form and health/ZUS base, not a second separate entrepreneur title; official ZUS materials indicate multiple activities are generally settled together. If the crypto stays in PIT-38, the PIT-38 gains themselves do not create separate entrepreneur ZUS.

4. Crypto-to-crypto neutrality — and the gas/fee problem

Pure VC↔VC arbitrage remains neutral. The PIT Act and current MF guidance both say that exchanging one virtual currency for another is not taxed. So ETH→USDC, USDC→WBTC, or DEX-pool-to-DEX-pool swaps remain outside current income recognition so long as each leg is still virtual-currency↔virtual-currency.

But “no tax until EUR/PLN exit” is too broad. Tax also arises when crypto is used for a service or to settle another obligation. For bot operators, that creates a real issue for gas, bridge fees, flash-loan fees, and similar crypto-paid charges. So the swap legs may be neutral while the fee payments are not. That point follows directly from the statutory definition, even though published DeFi guidance is still thin.

The cost pool is also narrower than “all fiat ever put into the bot wallet.” Eligible PIT-38 costs are documented amounts directly spent to acquire virtual currency plus costs related to taxable disposal, with unused excess carried forward year to year. Borrowed funds, internal wallet transfers, bridge transfers, and the gross amount of a flash loan are not acquisition costs.

Functionally, this is an annual aggregate pool, not a statutory FIFO/per-coin-basis system. PIT-38 asks for annual revenue, current-year costs, carried costs, and unutilized costs, rather than token-by-token basis reporting.

5. Gas fees, flash-loan fees, server costs, bot-development costs

On deductibility, the conservative PIT-38 answer is restrictive. The statute excludes costs related to swapping one virtual currency for another, and MF guidance also excludes indirect costs such as financing costs. That makes gas on VC↔VC arbitrage, gas on bridge hops, and flash-loan fees poor PIT-38 cost candidates; failed-transaction gas is weaker still. The strongest PIT-38 fee-deduction case is a fee directly tied to a later taxable fiat sale or other taxable disposal.

The awkward result is that a fee paid in crypto may be a realization event, while still not being an easy PIT-38 cost if it belongs to a VC↔VC strategy. That is why the gas issue is not simply “deductible or not”; it is potentially both a realization problem and a cost-limitation problem.

Server hosting, cloud spend, monitoring subscriptions, hardware, and similar bot overhead are also weak PIT-38 costs, because the official rule is limited to direct acquisition costs and disposal-related costs, and MF guidance excludes comparable indirect items such as mining hardware and electricity. If the activity were ordinary business income on general rules, those items would usually reopen as business expenses; under ryczałt they still would not matter.

Your own coding time is not a tax cost. The PIT Act excludes the value of the taxpayer’s own work from deductible costs. External contractors or purchased tooling are different, but for PIT-38 they still remain too indirect in most cases.

6. Liquidation bonuses

This is the greyest point. I did not locate an open published Polish ruling directly on Aave/Compound/Morpho-style liquidation proceeds. The better taxpayer argument is that a liquidation is not a “free” receipt like an airdrop: you give value by repaying debt, usually with your own or flash-loaned crypto, and you receive collateral at a favorable protocol-set ratio. On that view, the whole event is closer to a VC↔VC exchange at a favorable price than to a gratuitous reward. If that analysis is accepted, the liquidation itself is neutral, later VC↔VC swaps of the received collateral remain neutral, and only the later fiat/service/obligation disposal is taxed.

The risk is that KIS has taken receipt-time positions for other reward-like crypto inflows such as staking and airdrops. Those rulings are not about liquidations, but they show the administration is willing to tax newly received crypto before disposal in some contexts. So “liquidation bonus taxed only on later disposal” is defensible, but not fully de-risked. This is the point where an individual ruling would add the most value.

If you want a precise answer to your question 20, the cleanest formulation is not really “zero cost basis” in FIFO terms. Under Polish PIT-38, the more accurate statement is: the 0.1 ETH bonus does not create a new direct acquisition expenditure in the cost pool. Later taxable disposal creates revenue; the cost side comes from the annual global pool of eligible acquisition/disposal costs, not from a token-specific tag.

7. Flash loans

I would not assume flash loans are automatically invisible. The safe economic view is that the borrowed principal should be argued as tax-neutral because it is borrowed and repaid in the same atomic transaction and there is no durable enrichment; the 2024 smart-contract interpretation is helpful by analogy because it rejected income where the automated mechanics did not produce real enrichment. But the statutory wording is awkward, because repaying a liability in crypto falls within “uregulowanie innych zobowiązań.” I did not find an open Polish ruling squarely on flash loans.

For the fee, the safer PIT-38 view is negative: by analogy to the MF exclusion for financing costs and to the 2024 smart-contract interpretation denying a protocol “stability fee” as a direct crypto cost, flash-loan fees are weak PIT-38 deductions when they support VC↔VC arbitrage. And if the fee is paid in crypto, it may itself be a disposal to a service/obligation.

8. Reporting 365,000 transactions on PIT-38

PIT-38 still works on annual aggregates, not line-by-line reporting. The return wants annual revenue from taxable disposals and annual eligible costs/carryforwards. The practical burden is evidentiary: you need a defensible ledger that classifies each on-chain flow as own-wallet transfer, VC↔VC swap, taxable disposal to fiat/service/obligation, borrowing/repayment, reward/bonus receipt, or fee. MF also confirms exchanges do not issue PIT-8C/PIT-11 for crypto, so the reconstruction burden is on you.

As a practical file, keep wallet and CEX exports, tx hashes, chain and block timestamps, protocol call traces, bank statements, invoices for hosting/tools, and a reconciliation workbook that shows how raw activity was converted into PIT-38 aggregates. Where amounts are denominated in foreign currency, the PIT Act uses the average NBP rate from the last business day before the revenue or cost. For purely crypto-valued gas/fee items, the statute does not give a DeFi-specific valuation method in the materials I reviewed, so consistency and archived pricing evidence matter.

9. Germany/Japan servers and PE risk

A Polish tax resident is taxed in Poland on worldwide income, subject to treaties. So simply running the bot on infrastructure in Germany, Japan, or elsewhere does not move the income out of Poland. Under both the Poland-Germany and Poland-Japan treaties, business profits are taxed only in the residence state unless there is a permanent establishment in the other state.

The hard PE question is the server. OECD treaty commentary says a website is not a PE, but a server can be if it is a fixed place at the enterprise’s disposal and performs core business functions; ordinary hosting on a third-party ISP’s server usually is not enough. Applied here: ordinary cloud/VPS hosting is usually low PE risk, while a dedicated server or colocated machine in Germany/Japan running the core trading engine is more arguable if, and only if, the activity is first recharacterized as business income. If the crypto remains in PIT-38 as own-account capital gains, foreign-server PE analysis becomes much less central.

The “location” of a smart contract or blockchain is not, by itself, a treaty nexus. Treaty allocation is built around persons, states, and fixed places of business, not around the chain on which the protocol code lives. That is an inference from the treaty/PE framework rather than an explicit DeFi rule.

10. Worked examples

Example 1: 10 ETH bought for 25,000 EUR; after 50,000 VC↔VC arbitrage trades the wallet holds 12 ETH + 500 USDC; later 500 USDC is sold for EUR. On the cleanest PIT-38 model, the swap legs themselves do not create PIT-38 revenue. The EUR sale of 500 USDC does. The cost side is not a unit basis for that 500 USDC; it is the annual crypto cost pool: documented acquisition costs and disposal costs from the year plus carryforward from prior years. If the 25,000 EUR acquisition spend is still in the pool, a small EUR sale can easily be fully absorbed by costs, with the unused balance carried forward. Nothing from the bot trades goes into PIT-28 if the bot stays in PIT-38; PIT-28 remains only for the software business. The caveat, again, is that gas and similar crypto-paid fees may create separate taxable disposals.

Example 2: the bot liquidates a position and gets a 0.1 ETH bonus; later ETH→USDC; later USDC→EUR on Kraken. The most defensible pro-taxpayer treatment is: liquidation event treated as neutral VC↔VC settlement; ETH→USDC still neutral; USDC→EUR creates PIT-38 revenue. The 0.1 ETH does not create a new direct acquisition cost merely because it was received; the cost side still comes from the global eligible cost pool. The risk is that KIS could analogize the bonus to other reward-like crypto receipts and argue for taxation at receipt, which is why liquidation bonuses are the least settled part of the structure.

11. What published Polish materials I actually found

The concrete open materials I found are:

KIS, 28 November 2025, 0113-KDIPT2-3.4011.709.2025.2.SJ — very active own-account crypto trading still treated as PIT-38 capital gains rather than business income.

KIS, 22 October 2024, 0115-KDIT1.4011.591.2024.2.MR — automated smart-contract / stablecoin mechanics; helpful for VC↔VC neutrality and for the restrictive view on protocol fees that are not direct acquisition/disposal costs.

Several 2024–2025 KIS rulings on airdrops/staking — useful only by analogy, because they support a receipt-time tax approach for reward-like crypto inflows.

Among the open materials I reviewed, I did not locate a published KIS interpretation or WSA/NSA judgment squarely on DeFi liquidation bots, flash-loan arbitrage, DEX arbitrage bots, or MEV searcher bots as of 19 March 2026.

12. Risk map

Lowest-risk filing position today: own-account bot trading stays in PIT-38; VC↔VC swap legs are neutral; direct acquisition costs carry forward; PIT-28 remains only for software income.

Medium-risk issue: treating liquidation bonuses as neutral until later disposal. The argument is good economically, but published Polish materials are not directly on point and KIS has been aggressive on reward-like receipts.

Higher-risk issue: ignoring gas/bridge/flash-loan fees completely. Statutorily, using crypto for services or to settle obligations is within taxable disposal, while deductibility of VC↔VC-related fees is narrow.

High-risk position: treating self-trading bots as AML art. 2 ust. 1 pkt 12 business without actually servicing third parties. The statutory AML categories and the 2025 KIS ruling point the other way.

The two places where an individual ruling would buy the most certainty are liquidation bonuses and crypto-paid fees (gas / flash / bridge / relayer).