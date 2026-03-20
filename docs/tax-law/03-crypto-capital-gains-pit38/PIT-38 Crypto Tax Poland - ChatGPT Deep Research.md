# Crypto Capital Gains and PIT-38 Reporting in for Tax Years 2023–2025

## Executive summary

For individuals (non-business trading) in Poland, the core rule is that **PIT at 19% applies to “odpłatne zbycie walut wirtualnych” (paid disposal of virtual currencies)**, i.e., when crypto is exchanged for **fiat**, **goods/services**, **non-crypto property rights**, or used to **settle liabilities**. citeturn18search22turn27search1turn26search2

A **crypto-to-crypto exchange (including stablecoin-to-stablecoin)** is **tax-neutral for PIT** (no immediate taxable revenue). citeturn18search22turn27search1turn28search23

Poland’s method for costs is not FIFO: it is effectively a **pooled annual approach** in PIT-38. You report (a) total annual revenue from taxable disposals and (b) **all documented acquisition/disposal costs incurred in the year**, even if you had **no sales**, and **any excess costs roll forward** to future years (the law frames this as carried costs, not a “loss”). citeturn21view0turn18search22turn26search2turn15view0

For PIT-38, crypto is reported in **Section E** (virtual currency section). The **field numbers differ by year/form version** (2023–2024 vs 2025). citeturn24view0turn25view0turn25view1

Treatment of **staking rewards, airdrops, and interest paid in crypto** is an area with **material controversy**: a line of tax authority interpretations treats **receipt** as taxable income (often as “prawa majątkowe”), while some administrative-court rulings support taxation **only upon disposal** (sale/exchange for fiat, etc.). This is a key risk area that often determines whether taxpayers seek individual rulings or litigation-grade documentation. citeturn29view2turn30search9turn30search0

## Legal framework and key definitions

Polish PIT law classifies **income from paid disposal of virtual currencies** as **capital income**. The statutory definition of taxable “odpłatne zbycie” (paid disposal) is crucial for determining what is and is not a taxable event. citeturn27search1turn26search2turn18search22

### What “odpłatne zbycie waluty wirtualnej” includes

Under the PIT Act’s definition, “odpłatne zbycie waluty wirtualnej” includes exchanging a virtual currency for:  
- **legal tender (fiat)**,  
- **a good**, **a service**, or **a property right other than a virtual currency**, or  
- using crypto to **settle other liabilities**. citeturn27search1turn18search22turn15view0

This is the backbone for classifying: (a) exchange trades to EUR/PLN, (b) spending crypto, and (c) many “pay with crypto” scenarios.

### Tax rate and separation from other income categories

Income from paid disposal of virtual currencies is taxed at **19%** (flat rate) under the PIT capital-gains regime. citeturn26search2turn28search7

Importantly, PIT law explicitly states that **income from disposal of virtual currencies is not combined** with certain other income categories, including other capital-gains categories taxed under art. 30b(1) (e.g., securities) and income under the progressive scale/business tax regimes. citeturn26search2turn15view0  
Practically, this is implemented via **separate parts/lines** for crypto vs securities inside PIT-38. citeturn25view0turn25view1turn24view0

### What counts as “virtual currency” for PIT purposes

PIT references the AML-law definition of “waluta wirtualna,” which broadly covers a digital representation of value that is not legal tender/e-money/financial instrument, but can be traded/exchanged and stored/transferred electronically. citeturn15view0  
In practice this definition generally captures mainstream cryptocurrencies and many stablecoins (the classification can matter most for borderline tokens). citeturn15view0

## Taxable vs non-taxable events

This section answers Questions 1–2 and frames the rest of the reporting logic.

### Classification table

| Event / activity | PIT taxable event under virtual-currency rules? | Why it is (or is not) “odpłatne zbycie” |
|---|---:|---|
| Buy crypto with EUR (fiat → crypto) | No | Not a disposal; it is acquisition and creates documented acquisition costs. |
| Sell crypto for EUR/PLN (crypto → fiat) | Yes | Exchange of virtual currency for legal tender is explicitly within “odpłatne zbycie.” |
| Exchange BTC → ETH (crypto → crypto) | No | Crypto-to-crypto swaps are not included in “odpłatne zbycie.” |
| Exchange USDT → USDC (stablecoin → stablecoin) | No | Same category as crypto-to-crypto: exchange between virtual currencies. |
| Convert USDC → EUR using an exchange “convert” function | Yes | Economically and legally: virtual currency exchanged for fiat. |
| Pay for goods/services with crypto | Yes | Exchange of crypto for goods/services is explicitly included. |
| Gift crypto (no consideration) | Generally no PIT for the donor | A gift is not “odpłatne” (paid); however it may trigger **gift/inheritance tax** for the recipient under separate rules. |
| Transfer between own wallets / exchange ↔ self-custody | No | Mere transfers, without exchange for fiat/goods/services/rights and without settling a liability, are not “odpłatne zbycie.” |

The Ministry of Finance tax portal states directly that (a) taxable disposal includes sale for fiat, exchange for goods/services/other rights, and settling liabilities, and (b) **exchange between virtual currencies is not taxed**. citeturn18search22  
The PIT statutory definition of “odpłatne zbycie” aligns with that classification. citeturn27search1turn15view0  
Administrative case law also supports the non-taxation of crypto-to-crypto swaps (in addition to the post‑2019 statutory structure). citeturn28search23turn28search4

### What “paid disposal” means for your specific scenarios

**Selling crypto for fiat on an exchange (EUR/PLN)** is a textbook taxable event, because it is explicitly an exchange of virtual currency into legal tender. citeturn18search22turn27search1turn26search2

**“Convert” tools (e.g., stablecoin → EUR)** are treated by substance: if you exchange a virtual currency into fiat, it is “odpłatne zbycie,” even if the UI uses “convert” rather than “sell.” citeturn18search22turn27search1

**Stablecoin-to-stablecoin (USDT↔USDC)** is still a swap between virtual currencies and is therefore **not** a taxable disposal under the virtual-currency definition of “odpłatne zbycie.” citeturn18search22turn28search23

**Spending crypto for goods/services** is explicitly included in “odpłatne zbycie” (it is treated like disposal for consideration). citeturn18search22turn27search1

**Gifting crypto** is generally outside “odpłatne zbycie” because it lacks consideration; the tax issue typically shifts to **inheritance and gift tax** for the recipient (separate from PIT). citeturn9view5turn28search13

## Staking rewards, airdrops, and interest

This section addresses Questions 3–5. The main point is that **the “virtual currency disposal” regime is clear**, but **how Poland treats “free” or “reward” crypto at receipt is not settled uniformly**.

### The “disposal only” reading based on the crypto-specific PIT regime

A strict “virtual currency” approach is that **PIT-38 captures income when you dispose** of virtual currency (for fiat/goods/services, etc.). Receipt of staking/airdrop/interest is not itself an exchange for fiat/goods/services and therefore is not “odpłatne zbycie.” citeturn27search1turn18search22turn26search2

Under that approach:
- **Staking rewards** are taxed **when you later dispose** of those rewarded coins (sell to fiat, spend, etc.).  
- **Airdrops** are taxed **when you later dispose** of the airdropped assets.  
- **Interest** paid in crypto (CeFi/DeFi) is treated similarly: the taxable event is disposal, not accrual/receipt.

A major practical implication is cost basis: because the PIT crypto-cost rule focuses on **documented expenditures** on acquisition, free/rewarded coins often produce **no acquisition expenditure**, so their disposal can be close to fully taxable (except for allowable disposal costs). citeturn21view0turn18search22

### The tax-authority approach: receipt can be taxable (property-rights income)

A significant line of individual tax interpretations from the tax authority (KIS) has treated **staking rewards and airdrops as taxable upon receipt**, characterizing them as income from **property rights (“prawa majątkowe”)** valued at market prices at the time of receipt and linked to the PIT Act’s general income concepts. citeturn29view2turn10view0

This approach is especially important because it implies:
- the taxpayer may have a taxable event **before** any cash-out,
- valuation methodology and timing matter,
- reporting may not be limited to PIT-38 (because “prawa majątkowe” income is generally not the PIT-38 crypto section).

### Court direction: staking taxation at disposal (not receipt)

Administrative courts have issued rulings supporting the view that staking rewards are not taxable income at the moment of receipt, and instead become relevant when the cryptocurrency is disposed. A public summary of a WSA ruling states that the staking reward becomes taxable income only when the rewarded virtual currency is sold (disposed). citeturn30search9turn30search0

### What this means for you in practice

Because your activity includes staking and other yield-like streams, you effectively face a **positioning decision**:

- A **more conservative stance** (aligned with some KIS interpretations) is: treat receipt of staking/airdrop rewards as taxable income at receipt, with market valuation; later disposal still falls under the virtual-currency disposal rules. citeturn29view2turn27search1turn26search2  
- A **taxpayer-friendly stance** (supported by some court reasoning at least for staking) is: tax only upon disposal under PIT-38, accepting that acquisition cost for rewarded coins may be zero in many cases. citeturn30search9turn21view0

Airdrops appear to be a particularly contentious area: KIS interpretations have explicitly treated airdrops as receipt-taxable in some scenarios, while other reasoning disputes that classification. citeturn29view2turn9view5

## Cost basis, currency conversion, fees, and the FIFO question

This section addresses Questions 7–11 and also overlaps with how PIT-38 Section E is filled.

### FIFO is not the Polish statutory method for PIT-38 crypto

Poland’s crypto rules are designed so that you **do not need to match specific purchases to specific sales** (which is what FIFO/LIFO do). A KIS interpretation quoting legislative justification explains that the method was chosen so it is **not necessary to identify particular expenditures with particular revenues**, and that **all costs incurred in a year are reported regardless of whether revenue occurred**, with carryforward of excess costs to the next year. citeturn21view0

So, to answer directly:
- **Poland does not “require FIFO” in the way many other countries do**; the operational model is pooled annual costs and revenues. citeturn21view0turn18search22  
- The PIT-38 form structure (separate columns for costs incurred in-year, costs carried forward, and “un-deducted costs”) reflects this pooled model rather than a per-lot matching method. citeturn24view0turn25view1turn25view0

### Exchange rates for EUR transactions

For PIT purposes, foreign-currency amounts are converted to PLN using the **average exchange rate published by entity["organization","Narodowy Bank Polski","central bank, warsaw"] (NBP)** from the **last business day preceding**:
- the day you obtain the **revenue** (for revenue amounts), and
- the day you incur the **cost** (for cost amounts). citeturn16search0turn21view0

NBP publishes the relevant average-rate tables (including archives and an API), which makes it possible to evidence the rate used for each transaction date. citeturn17search0turn17search1

### Which fees are part of deductible crypto costs

The PIT rule for crypto costs is that deductible costs include:
- documented expenditures **directly** incurred to acquire virtual currency, and
- costs related to disposal (including documented expenditures to intermediaries covered by AML “obliged institutions”). citeturn21view0turn18search22

A KIS interpretation focused on documentation explicitly treated an exchange “manipulation/transaction fee” shown in exchange reports as a cost that may be included in the crypto-cost bucket (in line with the statutory definition of costs). citeturn20view0turn20view2

A critical limitation: the PIT Act explicitly excludes from costs **expenses related to exchanging one virtual currency into another virtual currency**. citeturn21view0turn18search22  
So, for example, fees/spreads incurred on BTC→ETH or USDT→USDC swaps are the category most directly at risk of being **non-deductible** under the explicit statutory exclusion. citeturn21view0turn18search22

For **withdrawal fees and on-chain gas fees**, the law’s “direct acquisition/disposal” language is the key constraint: fees tightly connected to executing a taxable disposal are easier to defend as “related to disposal,” while wallet-to-wallet transfer costs are harder to defend as direct acquisition/disposal costs under the narrow statutory wording. citeturn21view0turn18search22

### Assets acquired before becoming a Polish tax resident

A particularly relevant KIS interpretation (in a cross-border residency-change fact pattern) states that when a taxpayer becomes a Polish tax resident, **undeducted documented acquisition costs incurred while resident in another country can be shown for the first time in PIT-38 for the year the taxpayer became a Polish resident**, provided those costs were not previously deducted in the other country. citeturn21view0

Applied to your Sweden→Poland transition:
- the documentary focus is on proving the original acquisition expenses (even if incurred while Swedish-resident), and
- converting those historic EUR costs to PLN using NBP rules for the date the cost was incurred (purchase date). citeturn21view0turn16search0

### Is pooling per asset or across all crypto?

Because the reporting method is pooled and PIT-38 requires **totals** for revenue/costs of “odpłatne zbycie walut wirtualnych,” the practical tax computation is **not per-asset FIFO**, but rather **aggregate** revenue and aggregate eligible costs for the year (plus carryforward). citeturn21view0turn24view0turn25view1

## PIT-38 form mechanics for crypto

This section answers Questions 12–15 and gives year-specific form guidance.

### Where crypto goes on PIT-38

Crypto is reported in **Section E** of PIT-38 (the part explicitly dedicated to “odpłatne zbycie walut wirtualnych”). citeturn24view0turn25view0turn25view1

Because PIT-38 form versions changed, field numbers differ:

- **Tax year 2023** (PIT-38(16)): crypto Section E uses fields **34–38**, with tax calculation in Section F. citeturn24view0  
- **Tax year 2024** (PIT-38(17)): crypto Section E still uses fields **34–38**. citeturn25view0  
- **Tax year 2025** (PIT-38(18)): crypto Section E uses fields **36–40** (shifted field numbering). citeturn25view1turn3view0

### What you report: totals, not a transaction-by-transaction attachment

PIT-38 requires reporting of **totals**:
- total annual **revenue** from taxable crypto disposals,
- total eligible **costs incurred in the tax year**,
- eligible **costs carried forward** from prior years, and
- resulting **income** (or, if costs exceed revenue, the “un-deducted costs” that carry forward). citeturn24view0turn25view1turn21view0

The same KIS interpretation citing legislative justification explicitly states the model does **not require identification of specific costs with specific revenues** and requires reporting costs even if revenue is absent. citeturn21view0

### Step-by-step computation aligned to PIT-38 Section E

The core Section E logic (across all three years) is:

1) **Compute total crypto disposal revenue (PLN)**  
Sum PLN values of all events that qualify as paid disposal (crypto→fiat, crypto→goods/service/rights, settling liabilities). citeturn18search22turn27search1

2) **Compute eligible costs incurred in the tax year (PLN)**  
Include documented direct acquisition costs and disposal-related costs; exclude costs linked to crypto→crypto swaps. citeturn21view0turn18search22turn20view2

3) **Add carried-forward costs from prior years**  
These are the “un-deducted” costs from earlier PIT-38 filings. citeturn24view0turn25view1turn21view0

4) **Income and carryforward**  
If revenue exceeds costs: income = revenue − (current-year costs + carryforward costs).  
If costs exceed revenue: income is effectively 0 and the residual becomes **next year’s carryforward costs** (this is a core design: crypto “loss” is not treated like standard PIT losses). citeturn21view0turn29view1turn18search22

### Are crypto gains combined with stock gains inside PIT-38?

PIT-38 is used for both securities-type capital gains and crypto, but they are handled in **separate sections** (securities vs crypto) and PIT law explicitly bars combining crypto disposal income with income taxed under art. 30b(1) (the securities-type regime) for income determination. citeturn26search2turn25view1turn24view0

### Filing deadline

For crypto disposal you file PIT-38 in the annual PIT filing window: **from 15 February to 30 April** of the year following the tax year (with rules on early submissions). citeturn22search8

## Documentation and audit readiness

This section answers Questions 16–19.

### What records you must keep

Polish crypto reporting is self-assessed: you must be able to substantiate (1) taxable disposal revenue and (2) eligible costs. A KIS interpretation stresses that the burden is on the taxpayer to prove that an expense was incurred and meets statutory cost criteria, and that costs must be properly documented. citeturn21view0

In practice, documentation typically includes:
- exchange trade history exports (CSV/PDF), including fee fields,
- deposit/withdrawal logs (exchange-side),
- bank transfer confirmations for fiat on-ramps/off-ramps,
- self-custody wallet transaction histories (TXIDs, timestamps, addresses),
- your PLN conversion workpapers showing the NBP rate used for each date, and
- reconciliation evidence showing that “transfers” are non-taxable movements rather than disposals. citeturn19view0turn21view0turn17search0turn16search0

### Is a formal “ewidencja walut wirtualnych” required?

The PIT crypto framework focuses on what must appear in the tax return and what can be defended as documented costs; it does not impose (in the core PIT-38 crypto provisions) a single mandatory format for a “register.” The KIS documentation-focused interpretation emphasizes an open approach to evidence rather than a specific statutory book/register format. citeturn19view0turn20view2

### What Art. 30b(6) and 30b(6a) require (and why it matters)

A KIS interpretation quotes the statutory obligation that:
- after year-end, the taxpayer must report crypto disposal income in the annual return (PIT-38), and
- the taxpayer must also report qualifying crypto costs **even if no revenue was earned that year**. citeturn15view0turn21view0

This is why a “buy-and-hold only” year can still require a PIT-38 filing in Poland if you incurred acquisition costs that year and want them recorded for carryforward. citeturn21view0turn18search22

### Are Binance/Kraken CSVs “enough”?

A KIS interpretation focused on evidence accepted that exchange reports (including ones that may not contain all personal identifiers) can constitute evidence in a tax proceeding, and it reaffirmed the general tax-procedure rule that **anything that helps clarify the case and is lawful may be admitted as evidence**. citeturn19view0turn20view2

Practically, for your setup (two exchanges + multiple self-custody chains), CSVs are often necessary but not always sufficient on their own—you usually want bank confirmations and wallet TXIDs to corroborate flows, timestamps, and ownership of addresses. citeturn19view0turn20view2turn21view0

### How long to keep records

Tax liabilities generally become time-barred after a statutory limitation period; the tax ordinance provides a baseline **5-year limitation period** (counted from the end of the calendar year in which the tax payment deadline passed). citeturn31search0  
For crypto, keeping records at least through that window (and longer if there are limitation suspensions or ongoing proceedings) is the standard defensible posture. citeturn31search0turn19view0

## Special situations: platform collapses, theft, and “losses”

This section addresses Question 6 and clarifies a common misconception.

### “Losses” in Poland’s PIT-38 crypto system

Poland’s crypto rules are structured so that **a PIT “loss” is not recognized in the normal way** for this category; instead, if costs exceed revenue, the difference carries forward as future costs (and the statute explicitly excludes typical loss-treatment mechanisms for crypto disposal). citeturn29view1turn18search22turn21view0

### What happens if crypto is stolen or lost in a collapse

If you **incurred documented acquisition costs**, those costs can still exist in the pooled-cost system even if the corresponding coins are later stolen or become unrecoverable; a published interpretation about stolen crypto indicates that acquisition costs are still to be shown as crypto costs and can roll forward under the standard carryforward mechanism. citeturn14search1turn21view0

For Celsius/BlockFi-type collapses, the practical (tax) question becomes:
- do you have documented acquisition costs that are already in your PIT-38 cost pool (or can be introduced consistent with the residency-change logic), and
- do you later receive any compensation/distribution (which may require separate tax analysis depending on its legal character). citeturn21view0turn13search11