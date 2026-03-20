# Tax Treatment of DeFi, Staking, and Airdrops in Poland
### A Comprehensive Guide for Complex Crypto Activities Under Polish PIT Law

***

## Executive Summary

Polish crypto tax law is currently in a state of **active interpretive conflict** between the tax authority (KIS – Krajowa Informacja Skarbowa) and the administrative courts (WSA). For most activities covered below — staking, airdrops, earn programs — KIS consistently requires taxation **at the moment of receipt** under PIT-36 (prawa majątkowe, art. 18 PIT), while multiple WSA judgments from 2023–2024 hold that **tax arises only upon disposal** (art. 17 ust. 1f PIT, PIT-38). This tension creates genuine legal risk regardless of the position chosen. Each section below presents both positions with citations and a practical recommendation.

**Core statutory framework:**
- **Art. 17 ust. 1 pkt 11 + art. 30b PIT** — taxable event on "odpłatne zbycie" (disposal) of virtual currencies at 19%, reported in PIT-38
- **Art. 17 ust. 1f PIT** — definition of disposal: exchange for legal tender, goods, services, or non-crypto property rights, or settlement of obligations
- **Art. 22 ust. 14–16 PIT** — cost basis = documented acquisition costs; excess costs carry forward to next year
- **Art. 9 ust. 3a pkt 2 PIT** — crypto losses cannot be offset against other income sources; carry-forward applies only within crypto/capital gains bucket
- **Art. 18 + art. 11 ust. 2/2a PIT** — KIS's legal hook for taxing receipt of rewards as "przychód z praw majątkowych"

***

## 1. Staking Rewards

### The Core Legal Dispute

The central question — whether receiving staking tokens is itself a taxable event — remains unresolved at the statutory level.

**KIS position (most recent interpretations through October 2025):** Receiving staking rewards creates immediate income (*przychód z praw majątkowych*) under art. 18 PIT, valued at market price on the date of receipt converted to PLN. This must be reported in **PIT-36** and taxed at progressive rates (12% or 32%). At disposal, the previously-taxed value becomes a **cost of acquisition** in PIT-38, preventing double taxation. KIS confirmed this in interpretations: 0112-KDIL2-2.4011.146.2024.2.IM (19 April 2024), 0112-KDIL2-2.4011.234.2025.3.AA (13 June 2025), and 0115-KDIT1.4011.558.2025.2.MK (10 October 2025).[^1][^2]

**WSA position (consistent in 2023–2024 judgments):** Art. 17 ust. 1f PIT comprehensively regulates crypto taxation and limits taxable events to *odpłatne zbycie* (disposal). Receipt of staking rewards is not disposal; the legislature deliberately chose to tax only the exit event, not acquisition. Taxing receipt would also require a valuation methodology that does not exist in statute — a violation of the *zasada określoności* (legal certainty principle). Key cases: WSA Wrocław (December 2023), WSA Warszawa III SA/Wa 179/24 (March 2024).[^3][^4][^5]

### Practical Tax Mechanics

| Approach | Tax Form | Timing | Rate | Cost Basis at Sale |
|----------|----------|--------|------|--------------------|
| **KIS (receipt taxed)** | PIT-36 (prawa majątkowe) | Year of receipt | 12% or 32% progressive | FMV on receipt date = acquisition cost in PIT-38 |
| **Court (sale-only)** | PIT-38 (kapitały pieniężne) | Year of sale | 19% flat | Zero cost basis — full proceeds taxable |

**The "nabycie walut wirtualnych" question (Q2):** KIS treats staking rewards as a new acquisition (*nabycie*) of a virtual currency, but does **not** count them as costs of acquisition in PIT-38 under art. 22 ust. 14, because they were "received for free." The KIS logic is: rewards are *przychód z praw majątkowych* first, then the taxed value transfers as cost into the crypto disposal regime. The courts reject the entire framing, saying art. 17 ust. 1f covers all crypto income exhaustively.[^6][^7][^3]

**Which to choose?** In a practical risk analysis:
- If the taxpayer's marginal income tax rate is 12% (first bracket, income under ~120,000 PLN/year including staking), the KIS approach may result in **lower total tax** than 19% at disposal.
- If the taxpayer is in the 32% bracket, the court approach (19% at disposal) is more favorable.
- Choosing the court approach **without a protective individual interpretation** (interpretacja indywidualna) means accepting the risk of KIS audit reassessment plus interest.
- The safest route for taxpayers expecting disputes is to file a **wniosek o interpretację indywidualną** before the tax year closes.[^8]

### Each Staking Reward as a FIFO Lot (Q15/Q16)

Under the KIS approach, each received staking reward creates a separate cost-basis lot that enters the FIFO queue for PIT-38 purposes. For DOT staking on Kraken with weekly rewards over a full year, this generates ~52 individual lots per year. Each must be valued in PLN at the market price on the date of receipt. KIS has not established any materiality threshold or simplified aggregation method. However, in the arbitrage interpretation from May–August 2025, KIS confirmed that what matters is the **annual aggregate** of income and costs, not per-transaction reporting — a principle that arguably extends to staking as well: each lot must be individually valued, but they are summed for the PIT.[^7][^9][^1][^8][^6]

**There is no de minimis threshold for small staking amounts.** Every satoshi received must in principle be valued. Practically, software tools (Kryptopity.pl, Divly, CryptoTax.pl) automate this by pulling API data.[^10][^1]

### Liquid Staking Tokens (stETH, DOT.S) — Q5

The exchange of ETH for stETH (or DOT for DOT.S) is a **crypto-to-crypto exchange** and is therefore **neutral for disposal tax purposes** (PIT-38) — it does not constitute *odpłatne zbycie* because both assets are virtual currencies. However, under KIS's broad interpretation:[^11][^12][^13]

- Receiving the liquid staking token at inception may be treated as receipt of new property, triggering the art. 18 PIT analysis
- Periodic rebase rewards (e.g., stETH balance increases) are treated identically to staking rewards — a new receipt event

Cryptotax.pl's 2025 guide confirms: "Liquid staking through platforms (Lido, Rocket Pool) — income arises when stETH/rETH is received or when rewards accrue". The KIS has not issued a dedicated liquid staking interpretation; the general staking interpretations apply by analogy.[^14][^10]

***

## 2. Airdrops

### Classification Under Polish Law

KIS classifies airdropped tokens as **przychód z praw majątkowych** (art. 18 PIT), not as darowizna (gift), and not as a capital gain under art. 17 ust. 1 pkt 11. The reasoning: the recipient received property of value; the fact that no consideration was paid is irrelevant for income recognition.[^15][^8]

### Receipt as Taxable Event (Q7)

KIS's August 2025 interpretation reviewed by kryptokancelaria.pl states: "Airdrop to nie darowizna, lecz przychód z praw majątkowych. Powstaje w momencie otrzymania tokenów, niezależnie od tego, czy mają one wartość rynkową". This creates the following structure:[^8]

- **PIT-36** in the year of receipt: report fair market value at receipt date
- **PIT-38** at disposal: report sale proceeds minus previously-taxed FMV as cost

### Worthless Tokens at Receipt (Q8)

If an airdropped token has **no determinable market value** at receipt (not listed on any exchange, no pricing data), there is no established KIS methodology. The art. 11 ust. 2a valuation rules require reference to "prices used in trading of items or rights of the same kind," which is impossible when no market exists. Several tax attorneys (Maciej Grzegorczyk / KHG) recommend in this case: apply a value of zero at receipt, with the zero value becoming the cost basis, and recognize all proceeds as income at disposal. This position is defensible given the statutory valuation gap the courts have highlighted.[^3][^8]

### Zero-Value Token Basis at Sale (Q9)

If receipt value was zero (or untaxed under the court approach), the **entire sale proceeds are gain** in PIT-38. There is no mechanism to retroactively assign a different cost basis once the token is sold. This is the standard treatment for assets received with no documented acquisition cost.[^16]

***

## 3. Earn and Lending Programs (Binance Simple Earn, Kraken Earn)

These programs are treated **identically to staking** under both KIS and court analyses, since the economic substance is the same — periodic receipt of crypto as compensation for depositing assets.[^17][^18]

**KIS treatment:** Each daily or weekly reward is a separate income event (*przychód z praw majątkowych*), to be declared in PIT-36, valued at FMV in PLN on the receipt date. The taxed value becomes acquisition cost in PIT-38 at disposal.[^9][^17]

**Example (Binance BNB staking, illustrative from cryptotax.pl):**
- 0.5 BNB received in rewards at average BNB price of 1,200 PLN
- Income: 600 PLN → PIT-36 at 12%/32%
- Later sold at 1,500 PLN: Proceeds 750 PLN − Cost 600 PLN = 100 PLN gain → PIT-38 at 19%[^19]

**Tax form:** PIT-36 for the receipt event; PIT-38 for the disposal event (both forms in the same year if the tokens are sold in the same tax year).[^1][^17]

***

## 4. Crowdloans (Kusama/Polkadot Parachain Crowdloans)

No KIS interpretation specifically addresses parachain crowdloans. The analysis must be constructed from first principles applying existing crypto tax rules.

### KSM Locking — Not a Disposal (Q11a)

Locking KSM into a crowdloan does **not** constitute *odpłatne zbycie* because:
- The KSM is returned at end of the lease period (no change of beneficial ownership)
- There is no exchange for non-crypto property

The locked KSM retains its original FIFO cost basis. KSM return after the lease period is similarly a non-taxable event — the coins reappear with the same lot cost as when locked.[^20][^21]

### Receiving Project Tokens as Crowdloan Reward (Q11b)

This is legally analogous to an airdrop or staking reward: the taxpayer receives new tokens in exchange for having locked KSM. Under **KIS logic**, this would be:
- Receipt = income event (*przychód z praw majątkowych* under art. 18)
- PIT-36 in the year received, valued at FMV on receipt date
- The FMV at receipt becomes the acquisition cost for PIT-38 at disposal

Under the **court approach**, these tokens would be taxable only when sold (PIT-38, 19%).

If the project tokens are subject to a **vesting schedule** (common in parachain crowdloans), the income under KIS logic would arise as each tranche vests and becomes accessible, not at the initial grant date.

***

## 5. Token Swaps and Redenominations

### LUNA → LUNA2 (Terra Collapse / Chain Fork) — Q12

The LUNA2 distribution was structured as an airdrop to LUNA/UST holders following the Terra fork on 27 May 2022. There was no exchange in the traditional sense — holders of old LUNA (now "LUNA Classic"/LUNC) received new LUNA2 tokens based on pre/post-collapse snapshots.[^22][^23]

**Tax treatment:**

| Item | Treatment |
|------|-----------|
| Old LUNA (LUNC) remaining in wallet | Continues as existing FIFO lot; cost basis unchanged |
| Receiving LUNA2 | Treated as airdrop receipt; under KIS: income at FMV on receipt date (PIT-36); under court approach: no event until sale |
| UST collapse to near-zero | No disposal event; cannot recognize loss until *odpłatne zbycie* occurs |
| LUNA/UST going to ~zero | **No deductible loss recognized** until tokens are actually sold for fiat or exchanged for non-crypto property[^24][^25] |

**Critical point on the UST/LUNA loss:** Polish tax law creates significant hardship here. Under art. 22 ust. 14, only "documented costs of acquiring" virtual currencies enter the cost basis. The collapse of UST or LUNA to near-zero does not by itself create a recognizable loss for PIT purposes. A deductible loss only arises when the asset is disposed of. If LUNA/LUNC was sold (even for a fraction of a cent) on a supported exchange, that disposal generates a deductible cost carryforward. If still held and worthless, there is **no current tax benefit**.[^24][^16]

**FIFO impact:** Under FIFO, old LUNA lots remain in the queue. When/if old LUNA (LUNC) is sold, the original purchase cost (likely high) offsets any minimal proceeds, creating a deductible excess cost that carries forward to future years in PIT-38.[^24]

### LUNA2 Cost Basis

If LUNA2 is treated as an airdrop: the cost basis is FMV on the airdrop receipt date (27 May 2022 or the date distributed by the exchange). If the token was worth approximately 5.50 USD at launch, that value converted to PLN at the NBP rate on that date is the acquisition cost.[^22]

***

## 6. Stablecoin Auto-Conversions (BUSD → FDUSD → USDC)

### The Neutrality Rule

The fundamental rule under Polish crypto tax law: **exchange of one virtual currency for another virtual currency is NOT a taxable event** (art. 17 ust. 1f PIT — disposal requires exchange for legal tender, goods, services, or non-crypto property). This has been confirmed consistently, including:[^12][^21][^20]
- KIS individual interpretation on USDT (February 2025): "wymiana kryptowaluty na stablecoina nadal pozostaje neutralna podatkowo"[^12]
- PwC analysis on crypto-to-crypto: neutral taxation confirmed[^21]
- March 2026 attorney commentary (Maciej Grzegorczyk): "zamiana kryptowalut na stablecoiny w Polsce pozostaje neutralna podatkowo"[^26]

BUSD, FDUSD, and USDC are all classified as virtual currencies under Polish law (they are not legal tender). Therefore:

| Conversion | Tax event? | Reasoning |
|------------|------------|-----------|
| BUSD → FDUSD (Binance forced, Jan 2024) | **No** | Crypto-to-crypto, both virtual currencies |
| FDUSD → USDC | **No** | Crypto-to-crypto, both virtual currencies |
| BUSD → PLN/USD (fiat off-ramp) | **Yes** | Disposal for legal tender |

### Cost Basis Transfer in Stablecoin Swaps

Since the conversion is neutral, the **original cost basis from BUSD carries through to FDUSD and then to USDC**. The FIFO queue for stablecoins works as follows: the oldest acquired BUSD lots transfer their cost basis into FDUSD, then into USDC. When the USDC is eventually sold for fiat, the taxable gain is measured against the original BUSD purchase price.[^27][^28]

**Practical note for Binance-forced conversions:** Binance performed auto-conversions at 1:1 with zero fees. For tax purposes, treat these as non-events: same lot count, same PLN cost per unit, same acquisition date.[^29]

***

## 7. Terra/Anchor Losses — UST and LUNA Collapse

### Can Losses Be Claimed? (Q14)

This is a painful area of Polish tax law. The answer is: **not immediately, and only upon disposal**.

- **KIS position on crypto losses:** The loss from a worthless token is only recognized in PIT-38 when the token is *actually disposed of* — sold for fiat, exchanged for non-crypto, or used to pay for services. Mere economic worthlessness does not create a tax event.[^30][^24]
- **KIS on theft/fraud losses (2025 interpretation):** Even tokens lost to theft or scams cannot be claimed as costs — "utrata środków w wyniku przestępstwa nie stanowi kosztu uzyskania przychodu". By extension, regulatory/protocol collapse losses follow the same logic.[^8]
- **Carryforward mechanism (art. 22 ust. 16):** The good news is that if you sold LUNA/UST at a loss (even for dust), the excess of costs over proceeds carries forward into future PIT-38 years and can offset future crypto gains. There is no 5-year limit for carrying forward this excess (unlike general losses) — it rolls forward indefinitely within the virtual currency tax bucket.[^31][^24]

**Strategy for near-worthless tokens:** If you still hold LUNA Classic (LUNC) or UST at near-zero value, consider executing a small disposal (even selling a fraction for minimal proceeds) to crystallize the loss into a cost carryforward in PIT-38. This converts an economically useless position into a future tax benefit.

### Remaining LUNA2 Dust

The LUNA2 tokens received via airdrop (if small/worthless) carry a zero or near-zero cost basis if taxed at receipt. Upon eventual sale, proceeds will largely be gain. If the token was received for "free" with no FMV at receipt, the cost basis is zero and the entire sale proceeds are taxable.[^16][^8]

***

## 8. FIFO Mechanics for Staking Rewards

### Each Reward = New FIFO Lot

Under the KIS approach, each staking reward receipt creates a **new virtual currency lot** with:
- Date: the date of receipt
- Quantity: the token amount received
- Cost basis: FMV in PLN on that date[^6][^10]

These lots enter the universal FIFO queue for that token. When the token is subsequently sold, FIFO means the oldest lots are disposed of first.

**Example for 52 DOT weekly rewards from Kraken staking in one year:**
- Each Friday's reward creates a new FIFO lot
- 52 lots per year, each with a different PLN cost basis
- Kraken provides an API export; tools like Kryptopity or Divly import this automatically

### No Materiality Threshold

**There is no de minimis exemption for cryptocurrency transactions in Poland.** Unlike some other countries, even sub-złoty rewards are in principle taxable. The only practical relief is that KIS confirmed (in the arbitrage context) that **annual aggregates** are what matter for the declaration — you don't file 365 individual transactions, you report total income and total costs for the year in PIT-38.[^32][^8]

### Aggregating Staking Costs and Income

For PIT-38:
- Column "Przychody" = sum of all crypto disposals in the year (fiat sales only)
- Column "Koszty" = sum of all documented acquisition costs of the disposed lots (FIFO)
- Staking rewards that were taxed under KIS at receipt → their receipt-date FMV enters the cost column when those lots are eventually sold
- Staking rewards not yet sold → the PLN equivalent of their taxed value is already included in PIT-36 but not yet in PIT-38

***

## 9. Summary Table: Activity Classification

| Activity | KIS Position | Court Position | Form (KIS) | Form (Court) | Cost Basis | FIFO Treatment |
|----------|-------------|----------------|------------|--------------|------------|----------------|
| Staking rewards (DOT, ETH, SOL, etc.) | Taxable at receipt (art. 18) | Taxable at disposal only | PIT-36 + PIT-38 | PIT-38 | FMV at receipt (KIS); Zero (court) | Each reward = new lot |
| Kraken/Binance Earn rewards | Same as staking | Same as staking | PIT-36 + PIT-38 | PIT-38 | FMV at receipt | Each reward = new lot |
| Airdrops (Binance) | Taxable at receipt | Taxable at disposal | PIT-36 + PIT-38 | PIT-38 | FMV at receipt; Zero if no market | New lot at receipt |
| Crowdloan reward tokens | By analogy to airdrop: at receipt | Taxable at disposal | PIT-36 + PIT-38 | PIT-38 | FMV on vest/receipt date | New lot per tranche |
| KSM locking (crowdloan) | Non-event | Non-event | — | — | Unchanged | No change |
| KSM returned after lease | Non-event | Non-event | — | — | Original cost | No change |
| LUNA → LUNA2 (fork airdrop) | Income at receipt (FMV) | Income at sale | PIT-36 + PIT-38 | PIT-38 | FMV on airdrop date | New lot |
| Old LUNA collapse to zero | No event (not disposed) | No event | — | — | Original cost preserved | Carries in FIFO |
| BUSD → FDUSD → USDC (forced) | **Non-event** (confirmed by KIS) | Non-event | — | — | Carries through from BUSD | Same lot, same date |
| stETH receipt for ETH staked | Disputed; by analogy: income | Non-event | PIT-36 (KIS) | — | FMV on conversion | New lot |
| Sell crypto for PLN | Taxable disposal | Taxable disposal | PIT-38 | PIT-38 | FIFO | FIFO applies |
| Crypto-to-crypto swap | Non-event | Non-event | — | — | Cost carries through | No change |

***

## 10. Key Legal References

| Provision | Substance |
|-----------|-----------|
| Art. 17 ust. 1 pkt 11 PIT | Capital gains from virtual currency disposal = capital income |
| Art. 17 ust. 1f PIT | Definition of "disposal": only fiat, goods, services, non-crypto property |
| Art. 18 PIT | Property rights income — KIS's basis for taxing staking/airdrops at receipt |
| Art. 11 ust. 2 / 2a PIT | Valuation rules: market price at time and place of receipt |
| Art. 22 ust. 14 PIT | Cost basis: documented costs of acquiring virtual currency |
| Art. 22 ust. 15–16 PIT | Costs deducted in year incurred; excess carries forward |
| Art. 9 ust. 3a pkt 2 PIT | Crypto losses cannot offset other income sources |
| Art. 30b PIT | 19% flat rate on capital gains from virtual currencies |

**Relevant KIS interpretations:**
- 0112-KDIL2-2.4011.146.2024.2.IM (19 April 2024) — staking and airdrop taxable at receipt[^2]
- 0112-KDIL2-2.4011.234.2025.3.AA (13 June 2025) — same, confirmed for 2025[^1]
- 0115-KDIT1.4011.558.2025.2.MK (10 October 2025) — same, most recent[^1]
- KIS on USDT/stablecoin neutrality (February 2025) — crypto-to-crypto neutral[^12]

**Relevant court judgments:**
- WSA Wrocław (December 2023) — staking taxes only at disposal[^5]
- WSA Warszawa III SA/Wa 179/24 (March 2024) — staking receipt not taxable; art. 17 ust. 1f is exclusive[^4][^3]

***

## 11. Practical Recommendations

1. **Obtain individual interpretations (interpretacje indywidualne)** for the highest-value activities before the tax deadline. A valid interpretation protects against KIS reassessment and interest even if KIS later changes its view. Cost: ~40 PLN per question, ~3 months processing.[^8]

2. **For staking decisions:** Choose your approach (KIS or court) consistently for the entire tax year. If choosing the court approach, document the legal basis (cite the WSA judgments above) and expect a higher scrutiny risk.

3. **BUSD/FDUSD/USDC conversions:** These are definitively non-events; document the original BUSD cost basis and preserve the chain through USDC.

4. **For LUNA/UST losses:** Consider selling remaining near-worthless positions in the current tax year to crystallize an excess cost carryforward in PIT-38. The carry-forward has indefinite duration within the crypto bucket.

5. **Documentation requirements:** Export full API history from every exchange (Kraken, Binance) for each tax year. Tools like Divly (Poland-native), Kryptopity.pl, or CryptoTax.pl can aggregate multi-exchange data and generate PIT-38 worksheets.[^10][^19][^1]

6. **Filing deadlines:** PIT-38 and PIT-36 are both due by **30 April** of the following year. PIT-38 must be filed even if no crypto was sold (to register cost basis).[^33][^34]

7. **Legislative outlook:** A draft Polish crypto asset law (implementing MiCA) was in parliamentary process as of early 2025. The law does **not** modify PIT taxation rules — MiCA is a licensing/regulatory framework and does not create new tax exemptions. The tax uncertainty therefore persists.[^35][^36][^12]

***

> **Disclaimer:** This analysis is based on publicly available KIS interpretations and WSA judgments available through March 2026. It does not constitute legal or tax advice. Given the active interpretive conflict between KIS and courts, engage a qualified *doradca podatkowy* (certified tax advisor) or *radca prawny* specializing in crypto for personal tax filings.

---

## References

1. [Jak opodatkowany jest staking i airdropy w Polsce? - Divly](https://divly.com/pl/przewodniki/staking-i-airdropy-podatek) - Sprawdź, jak w Polsce opodatkowany jest staking i airdropy. Czy podatek powstaje przy otrzymaniu czy...

2. [0112-KDIL2-2.4011.146.2024.2.IM | Interpretacje podatkowe MF](https://anylawyer.com/interpretacje-podatkowe/otrzymanie-nagrody-w-postaci-dodatkowych-jednostek-waluty-wirtualnej-w-ramach-stakingu-i-airdropu--0112-kdil2-2-4011-146-2024-2-im) - Interpretacja indywidualna dotyczy opodatkowania przychodów z nagród w postaci kryptowalut otrzymany...

3. [Otrzymanie waluty wirtualnej w ramach stakingu, czy trzeba ...](https://www.pit.pl/aktualnosci/otrzymanie-waluty-wirtualnej-w-ramach-stakingu-czy-trzeba-zaplacic-podatek-1011124) - Wraz z rozwojem technologii blockchain i rosnącą popularnością kryptowalut, kwestie podatkowe związa...

4. [Opodatkowanie nagród uzyskiwanych w procesie stakingu](https://kancelaria-skarbiec.pl/otrzymanie-kryptowaluty-w-ramach-stakingu-czy-trzeba-zaplacic-podatek/) - Opodatkowanie nagród uzyskiwanych w procesie stakingu, czyli mechanizmu konsensusu w sieciach typu p...

5. [Nagroda za staking kryptowalut. Co z przychodem? Wyrok ...](https://www.gazetaprawna.pl/podatki/artykuly/10786120,nagroda-za-staking-kryptowalut-co-z-przychodem-wyrok-wsa.html) - Nagroda w ramach stakingu kryptowalut jest przychodem podatkowym dopiero w momencie sprzedaży otrzym...

6. [Staking – jak rozliczać (interpretacja) | Kryptoprawo.pl](https://kryptoprawo.pl/staking-jak-rozliczac-interpretacja/) - Czy wiesz jak obecnie rozliczać staking? Mamy w tym zakresie interpretację. Kilka szczegółów z persp...

7. [Staking – rozliczenie z perspektywy obecnej praktyki ...](https://khg.pl/staking-rozliczenie-z-perspektywy-obecnej-praktyki-organow/) - Czy staking jest więc nadal neutralny podatkowo? Na ten moment należy przyjąć, że po Twojej stronie ...

8. [Przegląd interpretacji podatkowych – kryptowaluty, maj- ...](https://kryptokancelaria.pl/przeglad-interpretacji-podatkowych-kryptowaluty-w-2025/) - Przegląd najnowszych interpretacji podatkowych KIS dotyczących kryptowalut w 2025 roku. Sprawdź, jak...

9. [Co łączy staking i fiskusa? Nieprzewidywalność większa ...](https://mentzen.pl/blog/inne/kryptowaluty/co-laczy-staking-i-fiskusa-nieprzewidywalnosc-wieksza-niz-kurs-bitcoina/) - Staking to proces, w którym posiadacze kryptowalut “zamrażają” swoje aktywa w portfelu kryptowalutow...

10. [DeFi, Staking, Airdrops - Jak rozliczyć w Polsce 2025 | KryptoTax.pl](https://cryptotax.pl/blog/defi-staking-airdrops-podatki.html) - Kompleksowy przewodnik: jak opodatkować staking rewards, yield farming, liquidity mining, airdrops i...

11. [Kompletny przewodnik po składaniu zeznań podatkowych ...](https://divly.com/pl/wallets-and-exchanges/ethereum-podatek) - Złóż zeznanie podatkowe od kryptowalut Ethereum za rok 2026 bez problemu! Dzięki Divly Twoje podatki...

12. [Odpowiedź z Krajowej Informacji Skarbowej dot. ...](https://kryptokancelaria.pl/odpowiedz-z-krajowej-informacji-skarbowej-dot-stablecoinow/) - Zgodnie z interpretacją Krajowej Informacji Skarbowej, wymiana kryptowaluty na stablecoina, takiego ...

13. [Kompletny przewodnik po składaniu zeznań podatkowych Binance ...](https://divly.com/pl/wallets-and-exchanges/binance-smart-chain-podatek) - Złóż zeznanie podatkowe od kryptowalut Binance Smart Chain za rok 2026 bez problemu! Dzięki Divly Tw...

14. [Opodatkowanie kryptowalut](https://kancelaria-skarbiec.pl/opodatkowanie-kryptowalut/) - Opodatkowanie kryptowalut wynosi 19% od przychodu uzyskanego ze sprzedaży pomniejszony o koszty zwią...

15. [Kopanie, aktywny trading i airdropy – decyzje podatkowe ...](https://kryptoprawo.pl/kopanie-aktywny-trading-i-airdropy-decyzje-podatkowe-dla-inwestorow-krypto/) - W jednej z najnowszych interpretacji podatkowych podatnik otrzymał tokeny w ramach aridropu czyli be...

16. [Upadłość giełdy kryptowalut a podatki: jak rozliczyć ...](https://divly.com/pl/przewodniki/upad%C5%82o%C5%9B%C4%87-gie%C5%82dy-kryptowalut-a-podatki-jak-rozliczy%C4%87-odzyskane-%C5%9Brodki) - Giełda upadła (FTX, Celsius, Mt. Gox)? Sprawdź, kiedy pojawia się podatek przy odzyskanych kryptowal...

17. [Binance Simple Earn – jak rozliczyć? - Kryptoprawo.pl](https://kryptoprawo.pl/binance-simple-earn-jak-rozliczyc/) - W jaki sposób rozliczyć się z Binance Simple Earn? Wbrew pozorom w chwili zamiany tokenów na waluty ...

18. [Podatek od kryptowalut w 2024 roku - Instytut Kryptografii](https://instytutkryptografii.pl/home2/podatek-od-kryptowalut-w-2024-roku-szczegolowy-przewodnik-rozliczen/) - Poznaj zasady rozliczeń podatku od kryptowalut w 2024 roku. Sprawdź nasz przewodnik, aby uniknąć błę...

19. [Rozliczenie Binance w Polsce - Instrukcja krok po kroku 2025](https://cryptotax.pl/blog/rozliczenie-binance-polska.html) - Jak rozliczyć Binance w Polsce? Eksport danych, Binance Earn, P2P, Convert i obliczanie podatku PIT-...

20. [Wymiana kryptowalut ma być neutralna podatkowo](https://bttp.pl/aktualnosci/wymiana-kryptowalut-ma-byc-neutralna-podatkowo/) - Wymiana bitcoinów np. na ether, litecoin czy inną walutę wirtualną ma być neutralna podatkowo. Dotyc...

21. [Wymiana jednej kryptowaluty na drugą neutralna podatkowo ...](https://studio.pwc.pl/aktualnosci/wyroki/wymiana-jednej-kryptowaluty-na-druga-neutralna-podatkowo) - Wymiana jednej kryptowaluty na inne z punktu widzenia podatku od dochodów osób prawnych powinna być ...

22. [Terra 2.0 rusza z airdropem LUNA](https://pl.beincrypto.com/terra-2-0-rusza-z-airdropem-luna/) - Terraform Labs uruchomiło w piątek nowy blockchain Terra 2.0. Według CoinGecko nowy token LUNA koszt...

23. [Terra 2 zostanie uruchomiona 27 maja. Co musisz wiedzieć?](https://bitcan.pl/blog/terra-2-zostanie-uruchomiona-27-maja-co-musisz-wiedziec/) - W dniu 27 maja 2022 roku Terra 2 zostanie uruchomiona jako nowy blockchain. · W jego ramach miejsce ...

24. [Strata z handlu wirtualną walutą - jak rozliczyć?](https://poradnikprzedsiebiorcy.pl/-czy-strata-z-handlu-wirtualna-waluta-musi-byc-wykazana-w-deklaracji-rocznej) - Popularne w ostatnim czasie handlowanie wirtualną walutą nie zawsze przynosi zyski. Czy strata z han...

25. [Rozliczanie strat z kryptowalut – jak odliczyć?](https://litigato.pl/rozliczanie-strat-z-kryptowalut/) - Jak rozliczyć straty z kryptowalut w PIT? Sprawdź zasady odliczeń, przenoszenie strat na kolejne lat...

26. [Zamiana kryptowalut na stablecoiny nie podlega podatkowi](https://pl.beincrypto.com/ekspert-prawa-zamiana-kryptowalut-stablecoiny-nie-podlega-podatkowi/) - Maciej Grzegorczyk wyjaśnia, że zamiana kryptowalut na stablecoiny w Polsce pozostaje neutralna poda...

27. [Jak rozliczać kryptowaluty w 2023 roku?](https://rozliczkryptowaluty.pl/artykuly/jak-rozliczac-kryptowaluty-w-2023-roku/)

28. [Rozliczenie PIT od przychodów ze sprzedaży kryptowalut](https://www.pitax.pl/wiedza/poradnik-rozliczenia/rozliczenie-pit-od-przychodow-ze-sprzedazy-kryptowalut/) - Podstawą opodatkowania jest dochód, gdy przychód przewyższa koszty. Stawka podatku od dochodu z odpł...

29. [Zawiadomienie dotyczące usunięcia BUSD i konwersji ...](https://www.binance.com/pl/support/announcement/detail/1c98ce7bb464422dbbaeda7066ae445b) - Informujemy, że w związku ze wstrzymaniem mintu nowych BUSD przez Paxos, Binance zaprzestanie wsparc...

30. [Rozliczenia PIT od kryptowalut – obowiązki podatkowe ...](https://www.mddp.pl/rozliczenia-pit-od-kryptowalut-i-obowiazki-podatkowe-z-tym-zwiazane/) - Jakie są obowiązki podatkowe dotyczące rozliczenia PIT od kryptowalut? Jak w rozliczeniach tych mogą...

31. [Jak samodzielnie rozliczyć podatek od kryptowalut w 2025?](https://kancelariamw.pl/jak-rozliczyc-podatek-od-kryptowalut/) - Jak rozliczyć kryptowaluty w PIT? Schemat podatkowy w naszym przypadku jest dość prosty: przychód mi...

32. [Jak uniknąć podatku od kryptowalut w Polsce](https://divly.com/pl/przewodniki/jak-uniknac-podatku-od-kryptowalut) - W przeciwieństwie do zwykłego PIT, w przypadku kryptowalut nie ma kwoty wolnej od podatku. Nawet nie...

33. [Jak rozliczyć zyski z kryptowalut w Polsce? Praktyczny poradnik dla ...](https://adnpodatki.pl/jak-rozliczyc-zyski-z-kryptowalut-w-polsce-praktyczny-poradnik-dla-inwestorow/) - Kryptowaluty stały się jednym z najpopularniejszych aktywów inwestycyjnych ostatnich lat. Według rap...

34. [Jak rozliczyć podatek od kryptowalut w 2025 roku?](https://litigato.pl/jak-rozliczyc-podatek-od-kryptowalut/) - Rozliczenie kryptowalut za 2025 r. robisz w PIT-38 składanym do 30 kwietnia 2026 r., wykazując przyc...

35. [MiCA 2025: Koniec VASP, start licencji CASP](https://dudkowiak.pl/fintech/implementacja-mica-w-polsce/) - Rewolucja w przepisach dot. kryptoaktywów. Sprawdź, kogo obejmuje MiCA, jakie są wymagania CASP i ja...

36. [Regulacje kryptoaktywów w Polsce: MiCA i krajowa ustawa](https://www.imlovingcrypto.com/post/regulacje-kryptoaktyw%C3%B3w-w-polsce-mica-i-krajowa-ustawa-gdzie-jeste%C5%9Bmy) - 1. MiCA – ramy unijne już obowiązująRozporządzenie MiCA (Markets in Crypto-Assets, (UE) 2023/1114) w...

