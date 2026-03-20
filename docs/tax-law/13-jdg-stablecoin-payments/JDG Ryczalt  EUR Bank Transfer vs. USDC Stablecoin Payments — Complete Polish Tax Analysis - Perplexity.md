# JDG Ryczalt: EUR Bank Transfer vs. USDC Stablecoin Payments — Complete Polish Tax Analysis

**Prepared for:** Polish tax resident, JDG (PKD 62.01.B), ryczałt od przychodów ewidencjonowanych 12%, single foreign B2B software development client, existing ~319K PLN crypto cost pool carry-forward.

***

## Executive Summary

Receiving USDC as payment for software development services under a JDG on ryczałt creates **two separate tax layers** — a PIT-28/ryczałt layer (identical to EUR) and a PIT-38 capital gains layer (unique to crypto). However, the specific combination of factors in this case — stablecoins pegged to USD, near-immediate conversion available, and a 319K PLN cost pool carry-forward — means that **Option B (USDC) can be tax-neutral or even marginally advantageous**, at the cost of significantly higher compliance complexity and documentation burden.

The legal framework is confirmed by multiple KIS interpretations, most directly Nr **0113-KDIPT2-1.4011.665.2022.2.MGR** (21 October 2022), which explicitly confirmed that an IT service provider on ryczałt can tax crypto-received service revenue at the applicable ryczałt rate, and Nr **0114-KDIP3-1.4011.540.2023.1.PT** (25 August 2023), reconfirming the same.[^1][^2]

***

## Part 1: Revenue Recognition and Ryczałt Calculation

### 1. Revenue Date and PLN Value for USDC Payments

Under Art. 14(1c) of the PIT Act, the revenue date for business income arises on whichever occurs **first** among: (a) service completion/delivery, (b) invoice issuance, or (c) payment receipt. For a monthly software development engagement, this is typically the invoice date or end-of-period completion date.[^3]

**The PLN value for ryczałt is determined by the invoice face value, not the USDC market rate at transfer time.** If the invoice states 10,000 USD, the ryczałt base is 10,000 USD × NBP average USD/PLN rate from the last business day before the revenue date. The fact that settlement occurs in USDC is treated as a barter payment mechanism — the underlying service value governs, not the token count transferred.[^4][^2][^1]

If the invoice is denominated directly in USDC units (without a USD or EUR peg), then KIS interpretacja Nr **0114-KDIP3-1.4011.51.2025.1.AK** (11 March 2025) governs: the value equals the **arithmetic mean of the opening and closing price on the day preceding the revenue date**, sourced from a reputable market data provider (e.g., CoinMarketCap), first converted to USD, then to PLN via NBP rate. This two-step conversion adds methodological complexity and creates documentation requirements.[^1]

**Practical recommendation:** Invoice in USD or EUR (not USDC units). This makes the PLN base unambiguous — it uses a published NBP rate rather than requiring a methodology judgment call about crypto market data.

### 2. Invoice Currency vs. Payment Medium

The invoice currency (USD or EUR) controls the ryczałt base. The medium of payment (USDC on-chain) is irrelevant to the PIT-28 calculation. The ryczałt is always calculated on the service value stated in the invoice, converted to PLN at the NBP rate from the business day before the revenue date.[^5][^1]

### 3. "Payable in USDC" vs. "Payable in USD (Settled in USDC)"

This framing distinction has practical relevance beyond mere documentation aesthetics:

- **"Payable in USDC":** Creates ambiguity about whether the invoice is a USDC-denominated instrument (requiring crypto market pricing methodology) or a USD-equivalent instrument settled in USDC.
- **"Payable in USD, settlement acceptable in USDC at spot rate":** Makes clear that the obligation is USD-denominated and the crypto is a settlement mechanism. This strengthens the position that NBP USD/PLN is the correct conversion rate and reduces audit risk.

KIS consistently treats crypto payment as barter, but the **barter doctrine does not change the ryczałt base** when the service value is clearly stated in a fiat currency — the fiat amount is the recognized business income.[^6][^5][^1]

### 4. EUR Bank vs. USDC at the Ryczałt Layer: Is There a Difference?

At the ryczałt layer alone, there is **no material difference** — both are 12% on gross PLN-equivalent service revenue. However, important accounting distinctions arise:[^2]

- **EUR bank payments** trigger *różnice kursowe* (FX differences under Art. 24c PIT) between the invoice date rate and the payment date rate, which can increase or decrease ryczałt-level income.[^5]
- **USDC payments do not trigger różnice kursowe** under Art. 24c PIT, because USDC is a waluta wirtualna, not a waluta obca (foreign currency). KIS Interpretacja Nr **0115-KDIT1.4011.25.2024.1.MR** (19 February 2024) explicitly confirmed this. The only "FX" movement in the USDC scenario is handled through the PIT-38 capital gains layer, not the ryczałt layer.[^5]

This is actually a **simplification for ryczałt** — no invoice-to-payment FX reconciliation is needed. The ryczałt base is fixed at the revenue date NBP rate, period.

***

## Part 2: The PIT-38 Layer (Crypto Disposal)

### 5. Double Reporting — Is This Correct for a JDG on Ryczałt?

**Yes, double reporting is mandatory and legally correct.** This is confirmed by the explicit structure of Art. 17(1g) PIT, which states that crypto disposal income is always classified as capital gains (kapitały pieniężne) even when arising within a business context — except for entities whose registered business activity is crypto exchange/intermediation (Art. 2(1)(12) AML Act).[^7][^5]

The two events are fully independent:

1. **PIT-28 (ryczałt):** Recognized at service delivery/invoice date. Base = invoice value in PLN at NBP rate. Tax = 12%. Reported monthly (PPE declaration) and annually.
2. **PIT-38:** Recognized upon disposal of USDC (i.e., exchange to EUR/PLN, payment for goods/services, or any non-crypto-to-crypto transaction). Base = disposal proceeds minus cost basis. Tax = 19%. Reported annually by 30 April of the following year.[^8][^9]

**The ryczałt receipt PLN value becomes the PIT-38 cost basis.** The KIS interpretacja Nr 0114-KDIP3-1.4011.51.2025.1.AK confirmed: "Your expenditure directly incurred on the acquisition of the virtual currency will be the value of the receivable that you recognized as settled by receipt of the virtual currency — i.e., the value of your remuneration due from services rendered". This creates a clean, mirrored structure: if USDC is converted at the same value it was received, the PIT-38 gain is zero.[^1]

### 6. Immediate Conversion — Near-Zero PIT-38 Gain

If USDC is converted to EUR on the same day (or within hours) of receipt, the disposal proceeds in PLN will be virtually identical to the cost basis (the ryczałt-recognized value), with differences limited to:

- Exchange spreads (typically 0.1–0.3% on Binance/Kraken)
- Short-term USD/PLN rate movement between the NBP snapshot (day before) and the actual conversion time
- USDC de-peg risk (historically negligible for USDC, sub-0.1%)

The net PIT-38 income in this scenario is **effectively zero or de minimis**. Any minimal gain would also be offset by the existing 319K PLN cost pool carry-forward (see Part 4).[^5]

### 7. Holding USDC — FX Movement Becomes PIT-38 Taxable

USDC is pegged 1:1 to USD, so its crypto value is stable. However, the USD/PLN exchange rate fluctuates. The PIT-38 gain/loss when converting USDC to EUR is calculated as:

> **PIT-38 income** = (Disposal proceeds in PLN) − (Cost basis in PLN)
> 
> = (USDC quantity × USD/PLN rate at disposal) − (Invoice USD value × USD/PLN rate at revenue date)

If the USD strengthens against PLN between receipt and disposal, this creates a **taxable gain at 19%**. If USD weakens, this creates a loss that is **not a tax loss** (it carries forward as a cost pool for future PIT-38 calculations).[^9][^8]

The direction of this FX risk depends on macroeconomic factors. For a developer expecting to convert relatively quickly, the risk is limited. For a developer holding USDC as a USD-denominated savings vehicle, this creates a meaningful annual PLN-equivalent FX gain/loss that must be tracked and reported.

### 8. USDC → ETH → DeFi: No PIT-38 Disposal Event

A crypto-to-crypto swap (e.g., USDC → ETH) remains **neutral for PIT-38** under current Polish law. Multiple KIS interpretations from 2025–2026 confirmed this position explicitly for USDC and USDT, including a March 2026 confirmation that **despite MiCA's classification of USDC/USDT as e-money tokens, Polish tax law's definition of waluta wirtualna still applies for tax purposes** and the exchange remains neutral.[^10][^11]

This means:
- USDC → ETH: no tax event
- ETH used for DeFi (liquidity provision, lending, etc.): no tax event until ETH is disposed of for fiat/goods
- Only the final fiat exit creates a PIT-38 disposal event

**However:** ETH received as DeFi yield/staking rewards may create a separate PIT-38 income event at receipt (KIS has treated yield/rewards as income at receipt). This is a separate issue from the USDC holding itself.[^12]

***

## Part 3: FX and Accounting Complications

### 9. Różnice Kursowe — EUR vs. USDC

| | EUR Bank Transfer | USDC |
|---|---|---|
| Różnice kursowe (Art. 24c PIT) | **Yes** — arise between invoice NBP rate and payment NBP rate | **No** — explicitly excluded by KIS (USDC is not waluta obca)[^5] |
| Impact on ryczałt base | Yes — FX difference adjusts income/cost | No — ryczałt base is fixed at revenue date |
| Where FX movement appears | Ryczałt layer (income/cost adjustment) | PIT-38 layer only |
| Accounting complexity | Moderate — two-rate system needed | Lower at ryczałt layer; higher overall (PIT-38 added) |

This is a **genuine advantage of USDC at the ryczałt/accounting level** — no FX reconciliation between invoice and payment is needed. The ryczałt amount is locked in at the invoice/service date.

### 10. Ewidencja Przychodów — Recording USDC Payments

The ewidencja przychodów for ryczałt requires: entry date, revenue date, document number, and PLN revenue amount. For USDC payments, the entry should record:[^13]

- **Revenue date:** Service completion or invoice date (NOT the USDC transfer date, unless that is earlier)
- **PLN amount:** Invoice USD/EUR value × NBP rate from last business day before revenue date
- **Document reference:** Invoice number
- **Supporting documentation:** Blockchain transaction hash + on-chain explorer export showing USDC receipt, wallet address, timestamp, and amount

A separate **PIT-38 acquisition log** must also be maintained recording: USDC quantity received, receipt date (actual on-chain date), PLN cost basis (= ryczałt revenue amount), and source (service invoice number). This log is separate from the ewidencja przychodów and is used for PIT-38 filing.[^14]

### 11. VAT — No Difference

The JDG is VAT-exempt under the 200K PLN threshold. Services rendered to a foreign B2B client (outside Poland) are not subject to Polish VAT regardless of payment method — the place of supply is the client's location under the reverse charge mechanism. Neither EUR nor USDC payments create any Polish VAT obligation for this specific setup.[^15]

If and when the JDG exceeds the 200K PLN threshold and registers for VAT, the analysis changes — USDC receipts would still be VAT-exempt financial services when converted (Art. 43(1)(7) VATU), but the double-service nature of crypto payment could create complicating interactions with partial VAT deduction rights. For now, this is not a concern.[^16]

***

## Part 4: Practical Advantages and Disadvantages

### 12. Tax Advantages of USDC (with 319K PLN Cost Pool)

**The 319K PLN carry-forward is the decisive factor that makes Option B potentially superior:**

Under Polish law, the PIT-38 cost pool is a shared "bucket" that aggregates all virtual currency acquisition costs, regardless of coin type, across years. The existing 319K PLN carry-forward means:[^8][^9]

- **Any PIT-38 gains from USDC disposal are immediately absorbed** by the existing cost pool before becoming taxable
- Even if USD/PLN appreciates significantly (e.g., 10% over 6 months on a 50,000 USD receivable = ~21,000 PLN gain), this would still be fully offset
- The developer must **deplete the 319K PLN cost pool before paying any PIT-38 tax** on USDC proceeds, regardless of the FX direction

Additional advantages:

1. **No roznice kursowe complexity at ryczałt level** — ryczałt base is fixed, no invoice-to-payment reconciliation[^5]
2. **Crypto-to-crypto tax deferral option** — USDC can be swapped to ETH for DeFi use without triggering disposal; fiat exit can be timed strategically[^17][^18]
3. **USD exposure** — if PLN weakens vs. USD (common historical trend), holding USDC creates a PLN gain that the cost pool can absorb; this is essentially a free currency hedge for amounts within the 319K PLN buffer
4. **Cost basis recycling** — receiving USDC at ryczałt value creates high cost basis; if USDC is converted near the receipt value, net PIT-38 gain is minimal even without the carry-forward

### 13. Tax Disadvantages and Risks

**Compliance and operational risks:**

1. **PIT-38 filing obligation is perpetual** — even in years with zero disposal, if USDC is acquired (received as payment), PIT-38 costs must be declared. Missing this creates loss of carry-forward rights.[^19][^20]
2. **Dual reporting burden** — monthly PPE ryczałt reports + annual PIT-28 + annual PIT-38. EUR route requires only ryczałt reporting.
3. **Documentation intensity** — blockchain records, on-chain explorer exports, exchange transaction histories, price source archives. Giełdy typically retain data for 1–3 years; archiving must be done proactively.[^14]
4. **Banking friction** — large EUR deposits from crypto exchanges may trigger AML due diligence at the Polish business bank, requiring source-of-funds declarations.[^21]
5. **KIS interpretation stability risk** — MiCA's classification of USDC/USDT as e-money tokens created legal uncertainty in 2025; while KIS confirmed neutral treatment in early 2026, this remains an area of ongoing legal evolution. A policy reversal could retroactively complicate prior-year positions.[^11][^10]
6. **Reclassification risk** — if the developer's crypto activity (DeFi, holding, trading) becomes significant, tax authorities could argue that the crypto handling constitutes a separate regulated activity. This risk is low but not zero for an active DeFi participant.
7. **Smart contract/custody risk** — USDC on-chain carries non-tax risks (contract exploits, wallet security, network-specific risks) absent from bank EUR transfers.

### 14. Existing KIS Interpretations for JDG Ryczałt + Stablecoins/Crypto

The following directly applicable interpretations exist:

| Sygnatura | Data | Kwestia | Trafność |
|---|---|---|---|
| 0113-KDIPT2-3.4011.549.2019.3.PR | 9.01.2020 | Crypto payment = barter, business income | Core doctrine[^2] |
| 0113-KDIPT2-1.4011.665.2022.2.MGR | 21.10.2022 | IT provider on ryczałt + crypto payment = ryczałt applies | **Direct precedent**[^2] |
| 0114-KDIP4-3.4012.652.2022.3.IG | 13.02.2023 | Crypto payment = VAT-exempt financial service | VAT layer[^22] |
| 0114-KDIP2-2.4010.216.2022.4.SP | 13.01.2023 | Crypto invoice payment → cost basis = invoice value | PIT-38 cost basis[^23] |
| 0115-KDIT1.4011.25.2024.1.MR | 19.02.2024 | Crypto ≠ waluta obca, no różnice kursowe | Ryczałt FX layer[^5] |
| 0114-KDIP3-1.4011.540.2023.1.PT | 25.08.2023 | Ryczałt rate applies to crypto-paid services | Confirmed rate[^1] |
| 0114-KDIP3-1.4011.51.2025.1.AK | 11.03.2025 | Price methodology: arithmetic mean open/close | Valuation[^1] |
| KIS March 2026 (reported) | 03.2026 | USDC/USDT = waluta wirtualna despite MiCA; crypto-crypto neutral | **Current stablecoin status**[^10][^11] |

**Important caveat:** No single interpretation addresses the specific combination of: JDG + ryczałt 12% + stablecoins + large cost pool carry-forward + DeFi use of received USDC. Seeking a personal interpretacja indywidualna (KIS ruling) is strongly advisable before committing to Option B at scale.

***

## Part 5: Cash Flow and Banking

### 15. USDC → Exchange → EUR → Bank: Additional Tax Events?

The chain USDC → EUR on exchange → bank withdrawal creates **one PIT-38 taxable event** (the USDC → EUR conversion on the exchange). The EUR withdrawal from exchange to bank account is a **pure cash movement and creates no additional tax event**.[^5]

However, practical banking issues arise:
- Polish banks may treat frequent large EUR inflows from crypto exchanges as AML-flagged. The bank may request a written declaration of source of funds.[^21]
- Maintaining a clear paper trail (service contract → invoice → blockchain receipt → exchange conversion confirmation → EUR SEPA transfer) significantly reduces AML friction.
- For smaller amounts (typical monthly IT invoices of 5,000–15,000 EUR equivalent), this is generally manageable with good documentation.

### 16. AML/VASP Registration — Not Required for This Use Case

**Receiving USDC as payment for software services does NOT require VASP registration.** The Polish AML Act requires registration in the Rejestr działalności w zakresie walut wirtualnych only for entities that provide virtual currency exchange services **to third parties** — i.e., operating as an exchange, crypto-to-fiat conversion service, custodial wallet provider, or brokerage.[^24][^25][^26]

A developer receiving USDC as payment for their own software services, then personally converting it on Binance/Kraken (a registered VASP) for their own account, does not meet any of the four registration-triggering activities. The exchange platforms (Binance, Kraken) hold the VASP registration and bear the AML obligations for the conversion transaction.[^26]

No additional regulatory registration is required.

***

## Complete Tax Journey Comparison

### Option A: EUR via SEPA Bank Transfer

| Step | Action | Tax Event | Complexity |
|---|---|---|---|
| 1 | Invoice issued in EUR | Revenue recognized at NBP EUR/PLN rate (day before) | Low |
| 2 | Client pays EUR (may be days/weeks after invoice) | Różnice kursowe adjustment to ryczałt income | Moderate |
| 3 | EUR hits business bank account | No new tax event | — |
| 4 | Pay ryczałt 12% monthly | Monthly PPE declaration | Low |
| **Annual** | PIT-28 only | One filing | **Simple** |

**FX risk:** Invoice-to-payment EUR/PLN difference adjusts ryczałt base (can be income or cost).

### Option B: USDC On-Chain → Exchange → EUR → Bank

| Step | Action | Tax Event | Complexity |
|---|---|---|---|
| 1 | Invoice issued in USD (payment in USDC) | Revenue recognized at NBP USD/PLN rate (day before) | Low |
| 2 | Client sends USDC on-chain | No ryczałt event (already recognized); USDC acquired with cost basis = ryczałt value | Moderate (record blockchain tx) |
| 3a | Immediate: USDC → EUR on exchange | PIT-38 disposal; gain ≈ 0 (only spread/fees) | Moderate |
| 3b | Delayed: hold USDC weeks/months | No tax event during hold | Low (during hold) |
| 4 | (If delayed) USDC → EUR on exchange | PIT-38 disposal; gain = USD/PLN FX movement × quantity; absorbed by 319K cost pool | Moderate |
| 5 | EUR from exchange → business bank | No tax event | Low |
| 6 | Pay ryczałt 12% monthly | Monthly PPE declaration | Low |
| **Annual** | PIT-28 + PIT-38 | **Two filings** | **Higher** |

**FX risk:** Absorbed by PIT-38 layer and existing cost pool. Within the 319K PLN buffer, no net additional tax even with significant USD/PLN appreciation.

### Total Tax Burden Comparison

| Tax Component | Option A (EUR) | Option B (USDC — immediate) | Option B (USDC — held, USD strengthens) |
|---|---|---|---|
| Ryczałt 12% | ✅ 12% on service revenue | ✅ 12% on service revenue | ✅ 12% on service revenue |
| Różnice kursowe on ryczałt | ±Adjustment (±0.5–2% typical) | ❌ None | ❌ None |
| PIT-38 19% | ❌ None | ~0% (spread only) | **0%** (absorbed by 319K carry-forward) |
| **Effective net tax rate** | **~12% ± small FX adj.** | **~12%** | **~12% (carry-forward eliminates PIT-38)** |
| Net additional compliance cost | Low | Higher | Higher |

For this specific developer, **the net tax burden is virtually identical** across scenarios. The cost pool carry-forward neutralizes any PIT-38 risk that USDC introduces.

### Risk and Compliance Comparison

| Factor | Option A (EUR) | Option B (USDC) |
|---|---|---|
| Compliance forms | PIT-28 only | PIT-28 + PIT-38 |
| Documentation | Invoice + bank statement | Invoice + blockchain records + exchange records + price archives |
| Audit risk | Low (conventional) | Moderate (crypto transactions draw more scrutiny) |
| AML at bank | Normal | Possible enhanced DD for crypto-origin EUR |
| VASP registration | Not required | Not required |
| Legal certainty | Very high | High (good KIS precedents, but MiCA evolution risk) |
| Accounting software | Standard | May need crypto-specific tax tools |
| Recommended action | Straightforward | Maintain meticulous records; consider own KIS ruling |

***

## Practical Recommendation

**For this developer's specific situation, Option B (USDC) is tax-neutral relative to Option A (EUR) and potentially advantageous**, due to the 319K PLN cost pool carry-forward absorbing all foreseeable PIT-38 exposure and the elimination of różnice kursowe complexity at the ryczałt layer.

The recommendation depends on prioritization:

- **If minimizing compliance burden is the priority:** Stay with Option A (EUR). One annual filing, zero crypto tracking, no documentation risk.
- **If leveraging the existing cost pool and USD exposure is valuable:** Switch to Option B. The 319K PLN cost pool can absorb years of PIT-38 gains, effectively making the USDC route tax-equivalent to EUR while adding flexibility for DeFi operations with received funds.
- **If considering Option B:** Invoice in USD (not USDC units), include a clause that "payment acceptable in USDC at market rate equivalent," convert USDC on Binance/Kraken (or similar regulated exchange), and maintain complete blockchain + exchange audit trails. File PIT-38 annually even in zero-gain years to preserve carry-forward rights.
- **Strongly recommended regardless:** Request a personal interpretacja indywidualna from KIS covering the specific facts (JDG, PKD 62.01.B, ryczałt 12%, USDC receipt for IT services, carry-forward cost pool). The fee is ~40 PLN and provides legal protection against future position changes.[^20]

> **Disclaimer:** This analysis is based on publicly available KIS interpretations and Polish tax law as of March 2026. Tax law in the crypto domain is evolving rapidly. This is not formal tax advice; a qualified Polish tax advisor (doradca podatkowy) should review the specific facts before implementation.

---

## References

1. [Kryptowaluta jako środek płatniczy? Skutki podatkowe ...](https://accreo.pl/kryptowaluta-jako-srodek-platniczy-skutki-podatkowe-zaplaty-kryptowaluta-za-towary-lub-uslugi/)

2. [Centrum wiedzy - Płatności za usługi w walutach wirtualnych - KIP](https://izbapodatkowa.pl/baza-wiedzy/platnosci-za-uslugi-w-walutach-wirtualnych/) - Płatności za usługi w walutach wirtualnych

3. [Rozliczenie zapłaty w kryptowalucie na gruncie PIT](https://poradnikprzedsiebiorcy.pl/-jak-wyglada-rozliczenie-zaplaty-w-kryptowalucie) - Czy wiesz, że masz możliwość przyjąć zapłatę w kryptowalutach? Jak zatem wygląda prawidłowe rozlicze...

4. [Po jakim kursie przeliczać transakcje w walucie innej niż PLN ...](https://paycointax.pl/po-jakim-kursie-przeliczac/) - Jaki kurs wymiany wybrać? Jak rozliczać kryptowaluty ... przelicza się na PLN według kursu NBP właśc...

5. [Różnice kursowe a rozliczenie faktury w kryptowalucie](https://poradnikprzedsiebiorcy.pl/-zaplata-w-kryptowalucie-za-fakture-jak-rozliczyc-roznice-kursowe) - Różnice kursowe przy zapłacie w kryptowalucie mogą mieć wpływ na rozliczenia podatkowe przedsiębiorc...

6. [Ustalenie kosztu uzyskania przychodów z odpłatnego zbycia waluty ...](https://akademialtca.pl/blog/ustalenie-kosztu-uzyskania-przychodow-z-odplatnego-zbycia-waluty-wirtualnej)

7. [Otrzymanie należności w wirtualnej walucie a PIT](https://poradnikprzedsiebiorcy.pl/-otrzymanie-naleznosci-w-wirtualnej-walucie-a-przychod-podatkowy) - Przychody z odpłatnego zbycia wirtualnej waluty są zaliczane do osobnego przychodu, jakim jest przyc...

8. [Jak rozliczyć PIT od kryptowalut w 2025 roku?](https://akademialtca.pl/blog/jak-rozliczyc-pit-od-kryptowalut-w-2025-roku) - W Polsce dochody ze sprzedaży kryptowalut są traktowane jako dochody z kapitałów pieniężnych i podle...

9. [Rozliczanie kryptowalut - wszystko co musisz wiedzieć | Blog](https://solidnaksiegowa.com/rozliczanie-kryptowalut-wszystko-co-musisz-wiedziec/) - Dochody z kryptowalut w Polsce rozlicza się za pomocą formularza PIT-38, który należy złożyć do 30 k...

10. [Masz USDT lub USDC? Skarbówka wydała ważny ...](https://comparic.pl/masz-usdt-lub-usdc-skarbowka-wydala-wazny-komunikat-dla-inwestorow/) - Interpretacja podatkowa potwierdza, że wymiana kryptowalut na stablecoiny, takie jak USDT i USDC, po...

11. [Odpowiedź z Krajowej Informacji Skarbowej dot. ...](https://kryptokancelaria.pl/odpowiedz-z-krajowej-informacji-skarbowej-dot-stablecoinow/) - Zgodnie z interpretacją Krajowej Informacji Skarbowej, wymiana kryptowaluty na stablecoina, takiego ...

12. [Przegląd interpretacji podatkowych – wrzesień–grudzień ...](https://kryptokancelaria.pl/przeglad-interpretacji-podatkowych-wrzesien-grudzien-2025/) - Nnajważniejsze interpretacje KIS o kryptowalutach z końcówki 2025. Mt.Gox, airdropy, stablecoiny, ar...

13. [Ewidencja przychodów na ryczałcie – jak prowadzić?](https://mk.rp.pl/blog/ewidencja-przychodow/) - Ewidencję przychodów można prowadzić zarówno w formie elektronicznej (np. za pomocą programu księgow...

14. [Dokumenty potrzebne do rozliczenia kryptowalut - Checklista 2025](https://cryptotax.pl/blog/dokumenty-rozliczenie-kryptowalut.html) - Kompletna lista dokumentów wymaganych do rozliczenia podatku od kryptowalut. Dowiedz się co zachować...

15. [Praca zdalna dla zagranicznego Klienta w IT – co musisz ...](https://umowywit.pl/praca-zdalna-dla-zagranicznego-klienta-w-it/) - Jeśli usługi byłyby świadczone na rzecz klienta z Polski to podatek VAT należałoby doliczyć do kwoty...

16. [Kryptowaluty: zwolnienie z VAT dla sprzedaży kryptowalut. ...](https://moorepolska.pl/kryptowaluty-zwolnienie-z-vat-dla-sprzedazy-kryptowalut-analiza-przepisow-i-praktyczne-zastosowanie/) - Jeżeli miejscem świadczenia usług jest terytorium Polski, wówczas sprzedaż kryptowalut będzie zwolni...

17. [Kompletny przewodnik po rozliczaniu kryptowalut w 2026 roku](https://efekta.waw.pl/kompletny-przewodnik-po-rozliczaniu-kryptowalut-w-2026-roku/) - Rozliczanie kryptowalut w PIT za 2025? Dowiedz się, jak opodatkować przychód z kryptowalut i prawidł...

18. [PIT 38 i kryptowaluty: jak wypełnić (Kompleksowy poradnik)](https://beatcoin.pl/poradniki/pit-38-i-kryptowaluty-jak-wypelnic-kompleksowy-poradnik/) - Dla polskiego urzędu skarbowego USDT, USDC czy DAI to dokładnie takie same kryptowaluty jak Bitcoin ...

19. [Kryptowaluty w PIT-38 za 2025 r. Lepiej zapłać podatek](https://businessinsider.com.pl/prawo/podatki/kryptowaluty-w-pit-38-za-2025-r-lepiej-zaplac-podatek/lq4q8zy) - Ekspert zwraca uwagę, że częstym błędem jest ujmowanie w PIT-38 wyłącznie przychodów z wymiany krypt...

20. [Przegląd interpretacji podatkowych – kryptowaluty pod lupą](https://kryptokancelaria.pl/przeglad-interpretacji-podatkowych-kryptowaluty-pod-lupa/) - Zobacz, jak fiskus interpretuje podatki w przypadku osób związanych z kryptowalutami. Analiza najnow...

21. [Oświadczenie o źródle pochodzenia środków w AML - kiedy składać ...](https://rpms.pl/oswiadczenie-o-zrodle-pochodzenia-srodkow-w-aml-kiedy-skladac-i-jak-jest-oceniane/) - Obowiązujące przepisy o przeciwdziałaniu praniu pieniędzy i finansowania terroryzmu (AML) nakładają ...

22. [Zapłata kryptowalutą to barter i usługa zwolniona z VAT](https://solveoadvisory.pl/zaplata-kryptowaluta-to-barter-i-usluga-zwolniona-z-vat/) - Zdanem fiskusa, zapłata kryptowalutami za świadczone usługi informatyczne jest w istocie transakcją ...

23. [Rozliczenie transakcji pomiędzy stronami poprzez ...](https://isp-modzelewski.pl/serwis/rozliczenie-transakcji-pomiedzy-stronami-poprzez-kryptowaluty-a-skutki-podatkowe-w-podatku-dochodowym-od-osob-prawnych/) - Na gruncie polskiego prawa waluty wirtualnej (kryptowaluty) nie można traktować na równi z prawnym ś...

24. [Handel kryptowalutami w Polsce - Pamiętaj o obowiązku rejestracji!](https://rpms.pl/handlujesz-kryptowalutami-pamietaj-o-obowiazku-rejestracji/) - Od 31 października 2021 r. działalność gospodarcza w zakresie walut wirtualnych stanie się działalno...

25. [Kto musi wpisać się do rejestru działalności w zakresie ...](https://sawaryn.com/publikacje/kto-musi-wpisac-sie-do-rejestru-dzialalnosci-w-zakresie-walut-wirtualnych/) - Pamiętaj o tym, że podmiot, który wykonuje działalność z zakresu walut wirtualnych bez wymaganej rej...

26. [Jak uzyskać licencję na handel walutami wirtualnymi w Polsce (VASP) - Progress Holding](https://progressholding.pl/pl/jak-uzyskac-licencje-na-handel-walutami-wirtualnymi-w-polsce-vasp/) - Potocznie licencja VASP w Polsce na handel walutami wirtualnymi oznacza wpisanie firmy do Rejestru d...

