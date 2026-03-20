# Tax Classification of Stablecoins (USDC/USDT) in Poland — 2026 Analysis

> **Executive Summary**: Under current Polish law, USDT retains unambiguous status as *waluta wirtualna* (virtual currency). USDC sits in a legally grey zone because its issuer (Circle) obtained an EU Electronic Money Institution license in June 2024, technically making USDC *pieniądz elektroniczny* — which falls **outside** the Polish definition of *waluta wirtualna*. Poland's implementing legislation for MiCA, which would have resolved this conflict by keeping EMTs within the *waluta wirtualna* category, was vetoed **twice** by President Nawrocki (December 2025 and February 2026). As of March 2026, the legal risk around USDC is real but most practitioners continue to apply the status quo approach based on KIS informal guidance. There are no published binding interpretacje indywidualne that definitively resolve the USDC EMT problem.

***

## 1. Legal Foundation: The Definition of *Waluta Wirtualna*

The definition of *waluta wirtualna* that drives all Polish crypto taxation comes from **Art. 2 ust. 2 pkt 26 of the AML Act** (Ustawa z dnia 1 marca 2018 r. o przeciwdziałaniu praniu pieniędzy oraz finansowaniu terroryzmu). Virtual currency is a digital representation of value that:

- Is NOT legal tender issued by the NBP or any central bank[^1]
- Is NOT an international unit of account established by an international organization[^2]
- Is **NOT pieniądz elektroniczny** (electronic money) under the Payments Services Act of 19 August 2011[^3]
- Is NOT a financial instrument, bill of exchange, or cheque[^2]
- AND is exchangeable for legal tender in commercial transactions, accepted as a medium of exchange, and can be stored/transferred electronically[^2]

The Polish PIT Act (Art. 5a pkt 33a) and CIT Act (Art. 4a pkt 22a) both refer directly to this AML definition. The entire special crypto taxation regime — including the rule that crypto-to-crypto swaps are tax-neutral — applies **only** to assets meeting this definition.[^2]

***

## 2. How Polish Crypto Taxation Works (The Framework)

Before addressing classification, it helps to understand the tax mechanics. Under PIT Art. 17 ust. 1 pkt 11 and Art. 30b:[^4][^5]

- **Taxable event** = *odpłatne zbycie waluty wirtualnej*: the disposal of a virtual currency by exchanging it for **legal tender, goods, services, or property rights that are NOT virtual currency**[^6][^4]
- **Not taxable** = exchanging one waluta wirtualna for another waluta wirtualna (krypto-krypto is always neutral)[^7][^4]
- **Tax rate** = 19% flat (capital gains, Art. 30b ust. 1a PIT)[^5]
- **Reporting** = annual PIT-38 declaration[^8][^9]
- **Revenue** = amount received in fiat, converted to PLN at the average NBP exchange rate from the **last business day before** the receipt date (Art. 11a ust. 1 PIT)[^5]
- **Cost basis** = documented direct expenditures to acquire the virtual currency, plus disposal costs (exchange commissions)[^10][^8]
- Excess costs over revenue **are not a loss** — they roll forward to offset gains in the next year[^10][^5]

***

## 3. USDT Classification — Straightforward

Tether (USDT) **does not hold an EMI license** under MiCA. It has not sought approval from any EU financial regulator. Because Tether lacks the EMI authorization required under MiCA's e-money token regime, USDT cannot be considered *pieniądz elektroniczny* for purposes of EU law.[^11][^12][^13]

As a result, USDT satisfies all positive criteria of the AML definition and fails none of the exclusions. **USDT is unambiguously a waluta wirtualna**. Crypto-to-USDT swaps are definitively non-taxable, and USDT-to-fiat conversion is the taxable event.[^14][^7]

> **Practical note**: Binance and other EU-regulated exchanges delisted or restricted USDT following ESMA's Q1 2025 guidance. If you are using USDT on Binance as a Polish user, you may have been automatically converted to USDC by the exchange — with significant tax implications discussed below.[^15][^16]

***

## 4. USDC Classification — The Core Legal Problem

### 4a. What MiCA Does

The EU MiCA Regulation (Regulation (EU) 2023/1114) entered into force on June 30, 2024 for stablecoin provisions. MiCA classifies stablecoins pegged to a single fiat currency as **e-money tokens (EMT)** under Art. 3(1)(7). Crucially, **Art. 48(2) MiCA explicitly states that EMTs shall be deemed to be electronic money** (*pieniądz elektroniczny*).[^17][^18][^3]

### 4b. Circle's EMI License

On June 30, 2024, Circle's French subsidiary (Circle Mint France) received an Electronic Money Institution (EMI) license from France's Autorité de Contrôle Prudentiel et de Résolution (ACPR). Circle was the **first global stablecoin issuer** to comply with MiCA. From that date, both USDC and EURC are issued in the EU under MiCA's e-money token framework.[^19][^20][^17]

Under EU law on passporting of financial licenses (applied also in Poland), an EMI license granted in one EU member state is valid throughout the EU. This means Circle's French EMI license — and by extension USDC's status as *pieniądz elektroniczny* — is legally effective in Poland.[^21]

### 4c. The Conflict with Polish Tax Law

Here is the direct legal collision:

| Criterion | AML Art. 2(2)(26) Requirement | USDC Post-MiCA |
|---|---|---|
| Not legal tender | ✅ Not legal tender | ✅ Not legal tender |
| Not pieniądz elektroniczny | **Must NOT be** e-money | **IS** e-money (MiCA Art. 48(2)) |
| Exchangeable for fiat | ✅ Yes | ✅ Yes |

Because USDC satisfies the EMT definition under MiCA and has an authorized EMI issuer, **a literal reading of Polish law would exclude USDC from the definition of waluta wirtualna**. If USDC is not a waluta wirtualna, then:[^3][^21][^2]

- Converting ETH or BTC to USDC would be a **taxable disposal** of ETH/BTC (exchanging a virtual currency for something that is NOT a virtual currency)
- The Polish *special* crypto tax regime (PIT-38, krypto-krypto neutrality) would not apply to USDC transactions

This is not a theoretical concern — tax practitioners have explicitly flagged it.[^21][^3]

***

## 5. KIS Interpretations and Official Guidance

### 5a. KIS Informal Response (February 2025)

Tax lawyer Maciej Grzegorczyk (Kryptokancelaria) obtained an **informal verbal response** from KIS in February 2025. KIS stated:[^7]

- Exchanges of crypto to stablecoins like USDT remain **tax-neutral**
- MiCA's classification of EMTs as e-money does **not affect Polish tax law**
- For tax purposes, what matters is whether a stablecoin meets the Polish AML definition

**Critical caveat**: This was a verbal/telephone consultation, **not a binding interpretacja indywidualna**. KIS verbally indicated a favorable direction but did not issue a formal ruling.[^7]

### 5b. March 2026 Interpretacja Indywidualna

In early March 2026, media reports confirmed a **binding interpretacja indywidualna** confirming that stablecoin exchanges remain tax-neutral. The interpretation cited that "wymiana pomiędzy walutami wirtualnymi pozostaje neutralna podatkowo" (exchanges between virtual currencies remain tax-neutral). However, based on available information, this interpretation appears to concern USDT/general stablecoins and may not have specifically resolved the USDC post-EMI license problem.[^22][^23]

### 5c. KIS Interpretation 0115-KDIT1.4011.745.2025.3.MN (November 24, 2025) — *Prop Trading Salary*

This interpretation directly addressed stablecoin salary payments in a prop trading context. KIS ruled:[^24]

1. **Receipt of stablecoins as salary** = immediate taxable income from personal activity (*działalność wykonywana osobiście*), taxed under the standard progressive tax scale at the moment of receipt
2. **Later sale of those stablecoins** = separate taxable event as capital gains (PIT-38, 19%)

The underlying logic: stablecoins ARE waluta wirtualna, but their receipt as compensation for services is income at receipt — not deferred until disposal. The value of salary income recognized at receipt becomes the cost basis for capital gains purposes.[^24]

### 5d. KIS Interpretation 0114-KDIP3-1.4011.51.2025.1.AK (March 11, 2025) — *IT Contractor Salary*

For an IT contractor (JDG) receiving crypto salary:[^25]
- Revenue from services = recognized at invoice issuance (business income)
- The invoiced value (PLN equivalent) becomes the **cost basis** for capital gains when the crypto is later disposed
- Prevents double taxation: income taxed once as business revenue, then the same value deducted as cost on PIT-38[^26]

### 5e. KIS Interpretation 0115-KDIT1.4011.22.2025.1.MR (March 4, 2025) — *Employee Bonus in Crypto*

Confirms that a crypto bonus received through employment:[^26]
- Value recognized as income in PIT-36 (employment income) becomes cost basis in PIT-38
- When the crypto is later sold, the previously taxed employment income amount is a deductible cost — no double taxation

***

## 6. MiCA Implementation Status in Poland — Legislative Chaos

Poland's national implementing legislation for MiCA (Ustawa o rynku kryptoaktywów) has been vetoed **twice** by President Karol Nawrocki:

| Date | Event |
|---|---|
| November 7, 2025 | Sejm passes first version of crypto assets law |
| December 1, 2025 | President Nawrocki vetoes the law (first veto)[^27][^28] |
| December 17, 2025 | Sejm passes second version (near-identical)[^29] |
| January 7, 2026 | Senate approves with one amendment[^30] |
| January 23, 2026 | Sejm rejects Senate amendment, sends to President[^31] |
| February 11, 2026 | President Nawrocki vetoes again (second veto)[^32][^33] |
| **March 2026** | **No implementing law exists; Poland non-compliant** |

The original implementing law contained a provision that would have **saved** taxpayers: it stated that EMTs (like USDC) would **remain classified as waluta wirtualna** for Polish tax purposes unless the taxpayer explicitly chose to treat them as electronic money for accounting purposes. **This critical fix never entered into force.**[^21]

Poland has until **July 1, 2026** to implement MiCA's CASP licensing framework. Without a third parliamentary attempt succeeding, Polish crypto exchanges may be unable to operate after that date.[^34][^21]

***

## 7. Transaction-by-Transaction Tax Analysis

### 7a. Receiving USDC as Salary (Freelancer/Contractor)

Receiving USDC as salary on Polygon constitutes two distinct events:

**Event 1 — Receipt of salary:**
- This is income from the contract/service rendered
- For a sole trader (JDG): business income (*przychód z działalności gospodarczej*) recognized on the invoice date[^25]
- For an employee/B2B contractor: income from employment or personal activities (*przychody z działalności wykonywanej osobiście*), recognized when stablecoins arrive in the wallet[^24]
- Valuation: PLN equivalent at the **average exchange rate from the last business day before receipt** (Art. 11a PIT), or at the market rate of the crypto if denominated directly in crypto[^25][^5]
- Tax: standard income tax rate (progressive scale or flat 19% for JDG podatek liniowy) or ryczałt

**Event 2 — Converting USDC to EUR (the taxable crypto disposal):**
- Revenue = EUR amount received × NBP average EUR/PLN rate from last business day before the conversion[^5]
- Cost basis = value of salary recognized as income in Event 1 (prevents double taxation)[^26][^25]
- Net income = Revenue − Cost basis
- Tax = 19% if positive; if negative, the excess rolls forward to the next year on PIT-38[^10]

### 7b. Receiving USDT from Selling ETH (ETH → USDT)

Under current practice (and KIS informal guidance):

- Swapping ETH for USDT = **krypto-krypto exchange** = **neutral tax event**[^14][^7]
- No revenue recognized at the ETH→USDT step
- The cost basis of the ETH **transfers to** the USDT (i.e., USDT inherits ETH's cost basis — the PLN amount you originally paid for the ETH)[^35]
- Taxable event occurs when USDT is converted to EUR or PLN fiat

> **Legal risk note for USDC specifically**: The same analysis applies if you swap ETH for USDC, **but there is an unresolved legal risk** that USDC's EMI status makes this a taxable ETH disposal. If taking a conservative approach: treat the ETH→USDC conversion as disposal of ETH with revenue equal to the USDC amount valued at the mid-market USD rate × NBP USD/PLN rate on the day prior.

### 7c. Converting USDC to USDT (Stablecoin-to-Stablecoin)

**If both USDC and USDT are waluta wirtualna**: This is a krypto-krypto swap → tax-neutral.[^14][^7]

**The legal risk**: If USDC is pieniądz elektroniczny (not waluta wirtualna) and USDT is waluta wirtualna, then swapping USDT for USDC could be treated as a **disposal of USDT** (waluta wirtualna → non-virtual-currency). This would create a taxable event at the USDT/USDC conversion step.

In practice, most practitioners treat this as neutral, consistent with the KIS informal guidance. **However, the USDC EMI problem means this carries genuine legal exposure that differs from USDT↔USDT type swaps.**

### 7d. Binance Auto-Conversions (BUSD → FDUSD → USDC)

Binance's auto-conversion of BUSD to FDUSD and subsequently to USDC was a platform-initiated action affecting EU users. Under current practice:[^16]

- Each conversion step in the chain is a krypto-krypto swap → neutral if all are waluta wirtualna[^7]
- The final conversion to USDC carries the USDC EMI risk described above
- In practice: treat the entire chain as neutral with cost basis inherited from the original BUSD position
- **Keep exchange records showing these were involuntary/automatic conversions**, as this supports the argument that no taxable disposal occurred

### 7e. Transferring USDC Between Wallets (Polygon → Binance)

A mere transfer of USDC from a self-custody wallet on Polygon to your Binance account is **NOT a taxable event**. Transfer between own accounts/wallets does not constitute a disposal (*odpłatne zbycie*). No revenue is recognized.[^4]

***

## 8. Revenue Calculation When Converting Stablecoins to EUR

When you convert USDC or USDT to EUR on Binance or Kraken:

**Revenue = EUR amount received × NBP EUR/PLN average exchange rate from the last business day preceding the conversion date** (Art. 11a ust. 1 PIT)[^5]

**Example**: You convert 6,000 USDC to 5,500 EUR on March 15, 2026. The NBP EUR/PLN rate on March 14 (Friday) is 4.27. Revenue = 5,500 × 4.27 = **23,485 PLN**.

> **Not** the USDC nominal value in USD × NBP USD/PLN rate. The actual EUR received × the EUR/PLN rate is the correct approach, as that is the actual consideration received.[^36][^5]

***

## 9. Cost Basis Determination by Acquisition Method

| Acquisition Method | Cost Basis for PIT-38 | Legal Basis |
|---|---|---|
| **Received as salary (JDG)** | PLN value on invoice (business revenue) | KIS interp. 0114-KDIP3-1.4011.51.2025.1.AK[^25] |
| **Received as salary (employment)** | PLN value at receipt (employment income) | KIS interp. 0115-KDIT1.4011.22.2025.1.MR[^26] |
| **Received as prop trading fee** | PLN value at receipt (personal activity income) | KIS interp. 0115-KDIT1.4011.745.2025.3.MN[^24] |
| **ETH → USDC swap** | Cost basis of the original ETH (carry-through) | Art. 22(14) PIT — neutral exchange retains basis[^35] |
| **Purchased directly with EUR** | EUR amount × NBP EUR/PLN on day before purchase | Art. 11a ust. 1 PIT; Art. 22(14) PIT[^5] |
| **Purchased with PLN** | PLN purchase price | Art. 22(14) PIT[^10] |

**Important**: Exchange commissions paid to acquire or sell virtual currency are **deductible costs** (e.g., Binance trading fees, Kraken withdrawal fees). Costs from krypto-krypto conversions (e.g., ETH→USDC swap fee) are **not** separately deductible — they are subsumed in the neutral exchange.[^8]

***

## 10. Practical Example: 6,000 USDC Salary → EUR

**Scenario**: You receive 6,000 USDC as salary for freelance IT work on Polygon in Q1 2026. The USDC is valued at 4.00 PLN/USDC at the time of receipt (total salary = 24,000 PLN). Later, you convert 6,000 USDC to 5,500 EUR on Binance; the NBP EUR/PLN rate the day before conversion is 4.27 PLN/EUR. Binance charges a 0.1% conversion fee (worth ~55 PLN equivalent).

**Step 1 — At receipt (salary income event):**
- Business income (JDG): 24,000 PLN (recognized, taxed at business rate or ryczałt)
- Cost basis for future PIT-38 calculation: **24,000 PLN**

**Step 2 — At conversion to EUR (crypto disposal event):**
- Revenue: 5,500 EUR × 4.27 = 23,485 PLN
- Cost basis: 24,000 PLN (from salary recognized above)
- Conversion fee: 55 PLN (deductible cost related to disposal)
- Net income: 23,485 − 24,000 − 55 = **−570 PLN (loss)**
- Tax: 0 PLN (loss, not a capital loss per se — the 570 PLN rolls forward to offset future crypto gains)

**Answer to Question 11**: Option **(a)** is closest — it is a crypto disposal with revenue 23,485 PLN and cost 24,055 PLN (including fees), resulting in a carried-forward cost excess of ~570 PLN. This is **not a recognized loss** in the traditional sense — it is an excess of costs that reduces taxable income from crypto disposals in the following year.[^10][^5]

***

## 11. Risk Matrix: USDC vs. USDT

| Transaction | USDT Treatment | USDC Treatment | Risk Level |
|---|---|---|---|
| ETH → USDT swap | Tax-neutral (krypto-krypto) | Tax-neutral (current practice) / **Potential ETH disposal (literal law)** | USDC: **Medium-High** |
| USDT → fiat conversion | Taxable disposal | Taxable disposal | Both: definitive |
| USDC → fiat conversion | N/A | Taxable disposal | Definitive |
| USDC ↔ USDT swap | — | Tax-neutral (practice) / Potential taxable event | **Medium** |
| Binance BUSD→USDC auto-convert | — | Tax-neutral in practice | Low-Medium |
| Transfer between own wallets | Non-taxable | Non-taxable | None |
| Receiving as salary | Income at receipt | Income at receipt | Both: definitive |

***

## 12. What Would Resolve the USDC Problem

The **vetoed implementing law** (Ustawa o rynku kryptoaktywów) contained an explicit provision stating that EMTs remain within the *waluta wirtualna* category for Polish tax purposes unless the taxpayer opts otherwise for accounting reasons. This would have provided:[^37][^21]

- Legal certainty that ETH→USDC swaps remain neutral
- Clear cost-basis inheritance through USDC
- USDC→fiat as the single taxable event

Until a third legislative attempt succeeds (must happen before July 1, 2026) or the Ministry of Finance issues explicit guidance, taxpayers face three options:[^34]

1. **Practical approach (majority practice)**: Treat USDC as waluta wirtualna following KIS informal guidance. Higher legal risk if audited on pre-2026 filings for periods after June 30, 2024.
2. **Conservative approach**: Treat each disposal of a "real" crypto into USDC as a taxable disposal, calculate revenue at the USDC receipt moment. Overpays but creates no audit risk.
3. **Seek a binding interpretacja indywidualna**: Request a formal ruling from KIS specifically addressing whether your USDC transactions constitute waluta wirtualna exchanges. This takes 3 months but provides legal protection.

***

## 13. Summary of Key Legal References

| Legal Source | Relevance |
|---|---|
| Art. 2 ust. 2 pkt 26 Ustawa AML (2018) | Definition of waluta wirtualna |
| Art. 5a pkt 33a Ustawa PIT | PIT reference to AML definition |
| Art. 17 ust. 1 pkt 11 Ustawa PIT | Capital gains from crypto disposal |
| Art. 17 ust. 1f Ustawa PIT | Definition of "disposal" (excludes krypto-krypto) |
| Art. 30b ust. 1a Ustawa PIT | 19% flat rate on crypto gains |
| Art. 22 ust. 14-16 Ustawa PIT | Cost basis rules for virtual currencies |
| Art. 11a ust. 1 Ustawa PIT | NBP rate for FX conversion |
| MiCA Art. 3(1)(7) | Definition of EMT |
| MiCA Art. 48(2) | EMTs are pieniądz elektroniczny |
| Circle/ACPR EMI License | June 30, 2024 — USDC becomes formal e-money in EU |
| KIS 0115-KDIT1.4011.745.2025.3.MN | Stablecoin salary → double tax event (prop trading) |
| KIS 0114-KDIP3-1.4011.51.2025.1.AK | Crypto salary → business income + cost basis |
| KIS 0115-KDIT1.4011.22.2025.1.MR | Employee bonus in crypto → cost basis mechanism |
| KIS verbal response (Feb 2025) | USDT exchange neutral despite MiCA; not binding |
| KIS interpretacja (Mar 2026) | Stablecoin exchange remains neutral; details unconfirmed |

***

*This analysis reflects the legal situation as of March 19, 2026. Tax law in the Polish crypto space is evolving rapidly; obtaining an individual tax ruling (interpretacja indywidualna) is strongly recommended for material transactions. This report is for informational purposes and does not constitute legal or tax advice.*

---

## References

1. [Kryptowaluty a ustawa o przeciwdziałaniu praniu pieniędzy oraz finansowaniu terroryzmu](https://www.fornalik.law/2018/04/11/kryptowaluty-a-ustawa-o-przeciwdzialaniu-praniu-pieniedzy-oraz-finansowaniu-terroryzmu/)

2. [Projekt ustawy o kryptoaktywach a podatki](https://blog-tpa.pl/2024/04/08/projekt-ustawy-o-kryptoaktywach-a-podatki/) - Tylko przykładowo – tokeny będące e-pieniądzem (EMT) będą opodatkowane jak pieniądz elektroniczny (n...

3. [Czy MiCA zamieszała w rozliczeniach podatkowych?](https://paycointax.pl/czy-mica-zamieszala-w-rozliczeniach-podatkowych/) - Czy trzeba rozliczyć wyjście do stablecoinów? Co na to MiCA?

4. [Kompletny przewodnik po rozliczaniu kryptowalut w 2026 ...](https://efekta.waw.pl/kompletny-przewodnik-po-rozliczaniu-kryptowalut-w-2026-roku/) - Dochód ze sprzedaży lub wymiany kryptowalut podlega 19% podatkowi dochodowemu i należy go prawidłowo...

5. [Skutki podatkowe otrzymania nagrody w formie kryptowaluty](https://izbapodatkowa.pl/baza-wiedzy/skutki-podatkowe-otrzymania-nagrody-w-formie-kryptowaluty/) - Przychód ten będzie zaliczony do przychodów z kapitałów pieniężnych. Jak wynika z art. 17 ust. 1 pkt...

6. [Rozliczenie kryptowalut na PIT-38 – jak prawidłowo ...](https://mentzen.pl/blog/inne/kryptowaluty/rozliczenie-kryptowalut-na-pit-38-jak-prawidlowo-rozliczyc-podatek/) - Dochody (lub straty) ze sprzedaży kryptowalut należy rozliczyć na formularzu PIT-38 jako przychody z...

7. [Odpowiedź z Krajowej Informacji Skarbowej dot. ...](https://kryptokancelaria.pl/odpowiedz-z-krajowej-informacji-skarbowej-dot-stablecoinow/) - Stablecoiny, takie jak USDT, wciąż są traktowane jako kryptowaluty, a ich wymiana nie powoduje obowi...

8. [Rozliczenie PIT od przychodów ze sprzedaży kryptowalut](https://www.pitax.pl/wiedza/poradnik-rozliczenia/rozliczenie-pit-od-przychodow-ze-sprzedazy-kryptowalut/) - Sprzedaż kryptowalut (walut wirtualnych) rozliczasz w PIT wtedy, gdy w 2025 doszło do odpłatnego zby...

9. [Jak rozliczyć podatek od dochodów w kryptowalutach?](https://www.fakturaxl.pl/jak-rozliczyc-podatek-od-dochodow-w-kryptowalutach) - Przychód uzyskany ze zbycia kryptowalut podlega pod opodatkowanie podatkiem w stawce 19%. Rozlicza s...

10. [Wydatki poniesione na koparkę wirtualnych walut](https://poradnikprzedsiebiorcy.pl/-wydatki-poniesione-na-koparke-wirtualnych-walut-najwazniejsze-informacje) - Czy wydatki poniesione na koparkę wirtualnych walut mogą zostać rozliczone w kosztach podatkowych? O...

11. [Dlaczego Tether sprzeciwia się regulacjom MiCA?](https://bithub.pl/kryptowaluty/dlaczego-tether-sprzeciwia-sie-regulacjom-mica/) - Tether odrzuca MiCA i opuszcza rynek UE. Dowiedz się, dlaczego największy stablecoin świata stawia n...

12. [USDT, USDC i MiCA – co warto wiedzieć w 2025 r.?](https://kryptoprawo.pl/usdt-usdc-i-mica-co-warto-wiedziec-w-2025-r/) - USDT i USDC pod lupą unijnych przepisów – MiCA wprowadza ograniczenia dla użytkowników kryptowalut, ...

13. [UE zatwierdza licencję MiCA dla 10 emitentów ...](https://cryps.pl/ue-zatwierdza-licencje-mica-dla-10-emitentow-stablecoinow-co-dalej-z-tetherem/) - 10 emitentów stablecoinów zostało zatwierdzonych przez Unię Europejską (UE) na bazie regulacji MiCA....

14. [Podatek od wymiany kryptowalut na stablecoiny - JPK Traders](https://jpktraders.pl/podatek-od-wymiany-kryptowalut/) - Czy wymiana BTC na USDT podlega opodatkowaniu? Poznaj oficjalne stanowisko KIS i dowiedz się, jak ro...

15. [Po tym terminie nie kupimy już Tethera (USDT) w Europie - CrypS.pl](https://cryps.pl/po-tym-terminie-nie-kupimy-juz-tethera-usdt-w-europie/) - Wygląda na to, że zostało nam już tylko kilka tygodni na kupowanie stablecoinów bez licencji MiCa na...

16. [Pamiętaj o MICA: Europejskie giełdy krypto usuwają USDT](https://pl.beincrypto.com/pamietaj-mica-europejskie-gieldy-krypto-usuwaja-usdt/) - Od nowego roku przepisy MICA zmienią zasady gry dla stablecoinów w Unii Europejskiej. Giełdy krypto ...

17. [Circle is First Global Stablecoin Issuer to Comply with MiCA](https://www.circle.com/pressroom/circle-is-first-global-stablecoin-issuer-to-comply-with-mica-eus-landmark-crypto-law) - With this license, both USDC and EURC are now being issued in the EU in compliance with MiCA's regul...

18. [INFO MiCA](https://www.fintech.gov.pl/mica/info-mica)

19. [Advised by De Gaulle Fleurance, Circle obtains approval ...](https://www.degaullefleurance.com/en/actualites/conseille-par-de-gaulle-fleurance-circle-obtient-un-agrement-detablissement-de-monnaie-electronique-eme-aupres-de-lacpr/) - Circle France is now authorized to issue, manage and make available electronic money (and in particu...

20. [Circle lands e-money license. Will mint USDC, EURC ...](https://www.ledgerinsights.com/circle-lands-e-money-license-will-mint-usdc-eurc-mica-compliant-stablecoins-in-eu/) - Circle has been granted an e-money license and has started minting EURC and USDC out of Europe in co...

21. [Podatek od kryptowalut a weto ustawy o rynku kryptoaktywów](https://tomczykowscy.pl/podatek-od-kryptowalut-a-weto-ustawy-o-rynku-kryptoaktywow/) - Bitocina) na USDC rodzi zatem ryzyko opodatkowania 19% podatkiem dochodowym. Ryzyko to nie powinno d...

22. [Masz USDT lub USDC? Skarbówka wydała ważny ...](https://comparic.pl/masz-usdt-lub-usdc-skarbowka-wydala-wazny-komunikat-dla-inwestorow/) - Interpretacja podatkowa potwierdza, że wymiana kryptowalut na stablecoiny, takie jak USDT i USDC, po...

23. [Zamiana kryptowalut na stablecoiny nie podlega podatkowi](https://pl.beincrypto.com/ekspert-prawa-zamiana-kryptowalut-stablecoiny-nie-podlega-podatkowi/) - “W interpretacji indywidualnej wyraźnie wskazano, że wymiana pomiędzy walutami wirtualnymi pozostaje...

24. [Opodatkowanie stablecoinów prop trading: Analiza KIS](https://quark.house/2025/12/16/opodatkowanie-stablecoinow-jako-wynagrodzenia-kiedy-powstaje-przychod-z-prop-tradingu/) - Zrozum opodatkowanie stablecoinów prop trading według KIS (0115-KDIT1.4011.745.2025.3.MN). Analiza p...

25. [Opodatkowanie wynagrodzenia otrzymanego w ...](https://akademialtca.pl/blog/opodatkowanie-wynagrodzenia-otrzymanego-w-kryptowalutach) - Interpretacja podatkowa wskazuje, że wynagrodzenie w kryptowalutach podlega opodatkowaniu w sposób a...

26. [Interpretacja indywidualna - Interpretacja - 0115-KDIT1.4011.22.2025.1.MR](https://www.interpretacje.pl/pit/9758152,interpretacjaindywidualna-interpretacja-0115kdit14011222025.html) - Interpretacja indywidualna z dnia 4 marca 2025 r., Dyrektor Krajowej Informacji Skarbowej, sygn. 011...

27. [Prezydenckie weto do ustawy o rynku kryptoaktywów i jego skutki](https://dudkowiak.pl/blog/prezydenckie-weto-do-ustawy-o-rynku-kryptoaktywow/) - Prezydenckie weto do ustawy o rynku kryptoaktywów wstrzymuje wdrożenie przepisów MiCA w Polsce na ro...

28. [Prezydent wetuje kolejną ustawę. "Przepisy zagrażają ...](https://www.money.pl/gospodarka/prezydent-wetuje-kolejna-ustawe-przepisy-zagrazaja-wolnosciom-polakow-7227855946697632a.html) - Karol Nawrocki zawetował ustawę o rynku kryptoaktywów. "Prezydent korzysta z konstytucyjnej prerogat...

29. [Sejm zagłosował ws. kryptowalut. Prezydent już raz ...](https://www.money.pl/gospodarka/sejm-zaglosowal-ws-kryptowalut-prezydent-juz-raz-zawetowal-ten-projekt-7233730214214144a.html) - Rządowa ustawa o kryptoaktywach ponownie została poddana głosowaniu w Sejmie. W czwartek izba niższa...

30. [Kryptoaktywa 2.0. Senat przyjął, ustawa znów na biurku prezydenta](https://businessinsider.com.pl/prawo/kryptoaktywa-20-senat-przyjal-ustawa-znow-na-biurku-prezydenta/80kbt3y) - Senat przyjął dziś ustawę o kryptoaktywach 2.0. Wprowadzili jedną poprawkę, choć senatorowie PiS chc...

31. [Kryptoaktywa w Sejmie. Posłowie podjęli decyzję](https://businessinsider.com.pl/finanse/kryptoaktywa-w-sejmie-poslowie-podjeli-decyzje/yf7cg56) - Po tym, jak prezydent Karol Nawrocki odrzucił pierwotną wersję ustawy o kryptoaktywach, rząd ponowni...

32. [Kolejne weto prezydenta Nawrockiego. Blokuje ponownie jeden ...](https://businessinsider.com.pl/wiadomosci/karol-nawrocki-ponownie-zawetowal-ustawe-o-kryptowalutach-co-dalej-z-rynkiem/v3emvmz) - Po raz kolejny na styku polityki i nowoczesnych finansów doszło do znaczącego spięcia na krajowej sc...

33. [Prezydent znów blokuje ustawę o kryptowalutach. Rząd zapowiada ...](https://www.gazetaprawna.pl/wiadomosci/kraj/artykuly/10645559,prezydent-znow-blokuje-ustawe-o-kryptowalutach-rzad-zapowiada-ujawnie.html) - Prezydent Karol Nawrocki po raz drugi w ciągu kilku miesięcy zawetował ustawę regulującą rynek krypt...

34. [Koniec polskich giełd kryptowalut? Weto Karola Nawrockiego i ...](https://businessinsider.com.pl/prawo/koniec-polskich-gield-kryptowalut-weto-karola-nawrockiego-i-upor-rzadu-poglebia/ebymkwp) - Polska pozostanie bez rynku krypto, a firmy świadczące usługi w zakresie kryptoaktywów, czyli np. gi...

35. [Ustalenie kosztu uzyskania przychodów z odpłatnego ...](https://akademialtca.pl/blog/ustalenie-kosztu-uzyskania-przychodow-z-odplatnego-zbycia-waluty-wirtualnej) - Dochodem z odpłatnego zbycia walut wirtualnych jest osiągnięta w roku podatkowym różnica między sumą...

36. [Jak rozliczać się z kryptowalut w 2025 roku?](https://www.ifirma.pl/blog/jak-rozliczac-sie-z-kryptowalut-w-2025-roku/) - przychody uzyskiwane z kryptowalut należy zsumować i rozliczać można wyłącznie z przychodami uzyskiw...

37. [Weto dla ustawy o rynku kryptoaktywów - oby korzystne ...](https://www.mddp.pl/weto-dla-ustawy-o-rynku-kryptoaktywow-oby-korzystne-zmiany-podatkowe-wrocily-w-nowej-wersji-przepisow/) - Obecnie polskie przepisy powodują, że emitent tokenów musi zapłacić 19% podatku już przy ich emisji,...

