# Cost Basis and Valuation Rules for Crypto Tax Under Polish PIT

## Legal framework for “virtual currency” disposals and what is taxable

Polish PIT rules treat most retail (non-business) crypto investing under the **capital gains** regime (19%) when you perform an **“odpłatne zbycie waluty wirtualnej”** (paid disposal of virtual currency). The statutory definition is crucial because it determines **which events create taxable “przychód”** and which do not.

Under **Art. 17 ust. 1f ustawy o PIT**, *“paid disposal of virtual currency”* includes (i) exchanging virtual currency for **legal tender**, **goods**, **services**, or a **property right other than virtual currency**, and (ii) using virtual currency to **settle other liabilities**. citeturn33view0

A direct implication of this definition is that **crypto-to-crypto exchanges are not listed as a taxable disposal event** under Art. 17 ust. 1f. In practical terms, swapping BTC→ETH, or BUSD→FDUSD→USDC (stablecoin “auto-conversion”) **does not create PIT revenue at the swap moment** (though it may affect later reporting because it changes what you hold). citeturn33view0

The “virtual currency” capital-gains regime is then taxed at **19%**, with the annual taxable result computed as a **yearly net**: the **difference between the sum of revenues from paid disposals and the deductible costs determined under Art. 22 ust. 14–16**. citeturn34view1

## PLN valuation rules and NBP exchange-rate rules

### The core conversion rule in Art. 11a

Polish PIT has one central conversion mechanism for **amounts expressed in foreign currency** (EUR, USD, etc.): **Art. 11a**.

Art. 11a ust. 1 (income side) and ust. 2 (cost side) both point to the **NBP “kurs średni” (average rate)** from the **last business day preceding** the relevant day (income receipt day or cost incurrence day). citeturn32view0

Because your disposals on entity["company","Binance","crypto exchange"] and entity["company","Kraken","crypto exchange"] are primarily **crypto→EUR** conversions, your tax-relevant values often become “foreign-currency amounts” (EUR), which then must be translated into PLN using Art. 11a. citeturn32view0turn33view0

### Confirming what Art. 11a actually says (and correcting the ust. number)

You referenced “Art. 11a ust. 2” as the rule for converting income. In the consolidated wording shown in the official text as of late 2025, **income conversion is Art. 11a ust. 1**, while **cost conversion is Art. 11a ust. 2**. citeturn32view0

The critical statutory phrase (verbatim excerpt) is:

> “**…z ostatniego dnia roboczego poprzedzającego dzień uzyskania przychodu**” citeturn32view0

And the corresponding cost-side phrase is:

> “**…z ostatniego dnia roboczego poprzedzającego dzień poniesienia kosztu**” citeturn32view0

### How this applies to your common transaction types

#### Selling USDC for EUR on an exchange

**What is “income”?**  
For a taxable disposal, the taxable “przychód” is driven by the disposal event defined in Art. 17 ust. 1f (exchange to legal tender). When you sell USDC and receive **EUR**, your receipts are denominated in a **foreign currency amount (EUR)**, so Art. 11a applies to the EUR amount. citeturn33view0turn32view0

**Which NBP rate? trade-day vs. day-before?**  
Art. 11a’s rule is not “trade-day rate.” It is the **NBP average rate from the last business day preceding the day the income is obtained**. citeturn32view0  
So, for a disposal executed on date **D**, you typically use the NBP average EUR rate from **the last business day before D**.

**What if the trade happens on a Saturday?**  
Saturday is not a business day for NBP tables, and—more importantly—Art. 11a explicitly requires the **last business day preceding the income day**. So if the transaction date is Saturday, the relevant “last business day preceding” is normally **Friday** (unless Friday was a holiday, in which case it would be the prior business day). citeturn32view0

#### Crypto purchased with EUR on an exchange

When you buy crypto using EUR, your “wydatki…poniesione w walutach obcych” (costs incurred in foreign currency) are translated to PLN under Art. 11a ust. 2 using the **NBP average rate from the last business day preceding the cost-incurrence day**. citeturn32view0

In plain terms, for purchase date **D**:

- **Cost in PLN = EUR spent × NBP(EUR) from last business day before D**. citeturn32view0

#### Does the “last business day before” rule apply to both revenue and cost basis?

Yes, but via **two different ustępy**:

- **Income / revenue** in foreign currency → Art. 11a ust. 1 (day-before rule). citeturn32view0  
- **Costs** in foreign currency → Art. 11a ust. 2 (day-before rule). citeturn32view0

### USDC salary receipts and how to pick USD vs. EUR for valuation

A USDC salary payment is usually a **separate PIT event** (employment / services income), distinct from later capital-gains taxation on disposal.

**Step one: value the “salary income” at receipt**  
Employment income includes not only cash but also the **value of benefits in kind** (“świadczenia w naturze”) and equivalents, with valuation tied to market pricing rules in the PIT act. citeturn32view0  
A recent interpretation concerning remuneration paid in crypto states that **the value of income is the value of the received benefit expressed in traditional currency, i.e., the equivalent value of the received crypto**. citeturn28view1

**Step two: convert to PLN**  
If you establish the salary’s value in a foreign currency (commonly USD or EUR), then Art. 11a governs conversion of that foreign-currency amount into PLN using the **NBP average rate from the last business day before the receipt day**. citeturn32view0

**Should USDC be treated as “USD” because it is pegged?**  
Legally, USDC is a **virtual currency**, not “USD.” The statute does not provide an “official NBP USDC rate.” What the law requires is that (i) you determine the value of the received benefit and (ii) if that value is expressed in foreign currency, apply Art. 11a to convert it to PLN. citeturn32view0turn28view1

Practically:
- If USDC is trading at ~1.00 USD, many taxpayers approximate **USDC amount × 1.00 USD** and then convert USD→PLN via NBP.  
- If USDC is **depegged** (e.g., 0.97 USD or 1.02 USD), a defensible approach is to use the **actual market price** (e.g., from a reputable exchange snapshot at receipt time), because employment/benefit valuation is anchored in market value logic rather than a peg assumption. citeturn32view0turn28view1

### Getting the correct NBP “kurs średni” values

For operational use, you typically source NBP average rates from the adult official publications:

- The entity["organization","Narodowy Bank Polski","central bank, warsaw"] **Table A (average exchange rates)** pages, citeturn3search1  
- Or the official **NBP Web API** (useful for automated extraction of the “last business day” rate in scripts / spreadsheets). citeturn3search0

## Cost basis and deductible costs for crypto disposals

### The statutory crypto cost rule: Art. 22 ust. 14–16

Polish PIT **does not use “basis per lot” as the primary statutory mechanism** for virtual currencies. Instead, it defines what counts as deductible costs and how they are recognized across years.

Under **Art. 22 ust. 14**, deductible costs for paid disposal of virtual currency are:

- **documented expenses directly incurred to acquire virtual currency**, and  
- **costs related to disposal**, including documented expenses paid to entities providing exchange-type services referenced in AML rules. citeturn32view2

Recognition across years:

- **Costs are deducted in the year they are incurred** (Art. 22 ust. 15). citeturn32view2  
- If costs exceed crypto disposal revenues in a year, the **excess is carried forward** and increases the next year’s costs (Art. 22 ust. 16). citeturn32view2

Additionally, **Art. 30b ust. 6a** requires that you **report crypto costs in PIT-38 even when you have no crypto-disposal revenues that year**—which is directly connected to preserving the carryforward mechanism. citeturn32view3turn32view2

A separate 2025 interpretation addressing multi-year reporting underscores that the “carryforward mechanics” exist precisely because costs can be reported and then used later, and it discusses timing expectations for reporting historical costs. citeturn28view2

### What costs are deductible vs. not deductible in practice

Because Art. 22 ust. 14 uses a “directly incurred” constraint, classification is often where disputes arise.

**Usually deductible (when properly documented and “direct”)**

- **Purchase price of the crypto being sold** (e.g., EUR paid to acquire the virtual currency). This is the paradigm “direct expense to acquire.” citeturn32view2turn32view0  
- **Exchange trading fees / commissions** that attach to buying or selling (spot trading commission). A 2025 interpretation explicitly accepted certain commissions connected with selling virtual currencies (including cases where the fee was charged in PLN and where it was charged in virtual currency). citeturn17view0  
- **Certain sale-related fees charged in crypto**: the same interpretation treated some “fees during sale” as acceptable costs even when deducted in virtual currency (fact-pattern dependent). citeturn17view0

**Often disputed or frequently rejected (riskier)**

- **Deposit/top-up intermediary fees** (e.g., a 1% fee charged by an intermediary app for funding the exchange) and **fees for transferring proceeds from an app to a bank** were rejected as not directly tied to acquisition/disposal in a 2025 interpretation (fact-pattern: fees related to depositing/withdrawing fiat rather than buying/selling the virtual currency). citeturn17view0  
- **Withdrawal fees from an exchange** and **blockchain network fees (gas)**:  
  - If the fee is **integral to executing the disposal** (e.g., on-chain fee needed to deliver crypto to a counterparty as part of a taxable settlement), an argument exists that it is “related to disposal.”  
  - If it is merely moving assets between your own wallets or for convenience, it is harder to defend as “directly related.”  
  This follows from the statute’s “directly incurred” framing. citeturn32view2  
  (This area is highly fact-specific and where taxpayers often seek individual rulings.)
- **VPN subscriptions, hardware wallets, general security tools**: typically do not meet “directly incurred to acquire” nor “related to disposal” as those phrases are used in Art. 22 ust. 14, so they are usually treated as **non-deductible** for PIT-38 crypto disposal purposes. citeturn32view2

### If crypto was received “for free” (airdrop, some DeFi distributions)

For PIT-38 crypto disposal purposes, **Art. 22 ust. 14 focuses on documented expenses**. If you received tokens without paying anything and cannot show a direct acquisition expense, then under a strict reading your **disposal cost can be effectively zero**, even though you might have later taxable revenue at disposal. citeturn32view2turn34view1

However, there is a major practical complication: whether the receipt itself is taxed as a separate PIT event.

A 2025 airdrop interpretation states (in its presented reasoning) that tax authorities may treat **the receipt of tokens in an airdrop as taxable “przychód z praw majątkowych” at the moment of receipt**, valuing the received tokens and tying it to Art. 18 in connection with Art. 11 ust. 1. citeturn25view1  
This is contested reasoning in some taxpayer arguments and can be litigation-prone, but the existence of this interpretive stance is important for cost-basis planning. citeturn25view1

### Crypto received as salary or payment for services: cost basis linkage

If you receive virtual currency as part of compensation (salary/bonus) and it was taxed as ordinary income (e.g., shown on PIT-36), authorities have accepted that **the already-taxed value can be treated as a cost when you later dispose of that crypto in PIT-38**, to avoid double taxation.

A 2025 interpretation explicitly addressed a **bonus in crypto** that had been reported as employment income and held that treating that value as a PIT-38 cost on later disposal was correct in that case. citeturn30view0turn30view3

This supports the practical rule-of-thumb you asked for:

- **Salary received in USDC**: your later PIT-38 cost for those units is typically the **PLN value that was (or should have been) recognized as income at receipt**, provided you can document that valuation and taxation track. citeturn30view0turn28view1

## FIFO, per-asset queues, cross-year holdings, and stablecoin migrations

### Is FIFO mandated for crypto disposals?

For virtual currencies, the statute computes taxable income **annually** as the difference between:

- the **sum of revenues** from paid disposals of virtual currencies, and  
- the **costs per Art. 22 ust. 14–16**. citeturn34view1turn32view2

This structure **does not mandate matching specific acquisition lots to specific disposals** (FIFO/LIFO/specific identification) the way some other jurisdictions do.

Moreover, Polish PIT explicitly uses FIFO in other contexts. In the same Art. 30b, **FIFO is expressly stated for certain investment-fund participation units when identification is not possible**. citeturn32view3  
That serves as strong evidence that when the legislature wants FIFO, it writes FIFO—yet it does not do so for virtual currency disposals. citeturn32view3turn34view1

**Conclusion:** FIFO is **not explicitly mandated** for virtual currency taxation under the standard PIT-38 scheme; it is more of an internal accounting convention some taxpayers use, but it is not the statutory computational backbone. citeturn34view1turn32view2

### Is FIFO applied per-asset or across all crypto?

Because the tax calculation is based on **aggregate sums** (“sumą przychodów… z tytułu odpłatnego zbycia walut wirtualnych”) and the crypto cost bucket defined in Art. 22 ust. 14–16, the statute operates as **a pooled, category-level computation**, not separate per-asset queues. citeturn34view1turn32view2

### Crypto acquired before becoming Polish tax resident

Your question is effectively about whether Poland applies a “step-up” in basis at the moment of becoming tax resident.

The crypto-specific cost rule in Art. 22 ust. 14 is anchored in **documented direct acquisition expenses**; it does not include an explicit “market value at residency start” reset. citeturn32view2

So, absent a special rule in the PIT act for residency-change step-ups (none appears in the crypto cost provisions shown), the conservative approach is:

- retain **historical acquisition documentation**,  
- convert the historical amounts into PLN as needed using Art. 11a, and  
- use those documented acquisition expenses within the Art. 22 ust. 14 framework when disposals are later taxed in Poland. citeturn32view2turn32view0

Because residency-change cases can involve tax-treaty interactions and factual complexity, taxpayers often seek professional advice or individual rulings for high-value positions.

### Stablecoin “auto-conversion” (e.g., BUSD→FDUSD→USDC)

If the exchange forces a conversion between virtual currencies and you receive another virtual currency, that conversion itself generally falls outside the Art. 17 ust. 1f definition of taxable disposal (no exchange to legal tender/goods/services/property-right-other-than-virtual-currency). citeturn33view0

Under the pooled-cost approach, such a conversion typically does not create a new revenue item; it mainly affects **what asset you later dispose of** and how you document continuity (and any fees, if applicable). citeturn33view0turn32view2

## Worked examples for correct PLN conversion and multi-year cost handling

The examples below are mechanical demonstrations of the rules; they use simplified numbers so the focus stays on **which day’s NBP rate is legally required**.

### Example: USDC→EUR sale on a Saturday

- Trade execution: **Saturday 2026-03-14**  
- You sell **1,000 USDC** and receive **920 EUR** (net after trading fee).  
- Legal rule: foreign-currency income is converted using the **NBP average rate from the last business day preceding the income day**. citeturn32view0  
- “Income day” aligns with the **disposal event** (exchange to legal tender) defined in Art. 17 ust. 1f. citeturn33view0  

Assume:
- NBP EUR average rate from **Friday 2026-03-13** = **4.50 PLN/EUR** (illustrative).

Then:
- **Revenue in PLN = 920 EUR × 4.50 = 4,140 PLN**. citeturn32view0turn33view0

### Example: Buying BTC with EUR and computing the PLN “cost bucket”

- Purchase date: **Monday 2026-02-02**  
- You spend **2,000 EUR** to buy BTC.  
- Legal rule: costs incurred in foreign currency are converted using **NBP average rate from the last business day preceding the cost-incurrence day** (Art. 11a ust. 2). citeturn32view0  

Assume:
- NBP EUR average rate from **Friday 2026-01-30** = **4.55 PLN/EUR**.

Then:
- **Cost added to the crypto cost bucket = 2,000 × 4.55 = 9,100 PLN**. citeturn32view0

If you have no crypto disposals in 2026, that 9,100 PLN cost is still reportable and, if it exceeds revenue, it carries forward. citeturn32view2turn32view3

### Example: USDC salary receipt and later disposal

**Receipt (employment income event)**  
- You receive **3,000 USDC** as a bonus.  
- A crypto remuneration interpretation states the income value is the **traditional-currency equivalent of the crypto received**. citeturn28view1  
- Convert any foreign-currency valuation to PLN via Art. 11a. citeturn32view0  

Assume:
- At receipt time, USDC trades at **0.995 USD** (slight depeg).  
- Value in USD = 3,000 × 0.995 = **2,985 USD**.  
- NBP USD rate from last business day before receipt = **4.00 PLN/USD**.

Then:
- **Salary income recognized ≈ 2,985 × 4.00 = 11,940 PLN**. citeturn32view0turn28view1  

**Later disposal (PIT-38 virtual currency)**  
When you later dispose of those USDC in a taxable event, the bonus interpretation supports treating the already-taxed value as a **PIT-38 cost**, avoiding taxing the same economic inflow twice. citeturn30view0turn30view3

### Example: Multi-year carryforward without FIFO

- Year 1: buy crypto (cost bucket increases), no disposals.  
- Year 2: sell crypto for EUR (revenue), offset by cost bucket.

This is driven by:
- yearly net rule for crypto disposals (sum of revenues minus costs), citeturn34view1turn32view2  
- deduction timing and carryforward in Art. 22 ust. 15–16, citeturn32view2  
- obligation to report costs even with zero revenues in Art. 30b ust. 6a. citeturn32view3  

## Record-keeping, documentation, and retention

### Does Art. 30b ust. 6 require an “ewidencja walut wirtualnych”?

In the consolidated statutory text shown, **Art. 30b ust. 6** imposes an obligation to file the annual return and compute tax, and **Art. 30b ust. 6a** requires reporting crypto costs even if there were no disposal revenues. There is **no mention of a mandated “ewidencja walut wirtualnych” format** in this part of the statute. citeturn32view3

So, rather than a rigid statutory “register,” the practical obligation is to maintain **sufficient evidence** to substantiate:

- annual totals of revenue from taxable disposals, citeturn34view1turn33view0  
- annual costs incurred (and carried forward), citeturn32view2turn32view3  
- the foreign-currency→PLN conversions under Art. 11a, citeturn32view0  
- and any “already taxed as salary” linkage used as a PIT-38 cost. citeturn30view0turn28view1  

### Are exchange CSV exports and confirmations sufficient?

A 2025 interpretation on documentation indicates that **generated reports and transfer confirmations** (even without complete personal data) **can serve as tax evidence** for crypto transactions, depending on content and context. citeturn31search7

At minimum, the documentation should allow you to reconstruct:

- timestamp/date (and time zone)  
- platform/account identifier  
- asset and amount disposed/acquired  
- settlement currency (e.g., EUR) and amount received/paid  
- fees (type, amount, currency)  
- wallet addresses / transaction IDs for on-chain transfers (where relevant)  
- the exact NBP rate date used (last business day before D) and the PLN computation trail citeturn32view0turn31search7  

### Per-transaction detail vs. annual totals

Because the tax computation is annual-aggregate, the statute is written in “sum of revenues” and “cost bucket” terms, not lot-by-lot matching. citeturn34view1turn32view2  
That said, you generally need **transaction-level source evidence** to prove the annual totals and the correct Art. 11a conversion dates, especially when multiple exchanges and wallets are involved. citeturn31search7turn32view0

### Real-time maintenance vs. reconstruction at filing time

There is no explicit “must be maintained in real time” rule in the cited statutory excerpts, but Art. 30b ust. 6/6a makes you responsible for correct annual reporting, and the documentation interpretation confirms that reports can be used as evidence. citeturn32view3turn31search7  
Accordingly, reconstruction from exchange records is generally possible, but you must ensure conversion dates and PLN computations are correct.

### How long must records be retained?

A practical retention baseline is driven by the statute of limitations for tax liabilities. Under **Ordynacja podatkowa Art. 70 §1**, a tax liability generally **expires after 5 years**, counted from the end of the calendar year in which the payment deadline passed. citeturn31search0

Therefore, keeping crypto tax records for **at least 5 years** after the relevant PIT payment deadline is a common minimum, with the caveat that limitation periods can be affected by specific suspension/interruption rules in Ordynacja (outside the scope of Art. 70 §1 alone). citeturn31search0