# Tax Treatment of USDC Salary Payments in Poland (2024–2025): Pre-JDG Analysis

> **Disclaimer:** This document is research and analysis for informational purposes only. It does not constitute legal or tax advice. For binding guidance, consult a certified Polish tax advisor (doradca podatkowy) or obtain an individual interpretation (interpretacja indywidualna) from KIS.

***

## Executive Summary

The 2024 PIT-37 filing contains at least **two critical errors**: the wrong form was used (PIT-36 should have replaced PIT-37), and no PIT/ZG attachment was included for foreign-sourced income. Additionally, **no monthly advance tax payments** were made during 2024, which creates an interest liability under Art. 53a of the Tax Code — even though the full annual tax was paid at filing. The income classification as *działalność wykonywana osobiście* (Art. 13 pkt 8 PIT) is likely defensible per multiple KIS precedents, but the form and procedural omissions are significant. The ZUS situation is a potential hidden liability of substantial size. For 2025, the pre-JDG period must be reported separately on PIT-36 and cannot be retroactively absorbed into the JDG's ryczałt filings.

***

## Part I: Evaluation of the 2024 PIT-37 Filing

### Wrong Form: PIT-37 vs. PIT-36

**PIT-37 was the incorrect form** for this situation. PIT-37 is strictly reserved for income that has already been processed by a *Polish płatnik* (payer), meaning one that has issued a PIT-11, PIT-11A, PIT-40A, PIT-R, or IFT-1R information form to the taxpayer. A US-registered DeFi company with no Polish legal presence (no branch, no registered establishment, no Polish entity) is not a Polish płatnik and cannot issue any of these documents. An IFT-1R is issued only by Polish entities paying foreign residents — the opposite direction of the scenario here.[^1][^2][^3]

When income is earned directly from a foreign payer without any Polish płatnik intermediary, the correct form is **PIT-36**. PIT-36 explicitly covers: "dochody zagraniczne bez pośrednictwa polskich płatników" and "przychody ze źródeł krajowych bez pośrednictwa płatnika." The form distinction matters legally because PIT-37 lacks the fields to self-declare foreign income, carries no obligation for the taxpayer to compute monthly advance payments on that income, and does not permit the PIT/ZG foreign income attachment.[^2][^4][^1]

### Missing PIT/ZG Attachment

When a Polish tax resident earns income from a foreign source, a **PIT/ZG (Informacja o wysokości dochodów/strat z zagranicy)** attachment is mandatory. This attachment accompanies the PIT-36 declaration and identifies the country of the income source, the applicable double-taxation treaty method, and the foreign income amounts. No PIT/ZG was filed with the 2024 return, compounding the form error.[^5][^6][^7]

### Was the Income Classification Correct?

The tax company classified the income under **Art. 13 pkt 8 ustawy o PIT** (przychody z działalności wykonywanej osobiście — umowa zlecenie/o dzieło). This classification is **probably correct** and is supported by KIS interpretations, including a 2023 ruling where the Director of KIS confirmed that income from a foreign US company ("niezależny kontraktor", X Inc. registered in USA) constitutes *działalność wykonywana osobiście* under Art. 13 pkt 8, rather than *pozarolnicza działalność gospodarcza*. The key factor supporting Art. 13 pkt 8 is that the US company, as a foreign legal entity (*osoba prawna*), qualifies as the type of payer enumerated in the provision, even though it is foreign.[^8][^9]

**The 20% koszty uzyskania przychodu** are correctly applied. Art. 22 ust. 9 pkt 4 PIT provides for a 20% deduction from the revenue base for income from Art. 13 pkt 8 sources, regardless of whether the payer is Polish or foreign. This deduction was correctly calculated at 479,092.64 × 20% = 95,818.53 PLN.[^4]

#### Alternative Classification Risk: De Facto Business Activity

There is a **medium-risk counterargument**: when personal services are provided regularly, continuously, and for profit — especially biweekly payments throughout an entire year from a single client — Polish tax authorities can reclassify such activity as *pozarolnicza działalność gospodarcza* under Art. 5a ust. 6 PIT. The characteristics of the 2024 work arrangement (regular recurring payments, organized service delivery, continuous engagement) mirror the statutory definition of business activity. If reclassified, the income would need to be reported on a different section of PIT-36, ZUS contribution rules would shift, and the 20% cost deduction might be questioned. However, since no JDG was registered in 2024, this is an uncomfortable grey zone — and the KIS precedent cited above  provides reasonable protection against reclassification, particularly where the taxpayer does not bear the full economic risk of the service contract.[^9][^2]

### The USDC Question: Waluta Wirtualna or Fiat Equivalent?

USDC is a stablecoin issued on the Polygon blockchain. Under Polish law, it falls squarely within the definition of **waluta wirtualna** (Art. 5a pkt 33a ustawy o PIT, cross-referenced to Art. 2 ust. 2 pkt 26 of the AML Act), which defines a virtual currency as "cyfrowe odwzorowanie wartości" that is exchangeable for legal tender and transferable electronically. For the entire 2024 tax year, USDC's status as a waluta wirtualna was unambiguous.[^10][^11]

**Note on MiCA (relevant from late 2024 onward):** USDC's issuer (Circle) obtained an EMI (electronic money institution) license in the EU, technically classifying USDC as an *e-money token* (EMT) under MiCA, which could imply it is "pieniądz elektroniczny" rather than a "waluta wirtualna" — since the AML Act definition excludes pieniądz elektroniczny from waluta wirtualna. As of March 2026, the Polish Sejm's *ustawa o rynku kryptoaktywów* was **vetoed twice** (December 2025 and March 2026), leaving this regulatory gap unresolved. However, KIS issued an interpretation in early 2026 confirming that stablecoins including USDC should **continue to be treated as waluta wirtualna** for PIT purposes pending legislative resolution. The risk of reclassification of USDC exists but is currently low.[^12][^13][^14]

### Taxable Event: When Does Income Arise from USDC Payments?

KIS has issued a consistent line of interpretations establishing that **receiving cryptocurrency as payment for services constitutes a barter transaction (transakcja barterowa)**, creating income at the moment of receipt. The key references:[^15][^16]

- KIS 0113-KDIPT2-3.4011.549.2019.3.PR (January 2020): payment in crypto for IT services = income from business activity at receipt[^15]
- KIS 0113-KDIPT2-1.4011.665.2022.2.MGR (October 2022): crypto received for services, taxed at ryczałt rate at receipt[^15]
- KIS 0111-KDIB1-1.4010.303.2023.1.MF (July 2023): receiving crypto as payment for IT services = barter = income at receipt, with the crypto acquisition cost equal to the declared service value[^16]
- KIS 0113-KDIPT2-3.4011.546.2024.1.SJ (October 2024): crypto received as bonus = *inne źródła* income taxable at receipt at market value, taxed under Art. 27 ust. 1 PIT (progressive scale)[^17]

**This is consistent with Sweden's Skatteverket position** as described in the query. Poland's KIS views USDC received as salary as service income at the moment of receipt, not as a crypto capital gain event.

**PLN valuation method:** The USDC received must be valued in PLN using the **NBP middle rate for USD from the last business day before the date of receipt** (Art. 11a ust. 1 PIT). Since USDC maintains a 1:1 USD peg, this effectively means: number of USDC × NBP USD/PLN rate (t-1).[^18][^19][^20]

### The PIT-38 Interaction

This is where the **barter doctrine produces its most important consequence**. When USDC is received as service income and declared at its PLN value at receipt, that declared PLN value becomes the **cost basis for the USDC** on PIT-38. Therefore:[^21][^15]

- PIT-38 *przychód* = PLN equivalent of EUR received (at NBP EUR rate, day before sale)
- PIT-38 *koszt* = PLN value declared as service income at receipt of each USDC tranche
- **Net gain ≈ FX movement only** (USD/PLN at receipt vs EUR/PLN at sale, adjusted through the USDC/USD peg)

For the USDC→EUR conversions in 2024 and 2025, the cost basis should approximate the income already declared, making the net PIT-38 liability very small — effectively only capturing currency movements between the USDC receipt date and the EUR conversion date. **This aligns precisely with the Swedish Skatteverket approach**, treating USDC as a service payment and only the subsequent disposal as a secondary capital event.

**However:** the 2024 filing did NOT include a PIT-38 for the USDC→EUR conversions. If any USDC was sold in 2024, a PIT-38 should have been filed — even if the resulting tax is near zero due to the high cost basis. Failing to file PIT-38 when required is an administrative error, even if no tax is owed.

***

## Part II: Advance Tax Obligations and Interest Liability

### Was Monthly Zaliczka Required?

**Yes, and this is the most financially significant procedural error.** Art. 44 ust. 1a ustawy o PIT explicitly requires individuals receiving income from Art. 13 sources (działalność wykonywana osobiście) **without a Polish płatnik** to calculate and remit monthly advance tax payments themselves — by the 20th day of the following month. The provision reads that this obligation applies to those receiving "przychody bez pośrednictwa płatnika." A foreign US company paying USDC with no Polish presence = no Polish płatnik = self-reporting obligation.[^8]

The monthly advances must be calculated as: cumulative income since January × applicable tax rate (12% / 32%) – standard allowances – previously paid advances. For December, the advance is payable by January 20 of the following year, not by April 30.[^8]

### Consequences of Not Paying Monthly Advances

**Interest under Art. 53a Ordynacji podatkowej** is the primary consequence. This provision allows the tax authority to determine interest on advance tax payments calculated from the statutory due date of each monthly installment through the date the annual tax return is filed (or the last day of the filing deadline if late). The taxpayer is expected to **self-calculate and pay this interest** — the office does not send a notice. Failure to self-pay can result in the interest being discovered during audit.[^22][^23]

Interest rate: the standard rate under Polish tax law is 200% of the base NBP rate + 2%, historically ranging around **8–10% per annum** in 2024. For 479K PLN of income spread across 12 months, and interest calculated on rolling monthly underpayments through April 30, 2025, the estimated interest liability is roughly **PLN 5,000–10,000** depending on the income distribution across months.

**No criminal liability (KKS)** arises simply from failing to pay monthly advances, provided the full annual tax is paid upon filing. Criminal tax liability under the KKS typically requires intent to evade tax, not mere procedural non-compliance with advance payment schedules.[^24]

**The 95,048 PLN full tax was paid at filing** — this eliminates the principal liability, but interest on the monthly shortfalls **does not automatically extinguish upon filing**. Under Art. 53a OP, the authority may separately assess this interest. The taxpayer should proactively calculate and pay estimated interest now to avoid compounding.[^22]

***

## Part III: The Korekta — Correcting the 2024 Filing

### Can PIT-37 Be Corrected to PIT-36?

**Yes.** Under Art. 81 § 1 Ordynacji podatkowej, a taxpayer may file a corrective declaration at any time before the statute of limitations expires (5 years from the end of the calendar year in which the tax fell due — so PIT-37 for 2024 can be corrected until December 31, 2030). The correction is made on the **correct form** (in this case PIT-36 for the year 2024) marked as "korekta", which completely replaces the original filing. The incorrect PIT-37 becomes void.[^25][^26][^27][^28]

### What the Korekta Should Accomplish

| Item | Original PIT-37 | Corrected PIT-36 |
|------|----------------|-----------------|
| Form | PIT-37 (wrong) | PIT-36 (correct) |
| Attachment | None | PIT/ZG (foreign income from USA) |
| Income section | Sec. E, Art. 13 pkt 8 | Part D (Art. 13), foreign-source row |
| 20% cost deduction | Applied (correct) | Same, maintained |
| Revenue amount | 479,092.64 PLN | Verify vs NBP USD rates at each receipt date |
| PIT-38 for crypto | Not filed | File separately if any USDC sold in 2024 |
| DTA method | Not indicated | Proporcjonalne odliczenie (1974 US-Poland treaty) |
| Zaliczka paid | 0 PLN | 0 PLN (but interest owed separately) |

**Priority actions for the 2024 korekta:**
1. File PIT-36 (korekta) with PIT/ZG, replacing PIT-37
2. Verify the PLN income amount using NBP USD rates for each USDC receipt date
3. Calculate and pay interest on unpaid monthly advances (Art. 53a OP)
4. If USDC was converted to fiat in 2024, file PIT-38 (possibly near-zero liability if cost basis = declared income)

The **total tax liability should not change materially** if the income amount was calculated correctly (NBP USD rates × USDC received). The key benefit of the korekta is removing formal legal risk — using the wrong form means the filed return may not be legally valid as a PIT-36 declaration, which could create complications if audited.

### Poland–USA Double Taxation Treaty

The applicable treaty is the 1974 Convention between Poland and the USA (Dz.U. z 1976 r. Nr 31, poz. 178, in force from 1976). A new convention was signed in 2013 but its ratification status in both countries requires confirmation. Under the 1974 treaty, income from **independent personal services** (Art. 14 — wolne zawody) is taxable **only in the country of residence**, unless the taxpayer maintains a fixed base in the other country. Since the taxpayer is a Polish resident with no US fixed base, the income is taxable exclusively in Poland. No US tax was paid. The method of double-tax relief in PIT/ZG should be noted as *proporcjonalne odliczenie* (with zero credit, since no tax was paid abroad).[^29][^30][^31][^4]

***

## Part IV: 2025 Pre-JDG Income — Correct Treatment

### Classification and Form

The Jan–Apr 2025 USDC payments (40,500 USDC ≈ 160,000–165,000 PLN) received **before JDG registration** must be reported as **personal income, not business income**. Pre-JDG income cannot be retroactively attributed to the JDG, regardless of when the JDG was established. The JDG's tax obligations begin on its registration date.[^32][^33]

**These payments cannot be classified as działalność nierejestrowana** either — the monthly limit for unregistered activity in 2025 was PLN 3,499.50 per month. Each payment of 6,000 USDC ≈ 24,000 PLN individually far exceeds this threshold, making nierejestrowana impossible.[^33][^32]

The same classification as **Art. 13 pkt 8 (działalność wykonywana osobiście)** that was applied in 2024 applies here, reported on **PIT-36 for the year 2025** (due April 30, 2026), with PIT/ZG attachment. The 20% cost deduction applies.

The fact that a JDG was later registered further strengthens the *de facto* business activity argument for this period. However, absent a JDG during Jan–Apr, the practical approach is to report as Art. 13 pkt 8 on PIT-36, identical to the 2024 treatment.

### Monthly Advance Payments in 2025

The **same Art. 44 ust. 1a obligation applies** for the Jan–Apr 2025 period. Monthly advances should have been paid by February 20, March 20, April 20, and May 20, 2025. If not paid, interest on those advances will accrue from those due dates through the April 30, 2026 filing date.

Once the JDG is registered and ryczałt applies, **the JDG handles its own advance payments separately** under the ryczałt regime — the two income streams are entirely separate.

### PLN Valuation of USDC Receipts in 2025

Same methodology as 2024: NBP USD/PLN middle rate from the last business day before each USDC receipt date. Specific rates for each of the seven payment dates (January–April 2025) must be obtained from the NBP archive (nbp.pl) and applied to each tranche.[^20][^18]

### PIT-38 for 2025 USDC→EUR Conversions

Conversions of USDC to EUR on Binance/Kraken in 2025 trigger PIT-38 obligations. With USDC already taxed as service income at receipt:[^34][^35]
- Cost basis = PLN NBP USD rate (day before receipt) × USDC amount
- Revenue = PLN NBP EUR rate (day before conversion) × EUR amount received
- Net gain ≈ only exchange rate movement between receipt and conversion

This **dual-taxable-event treatment** (service income + crypto disposal) is exactly what KIS requires in the barter doctrine interpretations. The second event (disposal) is taxed as *przychody z kapitałów pieniężnych* at 19% on net gain, reported on PIT-38. Both PIT-36 (for service income) and PIT-38 (for crypto gains) must be filed for 2025.[^34][^17][^16][^15]

***

## Part V: ZUS Social Insurance Obligations

### Legal Framework for the 2024 and Pre-JDG 2025 Periods

The Poland–USA Totalization Agreement (Dz.U. 2009 Nr 46, poz. 374, effective March 1, 2009) governs social insurance between the two countries. The general rule in Art. 6 ust. 1 of this agreement is **lex loci laboris**: a person is subject to the social security legislation of the country where they work. A Polish resident working remotely from Poland for a US company is working on Polish territory, regardless of the employer's location.[^36][^37][^38]

This means **Polish ZUS applies**, not US Social Security, for the 2024 and pre-JDG 2025 periods. Under Polish law, a person performing services under umowa zlecenie (or any umowa o świadczenie usług) on Polish territory is subject to mandatory ZUS contributions: emerytalne (pension), rentowe (disability/survivors), wypadkowe (accident) are obligatory; chorobowe (sickness) is voluntary.[^37][^39][^38]

### Who Pays ZUS When the Employer is Foreign?

The US DeFi company has no Polish registration and is not a *płatnik składek* in the Polish ZUS system. In such cases, **the person performing the services is required to register themselves as a ZUS płatnik** and remit both the "employer" and "employee" portions of ZUS contributions. The ZUS website explicitly provides guidance on a foreign employer registering (or failing to register) as a składki payer — and if the foreign entity doesn't, the employed person must.[^40]

The contribution base is the gross przychód. For a person whose sole title to insurance is umowa zlecenie (no JDG, no employment contract), the full mandatory ZUS rates apply:
- Emerytalne: 19.52% (split: 9.76% employer + 9.76% employee)
- Rentowe: 8% (split: 6.5% employer + 1.5% employee)
- Wypadkowe: ~1.67% (employer)
- Zdrowotne: 9% (employee)
- Total effective burden (all contributions): approximately **38–40% of gross income**

Applied to 479,092 PLN in 2024, this represents a potential ZUS liability of approximately **PLN 180,000–190,000** in total contributions for 2024 alone. This is the **single largest financial risk** of the entire situation and should be assessed with urgency.

### Should Retroactive ZUS Be Corrected?

ZUS contributions can be corrected retroactively. The statute of limitations for ZUS contribution assessment is **5 years** from the due date of each contribution. If the taxpayer proactively self-registers and declares retroactive contributions, it may be possible to negotiate a payment plan (układ ratalny). Doing nothing is riskier: if the large income declaration on the corrected PIT-36 triggers a ZUS cross-check, the ZUS can independently assess the full contributions plus interest at 14.5% p.a. (the elevated rate for ZUS defaults).

**Important nuance:** The KIS interpretation framework treats the ZUS situation for foreign-payer zlecenie income as complex and often left unaddressed by tax advisors. The fact that the tax company filed PIT-37 (wrong form) and apparently never addressed ZUS suggests this was indeed missed. A specialist ZUS advisor should be consulted immediately.

***

## Part VI: Risk Summary and Urgency Matrix

| Issue | Severity | Financial Impact | Urgency |
|-------|----------|-----------------|---------|
| Wrong form (PIT-37 → PIT-36) | High | Administrative; invalidation risk | File korekta asap |
| Missing PIT/ZG attachment | High | Formal error; may trigger audit | File with korekta |
| No monthly advance payments (2024) | Medium-High | ~PLN 5,000–10,000 in interest | Calculate + pay now |
| ZUS contributions not paid (2024) | Critical | ~PLN 180,000–190,000 | Consult ZUS specialist urgently |
| No PIT-38 for 2024 USDC→EUR | Medium | Likely near-zero tax; formal error | File separate PIT-38 if applicable |
| ZUS contributions not paid (2025 pre-JDG) | High | ~PLN 60,000–65,000 | Bundled with 2024 ZUS fix |
| Monthly advances not paid (2025 pre-JDG) | Medium | ~PLN 1,500–3,000 interest | Include in 2025 PIT-36 filing |
| USDC valuation methodology | Low-Medium | Depends on NBP rate vs declared amount | Verify on korekta |
| USDC reclassification post-MiCA | Low | Uncertain; currently KIS confirmed status quo | Monitor; low action now |
| De facto business activity | Low-Medium | Reclassification risk if audited | Mitigated by KIS precedent |

***

## Part VII: Key KIS Interpretations to Reference

When preparing the korekta and 2025 filing, the following binding KIS precedents support the positions taken:

1. **0113-KDIPT2-3.4011.549.2019.3.PR** (January 2020): USDC/crypto received for services = barter = service income at receipt + PIT-38 cost basis equals declared income[^15]
2. **0113-KDIPT2-1.4011.665.2022.2.MGR** (October 2022): Crypto payment for services to JDG taxed at ryczałt at receipt; subsequent disposal taxed on PIT-38[^15]
3. **0111-KDIB1-1.4010.303.2023.1.MF** (July 2023): Crypto received as IT service payment = barter; CIT (applicable logic also to PIT); cost basis = invoice value at receipt[^16]
4. **KIS (2023, foreign US company)**: Income from foreign US company "niezależny kontraktor" = Art. 13 pkt 8 (not business activity)[^9]
5. **0113-KDIPT2-3.4011.546.2024.1.SJ** (October 2024): Crypto bonus received by individual = inne źródła (Art. 20), valued at receipt; later disposal = PIT-38[^17]
6. **KIS (March 2026)**: Stablecoins (USDC/USDT) remain treated as waluta wirtualna for PIT — exchange to stablecoin is neutral[^12]

The taxpayer may also apply for their own **interpretacja indywidualna** (individual ruling) from the Director of KIS (fee: 40 PLN) to bind the tax authority to a specific position on the USDC valuation methodology or income classification going forward. This is highly recommended given the regulatory uncertainty around USDC post-MiCA.

***

## Part VIII: Recommended Action Plan

**Immediate (before April 30, 2026 — 2025 PIT deadline):**

1. **Engage a tax advisor with international PIT experience** (the original tax company demonstrated insufficient expertise for this case)
2. **File PIT-36 (korekta) for 2024**, replacing PIT-37 — with PIT/ZG attachment
3. **Calculate unpaid advance tax interest for 2024** (Art. 53a OP) and pay it proactively
4. **Verify 2024 USDC income amount** against NBP USD rates for each receipt date; adjust if the declared 479,092 PLN differs
5. **File PIT-38 for 2024** if any USDC was sold/converted in 2024 (even with near-zero liability)
6. **Prepare and file 2025 PIT-36** for Jan–Apr 2025 income, separately from JDG ryczałt
7. **Include PIT/ZG** for the 2025 pre-JDG income
8. **Calculate and declare interest** on unpaid advances for Jan–Apr 2025

**Medium-term (within 3–6 months):**

9. **Consult a ZUS specialist** regarding retroactive ZUS contribution obligations for 2024 and early 2025
10. **Assess totalization agreement implications** — confirm whether a PL/USA 1 certificate could have applied, and whether any US Social Security was paid (if so, may reduce Polish ZUS obligation)
11. **Apply for a KIS interpretacja indywidualna** covering: (a) USDC classification as waluta wirtualna in light of MiCA, and (b) confirmation of barter-doctrine treatment for USDC salary going forward

**Ongoing:**

12. **For future JDG operations**: since ryczałt is chosen, maintain documentation of each USDC receipt date and NBP USD rate; maintain separate PIT-38 calculations for each USDC→EUR conversion
13. **Monitor the Polish ustawa o rynku kryptoaktywów** (currently vetoed twice as of March 2026) — a third legislative attempt may change USDC's tax classification[^13]

---

## References

1. [PIT 36 2025/2026 - jak rozliczyć deklarację](https://www.e-pity.pl/pit-36/) - Termin złożenia deklaracji PIT-36 za rok 2025 upływa 30 kwietnia 2026 roku (środa). Data ta obowiązu...

2. [PIT-36: rozliczenie w 2026 roku za 2025 rok](https://www.pitax.pl/pit36/) - W sezonie za 2025 / 2026 końcowy termin złożenia i rozliczenia formularza PIT-36 przypada na 30 kwie...

3. [Podatek u źródła od przychodów z działalności ...](https://rachunkowosc.com.pl/podatek-u-zrodla-od-przychodow-z-dzialalnosci-wykonywanej-osobiscie) - W państwie źródła przychody te podlegają opodatkowaniu, pod warunkiem że podatnik ma w tym państwie ...

4. [Rozliczenie dochodów uzyskanych za granicą z działalności wykonywanej osobiście – www.VademecumPodatnika.pl](http://www.vademecumpodatnika.pl/artykul_narzedziowa,746,0,11319,rozliczenie-dochodow-uzyskanych-za-granica-z-dzialalnosci.html) - Vademecum podatnika - podstawowe informacje na temat podatków. Rozliczanie podatku VAT. Przychody i ...

5. [Załącznik PIT/ZG do PIT 36 - poradnik](https://www.e-pity.pl/pit-36/zalacznik-pit-zg/) - metodę proporcjonalnego odliczenia - dochody osiągnięte za granicą łączy się z dochodami ze źródeł p...

6. [Załącznik PIT/ZG do PIT-36L - jak wypełnić](https://www.e-pity.pl/pit-36l/zalacznik-pit-zg/) - Załącznik ten składają podmioty uzyskujące w roku podatkowym przychody z zagranicy. Dołącza się go d...

7. [PIT/ZG - dochody zagraniczne - PIT-y roczne 2025/2026 - PIT.pl](https://www.pit.pl/pit-zg/) - Jeżeli podatnik do przychodów z zagranicy ma obowiązek stosować zasadę proporcjonalnego odliczenia –...

8. [Czasem zleceniobiorca sam musi wpłacać zaliczki na PIT - rp.pl](https://pro.rp.pl/podatki/art13180841-czasem-zleceniobiorca-sam-musi-wplacac-zaliczki-na-pit) - Osoba, która pracuje na umowę zlecenie lub umowę o dzieło, musi sama wpłacać zaliczki na podatek doc...

9. [Jak osoba wykonująca usługi dla zagranicznej firmy jako ...](https://www.gazetaprawna.pl/podatki/artykuly/10757319,jak-osoba-wykonujaca-uslugi-dla-zagranicznej-firmy-jako-niezalezny-kontraktor-powinna-zakwalifikowac-swoje-przychody.html) - Wnioskodawczyni może teraz prawidłowo zakwalifikować uzyskiwane przychody jako przychody z działalno...

10. [Prawo kryptowalut w Polsce – Status i regulacje (2026)](https://www.ktzr.pl/prawo-kryptowalut-polska/) - Odpowiedź: Ustawa AML uznaje waluty wirtualne za „wartości majątkowe”, obok praw majątkowych, mienia...

11. [Nowe zasady opodatkowania walut wirtualnych (kryptowalut ...](http://www.witoldsrokosz.pl/pl/blog/nowe-zasady-opodatkowania-walut-wirtualnych-kryptowalut-w-zakresie-podatkow-dochodowych) - Przede wszystkim obie ustawy: o podatku dochodowym od osób fizycznych oraz o podatku dochodowym od o...

12. [Masz USDT lub USDC? Skarbówka wydała ważny ...](https://comparic.pl/masz-usdt-lub-usdc-skarbowka-wydala-wazny-komunikat-dla-inwestorow/) - Interpretacja podatkowa potwierdza, że wymiana kryptowalut na stablecoiny, takie jak USDT i USDC, po...

13. [Podatek od kryptowalut a weto ustawy o rynku kryptoaktywów](https://tomczykowscy.pl/podatek-od-kryptowalut-a-weto-ustawy-o-rynku-kryptoaktywow/) - Tokeny EMT mają utrzymywać stabilną wartość dzięki temu, że są powiązane z jedną walutą „tradycyjną”...

14. [Jak MiCA reguluje stablecoiny w 2025?](https://kryptokancelaria.pl/stablecoiny-w-regulacjach-europejskich-i-mica/) - Relacja między EMT a pieniądzem elektronicznym w MiCA jest hybrydowa: z jednej strony EMT są traktow...

15. [Centrum wiedzy - Płatności za usługi w walutach wirtualnych - KIP](https://izbapodatkowa.pl/baza-wiedzy/platnosci-za-uslugi-w-walutach-wirtualnych/) - Płatności za usługi w walutach wirtualnych

16. [Dotyczy ustalenia, czy: - prawidłowa jest interpretacja Wnioskodawcy, iż otrzymanie waluty wirtualnej jako płatności za świadczone usługi informatyczn... - Interpretacja - 0111-KDIB1-1.4010.303.2023.1.MF](https://www.interpretacje.pl/cit/9279111,dotyczy-ustalenia-czy-prawidlowa-jest-interpretacja-wnioskodawcy.html) - Interpretacja indywidualna z dnia 19 lipca 2023 r., Dyrektor Krajowej Informacji Skarbowej, sygn. 01...

17. [Skutki podatkowe otrzymania nagrody w formie kryptowaluty - KIP](https://izbapodatkowa.pl/baza-wiedzy/skutki-podatkowe-otrzymania-nagrody-w-formie-kryptowaluty/) - Kryptowaluty spełniają definicję waluty wirtualnej, o której mowa w art. 5a pkt 33a ustawy o podatku...

18. [Według jakiego kursu należy przeliczyć przychody ...](https://pckp.pl/baza-wiedzy/wedlug-jakiego-kursu-nalezy-przeliczyc-przychody-wyplacane-w-walutach-obcych/) - Według jakiego kursu należy przeliczyć przychody wypłacane w walutach obcych?

19. [Jak rozliczać transakcje kryptowalutowe w Polsce? Przewodnik po przepisach podatkowych](https://comparic.pl/jak-rozliczac-transakcje-kryptowalutowe-w-polsce-przewodnik-po-przepisach-podatkowych/) - Inwestowanie w kryptowaluty staje się coraz bardziej popularne, a wraz z nim rośnie potrzeba zrozumi...

20. [PIT/ZG – jak przeliczyć walutę? - BorsukPodatki.pl](https://borsukpodatki.pl/pit-zg-jak-przeliczyc-walute/) - Należy wziąć pod uwagę średni kurs obcej waluty ogłaszany przez Narodowy Bank Polski, jaki był aktua...

21. [Otrzymanie należności w wirtualnej walucie a PIT](https://poradnikprzedsiebiorcy.pl/-otrzymanie-naleznosci-w-wirtualnej-walucie-a-przychod-podatkowy) - Sprawdź, jak rozliczać otrzymanie należności w wirtualnej walucie na gruncie podatku dochodowego! Do...

22. [Kiedy przedawniają się odsetki od zaliczek zapłaconych po ...](https://pro.rp.pl/podatki/art16093251-kiedy-przedawniaja-sie-odsetki-od-zaliczek-zaplaconych-po-terminie) - Niestety, przepis ten nie określa, kiedy odsetki te – jako zobowiązanie uboczne w stosunku do zalicz...

23. [Odsetki za zwłokę - POLTAX - Baza prawa podatkowego](https://www.poltax.pl/baza_prawa_podatkowego/odsetki_za_zwloke,313/odsetki_za_zwloke,58) - Początkowy dzień biegu odsetek za zwłokę określa ustawa w art. 53 § 4 i 5 OrdPU * . Odsetki za zwłok...

24. [Niezapłacenie zaliczki na podatek dochodowy w terminie](https://poradnikprzedsiebiorcy.pl/-jakie-sankcje-groza-za-niezaplacenie-zaliczki-na-podatek-dochodowy-w-terminie) - Podatek niezapłacony w ustawowo przewidzianym terminie to zaległość podatkowa. Podstawową konsekwenc...

25. [Korekta zeznania - PITy 2025/2026 - deklaracja korygująca](https://www.pit.pl/korekta-zeznania/) - Poprzez zeznanie korygujące podatnik zmienia treść pierwotnie przekazanej deklaracji. W wyniku zmian...

26. [Jak korygować deklaracje i zeznania podatkowe? - Pity - PIT.pl](https://www.pit.pl/zasady-ksiegowosci-ksiegowosc/jak-korygowac-deklaracje-i-zeznania-podatkowe-1009930) - Deklaracje i zeznania podatkowe można korygować do czasu upływu terminu przedawnienia podatku, które...

27. [Art. 81. Ord. Podatk. - Ordynacja podatkowa - LexLege](https://lexlege.pl/ordynacja-podatkowa/art-81/) - Art. 81. Ord. Podatk. - Ordynacja podatkowa - § 1. Jeżeli odrębne przepisy nie stanowią inaczej, pod...

28. [Przedawnienie odsetek za zwłokę od zaległości ...](https://podatkowyreferat.online/2023/04/19/przedawnienie-odsetek-za-zwloke-od-zaleglosci-podatkowych/) - Zgodnie z art. 70 § 1 ustawy Ordynacja podatkowa zobowiązanie podatkowe przedawnia się z upływem 5 l...

29. [Dochody zagraniczne w PIT/ZG](https://www.szlachetnapaczka.pl/jedenprocent/artykuly/dochody-zagraniczne-w-pit-36-zg/) - Rozliczenie dochodów z zagranicy – metoda proporcjonalnego odliczenia; Jakie dochody wykazuje się w ...

30. [Jak w międzynarodowych umowach podatkowych są traktowane wolne zawody](https://podatki.gazetaprawna.pl/artykuly/483322,jak-w-miedzynarodowych-umowach-podatkowych-sa-traktowane-wolne-zawody.html) - Jak zmieniły się zasady opodatkowania z wolnych zawodów w regulacjach umów o unikaniu podwójnego opo...

31. [Umowa między Rządem Polskiej Rzeczypospolitej Ludowej a ...](https://finanse-arch.mf.gov.pl/pl/web/wp/wynik/-/asset_publisher/JLw0/content/umowa-miedzy-rzadem-polskiej-rzeczypospolitej-ludowej-a-rzadem-stanow-zjednoczonych-ameryki-o-uniknieciu-podwojnego-opodatkowania-i-zapobiezeniu-uchylaniu-sie-od-opodatkowania-w-zakresie-podatkow-od-dochodu-podpisana-w-waszyngtonie-dnia-8-pazdziernika-1974-r/pop_up?_101_INSTANCE_JLw0_viewMode=print)

32. [Działalność nierejestrowana a kwota wolna od podatku](https://poradnikprzedsiebiorcy.pl/-dzialalnosc-nierejestrowana-a-kwota-wolna-od-podatku) - Od 1 stycznia 2026 r. zmianie ulegnie sposób ustalania limitu przychodu uprawniającego do prowadzeni...

33. [Działalność nierejestrowana w 2025 roku – limit, ZUS ...](https://mk.rp.pl/blog/dzialalnosc-nierejestrowana-w-2025-roku-limit-co-z-zus-czy-jest-opodatkowana/) - Działalność nierejestrowana staje się działalnością gospodarczą w momencie przekroczenia miesięczneg...

34. [Rozliczenie kryptowaluty w PIT-38: obowiązki, koszty i ...](https://kurdynowski.com.pl/rozliczenie-kryptowaluty-w-pit-38-obowiazki-koszty-i-przychody/) - Rozliczenie kryptowalut w PIT-38 to kluczowy element odpowiedzialnego inwestowania. Dowiedz się, jak...

35. [Jak rozliczać się z kryptowalut w 2025 roku?](https://www.ifirma.pl/blog/jak-rozliczac-sie-z-kryptowalut-w-2025-roku/) - Koszty poniesione w danym roku podatkowym na zakup kryptowalut należy wykazać w zeznaniu rocznym PIT...

36. [Totalization Agreements - Ambasada USA w Polsce](https://pl.usembassy.gov/pl/totalization-agreements/) - Pełny tekst umowy w jęz. polskim i angielskim jest dostępny tutaj (PDF 1,1 MB). Umowa dotyczy kilku ...

37. [USA](https://www.zus.pl/pracujacy/pracujacy-poza-ue-eog-lub-szwajcaria/usa) - 1 Umowy stanowi, że osoby podlegają ustawodawstwu dotyczącemu zabezpieczenia społecznego tej Umawiaj...

38. [Umowa zlecenia zawarta z nierezydentem a obowiązek ...](https://doradca.lublin.pl/publikacje/prawo-pracy-i-ubezpieczen-spolecznych/umowa-zlecenia-zawarta-z-nierezydentem-a-obowiazek-oplacania-skladek-do-zus) - O konieczności zgłoszenia umowy zlecenia do obowiązkowych składek na ubezpieczenia społecznie nie de...

39. [Zgłoszenie zleceniobiorcy do ubezpieczeń społecznych i ...](https://www.zus.pl/-/zgloszenie-zleceniobiorcy-do-ubezpieczen-spolecznych-i-zdrowotnego) - Przypominamy, że każda umowa zlecenia albo umowa o świadczenie usług jest odrębnym tytułem do ubezpi...

40. [Zgłoszenie podmiotu pełniącego rolę płatnika zagranicznego](https://www.zus.pl/firmy/zgloszenie-platnika/firmy/zgloszenie-podmiotu-pelniacego-role-platnika-zagranicznego) - Jeśli jesteś pracownikiem, który przejął obowiązki zagranicznego pracodawcy, zgłoś się do ZUS jako p...

