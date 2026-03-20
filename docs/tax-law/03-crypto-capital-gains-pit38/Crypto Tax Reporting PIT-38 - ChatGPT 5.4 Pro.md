Below is the current Polish PIT-38 crypto framework for tax years 2023, 2024, and 2025, with the points that are clear in the statute separated from the points that come mainly from tax interpretations.

## Bottom line

For a Polish tax resident, the crypto regime on PIT-38 is built around one taxable category: **“odpłatne zbycie walut wirtualnych”** taxed at **19%** under **art. 30b ust. 1a ustawy o PIT**. The statute defines that disposal as exchanging virtual currency for legal tender, for goods, for services, for a property right other than virtual currency, or using virtual currency to settle another liability. Crypto-to-crypto exchanges are **not** treated as taxable disposal under that definition. ([ISAP][1])

The regime is **annual and aggregate**. On PIT-38 you report yearly totals, not a transaction-by-transaction schedule: total taxable crypto revenue for the year, current-year deductible crypto costs, prior-year unused crypto costs carried forward, the resulting income, and unused costs to carry forward again. The Ministry of Finance states explicitly that with virtual currencies **you do not show a tax loss** from disposal; if costs exceed revenue, income is zero and the excess costs carry forward. ([ISAP][1])

A crucial correction to your assumptions: I would **not** confirm FIFO for Polish crypto PIT. The FIFO provisions in **art. 30b ust. 7–7a** do **not** cover income taxed under **art. 30b ust. 1a** (crypto). For crypto, the statute uses the separate annual total-revenue / total-cost mechanism in **art. 30b ust. 1b** together with **art. 22 ust. 14–16**. ([ISAP][1])

## The legal provisions that matter most

The key PIT provisions are:

* **art. 3** — Polish tax residence determines whether worldwide income is taxable in Poland. ([ISAP][1])
* **art. 11a ust. 1–2** — foreign-currency revenues and costs are translated into PLN using the NBP average rate from the last business day before the revenue date or cost date. ([ISAP][1])
* **art. 17 ust. 1 pkt 11** — revenue from paid disposal of virtual currency is a capital-gains source. ([ISAP][1])
* **art. 17 ust. 1f–1g** — definition of “odpłatne zbycie waluty wirtualnej” and the business carveout. ([ISAP][1])
* **art. 22 ust. 14–16** — deductible crypto costs and carryforward of unused costs. ([ISAP][1])
* **art. 23 ust. 1 pkt 38d** — expenses connected with exchanging one virtual currency for another are not tax-deductible costs. ([ISAP][1])
* **art. 30b ust. 1a, 1b, 5d, 6, 6a** — 19% rate, income formula, non-combination with other buckets, annual filing, and obligation to report costs even with no revenue. ([ISAP][1])
* **art. 45 ust. 1 and ust. 1a pkt 1** — PIT-38 filing by 30 April. ([ISAP][1])

The definition of **“waluta wirtualna”** used by PIT comes from the AML Act: **art. 2 ust. 2 pkt 26 ustawy AML**. That definition excludes, among other things, legal tender, e-money, and financial instruments. ([ISAP][2])

---

## 1) Taxable vs non-taxable events

### Selling crypto for fiat

Yes. Selling BTC, ETH, SOL, DOT, etc. for **EUR or PLN** on Binance, Kraken, or elsewhere is a classic **odpłatne zbycie waluty wirtualnej** and is taxable at 19% under the PIT-38 crypto rules. The same applies when the exchange function is called “Sell,” “Trade,” or “Convert” if the result is legal tender. ([ISAP][1])

### Converting USDC to EUR via Binance Convert

Yes, **if** the token disposed of qualifies as a **waluta wirtualna** under the AML definition, converting it into **EUR** is an exchange into legal tender and therefore taxable disposal. The statute taxes exchange of virtual currency into legal tender regardless of the exchange interface used. ([ISAP][1])

### Converting USDT to USDC

Under the current crypto rules, **crypto-to-crypto exchange is not taxable**. The Ministry of Finance says directly that exchanging one virtual currency for another does not create revenue, and **art. 23 ust. 1 pkt 38d** also excludes swap-related expenses from deductible costs. The caveat is definitional: this non-taxable treatment presumes that both sides are “waluty wirtualne” within the AML definition. ([Podatki][3])

### Selling crypto for goods or services

Yes. The statutory definition of **odpłatne zbycie** expressly includes exchanging virtual currency for **goods**, **services**, or another **property right**, and also using crypto to settle another obligation. Paying a contractor in crypto or buying a laptop directly with crypto is within the taxable definition. ([ISAP][1])

### Gifting crypto

A pure gift is **not** “odpłatne” for PIT-38 purposes, so it is not a PIT-38 crypto disposal event. The statute taxes disposal **for consideration**; a gift is not an exchange for money, goods, services, or another right. That said, gifts can raise separate issues under inheritance and gift tax rules, which are outside PIT-38. ([ISAP][1])

### Transfers between your own exchange accounts and self-custody wallets

Not taxable. Moving coins between your own Binance account, Kraken account, Ledger, MetaMask, or other self-custody wallets is not a disposal at all, provided you remain the beneficial owner and there is no exchange for fiat, goods, services, another right, or another liability. This is a record-reconciliation issue, not a revenue event. The taxable definition in the statute supports that result. ([ISAP][1])

---

## 2) Staking rewards, airdrops, and crypto interest

This is where the law is **less settled**.

### What the statute clearly says

The PIT crypto provisions in **art. 17 / 22 / 30b** are written for **disposal** of virtual currency. They do **not** expressly say how to tax **receipt** of new tokens from staking, airdrops, or “Simple Earn”-type interest. ([ISAP][1])

### Current conservative KIS practice

The current line in individual interpretations treats **staking rewards**, **airdrop tokens**, and similar reward tokens as taxable **at receipt**, typically as income from **property rights (prawa majątkowe)** under **art. 18 PIT**, valued at market value on receipt. Later, when those received tokens are sold for fiat or otherwise disposed of in a taxable way, that later disposal goes into the PIT-38 crypto regime. KIS has also accepted that the value taxed at receipt can become the cost when those reward tokens are later sold. ([Inforlex][4])

Applied to your questions, the conservative reading is:

* **staking rewards** — taxable at receipt outside PIT-38; later fiat sale also enters PIT-38, with cost based on the value already recognized at receipt. ([Inforlex][4])
* **airdrops** — same conservative treatment: taxable at receipt outside PIT-38; later sale goes to PIT-38. ([Inforlex][5])
* **Binance Simple Earn / CeFi / DeFi interest** — there is no equally clear statutory rule, but by analogy to the reward-token interpretations, the conservative approach is to treat the credited reward/interest tokens as taxable at receipt outside PIT-38, then treat later fiat disposal as a separate PIT-38 event. That is an inference from the interpretation line rather than an explicit MF rule. ([Inforlex][4])

### Important caveat: there is contrary case law on staking

There is at least one administrative-court judgment, **WSA we Wrocław, 6 December 2023, I SA/Wr 413/23**, summarized as holding that staking rewards should be taxed only when sold, not on receipt. That means the area is **not fully settled**. In practice, the more conservative filing position is still the current KIS line above unless you want to defend the court-based position. ([Inforlex][6])

### Cost basis of staking / airdrop / interest tokens

The PIT Act does not spell this out in the crypto chapter. The usable support comes from KIS: where reward tokens were already taxed at receipt, KIS accepted that their market value on receipt can be treated as the later cost of acquisition when those same tokens are sold. ([Inforlex][4])

---

## 3) Platform collapses, Celsius, BlockFi, Terra/UST

Polish PIT-38 crypto does **not** work like a classic capital-loss system where you realize and deduct a separate trading loss. The Ministry of Finance states that with virtual currencies “**nigdy nie wystąpi strata**” from disposal; if your costs exceed the year’s revenues, income is zero and the excess costs carry forward under **art. 22 ust. 16**. ([Podatki][3])

So for **Celsius, BlockFi, Terra/UST**, the safest current view is:

* the collapse itself is **not** entered on PIT-38 as a separate deductible loss event;
* if you had **documented acquisition costs**, those costs belong in the crypto cost bucket under **art. 22 ust. 14–16** and can continue to carry forward if not absorbed by taxable disposal revenue;
* there is no separate PIT-38 line for “platform collapse loss” or “worthless crypto loss.” ([ISAP][1])

A 2025 interpretation on a scam fact pattern is helpful by analogy: KIS said that sending purchased crypto to a scammer without receiving anything is **not** “odpłatne zbycie,” but the documented acquisition costs can still remain in the PIT-38 cost mechanism and carry forward. That is not a Celsius ruling, but it points in the same direction. ([Inforlex][7])

If you later receive compensation through a bankruptcy, restructuring, or court plan, that recovery needs a separate analysis at that time. There are narrow interpretations on compensation after exchange collapse, but they are highly fact-specific. ([Inforlex][8])

---

## 4) Costs, FX conversion, fees, pre-residency purchases, and FIFO

### FIFO

Polish law does **not expressly impose FIFO for crypto**. The FIFO wording in **art. 30b ust. 7–7a** applies to other capital-gains situations, not to crypto income under **art. 30b ust. 1a**. For crypto, the statute uses the annual aggregate formula in **art. 30b ust. 1b** plus the cost rules in **art. 22 ust. 14–16**. ([ISAP][1])

So the right answer to your questions 7 and 11 is: **no statutory FIFO rule for crypto, neither per-asset nor across all crypto is expressly prescribed.** What you do need is a defensible method and full records proving your acquisition expenses and your own-wallet transfers. ([ISAP][1])

### EUR-denominated purchases and sales

Yes. For crypto bought in **EUR**, the cost is translated into **PLN** using the **NBP average rate from the last business day before the cost date** under **art. 11a ust. 2**. For crypto sold for EUR, the revenue is translated into PLN using the **NBP average rate from the last business day before the revenue date** under **art. 11a ust. 1**. ([ISAP][1])

### Which costs are deductible

The statute allows **documented expenses directly incurred for acquisition of virtual currency** and **costs connected with disposal of virtual currency**, including documented intermediary fees. The Ministry’s guidance gives those categories expressly and also says some items are not deductible. ([ISAP][1])

That means, in principle:

* **purchase trading fees / exchange commissions** — generally yes, if directly connected and documented. ([ISAP][1])
* **sale trading fees / exchange commissions** — generally yes, as disposal-related costs. ([ISAP][1])
* **loan interest / financing costs used to buy crypto** — no. ([Podatki][3])
* **mining equipment / electricity** — no. ([Podatki][3])
* **expenses related to exchanging one crypto for another** — no, by **art. 23 ust. 1 pkt 38d**. ([ISAP][1])

### Withdrawal fees and network gas

This point is **not cleanly settled** in official general guidance.

What is clear is that:

* fees connected with **crypto-to-crypto swaps** are problematic, because swap-related expenses are excluded by **art. 23 ust. 1 pkt 38d**; and
* KIS has treated paying certain fees in crypto as itself involving settlement of an obligation in crypto, which can complicate the analysis. ([ISAP][1])

For **pure own-wallet withdrawal fees / network gas** unrelated to a taxable fiat sale, I did not find a Ministry source giving a blanket “yes.” For audit safety, I would treat them cautiously unless they are directly and provably tied to a taxable disposal. If they are directly connected with a taxable fiat exit, there is at least an argument that they are disposal-related costs under **art. 22 ust. 14**, but that point is weaker than exchange trading commissions. ([ISAP][1])

### Crypto acquired before becoming a Polish tax resident

For a person who became a Polish tax resident in 2023, the residence rule matters first: from the start of Polish residence, Poland taxes worldwide income under **art. 3 ust. 1**; before that, the scope is different. ([ISAP][1])

On the cost side, recent KIS interpretations say that **documented acquisition costs incurred before moving to Poland** can still be recognized in the Polish PIT-38 crypto mechanism after becoming a Polish resident, provided they were not already deducted elsewhere and are properly documented. The interpretations do **not** suggest a reset to market value on migration; the logic is the **original acquisition cost**, translated into PLN under the normal FX rules. ([Inforlex][9])

So for BTC bought in 2021 while resident in Sweden, the defensible Polish position is generally: use the **original acquisition cost**, converted into PLN under **art. 11a**, not a fresh 2023 market-value basis. Because this is not stated in the statute as explicitly as the basic disposal rules, it is an interpretation-based point rather than a black-letter statutory one. ([Inforlex][9])

---

## 5) PIT-38: where crypto goes and what you report

Crypto goes in the part of PIT-38 dedicated to income taxed under **art. 30b ust. 1a**.

### 2023 PIT-38 and 2024 PIT-38

For tax years **2023** and **2024**, the crypto row is in **Section E**. The official forms and brochures show these key boxes:

* **poz. 34** — revenue from paid disposal of virtual currencies
* **poz. 35** — current-year deductible costs
* **poz. 36** — prior-year unused crypto costs carried into the year
* **poz. 37** — income
* **poz. 38** — costs not deducted in the year, carried forward. ([Gov.pl][10])

### 2025 PIT-38

For tax year **2025**, the form layout moved the crypto positions, but the logic stayed the same. In the official 2025 form:

* **poz. 36** — revenue
* **poz. 37** — current-year costs
* **poz. 38** — prior-year carried costs
* **poz. 39** — income
* **poz. 40** — unused costs to carry forward. ([Gov.pl][11])

### Do you report totals or each transaction?

You report **totals**, not individual transactions. The PIT-38 form and official brochures ask only for annual aggregate figures. Transaction-level records are for your own workpapers and for audit support, not for attachment to the return. ([Gov.pl][11])

### Is crypto combined with stocks and other capital gains?

No. Crypto is reported on PIT-38, but **art. 30b ust. 5d** says income from paid disposal of virtual currency is **not combined** with income taxed under the regular **art. 30b ust. 1** capital-gains regime and also not with scale-taxed or flat-taxed business income. So it sits on the same return, but in a **separate bucket**. ([ISAP][1])

### Filing deadline

The return is filed from **15 February to 30 April** of the following year. So the relevant deadlines were:

* for **2023** — by **30 April 2024**
* for **2024** — by **30 April 2025**
* for **2025** — by **30 April 2026**. ([ISAP][1])

---

## 6) Step-by-step PIT-38 method for crypto

1. **Identify only taxable disposal events** for the year: crypto sold for fiat, crypto spent on goods/services, crypto used to settle liabilities. Ignore own-wallet transfers. Ignore crypto-to-crypto swaps as disposal events. ([ISAP][1])

2. **Translate each taxable revenue into PLN** using the NBP average rate from the last business day before the revenue date. Sum them into annual crypto revenue. ([ISAP][1])

3. **Collect current-year deductible crypto costs**: documented direct acquisition costs and disposal-related costs, translated into PLN under **art. 11a ust. 2** where relevant. Exclude swap-related expenses, financing costs, mining hardware/electricity. ([ISAP][1])

4. **Add prior-year unused crypto costs** carried forward under **art. 22 ust. 16** and **art. 30b ust. 6a**. ([ISAP][1])

5. **Compute income** as annual revenue minus current-year costs minus prior-year carried costs, using the form’s mechanics. If costs exceed revenue, income is zero and the unused balance carries forward; you do not show a tax loss from crypto disposal. ([ISAP][1])

6. **Enter the totals in Section E** of the relevant PIT-38 version for the tax year. ([Gov.pl][11])

7. **If you also had staking / airdrop / reward receipts** and you follow the conservative KIS line, treat the receipt-time taxation outside PIT-38 and only put the later taxable disposal into PIT-38. ([Inforlex][4])

---

## 7) Documentation and record-keeping

### Is there a mandatory formal “ewidencja walut wirtualnych”?

I did **not** find a PIT provision imposing a named, formal template called an “ewidencja walut wirtualnych” for private investors. The real legal burden comes from **art. 22 ust. 14**, which requires **documented** acquisition/disposal costs, and from the general need to substantiate what you put on the return. ([ISAP][1])

### What does art. 30b ust. 6 require?

**Art. 30b ust. 6** is mainly a **filing obligation**: after the tax year, the taxpayer files a return showing the income obtained in the year. **Art. 30b ust. 6a** adds that in the case of virtual currencies you also show the costs incurred in the tax year even if you had no revenue in that year. It is not a detailed bookkeeping blueprint. ([ISAP][1])

### Are Binance/Kraken CSV exports enough?

Sometimes yes, but often **not by themselves** once self-custody is involved.

Exchange exports are strong evidence for:

* trade dates,
* quantities,
* prices,
* trading fees,
* deposits and withdrawals. ([ISAP][1])

But for a mixed exchange + self-custody history, the prudent evidence pack is wider:

* Binance / Kraken CSV exports and account statements
* trade confirmations and Convert history
* bank transfer confirmations for fiat in/out
* wallet addresses and transaction hashes
* block-explorer records proving that withdrawals were transfers to your own wallets rather than taxable disposals
* records of staking / Simple Earn / airdrop receipts with timestamps and fair values used
* the NBP exchange rates used for each foreign-currency revenue and cost
* for pre-residency acquisitions, the original purchase proofs and payment evidence. ([Inforlex][9])

The Ministry also notes that crypto exchanges do **not** have the ordinary broker-style duty to issue PIT-8C/PIT-11 for this regime, so the taxpayer must compile the numbers independently. ([Podatki][3])

### How long to keep records

For practical safety, keep them at least until the tax liability limitation period expires. Under **art. 70 §1 Ordynacji podatkowej**, tax liabilities generally expire after **5 years** from the end of the calendar year in which the payment deadline passed. ([ISAP][12])

---

## Direct answers to your numbered questions

1. **Yes**: only **odpłatne zbycie walut wirtualnych** is taxed in the PIT-38 crypto regime at 19%, and **crypto-to-crypto swaps are not taxable**. ([ISAP][1])

2. **Odpłatne zbycie** includes sale for fiat, exchange for goods/services/other rights, and using crypto to settle liabilities. So:

   * crypto → EUR/PLN: **taxable**
   * USDC → EUR: **taxable** if the token qualifies as a virtual currency
   * USDT → USDC: **not taxable** as crypto-to-crypto
   * goods/services purchase with crypto: **taxable**
   * gift: **not a PIT-38 disposal**. ([ISAP][1])

3. **Staking rewards** are not expressly regulated in the crypto chapter. The conservative current KIS line is **tax at receipt outside PIT-38**, then later PIT-38 on disposal; cost basis for later sale is generally the value taxed at receipt. There is contrary case law, so this point is not fully settled. ([Inforlex][4])

4. **Airdrops**: same conservative KIS line — **taxable at receipt outside PIT-38**, then later PIT-38 on disposal; value on receipt serves as later cost. ([Inforlex][5])

5. **Crypto interest / Simple Earn**: not clearly regulated by statute; conservative treatment is by analogy to staking/reward interpretations — taxable at receipt outside PIT-38, later PIT-38 on disposal. ([Inforlex][4])

6. **Collapsed platforms**: no separate deductible PIT-38 loss entry. The acquisition costs stay in the cost/carryforward mechanism; the collapse itself is not a disposal. ([Podatki][3])

7. **FIFO**: I would **not confirm FIFO** for crypto. The statute does not impose it for art. 30b ust. 1a income. ([ISAP][1])

8. **EUR purchases**: yes, use the **NBP average rate from the last business day before the cost date** under **art. 11a ust. 2**. Revenue uses the analogous rule in **art. 11a ust. 1**. ([ISAP][1])

9. **Fees**: trading/sale fees are generally includable if directly connected and documented. Swap-related fees are excluded by **art. 23 ust. 1 pkt 38d**. Withdrawal/network fees are less certain and should be treated cautiously unless directly tied to taxable disposal. ([ISAP][1])

10. **Pre-Polish-residency acquisitions**: generally use the **original acquisition cost**, not a migration step-up, provided it is documented and not already deducted elsewhere. This comes from interpretation practice rather than an explicit statutory sentence. ([Inforlex][9])

11. **Per-asset or across all crypto FIFO?** Neither is expressly required, because the statute does not impose FIFO for crypto at all. The form works on annual totals. ([ISAP][1])

12. **PIT-38 field location**: yes, crypto is in the section for income/costs under **art. 30b ust. 1a** — Section E on the current forms. ([Gov.pl][11])

13. **What is reported**: annual totals for revenue, current-year costs, prior-year carried costs, resulting income, and unused costs to carry forward. Not individual transactions. ([Gov.pl][11])

14. **Combined with stocks?** Same return, but separate tax bucket; crypto is not combined with ordinary art. 30b ust. 1 capital gains. ([ISAP][1])

15. **Deadline**: yes, by **30 April** of the following year, with filing window starting **15 February**. ([ISAP][1])

16–19. **Documentation**: keep enough evidence to prove all numbers. There is no clear statutory formal template for a private “crypto register,” but you need documentation of acquisition costs, disposal proceeds, own-wallet transfers, reward receipts, and FX conversions. Exchange CSVs are often necessary but not always sufficient when self-custody is involved. ([ISAP][1])

## Practical takeaway for your fact pattern

For 2023–2025, your working model should be:

* tax only **fiat exits** and direct spending of crypto on goods/services/liabilities in PIT-38;
* ignore **BTC→ETH**, **USDC→USDT**, and other crypto-to-crypto swaps as revenue events;
* treat **own transfers** Binance/Kraken ↔ self-custody as non-taxable but document them carefully;
* carry forward unused documented acquisition costs when costs exceed revenue;
* treat **staking / airdrop / Simple Earn** receipts cautiously because that area is not fully settled, with the conservative position being receipt-time taxation outside PIT-38 and later PIT-38 at disposal. ([Podatki][3])

If useful, I can turn this into a **year-by-year filing checklist for 2023, 2024, and 2025**, or a **transaction-classification template** you can apply to Binance/Kraken CSV exports.

[1]: https://isap.sejm.gov.pl/isap.nsf/download.xsp/WDU19910800350/U/D19910350Lj.pdf "https://isap.sejm.gov.pl/isap.nsf/download.xsp/WDU19910800350/U/D19910350Lj.pdf"
[2]: https://isap.sejm.gov.pl/isap.nsf/download.xsp/WDU20180000723/U/D20180723Lj.pdf "https://isap.sejm.gov.pl/isap.nsf/download.xsp/WDU20180000723/U/D20180723Lj.pdf"
[3]: https://www.podatki.gov.pl/podatki-osobiste/pit/informacje-podstawowe/co-jest-opodatkowane/zbycie-kryptowalut/ "https://www.podatki.gov.pl/podatki-osobiste/pit/informacje-podstawowe/co-jest-opodatkowane/zbycie-kryptowalut/"
[4]: https://www.inforlex.pl/dok/tresc%2CFOB0000000000006403313%2CInterpretacja-indywidualna-z-dnia-24-listopada-2023-r-Dyrektor-Krajowej-Informacji-Skarbowej-sygn-0115-KDIT1-4011-687-2023-1-MR.html "https://www.inforlex.pl/dok/tresc%2CFOB0000000000006403313%2CInterpretacja-indywidualna-z-dnia-24-listopada-2023-r-Dyrektor-Krajowej-Informacji-Skarbowej-sygn-0115-KDIT1-4011-687-2023-1-MR.html"
[5]: https://www.inforlex.pl/dok/tresc%2CFOB0000000000006979668%2CInterpretacja-zwiazana-z-opodatkowaniem-dochodow-z-handlu-kryptowalutami-i-traktowaniem-airdropow-jako-przychod-Interpretacja-indywidualna-z-dnia-13-czerwca-2025-r-Dyrektor-Krajowej-Informacji.html "https://www.inforlex.pl/dok/tresc%2CFOB0000000000006979668%2CInterpretacja-zwiazana-z-opodatkowaniem-dochodow-z-handlu-kryptowalutami-i-traktowaniem-airdropow-jako-przychod-Interpretacja-indywidualna-z-dnia-13-czerwca-2025-r-Dyrektor-Krajowej-Informacji.html"
[6]: https://www.inforlex.pl/dok/tresc%2CWSA.2023.012.016046931%2CWyrok-WSA-we-Wroclawiu-z-dnia-6-grudnia-2023-r-sygn-I-SA-Wr-413-23.html "https://www.inforlex.pl/dok/tresc%2CWSA.2023.012.016046931%2CWyrok-WSA-we-Wroclawiu-z-dnia-6-grudnia-2023-r-sygn-I-SA-Wr-413-23.html"
[7]: https://www.inforlex.pl/dok/tresc%2CFOB0000000000007024713%2CInterpretacja-indywidualna-z-dnia-7-sierpnia-2025-r-Dyrektor-Krajowej-Informacji-Skarbowej-sygn-0115-KDIT1-4011-448-2025-2-MST.html "https://www.inforlex.pl/dok/tresc%2CFOB0000000000007024713%2CInterpretacja-indywidualna-z-dnia-7-sierpnia-2025-r-Dyrektor-Krajowej-Informacji-Skarbowej-sygn-0115-KDIT1-4011-448-2025-2-MST.html"
[8]: https://www.inforlex.pl/dok/tresc%2CFOB0000000000007486300%2CInterpretacja-indywidualna-z-dnia-15-grudnia-2025-r-Dyrektor-Krajowej-Informacji-Skarbowej-sygn-0112-KDIL2-1-4011-889-2025-1-JK.html "https://www.inforlex.pl/dok/tresc%2CFOB0000000000007486300%2CInterpretacja-indywidualna-z-dnia-15-grudnia-2025-r-Dyrektor-Krajowej-Informacji-Skarbowej-sygn-0112-KDIL2-1-4011-889-2025-1-JK.html"
[9]: https://www.inforlex.pl/dok/tresc%2CFOB0000000000006932617%2CSkutki-podatkowe-sprzedazy-walut-wirtualnych-przez-osobe-fizyczna-i-mozliwosc-odliczenia-kosztow-nabycia-w-deklaracji-PIT-38-Interpretacja-indywidualna-z-dnia-30-kwietnia-2025-r-Dyrektor-Krajowej.html "https://www.inforlex.pl/dok/tresc%2CFOB0000000000006932617%2CSkutki-podatkowe-sprzedazy-walut-wirtualnych-przez-osobe-fizyczna-i-mozliwosc-odliczenia-kosztow-nabycia-w-deklaracji-PIT-38-Interpretacja-indywidualna-z-dnia-30-kwietnia-2025-r-Dyrektor-Krajowej.html"
[10]: https://www.gov.pl/attachment/17d2cf10-3b57-4f7a-b37c-5502fdb92899 "https://www.gov.pl/attachment/17d2cf10-3b57-4f7a-b37c-5502fdb92899"
[11]: https://www.gov.pl/attachment/1874d956-4063-4a9c-a65c-ab7b6bc7aa30 "https://www.gov.pl/attachment/1874d956-4063-4a9c-a65c-ab7b6bc7aa30"
[12]: https://isap.sejm.gov.pl/isap.nsf/download.xsp/WDU20120000749/O/D20120749.pdf "https://isap.sejm.gov.pl/isap.nsf/download.xsp/WDU20120000749/O/D20120749.pdf"
