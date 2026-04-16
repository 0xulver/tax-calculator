# Research: Audit the Tax Calculator Implementation and Assumptions

## Objective

We want an external audit of a Polish tax calculator covering cryptocurrency, foreign-source personal income, and JDG ryczalt income. The audit should focus on:

1. whether the legal assumptions are correct
2. whether the available data is being interpreted correctly
3. whether the current processing logic would produce the right Polish tax-form outputs
4. whether any important data is missing, misclassified, double-counted, or ignored

Highest-priority issue:

- whether the calculator is allowed to include a **large pre-Poland cost pool** in Polish PIT-38 at all
- and, separately, whether **pre-residency salary-paid USDC** can become Polish PIT-38 acquisition cost later

Do not assume the implementation is correct. Treat this as an adversarial review.

This is a prompt for an **external research agent**. Do **not** assume you can access any local filesystem, code repository, CSVs, PDFs, or markdown files unless they are explicitly pasted or attached. Work only from the facts stated in this prompt and from your own legal research.

The goal is not a generic Polish crypto-tax memo. The goal is to inspect the described dataset, the described processing rules, and the described form outputs, then identify anything that should be corrected.

---

## Scope

Focus on the Polish filings and the calculations that feed them:

- PIT-38 for crypto capital gains / cost carry-forward
- PIT-36 for pre-JDG foreign-source USDC income
- PIT-28 for JDG ryczalt income
- PIT/ZG where relevant

Swedish issues are out of scope unless they directly change the Polish filing treatment.

This research should **complement** earlier Sweden -> Poland research, not duplicate it.

---

## Prior Research Baseline

Treat the following as **already-researched baseline conclusions** unless you think they are materially incomplete or wrong:

- Polish tax residency begins prospectively from the actual move / transfer of centre of vital interests, not retroactively from January 1, 2023.
- The Poland-Sweden DTT tie-breaker framework has already been analyzed.
- There is **no general Polish immigration step-up** for crypto cost basis.
- Documented pre-residency fiat-to-crypto acquisition costs may be deductible in Poland if they were not already consumed in Sweden.
- Sweden's 10-year rule does not normally reach native crypto.

What this new audit should focus on instead:

- whether the calculator is stretching the old pre-residency cost-basis conclusion too far
- whether the old conclusion about pre-residency costs safely covers **pre-residency salary or compensation paid in USDC**, not just fiat purchases on exchanges
- what evidence standard is needed for that more aggressive position
- whether the implementation should carve out or downgrade the risk of that category even if the broader residency analysis remains correct

Only re-open those older Sweden -> Poland conclusions if the implementation now depends on a nuance they did not squarely answer.

---

## Taxpayer Context

- Swedish citizen
- Moved to Poland on `2023-04-12`
- First Polish tax year assumed by the calculator: `2023`
- JDG started in `2025-05`
- Pre-JDG work was paid in USDC on Polygon
- JDG work in 2025 was invoiced in EUR
- Crypto trading / liquidation activity happened mainly on Binance and Kraken
- Some earlier fiat-to-crypto purchases happened before Polish residency on Celsius/Simplex, Coinbase, and FTX

The calculator currently assumes that pre-Poland acquisition costs can still be carried into Polish PIT-38 once the taxpayer becomes Polish resident.

This must be tested in two separate buckets:

1. **Pre-residency fiat purchases on exchanges / card processors**
   - examples: Celsius/Simplex, Coinbase, FTX
   - the taxpayer can usually show purchase transactions directly
2. **Pre-residency salary or compensation paid in USDC**
   - examples: wallet transfers recorded from on-chain payment history
   - this is the riskier category and should be analyzed separately, not bundled together with exchange purchases

---

## Current Input Data We Have

The list below is a **descriptive inventory**, not something you can directly open unless I separately provide the files.

### 1. Exchange exports

We currently have:

- Binance raw exports for 2020-2025
- Kraken yearly ledger exports covering 2019-12-31 through 2025-12-31
- an FTX core-transactions CSV export
- no raw Coinbase CSV export at present

### 2. Manual structured text inputs for salary / purchases

We also have manually structured text records for:

- pre-residency and post-residency salary / compensation receipts in USDC
- manual Coinbase purchase history
- manual Celsius/Simplex purchase history
- an old FTX manual purchase file that should now be treated as historical only, because FTX is modeled from the real ledger export

Important:

- the manual Coinbase and Celsius/Simplex purchase histories are currently active PIT-38 cost inputs
- the old FTX manual purchase history should no longer be a live PIT-38 source
- part of the manual salary / compensation history predates Polish residency and currently feeds the PIT-38 cost chain
- the manual files use a simple repeating block format:
  - URL or transaction reference
  - date
  - amount + asset
  - optional fee line

### 3. Invoice / business-income documents

We currently have:

- 7 machine-readable XML invoices for 2025 Clearstar JDG income
- 7 Conclave PDF invoices from 2025 that are not yet parsed by code

### 4. ZUS documents

We currently have:

- 8 ZUS DRA documents covering `2025-05` through `2025-12`

These feed the PIT-28 health-insurance deduction assumptions.

### 5. Cached market / FX data

The calculator also uses cached:

- NBP exchange-rate data
- CoinGecko historical price data

### 6. Evidence already available for the risky pre-residency salary-USDC bucket

The taxpayer is not relying only on generic recollection. The supporting material includes or can document:

- on-chain transactions showing receipt / transfer of USDC
- an employment or service contract supporting that those transfers were compensation for work
- Swedish tax returns showing that those amounts were reported and taxed in Sweden

External reviewers should treat this as an evidence-backed scenario, not a bare unsupported claim.

The key legal question is therefore not just whether the receipts happened, but whether that combination of evidence is sufficient to let those pre-residency USDC receipts become Polish PIT-38 acquisition cost after the move.

---

## Current Processing Pipeline

This is a descriptive summary of the calculator logic. Do not assume you can inspect the code unless I separately provide it.

At a high level, the calculator currently does this:

1. normalize Binance, Coinbase, FTX, and Kraken exchange data into a unified transaction model
2. write normalized exchange ledgers
3. run a PIT-38 cost-pool calculation from normalized exchange data plus the manual salary / purchase records
4. generate PIT-38 reports plus separate PIT-36 and PIT-28 reports

Please verify whether those outputs are legally and computationally correct and whether they correspond to the right official forms.

---

## How The Calculator Currently Interprets The Data

### Exchange normalization

There is one exchange normalizer per exchange. The normalizers attempt to convert each exchange export into unified transaction rows with fields such as:

- date
- source
- source transaction ID
- transaction type
- asset
- amount
- fee
- fee asset
- counterparty asset
- counterparty amount
- notes

Please audit whether the exchange-specific normalization rules are correct, especially:

- Binance grouped trade reconstruction
- Kraken trade-leg pairing
- FTX spot-trade parsing and treatment of fiat exchange rows
- Coinbase handling, especially given that no raw Coinbase CSV is currently present

### Manual salary / purchase parsing

The calculator uses one parser for both:

- USDC salary receipts
- manual pre-residency fiat purchases

Current parser behavior:

- `USDC` / `USDT` amounts use USD NBP rate
- `EUR` amounts use EUR NBP rate
- `SEK` amounts use SEK NBP rate
- optional fee lines are added into PLN cost
- if a fee is in the same asset, it also increases the asset amount

Please verify whether this treatment is legally and economically correct.

### PIT-38 engine

The PIT-38 engine currently assumes:

1. Poland uses **annual cost pooling**, not FIFO, for crypto under PIT-38.
2. Taxable revenue is only `crypto -> fiat` disposal.
3. `crypto -> crypto` swaps are not taxable.
4. Fiat spent acquiring crypto is deductible cost.
5. Salary paid in USDC creates PIT-38 acquisition cost at the PLN value already recognized as income.
6. Stablecoin deposits to exchanges can count as PIT-38 cost events if they are not already covered by salary data for that year.
7. Trade fees on taxable `buy` / `sell` rows are deductible.
8. Funding fees and withdrawal-side fees are **not** deductible and are ignored.
9. Stablecoins are treated as virtual currency, not fiat.
10. PLN valuation uses NBP rates when a fiat or stablecoin counterparty exists, otherwise CoinGecko historical PLN price fallback is used.

Please check each of those assumptions separately.

For assumption 5 in particular, do **not** answer at a high level. Split it into:

- salary paid in USDC while already Polish resident
- salary paid in USDC before Polish residency

Those may have different legal outcomes.

### PIT-36 engine

The PIT-36 engine currently assumes:

- Jan-Apr 2025 USDC payments are personal income before JDG
- legal classification: `Art. 13 pkt 8 ustawy o PIT`
- 20% cost deduction applies
- tax scale applies
- kwota wolna is used
- the same PLN value also becomes PIT-38 cost basis later under the barter doctrine
- PIT/ZG should be attached because the payer is foreign

Please audit whether that is the right legal classification and whether the tax computation is correct.

### PIT-28 engine

The PIT-28 engine currently assumes:

- 2025 Clearstar JDG revenue is taxed under ryczalt
- 12% rate for IT / software services
- revenue date is effectively invoice issue date in the current implementation
- EUR invoices are converted using NBP EUR/PLN from the last business day before issue date
- 50% of paid health insurance is deductible

Please audit whether that is the correct form, rate, timing rule, and deduction treatment.

---

## Current Normalized Dataset

Current normalized exchange ledger summary:

- total rows: `1,938`

By source:

- Kraken: `1,087`
- Binance: `754`
- FTX: `97`
- Coinbase: `0` raw normalized rows right now

By transaction type:

- `staking_reward`: `346`
- `deposit`: `274`
- `swap_out`: `216`
- `swap_in`: `216`
- `withdrawal`: `177`
- `buy`: `166`
- `earn_reward`: `132`
- `sell`: `128`
- `fiat_withdrawal`: `120`
- `internal_transfer`: `88`
- `earn_allocation`: `26`
- `airdrop`: `25`
- `interest`: `7`
- `fiat_deposit`: `5`
- `token_swap`: `3`
- `funding_fee`: `2`
- `fiat_exchange`: `2`
- `adjustment`: `2`
- `conversion`: `2`
- `recovery`: `1`

Please verify whether any transaction types are being wrongly ignored, wrongly included, or wrongly mapped.

---

## Current Output Artifacts

If I do not separately paste or attach the generated artifacts, use the summarized figures below rather than pretending to inspect them directly.

The calculator currently produces:

- normalized exchange ledgers per exchange plus a combined normalized ledger
- yearly PIT-38 outputs
- a 2025 PIT-36 report
- a 2025 PIT-28 report
- filing summaries / form-entry guides

---

## Current Reported Results

### PIT-38 carry-forward chain

Current output:

| Tax Year | Carry-forward |
| --- | ---: |
| 2022 -> 2023 | 668,757.92 PLN |
| 2023 -> 2024 | 960,686.74 PLN |
| 2024 -> 2025 | 663,243.77 PLN |
| 2025 -> 2026 | 589,298.07 PLN |

Current 2023-2025 PIT-38 filing values:

#### 2023 PIT-38

- Poz. 34: `411,143.91`
- Poz. 35: `703,072.73`
- Poz. 36: `668,757.92`
- Poz. 37: `0.00`
- Poz. 38: `960,686.74`

#### 2024 PIT-38

- Poz. 34: `785,508.57`
- Poz. 35: `488,065.61`
- Poz. 36: `960,686.74`
- Poz. 37: `0.00`
- Poz. 38: `663,243.77`

#### 2025 PIT-38

- Poz. 36: `271,316.95`
- Poz. 37: `197,371.25`
- Poz. 38: `663,243.77`
- Poz. 39: `0.00`
- Poz. 40: `589,298.07`

### PIT-36 2025

Current output:

- Gross income: `162,735.75 PLN`
- 20% costs: `32,547.15 PLN`
- Taxable income: `130,188.60 PLN`
- Tax base after kwota wolna: `100,189 PLN`
- Tax due: `14,060 PLN`

### PIT-28 2025

Current output:

- Total revenue: `267,794.30 PLN`
- Tax before health deduction: `32,135 PLN`
- Health insurance paid: `5,847.67 PLN`
- Deduction: `2,923.84 PLN`
- Tax due: `29,211 PLN`

The current filing summary treats PIT-28 monthly payments as already paid and expects about `3,077 PLN` refund / overpayment offset.

---

## Known Areas Of Fragility / Possible Error

Please pay special attention to these:

1. **Pre-residency cost basis**
   - Use the earlier Sweden -> Poland research as the starting point, not as a blank slate.
   - Is the calculator right to pull 2020-2022 acquisition costs into the 2023 Polish PIT-38 chain?
   - If yes, under what exact legal theory?
   - If no, which parts must be removed?
   - Answer this separately for:
     - documented fiat purchases on exchanges / processors
     - salary / compensation received in USDC before Polish residency
   - If the answer differs between those categories, say so clearly.

2. **Pre-residency salary-paid USDC is the single riskiest bucket**
   - If someone received USDC as compensation before becoming Polish tax resident, and later disposed of that USDC while Polish resident, can the calculator treat the historical PLN-equivalent value at receipt as Polish PIT-38 cost basis?
   - Does it matter whether that earlier receipt was ever taxed in another jurisdiction, was untaxed, or cannot be tied cleanly to a personal-income filing?
   - Is on-chain proof of receipt enough, or does the taxpayer also need proof of the legal nature of the payment as compensation?
   - In this case, assume the taxpayer can show: on-chain USDC transfers, the employment/service contract, and Swedish tax returns where those amounts were taxed. Does that make the position materially stronger, or is it still legally insufficient?
   - If this bucket is not allowed, should those amounts be excluded entirely from the Polish cost pool?

3. **USDC salary -> PIT-36 + PIT-38 overlap**
   - Is the same PLN value correctly treated as:
     - income at receipt for PIT-36
     - acquisition cost for PIT-38
   - Are there any double-tax / double-deduction issues?

4. **Stablecoin deposits treated as PIT-38 costs**
   - When is this correct?
   - When is it double-counting?
   - Is the current salary-year dedup logic sufficient?

5. **Fee policy**
   - Current logic includes trade fees on `buy` / `sell`
   - Current logic excludes `funding_fee`, `withdrawal`, and `fiat_withdrawal` fees
   - Is that the right line under Polish PIT-38 rules?

6. **Exchange normalization heuristics**
   - Binance grouped trade reconstruction may be wrong if grouped entries combine unrelated legs
   - Kraken trade reconstruction may mis-handle fees or pairings
   - FTX ledger interpretation may still miss economically relevant costs
   - Coinbase currently relies on manual fallback because raw CSV is absent

7. **PIT-36 legal classification**
   - Is `Art. 13 pkt 8` the right basis?
   - Is 20% KUP correct here?
   - Should 2023 and 2024 also be corrected to PIT-36 + PIT/ZG using the same logic?

8. **PIT-28 revenue-date rule**
   - The implementation currently uses invoice issue date
   - Is that always correct for these Clearstar invoices?
   - If payment date or service-completion date should control, which rows change?

9. **Data completeness**
   - Coinbase raw CSV missing
   - Conclave PDFs not parsed into structured data
   - Some historical salary / wallet evidence may still be manual
   - Are we relying on too much hand-entered data?

10. **Ignored transaction classes**
   - `internal_transfer`, `earn_allocation`, `fiat_deposit`, `fiat_withdrawal`, `funding_fee`, `unknown` are currently ignored by PIT-38
   - Is that fully correct?

11. **Valuation fallback**
   - The calculator prefers NBP based on counterparty fiat / stablecoin
   - It falls back to CoinGecko PLN price otherwise
   - Is that correct for each category of event?

---

## What We Need From The External Audit

Please produce a review with these sections:

1. **Bottom-line verdict**
   - Which parts of the current implementation look correct
   - Which parts are likely wrong
   - Which parts are uncertain

2. **Data audit**
   - What source data exists
   - What important data is missing
   - Which data sources are manual proxies rather than primary-source exports
   - Which items should be re-checked first

3. **Legal audit of assumptions**
   - Start from the existing Sweden -> Poland baseline and identify where this calculator is relying on an extension or inference beyond that earlier research.
   - For each major assumption above, say:
     - correct
     - probably correct but risky
     - unclear
     - incorrect
   - Provide legal support at article / interpretation level where possible
   - Explicitly separate:
     - pre-residency exchange purchases
     - pre-residency salary-paid USDC
     - post-residency salary-paid USDC

4. **Implementation audit**
   - Which processing paths look logically sound
   - Which processing paths are likely to misstate tax results
   - Which transaction types or fees are likely mishandled

5. **Form-output audit**
   - Check whether the current outputs really map to the right Polish forms
   - Check whether the PIT-38 positions are correct
   - Check whether PIT-36 and PIT-28 treatment is correct
   - Flag any missing annexes such as PIT/ZG

6. **Corrections**
   - If you think something is wrong, give the corrected rule
   - If possible, say which rows / datasets / form fields would change
   - If possible, estimate the direction of change:
     - higher tax
     - lower tax
     - lower carry-forward
     - higher carry-forward

7. **Risk ranking**
   - Which issues are highest risk if the taxpayer files now
   - Which issues can wait

Please rank the pre-residency salary-USDC question explicitly. If you think that bucket is not supportable, say that plainly even if the rest of the calculator is acceptable.

---

## Desired Standard Of Answer

We want a concrete, audit-style answer, not generic commentary.

Please:

- cite legal sources, official guidance, or serious tax analysis where possible
- separate legal certainty from inference
- identify where the calculator is relying on convenience heuristics
- say explicitly if a result depends on missing evidence
- be willing to disagree with the current assumptions

If you believe the current calculator is materially wrong, say exactly where and why.
