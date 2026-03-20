Below is a Poland-focused reference guide to cryptocurrency taxation for individuals, current on **19 March 2026**. It is centered on **PIT**. VAT, PCC, and full corporate-CIT issues are separate layers and are only touched here where needed.

## Core picture

Polish crypto taxation for individuals is still built mainly on the **PIT Act**, not on a separate crypto-tax statute. The key provisions are **art. 5a pkt 33a** (importing the definition), **art. 17 ust. 1 pkt 11 and ust. 1f–1g** (what counts as taxable disposal), **art. 22 ust. 14–16** (deductible costs), and **art. 30b ust. 1a–1b and ust. 5d** (19% rate and separate basket), with annual reporting on **PIT-38**. The term **“waluta wirtualna”** is borrowed directly from the AML Act, **art. 2 ust. 2 pkt 26**. ([ISAP][1])

The current dedicated regime took effect on **1 January 2019** under the amending act of **23 October 2018** (Dz.U. 2018 poz. 2193). Before 2019, Ministry of Finance guidance treated crypto under general PIT principles and the system did not yet have today’s dedicated statutory crypto basket. The 2019 reform created the separate virtual-currency rules, moved ordinary crypto gains into the art. 30b regime, and made **crypto-to-crypto swaps** non-taxable. ([ISAP][2])

For most people, the rule set is simple: **19% PIT on annual net income from taxable disposal of qualifying virtual currency, reported on PIT-38; crypto-to-crypto swaps are not taxed; excess documented costs carry forward; and ordinary own-account trading usually stays in PIT-38 even if you also run a sole proprietorship.** The biggest live changes in 2026 are not the tax rate, but **reporting and visibility** through DAC8 and the still-unfinished Polish MiCA implementation. ([ISAP][1])

## 1. Legal foundation

**Yes — for individuals, the main law is the PIT Act.** The most important articles are exactly the ones you flagged:
**art. 17** for the taxable source and meaning of disposal, **art. 22** for deductible costs, and **art. 30b** for the 19% rate and separate settlement. In practice, the full working set is **art. 5a pkt 33a**, **art. 17 ust. 1 pkt 11**, **art. 17 ust. 1f–1g**, **art. 22 ust. 14–16**, and **art. 30b ust. 1a–1b, 5d**. ([ISAP][1])

There is **no separate enacted Polish “crypto tax act”** that overrides those PIT rules. What exists outside the PIT Act are: the **AML Act**, which defines “waluta wirtualna”; the **DAC8 implementation law**, which adds tax reporting and information exchange; and **MiCA**, which regulates the market and service providers but does not itself rewrite the Polish PIT tax base. ([ISAP][3])

## 2. What counts as “waluta wirtualna”

Under the AML Act, “waluta wirtualna” is a **digital representation of value** that is **not** legal tender, an international unit of account, **e-money**, a financial instrument, a bill or cheque, and that is exchangeable in commerce for legal tender, accepted as a means of exchange, and can be electronically stored, transferred, or traded. PIT uses this exact AML definition by reference. ([ISAP][3])

That definition clearly covers **standard fungible cryptocurrencies** such as Bitcoin, Ether, and similar coins/tokens used as tradable exchange media. It does **not** automatically cover every blockchain-based token: if something is actually **e-money**, a **financial instrument**, or another kind of right, it falls outside this special definition. ([ISAP][3])

For **NFTs**, the Polish tax practice is usually that a genuinely **non-fungible** token is **not** “waluta wirtualna.” An official Eureka interpretation snippet from 1 September 2022 states that an NFT token is blockchain-based but **is not kryptowaluta / waluta wirtualna because it is non-fungible**. That means NFT cases often fall outside the special 19% virtual-currency regime and must be classified under general tax rules instead. ([Eureka][4])

For **wrapped tokens** (for example wBTC or some staking derivatives), **governance tokens**, and **LP tokens**, Polish law gives no bright-line statutory sub-category. The right test is still the AML definition: is the token fungible, tradable, transferable, accepted as a medium of exchange, and not really e-money or a financial instrument? Wrapped BTC has a stronger case than a governance token or LP receipt. LP and governance tokens are the most uncertain, because they often look more like a **claim, governance right, or pool position** than a general exchange medium. On today’s text, that distinction matters a lot: if you exchange crypto for something that is **not** “waluta wirtualna,” art. 17 ust. 1f can treat that as a **taxable disposal into a property right other than virtual currency**. ([ISAP][3])

## 3. Taxable events, tax rate, costs, and forms

### Tax rate

**Yes — the default Polish PIT rate for ordinary crypto disposal is 19%.** Art. 30b ust. 1a says that income from the paid disposal of virtual currency is taxed at **19%**, and art. 30b ust. 1b defines the taxable income as **revenue minus the costs from art. 22 ust. 14–16**. The tax portal repeats the same rule. ([ISAP][1])

### What is taxable

“Paid disposal” means exchanging virtual currency for **fiat**, for a **good**, for a **service**, for a **property right other than virtual currency**, or using crypto to **settle another obligation**. That is why cashing out to PLN/EUR, buying a laptop with BTC, or repaying a debt in crypto are all taxable moments. By contrast, the official MF guidance says that **exchange of one virtual currency for another virtual currency is not taxable**. ([ISAP][1])

A practical corollary is that **transfers between your own wallets or exchanges are generally not taxable**, because they are not listed in art. 17 ust. 1f as a disposal event. The tax point is not the movement of the asset, but the taxable conversion or use. Recordkeeping still matters, because you may later need to prove that a transfer was only a self-transfer rather than a disposal. ([ISAP][1])

### Costs and “losses”

Deductible costs are narrowly defined: **documented expenses directly incurred to acquire virtual currency** plus disposal-related costs, including certain documented fees paid to relevant intermediaries/entities. The official MF guidance is explicit that **loan/credit costs**, **costs of crypto-to-crypto swaps**, **mining hardware**, and **electricity used for mining** are not deductible in the PIT-38 crypto basket. ([ISAP][1])

Polish law also does **not** give you a classic tax loss on virtual currency. If revenue is lower than costs, the official guidance says your income is simply **zero**; the excess documented costs are carried into later years instead. In other words, crypto has a **cost carry-forward mechanism**, not a normal loss-offset mechanism against other income. ([podatki][5])

### Which return: PIT-38, PIT-36, PIT-36L, PIT-28

For ordinary individual crypto disposal, the correct form is **PIT-38**. MF’s current guidance says you must file it not only when you had taxable disposal revenue, but also when you **only incurred acquisition costs** in the year. Current guidance also states the filing window as **15 February to 30 April** of the following year. ([podatki][5])

**PIT-36**, **PIT-36L**, and **PIT-28** do not replace PIT-38 for ordinary own-account crypto trading. The forms pages show that PIT-36 is for scale-taxed income, PIT-36L for linear-tax business income, PIT-28 for ryczałt cases, while PIT-38 is the form for capital gains and specifically also for revenue/costs from paid disposal of virtual currency. ([podatki][6])

### JDG / sole proprietorship

A **JDG that merely trades its own crypto portfolio usually still settles under PIT-38**, not as ordinary business income. This follows from art. 17 ust. 1g and from MF guidance, which expressly says the PIT-38 crypto rules also apply when the disposal occurs within business activity, **except** for businesses described in AML Act art. 2 ust. 1 pkt 12. Այդ exception is the business of **exchange between crypto and fiat, exchange between crypto-assets, intermediation in such exchange, and operating wallets/accounts**. ([ISAP][1])

So the answer to “can a JDG report crypto trading as business income?” is usually **no for own trading, yes only for an actual crypto-service business**. Merely having a sole proprietorship does not let you re-route your personal trading into PIT-36L or PIT-28. If your business is actually a regulated virtual-currency service activity, then you enter the general business-tax world instead of PIT-38. ([ISAP][1])

### Progressive 12% / 32%

The special virtual-currency disposal basket is **separate** from scale-taxed income and from linear business income. Art. 30b ust. 5d says income from paid disposal of virtual currency is **not combined** with income taxed under the general scale or the linear business tax; the current scale remains **12% up to 120,000 PLN and 32% above**. ([ISAP][1])

So **ordinary crypto trading/disposal is not taxed at 12%/32%**. Those rates become relevant only when the inflow is classified **outside** the special art. 17 / art. 30b virtual-currency regime — for example because the asset is not “waluta wirtualna” at all, or because the tax authority characterizes a receipt as some other kind of ordinary income. Recent interpretations reported in legal databases show that this boundary is exactly where controversies around **staking**, **airdrops**, or non-standard tokens arise. ([ISAP][1])

## 4. EU context: DAC8 and MiCA

### DAC8

DAC8 does **not** change the 19% PIT rate. It is a **mandatory reporting and automatic information-exchange** regime for crypto-asset data. The European Commission says the rules apply from **1 January 2026**, reporting CASPs begin collecting data from that date, the first reporting year is **2026**, and the first exchanges between tax authorities happen by **30 September 2027**. ([Taxation and Customs Union][7])

Poland implemented DAC8/DAC9 in **March 2026**. The Ministry of Finance states that DAC8 introduces mandatory reporting and automatic exchange of information on crypto-asset transactions. The Polish implementing law provides that the **first reporting period is 2026** for transmission in **2027**, and that providers send user crypto-asset information to the **Head of KAS by 30 June** of the following year, with transitional rules covering the gap from **1 January 2026** until the law entered into force. ([Gov.pl][8])

For a Polish taxpayer, the practical message is simple: **from 2026 onward, centralized platform data will become far more visible to tax authorities**. DAC8 uses the broader EU **crypto-asset** framework, so reporting can be wider than the Polish PIT concept of “waluta wirtualna.” That matters especially in grey zones like some NFTs, stablecoins, and non-standard DeFi tokens. ([Taxation and Customs Union][7])

### Binance and Kraken

You should assume that large centralized platforms serving EU residents will fall within this reporting wave. Binance says DAC8 applies to **EU tax residents**, that Binance is required to collect and verify certain tax data, and that user/transaction data may be reported to relevant tax authorities. Kraken says that under **CARF/DAC8-style reporting** it may need to report transfers, values, and account-holder identity data. ([Binance][9])

So the practical answer to “will Binance and Kraken report Polish users?” is: **for EU-tax-resident users, you should assume yes in scope, with first reportable year 2026 and first authority-to-authority exchanges in 2027.** Whether the first filing is made directly to Poland or to another EU authority depends on the reporting entity, but DAC8 is designed so the information can then be exchanged to Poland. ([Taxation and Customs Union][7])

### MiCA

MiCA is **market regulation**, not a tax amendment. At EU level it applies from **30 June 2024** for the ART/EMT parts and from **30 December 2024** generally. It does **not** itself rewrite Polish PIT rules on taxable disposal, rates, or PIT-38 reporting. ([EUR-Lex][10])

MiCA still matters indirectly: it affects which entities may lawfully provide services, how assets/services are categorized in the EU, and what compliance records exist. In Poland, KNF states that because the national act has not yet entered into force, **no public authority has been designated** for most MiCA supervision; existing Polish operators are effectively living on the MiCA transition period only until **1 July 2026**. A Sejm **crypto-assets bill** is pending, and was referred for opinions on **18 March 2026**. ([KNF][11])

### 2025–2026 legislative outlook

As of **19 March 2026**, I did **not** find any enacted change to the core Polish PIT treatment of ordinary crypto disposal: the 2019 model is still in force. The live changes are **DAC8 reporting** and the unfinished Polish **MiCA/crypto-assets** package, not a new PIT rate. A pending Sejm crypto-assets bill also contains taxpayer-friendly language on staking, but that is still only a **proposal**, not current law. ([podatki][5])

## 5. How common activities are currently treated

### Clear rules

* **Sale of crypto for fiat**: taxable disposal under PIT-38 at 19% on annual net income. ([ISAP][1])
* **Using crypto to buy goods/services or settle a debt**: also taxable disposal. ([ISAP][1])
* **Crypto-to-crypto swap**: not taxable. ([podatki][5])
* **Own-wallet transfer**: generally not taxable, because it is not a disposal category under art. 17 ust. 1f; but keep records proving it was only a transfer. ([ISAP][1])

### Mining

The statute taxes **disposal** of the mined coins, not the mere existence of the coins in your wallet under the special art. 30b disposal rule. The major problem is cost basis: MF guidance explicitly says that **mining hardware** and **electricity** are **not** deductible PIT-38 crypto costs. The practical result is harsh: later sale of mined coins may be taxed with little or no deductible basis in the special crypto basket. ([podatki][5])

### Staking

This is one of the least settled areas in Polish crypto tax. On the **text of the statute**, the taxpayer-friendly argument is that tax should arise only on **paid disposal**, because art. 17 ust. 1f defines taxable disposal events and does not list mere accrual of a staking reward. But recent KIS interpretations reported in legal databases have taken the opposite view and treated **receipt of staking rewards** as taxable on receipt. A pending Sejm crypto-assets bill would codify the disposal-only approach by saying that receiving virtual currency from staking does **not** itself create revenue. ([ISAP][1])

For your practical baseline document, I would treat **staking timing as unresolved**:
**best textual argument** = tax on disposal;
**current authority risk** = some KIS positions taxing receipt;
**best future legislative signal** = possible move toward disposal-only treatment. ([ISAP][1])

### If staking pays a different token (for example DOT.S vs DOT)

If the “migration” or unstaking process is economically just an **exchange of one virtual currency for another virtual currency**, current law gives a strong argument for **no taxable event**. If, however, the thing received is better classified as **not** being “waluta wirtualna” — for example a different property right or claim — the risk increases because art. 17 ust. 1f taxes exchange into a **property right other than virtual currency**. ([podatki][5])

### DeFi: AMMs, liquidity provision, yield farming, borrowing

There is **no mature, unified Polish PIT framework for retail DeFi** in the statute. There **are** KIS interpretations touching DeFi-like structures: an official Eureka result from 1 September 2022 explicitly discusses a **“pula płynności”** operating through smart contracts. But that is not the same as a settled, across-the-board PIT rule for Uniswap-style user activity. ([Eureka][4])

The most defensible current framework is functional:

* **Providing liquidity to an AMM**: if you deposit crypto and receive an LP token that itself qualifies as **virtual currency**, there is a strong argument for crypto-to-crypto neutrality. If the LP token is instead a **claim/right** rather than “waluta wirtualna,” the deposit can look like a taxable exchange into a non-crypto property right under art. 17 ust. 1f. ([ISAP][1])
* **Yield farming / liquidity mining rewards**: same uncertainty as staking. The statute supports a disposal-only argument; recent reward/staking interpretations show a real authority tendency to tax some receipts earlier. ([ISAP][1])
* **Borrowing against crypto collateral**: a plain loan does not fit the statutory list of disposal events, so mere borrowing against collateral is generally the strongest case for non-taxability. But **liquidation of collateral** or **repaying an obligation with crypto** is much harder and can become taxable disposal. ([ISAP][1])
* **Smart-contract exploit / rug-pull losses**: I found no clear official relief. Because only direct acquisition/disposal costs count, and because virtual currency does not generate a classic deductible loss, deduction arguments for hacks/rug-pulls are weak and fact-specific. ([ISAP][1])

## 6. Common pitfalls and audit risk

The most common Polish crypto mistakes are usually these:

1. **Not filing PIT-38** when you only bought crypto and incurred costs but did not sell.
2. Assuming an exchange will send you **PIT-8C or PIT-11**. MF says exchanges do **not** have that statutory duty.
3. Forgetting that spending crypto on **goods/services/debts** is taxable.
4. Claiming non-deductible items such as **loan costs**, **mining rigs**, or **electricity**.
5. Assuming that a **JDG**, lineal tax, or sheer trading volume automatically turns own crypto trading into business income.
6. Keeping weak evidence of acquisition cost and wallet flows. ([podatki][5])

I did **not** find a public official crypto-specific checklist of “audit triggers.” The safe assumption is that the risk zones are exactly where the law creates hard duties: unsupported costs, non-filed PIT-38 returns, visible centralized-platform activity that does not match returns, and misclassification of non-standard tokens or DeFi positions. Visibility is increasing because virtual-currency businesses already sit in the AML perimeter, and DAC8 adds formal tax reporting from **2026**. ([ISAP][3])

## 7. Voluntary disclosure and limitation period

There is **no crypto-specific amnesty** that I found. The general Polish mechanism is **czynny żal** under **art. 16 KKS**. It can protect against penal-fiscal punishment if the taxpayer discloses the offence before the authority already has clearly documented knowledge of it and then cures the default. e-Urząd Skarbowy provides an online form for this filing. ([Gov.pl][12])

The **basic** statute of limitations is **5 years from the end of the calendar year in which the tax payment deadline expired**. MF’s current guidance on document retention gives the practical example that records for the **2025** PIT return should be kept until **31 December 2031**. ([ISAP][13])

## Bottom line

The Polish baseline is still the **2019 regime**: for qualifying **“waluty wirtualne”**, ordinary disposal is taxed at **19%** in **PIT-38**, **crypto-to-crypto swaps are neutral**, and unused documented costs carry forward instead of creating a normal tax loss. The hardest unresolved areas are **classification of non-standard tokens** and **timing for staking / DeFi rewards**. The main 2026 change is not the PIT rate but **tax visibility**: DAC8 starts with **2026 data**, while Poland is still finishing the domestic MiCA/crypto-assets framework. ([ISAP][1])

If useful, the next step is to turn this into a **decision tree by activity** (spot trading, staking, LPing, lending, NFTs, mining, salary in crypto, airdrops) with a separate column for **clear / uncertain / high-risk** treatment.

[1]: https://isap.sejm.gov.pl/isap.nsf/download.xsp/WDU19910800350/U/D19910350Lj.pdf "https://isap.sejm.gov.pl/isap.nsf/download.xsp/WDU19910800350/U/D19910350Lj.pdf"
[2]: https://isap.sejm.gov.pl/isap.nsf/download.xsp/WDU20180002193/T/D20182193L.pdf "https://isap.sejm.gov.pl/isap.nsf/download.xsp/WDU20180002193/T/D20182193L.pdf"
[3]: https://isap.sejm.gov.pl/isap.nsf/download.xsp/WDU20180000723/U/D20180723Lj.pdf "https://isap.sejm.gov.pl/isap.nsf/download.xsp/WDU20180000723/U/D20180723Lj.pdf"
[4]: https://eureka.mf.gov.pl/informacje/podglad/506478 "https://eureka.mf.gov.pl/informacje/podglad/506478"
[5]: https://www.podatki.gov.pl/podatki-osobiste/pit/informacje-podstawowe/co-jest-opodatkowane/zbycie-kryptowalut/ "https://www.podatki.gov.pl/podatki-osobiste/pit/informacje-podstawowe/co-jest-opodatkowane/zbycie-kryptowalut/"
[6]: https://www.podatki.gov.pl/twoj-e-pit/pytania-i-odpowiedzi/kogo-dotyczy-i-gdzie-jest-dostepna-usluga-twoj-e-pit/13-kogo-dotyczy-usluga-twoj-e-pit/ "https://www.podatki.gov.pl/twoj-e-pit/pytania-i-odpowiedzi/kogo-dotyczy-i-gdzie-jest-dostepna-usluga-twoj-e-pit/13-kogo-dotyczy-usluga-twoj-e-pit/"
[7]: https://taxation-customs.ec.europa.eu/taxation/tax-transparency-cooperation/administrative-co-operation-and-mutual-assistance/directive-administrative-cooperation-dac/dac8_en "https://taxation-customs.ec.europa.eu/taxation/tax-transparency-cooperation/administrative-co-operation-and-mutual-assistance/directive-administrative-cooperation-dac/dac8_en"
[8]: https://www.gov.pl/web/finanse/ustawa-o-wymianie-informacji-podatkowych-z-innymi-panstwami-oraz-niektorych-innych-ustaw-z-podpisem-prezydenta-rp "https://www.gov.pl/web/finanse/ustawa-o-wymianie-informacji-podatkowych-z-innymi-panstwami-oraz-niektorych-innych-ustaw-z-podpisem-prezydenta-rp"
[9]: https://www.binance.com/en/support/faq/detail/448a1208adf54c97b00100466fee26d7 "https://www.binance.com/en/support/faq/detail/448a1208adf54c97b00100466fee26d7"
[10]: https://eur-lex.europa.eu/summary/MS/4626998 "https://eur-lex.europa.eu/summary/MS/4626998"
[11]: https://www.knf.gov.pl/knf/pl/komponenty/img/Stanowisko_UKNF_-_nadzor_nad_krypto_96996.pdf "https://www.knf.gov.pl/knf/pl/komponenty/img/Stanowisko_UKNF_-_nadzor_nad_krypto_96996.pdf"
[12]: https://www.gov.pl/web/gov/elektroniczny-czynny-zal "https://www.gov.pl/web/gov/elektroniczny-czynny-zal"
[13]: https://isap.sejm.gov.pl/isap.nsf/download.xsp/WDU19971370926/U/D19970926Lj.pdf "https://isap.sejm.gov.pl/isap.nsf/download.xsp/WDU19971370926/U/D19970926Lj.pdf"
