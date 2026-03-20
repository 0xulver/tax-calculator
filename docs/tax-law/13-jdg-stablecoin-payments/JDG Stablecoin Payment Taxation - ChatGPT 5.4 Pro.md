Bottom line: for your fact pattern, **Option A (EUR bank transfer)** is the cleaner default. For the **service side**, the 12% ryczałt should generally be the same whether the client settles by SEPA or in USDC, **provided the remuneration is still denominated in EUR/USD**. The major difference starts **after payment**: EUR leads to ordinary business FX mechanics, while USDC creates a separate **PIT-38 virtual-currency layer** when you later exchange it for fiat or use it to pay non-crypto obligations. The biggest uncertainty is not the ryczałt itself, but whether the service receivable’s value is unquestionably accepted as the **PIT-38 acquisition cost** without your own KIS interpretation. ([Sejm API][1])

## Comparison table

| Stage                                         | Option A — client pays EUR to JDG bank account                                                                                                                                                                                                                                                                                                                 | Option B — client pays USDC to wallet, then optional hold / exchange / withdrawal                                                                                                                                                                                                                                                                                                                                      |
| --------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **1. When business revenue arises**           | For ryczałt, business revenue follows PIT art. 14. In a typical ongoing B2B setup with monthly settlement periods, the income date is the **last day of the settlement period** stated in the contract/invoice. Otherwise it is usually the **service completion / partial completion date**, not later than the invoice date or payment date. ([Sejm API][1]) | Same business-income rule. An official EUREKA result for a crypto-payment interpretation states that payment in virtual currency for a performed service does **not** move the business-income date to the payment day merely because crypto was used as settlement. ([Sejm API][1])                                                                                                                                   |
| **2. PLN value for PIT-28 / monthly ryczałt** | If the invoice is in EUR or USD, convert the foreign-currency revenue to PLN using the **NBP average rate from the last working day before the income date**. ([ISAP][2])                                                                                                                                                                                      | If the invoice is still **denominated in EUR/USD** and USDC is only the settlement rail, the cleaner reading is to keep the **invoice/receivable currency** for the business-revenue conversion. If the remuneration is instead stated directly in **USDC**, you lose the simple foreign-currency conversion rule and move toward valuing the non-cash/virtual-currency consideration at **market value**. ([ISAP][2]) |
| **3. Ryczałt rate**                           | Assuming your services fall under software-related PKWiU ex 62.01.1, the ryczałt rate is **12%** of the PLN revenue. ([Podatki][3])                                                                                                                                                                                                                            | Same. The settlement medium does not change the service classification. ([Podatki][3])                                                                                                                                                                                                                                                                                                                                 |
| **4. What happens after receipt**             | Later EUR settlement can generate **business FX differences** under art. 24c, which the ryczałt act imports for ryczałt taxpayers. ([Sejm API][1])                                                                                                                                                                                                             | Virtual currency is legally defined separately from legal tender / foreign currency. The ordinary business FX-difference regime does not fit cleanly here; instead, later disposal of the USDC falls into the **PIT-38 virtual-currency regime**. Published summaries of KIS interpretations also report a **no-standard-FX-differences** view for crypto settlements. ([ISAP][4])                                     |
| **5. When extra tax appears**                 | Usually no second tax layer just because funds hit the bank; only the service-side ryczałt and possible ordinary FX differences. ([Sejm API][1])                                                                                                                                                                                                               | Exchanging USDC for EUR/PLN is an **odpłatne zbycie waluty wirtualnej**. So is using USDC to buy goods/services or settle debts. Pure **crypto-to-crypto** exchange is outside that disposal definition. ([ISAP][2])                                                                                                                                                                                                   |
| **6. Transfer to bank**                       | The bank receipt itself is just the cash settlement of your receivable.                                                                                                                                                                                                                                                                                        | The taxable event is the **USDC → EUR/PLN exchange**, not the later transfer of already-converted fiat from the exchange to your bank. That later bank withdrawal is not a separate disposal event. This follows from the statutory disposal definition. ([ISAP][2])                                                                                                                                                   |
| **7. VAT**                                    | Payment medium does not change VAT place-of-supply rules. For B2B services, the general rule in art. 28b is the customer’s location. Separately, the Polish subject-matter VAT exemption threshold is **240,000 PLN in 2026**, not 200,000 PLN. For EU B2B services, a VAT-exempt taxpayer can still need **VAT-UE registration**. ([Gov.pl][5])               | Same. VAT follows the service, not whether the customer used SEPA or USDC. ([Gov.pl][5])                                                                                                                                                                                                                                                                                                                               |
| **8. Documentation**                          | Invoice + bank statement is usually enough.                                                                                                                                                                                                                                                                                                                    | You need a stronger trail: invoice/contract wording, wallet address, tx hash, explorer record, valuation method, exchange trade confirmation, fees, and bank withdrawal record. Official MF guidance also notes that crypto intermediaries do **not** issue PIT-8C/PIT-11 for you, so you must keep your own evidence. ([Podatki][6])                                                                                  |
| **9. AML / registration risk**                | Low.                                                                                                                                                                                                                                                                                                                                                           | Higher practical AML scrutiny, but merely accepting crypto for your own software services is **not** the regulated “virtual-currency activity” that requires registry entry. Registry entry is for exchange / crypto-to-crypto exchange / broking / custody-account activity. The Polish registry is still active in 2026 for those businesses. ([ISAP][4])                                                            |
| **10. Net assessment**                        | Lowest compliance burden and lowest interpretive risk.                                                                                                                                                                                                                                                                                                         | Workable, but more paperwork and more legal uncertainty; the key uncertainty is the later PIT-38 cost basis.                                                                                                                                                                                                                                                                                                           |

## Direct answers

### Revenue recognition and ryczałt

**1. If the JDG invoices 10,000 USD and receives 10,000 USDC, how is ryczałt revenue recognized?**
Assuming ordinary monthly/periodic B2B software billing, the income date is most often the **last day of the settlement period** under PIT art. 14 ust. 1e. If there is no contractual settlement period, the default is the **service completion / partial completion date**, not later than the invoice date or settlement date. So the date is **not automatically the USDC receipt date**. For a USD invoice, the clean business-revenue figure is **10,000 USD translated to PLN at the NBP average USD rate from the last working day before the income date**; the ryczałt is then **12% of that PLN amount**. ([ISAP][2])

**2. If the client pays in USDC but the invoice is denominated in USD or EUR, what drives the PLN conversion?**
My reading is that the **invoice / contractual receivable currency** should drive the business-income conversion, while the **payment medium** drives the later crypto consequences. So: invoice in USD/EUR, settlement in USDC → business revenue in PLN should still be determined off the USD/EUR receivable. This is also the cleaner interpretation line reported for a DKIS case involving a USD invoice settled in stablecoin-like crypto. ([Sejm API][1])

**3. Does it matter whether the invoice says “payable in USDC” vs “payable in USD (settlement in USDC)”?**
Yes. **Tax-wise, it matters.** “USD/EUR fee, settlement allowed in USDC” is the cleaner structure, because it keeps the service receivable anchored in a normal foreign currency and makes the ryczałt valuation argument much simpler. “Payable in USDC” pushes you toward saying the remuneration itself is a virtual-currency consideration, which is more dependent on market-value evidence and less neatly tied to the NBP foreign-currency conversion rule. In practice, I would strongly prefer **fiat-denominated remuneration + USDC settlement clause + agreed valuation source/timestamp**. That conclusion is an inference from the statutes plus the published interpretation summaries, not a sentence spelled out directly in the act. ([ISAP][2])

**4. For ryczałt purposes, is there any difference between EUR via bank and USDC on-chain?**
At the **service-tax level**, often no: the 12% ryczałt should be computed on the same underlying PLN service revenue if the remuneration is still denominated in EUR/USD. The difference is what happens later. EUR can create ordinary business FX differences; USDC usually does **not** fit that FX-difference regime, but instead creates later PIT-38 issues when you dispose of the coin. So the hidden complication is not a different ryczałt rate; it is the **second tax/compliance layer**. ([Sejm API][1])

### PIT-38 layer

**5. Is the “double-reporting” right: PIT-28/PIT-28 advances for the service and PIT-38 later for the crypto disposal? Does the ryczałt value become PIT-38 cost?**
Yes on the **two-layer structure**: the service revenue belongs in the business/ryczałt world, and later disposal of the virtual currency belongs in the **PIT-38 capital-income world**, because PIT art. 17 ust. 1g says the virtual-currency disposal rules also apply when the proceeds are obtained within business activity, except for businesses whose actual activity is virtual-currency exchange/broking/custody. ([ISAP][2])

The harder part is the **cost basis**. The statute says PIT-38 costs are the **documented expenses directly incurred to acquire** the virtual currency, plus disposal costs. It does **not** explicitly say, in black-letter statutory text, “the value previously taxed under ryczałt automatically becomes the acquisition cost.” Published summaries of DKIS interpretation **0115-KDIT1.4011.129.2023.2.MN** report exactly that favorable view: the satisfied business receivable/value of the service fee was treated as the direct acquisition cost for later PIT-38. I could confirm that interpretation’s existence and summaries, but I could not retrieve the full official EUREKA text in this environment, so I would treat this point as **well-supported but still interpretation-driven**, not perfect statute-level certainty. ([ISAP][2])

**6. If you convert USDC to EUR immediately, is the PIT-38 gain/loss basically zero?**
**Usually yes, if the favorable cost-basis view is accepted.** Then your disposal proceeds and your acquisition cost are almost the same, so the PIT-38 effect should be near zero apart from spread, fees, peg slippage, and timing differences between valuation and sale. If proceeds are slightly below costs, Poland’s crypto rules do **not** create a classic tax loss; excess costs roll forward to future years. ([Podatki][6])

**7. If you hold USDC for weeks/months waiting for a better EUR/PLN, does that movement become taxable on PIT-38?**
Yes. Once you hold the USDC, the later difference between its recognized acquisition cost and the value you realize on disposal is handled in the **PIT-38 crypto bucket**, not as ordinary business FX differences. If you later dispose at a lower value, you do not get a classic PIT-38 loss; you carry forward unused crypto costs. ([ISAP][2])

**8. If you use the USDC to buy ETH, is that non-taxable crypto-to-crypto?**
Yes, that is the standard statutory reading. The PIT disposal definition lists exchange of virtual currency for **legal tender, goods, services, other property rights, or settling obligations**. It does **not** list virtual-currency-to-virtual-currency exchange. Official MF guidance also says costs connected with exchanging one virtual currency for another are not treated as deductible disposal costs in that moment. ([ISAP][2])

### FX, accounting, VAT

**9. With EUR bank payments, FX differences arise. With USDC, do the same rules apply?**
For EUR: yes, ordinary business FX-difference rules can apply on ryczałt because the ryczałt act imports PIT art. 24c. For USDC: I would **not** treat later USDC/EUR or USDC/PLN movement as ordinary business FX differences. Virtual currency is defined separately from legal tender, and published interpretation summaries report the no-standard-FX-differences view for crypto settlements. Instead, the later movement is captured on PIT-38 when you dispose of the coin. ([Sejm API][1])

**10. Does the ewidencja przychodów need to record USDC differently from EUR?**
The **revenue entry itself** is still a PLN business-revenue entry based on the normal income-date/valuation rules. What changes is the supporting evidence: for USDC you need your own wallet and exchange trail because official MF guidance says crypto platforms do not issue PIT-8C/PIT-11 for you. So the register is not conceptually different, but the **audit pack** absolutely is. ([Sejm API][1])

**11. Any VAT difference between EUR and USDC?**
No material VAT difference just because of the payment rail. VAT follows the **service** and the place-of-supply rules, not whether the customer used SEPA or USDC. For B2B services, the general rule is art. 28b: customer location. Also, your threshold note is outdated: the Polish subject-matter exemption threshold is **240,000 PLN in 2026**. If the customer is in the EU, a VAT-exempt taxpayer may still need **VAT-UE registration** before the first qualifying cross-border B2B service. ([Gov.pl][5])

### Practical advantages / disadvantages

**12. Concrete tax advantages of USDC over EUR?**
Pure tax advantages are **limited**.

First, if the favorable cost-basis interpretation is respected, an **immediate** USDC→EUR/PLN sale is usually close to tax-neutral on PIT-38, so Option B can end up looking economically similar to EUR on the cash-tax side. ([Podatki][6])

Second, you can keep the funds **inside crypto** without immediate PIT-38 revenue, because crypto-to-crypto exchange is outside the disposal definition. That is more a **deferral / flexibility** benefit than a structural tax saving. ([ISAP][2])

Third, **your 319k PLN crypto cost pool matters**. Because business-obtained crypto disposals are still routed into the same PIT-38 virtual-currency regime, your existing carried-forward crypto costs should still be relevant against later sale proceeds. Official MF guidance confirms that unused crypto costs roll forward. For you specifically, that means Option B’s extra PIT-38 cash burden may be very low for some time. ([ISAP][2])

What this does **not** give you is a reliable “tax arbitrage.” Holding USDC and choosing when to convert can change the later PIT-38 result, but that is market exposure, not a built-in tax optimization. ([ISAP][2])

**13. Concrete disadvantages / risks?**
Yes:

1. **Two compliance buckets** instead of one: service revenue on ryczałt plus crypto disposal on PIT-38. ([ISAP][2])
2. **Cost-basis uncertainty**: the favorable result exists in interpretation summaries, but I would not call it bulletproof without your own interpretation. ([akademialtca.pl][7])
3. **Heavier documentation**: invoice/contract + wallet tx + valuation + exchange docs + self-maintained PIT-38 evidence. Exchanges do not send you a ready PIT-8C/PIT-11. ([Podatki][6])
4. **More AML/banking friction** in practice.
5. **Spending USDC directly** on goods/services/debts is itself a PIT-38 disposal, while on ryczałt your business costs generally do not reduce the 12% tax base. So using crypto as your operating cash can be especially clumsy on ryczałt. ([ISAP][2])

**14. Are there KIS interpretations specifically about ryczałt JDG receiving crypto/stablecoins?**
Yes, there are relevant interpretations or at least clearly indexed official search results:

* **0113-KDIPT2-3.4011.452.2017.1.AC** — official EUREKA result indicates that payment in virtual currency for a performed service does **not** make the business income arise on the payment date. ([eureka.mf.gov.pl][8])
* **0113-KDIPT2-1.4011.496.2022.2.MGR** — official EUREKA indexing shows keywords including **barter**, **ryczałt ewidencjonowany**, **kapitały pieniężne**, and **kryptowaluty**, so this one is directly in the zone you care about. ([eureka.mf.gov.pl][8])
* **0115-KDIT1.4011.129.2023.2.MN** — published summaries describe a JDG service fee in USD paid in stablecoin-like crypto, with the receivable value treated as the direct acquisition cost for later PIT-38 disposal. Again: I found the summaries and the sygnatura, but not the full official text in this environment. ([akademialtca.pl][9])

### Cash flow and banking

**15. If you receive USDC, convert to EUR on Binance/Kraken, then withdraw EUR to the business bank account, does the bank withdrawal create extra tax/reporting?**
The **taxable disposal** is the **USDC → EUR** exchange. The later **EUR transfer from the exchange to your bank** is not a second disposal event. The real issue is not a new tax event, but keeping a clean record of the trade, fees, and transfer chain. ([ISAP][2])

**16. AML/compliance: does a software JDG receiving on-chain payments need to register as a crypto service provider?**
On your facts, **no**. The regulated activity requiring entry in the Polish register is business consisting of: exchange crypto↔fiat, crypto↔crypto, broking such exchange, or running custody/account services for others. Merely accepting USDC as payment for your own software services is not that activity. The registry itself is still operating in 2026 for businesses that actually provide those services. ([ISAP][4])

## Practical recommendation for your setup

For **your** profile, I would treat the options this way:

* **Default / conservative choice:** **Option A (EUR)**. Lowest compliance burden, lowest interpretive risk, easiest bank and tax trail.
* **Option B (USDC)** only makes sense if you have a real non-tax reason to want it: on-chain settlement, intentional crypto treasury exposure, or desire to keep proceeds inside crypto instead of cashing out immediately.

Because you already have a large **319k PLN PIT-38 cost pool**, Option B is **less painful for you** than it would be for a typical taxpayer: that pool should be relevant against later disposals of business-received USDC, since those disposals still sit in the PIT-38 virtual-currency regime. But that is a **buffer**, not a reason that USDC is inherently better than EUR. ([ISAP][2])

My practical recommendation would be:

1. **If you stay with USDC, keep the commercial fee denominated in EUR or USD**, and write the contract/invoice as **“settlement may be made in USDC equivalent”** with a defined rate source and timestamp.
2. **Use a dedicated business wallet and exchange account** to avoid mixing business and personal flows.
3. **Convert quickly** if your goal is to minimize PIT-38 volatility.
4. **Do not scale this without an individual KIS interpretation** focused on two points:

   * the PLN valuation method for a fiat-denominated invoice settled in USDC, and
   * confirmation that the satisfied receivable is the **art. 22 ust. 14** acquisition cost for later PIT-38 disposal.

So the cleanest summary is:

* **EUR:** simpler, safer, usually the right default.
* **USDC:** can be made workable, and for you the cash-tax downside may be softened by the existing crypto cost pool, but it adds a second tax layer, more evidence work, and one important interpretation risk.

[1]: https://api.sejm.gov.pl/eli/acts/DU/2020/1905/text.html "https://api.sejm.gov.pl/eli/acts/DU/2020/1905/text.html"
[2]: https://isap.sejm.gov.pl/isap.nsf/download.xsp/WDU20250000163/T/D20250163L.pdf "https://isap.sejm.gov.pl/isap.nsf/download.xsp/WDU20250000163/T/D20250163L.pdf"
[3]: https://www.podatki.gov.pl/twoj-e-pit/pit-28-za-2025-rok/ "https://www.podatki.gov.pl/twoj-e-pit/pit-28-za-2025-rok/"
[4]: https://isap.sejm.gov.pl/isap.nsf/download.xsp/WDU20250000644/T/D20250644L.pdf "https://isap.sejm.gov.pl/isap.nsf/download.xsp/WDU20250000644/T/D20250644L.pdf"
[5]: https://www.gov.pl/attachment/8fde481a-18aa-4b1b-843e-5bbd303d6f94 "https://www.gov.pl/attachment/8fde481a-18aa-4b1b-843e-5bbd303d6f94"
[6]: https://www.podatki.gov.pl/podatki-osobiste/pit/informacje-podstawowe/co-jest-opodatkowane/zbycie-kryptowalut/ "https://www.podatki.gov.pl/podatki-osobiste/pit/informacje-podstawowe/co-jest-opodatkowane/zbycie-kryptowalut/"
[7]: https://akademialtca.pl/Materialy/Z_pasji_do_podatkow_22.05.23.pdf?srsltid=AfmBOooUu7eZAmVHTyW5F5gDqdDYQE_4kXl2TSwaOAyS5jjk_st6W2cn "https://akademialtca.pl/Materialy/Z_pasji_do_podatkow_22.05.23.pdf?srsltid=AfmBOooUu7eZAmVHTyW5F5gDqdDYQE_4kXl2TSwaOAyS5jjk_st6W2cn"
[8]: https://eureka.mf.gov.pl/informacje/podglad/511223%3BkeyWords%3D0113-KDIPT2-3.4011.452.2017.1.AC "https://eureka.mf.gov.pl/informacje/podglad/511223%3BkeyWords%3D0113-KDIPT2-3.4011.452.2017.1.AC"
[9]: https://akademialtca.pl/Materialy/Z_pasji_do_podatkow_22.05.23.pdf?srsltid=AfmBOoqrd-vrErQwaBE9Yu46waVODT-6tyv8_fLa7MT4xGJlA1RW2_Z7 "https://akademialtca.pl/Materialy/Z_pasji_do_podatkow_22.05.23.pdf?srsltid=AfmBOoqrd-vrErQwaBE9Yu46waVODT-6tyv8_fLa7MT4xGJlA1RW2_Z7"
