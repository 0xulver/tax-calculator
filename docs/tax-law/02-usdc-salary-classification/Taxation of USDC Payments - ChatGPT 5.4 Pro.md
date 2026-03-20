I could not access `/home/ulver/code/ai/tax-calculator/docs/personal-tax/pit.pdf` in this environment, so the 2024 assessment below is based on the fields and amounts you quoted.

**Bottom line**

* On the facts you gave, the 2024 **PIT-37 was very likely the wrong annual form**. Official 2024 PIT-37 guidance limits that form to scale-taxed income received **through a payer** shown on PIT-11/PIT-11A/PIT-40A/PIT-R/IFT-1R, while official 2024 PIT-36 guidance covers scale-taxed income **without a payer** and art. 13 income for which the taxpayer had to pay advances himself. ([Podatki][1])

* The tax firm’s **source classification** is less obviously wrong. Treating the remuneration as **art. 13 pkt 8 działalność wykonywana osobiście** with **20% KUP** is legally plausible even though the client was foreign and the payment medium was USDC. The bigger substantive risk is that the facts could be re-read as **de facto business activity** because the work was regular, organized, continuous and for profit. ([ISAP][2])

* Polish law points to a **two-step** result, closest to your Swedish precedent: first **service income**, then later **crypto disposal**. Receiving USDC for work is not best read as PIT-38-only income; later USDC -> EUR is a separate PIT-38 event. A 2024 KIS interpretation in a business case says the value of the receivable satisfied in virtual currency becomes the acquisition cost for later PIT-38 purposes, which would usually make later disposal close to tax-neutral except for price movement and fees. That interpretation is directly about JDG/business income, so for your pre-JDG art. 13 facts it is the best analogue I found, not a square official answer. ([ISAP][2])

* If 2024 stayed on art. 13 without a payer, **monthly advances were likely required**. Missing them creates arrears/interest exposure even if the annual tax was later paid on time. Paying the whole annual PIT in April 2025 does not automatically erase the missed-advance issue. ([ISAP][2])

* **PIT/ZG is probably not the main 2024 problem** if the work was physically performed from Poland and no US tax was paid. The more urgent issues are PIT-37 vs PIT-36, the advance-tax treatment, possible PIT-38 treatment of the USDC, and ZUS. ([ISAP][2])

## 1) 2024 filing: what looks wrong, and what is only arguable

### PIT-37 vs PIT-36

Assuming the US DeFi company did **not** act as a Polish payer and did **not** issue a Polish payer information form, **PIT-36 was the proper annual return**, not PIT-37. The official 2024 PIT-37 brochure says PIT-37 is for income received through a payer shown on PIT-11/PIT-11A/PIT-40A/PIT-R/IFT-1R. The official 2024 PIT-36 brochure says PIT-36 is for scale-taxed income where the taxpayer pays advances himself, including art. 13 pkt 2, 4, 6-9 income received without a payer. ([Podatki][1])

So, on the facts you gave, the **form choice looks like a real error**. The annual tax amount may or may not change much if the art. 13 classification stays the same, but the annual return architecture still looks wrong.

### Can it still be corrected?

Yes. The general rule is that a taxpayer may correct a filed return by filing a correcting return, unless the correction right is suspended by an audit/proceeding situation. ([Podatki][3])

Practically, I would treat the fix as a **correcting 2024 PIT-36** that supersedes the prior annual settlement, not as two parallel annual returns left standing side by side.

### Was the art. 13 pkt 8 classification itself wrong?

Not necessarily. Art. 13 pkt 8 covers personal services under zlecenie/dzieło-type arrangements obtained from entrepreneurs or legal persons, and art. 22 ust. 9 pkt 4 gives **20% KUP** for that source. Nothing in those provisions makes the result depend on the payer being Polish or on the remuneration being fiat. Art. 11 also taxes non-cash benefits at market value, so payment in USDC does not, by itself, force the receipt into PIT-38 instead. ([ISAP][2])

What **is** arguable is whether the facts were already **business activity** in substance. Art. 5a pkt 6 defines business activity as gainful activity carried out in one’s own name in an organized and continuous way, while art. 5b ust. 1 says activity is **not** treated as business only if all three employee-like conditions are met. Your facts increase business risk: recurring biweekly payments, one-client contracting pattern, organized software work for profit, and later formalization into JDG. ([ISAP][2])

My ranking on 2024 is:

* **Likely wrong:** PIT-37 instead of PIT-36.
* **Likely incomplete:** no proper advance-tax treatment.
* **Arguable but plausible:** art. 13 pkt 8 + 20% KUP.
* **Potentially missing:** PIT-38 treatment of the USDC.
* **Important separate risk:** ZUS.

## 2) What is the best Polish tax classification of USDC salary/payments?

For Polish law, the strongest answer is **not** “crypto gains only.” The better reading is:

1. **Service income** under the appropriate source rules, because the USDC is remuneration for work.
2. **Separate PIT-38 consequences** when the virtual currency is later disposed of. ([ISAP][2])

So for your question 17, the closest answer is **(c) both**, but with an important nuance: the first layer is **not** capital gains from crypto; it is service/business income. PIT-38 appears later, at disposal.

I view **“inne źródła”** as weak here, because there are more specific source rules for remuneration for work. I also view **PIT-38-only treatment of the initial receipt** as weak, because art. 17 and the PIT-38 brochure focus on **odpłatne zbycie** of virtual currency, not on the initial earning of remuneration. ([ISAP][2])

## 3) When is the taxable event, and what PLN value should be used?

### Service-income moment

If you stay with pre-JDG **art. 13**, the natural tax point is when the remuneration is **received or put at your disposal**, because art. 11 taxes received money, money values, and benefits in kind / other non-cash benefits. ([ISAP][2])

### PLN valuation

I would **not** treat USDC as ordinary foreign currency for black-letter valuation purposes. Art. 11a applies to amounts expressed in **foreign currencies**, while the 2024 KIS interpretation says virtual currency cannot be treated like legal tender / foreign currency. That means the cleaner legal route is to use the **market PLN value of the USDC at receipt time**, documented consistently, rather than simply applying the NBP USD rate as if USDC were USD. Using NBP USD as a proxy may be practical if it tracked $1 closely, but it is not the cleanest textual basis. ([ISAP][2])

### Later USDC -> EUR sale

That later exchange is a **PIT-38 event**, because disposal of virtual currency includes exchange for legal tender. ([ISAP][2])

### Cost basis for PIT-38

The most useful interpretation I found is KIS 0115-KDIT1.4011.25.2024.1.MR, reproduced by INFORLEX. It says that when a service receivable is settled in virtual currency, the taxpayer **acquires** the virtual currency for consideration, and the direct acquisition cost is the value of the receivable/wynagrodzenie satisfied by that crypto. It also says that if later sale proceeds equal those costs, there is no PIT-38 income, though the PIT-38 reporting obligation still exists. ([Inforlex][4])

That is exactly the logic that avoids double tax. I think it is the **best reading** for your situation too, but I want to be precise: the published interpretation I found is about **JDG/business income**, not an art. 13 non-business case.

## 4) What does that mean for 2024 and 2025 PIT-38?

This point is more important than it first appears.

If **any** 2024 USDC was sold, exchanged for EUR/PLN, used to buy goods/services, or used to settle liabilities in 2024, then a **2024 PIT-38 clearly belonged in 2024**. The PIT-38 brochure expressly treats those events as crypto disposals. ([Podatki][5])

Even if **no 2024 disposal** happened, there is still a **serious argument** that 2024 PIT-38 should have been filed to show **crypto acquisition costs carried forward**, because the PIT-38 brochure says the form is also for taxpayers who incurred crypto costs even with no crypto-sale revenue that year, and the 2024 KIS interpretation treats remuneration settled in crypto as such an acquisition cost. Again, that point is strongest in the JDG/business interpretation, so for your non-JDG facts I would call it a **material analogue, not a settled certainty**. ([Podatki][5])

That means the “no PIT-38 in 2024” issue is potentially broader than just “were there 2024 sales?”

## 5) Were monthly advances required, and what happens if they were missed?

Yes, **most likely**. Art. 44 ust. 1a covers taxpayers receiving, without a payer, foreign work income and art. 13 pkt 2, 4, 6-9 income; the official PIT-36 materials repeat that those taxpayers pay advances themselves. The due date is generally the **20th day of the following month**, with the year-end rule handled in the annual-return cycle. ([ISAP][2])

If they were not paid, the clearest statutory consequence is **tax arrears plus interest**. Ordynacja podatkowa says unpaid advances are arrears, interest runs from the day after the due date, and after year-end the authority may determine interest on missed advances up to the annual-return filing date. So if the full 2024 annual PIT was paid on time with the return, the missed-advance issue does **not** disappear, but the interest exposure should generally stop at the annual-return date rather than run forever. ([ISAP][6])

The reduced 50% self-correction interest rate appears unlikely to help now, because Ordynacja ties it to a correction within six months of the filing deadline. For 2024, that window has already passed. ([ISAP][6])

## 6) PIT/ZG and the Poland-USA treaty

The Ministry of Finance treaty list updated in January 2026 still shows the **1974 Poland-USA treaty** as the treaty in force. In that treaty, **art. 15** covers independent personal services, **art. 16** employment, and **art. 8** business profits. On your stated facts — Polish resident, work physically performed from Poland, no US fixed base / PE / US workdays indicated — the treaty points toward **Poland** as the taxing state, not the US. ([Podatki][7])

That is why I think **no PIT/ZG is probably not the core 2024 error**. The official MF page about “dochody z pracy wykonywanej za granicą” ties PIT-36 + PIT/ZG to **work performed abroad**, and the PIT Act treats work/personal activity performed in Poland as Polish-located income regardless of where remuneration is paid, which reinforces the view that work done from Poland for a US client is not obviously “foreign work income” for PIT/ZG purposes. ([Podatki][8])

I would revisit PIT/ZG only if any of the work was physically performed outside Poland, US tax was withheld/paid, or some US permanent-establishment / fixed-base fact exists that is not in your summary.

## 7) 2025 Jan-Apr before JDG

If you **do not** accept a de facto business reclassification, the cleanest 2025 approach is to treat Jan-Apr 2025 the same way as the defensible 2024 approach:

* **PIT-36** for the service income,
* self-paid **monthly advances**,
* **PIT-38** for later USDC -> EUR disposals,
* and possibly PIT-38 cost carryforward if you adopt the KIS cost-basis logic. ([Podatki][3])

The later JDG does **not automatically pull Jan-Apr 2025 into the JDG**. The only way to put those months into business is to say the business **already existed in substance**. If you do that, official business guidance says the CEIDG start date should reflect the **true first day of business**, and ryczałt is chosen by the **20th day of the month after the first business income**. That means a later April/May registration/election may not retroactively sanitize Jan-Apr business income. ([BizCentral][9])

So the two realistic 2025 positions are:

* **Defend non-business / art. 13** for Jan-Apr 2025, then later JDG from the true JDG start date.
* **Admit earlier business activity**, which opens earlier-start-date, form-of-taxation, and ZUS consequences.

## 8) ZUS: 2024 and Jan-Apr 2025

This is a real issue.

If the arrangement is treated as **zlecenie-like / analogous service contract**, Polish law provides a compulsory social-insurance title for such contractors, and health insurance follows the insured title. ZUS also has a specific **foreign payer** mechanism and explicitly says that the foreign-payer registration route covers both **umowa o pracę and umowa zlecenia** codes. So “foreign client with no Polish presence” does **not** automatically mean “no ZUS.” ([ISAP][10])

If the facts are instead treated as **business**, the official ZUS page on the Poland-USA social-security agreement says a self-employed person is subject only to the law of the state where they reside; for a Polish resident that points toward **Polish** social insurance, absent some specific treaty exception or certificate of coverage. ([zus.pl][11])

So for both 2024 and Jan-Apr 2025, ZUS is a genuine exposure point. Nonpayment can lead to interest, fines, an additional fee, and enforcement. ([zus.pl][12])

I did **not** separately verify whether there was any US certificate of coverage or some other treaty-specific social-security fact in your case. Without that, I would not assume ZUS was nil.

## Most urgent correction priorities

1. **2024 annual PIT:** strongly consider a **korekta to PIT-36** instead of leaving PIT-37 in place.
2. **2024 PIT-38:** decide whether 2024 also needs a PIT-38, either because there were actual 2024 disposals or because you want to preserve the carryforward-cost logic for crypto acquired as remuneration.
3. **2024/2025 advances:** quantify the missed art. 44 advances and likely interest exposure.
4. **2025 classification:** choose one coherent theory for Jan-Apr 2025 — either defend art. 13 outside business, or accept earlier business in substance.
5. **ZUS:** review 2024 and Jan-Apr 2025 with someone who handles foreign-payer ZUS, not just PIT.

## My overall assessment of the tax firm’s 2024 work

Most likely they made **at least one real mistake**: the **form**. They also likely **under-addressed** the consequences of having no Polish payer, especially **monthly advances** and likely **ZUS review**. Their actual **income-source classification** is not obviously absurd; it is one plausible reading. The crypto-specific weak point is that they seem to have treated the USDC only as a payment medium for PIT purposes, without clearly dealing with the separate **PIT-38 layer**.

The biggest unresolved technical point is not whether services paid in USDC are taxable as services — they most likely are. The biggest unresolved point is whether, for a **non-JDG art. 13 taxpayer**, the later PIT-38 cost basis can be defended as equal to the already-taxed remuneration value in the same way that KIS accepted for a JDG/business taxpayer. I think that is the **best reading**, but because I did not find a directly on-point published interpretation for the non-business fact pattern, that is the issue I would most want covered by an **individual interpretation**.

[1]: https://podatki-arch.mf.gov.pl/media/10539/broszura-pit-37-za-2024-r.pdf "https://podatki-arch.mf.gov.pl/media/10539/broszura-pit-37-za-2024-r.pdf"
[2]: https://isap.sejm.gov.pl/isap.nsf/download.xsp/WDU19910800350/U/D19910350Lj.pdf "https://isap.sejm.gov.pl/isap.nsf/download.xsp/WDU19910800350/U/D19910350Lj.pdf"
[3]: https://www.podatki.gov.pl/twoj-e-pit/pit-36-za-2025-rok/ "https://www.podatki.gov.pl/twoj-e-pit/pit-36-za-2025-rok/"
[4]: https://www.inforlex.pl/dok/tresc%2CFOB0000000000006502201%2CInterpretacja-indywidualna-z-dnia-19-lutego-2024-r-Dyrektor-Krajowej-Informacji-Skarbowej-sygn-0115-KDIT1-4011-25-2024-1-MR.html "https://www.inforlex.pl/dok/tresc%2CFOB0000000000006502201%2CInterpretacja-indywidualna-z-dnia-19-lutego-2024-r-Dyrektor-Krajowej-Informacji-Skarbowej-sygn-0115-KDIT1-4011-25-2024-1-MR.html"
[5]: https://podatki-arch.mf.gov.pl/media/10281/broszura-do-pit-38-za-2024-r.pdf "https://podatki-arch.mf.gov.pl/media/10281/broszura-do-pit-38-za-2024-r.pdf"
[6]: https://isap.sejm.gov.pl/isap.nsf/download.xsp/WDU20250000111/T/D20250111L.pdf "https://isap.sejm.gov.pl/isap.nsf/download.xsp/WDU20250000111/T/D20250111L.pdf"
[7]: https://podatki-arch.mf.gov.pl/podatkowa-wspolpraca-miedzynarodowa/wykaz-umow-o-unikaniu-podwojnego-opodatkowania/ "https://podatki-arch.mf.gov.pl/podatkowa-wspolpraca-miedzynarodowa/wykaz-umow-o-unikaniu-podwojnego-opodatkowania/"
[8]: https://www.podatki.gov.pl/podatki-osobiste/pit/informacje-podstawowe/co-jest-opodatkowane/dochody-z-pracy-wykonywanej-za-granica/ "https://www.podatki.gov.pl/podatki-osobiste/pit/informacje-podstawowe/co-jest-opodatkowane/dochody-z-pracy-wykonywanej-za-granica/"
[9]: https://prod.ceidg.gov.pl/CEIDG.CMS.ENGINE/GetFile.aspx?attid=eb801f75-1b62-4878-bf8e-d25e7e9b6df2 "https://prod.ceidg.gov.pl/CEIDG.CMS.ENGINE/GetFile.aspx?attid=eb801f75-1b62-4878-bf8e-d25e7e9b6df2"
[10]: https://isap.sejm.gov.pl/isap.nsf/download.xsp/WDU20250000350/T/D20250350L.pdf "https://isap.sejm.gov.pl/isap.nsf/download.xsp/WDU20250000350/T/D20250350L.pdf"
[11]: https://www.zus.pl/pracujacy/pracujacy-poza-ue-eog-lub-szwajcaria/usa "https://www.zus.pl/pracujacy/pracujacy-poza-ue-eog-lub-szwajcaria/usa"
[12]: https://www.zus.pl/firmy/rozliczenia-z-zus/sankcje-za-niewykonywanie-obowiazkow-z-zakresu-ubezpieczen-spolecznych "https://www.zus.pl/firmy/rozliczenia-z-zus/sankcje-za-niewykonywanie-obowiazkow-z-zakresu-ubezpieczen-spolecznych"
