## Bottom line

For a typical one-person software-development JDG on **ryczałt ewidencjonowany**, the income tax is usually **12% of tax revenue, not profit**. The legal rate for software/IT-related services is in **art. 12 ust. 1 pkt 2b** of the ryczałt act, while **art. 12 ust. 2** says ryczałt is computed **without deducting tax costs**. The important caveat is that the rate turns on the **actual PKWiU classification of the service**, not only the PKD entry such as 62.01.Z. If Polish VAT is charged, that VAT portion is not PIT/ryczałt revenue. ([European Legislation Identifier][1])

For EUR invoices, you still settle income tax in PLN. The EUR amount is translated using the **NBP average rate from the last business day before the day the revenue is obtained**. Under the default rule, the decisive date is usually the **revenue date** under the PIT act, not automatically the invoice date or payment date. From **1 January 2025**, ryczałt taxpayers can elect a **cash method** for B2B invoice-based transactions, in which case the payment date becomes the revenue date. ([European Legislation Identifier][2])

Monthly ryczałt is paid by the **20th of the next month** to the **mikrorachunek podatkowy**; there is **no separate monthly PIT declaration** comparable to JPK_V7 for this income tax. The annual return is **PIT-28**, filed from **15 February to 30 April** of the following year. ZUS is a **separate** monthly obligation, and for a solo JDG it is generally handled through **ZUS DRA**. ([European Legislation Identifier][1])

## Monthly obligations

**1) Is it 12% of gross revenue with no costs?**
Yes, for a typical software-development JDG the ryczałt is usually **12% of revenue** under **art. 12 ust. 1 pkt 2b**. It is a tax on **revenue, not profit**, and **tax-deductible costs are ignored** under **art. 12 ust. 2**. The nuance is that the legal test is the **actual service classification (PKWiU)**, not just the PKD code you registered. Also, if a transaction is subject to Polish VAT, the VAT amount is not part of PIT/ryczałt revenue. A limited deduction still exists for **50% of paid health contributions**, which can reduce ryczałt revenue under **art. 11 ust. 1a**. ([European Legislation Identifier][1])

**2) How does EUR invoicing work?**
You may invoice and get paid in EUR, but for tax you must convert the taxable revenue to PLN. The conversion rule comes from **PIT art. 11a ust. 1**, which the ryczałt regime uses through **art. 6** of the ryczałt act: use the **NBP average rate from the last business day before the day the revenue is obtained**. ([European Legislation Identifier][1])

**3) Which date controls the EUR→PLN conversion: invoice date, payment date, or something else?**
By default, it is the **revenue date**, not simply “invoice date” or “payment date.” For ordinary services, **PIT art. 14 ust. 1c** says the revenue date is the day the service is performed or partially performed, **no later than** the invoice date or payment date. For services settled in **periodic settlement periods**—which is very common in monthly B2B software contracts—**PIT art. 14 ust. 1e** moves the revenue date to the **last day of the settlement period** stated in the contract or invoice. From **2025**, if you validly elected the **cash method**, then **PIT art. 14c** makes the **payment date** the revenue date for covered B2B invoice transactions. For a JDG started mid-2025, that election had to be notified by the **20th day of the month after starting** the business, or by year-end if starting in December. ([European Legislation Identifier][2])

A practical example: if your contract says services are settled monthly for June 2025 and you invoice on 30 June but get paid on 10 July, the default rule usually treats **30 June 2025** as the revenue date, so the PLN amount is based on the **NBP average rate from the last business day before 30 June**. If you had elected the **cash method** for 2025, the relevant date would instead shift to **10 July 2025**. ([European Legislation Identifier][2])

**4) When are monthly tax payments due, and what gets filed monthly?**
The ryczałt payment is due by the **20th day of the next month**; the amount for **December** is due by **20 January** of the next year under **art. 21 ust. 1**. There is **no standalone monthly income-tax return** like JPK_V7 for ryczałt. In practice, you calculate the monthly tax yourself, keep the revenue records, and **pay it to your mikrorachunek podatkowy** identified with your **NIP**. Ministry guidance uses **PPE** as the payment symbol for during-year ryczałt payments, while **PIT-28** is the annual settlement symbol. JPK_V7/JPK_VAT is a **VAT** filing, not a ryczałt income-tax filing. ([European Legislation Identifier][1])

**5) Is ZUS separate, and what does it look like in the first years?**
Yes. **ZUS is separate from the tax office payment.** For a sole proprietor with only their own insurance, the monthly declaration is generally **ZUS DRA**, and the deadline for both the declaration and payment is usually the **20th of the next month**. There is also a separate **annual health-contribution reconciliation** shown in the **April** declaration of the following year, with payment due by **20 May**. ([zus.pl][3])

For a new business, **ulga na start** can exempt you from **social** ZUS for **6 calendar months**; during that relief period you still pay **health insurance**. If the business starts in the middle of a month, the 6-month count starts from the **next month**. After ulga na start, you can move to **preferencyjne składki** for up to **24 calendar months**, if you meet the conditions. During the preferential period, health insurance remains obligatory. ([zus.pl][4])

For **2025**, the ryczałt health contribution is a **fixed monthly amount based on annual revenue brackets**, not a percentage of actual monthly income: **461.66 PLN** up to **60,000 PLN** annual revenue, **769.43 PLN** above **60,000 PLN** up to **300,000 PLN**, and **1,384.97 PLN** above **300,000 PLN**. For the **preferential social base** in 2025, the base is **1,399.80 PLN**; minimum components are **273.24 PLN** pension, **111.98 PLN** disability, **34.30 PLN** voluntary sickness, plus accident insurance according to the applicable rate; there is no Fundusz Pracy when the mandatory base is below minimum wage. ([zus.pl][5])

## Yearly filing

**6) What is the annual form and deadline?**
The annual return for ryczałt is **PIT-28**. The filing window is **15 February through 30 April** of the year after the tax year. For tax year **2025**, that means filing by **30 April 2026**. It can be filed through **Twój e-PIT / e-Urząd Skarbowy**, the e-US app, e-Deklaracje, or on paper. ([European Legislation Identifier][1])

**7) What gets reported on PIT-28?**
It is not only a single annual number. The annual return covers the year’s **revenue**, permitted **deductions**, and the **ryczałt due**, and the PIT-28 also includes a section showing the ryczałt calculated during the year for each **month or quarter**. The underlying monthly bookkeeping remains your **ewidencja przychodów**. ([European Legislation Identifier][1])

**8) How does a mid-year start work?**
A JDG started in, for example, **March 2025** still files **one PIT-28 for 2025**, but it reports only the revenue actually earned **from the start date through 31 December 2025**. There is no separate “full-year equivalent” computation in the PIT-28 mechanism. For recordkeeping, the ryczałt act still requires the ordinary **ewidencja przychodów**, and if you use the 2025 cash method you also need the additional **invoice register** under **art. 15 ust. 11a**. ([European Legislation Identifier][1])

**9) Are there extra annual information returns because the clients are foreign?**
For income tax, I did **not** find a separate annual PIT information return that exists **only because the client is foreign**. The ordinary annual income-tax return remains **PIT-28**. The extra recurring obligations for foreign B2B clients are usually on the **VAT side**, especially **VAT-R** registration, **VAT-UE** information returns for qualifying EU B2B services, and **JPK_VAT/JPK_V7** if you are VAT-active. Separately, ZUS has the annual health-contribution reconciliation in the following April declaration. ([Podatki][6])

**10) Does VAT registration matter?**
Yes, but mainly for the **VAT layer**, not for the 12% income-tax mechanism itself. If you are **VAT-active**, you generally file **JPK_VAT** (currently JPK_V7M monthly or JPK_V7K quarterly, depending on your VAT settlement method). If you are **VAT-exempt** under the small-business exemption, you generally do **not** file JPK_VAT. However, a VAT-exempt taxpayer can still register for **VAT-UE** for qualifying intra-EU B2B services **without losing the VAT exemption**, and filing **VAT-UE alone does not create a JPK_VAT obligation**. ([Podatki][7])

For **2025**, the Polish VAT-exemption threshold is **200,000 PLN**, and for a business started mid-year it is **pro-rated** to the period of activity in that year. The increase to **240,000 PLN** starts only from **1 January 2026**. If you provide services to an EU business customer in a case covered by the B2B rule of **VAT Act art. 28b**, the customer generally accounts for the VAT in their own country, and **VAT-UE** filing may be required by the **25th of the next month**. ([Podatki][8])

## EUR-specific issues

**11) Are there FX gains/losses on EUR held in the business account?**
Yes. The ryczałt act, in **art. 6 ust. 1c**, imports the PIT act’s **art. 24c** foreign-exchange-difference rules. Positive FX differences increase taxable revenue and negative FX differences reduce it. This can happen when the EUR receivable is paid, and it can also happen later when EUR funds held in the business account are used, paid out, or exchanged. ([European Legislation Identifier][1])

**12) Is converting EUR to PLN in the bank a taxable FX event?**
Usually yes. Under **PIT art. 24c**, realized FX differences arise not only on collection of a foreign-currency receivable, but also on later **sale / outflow / payment using foreign-currency funds**. Where there is an actual bank conversion, the actual rate used in that transaction matters; if there is no actual rate, the statute falls back to the **NBP average from the last business day before the relevant day**. ([European Legislation Identifier][2])

**13) If you receive EUR and simply hold it, is there a year-end revaluation?**
Under the ordinary **art. 24c** mechanism, I did **not** find a separate year-end tax revaluation rule for a ryczałt JDG that merely continues to hold EUR. The statutory FX-difference rules are written around **realized events** such as receipt, payment, sale, or outflow of the foreign currency. So, as a practical rule, simply holding EUR through year-end does **not usually** create a separate ryczałt tax event by itself. ([European Legislation Identifier][1])

## Interaction with personal taxes

**14) Does ryczałt JDG income mix with PIT-38 crypto income?**
No. **Art. 3** of the ryczałt act says income taxed under ryczałt is **not combined** with income taxed under the ordinary PIT act. Crypto disposals are generally reported on **PIT-38**, even if the crypto transaction happens “in business,” unless you run the specifically regulated virtual-currency business described in the PIT guidance. ([European Legislation Identifier][1])

**15) Can business losses offset crypto gains, or vice versa?**
No. First, ryczałt normally does **not** produce an ordinary current-year “business loss” from expenses, because **costs are ignored**. Second, PIT-38 crypto results are separate: when crypto costs exceed crypto revenue, the statute does **not** create a deductible tax loss in the usual sense; instead, unused crypto acquisition costs are carried forward **within the crypto regime**. So there is no cross-offset between a ryczałt JDG and PIT-38 crypto. ([European Legislation Identifier][1])

**16) Is health insurance calculated differently under ryczałt, and what is the 2025 amount?**
Yes. Under ryczałt, the health contribution is based on **annual revenue brackets**, not actual monthly profit. For **2025**, the monthly amounts are **461.66 PLN**, **769.43 PLN**, and **1,384.97 PLN** depending on whether your annual revenue is up to **60,000 PLN**, above **60,000 PLN** to **300,000 PLN**, or above **300,000 PLN**. Also, **50% of paid health contributions** can reduce ryczałt revenue under **art. 11 ust. 1a** of the ryczałt act. ([zus.pl][5])

## What changed between 2024 and 2025 for this fact pattern

The material change I found for **2025** is that, from **1 January 2025**, ryczałt taxpayers can elect the **cash method** for qualifying B2B invoice transactions; that option did not exist in the earlier ryczałt rules the same way. The other clear 2024→2025 change is the **health-contribution amounts**: for ryczałt they increased from **419.46 / 699.11 / 1,258.39 PLN** in **2024** to **461.66 / 769.43 / 1,384.97 PLN** in **2025**. ([European Legislation Identifier][1])

## Practical compliance cycle

Each month, the usual sequence is: determine the **revenue date**; convert EUR revenue to PLN using the correct **NBP rate**; enter it into the **ewidencja przychodów**; include any **realized FX differences** when they arise; calculate the monthly ryczałt at **12%**; pay it by the **20th** to the **mikrorachunek**; and separately file/pay **ZUS** by the **20th**. If you are VAT-active, add **JPK_VAT/JPK_V7** by the **25th**; if you are VAT-exempt but providing qualifying EU B2B services, add **VAT-UE** by the **25th**. After year-end, file **PIT-28** by **30 April**, and complete the **annual health-contribution reconciliation** in the following **April ZUS declaration**, due by **20 May**. ([European Legislation Identifier][2])

Key legal anchors for your scenario are: **ryczałt act art. 12 ust. 1 pkt 2b** (12% software/IT rate), **art. 12 ust. 2** (no cost deduction), **art. 6 ust. 1c** (FX differences), **art. 6 ust. 1g** (cash method from 2025), **art. 15** (records), and **art. 21** (monthly payment and annual PIT-28 filing window), plus the cross-referenced **PIT act art. 11a**, **art. 14**, **art. 14c**, and **art. 24c** for EUR translation, revenue timing, cash method, and FX differences. ([European Legislation Identifier][1])

If useful, I can turn this into a one-page checklist for “monthly / annual / VAT / ZUS” operations for a Poland JDG invoicing in EUR.

[1]: https://eli.gov.pl/api/acts/DU/2025/843/text/O/D20250843.pdf "https://eli.gov.pl/api/acts/DU/2025/843/text/O/D20250843.pdf"
[2]: https://eli.gov.pl/api/acts/DU/2025/163/text/T/D20250163L.pdf "https://eli.gov.pl/api/acts/DU/2025/163/text/T/D20250163L.pdf"
[3]: https://www.zus.pl/documents/10182/167567/poradnik%2BZUS%2BDRA.pdf "https://www.zus.pl/documents/10182/167567/poradnik%2BZUS%2BDRA.pdf"
[4]: https://www.zus.pl/-/ulga-na-start-preferencyjna-podstawa-dzialalnosc-nieewidencjonowana-jakie-sa-warunki-uprawnienia-i-skutk-1 "https://www.zus.pl/-/ulga-na-start-preferencyjna-podstawa-dzialalnosc-nieewidencjonowana-jakie-sa-warunki-uprawnienia-i-skutk-1"
[5]: https://www.zus.pl/-/informacja-w-sprawie-podstawy-wymiaru-sk%C5%82adki-oraz-kwoty-sk%C5%82adki-na-ubezpieczenie-zdrowotne-w-2025-r.-dla-niekt%C3%B3rych-grup-ubezpieczonych "https://www.zus.pl/-/informacja-w-sprawie-podstawy-wymiaru-sk%C5%82adki-oraz-kwoty-sk%C5%82adki-na-ubezpieczenie-zdrowotne-w-2025-r.-dla-niekt%C3%B3rych-grup-ubezpieczonych"
[6]: https://www.podatki.gov.pl/podatki-firmowe/pit/informacje-podstawowe/ "https://www.podatki.gov.pl/podatki-firmowe/pit/informacje-podstawowe/"
[7]: https://www.podatki.gov.pl/podatki-firmowe/jednolity-plik-kontrolny/jpk_vat/jpk_vat/ "https://www.podatki.gov.pl/podatki-firmowe/jednolity-plik-kontrolny/jpk_vat/jpk_vat/"
[8]: https://www.podatki.gov.pl/podatki-firmowe/vat/stawki-i-limity/ "https://www.podatki.gov.pl/podatki-firmowe/vat/stawki-i-limity/"
