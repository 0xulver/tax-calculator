# JDG Ryczałt Tax Compliance Guide: IT Services in EUR (Poland 2025)

> **Scope:** This guide covers the full annual and monthly tax compliance cycle for a Polish sole proprietorship (JDG) registered under PKD 62.01.Z (software development), taxed under *ryczałt od przychodów ewidencjonowanych* at 12%, invoicing B2B clients in EUR. All figures reflect **tax year 2025** unless otherwise noted.

***

## Executive Summary

A JDG providing IT services under PKD 62.01.Z on ryczałt pays **12% tax on gross EUR revenue** converted to PLN — no cost deductions apply. Monthly obligations consist of a single bank transfer by the 20th of each following month, with no monthly declaration to file. The annual return is **PIT-28**, due **30 April 2026** for tax year 2025. EUR invoicing triggers mandatory NBP exchange-rate conversions and FX difference calculations. ZUS social contributions are entirely separate from income tax. Crypto gains are reported on a separate **PIT-38** form and cannot be offset against ryczałt income.

***

## Part 1: Monthly Tax Obligations

### 1.1 The 12% Rate for PKD 62.01.Z

Under **Art. 12 ust. 1 pkt 2b** of the *Ustawa o zryczałtowanym podatku dochodowym od niektórych przychodów osiąganych przez osoby fizyczne* (hereafter: "ustawa o ryczałcie"), the 12% rate applies to services related to:[^1][^2]

- PKWiU **62.01.1** — software design, programming, and development services
- PKWiU **62.01.2** — original software products
- PKWiU **62.02.10.0** — computer hardware advisory services
- PKWiU **62.09.20.0** — software installation services
- PKWiU **62.03.1** — network and IT system management

The 12% applies to **gross revenue** — there are **no deductions for costs** of any kind. A lower rate of 8.5% applies only to specific PKD 62.01 activities not involving programming (e.g., pure QA/testing without coding), which is a distinct minority position requiring careful classification. Standard software development, contract programming, web development, and architecture services all fall under 12%.[^3][^4][^5][^6]

### 1.2 What to Pay and When

During the tax year, ryczałt taxpayers **do not file any monthly declaration or form**. The obligation is purely a payment:[^7][^8]

- **Monthly taxpayers:** Transfer the ryczałt amount to your individual *mikrorachunek podatkowy* (tax micro-account) by the **20th day of the following month**. The amount for December is due **20 January** of the next year.[^9][^10]
- **Quarterly taxpayers:** If prior-year revenue did not exceed the equivalent of 200,000 EUR (approx. PLN 856,920 in 2025), you may opt for quarterly payments due by the 20th of the month after each quarter (i.e., 20 April, 20 July, 20 October, and 20 January).[^11][^9]

The payment is made via standard bank transfer using your unique mikrorachunek number. The applicable tax type code is **PPE** (podatek od przychodów ewidencjonowanych).[^8]

**There is no JPK_V7 or any periodic PIT form to submit monthly.** The only periodic electronic obligation relates to VAT-registered taxpayers (see Part 4).

### 1.3 Maintaining the Revenue Register (*Ewidencja Przychodów*)

Ryczałt taxpayers must maintain an *ewidencja przychodów* (revenue register) recording each invoice with date, number, and revenue amount per applicable stawka. The register must include:[^12][^13][^11]

- Invoice date and number
- Amounts by ryczałt rate tier (separate column for 12% vs any other applicable rate)
- EUR amounts converted to PLN (with the NBP rate applied — see Part 2)

If maintained electronically, the register must be exportable as **JPK_EWP** on demand from the tax authority. From 2027 (for tax year 2026 data), JPK_EWP will become an **annual mandatory submission** filed alongside PIT-28.[^14][^12]

***

## Part 2: EUR Invoicing — Exchange Rate Rules

### 2.1 Revenue Recognition Date

Under **Art. 14 ust. 1c ustawy o PIT** (applied by reference to ryczałt taxpayers), the revenue recognition date is the **earliest** of the following three events:[^15][^16]

1. Date of **service execution** (*wykonanie usługi*) or partial execution
2. Date the **invoice was issued** (*wystawienie faktury*)
3. Date **payment was received** (*uregulowanie należności*)

In practice for monthly retainer B2B IT contracts, if an invoice is issued on (say) the last day of the month for services rendered during that month, the invoice date is the recognition date. If the client pays in advance before the invoice, the payment receipt date becomes the recognition date.

### 2.2 Which NBP Rate to Use

Revenue denominated in EUR must be converted to PLN using the **NBP average (mid) rate** (*kurs średni NBP*) from the **last working day preceding** the revenue recognition date.[^17][^18][^15]

**Example:** If a service was completed (and invoice issued) on Wednesday 25 June 2025, the applicable NBP rate is the mid-rate published for **Tuesday 24 June 2025**. If the 24th is a holiday, use the rate from the last working day before that.

NBP rates are published daily at [nbp.pl/kursy](https://www.nbp.pl/home.aspx?f=/kursy/kursy.html) (Table A — average rates).

### 2.3 Booking the EUR Invoice in PLN

For each EUR invoice:

1. Identify the revenue recognition date (earliest of service/invoice/payment)
2. Look up NBP average EUR rate from the preceding working day
3. Multiply EUR amount × NBP rate = PLN revenue to enter in *ewidencja przychodów*
4. Record the NBP rate and date in your documentation for audit purposes

***

## Part 3: FX Gains and Losses (*Różnice Kursowe*)

### 3.1 Legal Basis

Ryczałt taxpayers are required to calculate FX differences on EUR revenues under **Art. 6 ust. 1c ustawy o ryczałcie**, which refers to **Art. 24c ustawy o PIT** with a modification: since ryczałt has no costs, **negative FX differences reduce revenue** (rather than increasing costs as they would under general rules).[^19][^20][^21]

Only revenue-side FX differences are relevant — there are no cost-side FX differences in ryczałt.[^21][^19]

### 3.2 How to Calculate

An FX difference arises when the EUR/PLN rate at the time of payment differs from the rate used to book the invoice:

- **Positive FX difference** (PLN received > PLN booked): EUR weakened between invoice date and payment → you received more PLN than booked. This **increases taxable revenue**.[^20][^22]
- **Negative FX difference** (PLN received < PLN booked): EUR strengthened between invoice and payment → you received less PLN than booked. This **decreases taxable revenue**.[^19][^20]

The FX difference equals:

> (PLN value at actual payment rate) − (PLN value at invoice NBP rate)

The "actual payment rate" is the bank's exchange rate applied on the day of receipt (*faktycznie zastosowany kurs waluty z dnia jego otrzymania*). If funds remain in a EUR account without conversion, the rate is typically the bank's buy rate on the date the payment was credited.[^20][^21]

### 3.3 Tax Rate on FX Differences

FX differences are taxed at the **same ryczałt rate as the underlying service** — i.e., **12%** for IT services.[^22]

### 3.4 EUR Held Without Converting

If EUR is retained in the business bank account without converting to PLN, FX differences are still calculated and recognized at the time the payment was **received** (credited to account), not deferred to the conversion date. There is **no year-end mark-to-market revaluation** requirement for ryczałt taxpayers — the FX difference crystallizes upon receipt of payment, regardless of whether the EUR is subsequently converted.[^21]

***

## Part 4: ZUS — Social and Health Insurance

ZUS obligations are entirely separate from income tax and paid to ZUS, not to the tax office.

### 4.1 Ulga na Start (First 6 Months)

New entrepreneurs may use the **ulga na start** for the first 6 calendar months of business activity. During this period:[^23][^24]

- **No social contributions** (emerytal, rentowe, chorobowe, wypadkowe) are due
- **Only health insurance** (*składka zdrowotna*) must be paid

This effectively reduces early-stage ZUS costs dramatically.

### 4.2 Preferencyjne Składki ZUS (Months 7–30)

After ulga na start (or upon waiving it), the entrepreneur pays **preferential (reduced) social contributions** for **24 full calendar months**, with a base of **30% of minimum wage**.[^25][^24]

| Contribution | Rate | 2025 Base (1,399.80 PLN) | 2025 Monthly |
|---|---|---|---|
| Emerytalna | 19.52% | 1,399.80 PLN | 273.24 PLN[^26] |
| Rentowa | 8.00% | 1,399.80 PLN | 111.98 PLN[^26] |
| Wypadkowa | 1.67% | 1,399.80 PLN | 23.38 PLN[^26] |
| Chorobowa (voluntary) | 2.45% | 1,399.80 PLN | 34.30 PLN[^26] |
| **Total (with sickness)** | | | **442.90 PLN[^26]** |
| **Total (without sickness)** | | | **408.60 PLN[^26]** |

In 2026, the minimum wage rises and the preferential base becomes 1,441.80 PLN, pushing total to 456.18 PLN/month (without sickness).[^27][^25]

### 4.3 Health Insurance (*Składka Zdrowotna*) Under Ryczałt 2025

Health insurance for ryczałt payers is a **fixed monthly amount** based on three revenue tiers (regardless of actual monthly revenue, the tier is assessed based on projected/prior-year annual revenue):[^28][^29][^30]

| Annual Revenue | Base | Monthly Contribution 2025 | Monthly 2026 |
|---|---|---|---|
| Up to 60,000 PLN | 60% avg. wage = 5,129.51 PLN | **461.66 PLN[^28]** | 498.35 PLN[^31] |
| 60,001–300,000 PLN | 100% avg. wage = 8,549.18 PLN | **769.43 PLN[^28]** | 830.58 PLN[^31] |
| Over 300,000 PLN | 180% avg. wage = 15,388.52 PLN | **1,384.97 PLN[^28]** | 1,495.04 PLN[^31] |

The base is **przeciętne wynagrodzenie z IV kwartału 2024 = 8,549.18 PLN**. Health insurance is paid at the rate of **9% of the applicable base**.[^30][^28]

> **Important:** Health insurance is **not deductible** from the ryczałt tax base (unlike under podatek liniowy). It is a separate cost of running the business.

ZUS social and health contributions are due by the **20th of the following month**.[^32]

***

## Part 5: Annual Filing — PIT-28

### 5.1 Form and Deadline

The annual return for ryczałt is **PIT-28**. For tax year 2025:[^33][^34][^35]

- **Filing window:** 15 February 2026 – **30 April 2026**[^34][^35][^33]
- Filings submitted before 15 February are treated as received on 15 February[^34]
- The form can be filed via **Twój e-PIT** (e-Urząd Skarbowy portal), the e-US mobile app, e-Deklaracje, or in paper form[^36]

> **Change from prior law:** Before 2022, PIT-28 was due by 31 January. The current 30 April deadline has been in force since tax year 2021. Some older sources still cite 31 January — this is outdated.[^37][^33]

### 5.2 Content of PIT-28

PIT-28 reports:[^38][^36]

- Total annual revenue broken down by ryczałt rate (12%, 8.5%, etc.)
- Health insurance amounts paid during the year
- Ryczałt tax calculated (sum of revenue × applicable rates)
- Any overpayments/underpayments vs monthly transfers
- Applicable deductions (IKZE contributions, internet, donations — ryczałt has limited deductions vs linear tax)

The form does **not require a month-by-month breakdown** — only annual totals per rate. Monthly details are maintained in the *ewidencja przychodów* register, not in the return itself.[^7][^12]

### 5.3 Mid-Year Business Start (Partial Year)

If the JDG was established in 2025 (say March or later), the PIT-28 for 2025 reports **only revenue earned from the date of business registration** through 31 December 2025. There is no special form for a partial year — PIT-28 simply contains the amounts actually earned during the period of activity.[^6][^39]

Note that for a JDG starting mid-year, the **VAT exemption limit of 200,000 PLN is prorated** proportionally to the number of months of operation. This also effectively reduces the ryczałt eligibility limit for the first year.[^40]

### 5.4 Any Tax Balance Due

If the monthly ryczałt payments made during the year are less than the annual tax calculated on PIT-28, the **underpayment must be settled by 30 April 2026** (the filing deadline). If overpaid, a refund is claimed on the same form.[^41]

***

## Part 6: VAT Considerations

### 6.1 VAT-Exempt (Zwolnienie Podmiotowe)

A JDG may remain VAT-exempt (*zwolniony podmiotowo*) as long as annual turnover does not exceed **200,000 PLN**. For a business started mid-year, this limit is prorated by months of operation.[^42][^43][^44][^40]

When VAT-exempt:
- **No JPK_V7** filing required[^45][^42]
- No output VAT charged on invoices
- No input VAT deduction on purchases
- Invoices carry "np" (nie podlega) notation instead of a VAT rate

### 6.2 B2B Services to EU Clients — Critical VAT-UE Obligation

Even when VAT-exempt in Poland, a JDG providing B2B IT services to EU-registered companies **must register for VAT-UE** before performing the first such service, using **form VAT-R** (Section C.3). This does not change the VAT-exempt status — it only activates the EU reporting number.[^46][^47]

Under **Art. 28b ustawy o VAT**, place of supply for B2B services is the **buyer's country** (reverse charge). The Polish JDG therefore invoices without Polish VAT, adding the annotation:

> *"Usługa nie podlega opodatkowaniu w Polsce — art. 28b ustawy o VAT. Miejsce opodatkowania: kraj nabywcy. Reverse charge."*[^48][^49]

**Following each month where EU B2B services were rendered, the JDG must file:**

| Form | Purpose | Deadline |
|---|---|---|
| **VAT-UE** (*Informacja podsumowująca*) | Report value of intra-EU B2B services per client NIP-UE | 25th day of following month[^50][^51] |

If no EU B2B transactions occurred in a given month, no VAT-UE filing is required. For clients outside the EU (e.g., a non-EU company), VAT-UE does not apply.[^52][^50]

### 6.3 VAT-Registered (Czynny Podatnik VAT)

If the JDG voluntarily registers as a VAT czynny taxpayer or exceeds the 200,000 PLN threshold:
- Monthly **JPK_V7** must be filed by the **25th of the following month**[^32]
- Output VAT is charged on domestic sales; EU B2B is still 0% with reverse charge[^48]
- Input VAT on business purchases becomes deductible
- EU B2B services must still be reported in VAT-UE[^53]

### 6.4 KSeF — Mandatory E-Invoicing from April 2026

The **Krajowy System e-Faktur (KSeF)** becomes mandatory for most JDGs from **1 April 2026**:[^54][^55][^56]

- From 1 February 2026: large enterprises (2024 turnover > 200 mln PLN)
- From **1 April 2026**: all remaining VAT-registered taxpayers and JDGs
- From 1 January 2027: micro-businesses with monthly invoiced sales ≤ 10,000 PLN[^57][^54]

For a VAT-exempt JDG that is also VAT-UE registered, the KSeF obligation depends on whether the JDG is a "podatnik VAT czynny" — VAT-exempt entities may have a deferred obligation. Clarification from MF guidance is recommended as this boundary is still evolving.

***

## Part 7: Ryczałt and Personal Taxes — Integration

### 7.1 Crypto Capital Gains (PIT-38)

Ryczałt business income (PIT-28) and crypto capital gains (PIT-38) are **completely separate tax streams** with no interaction:[^58][^59][^60]

| | PIT-28 (Ryczałt) | PIT-38 (Crypto) |
|---|---|---|
| Tax base | Gross revenue (no cost deduction) | Net gain (revenue minus acquisition costs) |
| Rate | 12% (IT services) | 19% flat |
| Deadline | 30 April 2026 | 30 April 2026 |
| Can offset other source? | No | No (crypto gain/loss only offsets crypto) |

There are no "business losses" under ryczałt — the tax base can only be zero or positive. Crypto losses cannot offset ryczałt income, and ryczałt income does not affect the crypto tax calculation.[^59][^60][^58]

***

## Part 8: 2024 vs 2025 Rule Comparison

| Topic | Tax Year 2024 | Tax Year 2025 |
|---|---|---|
| PIT-28 filing deadline | 30 April 2025 | **30 April 2026**[^33][^34] |
| Health insurance base (avg. wage Q4) | ~7,767 PLN | 8,549.18 PLN (↑~10%)[^28] |
| Health insurance Tier 1 (≤60k PLN) | ~419.46 PLN/month | **461.66 PLN/month**[^28][^31] |
| Health insurance Tier 2 (60k–300k PLN) | ~699.05 PLN/month | **769.43 PLN/month**[^28][^31] |
| Health insurance Tier 3 (>300k PLN) | ~1,258.29 PLN/month | **1,384.97 PLN/month**[^28][^31] |
| Preferential ZUS base | 1,272.60 PLN | 1,399.80 PLN[^26][^25] |
| VAT-UE SME cross-border exemption | Not available | Available from 1 Jan 2025[^61][^62] |
| KSeF | Voluntary | Mandatory from 1 Apr 2026[^54][^55] |
| JPK_EWP | On demand only | On demand (mandatory annual filing from 2027 for 2026 data)[^12] |
| Ryczałt eligibility limit | 2 mln EUR → ~9,218,200 PLN | 2 mln EUR → **~8,569,200 PLN**[^12] |

***

## Part 9: Summary Compliance Calendar (Tax Year 2025)

| Obligation | Frequency | Deadline | System/Form |
|---|---|---|---|
| Ryczałt income tax payment | Monthly | **20th of following month** (Dec → 20 Jan) | Mikrorachunek podatkowy, no form |
| ZUS social contributions (preferencyjne) | Monthly | 20th of following month | ZUS portal (PUE ZUS) |
| ZUS health insurance | Monthly | 20th of following month | ZUS portal (PUE ZUS) |
| VAT-UE intra-EU services report | Monthly (if EU clients) | **25th of following month** | e-Deklaracje: VAT-UE form |
| JPK_V7 (VAT-registered only) | Monthly | 25th of following month | e-Deklaracje: JPK_V7M |
| Annual PIT-28 return | Annual | **30 April 2026** | Twój e-PIT / e-Deklaracje |
| ZUS annual health insurance reconciliation (DRA/RCA) | Annual | With February ZUS payment | PUE ZUS |
| JPK_EWP (on demand in 2025; mandatory annually from 2027) | On demand | Per authority request | Electronic: JPK_EWP structure |

***

## Key Legal References

- **Ustawa z dnia 20 listopada 1998 r. o zryczałtowanym podatku dochodowym od niektórych przychodów osiąganych przez osoby fizyczne** (Dz.U. 1998 nr 144 poz. 930, as amended) — primary statute for ryczałt
  - Art. 6 ust. 1c — FX differences for ryczałt payers
  - Art. 12 ust. 1 pkt 2b — 12% rate for IT/software services
  - Art. 21 ust. 1 — monthly payment deadlines
- **Ustawa o podatku dochodowym od osób fizycznych (ustawa o PIT)** — Art. 14 ust. 1c (revenue recognition date), Art. 24c (FX differences)
- **Ustawa o podatku od towarów i usług (ustawa o VAT)** — Art. 28b (place of supply B2B), Art. 97 ust. 3 (VAT-UE registration), Art. 100 ust. 1 pkt 4 (VAT-UE reporting), Art. 113 ust. 1 and 9 (VAT exemption)

***

> **Disclaimer:** This guide reflects the state of Polish tax law as of March 2026 for tax year 2025. Tax rules change frequently; verify critical details with a certified tax advisor (*doradca podatkowy*) or official guidance from Ministerstwo Finansów at [podatki.gov.pl](https://www.podatki.gov.pl).

---

## References

1. [Kody PKD w IT a stawka ryczałtu 8,5% lub 12%](https://poradnikprzedsiebiorcy.pl/-kody-pkd-w-it-i-ich-wplyw-na-stawke-ryczaltu) - Czy wiesz, jak kody PKD w IT wpływają na stawkę ryczałtu a tym samym na wysokość podatku dochodowego...

2. [Ryczałt dla programisty IT – stawki, zasady, ograniczenia](https://br-progres.pl/blog/ryczalt-dla-programisty-o-czym-warto-pamietac/) - Czy ryczałt to dobra forma opodatkowania dla programisty? Sprawdź stawki 8,5% i 12%, wymagania, zale...

3. [Stawka ryczałtu 8,5%, czy 12% dla programistów, praca w IT jaki ...](https://www.fakturaxl.pl/stawka-ryczaltu-8-5-czy-12-dla-programistow-kod-pkd) - Branża IT może być objęta stawką ryczałtu w wysokości 8,5% i 12%. Dotyczy to niektórych kodów PKD wł...

4. [Ryczałt dla informatyków - 8,5% czy 12%?](https://www.jakplacicpodatki.pl/aktualnosci/ryczalt-dla-informatykow-85-czy-12-58) - Ryczałt dla informatyków: stawka 8,5% czy 12%?

5. [Kalkulator Ryczałtu IT - Oblicz Podatek 12% - Bookeper AI](https://www.bookeper.pl/kalkulatory/ryczalt) - Darmowy kalkulator ryczałtu dla programistów i branży IT. Oblicz podatek ryczałtowy 12% z odliczenie...

6. [Rozpoczęcie działalności opodatkowanej ryczałtem w ...](https://poradnikprzedsiebiorcy.pl/-rozpoczecie-dzialalnosci-opodatkowanej-ryczaltem-w-trakcie-roku-a-przekroczenie-limitu-obrotow) - Rozpoczęcie działalności opodatkowanej ryczałtem w trakcie roku podatkowego jest możliwe. Sprawdź, c...

7. [Ryczałt ewidencjonowany a miesięczna deklaracja](https://poradnikprzedsiebiorcy.pl/-ryczalt-ewidencjonowany-a-miesieczna-deklaracja) - W celu wygenerowania zaliczki na podatek należy przejść do zakładki: START » PODATKI » PODATEK DOCHO...

8. [podatki.gov.pl - Opodatkowanie ryczałtem od przychodów ...](https://www.podatki.gov.pl/podatki-firmowe/pit/informacje-podstawowe/co-jest-opodatkowane/opodatkowanie-ryczaltem-od-przychodow-ewidencjonowanych/) - Ryczałt wpłacasz w terminie: do 20. dnia każdego miesiąca za miesiąc poprzedni, a za grudzień – do 2...

9. [PIT-28. Do kiedy należy płacić zaliczki? - Pity | Rozlicz Twój e ...](https://www.pit.pl/aktualnosci/pit-28-do-kiedy-nalezy-placic-zaliczki-1010834) - W przypadku wyboru miesięcznych zaliczek podatnik zobowiązany jest do ich comiesięcznej zapłaty w te...

10. [Moment powstania przychodu w przypadku świadczenia ...](http://www.vademecumpodatnika.pl/artykul_narzedziowa,1366,0,23141,moment-powstania-przychodu-w-przypadku-swiadczenia-uslug.html) - 21 ust. 1 ustawy o zryczałtowanym podatku dochodowym, czyli w trakcie roku podatkowego - do dnia 20 ...

11. [JDG: Jaką formę opodatkowania wybrać w 2025 roku? - Siiamiwww.siiami.pl › blog › opodatkowanie-jdg](https://www.siiami.pl/blog/opodatkowanie-jdg/) - Jaką formę opodatkowania wybrać dla JDG w 2025? Poznaj dostępne formy opodatkowania i wybierz najlep...

12. [Ewidencja przychodów na ryczałcie - jak powinna wyglądać?](https://poradnikprzedsiebiorcy.pl/-ewidencja-przychodow-na-ryczalcie) - Ryczałt to dla niektórych firm bardzo opłacalna forma rozliczania się z urzędem. Dowiedz się z artyk...

13. [Ujmowanie przychodów w ewidencji ryczałtowca](http://www.podatekdochodowy.pl/artykul,1532,9640,ujmowanie-przychodow-w-ewidencji-ryczaltowca.html) - Podatek dochodowy - zawiera zagadnienia z zakresu: przychody podatkowe, koszty podatkowe, rozliczeni...

14. [JPK_EWP - wszystko co powinieneś wiedzieć!](https://poradnikprzedsiebiorcy.pl/-jpk-ewp-czyli-jednolity-plik-kontrolny-dla-ewidencji-przychodow) - do 31 grudnia 2025 roku - na żądanie organu podatnik składa plik JPK_EWP w zakresie określonym przez...

15. [Opodatkowanie w formie ryczałtu od przychodów ... - POLTAX](https://www.poltax.pl/baza_prawa_podatkowego/przedmiot_opodatkowania_ryczaltem_od_przychodow_ewidencjonowanych,376/opodatkowanie_w_formie_ryczaltu_od_przychodow_ewidencjonowanych,737) - Zgodnie z przepisami art. 14 ust 1c za datę powstania przychodu należnego uważa się z dzień wydania ...

16. [Stawki ryczałtu na przełomie roku](https://www.fakturaxl.pl/stawki-ryczaltu-na-przelomie-roku) - W przypadku przychodu ryczałtowego za grudzień 2020 roku, obowiązek podatkowy powstaje 31 grudnia 20...

17. [Faktura w walucie obcej a KSeF – jak przeliczać kursy ...](https://bizky.ai/blog/faktura-w-walucie-obcej-a-ksef-jak-poprawnie-przeliczac-kursy-walutowe-zgodnie-z-przepisami/) - Jak prawidłowo przeliczyć fakturę w walucie obcej w KSeF? Sprawdź zasady, kursy NBP i EBC oraz najcz...

18. [Kalkulator walutowy](https://fakturownia.pl/kursy-walut)

19. [Różnice kursowe w ryczałcie ewidencjonowanym](http://www.poradypodatkowe.pl/artykul,744,14292,roznice-kursowe-w-ryczalcie-ewidencjonowanym.html) - Porady Podatkowe to profesjonalny serwis o tematyce podatkowej. Zajmuje się zagadnieniami z podatku ...

20. [Różnice kursowe w ryczałcie ewidencjonowanym – www.kalkulatorypodatkowe.pl](http://www.kalkulatorypodatkowe.pl/artykul,1983,19185,roznice-kursowe-w-ryczalcie-ewidencjonowanym.html) - Kalkulatory podatkowe to zbiór bezpłatnych kalkulatorów, m.in.: odsetkowe, wyboru formy opodatkowani...

21. [Ryczałt: rachunek w euro a różnice kursowe - eGospodarka.pl](https://www.podatki.egospodarka.pl/61310,Ryczalt-rachunek-w-euro-a-roznice-kursowe,2,65,1.html) - Różnice kursowe przy ryczałcie ewidencjonowanym powstają, jeżeli wartość przychodu należnego na dzie...

22. [Obliczanie różnic kursowych, a ryczałt - Faktura XL](https://www.fakturaxl.pl/obliczanie-roznic-kursowych-ryczalt) - Podatnik, który wybrał ryczałt jako formę opodatkowania stosuje dla różnic kursowych taką samą stawk...

23. [ZUS przedsiębiorcy 2025: ile wynoszą składki i jak je policzyć?](https://direct.money.pl/artykuly/porady/zus-przedsiebiorcy-ile-wynosza-skladki-i-jak-je-policzyc) - Preferencyjny ZUS (24 mies.) — w 2025 r. podstawa to 1 399,80 zł (30% × 4 666 zł), stąd przykładowe ...

24. [Ulga na start, preferencyjna podstawa, działalność ...](https://www.zus.pl/-/ulga-na-start-preferencyjna-podstawa-dzialalnosc-nieewidencjonowana-jakie-sa-warunki-uprawnienia-i-skutk-1) - Przez kolejne 24 miesiące kalendarzowe będziesz opłacać składki od zadeklarowanej przez Ciebie kwoty...

25. [Preferencyjne składki ZUS 2025 r.](https://poradnikprzedsiebiorcy.pl/-preferencyjne-skladki-zus) - Podstawa wymiaru składek preferencyjnych wynosi 30% minimalnego wynagrodzenia za pracę. Ile wynoszą ...

26. [Preferencyjne składki ZUS 2025 – kto może z nich ...](https://bizky.ai/blog/preferencyjne-skladki-zus-2025-kto-moze-z-nich-skorzystac/) - Łączna wysokość preferencyjnych składek ZUS w 2025 roku wynosi zatem 442,90 zł miesięcznie, wliczają...

27. [Ulga na start a Mały ZUS – czym się od siebie różnią?](https://firmove.pl/aktualnosci/finanse/zus/ulga-na-start-a-maly-zus-czym-sie-od-siebie-roznia) - Dla porównania, w 2025 roku podstawa wymiaru wynosiła 1399,80 zł. Zwiększenie jej oznacza wyższe skł...

28. [Składka zdrowotna dla ryczałtu w 2025 r. Znamy nowe stawki](https://www.infakt.pl/blog/skladka-zdrowotna-dla-ryczaltu-w-2025-r/) - Wysokość składki zdrowotnej, którą opłacają ryczałtowcy, zależy od osiągniętego rocznego przychodu o...

29. [Składka zdrowotna - ryczałt 2025. Ile zapłaci przedsiębiorca?](https://mk.rp.pl/blog/skladka-zdrowotna-ryczalt-2025-ile-zaplaci-przedsiebiorca/) - Temat składki zdrowotnej nie schodzi z ust przedsiębiorców, szczególnie w kontekście ostatnio forsow...

30. [Składka zdrowotna ryczałt 2025 - jak ją wyliczyć?](https://poradnikprzedsiebiorcy.pl/-wyliczenie-skladki-zdrowotnej-u-ryczaltowca) - Jak wygląda wyliczenie składki zdrowotnej u ryczałtowca w 2025 roku? Czy wysokość składki zależy wył...

31. [Składka zdrowotna 2026 – ryczałt. Nowe stawki i progi [Tabela]](https://symfonia.pl/blog/rozwoj-firmy/jdg/skladka-zdrowotna-2025-ryczalt/) - Składka zdrowotna na ryczałcie 2025 – sprawdź stawki, progi przychodów i planowane zmiany w opłacani...

32. [Urząd Skarbowy i ZUS – terminy płatności składek i podatków](https://wste.pl/urzad-skarbowy-i-zus-terminy-platnosci-skladek-i-podatkow/) - Termin płatności zaliczek na PIT i CIT to 20. dzień miesiąca za miesiąc poprzedni, a VAT – 25. dzień...

33. [PIT 28 2025/2026 ryczałt - poradnik podatkowy](https://www.e-pity.pl/pit-28/) - Zeznanie roczne PIT-28 składasz w terminie od 15 lutego do 30 kwietnia 2026 roku. Złożenie deklaracj...

34. [PIT 28 2025 / 2026 - jak rozliczyć ryczałt i najem - ulgi i druk](https://www.pitax.pl/rozliczenie-pit-28/) - Korektę PIT-28 za 2025 rok można złożyć do 31 grudnia 2031 roku. Należy złożyć poprawiony formularz ...

35. [Kto i kiedy składa PIT-28 w 2026 roku? Podpowiadamy!](https://firmove.pl/aktualnosci/finanse/podatki/kto-i-kiedy-sklada-pit-28-podpowiadamy) - PIT-28 za rok podatkowy trwający od 1 stycznia do 31 grudnia 2025 roku należy złożyć w okresie od 15...

36. [Rozliczenie przychodów opodatkowanych ryczałtem](https://www.podatki.gov.pl/podatki-firmowe/pit/informacje-podstawowe/co-jest-opodatkowane/rozliczenie-przychodow-opodatkowanych-ryczaltem/) - Zeznanie składasz w terminie od 15 lutego do 30 kwietnia roku następującego po roku podatkowym. Uwag...

37. [ePIT 28 obowiązujący w 2025 roku](https://twoj-epit.pl/pit-28-obowiazujacy) - PIT 28 za rok 2025 należy złożyć do 31 stycznia 2026 roku. Jest to standardowy termin, który dotyczy...

38. [podatki.gov.pl - PIT-28 za 2025 rok](https://www.podatki.gov.pl/twoj-e-pit/pit-28-za-2025-rok/) - W tej części zeznania wykazuje się przychody oraz ryczałt należny z prowadzonej działalności gospoda...

39. [Ryczałt 2025 – komu się opłaca i jak rozliczać?](https://amavat.pl/ryczalt-co-musze-wiedziec/) - W 2025 roku roczny limit uprawniający do opodatkowania ryczałtem wynosi 8 569 200 zł, co odpowiada 2...

40. [Utrata zwolnienia z VAT w 2025 r. – możliwy powrót bez rocznej ...](https://rachunkowosc.com.pl/utrata-zwolnienia-z-vat-w-2025-r-mozliwy-powrot-bez-rocznej-karencji) - Rachunkowość - Pismo Stowarzyszenia Księgowych w Polsce

41. [Jak zapłacić ryczałt do US?](https://firmove.pl/aktualnosci/finanse/podatki/jak-zaplacic-ryczalt-do-us) - Co do zasady następuje to w terminie do 20. dnia miesiąca za miesiąc poprzedni lub do 20. dnia miesi...

42. [Zwolnienie z VAT a JPK_V7 | JPK.info.pljpk.info.pl › jpk-v7 › zwolnienie-z-vat-a-plik-jpk-v7m-v7k](https://jpk.info.pl/jpk-v7/zwolnienie-z-vat-a-plik-jpk-v7m-v7k/) - Podatnicy zwolnieni z VAT ze względu na obrót (do 200.000 zł rocznie) nie muszą przygotowywać plików...

43. [Obowiązki VAT czynnego podatnika – poradnik 2025](https://amavat.pl/obowiazki-vat-czynnego-podatnika-poradnik-2025/) - Poznaj wszystkie obowiązki VAT w 2025 roku: ewidencje, faktury, JPK, VAT-UE i KSeF. Praktyczny porad...

44. [Zwolnienie podmiotowe od podatku VAT - podatki.gov.pl](https://www.podatki.gov.pl/podatki-firmowe/vat/poradniki-i-informatory/zwolnienie-podmiotowe-od-podatku-vat/) - Portal podatki.gov.pl

45. [JPK_V7 a zwolnienie z VAT - co z obowiązkiem wysyłki?](https://poradnikprzedsiebiorcy.pl/-jpk-vat-a-zwolnienie-z-vat) - Czy korzystając ze zwolnienia z VAT należy składać JPK_V7? Sprawdź, czy nievatowcy mają obowiązek w ...

46. [Zwolnienie podmiotowe i eksport usług - KIP](https://izbapodatkowa.pl/baza-wiedzy/zwolnienie-podmiotowe-i-eksport-uslug/) - Informacje podsumowujące należy składać wtedy, gdy przedmiotem świadczenia są usługi opodatkowane we...

47. [Eksport usług do UE przez przedsiębiorców zwolnionych z ...](https://www.nex.katowice.pl/post/eksport-us%C5%82ug-do-ue-przez-przedsi%C4%99biorc%C3%B3w-zwolnionych-z-vat) - Polski przedsiębiorca, świadczący usługi na rzecz kontrahentów z UE, ma obowiązek składania informac...

48. [VAT przy eksporcie usług digital/IT/marketing z Polski do ...](https://aroksds.com/faq/vat-przy-eksporcie-uslug-digital-it-marketing-z-polski-do-ue-i-ukrainy-b2b-b2c/) - W typowych usługach B2B (firma-dla-firmy) miejscem opodatkowania jest kraj nabywcy (art. 28b ustawy ...

49. [Blog » Jak wystawić fakturę za usługi dla zagranicznego ...](https://solidnaksiegowa.com/jak-wystawic-fakture-za-uslugi-marketingowe-dla-zagranicznego-kontrahenta/) - Pamiętaj też, że przy usługach dla firm z UE często musisz składać dodatkową informację podsumowując...

50. [Obowiązek składania informacji podsumowujących VAT UE](https://biz.legalis.pl/obowiazek-skladania-informacji-podsumowujacych-vat-ue/) - Podatnik świadczy usługi na rzecz zagranicznego kontrahenta z UE, w związku z czym zobowiązany był d...

51. [VAT UE – co powinieneś wiedzieć? | Blog](https://solidnaksiegowa.com/vat-ue-co-powinienes-wiedziec/) - Najważniejszym z nich jest składanie informacji podsumowujących VAT-UE. W informacji tej wykazuje si...

52. [Rozliczanie VAT w sprzedaży międzynarodowej 2025](https://amavat.pl/rozliczanie-vat-a-sprzedaz-miedzynarodowa-jak-to-ugryzc/) - Praktyczny przewodnik po rozliczaniu VAT w sprzedaży międzynarodowej. WDT, WSTO, OSS, eksport, impor...

53. [Usługi programistyczne dla zagranicznych kontrahentów](https://poradnikprzedsiebiorcy.pl/-uslugi-programistyczne-dla-zagranicznych-kontrahentow-opodatkowanie) - Dokonując sprzedaży usług na rzecz unijnego kontrahenta, należy złożyć we właściwym urzędzie skarbow...

54. [KSeF od kiedy obowiązkowy? Terminy 2026 zatwierdzone ...](https://altab.pl/baza-wiedzy/ksef-od-kiedy-obowiazkowy/) - 1 kwietnia 2026 r. – obowiązek obejmuje wszystkie pozostałe przedsiębiorstwa (mikro, małe i średnie ...

55. [Od kiedy KSeF dla małych firm? - Pity | Rozlicz Twój e ... - PIT.pl](https://www.pit.pl/aktualnosci/od-kiedy-ksef-dla-malych-firm-1011769) - Oznacza to, że mniejsze firmy będą zobowiązane do wdrożenia KSeF najpóźniej do 1 kwietnia 2026 roku....

56. [KSeF dla małych firm i JDG – od kiedy i jak się przygotować?](https://www.comarch.pl/erp/blog/ksef-dla-malych-firm-i-jdg-od-kiedy-i-jak-sie-przygotowac/) - Kiedy KSeF stanie się obowiązkowy? · 1 lutego 2026 r. – dla przedsiębiorców, których wartość sprzeda...

57. [KSeF dla JDG od 2026. Wszystko, co musi wiedzieć ...](https://www.prawo-pracy.pl/ksef-dla-jdg-od-2026-wszystko-co-musi-wiedziec-wlasciciel-mikro-i-malej-firmy-p-2839.html) - od 1 lutego 2026 – KSeF jest obligatoryjny dla przedsiębiorców, których łączna wartość sprzedaży bru...

58. [Jak rozliczać się z kryptowalut w 2025 roku?](https://www.ifirma.pl/blog/jak-rozliczac-sie-z-kryptowalut-w-2025-roku/) - Kryptowaluty a rozliczenie podatkowe w 2025! Od darowizn po faktury - wszystko co musisz wiedzieć o ...

59. [Podatek od kryptowalut w Polsce 2025 – zasady i rozliczenie](https://polska-ksiegowosc.pl/2025/09/podatek-od-kryptowalut-w-polsce-2025-zasady-i-rozliczenie/) - Podatek od kryptowalut w Polsce wynosi 19% – sprawdź zasady rozliczenia, koszty do odliczenia i mome...

60. [Podatek od kryptowalut - jak rozliczyć PIT od krypto w 2025 ...](https://www.e-pity.pl/podatek-pit-od-kryptowalut/) - Podatnicy operujący kryptowalutami są zobowiązani rozliczyć w deklaracji PIT 2025/2006 przychody, ko...

61. [Zwolnienie z VAT dla małych firm w UE. Procedura SME od 2025| ifirma.pl](https://www.ifirma.pl/blog/zwolnienie-z-vat-dla-malych-firm-w-ue-kogo-dotyczy-procedura-sme-od-stycznia-2025/) - Procedura SME to szansa na uproszczenie rozliczeń podatkowych w UE! Firmy nie muszą rejestrować VAT ...

62. [Zwolnienie podmiotowe w podatku VAT – zmiany](https://es-doradztwo.pl/zwolnienie-podmiotowe-w-podatku-vat-zmiany-procedura-sme/) - informacja podsumowująca i jej znaczenie dla zastosowania stawki 0 % podatku VAT;; numer VAT UE kont...

