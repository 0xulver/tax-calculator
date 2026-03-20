Below is the rule set I would use for Polish PIT on crypto today.

The most important structural point is this: Polish crypto PIT is **not** a classic per-disposal lot-matching system. Under **art. 30b ust. 1b**, crypto income is the **annual** difference between the sum of disposal revenues and the costs from **art. 22 ust. 14–16**. Under **art. 22 ust. 15–16**, those costs are taken in the **year they are incurred**, and any unused excess carries forward to later years. That is why a US-style FIFO engine should not be the core of a Polish calculator, even though FIFO does appear in **art. 30b ust. 7–7a**. ([ISAP][1])

## 1) NBP exchange-rate rules

**1. The subsection in your question is slightly off.** The “day before revenue” rule is in **art. 11a ust. 1**, not ust. 2. The key Polish fragments are:

* ust. 1: **„Przychody w walutach obcych przelicza się na złote…”** and **„dzień uzyskania przychodu”**;
* ust. 2: **„Koszty poniesione w walutach obcych…”** and **„dzień poniesienia kosztu”**.
  For crypto, these rules apply when the amount being translated is a **foreign fiat currency amount** such as EUR or USD. They do not turn crypto itself into a foreign currency, and they do not apply to crypto-to-crypto swaps because those are not taxable disposals. ([ISAP][1])

**2. Selling USDC for EUR on Binance/Kraken:** for PIT the relevant concept is **przychód**, not **dochód**. Disposal of a virtual currency for legal tender is a taxable disposal, and MF’s current guidance says the revenue arises at the **moment of disposal**. For a normal spot trade, use the **EUR proceeds** and convert them using the **NBP EUR average rate from the last business day before the disposal date**. A same-day NBP rate is not what art. 11a says. If the trade happens on a Saturday, use Friday’s table; if Friday was not a business day, go back to the last earlier business day. NBP’s Table A is published only on business days, and its archive shows Friday 2026-03-13 followed by Monday 2026-03-16, with no weekend table in between. ([Podatki][2])

**3. USDC received as salary/service payment:** do **not** automatically use the NBP USD rate just because USDC targets USD. Official MF guidance defines a virtual currency as something that is **not legal tender**, and the PIT Act values non-cash benefits by **market value**. So the remuneration should be valued in PLN at the **actual market value of the USDC received** under the rules for the relevant income source. If USDC was at 0.97 USD on that day, use the actual 0.97 market value, not an assumed 1.00. Using an NBP USD rate can be a practical conversion aid only if your market quote is in USD; it is not because USDC is legally USD. For the later art. 30b crypto sale, the strongest practical reading is that the PLN value already taxed as remuneration should become acquisition cost, but the current primary sources I reviewed do not say that expressly for every salary-in-USDC fact pattern. ([Podatki][2])

**4. Crypto purchased with EUR on an exchange:** yes. The PLN crypto cost is the **EUR purchase amount plus any direct purchase fee**, translated using the **NBP EUR average rate from the last business day before the cost was incurred**. Under the current regime, that cost is reported in the **year incurred**, even if the coin is not sold in that year; unused excess carries forward. ([ISAP][1])

**5. So the “last business day before” rule applies on both sides.** Revenue uses **art. 11a ust. 1**; cost uses **art. 11a ust. 2**. The wording is parallel; only the trigger date changes: disposal/revenue date on the revenue side, cost-incurrence date on the cost side. ([ISAP][1])

## 2) What counts as deductible crypto cost

**6. The operative cost rule is in art. 22 ust. 14–16, not in art. 30b itself.** Art. 30b ust. 1b just says annual crypto income is annual revenue minus the costs defined in art. 22 ust. 14–16. The statute says deductible crypto costs are **documented expenditures directly incurred to acquire virtual currency** and **costs related to its sale**. ([ISAP][1])

**Firmly deductible:** the fiat purchase price you paid for the crypto; exchange commissions/trading fees directly attached to purchase or sale; and other documented intermediary fees directly tied to sale. Also note that these costs are taken **when incurred**, not only when the exact units are later sold. ([ISAP][1])

**Firmly non-deductible:** costs not directly connected with acquisition/sale, especially financing costs; costs connected with crypto-to-crypto exchange; mining hardware; and mining electricity. By the same direct-connection logic, **VPN** subscriptions and **hardware-wallet** purchases are on the non-deductible side. ([Podatki][3])

**Grey zone:** exchange withdrawal fees, on-chain gas, and fees paid in crypto. The primary sources I reviewed do not address these items expressly. The safest line is to include them only when you can show they were **directly necessary for a taxable fiat disposal** and are documented; for generic transfers, DeFi operations, staking mechanics, or crypto-to-crypto conversions, the safer answer is no. ([ISAP][1])

**7. Free crypto (airdrop, staking reward):** the official MF page says **odpłatne nabycie** happens only when you **incur expenditure**. Combined with art. 22 ust. 14, that means a **pure free airdrop** has no acquisition expenditure for art. 30b cost purposes, so the literal disposal-basis answer is **0**, not receipt-date market value. Staking rewards are more complicated on the receipt side, but the current primary rules I found still do not create an automatic art. 30b basis equal to market value at receipt. ([Podatki][4])

**8. Crypto received as payment for services / USDC salary:** first tax the receipt under the rules for that income source at its PLN value when received/valued there. The clean economic reading for the later art. 30b sale is to reuse that PLN value as crypto acquisition cost; otherwise the same economic amount can be taxed once as remuneration and again as full crypto-sale proceeds. I did not find current primary text that states this expressly for all remuneration-in-crypto cases, so this is a strong but not entirely risk-free position. ([ISAP][1])

## 3) FIFO

**9. FIFO is not just market practice.** **Art. 30b ust. 7** says that when identification is impossible, FIFO applies, and **art. 30b ust. 7a** extends that rule appropriately to other art. 30b incomes, including crypto income under **ust. 1b**. The caveat is that Polish crypto PIT is still annual and pooled, so FIFO has a much narrower practical role than in classic lot-matching systems. ([ISAP][1])

**10. Per asset or across all crypto?** The act does not expressly say “per asset” for crypto. The safer practical reading is **separate queues by asset** (BTC, ETH, USDC, etc.), not one combined queue across all crypto, because crypto-to-crypto exchanges are non-taxable and different tokens are not the same identifiable property. Treat that as a reasoned practice conclusion, not express statutory wording. ([Podatki][4])

**11. Holdings acquired before becoming Polish tax resident:** I found **no primary-source rule** granting a market-value step-up on the day Polish tax residency begins. The statute points to **documented acquisition expenditure**, not residency-date fair market value, so there is no clear textual basis in the provisions reviewed for a residency-date step-up. Because art. 22 ust. 15–16 are built around the year of incurrence and carryforward, this is one of the areas where an individual interpretation is worth considering if the amounts are large. ([ISAP][1])

**12. Stablecoin auto-conversion (for example BUSD → FDUSD → USDC):** treat it as **non-taxable** if there is no fiat leg, because crypto-to-crypto exchanges are non-taxable. The practical basis treatment is **continuity**: carry the historical acquisition cost through the replacement token and keep a clear audit trail. If there was a conversion fee, current MF guidance points against deducting costs related to crypto-to-crypto exchange. ([Podatki][4])

## 4) Record-keeping

**13. Art. 30b ust. 6 does not currently mention a named “ewidencja walut wirtualnych.”** Current **art. 30b ust. 6 and 6a** require annual PIT-38 reporting of crypto income and crypto costs, including costs in years with no disposal revenue. ([ISAP][1])

**14. The return itself is annual totals, not line-by-line filing.** But because deductible costs must be **documented**, the return separates current-year costs, prior-year unrelieved costs, and current-year unrelieved costs, and exchanges do not have to issue PIT-8C/PIT-11, in practice you need **transaction-level records**. ([ISAP][1])

**15. I did not find an express rule that records must be maintained in real time.** A reconstruction from complete exchange exports and other source documents by filing time should be defensible, provided it is auditable and reconciles to the annual PIT-38 numbers. ([ISAP][1])

**16. CSV exports and trade confirmations are the core evidence, but I would not treat them as the whole file** if there are deposits, withdrawals, wallet transfers, salary/service receipts, staking, airdrops, or auto-conversions. The stronger package is: exchange CSVs, order/trade confirmations, deposit/withdrawal histories, bank statements, wallet/tx-hash logs, fee records, and any invoices/contracts/screenshots needed to prove non-purchase acquisitions and market-value valuations. ([ISAP][1])

**17. Retention period:** keep the records at least until the tax limitation period expires, generally **5 years from the end of the calendar year in which the tax payment deadline expired**. For taxpayers obliged to keep tax books, **art. 86 § 1** expressly ties document retention to that limitation period. So a **2025 PIT** return due in **2026** should normally be kept through **31 December 2031**. ([ISAP][5])

## Worked examples

**Example A — USDC → EUR sale on a Saturday.**
Spot sale on Binance on **Saturday 14 March 2026**: **10,000 USDC** sold for **9,220 EUR**. PLN revenue = **9,220 × NBP EUR Table A from Friday 13 March 2026**. If Binance also charged a **9.22 EUR** sale fee that same day, the PLN sale-cost entry is **9.22 × the same Friday NBP EUR rate**, because the fee is a foreign-currency cost incurred on the sale date. ([Podatki][2])

**Example B — buy crypto with EUR.**
Buy crypto on **Tuesday 11 March 2026** for **5,000 EUR** plus a **20 EUR** trading fee. PLN crypto cost for PIT = **5,020 × NBP EUR rate from Monday 10 March 2026**. You report that cost in **2026**, even if the coin is not sold in 2026; unused excess carries forward. ([ISAP][1])

**Example C — USDC remuneration with a depeg.**
On **11 March 2026** you receive **1,000 USDC** as pay. On that date USDC actually trades at **0.997 USD**. The remuneration should be valued at the **actual market value** of what you received, not at an automatic **1,000 USD**. If you later sell the same **1,000 USDC** for EUR worth **4,050 PLN**, the strongest reading is that only the excess over the PLN value already taxed as remuneration should be taxed again under **art. 30b**; the statute, however, does not spell this out expressly for every remuneration-in-crypto scenario. ([Podatki][2])

**Example D — auto-conversion.**
An exchange auto-converts **1,000 BUSD** into **998 FDUSD** and later **997 USDC**, with no fiat leg. No taxable disposal arises on either conversion. Preserve the **original historical acquisition cost** from the BUSD position and carry it through to the final USDC position; do not create a new PLN basis from the conversion-date stablecoin quote. Any fee tied to the crypto-to-crypto conversion is on the non-deductible side under current MF guidance. ([Podatki][4])

## Minimal practical register format

A defensible crypto register should contain at least: timestamp; platform/wallet; event type (fiat purchase, fiat sale, crypto-to-crypto, transfer, auto-conversion, remuneration, airdrop/staking); asset and quantity out; asset and quantity in; fiat amount and currency; fee amount and fee asset; NBP table/rate used; PLN revenue or PLN cost; source document ID (CSV row, order ID, tx hash); and a flag for whether the item hits PIT-38 now, carries cost forward, or is non-taxable crypto-to-crypto. That is not statutory wording, but it is the minimum structure I would want in order to defend the annual PIT-38 totals. ([Podatki][4])

The two implementation rules that matter most are: **(1)** every foreign-fiat amount uses the **NBP rate from the last business day before the relevant revenue/cost date**, and **(2)** the Polish crypto engine is **annual revenue minus annual documented crypto costs with carryforward**, not a US-style per-disposal FIFO basis engine. ([ISAP][1])

[1]: https://isap.sejm.gov.pl/isap.nsf/download.xsp/WDU19910800350/U/D19910350Lj.pdf "https://isap.sejm.gov.pl/isap.nsf/download.xsp/WDU19910800350/U/D19910350Lj.pdf"
[2]: https://www.podatki.gov.pl/twoj-e-pit/pit-38-za-2025-rok/ "https://www.podatki.gov.pl/twoj-e-pit/pit-38-za-2025-rok/"
[3]: https://www.podatki.gov.pl/podatki-osobiste/pit/informacje-podstawowe/co-jest-opodatkowane/zbycie-kryptowalut/?utm_source=chatgpt.com "podatki.gov.pl - Zbycie kryptowalut"
[4]: https://www.podatki.gov.pl/podatki-osobiste/pit/informacje-podstawowe/co-jest-opodatkowane/zbycie-kryptowalut/ "https://www.podatki.gov.pl/podatki-osobiste/pit/informacje-podstawowe/co-jest-opodatkowane/zbycie-kryptowalut/"
[5]: https://isap.sejm.gov.pl/isap.nsf/download.xsp/WDU19971370926/U/D19970926Lj.pdf "https://isap.sejm.gov.pl/isap.nsf/download.xsp/WDU19971370926/U/D19970926Lj.pdf"
