As of **19 March 2026**, the most workable Polish PIT position is still this: **treat USDT, and in practice also USDC, as “waluta wirtualna” for PIT purposes**. On that approach, **crypto→stablecoin** and **stablecoin→stablecoin** swaps are neutral, while **stablecoin→EUR/PLN** is the taxable disposal. That matches the current PIT statute, which still imports the AML definition, the Ministry of Finance guidance that exchange between virtual currencies is not taxed, and public KIS snippets that continue to describe **Tether (USDT)** and **stablecoins** as virtual currencies. ([ISAP][1])

The caveat is **USDC after MiCA**. MiCA entered into force on **29 June 2023**, and the stablecoin titles (ART/EMT) have applied since **30 June 2024**. MiCA also says that **e-money tokens are deemed electronic money**, and Circle states that **EEA USDC issued by Circle SAS is an EMT**. That creates a real text-level tension because the Polish AML/PIT definition of “waluta wirtualna” excludes **electronic money**. But I do **not** see an enacted Polish PIT change that reclassified USDC from a specific date. The Polish crypto-assets bill expressly tried to **preserve the old tax treatment**, then was **vetoed on 12 February 2026**; official Polish materials later in February 2026 still referred to **ongoing work** on the project. ([EUR-Lex][2])

**1. Are USDC and USDT legally classified as “waluta wirtualna” under Polish law?**

**Practical tax answer: yes.** **Strict post-MiCA textual answer: USDC is arguable.** Current PIT still points to AML art. 2 ust. 2 pkt 26, and KIS materials publicly available still treat **USDT** and “stablecoins” as virtual currencies. For **USDC**, though, MiCA creates a serious interpretive issue because EMTs are treated as e-money, while the Polish AML/PIT definition excludes e-money. So the most accurate formulation is: **USDT — yes in current practice; USDC — yes in current practice, but no longer beyond doubt on pure literal analysis after MiCA**. ([ISAP][1])

**2. Has KIS issued stablecoin-specific interpretations?**

Yes. The clearest public examples I found are these:

* **0115-KDIT1.4011.25.2024.1.MR (19 Feb 2024)**: KIS treated payment for services in a **stablecoin / virtual currency** as a two-step situation; if the coin is immediately sold for fiat, there may be no separate crypto profit beyond the service income, and later crypto profit is measured against the value at the invoice/receipt date; exchange fees are deductible. ([Lex.pl][3])
* **0114-KDIP3-1.4011.341.2024.3.BS (2 Jul 2024)**: the facts named **Bitcoin, Ethereum and Tether (USDT)**, and the public snippet says the cryptocurrencies in the case satisfy the definition of **waluta wirtualna**. ([Lex.pl][4])
* **0115-KDIT1.4011.745.2025.3.MN (24 Nov 2025)**: public snippets say **stablecoins are waluty wirtualne**, and that remuneration paid in stablecoins creates ordinary income when received, with the later sale of the stablecoins treated separately under the crypto rules. ([Lex.pl][5])

**3. Does MiCA change the classification of stablecoins in Poland?**

**Regulatory classification: yes. Polish PIT classification: not automatically.** MiCA clearly distinguishes **EMTs** and **ARTs**, and those stablecoin rules have applied since **30 June 2024**. But Polish PIT/CIT were not automatically rewritten on that date. The official justification to the Polish crypto-assets bill explicitly said the PIT/CIT amendments were **not** about making MiCA apply; they were about **preserving the existing crypto tax rules** because the AML definition of “waluta wirtualna” was being removed and replaced by broader “kryptoaktywa”. ([ESMA][6])

**4. Under MiCA, USDC is an EMT. Does that change Polish tax treatment from a specific date?**

I do **not** see a clear Polish tax change date. Circle says EEA USDC is an EMT under MiCA, and MiCA says EMTs are e-money. But the Polish bill that was meant to hard-code the old tax treatment into PIT/CIT was vetoed, so there is **no enacted Polish statutory reclassification date** I can point to. The materials I found instead show a legislative intent to **keep the old tax result**, not to make stablecoins taxable differently from **30 June 2024** or any other specific date. ([Circle][7])

**5. If USDC is treated as “waluta wirtualna”, is ETH→USDC non-taxable and USDC→EUR taxable?**

Yes. Under current PIT rules, taxable disposal of virtual currency means exchange for **legal tender**, goods, services, other property rights, or settlement of liabilities. The Ministry of Finance also says that **exchange between virtual currencies is not taxed**. So on the current mainstream reading: **ETH→USDC is neutral**, **USDC→EUR is the taxable event**. A transfer from your own Polygon wallet to your own Binance/Kraken account is just a self-transfer, not a disposal event. ([ISAP][1])

**6. If USDC were reclassified outside “waluta wirtualna”, would ETH→USDC become taxable?**

**Probably yes.** This is an inference, not a published rule. If USDC stopped qualifying as “waluta wirtualna”, then ETH→USDC would no longer be an exchange between two virtual currencies covered by the current neutral rule. The official justification to the vetoed crypto-assets bill also says that **crypto-assets that are not “waluta wirtualna”** would remain taxed under the ordinary rules rather than the special crypto regime. ([ISAP][1])

**7. On USDC→EUR, what is the revenue?**

The revenue should be the **EUR actually received on the sale**, translated into PLN using the **NBP average EUR rate from the last working day before the revenue date** under PIT art. 11a ust. 1. It should **not** be “USDC amount × USD NBP rate” merely because USDC is pegged to USD. Sale-related exchange fees belong on the **cost** side, because PIT art. 22 ust. 14 includes documented costs connected with disposal, and KIS has treated exchange fees that way in the remuneration-paid-in-crypto scenario. The **bank withdrawal of EUR** is not a second taxable event; the taxable event is the **USDC→EUR sale** on the exchange. ([ISAP][1])

**8. What is the cost basis of USDC?**

**a) USDC received as salary / service remuneration:**
Generally, the later crypto cost should be the **PLN value already recognized as taxable remuneration when the USDC was received**. The published KIS materials on service remuneration paid in stablecoin/crypto say the later crypto result is measured against the **value at the invoice/receipt date**. For classic payroll salary, that is an analogy rather than the exact fact pattern in the cited rulings, but it is the same tax logic. ([Lex.pl][3])

**b) USDC received from selling other crypto (ETH→USDC):**
Do **not** step the basis up to the market value of USDC at the swap. The Polish crypto regime is annual and aggregate: the swap itself is neutral, and PIT expressly excludes **expenses connected with swapping one virtual currency for another** from deductible costs. Practically, you carry forward the **historical documented acquisition cost of the ETH** until you later make a taxable disposal to fiat or another non-crypto asset. ([Podatki][8])

**c) USDC bought directly with EUR:**
Yes: the cost is the **EUR paid**, translated into PLN using the **NBP average EUR rate from the last working day before the cost date** under art. 11a ust. 2, plus documented acquisition fees. ([ISAP][1])

**9. Is USDC↔USDT taxable?**

If both tokens are treated as **waluta wirtualna**, then **no**. It is a virtual-currency-to-virtual-currency swap, which the Ministry of Finance treats as non-taxable, and public KIS snippets treating **USDT** and **stablecoins** as virtual currencies fit that result. ([Podatki][8])

**10. What about Binance auto-conversions like BUSD→FDUSD→USDC?**

On the logic of current law, that should be **tax-neutral** as long as each leg is an exchange between tokens that qualify as **waluta wirtualna**. I did **not** locate a published KIS ruling specifically on Binance’s automatic **BUSD→FDUSD→USDC** migration in this review, so this point is an **inference from the general crypto→crypto rule**, not a direct ruling on that exact Binance process. ([Podatki][8])

**11. Your example: 6,000 USDC received as salary, valued at 24,000 PLN; later sold for 5,500 EUR worth 23,500 PLN**

The closest answer is **(a), with one correction**. On the crypto side, you would have:

* **revenue:** 23,500 PLN
* **deductible cost:** 24,000 PLN
* **taxable crypto income for the year:** **0 PLN**, not minus 500 PLN
* **carry-forward cost:** 500 PLN into the next year

Polish PIT computes crypto income annually as revenue minus costs, and the excess of costs over revenue is carried forward; the Ministry of Finance also states that with crypto disposal **a tax loss does not arise** in the ordinary sense. Separately, the original **24,000 PLN** was already taxable when the salary/service remuneration was received. ([ISAP][1])

**Bottom line**

For current Polish PIT compliance, I would classify your flows like this:

* **Receive USDC/USDT as remuneration:** ordinary income at receipt; that PLN value becomes the economic acquisition cost for later PIT-38. ([Inforfk][9])
* **Move the stablecoin to Binance/Kraken:** no tax event. ([ISAP][1])
* **ETH→USDT / USDT→USDC / USDC→USDT:** no tax event, assuming the tokens are treated as “waluta wirtualna”. ([Podatki][8])
* **USDC/USDT→EUR or PLN:** taxable disposal in PIT-38. Revenue is the actual EUR/PLN received; foreign-currency amounts are translated under art. 11a; sale fees go to costs. ([ISAP][1])

Because the unresolved point is really **USDC after MiCA**, not ordinary crypto mechanics, the cleanest protection for material amounts is an **individual interpretation** built around your exact chain: remuneration in USDC on Polygon, self-transfer to exchange, occasional ETH→USDT/USDC swaps, and final EUR withdrawal.

[1]: https://isap.sejm.gov.pl/isap.nsf/download.xsp/WDU19910800350/U/D19910350Lj.pdf "https://isap.sejm.gov.pl/isap.nsf/download.xsp/WDU19910800350/U/D19910350Lj.pdf"
[2]: https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=PI_COM%3AC%282024%29897 "https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=PI_COM%3AC%282024%29897"
[3]: https://sip.lex.pl/orzeczenia-i-pisma-urzedowe/pisma-urzedowe/0115-kdit1-4011-25-2024-1-mr-skutki-podatkowe-otrzymania-185248263 "https://sip.lex.pl/orzeczenia-i-pisma-urzedowe/pisma-urzedowe/0115-kdit1-4011-25-2024-1-mr-skutki-podatkowe-otrzymania-185248263"
[4]: https://sip.lex.pl/orzeczenia-i-pisma-urzedowe/pisma-urzedowe/0114-kdip3-1-4011-341-2024-3-bs-rozliczanie-pit-w-zwiazku-185259597 "https://sip.lex.pl/orzeczenia-i-pisma-urzedowe/pisma-urzedowe/0114-kdip3-1-4011-341-2024-3-bs-rozliczanie-pit-w-zwiazku-185259597"
[5]: https://sip.lex.pl/orzeczenia-i-pisma-urzedowe/pisma-urzedowe/0115-kdit1-4011-745-2025-3-mn-skutki-podatkowe-185306952 "https://sip.lex.pl/orzeczenia-i-pisma-urzedowe/pisma-urzedowe/0115-kdit1-4011-745-2025-3-mn-skutki-podatkowe-185306952"
[6]: https://www.esma.europa.eu/sites/default/files/2025-01/ESMA75-223375936-6099_Statement_on_stablecoins.pdf "https://www.esma.europa.eu/sites/default/files/2025-01/ESMA75-223375936-6099_Statement_on_stablecoins.pdf"
[7]: https://www.circle.com/legal/mica-usdc-whitepaper "https://www.circle.com/legal/mica-usdc-whitepaper"
[8]: https://www.podatki.gov.pl/podatki-osobiste/pit/informacje-podstawowe/co-jest-opodatkowane/zbycie-kryptowalut/ "https://www.podatki.gov.pl/podatki-osobiste/pit/informacje-podstawowe/co-jest-opodatkowane/zbycie-kryptowalut/"
[9]: https://inforfk.pl/tematy/lista?ct=01&gr=po.ko.wy&kfl=d&kw=dzia%C5%82alno%C5%9B%C4%87+wykonywana+osobi%C5%9Bcie "https://inforfk.pl/tematy/lista?ct=01&gr=po.ko.wy&kfl=d&kw=dzia%C5%82alno%C5%9B%C4%87+wykonywana+osobi%C5%9Bcie"
