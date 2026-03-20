# JDG Stablecoin Payments vs EUR Bank Transfers for a Polish Ryczałt Software Contractor

## Executive summary

For a software-development JDG taxed on **ryczałt 12%**, receiving client payments in **EUR via entity["organization","Single Euro Payments Area (SEPA)","european payment scheme"]** versus receiving **USDC/USDT on-chain** generally produces the **same ryczałt base** (gross business revenue), because ryczałt “przychód” for business activity is anchored to the same “amounts due” (kwoty należne) concept used in PIT business-income rules. citeturn26view4turn27view0turn27view1turn17view0

The **main difference** is that stablecoin settlement introduces a **second, separate tax “layer”**: once you later **dispose of** (sell/spend) the stablecoins, you step into the **PIT-38 / 19% virtual-currency regime**, with its own cost rules and reporting. citeturn17view1turn16view1turn37view4turn2view0

Crucially, the Polish tax authority (via individual interpretations) has accepted a structure in which:  
- receiving crypto as payment for business services produces **business revenue** taxed under your chosen form (here: ryczałt), and  
- the crypto you receive is treated as **paid acquisition** (“odpłatne nabycie”) of virtual currency; the **tax cost for PIT-38** can be the **value of the settled receivable** (the invoiced remuneration value), so immediate conversion often yields **near-zero PIT-38 profit**. citeturn17view0turn17view1turn16view1

Another major practical difference: the tax authority has also indicated that **crypto is not “waluta obca”** for tax FX-difference rules, so **tax FX differences (różnice kursowe) under art. 24c PIT do not arise** merely because an invoice is in USD/EUR but payment is in stablecoin; the crypto leg is treated as a **separate set of transactions** taxed under virtual-currency rules. citeturn36view1turn36view2

## Legal classification and why stablecoins create a separate PIT-38 track

Under entity["country","Poland","country in europe"]’s AML framework, “waluta wirtualna” is broadly defined as a digital representation of value that is not legal tender, e-money, a financial instrument, a bill of exchange, or a cheque, but is exchangeable in economic trade and may be stored/transferred electronically. This definition is routinely used as the reference point for classifying cryptocurrencies (including stablecoins such as USDC/USDT) as “waluta wirtualna.” citeturn21view0turn16view1

For PIT purposes, income from **paid disposal of virtual currency** is tracked as a distinct bucket (capital income) and taxed under the dedicated rules (19% under art. 30b). The statutory definition of “odpłatne zbycie waluty wirtualnej” covers exchange to legal tender, goods, services, other property rights (other than virtual currency), or paying obligations with virtual currency—this is the legal bridge connecting “spend/sell crypto” to PIT-38 taxation. citeturn16view1turn37view4turn2view0

## Ryczałt layer: revenue recognition date, PLN conversion, and invoice wording

### When ryczałt revenue is recognized

For business activity, Polish PIT uses an accrual-like rule: the revenue date is generally the day of **service performance** (or partial performance), **not later than** the invoice date or the day the receivable is settled. For services settled in billing periods (typical monthly B2B dev contracts), the revenue date is the **last day of the settlement period** specified in the contract or invoice (at least annually). citeturn27view1turn37view1

Ryczałt ties business taxable revenue (“przychody … z pozarolniczej działalności gospodarczej”) to the PIT business-revenue concept (art. 14 PIT), so—unless you have elected special cash-method options—your **ryczałt base is driven by the service/billing-period rule**, not by the on-chain receipt timestamp. citeturn26view4turn17view0turn37view1

**Answer to the “invoice vs completion vs receipt” question:** in the standard model, it is typically the **service completion / end of settlement period**, constrained by “not later than invoice or settlement.” citeturn27view1turn37view1

### Which PLN value is used for ryczałt

If the receivable is **denominated in a foreign fiat currency** (e.g., USD or EUR), PIT provides a direct conversion rule: convert the foreign-currency revenue into PLN using the **average entity["organization","Narodowy Bank Polski","central bank poland"]** (NBP) rate from the **last business day preceding the revenue date**. citeturn30view4turn37view0

If, instead, remuneration is **specified directly in crypto units** (e.g., “10,000 USDC”), KIS interpretations describe valuing the in-kind benefit using **market prices** (art. 11 principles for in-kind valuation) and then converting through a reference fiat currency (often USD) and then to PLN using the NBP rule by analogy/second step, because there is no single official “crypto rate.” citeturn17view1turn16view0turn16view1

**Answer to whether 12% is calculated on this PLN amount:** yes—ryczałt is calculated on the PLN “przychód” amount recorded in the revenue register; the act itself also emphasizes ryczałt is charged on revenue without deducting standard costs. citeturn17view0turn26view1turn37view5

### Does invoice currency or payment medium control the PLN conversion?

A KIS line of reasoning (accepted in multiple interpretations) is that the business revenue is the **remuneration due for the service** and that, for recognizing this revenue, it does not matter whether it was actually received yet or in what form it is paid; the consequences of obtaining virtual currency are then handled in the separate virtual-currency regime. citeturn17view0turn17view1turn35view0

Practically, this means:

- If your contract/invoice states “**$10,000 due**,” and the client settles it by sending $10,000-equivalent USDC, your ryczałt revenue is most defensibly treated as **$10,000 revenue** converted to PLN under NBP rules for foreign currency. citeturn17view0turn30view4turn37view0  
- If your contract/invoice states “**10,000 USDC due**,” then you lean into the “in-kind / market value” valuation approach for business revenue, which is more documentation-heavy even if USDC is usually close to $1. citeturn17view1turn16view0turn16view1

### Does contractual framing (“payable in USDC” vs “USD due, settled in USDC”) matter?

It can matter because it changes what you are claiming the “amount due” is:

- **“USD (or EUR) due, settled in USDC”** is aligned with the foreign-currency conversion mechanics (NBP for the fiat currency) and tends to reduce valuation ambiguity at the business-revenue stage. citeturn30view4turn17view0turn17view1  
- **“USDC due”** pushes you toward in-kind valuation logic (market price determination), even if stablecoins are relatively stable. citeturn17view1turn16view0turn16view1

### Hidden complications vs EUR bank transfers

For the **ryczałt layer alone**, both methods can still land at “12% of PLN revenue,” but the crypto route has additional moving parts: valuation evidence and the separate PIT-38 track. citeturn17view1turn2view0

## PIT-38 layer: “double reporting,” cost basis, holding period effects, and crypto-to-crypto swaps

### Is “PIT-28 plus PIT-38” really how it works on ryczałt?

KIS reasoning supports a two-track model:

- the service creates **business revenue** taxed under the chosen business regime (here: ryczałt), and  
- receiving virtual currency as settlement is handled under **art. 30b PIT** (virtual currency). citeturn17view0turn17view1turn16view1

So yes, it is “double reporting” in the sense of **two declarations**, but it is not necessarily “double taxation,” because the cost basis mechanism can neutralize the second layer if values do not move. citeturn17view1turn37view4

### Does the ryczałt receipt value become PIT-38 cost basis?

In a KIS interpretation addressing business services paid in crypto, the authority states that obtaining virtual currency as payment has the character of **paid acquisition**, and that the “direct expense” for acquisition is the **value of the receivable treated as settled**—i.e., the value of the remuneration due for the services. That value is treated as a cost of acquiring the virtual currency for art. 22(14) purposes. citeturn17view1turn35view0turn16view2

This is the key doctrinal bridge that turns “crypto payment” into:  
**Business revenue now** + **capital result later (with cost basis).** citeturn17view1turn35view0

### If you convert immediately, is PIT-38 gain/loss essentially zero?

If your disposal proceeds in PLN are approximately equal to the acquisition-cost value (the settled receivable value), then art. 30b’s income definition (“difference between proceeds and costs”) yields ~0 taxable income. This “zeroing” logic is explicitly acknowledged in the KIS reasoning (“if proceeds equal costs, no income is obtained”), while still emphasizing the reporting requirement. citeturn17view1turn37view4turn35view0

### If you hold USDC for weeks/months, is the movement taxable?

Yes—because when you later dispose of the virtual currency (e.g., exchange USDC to EUR/PLN), the proceeds in PLN can differ from the PLN value of your acquisition cost, and the difference is taxed as virtual-currency income under art. 30b (19%). citeturn37view4turn17view1turn16view1

This is the practical “FX exposure becomes PIT-38 exposure” effect of holding a fiat-pegged stablecoin. citeturn37view4turn17view1

### Crypto-to-crypto swaps: taxable or not?

The statutory definition of “odpłatne zbycie waluty wirtualnej” does **not** include exchanging one virtual currency for another; it is focused on exchange to legal tender, goods/services/rights, or settling obligations. citeturn16view1turn2view0

Tax guidance for individuals also states that **crypto-to-crypto exchanges are not taxable events**, while exchanges to fiat (and similar “exit” events) are taxable disposals. citeturn2view0turn16view1

A related constraint: PIT also provides that expenses connected with swapping one virtual currency for another are not treated as deductible costs (art. 23(1)(38d) as cited in KIS materials). citeturn15view2turn35view0

## FX differences, ewidencja, and VAT: where bank EUR and stablecoin differ operationally

### FX differences: EUR bank transfers vs stablecoin settlement

For foreign-currency business items, PIT contains a detailed **tax FX-differences** mechanism (art. 24c), comparing values at NBP average rates versus “actually applied” rates at receipt/payment. citeturn30view2turn37view3

Ryczałt explicitly imports this FX framework: for ryczałt business revenues, FX differences are applied “appropriately,” and (importantly) **negative FX differences reduce revenue** (because ryczałt generally does not recognize costs the same way as general taxation). citeturn25view1turn37view6

By contrast, a KIS interpretation addressing invoices in foreign currency paid in stablecoins states directly that because crypto is a virtual unit not treated as foreign currency in Polish law, **FX differences under art. 24c do not arise**, even if the invoice uses USD, and even after converting crypto to PLN; the business-service transaction and the virtual-currency transaction are treated as distinct. citeturn36view1turn36view2

### Ewidencja przychodów: does USDC need different treatment?

Ryczałt taxpayers generally have an obligation to keep the **revenue register (ewidencja)** and supporting evidence used for entries, kept at the place of business or in the accounting office. citeturn25view0

What changes with stablecoins is less the *ryczałt entry itself* (which remains a PLN revenue figure on the applicable revenue date) and more the *supporting evidence package*: in addition to invoice/contract, you will want contemporaneous proof of (a) wallet receipt details and (b) the valuation method used when crypto units themselves are the pricing unit. KIS reasoning on valuation emphasizes using market pricing references where needed. citeturn16view0turn17view1turn25view0

### VAT: does payment in USDC change anything?

Payment method does not change the core VAT “place of supply” rule for B2B services: for services supplied to a taxpayer, the place of supply is generally the customer’s establishment location (art. 28b VAT). citeturn34search0turn34search8

If VAT-relevant amounts are expressed in a foreign currency, VAT contains its own PLN conversion mechanism (art. 31a VAT) based on NBP (or ECB options under the statute). citeturn34search1turn34search13

One important update relative to your stated context: multiple professional and legal-commentary sources report that the Polish VAT small-taxpayer exemption limit increased to **240,000 PLN from 1 Jan 2026** (previously 200,000 PLN), tied to art. 113 VAT. citeturn34search10turn34search14turn34search2

If your client is in the entity["organization","European Union","supranational union"] and you provide B2B services under art. 28b, VAT-UE registration can apply even for VAT-exempt businesses; the Ministry’s guidance explicitly notes that VAT-UE registration does not itself remove the domestic exemption. citeturn34search7turn34search15turn34search8

## AML and banking workflow: registration risk, exchange cash-out, and what “creates tax”

### Do you need to register as a crypto service provider if you accept stablecoins?

AML law treats as “obligated institutions” those who run defined crypto-asset services—specifically businesses providing services in the scope of:  
(a) exchange between virtual currencies and payment instruments,  
(b) exchange between virtual currencies,  
(c) intermediation in those exchanges, or  
(d) custody-like account services enabling use of virtual currency units. citeturn24view1turn37view7

Simply **accepting** stablecoins as payment for software development services does not itself match this catalog of exchange/intermediation/custody services. The KIS fact patterns on crypto-paid IT services often explicitly assume the taxpayer is *not* performing AML art. 2(1)(12) services. citeturn29view0turn35view0

### If you cash out on an exchange and withdraw EUR to your business bank, do you create extra tax events?

The tax event in the virtual-currency regime is the **disposal** (e.g., exchange of USDC to EUR/PLN), because “odpłatne zbycie” covers exchange to legal tender. citeturn16view1turn2view0

A subsequent **bank withdrawal/transfer of already-converted EUR** is generally just movement of fiat funds and is not itself described by the statutory “virtual currency disposal” definition; the taxable “exit” was the crypto-to-fiat exchange. citeturn16view1turn2view0

## Comparison table and practical recommendation

### Complete “tax journey” comparison

| Stage | Option A: EUR via regular bank transfer | Option B: USDC/USDT on-chain |
|---|---|---|
| Business revenue recognition moment | Revenue date is typically tied to service performance or end of billing period; not later than invoice or settlement. citeturn37view1turn27view1turn26view4 | Same rule; KIS emphasizes form of payment does not change the fact that “amounts due” are business revenue. citeturn17view0turn35view0turn37view1 |
| PLN value for ryczałt base | If invoice/receivable is in EUR: convert using average NBP rate from the business day before the revenue date. citeturn37view0turn30view4 | If invoice/receivable is in USD/EUR: same NBP conversion logic for that fiat currency. If remuneration is specified directly in crypto units, KIS practice relies on market valuation then conversion. citeturn37view0turn17view1turn16view1 |
| Ryczałt tax | 12% of PLN “przychód” from the software service (assuming correct classification). citeturn29view0turn17view0 | Same 12% on the PLN “przychód.” citeturn17view0turn29view0 |
| FX differences in the ryczałt base | Tax FX differences (art. 24c PIT) can arise with foreign currency items; under ryczałt they are applied via art. 6(1c), and negative differences reduce revenue. citeturn37view6turn37view3turn30view2 | KIS indicates no art. 24c FX differences arise from crypto settlement (even if invoice USD) because crypto is not treated as foreign currency; crypto leg is separate. citeturn36view1turn36view2 |
| What you actually “receive” | EUR on bank account | Virtual currency (USDC/USDT) in a wallet |
| “Second layer” tax | Normally none *from the payment method itself* (unless you separately engage in crypto trading). | Applies once you dispose of the USDC/USDT: taxed at 19% under art. 30b virtual-currency rules (PIT-38). citeturn37view4turn16view1turn2view0 |
| PIT-38 cost basis for the stablecoins | N/A | KIS view: paid acquisition; cost can be the value of the settled receivable (your remuneration due) and related disposal fees. citeturn17view1turn35view0turn36view2 |
| If you convert the stablecoins immediately | N/A | Often near-zero PIT-38 income if proceeds ≈ costs; still requires proper reporting logic. citeturn17view1turn37view4 |
| If you hold the stablecoins | N/A | Any PLN-value change between acquisition-cost valuation and disposal can become PIT-38 income/loss under art. 30b. citeturn37view4turn17view1 |
| Crypto-to-crypto swaps | N/A | Generally not taxable as “disposal,” but swap-related expenses are restricted by PIT rules. citeturn2view0turn15view2turn16view1 |
| Compliance footprint | Standard: invoices, bank statements, possible FX difference computations. citeturn37view6turn37view3 | Adds: wallet transaction evidence, valuation methodology, PIT-38 tracking and potentially filing even when only costs are present, plus clearer separation of business vs personal traces. citeturn16view2turn25view0turn17view1turn35view0 |

### Total tax burden comparison in “formula” form

Let **R\_PLN** = PLN business revenue for the month (converted under relevant rules). citeturn37view0turn37view1turn26view4

**Option A (EUR bank transfer):**  
Total ≈ **0.12 × R\_PLN** plus/minus the effect of tax FX differences included in the ryczałt base under ryczałt’s imported FX rules. citeturn37view6turn30view2

**Option B (USDC/USDT):**  
Total ≈ **0.12 × R\_PLN** + **0.19 × max(0, D\_PLN − C\_PLN)**, where D\_PLN is PLN proceeds from disposal of virtual currency and C\_PLN is the virtual-currency cost basis (including, per KIS, the receivable value treated as settled). citeturn37view4turn17view1turn36view2

Your stated “large crypto cost pool carry-forward” (~319k PLN) is conceptually aligned with the statutory mechanism where excess virtual-currency costs over proceeds roll forward as costs to later years (art. 22(16)). In that framework, PIT-38 tax may remain zero until cumulative proceeds exceed cumulative costs. citeturn37view2turn16view2turn35view0

### Practical recommendation for the described setup

If your goal is **lowest compliance load and lowest “moving parts” risk**, staying with **EUR bank transfer** is structurally simpler because you remain inside the ryczałt/FX-differences workflow and avoid the mandatory PIT-38 lifecycle tied to crypto settlement. citeturn37view6turn30view2turn2view0

If you want the **optionality of on-chain receipt** (speed, treasury strategy, crypto familiarity) and can tolerate the extra reporting, stablecoin payment can be made more robust by anchoring the legal obligation in **USD/EUR** and stating that settlement may occur in USDC at a defined conversion convention—this aligns the ryczałt revenue quantification to the NBP foreign-currency rule while preserving the KIS-accepted “paid acquisition with receivable-value cost basis” model for PIT-38. citeturn37view0turn17view1turn36view2

In either option, revisit VAT assumptions for 2026: the small-business VAT exemption threshold is reported as **240,000 PLN from 1 Jan 2026**, and VAT-UE registration may still be relevant for EU B2B services even when VAT-exempt. citeturn34search10turn34search14turn34search15turn34search8