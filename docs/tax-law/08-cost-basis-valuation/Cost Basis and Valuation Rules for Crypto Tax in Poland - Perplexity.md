# Cost Basis and Valuation Rules for Crypto Tax in Poland

## Executive summary
Polish PIT rules for virtual currencies are built around an annual netting model, not transaction-by-transaction realization of cost by lot in the way many crypto tax tools present FIFO. The core statutory rule is that income from disposal of virtual currencies equals the annual difference between total proceeds from taxable disposals and deductible costs determined under Article 22(14)-(16) of the PIT Act.[^1][^2][^3]

The PLN conversion rule in Article 11a applies when amounts are expressed in foreign currency. Article 11a(1) says that revenue in foreign currency is translated into PLN at the NBP average rate from the last business day preceding the day the revenue is obtained, and Article 11a(2) says costs incurred in foreign currency are translated into PLN at the NBP average rate from the last business day preceding the day the cost is incurred.[^2]

For crypto, this means that when a taxable disposal yields EUR or another fiat currency, the fiat amount is generally converted to PLN using the NBP average rate from the last business day before the day of the taxable disposal. Likewise, when crypto is purchased using EUR or another foreign fiat, the foreign-currency purchase expense is generally converted to PLN using the NBP average rate from the last business day before the cost is incurred.[^4][^2]

The Ministry of Finance’s public guidance does not describe crypto tax as a FIFO system. Instead, it instructs taxpayers to report all documented acquisition costs incurred in the year, plus unrelieved costs carried from prior years, and to offset them against annual taxable disposal proceeds. That is materially different from a strict lot-matching method.[^3][^5]

A further complication is that Article 30b(7) and 30b(7a) contain a statutory FIFO rule that expressly applies to fund units and “appropriately” to other Article 30b income, including income from virtual currencies. However, the official Ministry guidance for crypto does not operationalize this rule as per-coin lot matching, and public tax guidance overwhelmingly presents crypto under the annual aggregate-cost model.[^5][^1][^3]

## Statutory framework
The key provisions are:

| Provision | Effect for crypto tax | Exact point that matters |
|---|---|---|
| Art. 17(1) pkt 11 and 17(1f) PIT | Defines taxable crypto proceeds as capital gains income from disposal of virtual currency | Taxable disposal means exchange of virtual currency for legal tender, goods, services, other property rights, or settling liabilities; crypto-to-crypto swaps are outside taxable disposal.[^6][^3] |
| Art. 30b(1a) PIT | Sets 19% tax rate | Income from disposal of virtual currencies is taxed at 19%.[^1][^3] |
| Art. 30b(1b) PIT | Defines annual taxable income | Income is the yearly difference between total taxable proceeds and costs under Art. 22(14)-(16).[^1] |
| Art. 22(14) PIT | Defines deductible costs | Only documented direct acquisition expenses and costs related to disposal are deductible.[^7][^3] |
| Art. 22(15)-(16) PIT | Timing and carryforward of crypto costs | Costs are deducted in the year incurred; excess costs carry forward to the next year.[^8][^3] |
| Art. 11a(1)-(2) PIT | FX translation rule | Foreign-currency revenue and foreign-currency costs are translated using the NBP average rate from the last business day before the relevant date.[^2] |
| Art. 30b(6) and 6a PIT | Annual reporting | PIT-38 must report crypto income, and also crypto costs even if no taxable disposal occurred that year.[^1][^3] |
| Art. 30b(7) and 7a PIT | FIFO rule in statute | FIFO is expressly stated for fund units and applied “appropriately” to other Article 30b income, including virtual currencies.[^1] |

## Exact wording of the exchange-rate rule
Article 11a(1) provides: “Przychody w walutach obcych przelicza się na złote według kursu średniego walut obcych ogłaszanego przez Narodowy Bank Polski z ostatniego dnia roboczego poprzedzającego dzień uzyskania przychodu.”[^2]

Article 11a(2) provides: “Koszty poniesione w walutach obcych przelicza się na złote według kursu średniego ogłaszanego przez Narodowy Bank Polski z ostatniego dnia roboczego poprzedzającego dzień poniesienia kosztu.”[^2]

For crypto taxation, these provisions matter whenever the amount to be recognized under PIT is denominated in EUR, USD, or another fiat currency rather than PLN. They do not create an NBP rate for crypto itself; they create an NBP conversion rule for foreign fiat amounts used to determine revenue or cost.[^3][^2]

## Does Article 11a apply to crypto transactions?
Yes, but only indirectly. Crypto is not a foreign currency for PIT purposes; rather, Article 11a is used when the relevant revenue or cost figure is expressed in foreign fiat, such as EUR or USD received from or spent on an exchange transaction.[^4][^2]

That is why Ministry and professional guidance describe a sale of virtual currency for non-PLN fiat as producing revenue equal to the foreign fiat proceeds translated into PLN under Article 11a(1). The same logic applies to acquisition costs paid in foreign fiat under Article 11a(2).[^4][^2]

## NBP rate rules in practice
### Selling USDC for EUR on Binance
If USDC is sold for EUR, the taxable revenue is the EUR amount received, because the taxable event is exchange of virtual currency for legal tender. Where the legal tender received is EUR rather than PLN, the EUR amount should be converted into PLN using the NBP average EUR rate from the last business day preceding the day the revenue arose.[^3][^4][^2]

Using the trade-date rate itself is not what Article 11a says. The statute explicitly points to the last business day preceding the day of obtaining the revenue, not the same-day rate.[^2]

If the trade occurs on a Saturday, the applicable NBP rate is still the rate from the last business day before Saturday, which will normally be Friday’s table A rate, unless Friday was not a business day. Article 11a expressly uses the “ostatni dzień roboczy poprzedzający” formulation, so weekends and holidays push the taxpayer back to the previous business day with an NBP rate.[^2]

### Purchase of crypto with EUR
For crypto purchased with EUR, the cost is the documented EUR amount directly spent to acquire the virtual currency, translated into PLN at the NBP average EUR rate from the last business day preceding the day the cost was incurred. That follows directly from Article 22(14) together with Article 11a(2).[^7][^3][^2]

This is the cleanest application of the rule, because the expense is directly incurred in a foreign fiat currency. Under the Ministry’s annual model, this PLN amount becomes part of the acquisition costs reported for the year and can either be offset that year or carried forward.[^3]

### Revenue and cost both use the “previous business day” rule
Yes. The statute is symmetrical: Article 11a(1) governs foreign-currency revenue, and Article 11a(2) governs foreign-currency costs. So the “last business day before” rule applies to both, but to different reference dates: revenue date for income, cost-incurrence date for costs.[^2]

## Salary paid in USDC
### Income side
Where services are remunerated in virtual currency, KIS guidance treats this as remuneration for services received in kind or in a barter-like structure. The service provider recognizes ordinary business or personal-service income at the value of the remuneration when received, converted into fiat/PLN according to the rules applicable to that source of income.[^9][^10]

KIS guidance also states that if the virtual currency later is sold, the taxpayer may recognize as crypto-tax cost the value at which the virtual currency was previously recognized as income on receipt. In other words, the earlier taxed value becomes the acquisition cost for PIT-38 purposes on later disposal.[^10][^9]

### Which reference currency should be used for USDC salary?
The safest legal framing is not “USDC is pegged to USD, therefore use the NBP USD rate,” but rather: determine the PLN value of the remuneration actually received at the time of receipt using its market value, then use that same taxed PLN amount as the crypto acquisition cost on later disposal. This follows the interpretation logic for crypto received as payment for services and avoids assuming a legal equivalence between USDC and USD.[^9][^10]

If the contract itself states remuneration in USD or EUR and payment is made in USDC as settlement of that contractual amount, then the contractual fiat amount may strongly support the PLN valuation. But if the token was not exactly at parity, the more defensible position is to use the actual market value of the USDC received on the receipt date, not an automatic 1:1 USD assumption.[^11][^10][^9]

### What if USDC was depegged?
If USDC was trading away from 1.00 USD, relying mechanically on the NBP USD rate alone would be hard to justify as a valuation of the crypto received. The tax logic for property or rights received in kind points toward market value at receipt, and KIS guidance on staking similarly emphasizes market value at the time and place of receipt rather than a fixed reference peg.[^12][^11]

Accordingly, if USDC salary is recognized as income upon receipt, the later crypto cost basis should be the PLN amount of that previously recognized income. If the token was depegged, that PLN amount should reflect the actual value of the USDC received, not a fictional parity value.[^11][^9]

## Deductible costs: what qualifies under Article 22(14)-(16)?
The statute allows only “udokumentowane wydatki bezpośrednio poniesione na nabycie waluty wirtualnej” and “koszty związane ze zbyciem waluty wirtualnej.” Ministry guidance adds that these include documented expenses paid to intermediaries involved in the sale.[^7][^3]

### Cost classification
| Item | Usually deductible? | Reasoning |
|---|---|---|
| Original purchase price of crypto bought for fiat | Yes | Directly incurred acquisition expense under Art. 22(14).[^7][^3] |
| Exchange trading fees on purchase | Usually yes | Part of direct acquisition expense if documented.[^7][^3] |
| Exchange trading fees on sale | Yes | Cost related to disposal; MF guidance expressly includes intermediary sale costs.[^3] |
| Fiat withdrawal fee charged by exchange after sale | Usually yes if directly tied to sale proceeds realization; otherwise arguable | Could qualify as cost related to disposal, but documentation and direct nexus matter.[^7][^3] |
| Blockchain network fee to transfer crypto between own wallets | Usually no | Not a direct acquisition expense and not necessarily a disposal cost; official guidance is narrower.[^3] |
| Gas fee paid to swap one crypto for another crypto | No for PIT-38 disposal cost | MF guidance says expenses connected with exchanging one virtual currency for another are not deductible.[^3] |
| Fee paid in the same token on a sale for fiat | Usually yes in principle | It is economically a disposal-related fee, but it should be documented and valued in PLN consistently.[^7][^3] |
| Hardware wallet cost | No | Not a direct acquisition expense or disposal cost.[^3] |
| VPN, laptop, phone, accounting software | No for private crypto PIT-38 | Indirect overhead, not direct acquisition/disposal cost.[^3] |
| Mining rig / mining hardware | No | MF guidance expressly excludes equipment for mining.[^3][^8] |
| Electricity for mining | No | MF guidance expressly excludes electricity used for mining.[^3] |
| Loan interest / credit cost used to fund purchases | No | MF guidance expressly excludes financing costs.[^3] |

The overall pattern is restrictive. If an expense is not tightly and directly linked to either acquiring the virtual currency or executing its taxable disposal, it is at serious risk of disallowance.[^8][^3]

## Free crypto: airdrops, staking, gifts
### Airdrops and staking rewards
Polish practice is unsettled at a policy level, but recent KIS interpretation practice tends to treat staking rewards as taxable income upon receipt, valued at market value at the time and place of receipt, with that same value then available as cost on later disposal of the rewarded tokens.[^13][^12][^11]

That means the answer is not automatically “cost basis zero.” If the receipt itself generated taxable income under PIT-36 or another source, the stronger interpretation is that the previously taxed PLN value should become the acquisition cost for later PIT-38 disposal.[^13][^11]

For a pure airdrop with no taxed income recognized at receipt, the conservative fallback is often a zero acquisition cost for PIT-38, because Article 22(14) focuses on documented direct acquisition expenses. But where an airdrop or reward was separately taxed as income at receipt, a strong argument exists that the taxed value should later function as the disposal cost basis, analogous to other property previously recognized as income.[^14][^11]

### Gifts and gratuitous transfers
Where crypto is received by gift, later sale still generates PIT income from disposal of virtual currency, but the donee generally lacks a direct acquisition expenditure under Article 22(14). Commentary and interpretation practice therefore point against treating gifted value itself as a crypto acquisition cost under PIT-38.[^15][^16]

This distinguishes gifts from situations where crypto was separately taxed as income on receipt. A gift is ordinarily governed by inheritance-and-donation tax logic, not by prior PIT recognition that could feed into crypto cost basis.[^17][^18]

## USDC salary as later crypto cost basis
Yes, where USDC was received as remuneration for services and the taxpayer recognized income on receipt, the PLN value at which that remuneration was or should have been recognized is the strongest candidate for later crypto cost basis on disposal. KIS commentary on crypto remuneration expressly follows that approach.[^10][^9]

The practical implication is that the taxpayer should preserve the documentation showing both sides of the event: the underlying invoice or service entitlement, and the exchange or wallet records showing the amount of USDC actually received and, where needed, its market valuation on that date.[^19][^10]

## FIFO: is it mandated?
### The statute
FIFO is expressly mentioned in Article 30b(7), which states that when specific fund units cannot be identified, income is deemed to arise from the units acquired earliest, and this is applied separately to each investment account. Article 30b(7a) then says that paragraph 7 applies appropriately to the other income referred to in Article 30b(1) and to the income referred to in Article 30b(1b), which includes virtual currencies.[^1]

So, at the level of black-letter law, there is indeed a statutory FIFO hook for crypto through Article 30b(7a). This is stronger than saying FIFO is merely market convention.[^1]

### The practical tension
Despite that statutory wording, the official MF crypto guidance does not instruct taxpayers to compute per-disposal lot cost under FIFO. Instead, it uses the annual aggregate formula: yearly proceeds minus current-year and carried-forward deductible costs.[^3]

Because of that tension, the most accurate statement is: FIFO has a textual statutory basis via Article 30b(7a), but Polish crypto compliance practice and official guidance are predominantly framed around annual aggregate costs rather than per-asset lot matching. For many taxpayers, those two approaches converge only partially, not perfectly.[^5][^1][^3]

### Per asset or all crypto combined?
Neither the Ministry guidance nor the publicly available official crypto page says that taxpayers must maintain separate FIFO queues for BTC, ETH, USDC, and so on. In fact, the annual-cost model on the official page aggregates costs of acquiring virtual currencies generally, not coin-by-coin.[^3]

If one tried to operationalize Article 30b(7a) literally, the more coherent reading would still be asset-specific rather than cross-asset, because one cannot identify lots across different assets as though BTC and ETH were interchangeable units. But this point is not clearly spelled out in official crypto guidance.[^5][^1]

## Pre-residency holdings
Recent commentary on interpretation practice indicates that a taxpayer who becomes a Polish tax resident and later sells crypto acquired earlier abroad may generally rely on the original documented acquisition cost rather than resetting basis to market value on the date Polish residence begins. Article 30b taxes the later disposal, and Article 22(14) focuses on documented direct acquisition expenses, not immigration-step-up value.[^20][^21]

That said, the factual record matters. The taxpayer must be able to document the historical acquisition expenditure. Absent reliable evidence of original cost, the practical ability to use that cost in PIT-38 is weakened.[^20][^19]

## Stablecoin auto-conversions
Under Polish PIT, exchange of one virtual currency for another virtual currency is not a taxable disposal. The official Ministry page says explicitly: “Wymiana pomiędzy walutami wirtualnymi, niezależnie od tego, czy jest dokonywana na giełdzie, czy jednostkowo, nie podlega opodatkowaniu.”[^3]

Therefore, an automatic exchange such as BUSD to FDUSD or FDUSD to USDC should generally be treated as a non-taxable crypto-to-crypto event, not a realization of PIT-38 revenue. Binance’s BUSD-to-FDUSD conversion was also executed as a 1:1 token conversion for eligible users, which supports treating it as a continuity event rather than a fiat disposal.[^22][^3]

The difficult part is basis continuity. Because the crypto-to-crypto conversion is not taxed, the economically sensible treatment is to carry forward the historical PLN acquisition cost into the replacement token. If there are multiple automatic conversions in sequence, the documentation should preserve the chain from original acquisition through each exchange-generated conversion event.[^23][^22][^3]

## Record-keeping and “ewidencja walut wirtualnych”
### Is there a statutory “ewidencja walut wirtualnych” requirement in Article 30b(6)?
No such wording appears in the currently accessible text of Article 30b. Article 30b(6) requires the taxpayer to report income in the annual return, and Article 30b(6a) requires reporting deductible costs even when no disposal revenue arose in that year.[^1]

The accessible statutory text does not set out a separate formal register template called “ewidencja walut wirtualnych.” What the law clearly requires is the ability to substantiate reported proceeds and documented costs.[^7][^1]

### What level of detail is needed?
Although the tax return itself reports annual totals, the supporting evidence should be maintained per transaction. Accounting and interpretive commentary indicate that electronic exchange records may serve as evidence if they identify the operation type, asset, price, fee, timestamp, and quantity involved.[^19]

That means annual totals are enough for PIT-38 filing, but not enough for audit support unless they can be reconciled back to detailed transaction-level evidence. In practice, a defensible crypto register should therefore be transaction-level, even though the return is annual.[^19][^3]

### Must records be maintained in real time?
No source found states that the register must be maintained contemporaneously day by day. The statutory requirement is evidentiary, not a formal real-time ledger obligation.[^19][^1]

Accordingly, reconstruction from exchange records at filing time should be acceptable, provided the reconstruction is accurate, complete, and supported by source documents. However, the more reconstruction is required after the fact, the greater the risk of gaps in evidence, especially around delisted assets, missing CSV exports, or incomplete fee histories.[^19][^3]

### Are CSV exports and trade confirmations sufficient?
Often yes, if they contain enough detail to establish proceeds, costs, dates, quantities, and fees. Commentary citing interpretation practice notes that documents may be electronic and that exchange CSV exports can be sufficient where they contain the information necessary to determine revenue and deductible costs correctly.[^19]

A prudent documentation package should include more than just CSVs: exchange account statements, raw trade confirmations, deposit and withdrawal logs, wallet addresses and hashes for on-chain transfers, screenshots for delisted pairs, and proof of fiat inflows/outflows when relevant.[^10][^19]

### How long should records be kept?
Under Article 86(1) of the Tax Ordinance, taxpayers required to keep tax books must retain books and related documents until expiration of the limitation period for the tax liability. Under Article 70(1) of the Tax Ordinance, that period is generally five years from the end of the calendar year in which the tax payment deadline passed.[^24][^25]

For annual PIT, that usually means the practical retention period extends well beyond five calendar years from the transaction date. For example, documents relevant to PIT due by 30 April of the following year generally need to be retained until the end of the fifth year counting from the end of that payment-deadline year, subject to suspension or interruption of limitation.[^25][^24]

## Worked examples
### Example 1: Selling USDC for EUR on a weekday
Facts: On Tuesday, 10 March, 20,000 USDC is sold on Binance for 18,500 EUR. Binance charges a 20 EUR trading fee.[^2][^3]

Tax treatment:
1. Taxable revenue arises because virtual currency is exchanged for legal tender.[^3]
2. Revenue in EUR is translated to PLN using the NBP EUR average rate from Monday, 9 March, assuming that was the last business day preceding the disposal date.[^2]
3. The 20 EUR fee is generally a disposal-related cost translated to PLN using the NBP EUR average rate from the last business day preceding the day that fee-cost is incurred.[^2][^3]
4. The remaining deductible crypto costs are those documented acquisition costs carried in the annual pool under Article 22(14)-(16).[^7][^3]

### Example 2: Sale on Saturday
Facts: On Saturday, 14 March, BTC is sold for 10,000 EUR on Kraken.[^2]

Tax treatment:
1. Revenue date is the disposal date, Saturday.[^3][^2]
2. Because Article 11a refers to the last business day preceding the day of obtaining revenue, the taxpayer uses the NBP EUR average rate from Friday, 13 March, unless Friday was itself not a business day.[^2]
3. A Saturday NBP rate is not used, because the statute does not permit same-day weekend translation.[^2]

### Example 3: Buying ETH with EUR
Facts: On 8 April, 5,000 EUR is spent to acquire ETH; exchange fee is 25 EUR.[^3][^2]

Tax treatment:
1. Both the purchase amount and the purchase fee are foreign-currency acquisition costs if directly connected with acquiring the ETH.[^7][^3]
2. Each EUR-denominated cost amount is translated into PLN at the NBP EUR average rate from the last business day preceding 8 April.[^2]
3. The resulting PLN amount becomes part of annual deductible crypto costs.[^3]

### Example 4: USDC salary later sold
Facts: A contractor invoices 4,000 USD-equivalent for services and receives 4,000 USDC on 5 May. On that date, USDC trades at 0.992 USD. The contractor later sells the USDC for EUR.[^11][^9]

Tax treatment:
1. On receipt, the contractor recognizes non-crypto operating income under the rules for the service income source, using the value of the remuneration received.[^9][^10]
2. Because the token is slightly depegged, the more defensible valuation is the actual market value of 4,000 USDC on 5 May, not an automatic 4,000 USD assumption.[^11][^9]
3. When the USDC is later sold, that earlier taxed PLN value should function as the crypto acquisition cost for PIT-38 purposes.[^9][^10]

### Example 5: Binance auto-conversion from BUSD to FDUSD
Facts: Binance automatically converts 8,000 BUSD to 8,000 FDUSD under its auto-conversion program.[^22]

Tax treatment:
1. No PIT-38 taxable revenue arises, because this is a crypto-to-crypto exchange.[^3]
2. The historical PLN acquisition cost attached to the BUSD should continue into the FDUSD position.[^22][^3]
3. If FDUSD is later converted to USDC, that second conversion is likewise non-taxable, and the same historical cost continuity should be preserved in records.[^23][^3]

## Practical compliance takeaways
For crypto sold into EUR or another foreign fiat, use Article 11a exactly as written: previous-business-day NBP rate for revenue, and previous-business-day NBP rate for foreign-currency costs.[^2]

For remuneration, staking rewards, or similar crypto receipts, do not default automatically to a stablecoin peg. The stronger position is to determine the PLN value actually recognized as income on receipt and carry that value into later PIT-38 cost basis if the receipt was separately taxed.[^10][^11][^9]

For deductibility, think narrowly. Exchange buy/sell fees usually qualify if documented; financing, hardware, mining electricity, and most overhead do not.[^8][^3]

For methodology, the cleanest doctrinal statement is that there is a statutory FIFO reference in Article 30b(7a), but the operative Ministry guidance for crypto uses an annual aggregate-cost framework. Any reporting methodology should therefore be internally consistent, thoroughly documented, and reconcilable to the annual PIT-38 figures.[^5][^1][^3]

## Bottom-line answers to the numbered questions
| Question | Short answer |
|---|---|
| 1 | Article 11a applies to foreign-currency amounts used in crypto taxation; exact wording is in Art. 11a(1) for revenue and 11a(2) for costs.[^2] |
| 2 | For USDC sold for EUR, revenue is EUR received translated at NBP EUR average rate from the last business day before the trade date; same-day trade rate is not the statutory rule; Saturday uses the previous business day’s NBP rate.[^2][^4] |
| 3 | For USDC salary, the safer basis is the PLN market value of the USDC actually received when income arose; if separately taxed then that PLN amount becomes later crypto cost basis; depeg should be respected.[^9][^11][^10] |
| 4 | Yes, purchase cost in EUR is generally EUR amount plus direct fees translated at the NBP EUR rate from the last business day before the cost was incurred.[^2][^3] |
| 5 | Yes, the “previous business day” rule applies to both revenue and cost, under Art. 11a(1) and (2) respectively.[^2] |
| 6 | Deductible: direct purchase price and direct disposal/acquisition fees if documented; non-deductible: financing, mining equipment, mining electricity, most indirect costs.[^3][^8] |
| 7 | Not always zero: if staking/airdrop was separately taxed as income on receipt, that taxed value is the stronger later cost basis; gifts are different and usually do not generate acquisition cost under Art. 22(14).[^11][^15] |
| 8 | Yes, for USDC salary the crypto cost basis should generally be the PLN value previously recognized as income on receipt.[^9][^10] |
| 9 | FIFO has an express statutory reference via Art. 30b(7) and 7a, but official crypto guidance still uses annual aggregate costs.[^1][^3] |
| 10 | No official crypto guidance clearly requires per-asset queues; annual reporting is aggregated, though literal FIFO logic would be more coherent per asset than across all tokens.[^1][^3] |
| 11 | Better view: original documented acquisition cost, not market value on becoming Polish resident.[^20][^21] |
| 12 | Auto-conversion between stablecoins is generally non-taxable crypto-to-crypto exchange; historical cost should continue into replacement token.[^3][^22][^23] |
| 13 | Accessible Art. 30b text does not contain a formal “ewidencja walut wirtualnych” content requirement; it requires annual reporting of income and costs.[^1] |
| 14 | Return is annual totals, but supporting evidence should be per transaction.[^19][^3] |
| 15 | No explicit real-time maintenance rule found; reconstruction from records is generally acceptable if complete and reliable.[^19] |
| 16 | CSV exports and confirmations are often sufficient if they contain enough detail, but a fuller audit file is safer.[^19][^10] |
| 17 | Keep records until limitation expires, generally five years from the end of the year in which the PIT payment deadline passed, subject to suspension/interruption rules.[^25][^24] |

---

## References

1. [Art. 30b. pod. dochod. fiz. - Ustawa o podatku dochodowym ...](https://lexlege.pl/ustawa-o-podatku-dochodowym-od-osob-fizycznych/art-30b/) - Dochodem z odpłatnego zbycia walut wirtualnych jest osiągnięta w roku podatkowym różnica między sumą...

2. [Art. 11a. pod. dochod. fiz. - Ustawa o podatku dochodowym ...](https://lexlege.pl/ustawa-o-podatku-dochodowym-od-osob-fizycznych/art-11a/) - 1. Przychody w walutach obcych przelicza się na złote według kursu średniego walut obcych ogłaszaneg...

3. [podatki.gov.pl - Zbycie kryptowalut](https://www.podatki.gov.pl/podatki-osobiste/pit/informacje-podstawowe/co-jest-opodatkowane/zbycie-kryptowalut/) - Portal podatki.gov.pl

4. [Skutki podatkowe otrzymania nagrody w formie kryptowaluty](https://izbapodatkowa.pl/baza-wiedzy/skutki-podatkowe-otrzymania-nagrody-w-formie-kryptowaluty/) - Jeżeli waluta wirtualna zostanie wymieniona na walutę tradycyjną, inną niż złoty, wartość przychodu ...

5. [A Crypto Tax Guide for Poland](https://nexo.com/pl/blog/a-crypto-tax-guide-for-poland) - Useful information about crypto taxes in Poland.

6. [Waluty wirtualne a podatek PIT](https://kryptoprawo.pl/waluty-wirtualne-a-podatek-pit/) - Po zmianie przepisów przychody z obrotu walutami wirtualnymi rozliczamy jako przychody z kapitałów p...

7. [Ustalenie kosztu uzyskania przychodów z odpłatnego ...](https://akademialtca.pl/blog/ustalenie-kosztu-uzyskania-przychodow-z-odplatnego-zbycia-waluty-wirtualnej) - Otrzymana waluta wirtualna może zostać odpłatnie zbyta, tj. zamieniona na środek płatniczy. Sprzedaż...

8. [Wydatki poniesione na koparkę wirtualnych walut](https://poradnikprzedsiebiorcy.pl/-wydatki-poniesione-na-koparke-wirtualnych-walut-najwazniejsze-informacje) - W kontekście powyższego należy zwrócić uwagę, że art. 22 ust. 14 ustawy PIT stanowi wyłącznie o wyda...

9. [Zapłata za usługę kryptowalutą – skutki w podatku ...](https://isp-modzelewski.pl/serwis/zaplata-za-usluge-kryptowaluta-skutki-w-podatku-dochodowym-od-osob-fizycznych/) - Niemniej jednak i tak będzie miał Pan obowiązek wykazania przychodów i kosztów dotyczących odpłatneg...

10. [Centrum wiedzy - Płatności za usługi w walutach wirtualnych - KIP](https://izbapodatkowa.pl/baza-wiedzy/platnosci-za-uslugi-w-walutach-wirtualnych/) - Płatności za usługi w walutach wirtualnych

11. [Staking – jak rozliczać (interpretacja) | Kryptoprawo.pl](https://kryptoprawo.pl/staking-jak-rozliczac-interpretacja/) - Czy wiesz jak obecnie rozliczać staking? Mamy w tym zakresie interpretację. Kilka szczegółów z persp...

12. [Otrzymanie waluty wirtualnej w ramach stakingu, czy trzeba ...](https://www.pit.pl/aktualnosci/otrzymanie-waluty-wirtualnej-w-ramach-stakingu-czy-trzeba-zaplacic-podatek-1011124) - Wraz z rozwojem technologii blockchain i rosnącą popularnością kryptowalut, kwestie podatkowe związa...

13. [Co łączy staking i fiskusa? Nieprzewidywalność większa ...](https://mentzen.pl/blog/inne/kryptowaluty/co-laczy-staking-i-fiskusa-nieprzewidywalnosc-wieksza-niz-kurs-bitcoina/) - Pomimo rosnącej popularności walut wirtualnych oraz nowych możliwości inwestycji, fiskus często nie ...

14. [Nieodpłatne otrzymanie kryptowalut a przychód podatkowy](https://poradnikprzedsiebiorcy.pl/-nieodplatne-otrzymanie-kryptowalut-czy-nalezy-odprowadzic-podatek) - Rynek walut wirtualnych stale się rozwija. Sprawdź, czy nieodpłatne otrzymanie kryptowalut zobowiązu...

15. [Skutki podatkowe darowizny walut wirtualnych](https://dochodowy.com.pl/artykul/skutki-podatkowe-darowizny-walut-wirtualnych) - Sprzedaż waluty wirtualnej nabytej przez Podatnika w drodze darowizny będzie stanowić przychód z kap...

16. [Darowizna kryptowaluty bez PIT, ale sprzedaż z podatkiem](https://www.gazetaprawna.pl/podatki/artykuly/10798952,kryptowaluta-pit-podatek-od-spadkow-i-darowizn.html) - Interpretacje indywidualne dyrektora KIS z 20 lipca 2021 r., sygn. 0115-KDIT1.4011.327.2021.4.MR, or...

17. [Darowizna wirtualnej waluty-dowiedz się więcej na ten temat!](https://poradnikprzedsiebiorcy.pl/-darowizna-wirtualnej-waluty-a-podatek-od-spadkow-i-darowizn) - Sprawdź, czy darowizna wirtualnej waluty podlega opodatkowaniu podatkiem od spadków i darowizn. Czy ...

18. [Kryptowaluta w darowiźnie - trzeba zapłacić podatek fiskusowi - PIT.pl](https://www.pit.pl/aktualnosci/kryptowaluta-w-darowiznie-trzeba-zaplacic-podatek-fiskusowi-1011075) - Osoby, które dostały w darowiźnie kryptowaluty mogą być zobowiązane do zapłaty podatku. Waluta wirtu...

19. [Transakcje dotyczące kryptowalut zapisujemy w księgach ...](https://www.gazetaprawna.pl/podatki/artykuly/10802399,jak-ksiegowac-transakcje-dot-kryptowalut.html) - Właśnie w przypadku kryptowalut są to najczęściej pliki CSV pochodzące z giełd opisujących wykonywan...

20. [Opodatkowanie wirtualnej waluty nabytej nieodpłatnie](https://poradnikprzedsiebiorcy.pl/-opodatkowanie-wirtualnej-waluty-najciekawsze-orzeczenia-organow-podatkowych) - W myśl art. 30b ust. 1a ustawy od dochodów uzyskanych z odpłatnego zbycia walut wirtualnych podatek ...

21. [Sprzedaż waluty wirtualnej: jak rozliczyć przychód?](https://podatki.gazetaprawna.pl/artykuly/10603329,sprzedaz-waluty-wirtualnej-jak-rozliczyc-przychod.html) - Osoba fizyczna prowadzi pozarolniczą działalność gospodarczą w zakresie IT. Przedsiębiorca zamierza ...

22. [Binance Completes the Conversion of BUSD Token ...](https://www.binance.com/en/support/announcement/detail/b7d1cd119211458eb676a9a324edf314) - Binance has completed the conversion of BUSD token balances to FDUSD for eligible users. Users may c...

23. [What Is BUSD Auto-Conversion and How to Deposit ...](https://www.binance.com/en/support/faq/detail/7a2571c63d97459ab4e44a8dd01cf7e8) - Binance has stopped BUSD Auto-Conversion for USDC, USDP, and TUSD that are newly deposited to Binanc...

24. [Przedawnienie zobowiązania podatkowego co do PIT](https://opodatkowanie-marynarzy.pl/przedawnienie-zobowiazania-podatkowego-co-do-pit/) - Zgodnie z przepisami (czyli art. 70 par. 1 Ordynacji podatkowej), zobowiązanie podatkowe przedawnia ...

25. [czyli po ilu latach dokumenty firmy stają się makulaturą](https://www.gazetaprawna.pl/podatki/artykuly/10777461,5-10-50-czyli-po-ilu-latach-dokumenty-firmy-staja-sie-makulatura.html) - Zgodnie z art. 86 par. 1 ordynacji podatkowej „podatnicy obowiązani do prowadzenia ksiąg podatkowych...

