# Tax Treatment of Crypto Losses from Celsius and BlockFi Bankruptcies for a Polish Resident

## Scope, assumptions, and why this is legally tricky

This report addresses how a **Polish tax resident** (today) should think about the tax treatment—under **Polish PIT rules for “virtual currencies” reported on PIT-38**—of crypto that became inaccessible on centralized lending/custody platforms that later entered bankruptcy, with possible partial recoveries. It also explains how to reflect those events in a FIFO-style tracker without creating tax outcomes that are hard to defend under Polish law. citeturn23view0turn21view1

Two complications drive most of the uncertainty:

1. **Polish crypto-PIT rules tax “paid disposal” (odpłatne zbycie) rather than mark-to-market value changes**, and the Ministry of Finance emphasizes that **a “tax loss” does not arise on crypto disposals**; instead, unused eligible costs roll forward (“nadwyżka kosztów”). citeturn23view0turn16view2turn16view0  
2. Whether sending BTC to an “interest/lending” account is merely a **non-taxable transfer** or a **taxable exchange of crypto for a claim (a property right)** can depend on the legal nature of the platform relationship (custody vs title-transfer lending). In the Celsius Earn context, U.S. bankruptcy decisions and commentary emphasize that the customer terms purported to **transfer title/ownership** of deposited assets to the platform; BlockFi likewise distinguished between “wallet/custody” vs “interest-bearing” accounts in bankruptcy outcomes. citeturn9search6turn10search17turn15search1turn15search4

This is general tax-technical research, not individualized tax/legal advice.

## Platform timeline and what “partial recovery” can look like

### Celsius (withdrawal freeze, bankruptcy filing, and distributions)
Celsius halted withdrawals in mid-June 2022 and filed for Chapter 11 bankruptcy in July 2022. citeturn15search7turn15search11

Celsius later emerged from Chapter 11 and began creditor distributions in **2024**, including distributions in cryptocurrency and U.S. dollars (and, for some creditors, equity in a reorganized mining business). citeturn26search0turn26search2turn26search6

### BlockFi (withdrawal pause, bankruptcy filing, and distributions)
BlockFi paused withdrawals/limited platform activity on **November 10, 2022**, followed by a Chapter 11 filing later in November 2022. citeturn15search10turn15search6

The BlockFi plan was confirmed and became effective in **October 2023**, and distributions commenced starting in **2024** for certain classes. citeturn26search5turn26search1

Bankruptcy outcomes also emphasized account-type distinctions: courts allowed returns to customers with certain **non‑interest-bearing “wallet” accounts**, while disputes existed around assets linked to interest-bearing products. citeturn15search1turn15search4

## Polish PIT crypto framework that governs what is and is not deductible

### What Poland taxes: “paid disposal” of virtual currency
Under the Polish PIT Act, “paid disposal” of virtual currency is defined as exchanging virtual currency for:
- legal tender,
- goods/services, or
- a property right other than a virtual currency,
or using virtual currency to settle other obligations. citeturn16view1turn23view0

The official Ministry of Finance tax portal also highlights that **crypto-to-crypto exchanges are not taxed** (they are outside “paid disposal” in this regime). citeturn23view0

### What costs are allowed, and how “loss” works in Poland for crypto
For PIT-38 crypto reporting, deductible costs are narrowly defined as:
- documented expenses directly incurred to acquire virtual currency, and
- costs connected with disposal (e.g., certain documented intermediary fees). citeturn16view2turn23view0

If eligible costs exceed revenue from taxable disposals in a year, **Poland does not produce a “crypto loss” in the way many countries do**. Instead:
- taxable income is effectively floored at **0**, and  
- the **excess costs carry forward** to future years as costs for future virtual-currency disposals. citeturn16view2turn23view0turn21view1

This is reinforced in two places:
- The PIT Act excludes losses from paid disposal of virtual currencies from the standard “deduct losses over 5 years” mechanism. citeturn16view0  
- The Ministry of Finance guidance explicitly states: “With crypto paid disposal, a loss never occurs,” and you carry forward the excess costs instead. citeturn23view0

### Filing mechanics: PIT-38 “virtual currencies” sections and cost carry-forward
The official PIT-38 brochure (2025 tax year edition) explains that:
- PIT-38 is used when you had revenue **or incurred costs** from paid disposal of virtual currencies, citeturn21view0  
- the virtual-currency section is completed even if you incurred costs but had no disposal revenue, citeturn21view1  
- positions 36–40 operationalize revenue, current-year costs, prior-year unutilized costs, computed income, and unutilized costs to carry forward. citeturn21view1  
It also notes foreign-currency conversion principles (NBP average rate rules referenced to the PIT Act). citeturn21view0

## Answering the core questions under Polish rules

### Can losses from Celsius/BlockFi bankruptcies be “claimed” in Poland?
If by “loss” you mean **deducting the collapsed value** (e.g., claiming the market value of BTC lost when withdrawals stopped), **Polish crypto-PIT rules do not provide a direct legal mechanism**. The eligible cost base is limited to documented acquisition costs and disposal-related costs, and the Ministry of Finance position is that no crypto “loss” arises—only a carry-forward of unused eligible costs. citeturn16view2turn23view0turn16view0

If by “loss” you mean **your historical acquisition costs for the BTC/DOT that ended up stuck**: those costs may still be valuable in Poland because:
- eligible acquisition costs are claimed (and, if unused, carried forward) within the PIT-38 crypto cost mechanism, independent of whether you successfully recover the same coins later. citeturn16view2turn21view1turn23view0

The high-level practical outcome in Polish PIT terms is:

- **Bankruptcy itself does not create a special deductible event** for virtual currency.  
- The Polish system can still let you use historic acquisition costs to offset future taxable crypto disposal revenues (your own sales/exchanges for fiat/goods/services/rights), because unused costs roll forward. citeturn16view2turn23view0turn21view1

### When does the “loss” occur for Polish tax purposes?
Under the statutory definition, the pivotal date for Polish crypto taxation is when an **“odpłatne zbycie”** occurs (exchange for fiat/goods/services/other property rights, or settlement of obligations). citeturn16view1turn23view0

Therefore, the following events are **not automatically taxable disposal moments** under Polish crypto rules:
- the platform halting withdrawals,
- the platform filing for bankruptcy,
- courts discussing whether assets are in the estate,
- the mere fact that recovery expectations fall. citeturn16view1turn23view0turn15search11turn15search6

What **can** become relevant under Polish rules is the first moment you actually **exchange** something that is still classified as “waluta wirtualna” for:
- **fiat (USD/EUR/PLN)**, or
- **a non-crypto property right** (e.g., shares), or
- goods/services. citeturn16view1turn23view0

Because Celsius/BlockFi recoveries can include **USD** and sometimes **non-crypto instruments**, one must analyze the distributions carefully: a distribution in fiat or in a non-crypto property right resembles the forms of consideration listed in the “paid disposal” definition, but the counterargument is that you may be receiving settlement of a **claim** rather than directly disposing of “waluta wirtualna.” The statute does not have a crypto-specific rule for bankrupt-platform “claims workflows,” which is why treatment can hinge on whether your earlier deposit is characterized as custody or as an exchange for a claim. citeturn16view1turn23view0turn9search6turn15search4

### Is depositing crypto to a custodial platform a “disposal” in Poland?
Under Polish law and guidance, **transfers that are not exchanges for fiat/goods/services/other rights are not listed as taxable crypto events**; the official definition focuses on exchange/settlement transactions. citeturn16view1turn23view0

However, “depositing” to a centralized platform can fall into two legally different economic forms:

**Custody/wallet-style relationship (title stays with customer).**  
A pure custody transfer is easier to view as a **non-taxable movement of the same asset** (analogous to moving between your wallets). BlockFi bankruptcy reporting highlighted that certain wallet customers could receive assets back, while other account types differed—supporting that “wallet/custody” may function as true custody. citeturn15search1turn15search4

**Interest-bearing / lending relationship (title-transfer; customer holds a claim).**  
In Celsius Earn, U.S.-law commentary on the bankruptcy emphasized that the terms were treated as transferring ownership/title of deposited assets into the bankruptcy estate—i.e., depositors become unsecured creditors with a claim rather than owners of specific coins. citeturn9search6turn10search17turn9search14  
This is conceptually close to the Swedish Tax Agency’s example of lending via a centralized platform: the depositor is viewed as exchanging BTC for a receivable (a claim to get back equivalent BTC), which is treated as a disposal in Sweden. citeturn29view0

**Polish risk point:** If the Polish tax authority analogized an interest-bearing “deposit” to an exchange of BTC for a **property right (claim)**, that may fall inside “paid disposal” (exchange for a property right other than virtual currency). citeturn16view1turn23view0

Polish law does not provide a single explicit rule that “lending crypto is/is not disposal,” so the most defensible stance depends on the **actual account type and contractual terms** (custody vs title-transfer lending). citeturn9search6turn15search4turn23view0

### If the economic loss happened in 2022 while resident in Sweden, can it be claimed in Poland now?
Polish PIT is residency-based:
- A person with “place of residence” in entity["country","Poland","republic of poland"] (center of vital interests or >183 days) is subject to unlimited tax liability on worldwide income. citeturn25view0  
- A non-resident is generally taxed only on Polish-sourced income. citeturn25view0

So, as a general rule:
- a 2022 taxable event that occurred while you were a Swedish tax resident would be handled under entity["country","Sweden","kingdom of sweden"] rules for that year, not by retroactively “claiming it” in Poland later. citeturn25view0turn29view0  
- Poland does not import foreign-year capital losses into PIT-38 crypto reporting; Poland’s crypto mechanism is built around reporting eligible costs and rolling forward unused costs within the Polish PIT-38 framework. citeturn21view1turn23view0turn16view2

A key practical implication is that **the same economic collapse can map to different taxable “realization” dates** depending on characterization:
- If your deposit to a lending program is treated as a disposal (exchange for a claim), then the relevant “disposal date” could be the deposit date (potentially pre-2022), and later bankruptcy is a loss on the claim. This resembles the Swedish approach to centralized platform lending. citeturn29view0turn9search6  
- If it is treated as custody/non-disposal, then bankruptcy doesn’t create a taxable disposal in Poland; you mainly preserve acquisition costs for future offsets. citeturn16view1turn23view0turn16view2  

If you need to amend Swedish filings, entity["organization","Skatteverket","swedish tax agency"] notes you can appeal decisions relating to the past six income years (e.g., in 2026, income year 2020 onward). citeturn27search1

## FIFO and tracker implications that stay aligned with Polish PIT realities

### Important: Polish PIT does not require FIFO, but your tracker still needs a consistent method
Polish PIT-38 crypto reporting is structured around **annual totals of revenue and eligible costs**, with explicit carry-forward of unused costs. citeturn16view2turn21view1turn23view0  
This is different from jurisdictions that require strict lot accounting (FIFO/LIFO). In practice, many Polish taxpayers keep a tracker anyway to substantiate totals, but the statutory framework is **cost-pool-like** (current-year costs plus prior-year unused costs). citeturn21view1turn23view0

So the FIFO questions are best answered in two layers:

- **Asset/inventory layer (what you actually hold / can access)**  
- **Polish PIT layer (how eligible costs and taxable “paid disposals” are computed)** citeturn16view1turn16view2turn23view0

### If BTC was sent to Celsius/BlockFi and never recovered, should FIFO lots be removed?
For inventory accuracy, you eventually need your tracker to reflect that you do **not** control those coins. For Polish PIT, however, creating an artificial “sale at zero” is risky because Polish taxation hinges on **actual paid disposal events**, and a bankruptcy loss is not listed as such. citeturn16view1turn23view0turn16view2

The most defensible tracker approach (while the bankruptcy is unresolved) is:

- Keep the original BTC lots intact but **move them into a separate “bankruptcy claim / frozen” account** (a non-taxable internal transfer). This preserves lot provenance and avoids booking a fictitious taxable disposal. citeturn16view1turn23view0

Once proceedings are clearly final and you know nothing further will be received, you have two practical options for the inventory layer:

- **Conservative (tax-safe) inventory write-off as non-taxable:** remove the unrecovered quantity using a tracker-specific “lost/abandoned” event classified as **non-taxable** (not as a “sale”). This aligns with the idea that Polish PIT taxes disposals, not mere losses. citeturn16view1turn23view0  
- **Do not fabricate proceeds:** avoid a “sale for 0 PLN,” because that implicitly asserts an “odpłatne zbycie” that did not occur. citeturn16view1turn23view0

### If partial recovery occurred, how should FIFO lots be adjusted?
If you eventually receive (say) 30% of your BTC back, you are not “choosing which satoshis return.” For internal consistency, pick a method and document it.

Two defensible mechanical choices for a FIFO tracker are:

**Method A: Allocate recovery to the oldest lots (FIFO-consistent).**  
- If 1.0 BTC was locked (assembled from multiple buys) and you receive 0.30 BTC, treat the returned 0.30 BTC as coming out of the oldest lots first.  
- The remaining 0.70 BTC stays in your “claim/frozen” bucket (and may later be marked unrecovered/non-taxable loss for inventory only).

**Method B: Pro-rata haircut across all locked lots (economically intuitive).**  
- Reduce each locked lot by 70% and release 30% from each lot back to accessible holdings.  
- This can be easier to justify economically if the bankruptcy plan explicitly applies a uniform percentage recovery to claims.

Polish PIT does not explicitly mandate FIFO lots, but you must be able to reconcile totals and valuations used for any taxable disposals you later report. citeturn21view1turn23view0

### Practically, should the crypto sent to Celsius/BlockFi be treated as still in the FIFO queue or consumed/lost?
A practical, Poland-aligned approach is:

- **While bankruptcy is unresolved:** treat it as “still yours but frozen,” i.e., keep it in a separate “bankruptcy claim/frozen” account (so it is not accidentally sold/spent in the tracker). citeturn26search0turn26search1turn23view0  
- **As distributions come in:** move amounts from the claim account back to custody/exchange accounts as “transfers,” not sales. Later, when you sell recovered crypto for fiat or use it to buy goods/services, that is the clear Polish taxable disposal moment. citeturn16view1turn23view0  
- **For unrecovered remainder:** treat it as an inventory write-off (non-taxable event) once finality is clear; do not rely on it as a Polish “deductible loss” event. citeturn23view0turn16view2  

This aligns with the Polish framing that taxable events are exchanges/settlements, not the mere disappearance of value or access. citeturn16view1turn23view0

## Documentation and PIT-38 reporting in Poland for bankrupt-platform situations

### What documentation you should retain
Because Polish authorities state that intermediaries (exchanges/platforms) generally do **not** issue Polish PIT information forms for your crypto transactions, your documentation burden is high. citeturn23view0

For Celsius/BlockFi bankruptcy-related positions, the strongest documentation stack typically includes:

- **Acquisition evidence (to substantiate eligible costs):** trade confirmations, exchange CSVs, bank transfer receipts, and fee statements showing the amounts spent to acquire BTC/DOT and any directly related acquisition fees. citeturn16view2turn23view0  
- **On-chain transfer evidence** from your self-custody addresses to the platform deposit addresses (e.g., blockchain explorer transaction IDs referencing your BTC address and the platform receiving addresses you listed). This links your acquisition history to the bankruptcy claim. citeturn23view0  
- **Platform account statements** showing balances before the freeze and the account type (wallet vs interest/lending product). This is crucial for the “is deposit a disposal?” characterization risk. citeturn15search4turn9search6  
- **Bankruptcy claim and distribution records** (PDFs/emails): claim ID, scheduled claim amount, distribution confirmations, and the asset type received (crypto vs USD). Official distribution administrators’ portals are often the best source of authoritative records (e.g., Celsius case administrator communications; BlockFi distributions portal). citeturn26search0turn26search7turn26search1  
- For any distributions in foreign currency, keep the **FX conversion basis** you used (PIT guidance references NBP average rate rules for converting foreign-currency amounts into PLN). citeturn21view0turn23view0

### Is there a specific PIT-38 field for “platform bankruptcy loss”?
No. The PIT-38 crypto section is designed around:
- **revenue from paid disposal** (poz. 36),
- **eligible costs incurred in the year** (poz. 37),
- **prior-year unutilized eligible costs** (poz. 38),
- computed income (poz. 39), and
- unutilized costs to carry forward (poz. 40). citeturn21view1

The brochure’s structure reflects the Ministry of Finance position that **you do not report a crypto tax “loss”**; if costs exceed revenue, you carry forward the difference. citeturn21view1turn23view0

### How bankruptcy recoveries can show up in PIT-38 in practice
Under the official definition, PIT-38 crypto revenue appears when you **exchange virtual currency** for fiat/goods/services/other property rights. citeturn16view1turn23view0

That creates three common cases for bankruptcy recoveries:

**Receiving crypto back (BTC/ETH/DOT).**  
Receipt itself is typically not a “disposal” event; the Polish taxable disposal would occur when you later sell or spend that crypto in one of the listed ways. citeturn16view1turn23view0

**Receiving USD (or other fiat) as part of distributions.**  
Economically, this resembles a conversion into fiat; whether you treat it as “paid disposal of virtual currency” or as settlement of a separate claim depends on your legal characterization of the platform relationship. The statutory text makes fiat exchange the core disposal concept, but it does not give a bespoke rule for bankruptcy-settlement mechanics. citeturn16view1turn23view0turn9search6

**Receiving non-crypto property (e.g., shares).**  
The statutory disposal definition explicitly includes exchange for a **property right other than virtual currency**. If you treat the distribution as an exchange of “waluta wirtualna” into shares, that points toward being inside the crypto disposal definition; if you instead treat the distribution as settlement of a non-crypto claim acquired earlier, it may fall under different PIT capital rules. citeturn16view1turn9search6turn26search0

Because this classification can materially change taxable timing and reporting, the controlling evidence is usually the **account/product terms** (custody vs title-transfer lending) and the distribution form. citeturn9search6turn15search4turn26search0