# Tax Treatment of Celsius & BlockFi Losses — Polish Tax Perspective (with Swedish Residency Context)

## Executive Summary

This report analyzes the Polish (and residually Swedish) tax treatment of funds lost or partially recovered from the Celsius Network and BlockFi bankruptcies. The core finding is that **Polish tax law provides no direct mechanism to claim a "loss" from a platform bankruptcy before a disposal event has actually occurred**. Instead, original acquisition costs carry forward indefinitely as a deductible cost base to offset future disposal revenue. The situation is complicated by the change in tax residency (Sweden → Poland), and by the Swedish tax agency's (Skatteverket) specific guidance that lending to Celsius constituted a disposal in Sweden at the moment of transfer.

***

## 1. Polish Crypto Tax Framework: The Basics

Since 2019, Poland's PIT Act (art. 17 ust. 1 pkt 11) classifies income from virtual currency trading as capital income, subject to a flat 19% rate, reported on the annual **PIT-38** form. A taxable "disposal" (*odpłatne zbycie*) is narrowly defined in art. 17 ust. 1f as:[^1][^2]

- Exchange of virtual currency for **fiat money** (PLN, EUR, USD, etc.)
- Exchange for **goods, services, or non-crypto property rights**
- **Settling liabilities** with virtual currency

Crucially, crypto-to-crypto swaps are explicitly **not** taxable events. Transferring crypto between one's own wallets is also tax-neutral.[^3][^4][^5]

***

## 2. Is Depositing to Celsius/BlockFi a Taxable "Disposal"? (Q3)

### Polish Law Position

Under strict Polish PIT interpretation, depositing BTC or DOT to a custodial platform like Celsius or BlockFi **does not constitute a taxable disposal** (*odpłatne zbycie*), because it is not an exchange for fiat, goods, services, or non-crypto rights. The official tax authority portal (podatki.gov.pl) confirms the disposal definition is limited to fiat or goods exchange. Polish tax law does not treat a custody deposit as a sale.[^6]

This means: **no taxable event occurred in Poland when you deposited BTC/DOT to Celsius or BTC to BlockFi.** The original purchase cost basis is preserved and carries with the asset.

### Swedish Law Position (Critical Difference)

Skatteverket took a materially different view. According to published Swedish tax authority guidance, **lending crypto to Celsius was treated as a disposal at the moment of transfer** — the depositor was deemed to have sold the assets, now holding only a *claim* against Celsius. This means:[^7]

- Swedish residents who deposited to Celsius in the Earn program must report a capital gain/loss for the year of transfer (2020–2022, depending on when the deposit was made)
- The subsequent claim against Celsius is treated as a separate financial instrument
- That claim can only be written off as a loss when it is formally "disposed of" — which requires a declared bankruptcy of a limited company or cooperative, not merely a Chapter 11 restructuring[^7]

**Since Celsius entered Chapter 11 restructuring** (not a final liquidation bankruptcy), Skatteverket's position was that Swedish residents could **not yet** write off the Celsius claim loss as of 2022–2023.[^8][^7]

***

## 3. When Does the Loss Crystallize for Tax Purposes? (Q2)

### Polish Perspective

Polish law does not explicitly address when a loss from a bankrupt crypto exchange is recognized. Based on KIS rulings and practitioner guidance, the operative tax moment is the **disposal event** — i.e., when recovered assets are eventually sold or used to purchase something. At that point:

- The recovery distribution is treated as taxable revenue (akin to a forced sale on your behalf)[^9]
- The **original acquisition cost** of the deposited crypto is deductible against that revenue[^2]

The KIS ruling on Mt.Gox (2025) is the closest precedent: KIS refused to characterize the recovery as tax-exempt compensation, and instead treated it as a crypto disposal at 19%. The taxpayer can deduct original purchase costs.[^10][^9]

There is **no recognized taxable loss event** under Polish law at any of these moments:
- When the platform files for bankruptcy
- When the platform stops allowing withdrawals
- When a court formally approves a restructuring plan

The loss becomes financially quantifiable (and deductible in the cost basis sense) only when a final **partial or full distribution** is received and the assets are subsequently sold, or when recovery becomes formally and permanently impossible with court finalization.

### Swedish Perspective (for 2022 Events)

Under Swedish law (applicable when the taxpayer was a Swedish resident):
- If Celsius deposits were treated as a disposal in Sweden, the capital gain/loss calculation should have been reported for the **year of transfer** (i.e., the year the BTC/DOT was deposited)
- The loss on the Celsius *claim* itself can only be deducted once the claim is formally disposed of — which requires a final bankruptcy declaration, not a Chapter 11 process[^7]
- Sweden taxes at 30% with 70% of losses deductible[^11]

***

## 4. Can Losses Be Claimed in Poland? (Q1)

### The "Nadwyżka Kosztów" Mechanism (Not a True Loss Deduction)

Poland's PIT law contains a **structural prohibition** on carrying forward crypto losses in the traditional sense. Art. 9 ust. 3a pkt 2 explicitly states that the loss carryforward provisions of art. 9 ust. 3 do **not** apply to income from virtual currency disposal. This is a key distinction.[^12][^13]

However, a related mechanism does exist: when **deductible costs exceed revenues** in a given year, the excess (*nadwyżka*) is **not a "loss" but rather a cost carried forward** to the following tax year under art. 22 ust. 16. This accumulates year over year until sufficient disposal revenue is recognized.[^14][^15]

**Practical implication:** If you originally paid PLN 100,000 for BTC later deposited to Celsius, and later recovered only PLN 30,000 worth through the bankruptcy, you would:
1. Report PLN 30,000 as disposal revenue (year of recovery sale)
2. Deduct PLN 100,000 as acquisition cost
3. Have PLN 70,000 of excess costs → this rolls forward to offset future crypto disposal income

### Fraud/Theft Analogy — A Warning

In 2025, KIS ruled that stolen crypto cannot generate a deductible loss, because the loss arises from third-party criminal action rather than a legitimate tax-generating activity. This restrictive view *could* theoretically be applied to a bankruptcy loss by analogy if KIS takes the position that no "disposal" occurred. The risk is real, though a bankruptcy (unlike theft) involves a formal legal process with documented creditor claims — which is a stronger evidentiary position.[^9]

### Can 2022 Swedish-Resident Losses Be Claimed in Poland? (Q4)

**In general: No — losses that occurred (or were recognizable) under Swedish tax residency belong to Swedish tax law, not Polish.** Poland taxes residents on worldwide income from the date of Polish tax residency. A loss that arose in Sweden (e.g., the Celsius deposit disposed of under Swedish rules) is a matter for Skatteverket, not KAS.

The Poland-Sweden double taxation treaty prevents the same income from being taxed twice, but it does not allow Polish residents to claim Swedish-origin losses in their Polish PIT-38. If you were required to report a capital gain from the Celsius deposit in your Swedish K4 return (for the year of deposit), and later incur a loss on the Celsius claim, that loss must be pursued through Swedish tax proceedings — specifically by filing an amended return or open claim (*öppet yrkande*) in Sweden.[^16]

**However**, if the acquired BTC/DOT cost basis was established before you became a Polish tax resident, and the *disposal event* (receiving bankruptcy distributions and selling them) occurs *while you are a Polish resident*, you can deduct the original acquisition costs on your Polish PIT-38 for the year of that disposal — even if the purchase predates your Polish residency. The MDDP guidance explicitly confirms that documented costs from before the current tax year (even pre-2019) can be used.[^2]

***

## 5. FIFO Implications (Q5, Q6, Q7)

### Poland's Actual Cost Method

Poland does **not** officially mandate FIFO for crypto. The PIT Act uses an aggregate costs approach: all documented acquisition costs for virtual currencies are pooled together and matched against total disposal revenues in a given year. This is confirmed by MDDP, a leading Polish tax firm. The "FIFO" label seen in some Polish crypto calculators is a simplification of the cost-matching logic, not a statutory requirement.[^17][^2]

### Practical FIFO/Cost Basis Treatment for Celsius/BlockFi

| Scenario | Recommended Treatment |
|---|---|
| **Fully unrecovered BTC/DOT** (no distribution yet received) | Keep the original acquisition cost in the cost pool. Report as *excess costs* (nadwyżka) each year, rolling forward. Do NOT remove from cost base. |
| **Partial recovery received** (e.g., 30% returned) | When you sell/use the recovered 30%, report that as disposal revenue. Apply the *full* original cost of those coins as deductible cost. The remainder (70%) stays in the cost pool pending further distributions or formal loss crystallization. |
| **Permanently unrecoverable (court confirms zero recovery)** | This is the hardest case. With formal court documentation confirming zero recovery, there is an argument for recognizing a disposal at zero proceeds, which creates a large cost/revenue imbalance — handled as carried-forward excess costs. No KIS ruling directly addresses this yet. |

### Treating Celsius/BlockFi Holdings Pending Resolution

The recommended approach under current Polish law is **(c): treat as a cost pool entry pending resolution**, not a completed disposal. Do not remove the lots from your cost pool and do not treat them as consumed. Each year, report the unrealized acquisition cost as part of your total cost pool. When (if) you receive distributions and sell them, the full original costs offset the disposal proceeds.

***

## 6. Partial Recovery: How to Adjust FIFO/Cost Basis (Q6)

When partial bankruptcy distributions are received and subsequently sold:

1. **Identify the original acquisition cost** (in PLN at the exchange rate on the date of purchase) of the BTC deposited to Celsius/BlockFi
2. **Report the distribution proceeds** as disposal revenue in the PIT-38 for the year you receive and sell (or exchange for fiat) the recovery assets
3. **Deduct the full original acquisition cost** for those coins
4. If costs > proceeds, the **excess carries forward** (art. 22 ust. 16) — this is not a loss carryforward (banned under art. 9 ust. 3a pkt 2), but a cost basis carryforward[^12][^14]

> **Example:** 1 BTC purchased for PLN 150,000. Deposited to Celsius. Received 0.3 BTC back from bankruptcy in 2024 (market value PLN 80,000). Sold the 0.3 BTC for PLN 80,000.
>
> Revenue = PLN 80,000
> Deductible cost = PLN 150,000 (full original cost of 1 BTC)
> Excess = PLN 70,000 → carried forward as costs for 2025 crypto disposals

***

## 7. Documentation Requirements (Q8)

To support any cost deductions related to Celsius/BlockFi in a PIT-38 filing, the following documentation should be retained:

- **Original purchase documentation** — bank transfers used to buy BTC/DOT, exchange receipts, invoices showing purchase price in PLN at acquisition date[^18][^2]
- **Transfer records** — blockchain transaction history showing movement of BTC from self-custody wallets to Celsius/BlockFi platform addresses
- **Platform account statements** — Celsius/BlockFi account screenshots or CSV exports showing holdings at date of bankruptcy filing
- **Bankruptcy court documents** — U.S. Bankruptcy Court filings for Celsius (Case No. 22-10964, SDNY) and BlockFi (Case No. 22-19361, D. NJ), including the plan of reorganization and distribution notices
- **Distribution notices** — any communications from the Celsius/BlockFi estate showing the amount and date of partial distributions
- **Wallet address documentation** — matching your known deposit addresses (provided in the query) to on-chain history is important for provenance

Without documented acquisition costs, KAS may reject any cost deduction claim.[^2]

***

## 8. PIT-38: Specific Reporting Mechanics (Q9)

There is **no dedicated field or checkbox for "platform bankruptcy losses"** on the PIT-38 form. The relevant reporting approach is:

- **Revenue section (Przychody):** Report any fiat proceeds from selling bankruptcy distribution assets in the year received
- **Costs section (Koszty uzyskania przychodów):** Enter the documented acquisition cost of the original deposited crypto in the year the disposal occurs — even if the purchase was made years earlier
- **Excess costs / Nadwyżka kosztów (carry-forward field):** If costs > revenue in any given year, report the excess in the designated carry-forward line of the PIT-38 (this field allows unused costs to roll to the following year's PIT-38 automatically)[^15][^14]

In years where no disposal occurs (you're still awaiting distributions), **you may still be required to file PIT-38** to report accumulated acquisition costs even without revenue — this preserves the cost pool in the tax system.[^19][^2]

***

## 9. Swedish Tax Obligations: Residual Considerations

If the taxpayer's Celsius deposits were made while a Swedish tax resident, and Skatteverket's interpretation applies (deposit = disposal), then:
- A Swedish K4 capital gain/loss calculation may be required for the year(s) of deposit
- Loss on the Celsius *claim* (not the crypto) can only be deducted in Sweden once the formal bankruptcy is finalized and the claim disposed of[^7]
- Swedish losses cannot be claimed on a Polish PIT-38[^16]
- The Poland-Sweden tax treaty (based on OECD model) allocates capital gains taxation to the country of residence at the time of the disposal[^20][^16]

It is strongly recommended to consult a Swedish tax specialist (or file an *öppet yrkande* open claim with Skatteverket) to preserve the option of claiming the Celsius claim loss in Sweden when it crystallizes.

***

## 10. Key Risks and Uncertainties

| Issue | Risk Level | Notes |
|---|---|---|
| KIS applying theft-loss logic to bankruptcy (no deduction) | Medium | Theft ruling [^9] is analogous but not identical; bankruptcy involves formal legal proceedings |
| No KIS ruling directly on Celsius/BlockFi | High | The Mt.Gox ruling is closest precedent but not binding |
| Swedish disposal treatment being unrecognized in Poland | High | Poland won't accept Swedish-law disposal events as Polish taxable events |
| Cost pool challenge for pre-2019 acquisitions | Low-Medium | MDDP confirms pre-2019 costs can be used; KIS occasionally challenges this [^2] |
| PIT-38 filing even with no disposal revenue | Medium | Required to preserve cost carry-forward; missing filings may lose cost basis rights |
| Partial recovery triggering full cost deduction in one year | Low | Structurally allowed under art. 22 ust. 14–16; need documentation |

***

## Conclusion and Recommended Actions

1. **Do not remove Celsius/BlockFi cost basis from your cost pool.** Under Polish law, no disposal has occurred yet (unless you received and sold bankruptcy distributions). Keep the original acquisition costs in your annual PIT-38 cost reporting.

2. **When bankruptcy distributions are received and sold**, report them as disposal revenue and deduct the full original acquisition cost. If costs exceed proceeds, the surplus carries forward.

3. **There is no direct "loss deduction" available** under Polish law for platform bankruptcies in the traditional sense. The closest mechanism is the cost-forward (nadwyżka), which is not technically a loss but achieves a similar economic result over time.

4. **For Swedish-period Celsius deposits:** consult a Swedish tax advisor. Skatteverket's position that the deposit was a disposal creates separate Swedish tax obligations that cannot be substituted by Polish tax treatment.

5. **File PIT-38 every year** to report and preserve your cost pool, even in years with zero disposal events.

6. **Obtain an individual tax ruling (interpretacja indywidualna) from KIS** regarding the specific bankruptcy scenario. This provides legal protection against KAS challenges and is especially warranted given the substantial amounts involved and the lack of explicit KIS guidance on Celsius/BlockFi specifically.

7. **Retain all documentation** — purchase records, transfer records, platform statements, and bankruptcy court filings — to substantiate cost claims during any future KAS audit.

---

## References

1. [Crypto Taxes in Poland 2026 | CoinW Academy](https://www.coinw.com/academy/articles/crypto-taxes-poland/203) - Learn how crypto is taxed in Poland in 2026, including the 19% tax rate, reporting rules, and NFT & ...

2. [Cryptocurrency tax in Poland: PIT-38 explained for investors](https://www.mddp.pl/pit-settlements-for-cryptocurrencies-and-related-tax-obligations/) - Every person who sold or purchased cryptocurrencies in 2024 should declare the income or expenses in...

3. [Poland crypto tax guide 2025 - Latest KAS updates - Kraken](https://www.kraken.com/fr/learn/poland-crypto-tax-guide) - Learn more about the latest crypto tax guidance in the Poland with the Kraken Learn Center.

4. [Poland crypto tax guide 2025 - Latest KAS updates](https://www.kraken.com/learn/poland-crypto-tax-guide) - Profits from disposing of crypto for PLN or spending crypto are taxed at 19%. Taxpayers report aggre...

5. [Poland Crypto Tax Guide 2025 [Podatek od Kryptowalut] | Koinly](https://koinly.io/guides/crypto-tax-poland/) - How is crypto taxed in Poland? We've got everything you need to know in our Poland Crypto Tax Guide ...

6. [podatki.gov.pl - Zbycie kryptowalut](https://www.podatki.gov.pl/podatki-osobiste/pit/informacje-podstawowe/co-jest-opodatkowane/zbycie-kryptowalut/) - Przychodem z odpłatnego zbycia są przychody uzyskane z tytułu wymiany waluty wirtualnej na prawny śr...

7. [Sweden Crypto Tax Guide 2026](https://kryptos.io/guides/sweden-crypto-tax-guide) - New regulations and stricter reporting mean wrong filings can get you fined. Use our Sweden crypto t...

8. [Sweden Crypto Tax 2025: A Complete Guide](https://www.weex.com/learn/articles/sweden-crypto-tax-2025-a-complete-guide-5882) - Cryptocurrency continues to reshape how Swedes save, invest, and conduct transactions in 2025. Yet,

9. [Przegląd interpretacji podatkowych – kryptowaluty, maj- ...](https://kryptokancelaria.pl/przeglad-interpretacji-podatkowych-kryptowaluty-w-2025/) - Przegląd najnowszych interpretacji podatkowych KIS dotyczących kryptowalut w 2025 roku. Sprawdź, jak...

10. [Odszkodowanie za upadek giełdy kryptowalut jest bez PIT](https://www.gazetaprawna.pl/podatki/artykuly/10781599,odszkodowanie-za-upadek-gieldy-kryptowalut-jest-bez-pit.html) - Polacy, którzy otrzymają odszkodowanie za kradzież bitcoinów z japońskiej giełdy walut wirtualnych, ...

11. [Income tax return and taxation of cryptocurrency in Sweden](https://skeppsbronskatt.se/en/2022/01/21/income-tax-return-and-taxation-of-cryptocurrency-in-sweden/) - Consequently, one has to declare capital gains and losses, in a K4-form, which is to be attached to ...

12. [Strata z handlu wirtualną walutą - jak rozliczyć?](https://poradnikprzedsiebiorcy.pl/-czy-strata-z-handlu-wirtualna-waluta-musi-byc-wykazana-w-deklaracji-rocznej) - W tym zakresie opodatkowaniu 19% stawką podatku podlega dochód będący różnicą pomiędzy przychodem a ...

13. [Opodatkowanie kryptowalut i kryptoaktywów podatkiem ...](http://www.witoldsrokosz.pl/pl/blog/opodatkowanie-kryptowalut-i-kryptoaktywow-podatkiem-dochodowym-od-osob-fizycznych) - W praktyce nie ma jednolitego podejścia do pojęcia kryptowalut, czasami jest ono stosowane tylko dla...

14. [Rozliczenie sprzedaży kryptowalut a podstawa ...](https://poradnikprzedsiebiorcy.pl/-rozliczenie-sprzedazy-kryptowalut-jak-ustalic-podstawe-opodatkowania) - Rozliczenie sprzedaży kryptowalut wiąże się z koniecznością opodatkowania dochodu. Jak prawidłowo ob...

15. [Rozliczenie PIT od przychodów ze sprzedaży kryptowalut](https://www.pitax.pl/wiedza/poradnik-rozliczenia/rozliczenie-pit-od-przychodow-ze-sprzedazy-kryptowalut/) - Nadwyżka kosztów nad przychodami przechodzi na następny rok i powiększa koszty w kolejnym rozliczeni...

16. [Cryptocurrency and Capital Gains – Poland 2026 | TaxRaven](https://taxravens.com/en/poland/crypto-investments) - Poland has one of Europe's clearest crypto tax systems: 19% flat tax on gains. No distinction betwee...

17. [Your Complete Crypto Tax Guide for Poland](https://nexo.com/pl/blog/a-crypto-tax-guide-for-poland) - Useful information about crypto taxes in Poland.

18. [Crypto Tax in Poland: 2025 Guide](https://www.dudkowiak.com/blog/crypto-tax-in-poland-2025-guide/) - Income from the sale of virtual currencies is taxed at a flat rate of 19%. There are no applicable d...

19. [Cryptocurrency tax in Poland in 2025 – rules and settlement](https://poland-accounting.eu/2025/09/cryptocurrency-tax-in-poland-in-2025-rules-and-settlement/) - Cryptocurrency tax in Poland is 19% – learn about settlement rules, deductible costs and when the ta...

20. [Tax Residency and Crypto Reporting in Poland](https://www.8lends.io/blog/tax-residency-and-crypto-reporting-in-poland) - Many crypto traders decide to just file taxes in whatever country they like. This isn't going to fly...

