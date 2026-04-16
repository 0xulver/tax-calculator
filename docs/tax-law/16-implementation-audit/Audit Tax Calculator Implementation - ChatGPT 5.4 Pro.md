Important limitation: the repo itself is not mounted in this environment. I could not inspect `src/tax_calc/*`, run `python -m tax_calc full`, or open the listed CSV/JSON/MD artifacts directly. What follows is therefore an adversarial legal/form/output audit of the implementation you described, not a verified line-by-line code review.

## 1. Bottom-line verdict

The broad PIT-38 framework is mostly right. Poland taxes crypto in PIT-38 on disposal, crypto-to-crypto swaps are neutral, unused documented costs carry forward year to year, stablecoins are treated as “waluta wirtualna,” and post-residency remuneration paid in crypto can later become PIT-38 acquisition cost. Your 2023/2024/2025 PIT-38 position mapping is also internally consistent with the official brochures. ([Podatki][1])

The repo’s weakest legal position is **not** the ordinary pre-Poland exchange/card-purchase bucket. Recent KIS practice does support carrying documented pre-residency acquisition costs into Polish PIT-38 when the later disposal is taxed in Poland and the costs were not already consumed abroad. The weakest position is the repo treating **pre-residency salary/compensation paid in USDC** as an ordinary PIT-38 cost bucket. That is an aggressive extension beyond the clearest current authority. With your evidence it is arguable, but I would not treat it as a default low-risk bucket or bundle it with exchange purchases. ([Inforlex][2])

The biggest likely computational errors are these: importing a pre-Poland pool without proving what cost remained **unrecovered** at the move date; treating stablecoin deposits as synthetic PIT-38 costs; using invoice issue date as the PIT-28 revenue date; and letting a foreign payer automatically trigger PIT/ZG. Those are legal-rule errors, not just formatting issues. ([Podatki][1])

Using your own reported numbers, removing the entire disputed 2022 opening carry of 668,757.92 PLN would reduce the 2023 carry to 291,928.82 PLN, flip 2024 to about 5.5k PLN of taxable crypto income, and flip 2025 to about 73.9k PLN of taxable crypto income. So the disputed opening pool is outcome-determinative.

## 2. Data audit

Based on your inventory, the strongest primary-source data are the Binance raw XLSX exports, Kraken ledgers, FTX CSV, Clearstar XML invoices, and the ZUS DRA PDFs.

The weakest evidence is where the repo is using hand-entered proxy files instead of primary exports: `coinbase-purchases.txt`, `celsius-simplex-purchases.txt`, `2022-fantom-salary.txt`, `2022-2023-pre-poland-salary.txt`, and the later salary/invoice text files. Those may be perfectly useful as working papers, but they are not the same as exchange ledgers, bank/card statements, invoices, contracts, or tax returns.

The biggest data gaps are: no raw Coinbase export, Conclave 2025 PDFs not parsed, no visible proof of **payment date** for ZUS health contributions, and no explicit move-date reconciliation showing which pre-Poland cost was still economically “alive” on 2023-04-12.

The first files I would re-check are:

* anything spanning the move date, especially `2022-2023-pre-poland-salary.txt`
* the active manual cost files for Coinbase and Celsius/Simplex
* whether `ftx-purchases.txt` is fully deactivated as a live source
* the unparsed Conclave PDFs
* the documents proving the legal nature of the pre-residency USDC receipts

## 3. Legal audit of assumptions

### PIT-38 core crypto rules

**“Poland uses annual cost pooling, not FIFO.” — Correct in effect, but imprecise in wording.**
The law/MF guidance use an annual aggregation-and-carry-forward mechanism for documented acquisition/disposal costs, not a lot-based FIFO method. That shorthand is acceptable operationally, but the legal rule is art. 22 ust. 14–16 plus PIT-38 carry-forward mechanics. ([Podatki][1])

**“Taxable revenue is only crypto → fiat.” — Incorrect as stated.**
Taxable disposal also includes exchange of crypto for goods, services, other property rights, or settling liabilities. Only crypto-to-crypto exchange is non-taxable. Any code path that taxes only fiat exits and ignores paying obligations in crypto is legally incomplete. ([Podatki][1])

**“Crypto → crypto swaps are not taxable.” — Correct.**
That includes swaps into USDC/USDT, because stablecoins are still “waluta wirtualna,” not fiat. BTC→USDC is not a fiat disposal. ([Podatki][1])

**“Fiat spent acquiring crypto is deductible cost.” — Correct.**
Only documented **direct** acquisition costs and disposal costs count. Financing costs and costs tied to crypto→crypto swaps do not. ([Podatki][1])

**“Trade fees on buy/sell rows are deductible.” — Probably correct, but only when the row is a real PIT-38 acquisition/disposal.**
Fees on fiat→crypto acquisitions and taxable disposals are the safest case. Fees on crypto→crypto trades should not be swept in automatically, because MF guidance excludes costs tied to virtual-currency-for-virtual-currency exchange. ([Podatki][1])

**“Funding fees and withdrawal-side fees are ignored.” — Probably correct.**
MF expressly excludes financing-type costs. Ordinary transfer/withdrawal plumbing is usually not a direct acquisition/disposal cost. ([Podatki][1])

**“USDC/USDT amounts can be valued with USD NBP.” — Usable heuristic, not a clean statutory rule.**
NBP is clearly the right conversion rule for foreign legal currencies. But USDC is not USD in legal form; treating 1 USDC = 1 USD is a practical valuation shortcut, not black-letter law. It is much safer when the underlying receivable/invoice is itself denominated in USD and the stablecoin is merely the settlement medium. ([Podatki][3])

### Residency-transition cost buckets

**Pre-residency exchange/card purchases — Probably correct, but only for unrecovered cost.**
The better reading of current KIS practice is that documented pre-residency purchase costs can be recognized in Polish PIT-38 when the later disposal is taxed in Poland, provided those costs were not already deducted/consumed abroad. That is **not** an immigration step-up. It is a carry-in of documented direct acquisition cost. ([Inforlex][2])

The repo, however, may be stretching that conclusion if it imports a **raw historical purchase total** rather than the amount that remained unrecovered at the migration date. On your own baseline, pre-residency costs are deductible only if they were not already consumed in Sweden. So the opening pool must be limited by a move-date reconciliation, not by “sum of old purchases.” That is the biggest conceptual check on the large 2022→2023 carry.

**Pre-residency salary/compensation paid in USDC — Unclear/aggressive; default inclusion is not supportable.**
The favorable 2025 interpretation on crypto remuneration basis deals with remuneration taxed in Poland when received. Extending that logic to remuneration received **before** Polish residency and taxed in Sweden is an inference, not a directly confirmed rule. Your evidence package—on-chain records, contract/service evidence, and Swedish tax returns—makes the argument materially stronger. But it still does not put this bucket on the same footing as ordinary fiat purchases on exchanges. I would not keep it in the default PIT-38 pool without a separate flag or, ideally, an individual interpretation on this fact pattern. ([Inforlex][4])

On-chain proof alone is not enough for this bucket. It shows receipt, not the legal nature of the transfer. For this category, the minimum serious evidence standard is: transaction hashes, wallet-control mapping, the contract/invoice/payslip or equivalent showing it was compensation, a defensible valuation method at receipt, and proof that the amount was actually taxed abroad.

**Post-residency salary/compensation paid in USDC — Probably correct.**
KIS accepted in 2025 that when remuneration/bonus is settled in crypto and taxed at receipt, the value of the receivable satisfied by that crypto is the acquisition cost for later PIT-38. That is the strong bucket. ([Inforlex][4])

For this bucket, the later PIT-38 cost should track the **gross value of the receivable settled by the crypto**, not the PIT-36 taxable base after 20% KUP. The 20% KUP belong to the service-income side; they do not redefine what was paid to acquire the crypto. The interpretation speaks in terms of the value of the receivable, not the reduced personal-income tax base. ([Inforlex][4])

### 2023 move-date consequence

Using your existing topic-09 baseline, 2023 must be split at **2023-04-12**.
Any 2023 PIT-38 revenue from disposals before that date is suspect. Pre-move 2023 acquisition costs may still be candidates for imported basis under the residency-transition theory, but pre-move disposals are not automatically Polish PIT-38 items. The same date split matters for any 2023 personal-income receipts in crypto.

### PIT-36 assumptions

**PIT-36 for Jan–Apr 2025 pre-JDG income — Probably the right form.**
Where there is no Polish payer withholding and the income is taxed on the scale, PIT-36 is the natural annual return. Foreign-currency amounts are converted using the NBP average rate from the last business day before the income/cost/payment date. ([Podatki][3])

**Art. 13 pkt 8 + 20% KUP — Plausible, but contract-dependent.**
Official PIT-36 guidance confirms 20% KUP for umowy zlecenia / o dzieło under art. 13 pkt 8. So the repo’s classification is supportable **if** the actual contract is really that kind of civil-law service/work contract. But your record describes “employment or service contract.” If it is actually employment, art. 13 pkt 8 is not the right classification. I cannot sign off on art. 13 pkt 8 without the actual contract. ([Podatki][3])

**“The same PLN value is PIT-36 income and later PIT-38 cost.” — Correct for the post-residency Poland-taxed bucket.**
That is the anti-double-taxation logic accepted by KIS. It is not an impermissible double deduction. ([Inforlex][4])

**“PIT/ZG should be attached because the payer is foreign.” — Too broad.**
Official PIT-36/PIT-ZG instructions key off income from activity performed abroad or from foreign sources taxed in Poland under the relevant methods. Foreign payer status alone is not the legal test. ([Podatki][3])

**Should 2023 and 2024 also be reviewed for PIT-36 corrections? — Yes.**
If post-2023-04-12 USDC compensation in those years was treated only as PIT-38 cost input and not as personal income at receipt, the repo is likely missing the non-business income side for those years.

### PIT-28 assumptions

**PIT-28 for 2025 JDG ryczałt — Probably correct, if ryczałt was validly chosen.**
**12% rate — probably correct only if the actual services fit the listed IT/software PKWiU categories.** It is not automatic for everything vaguely called “IT.” ([Podatki][5])

**“Revenue date = invoice issue date.” — Probably wrong.**
For business income, the default rule is the day of performance / partial performance, no later than invoice date or payment date. Ryczałt piggybacks on the business-income timing rules. So invoice date is an upper bound, not the universal rule. ([ISAP][6])

**“50% of health insurance is deductible.” — Correct, but only for amounts actually paid.**
The statute/official guidance talk about 50% of the health contributions **paid** in the tax year, evidenced by documents showing the outlay. DRA declarations alone are not payment proof. ([Podatki][7])

## 4. Implementation audit

Because I could not read the code, I cannot sign off on the Binance/Kraken/FTX/Coinbase normalizers themselves. But on the described logic, these are the highest-risk implementation defects:

* A **deposit should never create PIT-38 cost by itself**. A deposit is transfer plumbing. It can point to an upstream acquisition source; it is not itself an acquisition expenditure. The current “stablecoin deposit can count as cost if not already covered by salary_years” rule is likely wrong and highly double-count-prone. ([Podatki][1])

* **Dedup by year is not enough.** Double counting can happen across salary files, manual purchase files, exchange buys, and later deposits even when the years differ. Dedup needs provenance-level linking, not `salary_years`.

* **The same parser should not drive manual purchases and compensation receipts with the same fee logic.** For purchases, processor/exchange fees may be acquisition cost. For compensation receipts, later wallet-transfer fees usually are not. The current design is legally too coarse.

* **“Fee in same asset increases asset amount” is likely wrong** unless the file format explicitly records a net asset amount and the code is reconstructing gross units. Otherwise it overstates both quantity and cost.

* The engine must classify by **counterparty type**, not by exchange label. If a normalizer treats BTC/USDC as a fiat “sell” or “buy,” the PIT-38 result is wrong because USDC is virtual currency, not fiat. ([Podatki][1])

* Ignoring `internal_transfer`, `fiat_deposit`, and `fiat_withdrawal` as tax events is generally fine. But `staking_reward`, `earn_reward`, `interest`, `airdrop`, `adjustment`, `recovery`, `conversion`, and `token_swap` should not sit in a generic ignore bucket without a separate legal policy. Some may be zero-cost acquisitions for later sale; some may imply non-PIT-38 income issues.

* Data completeness is not proven while Coinbase raw data are missing and Conclave invoices remain unparsed.

## 5. Form-output audit

**PIT-38**
Your stated 2023, 2024, and 2025 PIT-38 line mappings are correct, and the arithmetic is internally consistent with the official brochure logic. For 2025, poz. 36 = revenue, poz. 37 = current-year costs, poz. 38 = prior carry, poz. 39 = income, poz. 40 = new carry. For 2023/2024 the numbering is one step earlier. The problem is not the form algebra; it is the substantive composition of the carry and current-year cost buckets. ([Podatki][8])

**PIT-36 2025**
The reported math is internally coherent **if** art. 13 pkt 8 is right: 20% of 162,735.75 is 32,547.15; taxable amount 130,188.60 rounds to 130,189; on the 2025 scale that gives 14,060 tax after rounding. But “tax base after kwota wolna = 100,189” is not the actual form logic; the form uses the rounded base and the scale with the 3,600 zł tax-reducing amount. PIT/ZG also is not automatic from foreign payer status alone. ([Podatki][3])

**PIT-28 2025**
The arithmetic is also internally coherent: 267,794.30 × 12% ≈ 32,135, then less 2,923.84 gives about 29,211. But I would not treat that as filing-ready yet, because one invoice folder is still unparsed, the revenue-date rule is likely too broad, and the health deduction depends on amounts actually paid in 2025, not merely shown on DRA forms. ([Podatki][5])

## 6. Corrections

1. **Split the pre-Poland PIT-38 opening pool into separate legal buckets.**
   Bucket A: documented fiat purchases on exchanges/processors.
   Bucket B: pre-residency salary/compensation paid in USDC.
   Bucket C: post-residency Poland-taxed salary/compensation paid in USDC.
   Only Bucket A is reasonably supportable as default. Bucket B should be excluded from the default pool or marked “aggressive/optional.” Bucket C is the strongest salary bucket.
   **Direction:** lower carry-forward if Bucket B is removed.

2. **Rebuild the imported pool as “unrecovered cost at move date,” not “sum of historical acquisitions.”**
   That means reconciling pre-Poland disposals/swaps under the prior residence period and limiting imported cost to what remained economically unconsumed on 2023-04-12.
   **Direction:** likely lower 2022→2023 carry-forward.

3. **Do not let deposits create cost.**
   Deposits should link to upstream source records; they should not manufacture PIT-38 basis.
   **Direction:** lower carry-forward, higher later PIT-38 tax.

4. **Split 2023 at 2023-04-12.**
   Pre-move disposals should not be treated as Polish PIT-38 revenue. Any post-move compensation receipts in 2023 should be reviewed for PIT-36 treatment, not left only in the PIT-38 cost chain.
   **Direction:** likely lower 2023 PIT-38 revenue if pre-move sales are currently included; potentially higher 2023 PIT-36 exposure.

5. **For post-residency crypto remuneration, use the gross remuneration value as PIT-38 basis.**
   Do not reduce later basis by the PIT-36 20% KUP.
   **Direction:** if the repo currently uses net taxable income as basis, future carry-forward should rise.

6. **Change PIT-28 revenue recognition.**
   Use the legally correct revenue date under art. 14, then use the corresponding FX date.
   **Direction:** monthly ryczałt and overpayment estimates may change; annual total may also change around year-end boundaries.

7. **Health deduction must be payment-based.**
   DRA PDFs are not enough by themselves; use bank/ZUS payment evidence.
   **Direction:** 2025 PIT-28 deduction may decrease.

8. **Obtain the missing primary data.**
   Raw Coinbase export, parsed Conclave invoices, and original purchase/payment proofs for manual files should be treated as blocking items for a serious filing package.
   **Direction:** unknown on tax amount, high on audit defensibility.

## 7. Risk ranking

1. **Pre-residency salary/compensation paid in USDC included as ordinary PIT-38 cost**
   This is the single highest-risk issue. My view: not supportable as a default low-risk bucket. At most it is an aggressive position that should be isolated and ideally covered by an individual interpretation. ([Inforlex][4])

2. **Imported pre-Poland pool not limited to unrecovered cost at move date**
   Legally, imported direct purchase cost may be fine; importing a raw historical pool is not. This can materially overstate every later carry figure.

3. **Stablecoin deposits treated as PIT-38 costs / year-based dedup**
   High risk of double counting.

4. **Post-move 2023/2024 compensation not separately treated under PIT-36**
   If those years currently feed only PIT-38 cost, that is a substantive filing gap.

5. **PIT-28 incompleteness and timing**
   Unparsed Conclave PDFs, invoice-date heuristic, and payment-vs-DRA health deduction all weaken the 2025 result.

6. **Missing Coinbase raw data and reliance on manual proxy files**
   This is as much an evidence risk as a calculation risk.

7. **Residual normalization/fee/reward classification issues**
   Important, but lower than the structural basis and form-classification issues above.

On the current record, I would **not** file from the calculator unchanged. The 2023–2025 PIT-38 algebra looks fine, but the opening cost pool and several feeder assumptions are not yet audit-safe.

[1]: https://www.podatki.gov.pl/podatki-osobiste/pit/informacje-podstawowe/co-jest-opodatkowane/zbycie-kryptowalut/ "https://www.podatki.gov.pl/podatki-osobiste/pit/informacje-podstawowe/co-jest-opodatkowane/zbycie-kryptowalut/"
[2]: https://www.inforlex.pl/dok/tresc%2CFOB0000000000006573410%2CInterpretacja-indywidualna-z-dnia-28-marca-2024-r-Dyrektor-Krajowej-Informacji-Skarbowej-sygn-0113-KDIPT2-3-4011-18-2024-2-NM.html "https://www.inforlex.pl/dok/tresc%2CFOB0000000000006573410%2CInterpretacja-indywidualna-z-dnia-28-marca-2024-r-Dyrektor-Krajowej-Informacji-Skarbowej-sygn-0113-KDIPT2-3-4011-18-2024-2-NM.html"
[3]: https://www.podatki.gov.pl/media/i11o5dtk/broszura-do-pit-36-za-2025-r.pdf "https://www.podatki.gov.pl/media/i11o5dtk/broszura-do-pit-36-za-2025-r.pdf"
[4]: https://www.inforlex.pl/dok/tresc%2CFOB0000000000006885875%2CInterpretacja-indywidualna-z-dnia-4-marca-2025-r-Dyrektor-Krajowej-Informacji-Skarbowej-sygn-0115-KDIT1-4011-22-2025-1-MR.html "https://www.inforlex.pl/dok/tresc%2CFOB0000000000006885875%2CInterpretacja-indywidualna-z-dnia-4-marca-2025-r-Dyrektor-Krajowej-Informacji-Skarbowej-sygn-0115-KDIT1-4011-22-2025-1-MR.html"
[5]: https://www.podatki.gov.pl/podatki-firmowe/pit/stawki-i-limity/ "https://www.podatki.gov.pl/podatki-firmowe/pit/stawki-i-limity/"
[6]: https://isap.sejm.gov.pl/isap.nsf/download.xsp/WDU20160002032/U/D20162032Lj.pdf "https://isap.sejm.gov.pl/isap.nsf/download.xsp/WDU20160002032/U/D20162032Lj.pdf"
[7]: https://www.podatki.gov.pl/podatki-firmowe/pit/informacje-podstawowe/co-jest-opodatkowane/opodatkowanie-ryczaltem-od-przychodow-ewidencjonowanych/ "https://www.podatki.gov.pl/podatki-firmowe/pit/informacje-podstawowe/co-jest-opodatkowane/opodatkowanie-ryczaltem-od-przychodow-ewidencjonowanych/"
[8]: https://www.podatki.gov.pl/media/g5ebnm2e/broszura-do-pit-38-za-2025-r.pdf "https://www.podatki.gov.pl/media/g5ebnm2e/broszura-do-pit-38-za-2025-r.pdf"
