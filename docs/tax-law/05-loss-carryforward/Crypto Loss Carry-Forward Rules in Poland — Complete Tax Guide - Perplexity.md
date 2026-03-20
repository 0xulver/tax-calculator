# Crypto Loss Carry-Forward Rules in Poland — Complete Tax Guide

## Executive Summary

Polish tax law contains a **critical distinction** that catches most traders by surprise: crypto does **not** use the standard loss carry-forward mechanism under Art. 9 ust. 3 PIT. Instead, it uses a separate cost-surplus ("nadwyżka kosztów") rollover under Art. 22 ust. 16 PIT. The practical implications are significant and largely favorable — there is **no time limit** on carrying forward crypto cost surpluses, and the full amount can generally be deducted in the next year (not just 50%). Cross-border situations add another layer of complexity, but a binding 2024 court ruling establishes that pre-residency purchase costs can be used in Polish filings.

***

## Part 1: The Fundamental Legal Framework

### The Standard Loss Rule (Art. 9 ust. 3 PIT) Does Not Apply to Crypto

Art. 9 ust. 3 of the Personal Income Tax Act (ustawa o PIT) is the general loss carry-forward rule for most income sources. It allows taxpayers to reduce income from the same source by a loss from prior years, subject to a 5-year window and either the **50% annual cap** or a **one-time deduction up to 5,000,000 PLN** (the choice between these two methods was introduced in 2019).[^1][^2]

However, Art. 9 ust. 3a pkt 2 PIT explicitly **excludes virtual currencies** from this mechanism. The phrase "przepis ust. 3 nie ma zastosowania do strat z odpłatnego zbycia walut wirtualnych" (the provision of paragraph 3 does not apply to losses from the disposal of virtual currencies) means that neither the 50% rule nor the 5 million PLN one-shot rule applies to crypto.[^3][^4]

This exclusion is not a disadvantage — it is actually more flexible, because the alternative mechanism under Art. 22 ust. 16 PIT has **no time cap**.

### The Actual Rule: Art. 22 ust. 16 PIT — Cost Surplus ("Nadwyżka Kosztów")

The operative provision for crypto losses is Art. 22 ust. 16 PIT:[^5][^6]

> *Nadwyżka kosztów uzyskania przychodów, o których mowa w ust. 14, nad przychodami z odpłatnego zbycia waluty wirtualnej uzyskanymi w roku podatkowym powiększa koszty uzyskania przychodów z tytułu odpłatnego zbycia waluty wirtualnej poniesione w następnym roku podatkowym.*

In plain terms: when deductible crypto costs exceed crypto revenues in a tax year, the surplus is carried into the **next year as additional costs** — effectively reducing the taxable base for that year. If the surplus still exceeds the following year's revenues, it rolls again to the year after, and so on.

**Critically, the Director of the National Revenue Information (Dyrektor KIS) confirmed in 2022 (interpretations 0113-KDIPT2-3.4011.249.2022.1.SJ and 0113-KDIPT2-1.4011.1269.2021.2.AP) that this roll-forward has no time limitation** — the costs may be carried indefinitely until they are fully matched against revenues from crypto sales.[^7]

### What Counts as Deductible Crypto Costs

Under Art. 22 ust. 14 PIT, deductible costs include:[^8][^7]

- Documented purchase price of virtual currencies (fiat-to-crypto acquisitions)
- Exchange commissions and transaction fees paid to intermediaries
- Withdrawal and transfer fees paid to exchanges covered under AML regulations

The following are **not** deductible:[^9][^8]
- Mining equipment, graphics cards, electricity
- Costs of crypto-to-crypto swaps (these are tax-neutral transactions, so neither revenue nor costs arise)
- Loan interest used to fund crypto purchases
- Any costs related to issuing tokens

***

## Part 2: Comparison — Art. 9 ust. 3 vs. Art. 22 ust. 16

| Feature | Art. 9 ust. 3 PIT (general losses) | Art. 22 ust. 16 PIT (crypto cost surplus) |
|---|---|---|
| Applies to crypto? | **No** (excluded by Art. 9 ust. 3a pkt 2) | **Yes** (exclusive mechanism) |
| Time limit for carry-forward | 5 years | **None** (confirmed by KIS) |
| Annual deduction cap | 50% of loss OR 5M PLN one-shot | **No cap** — full surplus deducted each year |
| Called legally | "Strata podatkowa" (tax loss) | "Nadwyżka kosztów" (cost surplus) |
| Can offset other income sources? | Only same income source | Only crypto revenues |
| Must appear in original return? | Yes | Yes |

[^2][^3][^7]

***

## Part 3: Siloing — What Crypto Losses Cannot Offset

Art. 30b ust. 5d PIT is explicit: crypto income **cannot be combined** with other income taxed under Art. 30b (stocks, bonds, derivatives) or under Art. 27 (salary/progressive scale) or Art. 30c (flat-rate business tax / liniowy).[^10][^11]

The consequence is categorical:
- A 2025 crypto loss **cannot** offset gains from stocks or bonds reported elsewhere on PIT-38[^12]
- It **cannot** reduce JDG (sole proprietorship) income, whether reported under ryczałt, liniowy, or the general scale[^12][^9]
- It **cannot** reduce rental income, employment income, or any other source

The crypto cost surplus (pole 38 of PIT-38) applies **exclusively** to future revenues from the disposal of virtual currencies.[^13][^12]

***

## Part 4: PIT-38 Form — Section E (Crypto)

Crypto transactions are declared in **Section E** of PIT-38 under the heading *"Dochód/koszty — art. 30b ust. 1a ustawy"* (from the 2023 tax year onward, dedicated fields are used):[^14][^15]

| Field | What to Enter |
|---|---|
| **Pole 34** | Revenues from crypto disposals in the current year (fiat received, market value of goods/services paid for with crypto) |
| **Pole 35** | Costs incurred in the current year (purchase prices of crypto sold + this year's commissions) |
| **Pole 36** | Cost surplus carried forward from **prior years** (i.e., the "pole 38" figure from last year's PIT-38) |
| **Pole 37** | Net income (34 − 35 − 36, if positive → taxable base at 19%) |
| **Pole 38** | Net cost surplus to carry to next year (when 35 + 36 > 34, i.e., total costs exceed revenues; this is the "new" nadwyżka kosztów) |

[^16][^15][^9]

**Important:** PIT-38 must be filed **even in years when only costs are incurred and no crypto sale takes place**. Some KIS interpretations suggest that failure to file PIT-38 in a cost-only year may forfeit the right to carry forward those costs. To be safe, file PIT-38 every year any crypto is purchased, sold, or exchanged.[^17][^18][^19]

### Declaring the 2025 Loss (15,000 PLN Surplus)

For the 2025 PIT-38:
- Pole 34: revenues from 2025 sales
- Pole 35: 2025 purchase costs and fees
- If costs exceed revenues: Pole 38 = 15,000 PLN (or the calculated surplus)

For the **2026 PIT-38**:
- Pole 36: 15,000 PLN (prior year cost surplus)
- The entire 15,000 PLN is deductible against 2026 crypto revenues — no 50% cap applies
- If 2026 revenues are less than 15,000 PLN, the remainder rolls again to pole 38 and carries into 2027

***

## Part 5: Year-by-Year Practical Example

| Year | Revenues (PLN) | Costs (PLN) | Prior Surplus (Pole 36) | Taxable Income | New Surplus (Pole 38) |
|---|---|---|---|---|---|
| 2025 | 10,000 | 25,000 | 0 | 0 | **15,000** |
| 2026 | 60,000 | 10,000 | 15,000 | 35,000 | 0 |
| 2027 | 5,000 | 3,000 | 0 | 2,000 | 0 |

In 2026: taxable income = 60,000 − 10,000 − 15,000 = **35,000 PLN** → tax = 35,000 × 19% = **6,650 PLN**
Without the surplus, tax would have been: (60,000 − 10,000) × 19% = **9,500 PLN**. Savings: **2,850 PLN**.

*Example variant: if 2026 revenues were only 8,000 PLN and costs were 1,000 PLN:*
8,000 − 1,000 − 15,000 = −8,000 → no tax, pole 38 = 8,000 PLN carried to 2027.

***

## Part 6: Cross-Border — Sweden-to-Poland Transition

### Tax Residency Framework

Poland taxes worldwide income of its tax residents (nieograniczony obowiązek podatkowy). Sweden does the same. The Poland–Sweden Double Taxation Convention (DTC) signed 19 November 2004, in force from 1 January 2006, determines which country has taxing rights.[^20][^21]

Under **Art. 13(4)/(5) of the Poland–Sweden DTC**, gains from the disposal of "other property" (which includes crypto as it is neither immovable property nor shares with real estate nexus) are taxable **only in the state of which the seller is a resident** at the time of disposal. This means:[^21]

- Crypto sold **while Swedish resident**: taxed only in Sweden (30% Swedish CGT)[^22]
- Crypto sold **while Polish resident**: taxed only in Poland (19% flat PIT-38)

The DTC also includes a **10-year lookback rule** (Art. 13(5) Poland-Sweden DTC): gains from property sold within 10 years of leaving Sweden may also be taxable in Sweden, but this primarily applies to shares; for generic "other property" the standard rule (residence at time of sale) governs.[^21]

### Years 2020–2022 (Swedish Residency)

For those years, the taxpayer was a Swedish resident. The obligation to pay tax in Poland did not exist. Accordingly:[^12][^21]
- No PIT-38 was required in Poland for 2020–2022
- No Polish crypto loss was generated in those years
- The ~461 PLN Swedish loss (2020), the ~31,000 PLN Swedish gain (2021), and the ~150,000 PLN Swedish gain (2022) are Swedish tax matters, not Polish

### The Key 2024 Court Ruling: WSA Warsaw III SA/Wa 1290/24

The Warsaw Administrative Court (WSA) issued a binding judgment on **29 August 2024** (III SA/Wa 1290/24) addressing exactly this situation — a taxpayer who changed residency (from the UK to Poland) and then sold crypto as a Polish resident, when the purchase costs were incurred as a non-resident.[^23][^24]

**The court held:**
1. Costs of acquiring crypto **before becoming a Polish resident can be included in PIT-38** — provided they have **not already been claimed as tax costs in the prior country of residence**
2. Only **cash purchases** (fiat → crypto) are deductible as costs in PIT-38. The court refused crypto-to-crypto swap costs, even if those transactions were taxed in the UK, citing the absence of a legal basis in Polish PIT law for such a deduction[^23]
3. Once you sell crypto **as a Polish resident**, the entire gain is subject to Polish PIT, regardless of where the crypto was acquired[^23]

**Application to the Sweden scenario:**
- If Swedish crypto purchases were made with fiat (SEK/EUR/PLN) and were NOT claimed as costs in Sweden for those specific assets, those purchase prices may be included in Polish PIT-38 as costs
- Crypto-to-crypto swap costs (e.g., BTC → ETH → sold for PLN) cannot be traced through as deductible costs in Poland
- Gains reported and **taxes paid** in Sweden reduce Polish tax liability via Art. 30b ust. 5e PIT (credit method)[^25][^26]

### Tax Residency Date: Becoming Polish Resident ~2023

Polish tax residency is established when an individual has their **center of vital interests** in Poland or spends more than 183 days per calendar year in Poland. The exact date matters:[^27]

- If Polish residency began **1 January 2023**: all of 2023 income is taxable in Poland on PIT-38
- If residency changed **mid-2023** (e.g., from June 2023): split-year treatment applies. Income from the date of becoming resident onward is taxable in Poland. Losses/surpluses from the Polish-resident period of 2023 onward carry forward

The 2023 net gain of ~146,000 PLN (assuming full-year Polish residency) would have been declared on PIT-38 for 2023 and taxed at 19%. Cost surplus from that year (if any) would carry forward.

***

## Part 7: Korekta PIT-38 — Corrected Returns and Statute of Limitations

### Filing Corrections

If a prior-year PIT-38 was incorrect (e.g., costs understated, transactions omitted, or a surplus not declared), a correction (korekta) can be filed. A korekta:
- Can add previously omitted costs, increasing the nadwyżka kosztów in a prior year
- Allows the corrected surplus to then be carried forward to subsequent years
- Requires czynny żal (voluntary disclosure) if the original return was unfiled, to avoid penalties[^28][^29]

### Statute of Limitations

Under Art. 70 of the Ordynacja Podatkowa, tax obligations expire after **5 years from the end of the calendar year in which the tax payment deadline passed**. The NSA (Supreme Administrative Court) upheld in a 2017 plenary ruling (II FPS 3/17) that the same 5-year period applies to verifying losses.[^30][^31][^32][^33]

| Tax Year | PIT-38 Deadline | Statute Expires |
|---|---|---|
| 2020 | 30 April 2021 | **31 December 2026** |
| 2021 | 30 April 2022 | 31 December 2027 |
| 2022 | 30 April 2023 | 31 December 2028 |
| 2023 | 30 April 2024 | 31 December 2029 |
| 2024 | 30 April 2025 | 31 December 2030 |
| 2025 | 30 April 2026 | 31 December 2031 |

[^34][^31]

**The 2020 window closes 31 December 2026.** If a correction revealing a cost surplus for 2020 is needed, it must be filed before year-end 2026.

### Can a Korekta Establish a New Cost Surplus?

Yes. If a corrected PIT-38 for a prior year shows that costs exceeded revenues (or that costs were omitted), the established surplus can be carried forward into subsequent years — appearing in pole 36 of the next year's return. The corrected year's pole 38 value propagates forward.[^34][^9]

***

## Part 8: Answering Each Question Directly

### Q1: Which loss rule applies — 50% annual limit or 5M PLN one-shot?

**Neither applies to crypto.** The 50% annual cap and the 5M PLN one-shot option under Art. 9 ust. 3 PIT are explicitly inapplicable to virtual currencies by Art. 9 ust. 3a pkt 2 PIT. The crypto-specific mechanism (Art. 22 ust. 16) has **no annual percentage cap** — the full surplus deducts each year until exhausted.[^3][^7]

### Q2: Do crypto losses offset stocks/bonds on PIT-38?

**No.** Art. 30b ust. 5d PIT prohibits combining crypto income with any other Art. 30b income (stocks, bonds, derivatives). They are separate sub-sources within PIT-38, and crypto cost surplus cannot cross into the stock/bond section.[^11][^10]

### Q3: Can crypto losses offset JDG/business income?

**No.** Crypto income is in the "kapitały pieniężne" source and cannot reduce income from działalność gospodarcza (whether ryczałt, liniowy, or skala). These are entirely separate income sources.[^9][^12]

### Q4: If a 2025 PIT-38 shows a loss, what appears on the form?

The 2025 PIT-38 (for income year 2025) will show in **Pole 38**: the amount by which total 2025 crypto costs exceeded 2025 crypto revenues (e.g., 15,000 PLN). Tax due will be zero. The return must still be filed.[^19][^16]

### Q5: Can Swedish-period losses (2020–2022) carry forward to Poland?

**Not directly as "losses."** There was no Polish tax obligation during those years, so no Polish strata or nadwyżka kosztów was generated. However, the **purchase costs** from those years (for crypto still held and later sold as a Polish resident) can appear in Polish PIT-38 as costs — provided they were not already claimed as tax costs in Sweden (per WSA III SA/Wa 1290/24).[^3][^21][^23]

### Q6: Can Swedish losses and Polish losses both be claimed?

**No double-counting allowed.** The rule from WSA III SA/Wa 1290/24 is clear: pre-residency purchase costs are only admissible in Polish PIT-38 **if they were not already deducted as tax costs in Sweden**. If a Swedish tax return treated those purchases as deductible costs generating a recognized loss, those same costs cannot also appear in Polish PIT-38.[^23]

### Q7: Does mid-2023 Polish residency affect loss carry-forward?

From the **date of becoming a Polish tax resident**, all crypto disposals trigger Polish PIT-38 reporting. Cost surpluses generated from the Polish-resident period (including the second half of 2023 if residency began then) carry forward indefinitely. The exact residency start date needs to be established (possibly via certificate of residency/tax registration date) for accuracy.[^21]

### Q8: How much of the 15,000 PLN 2025 loss can be deducted in 2026?

**The full 15,000 PLN in 2026**, assuming 2026 crypto revenues are at least that amount. Under Art. 22 ust. 16, there is no 50% cap — the entire cost surplus reduces the 2026 taxable base. If 2026 revenues are less than 15,000 PLN, the remainder rolls to 2027 without limit.[^1][^7]

### Q9: Must the loss be declared in the year of the loss?

**Yes — the loss year's PIT-38 must be filed.** The cost surplus must appear in pole 38 of the year in which it arises. It cannot be claimed retroactively in a later year without having first declared it in the year of the surplus. If the original PIT-38 was not filed, a korekta (or late filing) is needed to establish the surplus, subject to the 5-year statute of limitations.[^18][^35]

### Q10: Can a korekta PIT-38 revealing a prior-year loss be carried forward?

**Yes.** A corrected PIT-38 that establishes (or increases) the cost surplus in a prior year can be used as the basis for carrying that surplus forward. The corrected pole 38 figure propagates into pole 36 of the subsequent year's PIT-38.[^29][^9]

### Q11: What documentation is needed?

- **Exchange transaction histories**: complete CSV/Excel exports from all exchanges (Binance, Coinbase, Kraken, etc.) covering every purchase, sale, and fee
- **Purchase receipts**: bank transfer records or exchange confirmation emails showing the fiat amount spent to acquire crypto
- **Commission documentation**: fee schedules or transaction records showing commissions paid to exchange operators
- **Foreign tax records**: Swedish tax returns (Inkomstdeklaration) showing which costs were claimed there, if pre-residency costs are to be included in PIT-38 (per WSA III SA/Wa 1290/24)
- **Residency documentation**: Polish certificate of residency, Urząd Skarbowy registration date, or other proof of the date Polish tax residency commenced
- **Prior PIT-38 copies**: the filed returns showing pole 38 values, which substantiate pole 36 entries in subsequent years

[^36][^28][^16]

### Q12: Must the original loss-year PIT-38 be filed (or corrected) before carry-forward?

**Yes.** The cost surplus can only be carried forward if it was declared in the PIT-38 for the year it arose. If that PIT-38 was unfiled or incorrect, filing/correcting it is a prerequisite. For years where PIT-38 was simply not filed (e.g., cost-only years), a late filing can still be made within the 5-year limitation window — but czynny żal should be filed simultaneously to avoid penalties.[^29][^34]

***

## Part 9: The Specific Tax Situation Year-by-Year

| Year | Residency | Polish PIT-38 Obligation | Outcome |
|---|---|---|---|
| 2020 | Sweden | None (Swedish resident; loss ~461 PLN in Sweden) | No Polish loss; Swedish matter only |
| 2021 | Sweden | None (Swedish resident; gain ~31,000 PLN) | No Polish tax; Swedish CGT 30% applies |
| 2022 | Sweden (partial → Poland?) | Depends on exact residency date | If Swedish all year: no Polish PIT; if partial: consult DTA |
| 2023 | Poland (full year assumed) | **Yes** — gain ~146,000 PLN → PIT-38 → 19% tax ~27,740 PLN | Pre-residency purchase costs may be includable (WSA III SA/Wa 1290/24) |
| 2024 | Poland | **Yes** — gain ~3,000 PLN → tax ~570 PLN | Standard PIT-38 |
| 2025 | Poland | **Yes** — loss ~15,000 PLN → pole 38 = 15,000 PLN; zero tax | Carry to 2026 |
| 2026–2030 | Poland | **Yes** — pole 36 = 15,000 PLN in 2026 | Full deduction from first year of gains |

[^12][^21][^23]

***

## Part 10: Practical Steps and Action Items

1. **For 2025**: File PIT-38 by 30 April 2026, declaring the cost surplus in pole 38 (e.g., 15,000 PLN). No tax payable.

2. **For 2026 and beyond**: Enter the prior-year surplus in pole 36 of each subsequent PIT-38, reducing the taxable base. Track the rolling balance.

3. **Regarding Swedish-period purchase costs**: Obtain Swedish tax records (Inkomstdeklaration 2020–2022) to identify which crypto acquisitions were NOT claimed as tax costs in Sweden. Those fiat-to-crypto purchase costs can potentially be entered in PIT-38 as deductible costs for the year of sale, per WSA III SA/Wa 1290/24.

4. **Check 2020 statute deadline**: If a corrected or late PIT-38 for 2020 is considered, it must be filed before **31 December 2026** (5-year limitation from the end of 2021, when the 2020 tax payment deadline of 30 April 2021 passed).

5. **Consult a doradca podatkowy**: The cross-border issues (pre-residency costs, Sweden-to-Poland transition, applying the WSA judgment) carry enough ambiguity that professional advice with an individual tax ruling (interpretacja indywidualna) from KIS is strongly advisable before relying on large deductions.

6. **Obtain individual tax ruling (interpretacja indywidualna)**: Given the novel WSA III SA/Wa 1290/24 ruling, a taxpayer-specific interpretacja from KIS provides binding protection against reassessment. The fee is 40 PLN per scenario.

***

## Key Legal References

| Provision | Content |
|---|---|
| Art. 9 ust. 3 PIT | General 5-year loss carry-forward (50% cap or 5M PLN one-shot) — does NOT apply to crypto |
| Art. 9 ust. 3a pkt 2 PIT | Explicit exclusion of crypto from Art. 9 ust. 3 carry-forward |
| Art. 22 ust. 14 PIT | Definition of deductible crypto costs |
| Art. 22 ust. 15 PIT | Costs deductible in year incurred (with exception per ust. 16) |
| Art. 22 ust. 16 PIT | Cost surplus carries into next year (indefinitely per KIS) |
| Art. 30b ust. 1a PIT | 19% flat tax on crypto disposal income |
| Art. 30b ust. 1b PIT | Income = revenues minus costs under Art. 22 ust. 14-16 |
| Art. 30b ust. 5d PIT | Crypto income not combined with other capital income |
| Art. 30b ust. 5e PIT | Foreign crypto tax credit method for Polish residents |
| Art. 30b ust. 6a PIT | Obligation to declare costs in PIT-38 even without revenues |
| KIS interpretation 0113-KDIPT2-3.4011.249.2022.1.SJ | No time limit on rolling cost surplus |
| WSA Warsaw III SA/Wa 1290/24 (29 Aug 2024) | Pre-residency fiat-to-crypto purchase costs admissible in Polish PIT-38 |
| Poland–Sweden DTA (19 Nov 2004) Art. 13(5) | "Other property" gains taxable only in state of residence at time of sale |

---

## References

1. [podatki.gov.pl - Odliczenie straty PIT](https://www.podatki.gov.pl/ulgi-i-odliczenia/odliczenie-straty-pit/) - Portal podatki.gov.pl

2. [Jednorazowe rozliczanie straty w podatku dochodowym PIT i CIT](https://abak.com.pl/jednorazowe-rozliczanie-straty-w-podatku-dochodowym-pit-i-cit/)

3. [Strata z handlu wirtualną walutą - jak rozliczyć?](https://poradnikprzedsiebiorcy.pl/-czy-strata-z-handlu-wirtualna-waluta-musi-byc-wykazana-w-deklaracji-rocznej) - Na wstępie zaznaczmy, że przychody z odpłatnego zbycia wirtualnej waluty zaliczane są do źródła przy...

4. [Rozliczenie straty ze sprzedaży kryptowalut - Agata Błaszczyk](https://www.blogopodatkach.pl/rozliczenie-straty-ze-sprzedazy-kryptowalut-czy-bedzie-mozliwe-w-mysl-nowej-regulacji-prawnej/) - Planowane zmiany regulacji prawnej w zakresie kryptowalut wprowadzają nieco inny sposób rozliczania ...

5. [0113-KDIPT2-3.4011.290.2020.1.SJ | Interpretacje podatkowe MF](https://anylawyer.com/interpretacje-podatkowe/mozliwosc-zaliczenia-do-kosztow-uzyskania-przychodu-wydatkow-na-nabycie-waluty-wirtualnej--0113-kdipt2-3-4011-290-2020-1-sj) - Na podstawie art. 22 ust. 16 ustawy o podatku dochodowym od osób fizycznych, nadwyżka kosztów nabyci...

6. [0113-KDIPT2-1.4011.1269.2021.2.AP | Interpretacje podatkowe MF](https://anylawyer.com/interpretacje-podatkowe/transakcje-zwiazane-z-obrotem-walutami-wirtualnymi--0113-kdipt2-1-4011-1269-2021-2-ap) - 1. Podatnik, będący polskim rezydentem, prowadzi transakcje kupna/sprzedaży kryptowalut oraz emisji ...

7. [Korzystne interpretacje Dyrektora KIS dotyczące obrotu ...](https://bieluk.pl/blog/2022/07/21/korzystne-interpretacje-dyrektora-kis-dotyczace-obrotu-walutami-wirtualnymi/) - W ostatnim czasie Dyrektor Krajowej Informacji Skarbowej wydał parę korzystnych interpretacji indywi...

8. [Cryptoassets in Poland: tax traps, reporting duties and ...](https://bpcc.org.pl/cryptoassets-in-poland-tax-traps-reporting-duties-and-business-risks/) - Polish tax rules also create serious obstacles for companies aiming to issue their own cryptoassets....

9. [Jak samodzielnie rozliczyć podatek od kryptowalut w 2025?](https://kancelariamw.pl/jak-rozliczyc-podatek-od-kryptowalut/) - ... nadwyżkę kosztów nad przychodami to w polu 38 wpisujesz tę nadwyżkę jako stratę. W zeznaniu na p...

10. [Sprzedaż waluty wirtualnej: jak rozliczyć przychód?](https://podatki.gazetaprawna.pl/artykuly/10603329,sprzedaz-waluty-wirtualnej-jak-rozliczyc-przychod.html) - Osoba fizyczna prowadzi pozarolniczą działalność gospodarczą w zakresie IT. Przedsiębiorca zamierza ...

11. [Art. 30b. pod. dochod. fiz. - Ustawa o podatku dochodowym od osób ...](https://lexlege.pl/ustawa-o-podatku-dochodowym-od-osob-fizycznych/art-30b/) - Art. 30b. pod. dochod. fiz. - Ustawa o podatku dochodowym od osób fizycznych - 1. Od dochodów uzyska...

12. [Rozliczanie strat z kryptowalut – jak odliczyć?](https://litigato.pl/rozliczanie-strat-z-kryptowalut/) - Jak rozliczyć straty z kryptowalut w PIT? Sprawdź zasady odliczeń, przenoszenie strat na kolejne lat...

13. [PIT-38 - Instrukcja krok po kroku](https://pomoc.pitax.pl/instrukcja-pit-38/) - Czy mogę dopisać koszty wyższe niż przychód z części E (czyli wykazać stratę na tych transakcjach)?....

14. [Jak rozliczać się z kryptowalut w 2025 roku?](https://www.ifirma.pl/blog/jak-rozliczac-sie-z-kryptowalut-w-2025-roku/) - Kryptowaluty a rozliczenie podatkowe w 2025! Od darowizn po faktury - wszystko co musisz wiedzieć o ...

15. [PIT-38 jak wypełnić? Zakup i sprzedaż kryptowalut w PIT-38](https://podatkiprogramisty.pl/pit-38-jak-wypelnic-zakup-i-sprzedaz-kryptowalut-w-pit-38/) - Złożenie tego dokumentu do końca kwietnia 2024 roku to kluczowy krok dla osób, które uczestniczyły w...

16. [Jak wypełnić PIT-38 przy rozliczaniu kryptowalut? | Blog](https://solidnaksiegowa.com/jak-wypelnic-pit-38-przy-rozliczaniu-kryptowalut/) - Nieujęcie wszystkich transakcji – w deklaracji należy uwzględnić zarówno zyski, jak i straty. Podsum...

17. [Opodatkowanie kryptowalut i kryptoaktywów podatkiem ...](http://www.witoldsrokosz.pl/pl/blog/opodatkowanie-kryptowalut-i-kryptoaktywow-podatkiem-dochodowym-od-osob-fizycznych) - W praktyce nie ma jednolitego podejścia do pojęcia kryptowalut, czasami jest ono stosowane tylko dla...

18. [Przegląd interpretacji podatkowych – kryptowaluty pod lupą](https://kryptokancelaria.pl/przeglad-interpretacji-podatkowych-kryptowaluty-pod-lupa/) - Zobacz, jak fiskus interpretuje podatki w przypadku osób związanych z kryptowalutami. Analiza najnow...

19. [Rozliczenie PIT od przychodów ze sprzedaży kryptowalut](https://www.pitax.pl/wiedza/poradnik-rozliczenia/rozliczenie-pit-od-przychodow-ze-sprzedazy-kryptowalut/) - Ustal kwotę nadwyżki kosztów do przeniesienia, gdy koszty przewyższają przychód. Oblicz podatek jako...

20. [Konwencja między Rządem Rzeczypospolitej Polskiej a ... - Finanse](https://finanse-arch.mf.gov.pl/sv/web/wp/wynik/-/asset_publisher/JLw0/content/konwencja-miedzy-rzadem-rzeczypospolitej-polskiej-a-rzadem-krolestwa-szwecji-w-sprawie-unikania-podwojnego-opodatkowania-i-zapobiegania-uchylaniu-sie-od-opodatkowania-w-zakresie-podatkow-od-dochodu-podpisana-w-sztokholmie-dnia-19-listopada-2004-r/pop_up?_101_INSTANCE_JLw0_viewMode=print)

21. [Sweden, double tax treaty, convention - Poland - Webset.cz](https://www.webset.cz/english/tax_poland_sweden.htm) - Poland - double tax treaty ( convention ) between Poland and Sweden, company formation in Poland, po...

22. [Sweden Crypto Tax Guide 2026](https://kryptos.io/guides/sweden-crypto-tax-guide) - A flat tax rate of 30% applies to all gains made from crypto assets. Note that this only applies whe...

23. [jak opodatkować w przypadku zmiany rezydencji podatkowej? Istotny ...](https://www.nexiaadvicero.eu/obrot-kryptowalutami-jak-opodatkowac-w-przypadku-zmiany-rezydencji-podatkowej-istotny-wyrok-wsa/) - Rozliczanie przychodów z obrotu kryptowalutami wciąż budzi liczne wątpliwości podatników – szczególn...

24. [Jak rozliczyć kryptowaluty za 2025 rok? - Finanse Księgowość Kadry](https://ksiegowosc-skarbiec.pl/baza-wiedzy/jak-rozliczyc-kryptowaluty-za-2025-rok/) - Nie jesteś pewien jak rozliczyć kryptowaluty przed fiskusem? Skontaktuj się z nami 📞22 586 40 00☎️

25. [Opodatkowanie kryptowalut nie zależy od osiągnięcia zysku](https://podatki.gazetaprawna.pl/artykuly/9617224,opodatkowanie-kryptowalut-nie-zalezy-od-osiagniecia-zysku.html) - Podatnik, który obraca kryptowalutami zobowiązany jest do odprowadzenia podatku dochodowego. Dotyczy...

26. [Rozliczenie zagranicznych wirtualnych walut](https://poradnikprzedsiebiorcy.pl/-rozliczenie-zagranicznych-wirtualnych-walut) - Rozliczenie zagranicznych wirtualnych walut zależy od tego, czy z konkretnym krajem zawarta została ...

27. [How to lose your Polish tax residency](https://rezydencja-podatkowa-malta.pl/en/how-to-lose-your-polish-tax-residency/) - To lose Polish tax residency, you must transfer your center of vital interests abroad and spend fewe...

28. [Rozliczenie kryptowalut na PIT-38 – jak prawidłowo ...](https://mentzen.pl/blog/inne/kryptowaluty/rozliczenie-kryptowalut-na-pit-38-jak-prawidlowo-rozliczyc-podatek/) - Dochody (lub straty) ze sprzedaży kryptowalut należy rozliczyć na formularzu PIT-38 jako przychody z...

29. [Jak rozliczyć kryptowaluty na PIT-38 - Biuro Rachunkowe Kurdynowski](https://kurdynowski.com.pl/jak-rozliczyc-kryptowaluty-na-pit-38/) - Zachęcamy do przeczytania naszego wpisu blogowego ✔️ Jak rozliczyć kryptowaluty na PIT-38 - gwarantu...

30. [NSA w uchwale wyjaśnił, jak liczyć pięcioletni termin ...](http://www.poradypodatkowe.pl/artykul,1635,15990,nsa-w-uchwale-wyjasnil-jak-liczyc-piecioletni-termin.html) - W świetle tej uchwały, organy podatkowe mają pięć lat od końca roku podatkowego, w którym poniesiona...

31. [Deklaracje PIT z lat poprzednich a przedawnienie - PIT.pl](https://www.pit.pl/aktualnosci/deklaracje-pit-z-lat-poprzednich-a-przedawnienie-915131) - Termin przedawnienia zaległości wynikającej z realizacji ulgi mija w terminie 5 lat licząc od końca ...

32. [Prawo do weryfikacji straty przedawnia się po 5, a nie po 10 ...](https://doradca.lublin.pl/publikacje/newslettery/prawo-do-weryfikacji-straty-przedawnia-sie-po-5-a-nie-po-10-latach) - W konsekwencji w przypadku opisanym powyżej organ podatkowy będzie mógł weryfikować prawo do odlicze...

33. [Odliczanie strat z lat ubiegłych przez podatników PIT](http://www.rozliczeniapodatkowe.pl/artykul,1807,20567,odliczanie-strat-podatkowych-z-lat-ubieglych-przez-podatnikow.html) - Podatnik PIT od dochodu osiągniętego w 2022 r. może odliczyć straty z lat ubiegłych, które powstały ...

34. [Kryptowaluty a podatek PIT – jak je prawidłowo rozliczać i czy ...](https://www.pit.pl/pit-38/kryptowaluty-a-podatek-pit-jak-je-prawidlowo-rozliczac-i-czy-mozna-to-zrobic-w-ramach-dzialalnosci-gospodarczej) - Kryptowaluty od kilku lat są popularnym aktywem inwestycyjnym, a także spekulacyjnym. Trudno się dzi...

35. [Podatek dochodowy od kryptowalut. Co warto wiedzieć?](https://fintek.pl/podatek-dochodowy-od-kryptowalut-co-warto-wiedziec/) - Podmioty obracające walutami wirtualnymi nie są zobowiązanie do wystawienia PIT-8C, zatem obliczenie...

36. [Crypto Tax in Poland: 2025 Guide](https://www.dudkowiak.com/blog/crypto-tax-in-poland-2025-guide/) - Discover Poland’s 2025 crypto tax regulations: Understand the 19% flat tax on gains, reporting oblig...

