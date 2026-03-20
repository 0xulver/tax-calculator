# Tax Treatment of DeFi, Staking, and Airdrops in Poland

## Scope, assumptions, and why the answer is not one-size-fits-all

This report addresses Polish personal income tax treatment (PIT) for an individual taxpayer (natural person) engaging in crypto activities including staking (exchange and on-chain), “earn”/lending programs, airdrops, DeFi interactions (including lending/LP positions), crowdloans, forced token conversions by exchanges, and chain migrations such as the Terra/LUNA → LUNA2 transition. It is written as of **2026-03-19** (Europe/Warsaw) and focuses on Polish rules for **“waluty wirtualne”** (virtual currencies) and related interpretations by **entity["organization","Krajowa Informacja Skarbowa","tax information office, Poland"]** and court case trends where available. citeturn27view0turn18view0turn14view0turn16search6turn8search10

A key reason the answer is not uniform is that (a) Polish statute-by-statute crypto rules focus heavily on **taxation at “odpłatne zbycie” (paid disposal)**, while (b) many individual interpretations from **entity["organization","Krajowa Informacja Skarbowa","tax information office, Poland"]** have attempted to tax certain “free” crypto inflows (staking rewards / airdrops) **upon receipt** by classifying them as **income from “prawa majątkowe” (property rights)** under Art. 18 PIT, which has been challenged in administrative courts. citeturn19view0turn16search6turn14view0turn8search10

Because the user asked for a classification that includes “receipt vs disposal,” this report presents **two parallel tracks** where the law/practice is currently disputed:
- **Track A (KIS-restrictive / conservative)**: receipt of rewards/airdrops can be taxable as property-rights income.
- **Track B (disposal-only / litigation-aligned)**: receipt is not taxable; tax arises only upon paid disposal under the crypto regime.

## Baseline Polish PIT framework for “waluty wirtualne” and why it matters for DeFi

### Core statutory model for “waluty wirtualne”: tax at paid disposal, not at internal crypto movement

Polish PIT guidance for crypto disposals (as reflected in official tax portal explanations for PIT-38) treats income from virtual currencies primarily as arising **when a virtual currency is disposed of for consideration** (paid disposal), i.e., when it is exchanged:
- for legal tender (fiat),
- for goods,
- for services,
- for a property right other than a virtual currency,
- or used to settle other liabilities. citeturn27view0turn18view0

This definition is critical for DeFi, because many on-chain actions are **crypto-to-crypto** (swaps, wrapping, LP tokens, receipt tokens), and—at least at the level of the “crypto disposal” regime—Polish practice repeatedly states that **exchange between virtual currencies is tax-neutral**. citeturn22view1turn19view0turn27view0

### Reporting form for “odpłatne zbycie walut wirtualnych”: PIT-38

The official PIT-38 instructions explicitly state that a taxpayer must file PIT-38 if they had **revenue from paid disposal of virtual currencies** or if they **incurred acquisition costs** for virtual currencies even when no disposal revenue occurred that year. citeturn27view0

The PIT-38 guidance also states the **tax rate is 19%** for virtual-currency disposal and explains that deductible costs for the crypto regime are the **documented expenses directly incurred to acquire** virtual currency plus **documented costs connected with its disposal** (e.g., intermediary fees). citeturn27view0turn22view1

### Cost mechanics in the crypto regime look more like “cost pooling” than FIFO lots

The crypto regime defines annual crypto income as the **difference between the sum of disposal revenues and the costs defined in Art. 22 ust. 14–16**. citeturn22view1  
Separately, official PIT-38 guidance emphasizes that if costs exceed revenues, “unused costs” can be carried into later years rather than being treated as an immediately deductible “loss” in the usual sense. citeturn27view0turn22view1

This matters for your FIFO questions: while private tools commonly compute per-lot gains, Polish crypto reporting is often operationalized as yearly totals (revenues and pooled costs), with carryforward of unused costs. citeturn22view1turn27view0

### PLN valuation rule you will keep revisiting

For amounts denominated in foreign currency, PIT-38 guidance requires conversion to PLN using the average exchange rate of **entity["organization","Narodowy Bank Polski","central bank, Poland"]** from the last business day preceding the day income is obtained. citeturn27view0  
For crypto-denominated receipts taxed “at receipt” (Track A), valuations hinge on “market value at the time and place of receipt” logic used by KIS in individual interpretations. citeturn19view0turn18view0

## Classification matrix for the user’s activities

The table below summarizes the two-track reality where relevant. “Track A” reflects a conservative approach consistent with multiple KIS interpretations; “Track B” reflects the disposal-only reading commonly advanced by taxpayers and supported in several administrative court outcomes that set aside KIS interpretations in staking disputes.

| Activity type | Track A (KIS-restrictive) – when taxable | Track B (disposal-only / litigation-aligned) – when taxable | Typical PIT form(s) | Cost basis concept used in practice |
|---|---|---|---|---|
| Staking rewards (exchange staking, solo staking, liquid staking rewards) | **Taxable at receipt** as income from “prawa majątkowe” (Art. 18 in connection with Art. 11) in multiple KIS lines (valuation at market value). citeturn19view0turn25search0 | **Taxable only upon paid disposal** of the rewarded tokens (i.e., when exchanged for fiat/goods/services/other rights). Courts have set aside KIS staking interpretations (e.g., WSA Wrocław 2023; WSA Warsaw 2024), and press reports summarize the disposal-only conclusion. citeturn14view0turn16search6turn8search10turn9search21 | Track A: PIT-36 (scale-tax return) is the practical consequence of Art. 18 classification; Track B: PIT-38 under the crypto regime upon disposal. citeturn21view0turn19view0turn27view0 | Track A: receipt value becomes “entry value” and is later treated as deductible cost for crypto disposal (to avoid double tax) in KIS staking interpretations. citeturn25search0 Track B: no acquisition expense → typically **0** cost for the rewarded units (except disposal fees). citeturn27view0turn22view1 |
| Earn/lending rewards (centralized “earn”, lending-like yield) | Typically analogized to staking in KIS-style reasoning: taxable at receipt if treated as a “reward”/benefit received in crypto; valuation at receipt. citeturn19view0turn25search0 | If treated as “virtual currency acquisition without paid disposal,” then no tax until disposal of the received tokens. citeturn27view0turn9search21 | Same bifurcation (PIT-36 vs PIT-38) depending on classification logic. citeturn21view0turn27view0turn19view0 | Same bifurcation (receipt value becomes later cost vs cost 0 for “free” tokens). citeturn25search0turn27view0 |
| Airdrops (including exchange-distributed airdrops) | Some KIS interpretations explicitly treat airdrop receipt as taxable at receipt (Art. 11 valuation; property-rights framing). citeturn19view0 | There are also interpretations and commentary indicating a disposal-only approach for “free” tokens in certain fact patterns (income only when sold). citeturn8search21turn9search21 | Track A: PIT-36; Track B: PIT-38 upon disposal. citeturn21view0turn27view0turn19view0 | Track A: receipt value treated as later cost (if recognized as income at receipt); Track B: cost 0 (except disposal fees). citeturn25search0turn27view0 |
| DeFi swaps, wrapping, LP tokens, receipt tokens (crypto→crypto) | Generally **not taxed at the moment of crypto-to-crypto exchange** in the crypto regime; KIS materials describe crypto-to-crypto exchange as tax-neutral. citeturn22view1turn19view0 | Same. citeturn22view1turn27view0 | PIT-38 impacts arise only when paid disposal happens (fiat/goods/services/other rights). citeturn27view0 | Polish rules also say expenses related to **crypto-to-crypto exchange** are not deductible costs (Art. 23 ust. 1 pkt 38d as cited in interpretations). citeturn22view1turn19view0 |
| Crowdloans (KSM/DOT locked and returned; project tokens distributed) | Lock/return: typically no paid disposal (so not taxed at lock/return). Reward tokens: often analyzable as “airdrop-like”/reward receipt → potentially taxable at receipt under KIS-type logic. citeturn27view0turn19view0 | Lock/return: no tax. Reward tokens: potentially taxable only upon disposal under disposal-only theory. citeturn27view0turn9search21 | Same bifurcation (PIT-36 if receipt-taxed; PIT-38 if disposal-only). citeturn21view0turn27view0turn19view0 | Same bifurcation (receipt value later cost vs cost 0). citeturn25search0turn27view0 |
| Forced stablecoin conversions by an exchange (e.g., BUSD→FDUSD→USDC) | Generally treated as **virtual-currency-to-virtual-currency exchange** → tax-neutral at conversion moment. citeturn22view1turn19view0 | Same. citeturn22view1turn27view0 | PIT-38 only when later disposed for fiat/goods/services/other rights. citeturn27view0 | Fees on crypto-to-crypto exchange are generally not deductible under Art. 23(38d) approach cited in interpretations (if any fees were charged). citeturn22view1turn19view0 |
| Terra/LUNA “collapse” and LUNA→LUNA2 distribution | LUNA2 receipt may be treated like an airdrop/reward (potential receipt-tax risk) under restrictive logic. citeturn19view0 | Alternatively treated as non-taxable until disposal. citeturn9search21turn27view0 | PIT-36 risk (receipt-tax view) vs PIT-38 (disposal-only). citeturn21view0turn27view0turn19view0 | Same cost basis bifurcation; old LUNA acquisition costs remain within the crypto cost pool mechanics. citeturn22view1turn27view0 |

## Staking rewards and earn/lending programs

### Question 1: Is a DOT staking reward received on an exchange taxable at receipt, a new acquisition with zero basis, or not taxable until fiat?

**Track A (KIS-restrictive / conservative)**: KIS has treated crypto rewards from staking as **taxable upon receipt**, arguing they constitute income from “prawa majątkowe” (property rights) and must be valued at market value at the time and place of receipt. This position appears in an interpretation that covers both staking and airdrops (and explicitly states that, because crypto is treated as property rights, receipt creates Art. 18 income). citeturn19view0turn18view0  
In a separate staking-focused interpretation (Lido/solo staking), the same conclusion is summarized: rewards are Art. 18 income at receipt, valued at market value. citeturn25search0turn23search1

**Track B (disposal-only / litigation-aligned)**: Courts have set aside KIS staking interpretations, and press coverage of the WSA Wrocław ruling reports that a staking “reward” should be treated as taxable **only when the received crypto is sold** (i.e., when paid disposal occurs). citeturn14view0turn8search10turn16search6turn9search21  
Under this approach, receipt itself is not a taxable event; the taxpoint is aligned to the statutory disposal concept used for PIT-38 crypto reporting. citeturn27view0

**Answer to 1(a)/(b)/(c)**: In practice, Poland currently has a real split: Track A corresponds most to (a) “taxable at receipt”; Track B corresponds most to (b)/(c) in the sense that receipt is not taxed, and the rewarded crypto behaves like a “new acquisition” whose tax relevance appears at disposal (with a cost basis question discussed below). citeturn19view0turn27view0turn8search10

### Question 2: Does “nabycie walut wirtualnych” include receiving staking rewards?

The phrase that matters in the crypto regime is not “nabycie” in the abstract but **“udokumentowane wydatki… poniesione na nabycie waluty wirtualnej”** (documented expenses incurred to acquire a virtual currency). Official PIT-38 guidance and KIS materials emphasize that crypto-regime costs are built around **expenditures** directly incurred to acquire virtual currency and costs of paid disposal. citeturn27view0turn22view1

A staking reward is clearly an **acquisition of units** in an economic sense, but it usually involves **no “wydatki poniesione”** (no direct acquisition spend) by the recipient for the rewarded units themselves. Under a disposal-only reading, this is why practitioners often assign **zero acquisition cost** to the rewarded units (subject to disposal fees). citeturn27view0turn22view1

Under the receipt-tax (Track A) approach, KIS effectively treats staking reward receipt as a taxable inflow under Art. 11/Art. 18, and then (in other interpretations) allows the receipt value to be treated as a later cost when those rewarded units are disposed. citeturn19view0turn25search0

### Question 3: If staking rewards are taxed at receipt, PIT-38 or PIT-36?

If staking is taxed at receipt as **income from “prawa majątkowe” (Art. 18 PIT)** per KIS logic, it falls into the personal-income reporting track that is not PIT-38 crypto disposal. The official PIT-36 guidance discusses “dochody z praw autorskich i innych praw” within PIT-36 and presents Art. 18 “prawa majątkowe” as a PIT-36-type category. citeturn21view0turn19view0

Meanwhile, PIT-38 is explicitly positioned (in official guidance) as the form for **paid disposal of virtual currencies** and the associated crypto acquisition/disposal costs under Art. 22 ust. 14. citeturn27view0

So, in the KIS receipt-tax model, the reporting pattern becomes:
- receipt: PIT-36 (scale taxation track),
- later sale/disposal: PIT-38 (crypto disposal track). citeturn19view0turn27view0turn21view0

### Question 4: If not taxed at receipt, what is the cost basis when staking reward tokens are eventually sold?

If there is no tax at receipt and the rewarded tokens were obtained without a direct acquisition expenditure, the crypto regime’s cost definition (“documented expenses directly incurred to acquire”) often yields a **cost basis of 0** for those particular units, with only disposal-related costs (e.g., exchange selling fees) potentially deductible. citeturn27view0turn22view1

This is exactly why the receipt-tax approach matters: KIS interpretations acknowledge a mechanism where the receipt value (taxed at receipt as Art. 18 income) can be used as a later deductible cost when disposing of the rewarded units, mitigating double taxation. citeturn25search0

### Question 5: Liquid staking tokens (e.g., stETH-like receipt tokens) – is receiving them in exchange for underlying a taxable event?

A liquid staking action that economically looks like **virtual currency A → virtual currency B** is generally treated (in the crypto disposal regime) as **tax-neutral at the point of the exchange**, because KIS materials describe exchange between virtual currencies as neutral for PIT. citeturn22view1turn19view0

However, KIS materials also emphasize that **expenses related to exchanging one virtual currency for another** are not treated as deductible costs (Art. 23 ust. 1 pkt 38d is cited in the staking/airdrop interpretation). citeturn22view1turn19view0

So the most defensible “default” classification for liquid staking receipt tokens (assuming they qualify as “waluta wirtualna”) is:
- **Receipt of the liquid staking token**: no immediate PIT from the exchange itself (crypto-to-crypto neutrality),
- **Ongoing staking rewards paid in additional tokens**: disputed (receipt-tax vs disposal-only), as described above. citeturn22view1turn19view0turn8search10

## Airdrops

### Question 6: How are airdrops classified under Polish law?

There is no single, universally settled statutory “airdrop rule” in PIT-38 guidance. In practice, airdrops are treated through one of two lenses:

- **KIS receipt-tax lens**: treat received airdrop tokens as a taxable benefit (income) upon receipt and value them under Art. 11 valuation concepts, with KIS explicitly grouping airdrops with other “primary acquisition” events and concluding receipt generates income. citeturn19view0turn18view0  
- **Disposal-only lens**: treat airdrop receipt as non-taxable until a paid disposal occurs under the crypto regime. This view appears in some interpretive materials indicating that receipt itself does not create PIT income and that tax arises when the tokens are sold. citeturn8search21turn9search21turn27view0

A relevant “side” point: a KIS interpretation on inheritance/donation tax concluded that airdrops are not taxed under the gift tax regime as a “darowizna” (gift), even while discussing virtual currencies as “prawa majątkowe” in that context; it also notes PIT would be analyzed separately. citeturn17search2

### Question 7: If an airdrop token has value at receipt, is receipt itself taxable?

**Under Track A**, yes: KIS states that already at the moment of receiving staking and airdrop rewards, income arises “in the amount of the value of the received cryptocurrencies,” valued using market prices at the time and place of receipt. citeturn19view0turn18view0

**Under Track B**, no: tax would arise only at paid disposal (e.g., sale for fiat). citeturn9search21turn27view0

### Question 8–9: Worthless airdrops, zero basis, and full proceeds as gain

If a token truly has no determinable market value at receipt, Track A’s framework still conceptually requires valuation, but the taxable amount in PLN could be effectively **0** if there is no market price to apply (the interpretation relies on market-price valuation logic). citeturn19view0

On disposal-only logic, there is no receipt tax; when you later sell, the proceeds are taxable under PIT-38’s paid-disposal rules. citeturn27view0

For **cost basis**: if the airdropped token was acquired without direct acquisition expenditure, the PIT-38 cost definition (“documented expenses directly incurred to acquire”) leads to **0 acquisition cost** for the token itself (again, subject to disposal fees), which implies that if you later sell it for fiat, the proceeds are effectively taxable gain (net of allowable disposal costs). citeturn27view0turn22view1  
If the token was taxed at receipt (Track A), the receipt value is typically treated as the later “cost” to avoid double taxation under the KIS approach used in staking interpretations. citeturn25search0

## DeFi and crowdloans

### Question 10: Earn/lending rewards (Kraken Earn / Binance Simple Earn) – receipt vs disposal and reporting form

Polish official PIT-38 guidance focuses on **paid disposal** of virtual currencies (fiat/goods/services/other rights), and KIS materials restate that crypto-to-crypto exchange is neutral. citeturn27view0turn22view1

Where an “earn” program pays periodic rewards in tokens, the legal uncertainty mirrors staking:
- KIS-style reasoning taxes the inflow on receipt as a benefit valued at market price; KIS has applied this to crypto reward scenarios. citeturn19view0turn25search0
- Courts and disposal-only commenters treat receipt as non-taxable and focus on disposal events. citeturn9search21turn8search10

So the form/basis logic is the same as staking:
- receipt-tax view → PIT-36 at receipt; later PIT-38 on disposal minus cost equal to receipt value, consistent with the KIS approach in staking interpretations. citeturn21view0turn25search0turn27view0
- disposal-only view → PIT-38 on disposal; “free” rewarded units typically have 0 acquisition cost. citeturn27view0turn22view1

### Question 11: Kusama/Polkadot crowdloans – locking KSM, reward tokens, return of KSM

There is limited directly-on-point official PIT guidance specifically naming “crowdloans” in the sources reviewed. A crowdloan has three components that map reasonably cleanly onto the statutory disposal concept:

1) **Locking KSM** (or DOT) into a protocol mechanism with later return: this does not obviously match the PIT-38 “paid disposal” definition (no exchange for fiat/goods/services/other rights at that moment). citeturn27view0  

2) **Receiving project tokens** as a “reward”: this can resemble an airdrop or staking reward. KIS has explicitly treated airdrop/staking rewards as taxable on receipt under Art. 11/Art. 18 logic in at least one interpretation. citeturn19view0  
Under the opposite approach, tax arises when those project tokens are later disposed of in a paid disposal transaction. citeturn27view0turn9search21  

3) **KSM returned** after the lease period: returning the same virtual currency without exchanging it for fiat/goods/services/other rights does not look like a paid disposal. citeturn27view0

Because the crowdloan reward token is typically a distinct asset, the cost basis logic again follows the same forks:
- receipt-tax: receipt valuation becomes later cost (KIS pattern in staking). citeturn25search0  
- disposal-only: no acquisition expense → cost 0 for the reward tokens (subject to disposal fees). citeturn27view0turn22view1

## Token swaps, redenominations, and forced conversions

### Question 12: Terra collapse – receiving LUNA2, cost basis, and old LUNA in “FIFO”

**Receiving LUNA2** after an ecosystem migration/snapshot is economically similar to an airdrop-like distribution: you receive new tokens based on prior holdings. Under the KIS approach to airdrops/staking rewards, receipt of such tokens can be treated as taxable income at receipt (market value at time/place). citeturn19view0  
Under the disposal-only approach, receipt itself is not taxed; taxation occurs when you dispose of the received tokens in a paid disposal transaction. citeturn27view0turn9search21

**Cost basis of LUNA2** then follows the same fork:
- receipt-tax: receipt valuation becomes later disposal cost (KIS pattern). citeturn25search0  
- disposal-only: no direct acquisition expenditure → cost 0 (except disposal fees). citeturn27view0turn22view1

**What happens to old LUNA in FIFO?** Polish PIT-38 crypto mechanics are not framed as a statutory FIFO lot regime in official guidance; instead they are expressed as annual totals: income is the difference between the sum of paid-disposal revenues and the pool of deductible acquisition/disposal costs defined in Art. 22 ust. 14–16, with carryforward of unused costs rather than ordinary “loss” settlement. citeturn22view1turn27view0  
So “FIFO” is typically a software/accounting convention rather than a Polish statutory mandate; the critical Polish point is whether the taxpayer can substantiate their aggregate costs and disposal revenues. citeturn27view0turn22view1

### Question 13: Forced stablecoin conversions (BUSD→FDUSD→USDC) – taxable events and basis transfer

KIS materials explicitly state that **exchange between virtual currencies is tax-neutral**, regardless of where conducted. citeturn22view1turn19view0  
Therefore, a forced conversion of one stablecoin into another stablecoin (virtual currency → virtual currency) is typically analyzed as **not creating paid-disposal revenue** at the moment of the conversion, assuming both assets qualify as “waluta wirtualna.” citeturn22view1turn27view0

On costs: KIS cites the rule that expenses “connected with exchanging a virtual currency into another virtual currency” are not included as deductible costs (Art. 23 ust. 1 pkt 38d). citeturn22view1turn19view0  
In practice, the “basis transfer” question is often handled by cost pooling: the original acquisition costs remain part of the crypto cost pool and will be used against later paid disposals, rather than being “reset” on a tax-neutral crypto-to-crypto swap. citeturn22view1turn27view0

## Terra/Anchor losses, “dust,” and practical mechanics (FIFO, valuation burden, thresholds)

### Question 14: Can Terra/UST/LUNA losses be claimed? Is LUNA2 dust relevant?

Official PIT-38 guidance states that current rules **do not provide for determining and settling a “loss”** from paid disposal of cryptocurrencies in the usual way; instead, if expenses exceed revenues, the “unused costs” can be deducted from crypto revenues in subsequent years. citeturn27view0turn22view1  
KIS materials also cite statutory language excluding the usual PIT loss rule for virtual currency disposals. citeturn22view1turn19view0

What this typically means in Terra-collapse scenarios:
- If you had acquisition costs for UST/LUNA, those costs are part of your crypto cost pool (when properly documented) and may reduce tax on future paid crypto disposals, to the extent they were not already used against prior crypto revenues. citeturn27view0turn22view1  
- If you dispose of “dust” for fiat (even very small) or use dust to buy something (goods/services), that is still a “paid disposal” event in the statutory sense; it can matter for documenting that the position was closed, but the official framework does not turn price-collapse itself into a separate deductible “loss” item. citeturn27view0

### Question 15–16: Do staking rewards create new FIFO lots, and must each receipt be valued in PLN?

If you follow **Track A (receipt-tax)**, the KIS approach requires that **each time a reward is received**, income is recognized “already at the moment of receiving the reward,” and the income amount is the **market value** at “time and place” of obtaining it. citeturn19view0turn18view0  
That implies a practical need to record each receipt (or at least each valuation moment) and convert it to PLN.

If you follow **Track B (disposal-only)**, then reward receipts are not taxed at receipt and the valuation focus shifts mainly to **paid disposals** that are reported on PIT-38, consistent with the official description of taxable events for virtual currency. citeturn27view0turn9search21

For PLN conversion, PIT-38 guidance requires specific FX conversion rules where relevant (NBP average rate from the prior business day for foreign-currency amounts). citeturn27view0  
For receipt-tax scenarios, KIS relies on market-value valuation principles rather than a single statutory crypto-to-PLN formula in the PIT-38 guidance page. citeturn19view0

### Question 17: Is there a materiality threshold or simplified method for many small rewards?

Polish tax rules include statutory rounding mechanics: **tax bases are rounded to full PLN** under the general tax ordinance rounding rule (Art. 63 is explicitly presented as “Zaokrąglenie kwot”). citeturn28search9turn28search0

However, the rounding rule is not the same as a “materiality exemption.” The sources reviewed do not describe a crypto-specific de minimis threshold that would categorically remove small staking/airdrop receipts from reporting if they are otherwise taxable under the chosen classification approach. Where receipt-tax is followed, the KIS valuation-at-receipt concept still applies in principle regardless of frequency, and where disposal-only is followed, PIT-38 taxable events remain defined by the paid-disposal categories. citeturn19view0turn27view0turn28search9