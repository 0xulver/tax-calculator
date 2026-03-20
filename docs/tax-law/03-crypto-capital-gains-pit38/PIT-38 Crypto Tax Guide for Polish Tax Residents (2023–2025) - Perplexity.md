# PIT-38 Crypto Tax Guide for Polish Tax Residents (2023–2025)

## Executive Summary

Poland taxes cryptocurrency gains at a flat **19%** on profits from the *odpłatne zbycie walut wirtualnych* (paid disposal of virtual currencies). The legal framework, unchanged in substance since January 1, 2019, is anchored in the *ustawa o podatku dochodowym od osób fizycznych* (ustawa o PIT). All reporting flows through **form PIT-38**, with a filing deadline of **April 30** of the following year. Critically, crypto-to-crypto swaps are **tax-neutral**, costs carry forward indefinitely, and crypto gains are **segregated** from all other capital gains (stocks, ETFs) on the same form.

***

## 1. Legal Architecture

### Core Statutory References

| Article | Content |
|---------|---------|
| Art. 5a pkt 33a ustawy o PIT | Definition of *waluta wirtualna* (references AML Act, Art. 2 ust. 2 pkt 26) |
| Art. 17 ust. 1 pkt 11 | *Przychód z odpłatnego zbycia waluty wirtualnej* = capital income |
| Art. 17 ust. 1f | Statutory definition of *odpłatne zbycie waluty wirtualnej* |
| Art. 17 ust. 1g | Even crypto traded within a business is taxed as capital income (PIT-38)[^1] |
| Art. 22 ust. 14–16 | Deductible costs: documented acquisition + disposal expenses[^2] |
| Art. 30b ust. 1a | 19% flat tax on crypto gains[^3] |
| Art. 30b ust. 1b | Tax base = total revenues − costs per Art. 22 ust. 14–16[^4] |
| Art. 30b ust. 6a | Taxpayer must declare costs even in years with zero revenue[^3] |
| Art. 11a ust. 1 | FX conversion rule: NBP average rate from last business day **before** transaction[^5] |
| Art. 45 ust. 1a pkt 1 | Obligation to file PIT-38 annually |

***

## 2. Taxable vs. Non-Taxable Events

### Statutory Definition of *Odpłatne Zbycie*

Under **Art. 17 ust. 1f ustawy o PIT**, *odpłatne zbycie waluty wirtualnej* means:[^1][^6]
- Exchange of virtual currency for **legal tender** (any fiat currency: PLN, EUR, USD, etc.)
- Exchange for **goods**
- Exchange for **services**
- Exchange for **property rights other than virtual currency**
- **Settlement of liabilities** using virtual currency

Critically, exchange of virtual currency for **another virtual currency** is explicitly **excluded** from this definition, making crypto-to-crypto swaps tax-neutral.[^7][^8]

### Event Classification Table

| Transaction Type | Taxable? | Legal Basis | Notes |
|-----------------|----------|-------------|-------|
| Selling BTC/ETH/SOL for EUR or PLN | ✅ Yes | Art. 17 ust. 1f | Main taxable event[^9][^10] |
| Converting USDC to EUR via Binance Convert | ✅ Yes | Art. 17 ust. 1f | EUR is legal tender; USDC is virtual currency[^7] |
| BTC → ETH swap | ❌ No | Art. 17 ust. 1f exclusion | Crypto-to-crypto is neutral[^11][^12] |
| USDT → USDC swap | ❌ No | Art. 17 ust. 1f exclusion | Both are virtual currencies[^7][^13] |
| USDT → USDC → EUR (two-step) | ✅ Yes (step 2 only) | Art. 17 ust. 1f | USDC→EUR triggers tax; USDT→USDC does not[^13] |
| Paying for goods/services with crypto | ✅ Yes | Art. 17 ust. 1f | Value of goods/services = revenue[^9][^6] |
| Sending crypto as a gift | ❌ No (for donor) | Art. 17 ust. 1f (no consideration) | Recipient may owe gift/inheritance tax[^14][^15] |
| Buying crypto with EUR/PLN | ❌ No | — | Generates a deductible cost only[^16][^17] |
| Transferring crypto between own wallets | ❌ No | — | No disposal[^18][^19] |
| Holding crypto | ❌ No | — | No taxable event[^18] |
| Crypto-to-crypto swaps | ❌ No | Art. 17 ust. 1f | This rule applies since 2019[^8][^20] |
| Settling debt with crypto | ✅ Yes | Art. 17 ust. 1f | "Regulowanie innych zobowiązań"[^6] |

> **Important:** The 2019 reform (effective January 1, 2019) fundamentally changed the classification of crypto-to-crypto trades from taxable events to tax-neutral events. This applies to all tax years from 2019 onward, including 2023, 2024, and 2025.[^8][^20]

***

## 3. Staking Rewards

This is the **most contested area** in Polish crypto taxation. Two competing positions exist:[^21][^22]

### Position 1: KIS (Tax Authority) — Taxable at Receipt

The Director of the National Tax Information Office (*Dyrektor KIS*) consistently holds that staking rewards constitute *przychód z praw majątkowych* (income from property rights) under **Art. 18 ustawy o PIT**, taxable upon receipt. Key individual rulings include:[^23][^21]

- **0112-KDIL2-2.4011.146.2024.2.IM** (19 April 2024)[^22]
- **0112-KDIL2-2.4011.234.2025.3.AA** (13 June 2025)[^22]
- **0115-KDIT1.4011.558.2025.2.MK** (10 October 2025)[^22]

Under this approach:
- Value at market price on day of receipt → reported in **PIT-36** (progressive scale: 12% or 32%)[^22]
- At subsequent **disposal**, the previously taxed amount becomes the **cost basis** in PIT-38[^22]
- No double taxation if correctly applied — 12%/32% at receipt + 19% only on appreciation after receipt[^22]

### Position 2: Administrative Courts — Taxable Only at Disposal

Regional Administrative Courts (*WSA*) and the Supreme Administrative Court (*NSA*) increasingly rule that staking rewards do **not** generate income within the meaning of the PIT Act upon receipt:[^21]

- WSA Poznań, 9 April 2024 (I SA/Po 434/24)[^21]
- WSA Wrocław, 6 December 2023 (I SA/Wr 413/23)[^21]
- NSA, 22 March 2022 (II FSK 1688/19)[^21]

Under this approach: staking is treated as primary acquisition of virtual currency; taxable event arises **only upon disposal** in PIT-38 at 19% flat rate.[^21]

### Practical Recommendation

| Scenario | Approach | Risk Level |
|----------|----------|------------|
| File PIT-36 + PIT-38 (KIS-aligned) | Tax at receipt + cost basis at disposal | **Low** (follows authority) |
| File only PIT-38 at disposal | Tax only at sale | **Medium** (supported by courts, but disagreement with KIS) |
| Do nothing | — | **High** (non-compliance) |

**Conservative advice:** Follow the KIS position (tax at receipt, PIT-36) to avoid disputes. If staking rewards were not taxed on receipt in prior years, obtain an individual ruling (*interpretacja indywidualna*) before disposal.

**Cost basis of staking rewards (under KIS approach):** Equal to the market value declared as income at receipt. Under the court approach: zero cost basis (no payment was made to acquire them).[^13][^24]

***

## 4. Airdrops

The KIS position is that crypto received through airdrops constitutes income (*przychód z innych źródeł*) under **Art. 10 ust. 1 pkt 9** and **Art. 20 ust. 1** at the market value on the day of receipt, taxed under the general progressive scale and reported in **PIT-36**. The value on receipt day becomes the cost basis at disposal.[^5]

However, the practical guidance from multiple sources notes that KAS guidance on airdrops is **limited**. Where tokens were received with zero commercial activity (unsolicited airdrops), some practitioners treat them as non-taxable upon receipt with a zero cost basis at disposal. This is a **higher-risk** approach.[^24][^25][^13]

**Cost basis of airdrops:** Under the conservative (KIS-aligned) approach = fair market value on receipt day. Under the permissive approach = zero PLN.[^13][^24]

***

## 5. Interest Income (CeFi/DeFi Lending)

Interest earned from crypto lending on platforms such as Binance Simple Earn, Celsius (when operational), or DeFi protocols (Aave, Compound) is treated as **capital income** subject to 19% tax, analogous to other crypto-asset income. This is income upon receipt at fair market value.[^26]

There is **no specific KAS guidance** on DeFi interest as of 2025. Practitioners generally recommend treating it similarly to staking rewards — report in PIT-36 at receipt value, with that value becoming the cost basis at disposal. The absence of formal guidance makes an *interpretacja indywidualna* advisable for significant DeFi income positions.[^27]

***

## 6. Platform Collapse Losses (Celsius, BlockFi, Terra/UST)

### The Core Problem

When a platform collapses, no *odpłatne zbycie* (disposal) has occurred — the crypto was not sold or exchanged. As a result, the loss itself is **not a deductible event**. There is no specific Polish statutory mechanism to write off locked or lost crypto.[^28]

### Recovery and Subsequent Sale

If funds are **recovered** following bankruptcy/liquidation proceedings and subsequently sold:

- The sale **is taxable** at 19% in PIT-38[^29]
- The **original acquisition cost** is fully deductible, even if the purchase occurred before 2019[^29]
- Documentation required: bank transfer records to the platform that collapsed; exchange transaction history[^29]
- Individual ruling reference: Director of KIS, 21 November 2024, **0114-KDIP3-1.4011.619.2024.2.AK**[^29]

### Terra/UST and Total Loss

For completely worthless tokens (Terra/LUNA collapse where tokens became worthless): no disposal, no deduction. The cost basis is "stranded" and can only be deducted when/if a taxable disposal occurs. If the token can be sold even at a near-zero price on any exchange, selling it formally crystallizes the loss.

***

## 7. Cost Basis Rules

### No Statutory FIFO Requirement for PIT-38

Under the PIT framework for individuals (Art. 22 ust. 14–16 ustawy o PIT), costs are deducted **in the year incurred**, not matched to specific units sold. There is **no legal basis** for applying FIFO under the 2019+ regime for PIT-38 filers:[^30][^31]

> *"Przy rozliczaniu kosztów uzyskania przychodów z obrotu kryptowalutą brak jest podstaw prawnych do stosowania metody FIFO"* — KIS official guidance[^31]

The Polish system uses an **annual cost pool approach**:
- All acquisition costs incurred in the year go into the cost pool
- The cost pool is deducted against the year's crypto revenues
- If costs > revenues, the **excess carries forward** to the next year (Art. 22 ust. 15–16)[^2][^32]
- Unused cost pools are not time-limited — they accumulate until offset against future gains[^32]

> **Practical implication:** You do not need to calculate which specific coins were sold. Instead, add up all crypto acquisition costs paid in the year and all crypto sale revenues, then subtract. No per-transaction gain/loss calculation is required (or permitted) on PIT-38.[^33][^34]

### What Is Deductible (Art. 22 ust. 14)

| Cost Type | Deductible? | Notes |
|-----------|-------------|-------|
| Purchase price of crypto (fiat purchase) | ✅ Yes | Core cost[^7][^35] |
| Exchange trading fees (buy commissions) | ✅ Yes | Directly linked to acquisition[^11][^12] |
| Exchange trading fees (sell commissions) | ✅ Yes | Costs related to disposal[^11][^12] |
| Withdrawal fees (exchange to wallet) | ✅ Likely | If documented and linked to acquisition/disposal[^36] |
| Network gas fees | ✅ Likely | If directly linked to taxable acquisition/disposal[^36] |
| Mining equipment / electricity | ❌ No | Explicitly excluded[^7][^35] |
| Costs of crypto-to-crypto swaps | ❌ No | No Polish legal basis[^37][^38] |
| Loan/credit used to buy crypto | ❌ No | Financing costs excluded[^35] |
| Staking-related infrastructure costs | ❌ Unclear | No KAS guidance |

### NBP Exchange Rate for Foreign Currency Transactions

All EUR/USD/other foreign currency amounts must be converted to PLN using the **NBP average exchange rate from the last business day before the transaction date** (Art. 11a ust. 1 ustawy o PIT).[^11][^5]

Example: BTC sold on March 15, 2024 for €5,000 → use NBP EUR/PLN rate from March 14, 2024 (or March 13 if March 14 is a non-business day).

***

## 8. Pre-Residency Cost Basis

### Key Court Ruling

**WSA Warsaw, 29 August 2024 (III SA/Wa 1290/24)** — A landmark ruling for anyone who moved to Poland and holds crypto purchased abroad:[^38]

> Costs of acquiring cryptocurrencies incurred **before becoming a Polish tax resident** may be included in the PIT-38 cost pool, **provided those costs were not already deducted as tax costs in another country**.

### Application to the Sweden-to-Poland Migration (2023)

- Crypto purchased in Sweden before 2023 using fiat (EUR/SEK): **Original purchase cost is deductible** in Polish PIT-38 in the year of disposal, provided no Swedish CGT deduction was claimed[^38]
- Crypto acquired via crypto-to-crypto swaps while in Sweden: **NOT deductible** in Poland — Polish law does not recognize such swap costs regardless of whether they were taxed in Sweden[^38]
- Cost should be expressed in PLN using the NBP rate applicable on the purchase date[^11]
- Disposals made **after establishing Polish tax residency** (2023+) are fully taxable in Poland regardless of where the crypto was acquired[^38]

### Swedish Tax Treaty Consideration

The Poland–Sweden double taxation treaty may apply if Swedish CGT was paid on transactions before Polish residency was established. However, the WSA in the above ruling did not analyze the treaty dimension — **individual advice is recommended** for significant cross-border positions.

***

## 9. FIFO Per-Asset vs. Cross-Asset Pooling

Because Poland does **not** require FIFO, the question of per-asset vs. cross-asset accounting does not arise in the same way as in the UK or US. Costs and revenues are tracked **per category (virtual currencies as a whole)**, not per individual coin. This means:[^33][^2]

- BTC costs + ETH costs + SOL costs all pool together
- BTC revenues + ETH revenues + SOL revenues pool together
- The net of all these is reported in PIT-38 Part E as a single income/loss figure[^34][^33]

***

## 10. PIT-38 Form — Crypto-Specific Fields

### Form Structure Overview

PIT-38 has **two separate capital gains sections**:[^39]

| Section | Legal Basis | Applies To |
|---------|-------------|------------|
| **Part C** | Art. 30b ust. 1 | Stocks, ETFs, bonds, derivatives, investment funds |
| **Part E** | Art. 30b ust. 1a | **Crypto (walutywirtualne) only** |

**Crypto gains and losses cannot be combined with or offset against stock gains and losses**.[^40][^7]

### Part E — Field-by-Field Guide (PIT-38 for 2025, filed by April 30, 2026)

Source: Official *Broszura informacyjna do zeznania PIT-38* za rok 2025, Ministerstwo Finansów[^39]

| Field | Name | What to Enter |
|-------|------|---------------|
| **Poz. 36** | Przychody z odpłatnego zbycia walut wirtualnych (2025) | Total aggregated revenues from all taxable crypto disposals in 2025 (in PLN) |
| **Poz. 37** | Koszty uzyskania przychodów poniesione w 2025 r. | Total documented acquisition + disposal costs paid in 2025 (in PLN) |
| **Poz. 38** | Koszty z lat ubiegłych nieodliczone | Amount from **prior year's PIT-38, field 38/40** — undeducted cost surplus carried forward |
| **Poz. 39** | Dochód | Income = Poz.36 − (Poz.37 + Poz.38), if positive |
| **Poz. 40** | Nadwyżka kosztów | Excess costs = (Poz.37 + Poz.38) − Poz.36, if costs exceed revenues; carries to next year's Poz.38 |

### Part F — Tax Calculation on Crypto

| Field | Content |
|-------|---------|
| **Poz. 41** | Tax base = Poz.39 (rounded to whole PLN) |
| **Poz. 42** | Tax rate: **19%** |
| **Poz. 43** | Tax = Poz.41 × 19% |
| **Poz. 44** | Foreign tax paid (deductible with proportional limit; requires PIT/ZG attachment) |
| **Poz. 45** | Tax due = Poz.43 − Poz.44 |

### Multi-Year Cost Carryforward Example

| Year | Revenues | Costs (current year) | Carried-forward costs | Net income | Poz.40 (carry fwd) | Tax |
|------|----------|---------------------|----------------------|------------|-------------------|-----|
| 2023 | 0 | 50,000 | 0 | 0 | 50,000 PLN | 0 |
| 2024 | 80,000 | 10,000 | 50,000 | 20,000 | 0 | 3,800 PLN |
| 2025 | 30,000 | 5,000 | 0 | 25,000 | 0 | 4,750 PLN |

> In 2023, only purchases were made — PIT-38 must still be filed showing Poz.40 = 50,000 PLN.[^16][^17][^41]

### Prior Year Loss Carryforward: Crypto vs. Stocks

Unlike stock losses (which follow Art. 9 ust. 3 rules in Part C/D of PIT-38), **crypto excess costs are not losses in the traditional sense** — they are simply **undeducted costs** that roll forward automatically without a 5-year time limit and without the 50% annual cap that applies to stock losses.[^42][^3][^32]

***

## 11. Reporting: Aggregated Totals, Not Individual Transactions

The PIT-38 form requires **only aggregated annual totals**, not a transaction-by-transaction listing. The taxpayer is responsible for maintaining underlying records, but only the totals appear on the declaration.[^18][^34][^33]

You do **not** need to:
- List individual buy/sell transactions
- Identify which coins were sold
- Match specific lots to disposals

You **do** need to:
- Correctly aggregate all revenues from taxable disposals
- Correctly aggregate all deductible costs incurred in the year
- Apply the correct NBP FX rates for foreign-currency transactions

***

## 12. Documentation Requirements

### What Must Be Kept

Art. 30b ust. 6 ustawy o PIT requires taxpayers to demonstrate the accuracy of costs and revenues. The following documents should be retained:[^41][^43][^29]

- **Exchange transaction histories** — Binance and Kraken CSV exports (all trades, deposits, withdrawals)
- **Bank statements** showing transfers to/from exchanges
- **Receipts/confirmations** of crypto purchases
- **Exchange fee statements**
- **Self-custody wallet transaction records** (on-chain tx hashes with timestamps and amounts)
- For pre-2019 or pre-residency acquisitions: original purchase confirmations and bank transfers

### No Formal *Ewidencja Walut Wirtualnych* Required

There is **no statutory requirement** for individuals to maintain a formal *ewidencja walut wirtualnych* (virtual currency register) akin to a trading book. Art. 30b ust. 6 imposes an obligation to be able to substantiate cost deductions with documentation, but the form of that documentation is flexible.[^3][^2]

**Exchange CSV exports (Binance, Kraken) are generally sufficient** evidence, provided they clearly show: date, transaction type, amounts, fees, and asset names.[^30][^29]

### Retention Period

The Polish statute of limitations for tax matters is generally **5 years** from the end of the calendar year in which the tax liability became due (*Ordynacja podatkowa*, Art. 70). Retain all records accordingly. For costs incurred before becoming a Polish resident (e.g., 2020–2022 in Sweden), retain original documentation indefinitely since they may be used in future Polish filings.

***

## 13. Separation of Crypto from Other Capital Gains

**This is one of the most important practical rules.** Crypto is taxed in a completely separate sub-category:[^7][^40]

- **Crypto gains CANNOT offset stock losses** (and vice versa)
- **Crypto losses (excess costs) can ONLY be carried forward against future crypto income**
- Stocks/ETFs/derivatives are in **Part C** (Art. 30b ust. 1)
- Crypto is exclusively in **Part E** (Art. 30b ust. 1a)
- No *kwota wolna od podatku* (tax-free allowance) applies to crypto[^17][^44]

***

## 14. Filing Deadline and Submission

- **Filing window:** February 15 – **April 30** of the following year[^9][^18][^41]
- **Automatic acceptance:** If the taxpayer does not act on the pre-filled *Twój e-PIT* return by April 30, it is automatically accepted — but this pre-filled version likely **will not include crypto** correctly, as PIT-8C information from exchanges is not comprehensive. Always review and manually update.[^39]
- **Filing methods:** Paper form, e-Deklaracje desktop app, Twój e-PIT online portal[^33]
- **Attachment:** If foreign taxes were paid on crypto abroad, attach **PIT/ZG** (one per country)[^39]
- **Tax payment deadline:** Same as filing — April 30[^41]
- Tax periods: The obligation applies for each calendar year in which the taxpayer was a Polish tax resident (2023, 2024, 2025)[^10][^12]

***

## 15. Summary Classification for Specific Activities

### Complete Event Reference for the Described Portfolio

| Activity | Taxable Event? | Tax Treatment | Form | Notes |
|----------|---------------|---------------|------|-------|
| Buying crypto with EUR | No | Deductible cost | PIT-38, Poz. 37 | Report cost even without sales[^16] |
| Selling crypto for EUR | Yes | 19% CGT | PIT-38, Poz. 36 | Use NBP rate day before[^11] |
| BTC → ETH swap | No | Tax-neutral | — | Not reported on PIT-38[^7] |
| USDC → USDT | No | Tax-neutral | — | Both are virtual currencies[^13] |
| USDC → EUR | Yes | 19% CGT | PIT-38, Poz. 36 | EUR = fiat[^7] |
| DOT/ETH/SOL staking rewards | Contested | KIS: PIT-36 at receipt; Courts: PIT-38 at disposal | PIT-36 or PIT-38 | Get interpretacja indywidualna[^21][^22] |
| Airdrops | Contested | KIS: PIT-36 at receipt | PIT-36 | Conservative: report at receipt[^5][^13] |
| Binance Simple Earn interest | Contested | Similar to staking treatment | PIT-36 (conservative) | No formal KAS ruling[^26] |
| Celsius/BlockFi locked funds | No (yet) | No deduction until disposal | — | Deduct original cost when recovered + sold[^29] |
| Terra/UST total loss | No | No deduction mechanism | — | Crystallize by nominal sale if possible[^28] |
| Sending crypto as gift | No (for donor) | Recipient may owe gift tax | — | Not odpłatne (no consideration)[^14] |
| Inter-wallet transfers | No | — | — | Own wallet to own wallet[^18] |
| Withdrawal fees | Likely yes | Deductible cost | PIT-38, Poz. 37 | Documented, linked to disposal[^36] |
| Gas fees | Likely yes | Deductible cost | PIT-38, Poz. 37 | If directly tied to taxable event[^36] |
| Crypto bought pre-residency (Sweden) | N/A (purchase) | Cost deductible in year of disposal | PIT-38, Poz. 37 | Only if not deducted in Sweden[^38] |

***

## 16. Key Risks and Practical Warnings

- **Sanction rate of 75%:** Failure to report or deliberate tax fraud can trigger a punitive 75% tax rate — confirmed by multiple Polish tax authorities[^16]
- **DAC8 data sharing:** From January 1, 2026, all EU crypto asset service providers (including Binance and Kraken) must report customer data to EU tax authorities, including KAS. Polish residents' trading data on major exchanges will become visible to KAS[^36][^33]
- **Twój e-PIT pre-fill is unreliable for crypto:** The pre-filled form only includes data from PIT-8C information statements. Crypto exchanges do not systematically file PIT-8C in all cases — manually verify and complete Part E[^39]
- **Annual filing obligation even without sales:** If crypto was only purchased in 2023, 2024, or 2025, a PIT-38 must still be filed declaring the acquisition costs in Poz. 37 to preserve them for future carryforward[^17][^16]
- **Staking rewards pre-2025:** For DOT, ETH, SOL staking rewards received in 2023–2024 that were not reported in PIT-36, consider a corrective declaration or an individual tax ruling to establish the correct position[^23][^22]

***

*This guide is informational. Tax law may change and individual circumstances vary — consult a qualified Polish tax advisor (doradca podatkowy) for individual situations, especially regarding pre-residency assets, significant staking positions, and cross-border tax treaty analysis.*

---

## References

1. [Otrzymanie należności w wirtualnej walucie a PIT](https://poradnikprzedsiebiorcy.pl/-otrzymanie-naleznosci-w-wirtualnej-walucie-a-przychod-podatkowy) - W myśl art. 17 ust. 1f ustawy PIT przez odpłatne zbycie waluty wirtualnej rozumie się wymianę waluty...

2. [Rozliczenie sprzedaży kryptowalut a podstawa ...](https://poradnikprzedsiebiorcy.pl/-rozliczenie-sprzedazy-kryptowalut-jak-ustalic-podstawe-opodatkowania) - W przypadku sprzedaży kryptowalut podstawą opodatkowania jest dochód, czyli różnica pomiędzy przycho...

3. [Art. 30b. pod. dochod. fiz. - Ustawa o podatku dochodowym od osób ...](https://lexlege.pl/ustawa-o-podatku-dochodowym-od-osob-fizycznych/art-30b/) - Art. 30b. pod. dochod. fiz. - Ustawa o podatku dochodowym od osób fizycznych - 1. Od dochodów uzyska...

4. [Opodatkowanie kryptowalut i kryptoaktywów podatkiem ...](http://www.witoldsrokosz.pl/pl/blog/opodatkowanie-kryptowalut-i-kryptoaktywow-podatkiem-dochodowym-od-osob-fizycznych) - W praktyce nie ma jednolitego podejścia do pojęcia kryptowalut, czasami jest ono stosowane tylko dla...

5. [Skutki podatkowe otrzymania nagrody w formie kryptowaluty](https://izbapodatkowa.pl/baza-wiedzy/skutki-podatkowe-otrzymania-nagrody-w-formie-kryptowaluty/) - Jeżeli waluta wirtualna zostanie wymieniona na walutę tradycyjną, inną niż złoty, wartość przychodu ...

6. [podatki.gov.pl - PIT-38 za 2025 rok](https://www.podatki.gov.pl/twoj-e-pit/pit-38-za-2025-rok/) - W zeznaniu podatkowym za rok 2025 możesz wykazać stratę poniesioną w latach: 2020, 2021, 2022, 2023 ...

7. [Cryptocurrency tax in Poland: PIT-38 explained for investors - MDDP](https://www.mddp.pl/pit-settlements-for-cryptocurrencies-and-related-tax-obligations/) - Every person who sold or purchased cryptocurrencies in 2024 should declare the income or expenses in...

8. [Waluty wirtualne a podatek PIT](https://kryptoprawo.pl/waluty-wirtualne-a-podatek-pit/) - Po zmianie przepisów przychody z obrotu walutami wirtualnymi rozliczamy jako przychody z kapitałów p...

9. [Jak rozliczyć kryptowaluty w Polsce? PIT-38 za 2025](https://jpktraders.pl/jak-rozliczyc-kryptowaluty-w-polsce-pit-38-2025/) - Obowiązek podatkowy dotyczy każdej osoby fizycznej, która w 2025 roku dokonała odpłatnego zbycia wal...

10. [Cryptocurrency tax in Poland in 2025 – rules and settlement](https://poland-accounting.eu/2025/09/cryptocurrency-tax-in-poland-in-2025-rules-and-settlement/) - Cryptocurrency tax in Poland is 19% – learn about settlement rules, deductible costs and when the ta...

11. [How to settle cryptocurrencies in the PIT for 2024?](https://bttp.pl/en/aktualnosci/jak-rozliczyc-kryptowaluty-w-pit-za-2024-rok/) - Practical tips from Krzysztof Burzyński, tax advisor and partner at BTTP. Settling cryptocurrencies ...

12. [How to settle cryptocurrencies in the PIT for 2024?](https://bttp.pl/en/aktualnosci/how-to-settle-cryptocurrencies-in-the-pit-for-2024/) - A Polish tax resident must report global income, including cryptocurrencies. If tax was paid abroad,...

13. [A Crypto Tax Guide for Poland](https://nexo.com/pl/blog/a-crypto-tax-guide-for-poland) - Useful information about crypto taxes in Poland.

14. [How to tax a cryptocurrency donation?](https://www.nexiaadvicero.eu/en/how-to-tax-a-cryptocurrency-donation/) - Cryptocurrencies, with Bitcoin at the forefront, have revolutionized the financial world since their...

15. [Poland Crypto Tax Guide 2026 - Kryptoskryptos.io › guides › poland-crypto-tax-guide-2026](https://kryptos.io/guides/poland-crypto-tax-guide-2026) - Our 2026 Poland crypto tax guide reveals common mistakes traders make, and how to avoid costly mis-c...

16. [Kryptowaluty w PIT-38 za 2025 r. Lepiej zapłać podatek](https://businessinsider.com.pl/prawo/podatki/kryptowaluty-w-pit-38-za-2025-r-lepiej-zaplac-podatek/lq4q8zy) - Nawet jeśli w 2025 r. wyłącznie kupowałeś kryptowaluty (bez ich sprzedaży), to trzeba ująć w zeznani...

17. [Crypto Tax in Poland: 2025 Guide | Dudkowiak & Putyra](https://www.dudkowiak.com/blog/crypto-tax-in-poland-2025-guide/) - Discover Poland’s 2025 crypto tax regulations: Understand the 19% flat tax on gains, reporting oblig...

18. [Poland crypto tax guide 2025 - Latest KAS updates - Kraken](https://www.kraken.com/fr/learn/poland-crypto-tax-guide) - Learn more about the latest crypto tax guidance in the Poland with the Kraken Learn Center.

19. [Poland crypto tax guide 2025 - Latest KAS updates](https://www.kraken.com/learn/poland-crypto-tax-guide) - Learn more about the latest crypto tax guidance in the Poland with the Kraken Learn Center.

20. [Cryptocurrency tax in Poland in 2025 – rules and settlement - getsix](https://getsix.eu/getsix-blog/accounting-hr-payroll-tax-and-legal-alerts-poland/taxes-and-law-in-poland/cryptocurrency-tax-in-poland-in-2025-rules-and-settlement/) - Cryptocurrency tax in Poland is 19% – learn about settlement rules, deductible costs and when the ta...

21. [Staking of Virtual Currencies and Personal Income Tax (PIT)](https://blog-tpa.pl/2025/10/24/staking-of-virtual-currencies-and-personal-income-tax-pit/) - One of the key issues remains whether staking rewards constitute income subject to personal income t...

22. [Jak opodatkowany jest staking i airdropy w Polsce?](https://divly.com/pl/przewodniki/staking-i-airdropy-podatek) - Zdaniem KIS już samo otrzymanie tokenów jest traktowane jako dochód w rozumieniu ustawy o PIT. Krypt...

23. [Opodatkowanie nagród uzyskiwanych w procesie stakingu](https://kancelaria-skarbiec.pl/otrzymanie-kryptowaluty-w-ramach-stakingu-czy-trzeba-zaplacic-podatek/) - Jednym z kluczowych zagadnień jest opodatkowanie nagród uzyskiwanych w procesie stakingu, czyli mech...

24. [A Crypto Tax Guide for Poland](https://nexo.com/blog/a-crypto-tax-guide-for-poland) - Useful information about crypto taxes in Poland.

25. [How to Save Crypto Tax in Poland - Kryptoskryptos.io › blog › how-to-save-crypto-tax-in-poland](https://kryptos.io/blog/how-to-save-crypto-tax-in-poland) - Discover practical strategies to save crypto tax in Poland in 2026. Learn how to legally minimise yo...

26. [Cryptocurrency Taxation](https://kancelaria-skarbiec.pl/en/cryptocurrency-taxation/) - C.​​ Interest earned from cryptocurrency lending qualifies in most jurisdictions as taxable income u...

27. [Podatek Od Kryptowalut - Wszystko Co Musisz Wiedzieć w 2026 🟠](https://www.youtube.com/watch?v=zYkPJ1yujWA) - Podatki od kryptowalut nie muszą być skomplikowane - poradnik A-Z z Maciej Grzegorczyk
🟠 Rozlicz swo...

28. [Reporting crypto losses from Bankrupt Exchanges - CoinTracker](https://www.cointracker.io/blog/reporting-losses-related-to-bankrupt-exchanges) - You may be able to deduct losses related to insolvent exchanges when bankruptcy & other court procee...

29. [Rozliczenia PIT od kryptowalut – obowiązki podatkowe ...](https://www.mddp.pl/rozliczenia-pit-od-kryptowalut-i-obowiazki-podatkowe-z-tym-zwiazane/) - Jakie są obowiązki podatkowe dotyczące rozliczenia PIT od kryptowalut? Jak w rozliczeniach tych mogą...

30. [0113-KDIPT2-1.4011.518.2017.10.AP - AnyLawyer](https://anylawyer.com/interpretacje-podatkowe/sposob-ustalenia-kosztow-uzyskania-przychodu-w-zwiazku-z-transakcjami-sprzedazy-kryptowalut-pytanie-nr-3-oraz-dokumentowanie-transakcji-nabycia-i-sprzedazy-kryptowalut-pytanie-nr-4--0113-kdipt2-1-4011-518-2017-10-ap) - Koszty uzyskania przychodu z tytułu nabycia kryptowaluty należy rozpoznawać w momencie ich poniesien...

31. [Skutki podatkowe obrotu kryptowalutami w PIT, VAT i PCC](https://www.kis.gov.pl/wiadomosci/aktualnosci/-/asset_publisher/JSs9/content/id/7793320) - W rocznym PIT należy wykazać również przychody ze sprzedaży lub zamiany kryptowalut, takich jak m. i...

32. [Rozliczenie PIT od przychodów ze sprzedaży kryptowalut](https://www.pitax.pl/wiedza/poradnik-rozliczenia/rozliczenie-pit-od-przychodow-ze-sprzedazy-kryptowalut/) - Sprzedaż kryptowalut (walut wirtualnych) rozliczasz w PIT wtedy, gdy w 2025 doszło do odpłatnego zby...

33. [Poland Crypto Tax Guide 2025 [Podatek od Kryptowalut] | Koinly](https://koinly.io/guides/crypto-tax-poland/) - How is crypto taxed in Poland? We've got everything you need to know in our Poland Crypto Tax Guide ...

34. [Podatek od kryptowalut – jak rozliczyć PIT-38 kryptowaluty ...](https://pl.beincrypto.com/learn/podatek-od-kryptowalut/) - W sekcji E tego formularza musisz wpisać przychód uzyskany ze sprzedaży kryptowalut w rubryce 34. Na...

35. [Cryptocurrency tax in Poland in 2025 – rules and settlement](https://successful-investing-in-poland.com/cryptocurrency-tax-in-poland-in-2025-rules-and-settlement/) - Cryptocurrency tax in Poland is 19% – learn about settlement rules, deductible costs and when the ta...

36. [Cryptocurrencies In Poland | Intertax](https://polishtax.com/cryptocurrencies-in-poland/) - For individuals, Poland applies a flat 19% tax on profits from disposal of virtual currencies, typic...

37. [How to report crypto taxes in Poland (PIT)](https://divly.com/en/guides/polish-crypto-tax-filing-guide) - Learn how to report cryptocurrency in your Polish PIT return, online or on paper. A clear, beginner-...

38. [Obrót kryptowalutami – jak opodatkować w przypadku ...](https://www.nexiaadvicero.eu/obrot-kryptowalutami-jak-opodatkowac-w-przypadku-zmiany-rezydencji-podatkowej-istotny-wyrok-wsa/) - W rozliczeniu PIT-38 można wykazać koszty nabycia kryptowalut poniesione przed nabyciem rezydencji p...

39. [Broszura do PIT-38 za 2025 r.pdf](https://www.podatki.gov.pl/media/g5ebnm2e/broszura-do-pit-38-za-2025-r.pdf) - Broszura do PIT-38 STR. 7. Część E. DOCHÓD/KOSZTY – ART. 30B UST. 1A USTAWY. Część E wypełniają poda...

40. [Jak rozliczać się z kryptowalut w 2025 roku?](https://www.ifirma.pl/blog/jak-rozliczac-sie-z-kryptowalut-w-2025-roku/) - Już od 2019 roku rozliczanie kryptowalut odbywa się na podstawie “nowych” zasad, które wymagają skła...

41. [Jak wypełnić PIT-38 przy rozliczaniu kryptowalut? | Blog](https://solidnaksiegowa.com/jak-wypelnic-pit-38-przy-rozliczaniu-kryptowalut/) - Kto musi wypełnić PIT-38? · sprzedały kryptowaluty, uzyskując dochód/stratę, · wymieniły kryptowalut...

42. [Tax Poland How to Settle | MotaPl on Binance Square](https://www.binance.com/en/square/post/33391936722769) - I remind you 2026. Settling losses from cryptocurrencies in PIT-38 – how to do it for the year 2025....

43. [Rozliczenie kryptowaluty w PIT-38: obowiązki, koszty i ...](https://kurdynowski.com.pl/rozliczenie-kryptowaluty-w-pit-38-obowiazki-koszty-i-przychody/) - Dowiedz się, jak poprawnie wypełnić rozliczenie kryptowalut w formularzu PIT-38, aby uniknąć problem...

44. [Kryptowaluty a PIT – czy należy je rozliczać? Jak to wygląda?](https://e-stargard.pl/wiadomosci/pokaz/27332,kryptowaluty-a-pit-czy-nalezy-je-rozliczac-jak-to-wyglada) - Nie da się ukryć, że liczba zwolenników handel kryptowalutami stale rośnie.

