# Tax Classification of Stablecoins in Poland on USDC and USDT

## Background and why the classification matters

A Polish tax resident who uses USD‑pegged stablecoins as “bridge assets” (salary paid in USDC on-chain → exchange → EUR → bank; and crypto trading routed through USDT/USDC) is effectively asking one core question: **are USDC/USDT treated as “waluta wirtualna” (virtual currency) for Polish tax purposes, or as something closer to fiat/e‑money?**  

That classification is decisive because Polish PIT rules for virtual currencies are built around a narrow concept of a **taxable “disposal”** event (typically: exit into fiat, spending on goods/services, or settling liabilities), while **crypto-to-crypto exchanges are not treated as taxable disposal** if both legs are “waluta wirtualna”. citeturn17view3turn19view1turn56view0

This report reflects the legal framework and publicly available materials as of **2026‑03‑19** (Europe/Warsaw).

## Polish legal framework that determines whether something is “waluta wirtualna”

### Definition of “waluta wirtualna” in the AML Act

Poland’s baseline statutory definition of “waluta wirtualna” is in the AML Act (the Act of 1 March 2018 on counteracting money laundering and terrorist financing). It defines virtual currency as a **digital representation of value** that is **not**: legal tender (NBP/foreign central banks), an international unit of account, **electronic money**, a financial instrument, or a bill of exchange/cheque; and that **is exchangeable in economic transactions for legal tender and accepted as a medium of exchange**, and can be stored/transferred/traded electronically. citeturn56view0

That “not electronic money” exclusion is the key hinge for stablecoins. citeturn56view0

### Link between the PIT crypto tax regime and the AML definition

The PIT Act includes “odpłatne zbycie waluty wirtualnej” (paid disposal of virtual currency) as a source of capital gains revenue. citeturn17view3turn19view1  
The PIT rules for “waluty wirtualne” are expressly tied into the statutory framework that uses the AML definition (in practice, this is the definition used by tax authorities when analyzing whether a token is a “waluta wirtualna”). citeturn56view0turn17view3

### Definition of “electronic money” in Polish law

The AML definition excludes electronic money “in the meaning of” the Polish Payment Services Act. That Act defines electronic money as **monetary value stored electronically (including magnetically), issued with an obligation of redemption, for the purpose of payment transactions, accepted by entities other than only the issuer**. citeturn52view1turn56view0

So, at the level of statutes, the classification question becomes:

- If a stablecoin **is not** “pieniądz elektroniczny” under the Payment Services Act → it can still be “waluta wirtualna” if it meets the rest of the AML criteria. citeturn56view0turn52view1  
- If a stablecoin **is** “pieniądz elektroniczny” → it is excluded from the AML (and therefore PIT-“waluty wirtualne”) definition. citeturn56view0turn52view1

## Applying the Polish definitions to USDC and USDT

### Economic/technical profile of USDC and USDT

USDC is described by its issuer as a “fully reserved stablecoin” designed to maintain price equivalence to the US dollar and as redeemable 1:1 for US dollars. citeturn48search0turn48search2

USDT is described by its issuer as pegged 1:1 to a matching fiat currency (e.g., 1 USD₮ = 1 USD) and backed by reserves, and its terms describe redemption at par (subject to terms/fees). citeturn48search1turn48search7

As blockchain tokens used and traded on crypto venues, **both are plainly capable of electronic storage, transfer, and trading**, and are used as a medium of exchange in crypto markets—features that align with the positive limb of the AML definition. citeturn56view0turn48search0turn48search1

### Do USDC/USDT fall under the “electronic money” exclusion in Poland?

From the Polish statutory perspective, the exclusion turns on whether a given stablecoin is “pieniądz elektroniczny” under the Payment Services Act definition (monetary value stored electronically, issued with redemption obligation, for payment transactions, accepted by others). citeturn52view1turn56view0

USDC’s public materials emphasize 1:1 redeemability and reserve backing, which resembles an “obligation of redemption” element. citeturn48search0turn48search2  
USDT’s terms likewise speak to redemption at par (1 USD for 1 USD₮, less fees where applicable). citeturn48search7turn48search1

However, whether that is sufficient to classify them as “pieniądz elektroniczny” under Polish law is not just a technical question; it also intersects with financial-regulatory characterization (for example, whether the asset is treated as “e‑money” in the EU regulatory perimeter, and by whom it is issued). citeturn52view1turn56view0

### What Polish tax authority practice suggests about stablecoins

One directly relevant publicly accessible individual interpretation is:

- **Interpretation of 20 May 2025, sign. 0115‑KDIT1.4011.256.2025.1.MST** (PIT; inherited crypto and cost basis). In the applicant’s factual description, the portfolio explicitly includes stablecoins such as **Tether (USDT)** and **USDC**, and states that the cryptoassets “meet the definition of virtual currency” in the AML Act (and the case proceeds under the virtual-currency regime). citeturn26view0

This does not create a formal “token-by-token” classification list in the law (Polish statutes don’t work that way), but it is meaningful evidence of **how stablecoins are being handled in tax interpretation practice post‑MiCA: treated within the “waluta wirtualna” framework rather than as fiat**. citeturn26view0turn56view0

Another example (different tax) shows how Polish authorities often frame crypto—including stablecoin-like crypto—as **a property right rather than money**. A published summary referencing **an individual interpretation of 15 November 2024 (PCC; loan in a USD‑pegged stablecoin)** reports that the authority treated the cryptocurrency as a property right, not “money” for PCC purposes. citeturn39view0

## MiCA and whether it changes Polish classification or tax treatment

### What MiCA changes on the regulatory side

Under MiCA’s stablecoin taxonomy, fiat‑referencing stablecoins generally fall into the “e‑money token” category (a crypto‑asset that purports to maintain a stable value by referencing one official currency). citeturn40search11

MiCA also explicitly links e‑money tokens to the EU e‑money perimeter: in an official opinion, the entity["organization","European Banking Authority","eu banking regulator"] notes that MiCA provides (Article 48(2)) that **“e‑money tokens shall be deemed to be electronic money.”** citeturn46search4

MiCA’s timeline matters:

- EU regulators state that MiCA became applicable to issuers of ARTs/EMTs on **30 June 2024**, and to crypto‑asset service providers on **30 December 2024**. citeturn40search14  
- A Polish supervisory statement likewise notes the start of full application from **30 December 2024**. citeturn25search8

### Does MiCA automatically change Polish PIT on crypto disposals?

MiCA is a financial-markets regulation. It does not, by itself, rewrite Polish tax statutes. The crucial Polish tax hinge remains the **domestic definition chain**: AML “waluta wirtualna” (which expressly excludes electronic money) and the Payment Services Act’s electronic money definition. citeturn56view0turn52view1turn17view3

MiCA can still matter indirectly:

- If a particular stablecoin is treated (for Polish-law purposes) as “pieniądz elektroniczny” under the Payment Services Act, then—by black-letter AML text—it would be excluded from “waluta wirtualna.” citeturn56view0turn52view1  
- MiCA strengthens the argument that fiat‑pegged stablecoins resemble e‑money, because MiCA deems EMTs to be electronic money. citeturn46search4turn40search11

But as of the available public tax interpretation materials, there is no clear signal that Polish PIT treatment of mainstream USD‑pegged stablecoins has switched away from the “waluta wirtualna” framework; stablecoins continue to appear in the virtual-currency tax analysis ecosystem (including in 2025 texts, i.e., after MiCA application). citeturn26view0turn56view0

### Does USDC’s “EMT-like” profile change Polish tax treatment from a specific date?

From an EU-regulatory point of view, the EMT/ART regime started applying on **30 June 2024**. citeturn40search14  
However, **a Polish PIT reclassification date does not automatically follow**, because Polish PIT taxation turns on whether the asset is “waluta wirtualna” under the domestic definition chain (AML + Payment Services Act), and those domestic definitions were not automatically rewritten by MiCA. citeturn56view0turn52view1turn17view3

Practical takeaway: **the key trigger is not “MiCA effective date” alone, but whether Polish law (or Polish tax authority interpretation practice) treats the stablecoin you used as electronic money in the sense of the Polish Payment Services Act.** citeturn56view0turn52view1turn46search4

## Tax implications for the described transaction flows

### What is taxable if USDC/USDT are treated as “waluta wirtualna”

#### Taxable event definition

For PIT, “paid disposal of virtual currency” includes: exchange of virtual currency to legal tender, goods, services, or a property right other than virtual currency, or using virtual currency to settle other obligations. citeturn17view3

**Crypto-to-crypto swaps are not included in that disposal definition** because the definition requires that what you receive is legal tender / goods / services / other property rights—i.e., not another virtual currency. citeturn17view3

#### Tax rate and tax base

Income from disposal of virtual currencies is taxed at **19%**, and the “income” is the yearly difference between total “revenues” from disposals and allowable costs as defined for virtual currencies. citeturn19view1turn18view1

#### Costs (cost basis framework)

Costs for disposal of virtual currencies are defined as **documented expenses directly incurred to acquire virtual currency** plus **costs related to disposal** (including documented expenses to certain regulated entities, e.g., exchanges), with year-to-year carryforward of excess costs over revenues. citeturn18view1turn19view1turn57view1

### Answers to your key tax mechanics questions

#### If USDC is “waluta wirtualna,” is ETH → USDC non-taxable and USDC → EUR taxable?

Yes, under the statutory structure:

- ETH → USDC (virtual currency → virtual currency): **not a taxable “disposal” event** under the PIT “odpłatne zbycie” definition. citeturn17view3turn56view0  
- USDC → EUR (virtual currency → legal tender): **is** a taxable “disposal” event. citeturn17view3turn56view0

#### If USDC were not treated as “waluta wirtualna,” would ETH → USDC become taxable?

Mechanically, yes. If USDC is **not** “waluta wirtualna,” then exchanging ETH (virtual currency) for USDC would be exchanging virtual currency for a **property right other than virtual currency**, which falls inside the statutory “disposal” definition. citeturn17view3turn56view0

This is exactly why the “electronic money vs virtual currency” boundary is high-stakes for routing trades through stablecoins. citeturn56view0turn52view1turn46search4

#### What is “revenue” on USDC → EUR for tax purposes?

Under PIT mechanics, revenue is tied to what you receive from the disposal. When you dispose of virtual currency for EUR, the revenue is the **EUR amount received**, converted to PLN using the statutory FX conversion rule. citeturn17view3turn20view2turn19view1

The PIT rule for foreign-currency conversion states: **income in foreign currencies is converted to PLN using the average exchange rate published for the last working day preceding the day the income is earned**. citeturn20view2

So, in formula form (when you receive EUR):  

**Revenue (PLN) = EUR_received × NBP average EUR/PLN (previous working day)**. citeturn20view2turn17view3

Using “USDC amount × USD rate” is not the normal statutory framing when the disposal consideration is EUR; that “USD leg” is economically relevant but not the legal “currency of proceeds” if the exchange actually pays out EUR. citeturn20view2turn17view3

#### What is the cost basis of USDC depending on how it was acquired?

Polish PIT does *not* use a universal FIFO/lot-based basis rule in the statute for virtual currencies; instead it defines what counts as allowable costs for the annual computation (documented acquisition expenses + disposal costs, with carryforward). citeturn18view1turn19view1turn57view1

Because your scenarios include “salary paid in USDC” and “crypto-to-stable swaps,” the right answer becomes partly **black-letter statutory** and partly **tax-interpretation-risk management**.

##### USDC received as salary payment

Two separate tax layers are involved:

- **Employment/service income layer**: the PIT Act treats employment income as including the monetary value of in-kind benefits, not just cash. That is the legal gateway through which “salary paid in tokens” becomes taxable at receipt as salary/service income (depending on your contract type). citeturn20view2  
- **Virtual currency disposal layer**: later exchanging USDC to EUR is a virtual currency disposal taxed at 19% (if USDC is “waluta wirtualna”). citeturn17view3turn19view1

**Cost basis question (for the later USDC→EUR disposal):** the statutory wording for virtual-currency costs requires “documented expenses directly incurred to acquire” the virtual currency. citeturn18view1turn57view1

A very important data point from tax authority practice: in the May 2025 interpretation (0115‑KDIT1.4011.256.2025.1.MST) the authority emphasized that the PIT virtual-currency cost rule is grounded in art. 22(14)–(16) and denied a basis to treat the *value* of inherited crypto as cost, pointing out that art. 22(14) defines what counts as deductible cost for virtual-currency disposal. citeturn57view1turn26view0

That interpretation also shows the taxpayer attempted to argue by analogy to a general PIT rule for things received gratuitously (art. 22(1d)), but the authority still anchored the analysis in the special virtual-currency cost regime. citeturn57view1

**Implication:** for “salary-in-crypto,” there is a real interpretive possibility that the tax authority focuses tightly on whether you have “wydatki” (out-of-pocket acquisition expenses) for the USDC, which could lead to a conservative cost basis of **0** for the virtual-currency disposal (even though you already had taxable income at receipt). This is a risk area because the statute’s cost wording is expense-based. citeturn18view1turn57view1turn20view2

##### USDC received from selling other crypto (ETH → USDC) if both are “waluta wirtualna”

If both assets are virtual currencies, the ETH→USDC exchange is not itself a taxable disposal event. citeturn17view3turn56view0

Cost-wise, the statute allows costs that are documented acquisition expenses plus disposal costs, deducted against disposal revenues on the annual net basis, with carryforward. citeturn18view1turn19view1turn20view2

Practically, this means: **the taxable profit is realized when you later dispose to fiat (or goods/services), and your deductible costs are ultimately grounded in what you spent to acquire your virtual currencies (plus fees), rather than being “reset” at each crypto-to-crypto conversion.** citeturn18view1turn17view3turn19view1

##### USDC purchased directly with EUR

This is the cleanest statutory fit for “documented expenses incurred to acquire” virtual currency: the cost is essentially what you paid (EUR amount), converted to PLN under the foreign currency cost conversion rule (average FX rate from the last working day before the cost is incurred). citeturn18view1turn20view2turn17view3

### USDC-to-USDT swaps and stablecoin auto-conversions

#### Is USDC → USDT (or USDT → USDC) taxable?

If both stablecoins are treated as “waluta wirtualna,” then stablecoin-to-stablecoin conversion is **virtual currency → virtual currency**, and is not a taxable “disposal” under PIT’s disposal definition. citeturn17view3turn56view0

#### Are exchange-driven auto-conversions (e.g., BUSD → FDUSD → USDC) taxable?

Under the same assumption (each token is “waluta wirtualna”), each leg is still a virtual currency → virtual currency exchange, so **the conversion itself would not be a disposal event**. citeturn17view3turn56view0

What still matters for reporting is documenting fees (disposal-related costs can be deductible), and ensuring the later fiat exit is captured as the revenue event. citeturn18view1turn17view3turn20view2

## Worked example matching your scenario

### Facts

- 6,000 USDC received as salary.
- Value at receipt: 24,000 PLN.
- Later conversion: 6,000 USDC → 5,500 EUR.
- PLN value of received EUR at that time: 23,500 PLN.

### Is there a taxable event at the USDC → EUR step?

If USDC is treated as “waluta wirtualna,” then converting USDC to EUR is an exchange of virtual currency to legal tender, which is a taxable disposal event. citeturn17view3turn56view0

### Revenue amount

Revenue is the EUR proceeds converted to PLN using the statutory rule for foreign currency income conversion (average FX rate of last working day before the day the revenue is earned). In your numeric framing, that equals 23,500 PLN. citeturn20view2turn17view3

### Cost basis and resulting gain/loss: why there are two plausible treatments

The PIT statute states that virtual-currency costs are documented expenses directly incurred to acquire the virtual currency plus disposal-related costs. citeturn18view1turn57view1  

Because “salary-paid USDC” may not involve a documented cash acquisition expense, there is a genuine ambiguity/risk on whether the PLN value taxed as salary can be treated as “wydatki na nabycie” for the virtual-currency regime. The KIS inheritance interpretation illustrates a strict approach: the authority denied using the inherited value as cost because art. 22(14) defines costs in an expense-based way. citeturn57view1turn26view0

So, the two main outcomes are:

**Outcome A (economically intuitive, but needs to be defensible): cost = 24,000 PLN**  
If the 24,000 PLN salary valuation is treated as your acquisition “cost” for later disposal, then:
- Revenue: 23,500 PLN
- Cost: 24,000 PLN
- Result: **loss = 500 PLN** (ignoring fees; fees could increase the loss).  
This matches your option (a) in substance.

**Outcome B (conservative, expense-only reading anchored in art. 22(14)): cost = 0 PLN**  
If no “documented expenses directly incurred” exist, then:
- Revenue: 23,500 PLN
- Cost: 0 PLN
- Result: **income = 23,500 PLN** (again ignoring fees).  
This resembles your option (c) in effect but is not “no event”; it’s an event with potentially high taxable base.

What is *not* supported by the PIT disposal definition (assuming USDC is “waluta wirtualna”) is “no event because stablecoins aren’t crypto.” The disposal definition is about “waluta wirtualna” and does not carve out stablecoins as a category. citeturn17view3turn56view0

## Bottom-line conclusions

USDC and USDT are not named in Polish statutes as a closed list; classification is functional. Under the AML definition, a token qualifies as “waluta wirtualna” if it is a digital value representation, not legal tender/e‑money/financial instrument, and is exchangeable/accepted/tradeable electronically. citeturn56view0

On their publicly stated characteristics (USD‑referencing stable value, on-chain transferability, active trading), USDC and USDT generally fit the “waluta wirtualna” profile. citeturn56view0turn48search0turn48search1

MiCA creates potential tension because it classifies fiat‑referencing stablecoins as e‑money tokens and deems e‑money tokens to be electronic money at EU level; yet Polish “waluta wirtualna” excludes “pieniądz elektroniczny” as defined domestically. citeturn46search4turn40search11turn52view1turn56view0

As of the publicly accessible Polish interpretation materials reviewed here, stablecoins (including USDT and USDC) continue to appear as “waluty wirtualne” in the tax-interpretation universe *after* MiCA application, suggesting no clean “MiCA date” at which tax treatment flips. citeturn26view0turn40search14turn25search8

If USDC/USDT are treated as “waluta wirtualna,” then:
- crypto-to-stable swaps remain non-taxable disposal events, citeturn17view3turn56view0  
- stable-to-fiat is the taxable disposal, citeturn17view3  
- revenue is the fiat proceeds in PLN under the FX conversion rule, citeturn20view2  
- deductible costs hinge on “documented acquisition expenses” plus disposal costs, with carryforward. citeturn18view1turn19view1