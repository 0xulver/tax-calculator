# 1. Verdict

**File with changes / risk disclosures, not “clean ready to file.”**

The arithmetic supplied is internally consistent, the PIT-38 field mapping for 2023/2024/2025 is broadly correct, and Polish sources now support the general idea that documented pre-residency fiat/direct crypto acquisition costs can be brought into PIT-38 after becoming Polish resident. However, the selected posture’s **Layer C successor/replacement basis through crypto-to-crypto and DeFi transformations remains the main high-risk item**. Polish law expressly excludes expenses connected with crypto-to-crypto exchanges from tax costs, and recent KIS/court materials draw a sharp line between documented fiat/direct purchases and crypto-to-crypto “costs.” ([ISAP][1])

I could **not access the local filing files** you listed. Therefore I cannot certify that the event tables, duplicate controls, NBP rates, or private evidence files actually support the proposed values. The exact files needed are:

`outputs/pit38_max_no_debt_plus_oath_weth_dola_tge_rfgrain/pit38_results.json`, `pit38_detail.json`, `pit38_report_2023.md`, `pit38_report_2024.md`, `pit38_report_2025.md`, `outputs/normalized_all_exchanges.csv`, and the private evidence workpapers under `private/evidence/onchain/move-date-inventory-2023-04-12/`. These are needed to verify event totals, cost dates, NBP rates, duplicate source IDs, and the imported-basis tracing.

# 2. Critical corrections before filing

**No arithmetic field change is required based only on the numbers supplied.** The three carry-forwards calculate correctly.

The critical change is **presentation and legal framing**, especially for 2023 poz. 36. The 2023 PIT-38 brochure says poz. 36 is the amount from 2022 PIT-38 poz. 38: prior-year virtual-currency costs not deducted before 1 January 2023.  A 2025 KIS interpretation supports showing pre-residency costs for the first year of Polish residence, including use of the relevant PIT-38 cost positions, but it also says crypto-to-crypto exchange expenses cannot be treated as costs. ([Interpretacje][2])

Before filing, do these three checks:

1. **Break the 588,848.16 PLN imported basis by actual cost-incurrence year.** If any imported acquisition cost was incurred in 2023 before 2023-04-12, it should likely be in **2023 poz. 35**, not poz. 36. If all imported basis is pre-2023, poz. 36 is more defensible.

2. **Remove or segregate any Layer C amount that is based on crypto-to-crypto FMV, swap proceeds, swap fees, CDP/stability fees, debt principal, rewards, vesting, or “valuation uplift.”** Only original documented fiat/direct/taxed-remuneration acquisition expenditure should be claimed.

3. **Attach or retain a clear audit note** explaining that 2023 poz. 36 is being used for documented pre-Polish-residency acquisition costs of move-date crypto assets, not a synthetic full-history Polish crypto pool.

If the taxpayer wants a **lower-risk conservative filing that excludes all Layer C** and keeps only Layer A imported basis of 77,955.80 PLN, the resulting chain would be:

| Year |    Revenue | Current costs | Prior/imported costs |    Income | Carry-forward |
| ---: | ---------: | ------------: | -------------------: | --------: | ------------: |
| 2023 | 264,113.82 |    500,922.56 |            77,955.80 |      0.00 |    314,764.54 |
| 2024 | 785,654.54 |    488,065.61 |           314,764.54 |      0.00 |     17,175.61 |
| 2025 | 271,316.95 |    215,310.63 |            17,175.61 | 38,830.71 |          0.00 |

That conservative variant would create approximately **7,378 PLN tax for 2025** after rounding the tax base to 38,831 PLN and applying 19%.

# 3. Legal-risk findings

## High risk

**Layer C DeFi / crypto-to-crypto successor basis.** Polish PIT treats crypto-to-fiat, crypto-to-goods/services/property rights other than virtual currency, and settlement of obligations with crypto as taxable paid disposals; crypto-to-crypto is outside the direct disposal definition. ([ISAP][1]) But the PIT Act also states that expenses connected with exchanging one virtual currency for another are not tax-deductible costs. ([ISAP][1]) Recent materials on pre-residency cost importation support historical fiat/direct purchase costs, but they expressly reject crypto-to-crypto exchange expenses. ([Interpretacje][2])

**Borrowed/debt-sourced tokens and CDP mechanics.** Excluding ERN debt proceeds and ERN-funded legs is correct. A WSA Gdańsk case on DAI/CDP mechanics treated DAI-to-fiat as taxable revenue and rejected a stability fee as a cost because it was not directly incurred to acquire or dispose of DAI; the reasoning is adverse to claiming CDP/debt mechanics as acquisition cost. ([Lexedit][3])

**Evidence not independently reviewed.** I could not access the private evidence files or the report event tables. That blocks an actual evidence audit of WBTC, GTRAIN, OATH, BPT-RESERVE, Paymonade repairs, duplicate rows, and NBP rows.

## Medium risk

**Split-year residency date.** The split-year model is defensible if 2023-04-12 is in fact the date Polish tax residence began. Polish residents are taxed on worldwide income; nonresidents are taxed only on Polish-source income. ([ISAP][1]) The package should retain move-date facts, Swedish residence evidence, and any treaty tie-breaker support.

**2023 poz. 35 vs poz. 36 allocation.** The field total effect is usually nil because both fields feed the same annual crypto cost sum, but field correctness matters. Same-year pre-residency costs look more like 2023 costs; pre-2023 costs look more like poz. 36 import/prior costs, based on the 2025 KIS analogue. ([Interpretacje][2])

**Crypto remuneration.** Post-residency crypto remuneration taxed in Poland on receipt can be treated as acquisition cost for PIT-38 when later disposed, if the value of the receivable/wage/service fee settled by crypto is documented. KIS treated receipt of crypto for services as paid acquisition, with cost equal to the settled receivable/remuneration value. ([Inforlex][4])

## Low risk

**Field mapping and annual pooling.** 2023 and 2024 use poz. 34–38 for virtual currency. 2025 uses poz. 36–40. The official brochures confirm these mappings.  The statutory method is annual revenue less annual/current/prior crypto costs, not FIFO; the PIT-38 sections use annual sums and cost carry-forward. ([ISAP][1])

# 4. Direct answers to the legal questions

1. **Split-year approach:** yes, if 2023-04-12 is the correct Polish residence start date and pre-residency disposals were not Polish-source.
2. **Pre-residency basis:** yes for documented fiat/direct acquisition costs not previously deducted; KIS supports first showing them in PIT-38 for the year Polish residence begins. ([Interpretacje][2])
3. **Proof standard:** source documents proving direct expenditure: exchange statements, bank transfers, payroll/service invoices if crypto remuneration, dates, quantities, FX conversions, move-date holdings, and no prior deduction.
4. **Layer C through swaps/wrappers/LPs:** acceptable only as factual tracing of original documented cost, not as a new cost from crypto-to-crypto swaps or DeFi mechanics. This is high risk.
5. **Haircuts:** haircut or exclude any Layer C bucket whose basis is FMV at a swap, a debt leg, reward/vesting, a stability/financing fee, or an unsupported receipt token.
6. **Debt-sourced tokens:** correctly excluded unless a separate direct acquisition expenditure exists.
7. **BPT-RESERVE:** correctly excluded by default if ERN/CDP debt-sourced or potentially duplicative of WBTC collateral.
8. **OATH split:** reasonable in concept: include paid WETH/DOLA/WFTM-side components only if traced; exclude native/vesting/reward buckets.
9. **Post-residency crypto remuneration:** yes, if taxed on receipt and documented; cost equals the value of remuneration/receivable settled by crypto. ([Inforlex][4])
10. **Field mappings:** yes: 2023/2024 poz. 34–38; 2025 poz. 36–40. 
11. **2024 correction vs first filing:** correction if e-Urząd/Twój e-PIT shows a filed or auto-accepted PIT-38; first/late filing if no PIT-38 was filed. Twój e-PIT auto-accepts PIT-37/PIT-38 after 30 April if not rejected or separately filed. ([Podatki][5])
12. **Filing order / czynny żal:** file 2023 correction first, then 2024, then 2025, because 2024 uses the 2023 carry-forward and 2025 uses the 2024 carry-forward. Use czynny żal for any truly late first filing, especially 2024 if no auto-accepted return exists; corrections themselves may benefit from KKS art. 16a if legally effective and any tax arrears are paid. ([ISAP][6])

# 5. Arithmetic findings

The supplied arithmetic is correct:

| Check              |                                                Result |
| ------------------ | ----------------------------------------------------: |
| Imported basis sum |                                        588,848.16 PLN |
| 2023 carry-forward | 500,922.56 + 588,848.16 − 264,113.82 = 825,656.90 PLN |
| 2024 carry-forward | 488,065.61 + 825,656.90 − 785,654.54 = 528,067.97 PLN |
| 2025 carry-forward | 215,310.63 + 528,067.97 − 271,316.95 = 472,061.65 PLN |

The imported-basis component total is also exact:

77,955.80 + 142,580.44 + 44,138.35 + 5,292.90 + 25,964.04 + 100,518.44 + 159,526.15 + 17,172.86 + 15,596.93 + 102.25 = **588,848.16 PLN**.

The three Paymonade repairs look arithmetically reasonable under the NBP “last business day before” rule, which the official PIT-38 brochure states for foreign-currency amounts. 

| Event                               |                                                                                 Rate check |                     PLN check |
| ----------------------------------- | -----------------------------------------------------------------------------------------: | ----------------------------: |
| 2025-06-20, 2,000 EUR cost          | 4.2717 from the prior NBP business table because 2025-06-19 was not a normal NBP table day |     2,000 × 4.2717 = 8,543.40 |
| 2025-06-22, 2,200 EUR cost          |                                                                     4.2709 from 2025-06-20 |     2,200 × 4.2709 = 9,395.98 |
| 2024-11-04, 33.53231693 EUR revenue |                                                                     4.3530 from 2024-10-31 | 33.53231693 × 4.3530 = 145.97 |

NBP sources found match the relevant EUR rates: 4.2717 for table 117/A/NBP/2025, 4.2709 for table 118/A/NBP/2025, and 4.3530 for table 213/A/NBP/2024. ([NBP][7])

Not verified due missing files: annual event-table sums, duplicate row suppression, all NBP rows, and whether current-year salary/purchase/override rows are counted only once.

# 6. Evidence findings

These classifications are **provisional only**, based on your description. I did not see the actual workpapers.

| Bucket                                                  | Provisional classification                                                  | Audit comment                                                                                                                                  |
| ------------------------------------------------------- | --------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| Koinly-matched reviewable move-date rows, 77,955.80 PLN | **Adequate for filing now**, if backed by exchange/bank primary records     | Koinly alone is not enough; Koinly plus exchange exports, bank evidence, and move-date balance tie-out is acceptable.                          |
| Ethos WBTC trove collateral, 142,580.44 PLN             | **Weak but defensible**                                                     | Defensible only if original WBTC acquisition cost, collateral continuity, Reaper recovery/source-open, and no ERN double count are documented. |
| GLP USDC.e predecessor, 44,138.35 PLN                   | **Weak but defensible**                                                     | Needs proof that this is original fiat/stablecoin acquisition cost traced into a surviving DeFi receipt, not a crypto-to-crypto FMV reset.     |
| `rf-soWETH` WETH inputs, 5,292.90 PLN                   | **Weak but defensible**                                                     | Wrapper/receipt treatment can be defended if WETH input cost is original documented cost and not a swap cost.                                  |
| BPT-GTRAIN ETH-only input, 25,964.04 PLN                | **Weak but defensible**                                                     | Needs Balancer receipt trace and proof that the ETH input had documented cost.                                                                 |
| BPT-GTRAIN stablecoin-funded GRAIN, 100,518.44 PLN      | **Weak but defensible**                                                     | Higher scrutiny: must prove the GRAIN source is paid/direct and not reward/debt/duplicated stablecoin basis.                                   |
| WETH/OATH LP WETH-linked component, 159,526.15 PLN      | **Weak but defensible**                                                     | Large amount; needs exact LP input split and proof the WETH-linked basis is not also claimed elsewhere.                                        |
| WETH/OATH LP DOLA-funded OATH, 17,172.86 PLN            | **Weak; possibly not defensible if DOLA was debt-derived**                  | Must prove DOLA was acquired with direct cost and not ERN/CDP debt or WBTC-derived debt branch.                                                |
| OATH TGE/LGE WFTM payment proof, 15,596.93 PLN          | **Weak but defensible**                                                     | Payment-side proof can create cost basis if WFTM paid was itself acquired for direct cost or taxed income. No reward/vesting uplift.           |
| `rf-grain-OP` survivor, 102.25 PLN                      | **Adequate for filing now if trace is clean**                               | Immaterial; keep if OP-funded acquisition trace is simple.                                                                                     |
| 2025 Paymonade EUR purchases                            | **Adequate for filing now**, if bank/merchant and Binance ledger both exist | NBP math checks. Need duplication check against Binance raw import.                                                                            |
| 2024 Paymonade ETH sale                                 | **Adequate for filing now**, if manual repair is tied to the Binance event  | NBP math checks; amount is immaterial but should be traceable.                                                                                 |

# 7. Double-counting findings

The main double-counting risk is **WBTC collateral vs ERN/DOLA/LP/gauge positions**. If ERN or DOLA arose from a CDP/debt branch collateralized by the same WBTC, including both the WBTC collateral basis and downstream ERN/DOLA-funded LP/OATH/BPT basis would likely duplicate the same economic basis.

Specific double-counting checks required before filing:

1. **WBTC collateral vs BPT-RESERVE / ERN-funded legs:** BPT-RESERVE should stay excluded unless the evidence proves an independent paid acquisition source.
2. **DOLA-funded OATH vs WBTC DOLA branch:** include only if DOLA was independently paid-for, not borrowed/minted or already represented by WBTC collateral basis.
3. **GTRAIN stablecoin-funded GRAIN:** verify the stablecoin funding is not the same stablecoin basis counted in GLP, OATH, or other LP receipts.
4. **Paymonade overrides:** verify the manual rows replace broken ledger rows rather than adding on top of them.
5. **Crypto remuneration:** verify the same receipt is not counted both as taxable remuneration cost and as a later fiat purchase/manual cost.

# 8. Excluded-item findings

The current excluded list is generally prudent.

| Excluded item                                         | Finding                                                                                                                                                                               |
| ----------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ERN debt proceeds and ERN-funded legs                 | **Leave excluded.** Debt/minted tokens are not direct acquisition expenditure; high double-count risk.                                                                                |
| BPT-RESERVE                                           | **Leave excluded by default.** Re-add only with proof of independent paid source and no WBTC/ERN overlap.                                                                             |
| OATH-native bridge/reward/vesting/distributor buckets | **Leave excluded.** Rewards/vesting/native allocations need separate valuation and income-recognition analysis.                                                                       |
| Unsupported LP/vault balances                         | **Leave excluded.** Unsupported DeFi receipt balances are the weak point under art. 22(14).                                                                                           |
| Avalanche `frxETH` / `sfrxETH`                        | **Leave out of imported basis** if position starts after Polish residence; treat only under current-year Polish costs if acquired post-residency with documented cost.                |
| Pre-residency salary-paid USDC                        | **Do not include merely because it was salary.** It could be supportable only if salary/taxed-remuneration value, receipt date, surviving tokens, and non-duplication are documented. |

# 9. Questions that must be answered by the taxpayer

1. Do the imported-basis files show any acquisition costs incurred in **2023 before 2023-04-12**? If yes, those amounts may need to move from 2023 poz. 36 to poz. 35.

2. Does any Layer C amount use **crypto-to-crypto fair value, swap proceeds, swap fees, stability fees, or debt principal** rather than original documented fiat/direct/taxed-remuneration cost?

3. Is the DOLA-funded OATH component independent of the WBTC/ERN/CDP branch?

4. Does e-Urząd show an auto-accepted or otherwise submitted **2024 PIT-38**? If yes, submit a correction; if no, submit first/late PIT-38 with czynny żal.

5. Can the missing files be produced for final audit? Without them, the event-table and evidence audit remains unperformed.

# 10. Recommended filing wording

## Polish correction/audit-note wording for 2023

> Korekta dotyczy uzupełnienia części E zeznania PIT-38 o przychody i koszty z odpłatnego zbycia walut wirtualnych. Wykazane koszty obejmują udokumentowane, nierozliczone wydatki bezpośrednio poniesione na nabycie walut wirtualnych, w tym koszty poniesione przed uzyskaniem polskiej rezydencji podatkowej, dotyczące walut wirtualnych posiadanych na dzień uzyskania rezydencji podatkowej w Polsce i rozliczanych po tej dacie. Kwoty nie stanowią syntetycznego odtworzenia pełnej historii transakcji, lecz udokumentowany koszt nabycia przypisany do aktywów posiadanych na dzień zmiany rezydencji. Szczegółowe zestawienie transakcji, kursów NBP oraz dowodów nabycia jest przechowywane przez podatnika.

If poz. 36 includes pre-residency imported costs and there was no 2022 Polish PIT-38:

> Kwota wykazana w poz. 36 obejmuje udokumentowane koszty nabycia walut wirtualnych poniesione przed polską rezydencją podatkową i nierozliczone wcześniej dla celów podatkowych. Podatnik nie składał polskiego PIT-38 za 2022 r., ponieważ w tym okresie nie był polskim rezydentem podatkowym.

## English audit-note wording

> The 2023 PIT-38 position imports only documented acquisition costs for crypto assets held at the Polish tax-residency start date and later relevant to Polish taxable disposals. It does not reconstruct a synthetic full-history Polish crypto pool. Crypto-to-crypto transactions are not treated as direct Polish PIT-38 revenue or cost events; they are used only as factual tracing links where they preserve original documented acquisition cost.

## Czynny żal wording for a late first 2024 PIT-38

> Działając na podstawie art. 16 Kodeksu karnego skarbowego, zawiadamiam o niezłożeniu w terminie zeznania PIT-38 za 2024 r. Uchybienie wynikało z konieczności odtworzenia i zweryfikowania historii transakcji walut wirtualnych oraz kosztów przenoszonych z lat poprzednich. Zeznanie PIT-38 za 2024 r. zostało złożone niezwłocznie po zakończeniu weryfikacji. Z zeznania nie wynika podatek do zapłaty. Proszę o potraktowanie niniejszego pisma jako czynnego żalu.

If any tax is due, add:

> Podatek wraz z należnymi odsetkami został uiszczony / zostanie uiszczony niezwłocznie.

Final practical recommendation: **file the proposed zero-tax chain only with an explicit imported-basis audit note and after confirming the Layer C amounts are not crypto-to-crypto FMV/debt/stability-fee costs.** Otherwise, use the conservative Layer-A-only variant or seek an individual interpretation for Layer C.

[1]: https://isap.sejm.gov.pl/isap.nsf/download.xsp/WDU19910800350/U/D19910350Lj.pdf "Akt prawny"
[2]: https://www.interpretacje.pl/pit/9793755%2Cinterpretacjaindywidualna-stanowisko-prawidlowe-interpretacja-0.html "Interpretacja
indywidualna – stanowisko prawidłowe - Interpretacja - 0113-KDIPT2-3.4011.205.2025.2.NM - "
[3]: https://lexedit.ai/orzeczenia/i-sa-gd-13-25/wymiana-dai-na-walute-fiducjarna-przychodem-stability-fee-nie-kosztem "I SA/Gd 13/25 - Wojewódzki Sąd Administracyjny w Gdańsku oddalił skargę poda... | Lexedit"
[4]: https://www.inforlex.pl/dok/tresc%2CFOB0000000000006354149%2CInterpretacja-indywidualna-z-dnia-27-pazdziernika-2023-r-Dyrektor-Krajowej-Informacji-Skarbowej-sygn-0114-KDIP3-1-4011-797-2023-1-PT.html "
  Interpretacja indywidualna z dnia 27 października 2023 r., Dyrektor Krajowej Informacji Skarbowej, sygn. 0114-KDIP3-1.4011.797.2023.1.PT -
    INFORLEX Freemium
  "
[5]: https://www.podatki.gov.pl/twoj-e-pit/pytania-i-odpowiedzi/nadplatapodatek-do-zaplaty/103-co-w-przypadku-jesli-z-zeznania-automatycznie-zaakceptowanego-wynika-podatek-do-zaplaty/ "Serwis o podatkach - 10.3 Co w przypadku, jeśli z zeznania automatycznie zaakceptowanego wynika podatek do zapłaty?  "
[6]: https://isap.sejm.gov.pl/isap.nsf/download.xsp/WDU19990830930/U/D19990930Lj.pdf "Akt prawny"
[7]: https://nbp.pl/archiwum-kursow/tabela-nr-117-a-nbp-2025-z-dnia-2025-06-18/?utm_source=chatgpt.com "Tabela nr 117/A/NBP/2025 z dnia 2025-06-18"
