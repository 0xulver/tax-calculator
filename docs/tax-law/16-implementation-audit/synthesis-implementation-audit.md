# Synthesis: Tax Calculator Implementation Audit

Sources: ChatGPT 5.4 Pro, ChatGPT Deep Research, Gemini 3.1 Deep Research

Important limitation: these responses were generated from the **old prompt**, so the external agents could not actually inspect the local repo, source files, normalized ledgers, or generated outputs directly. This synthesis is therefore a synthesis of their **legal and conceptual audit**, not a verified line-by-line implementation review.

---

## High-Confidence Consensus

### 1. The core PIT-38 framework is broadly right
All three reports accept the broad structure of the crypto calculator:

- Poland uses annual aggregation / cost carry-forward for crypto rather than FIFO lot matching in the filing itself
- crypto-to-crypto swaps are non-taxable
- direct acquisition/disposal costs can feed PIT-38
- stablecoins are treated as virtual currency rather than fiat
- trade fees on taxable buy/sell activity are generally the right kind of cost
- funding / withdrawal style fees are generally safer to exclude

So the project is **not fundamentally wrong** on the main PIT-38 architecture.

### 2. Pre-residency fiat purchases are much stronger than pre-residency salary-paid USDC
All three reports distinguish between two very different pre-Poland buckets:

1. **documented fiat-to-crypto purchases** made before Polish residency
2. **salary / compensation received in USDC** before Polish residency

The strong consensus is:

- the first bucket is at least plausibly supported under current KIS practice, if properly documented and not already consumed / deducted abroad
- the second bucket is the single biggest legal risk in the whole calculator

This is the most important answer from the topic.

### 3. Pre-residency salary-paid USDC should not be treated as a safe default filing position
This is the clearest consensus across the responses.

All three effectively say that the calculator is overreaching if it treats **pre-residency compensation paid in USDC** as normal Polish PIT-38 cost basis by default.

The reasoning is consistent:

- Polish barter doctrine clearly supports post-residency Polish-taxed crypto compensation becoming later PIT-38 basis
- it does **not** clearly and directly support importing that same logic backward into a foreign tax period
- on-chain transfers, contracts, and Swedish tax returns make the facts better, but do not by themselves create a clear Polish statutory basis

The practical synthesis is:

- **documented pre-residency exchange/card purchases** can stay in the “plausible / supportable” bucket
- **pre-residency salary-paid USDC** belongs in an “aggressive / optional / interpretation-needed” bucket, not in the default carry-forward chain

### 4. Stablecoin deposits should not create PIT-38 cost by themselves
This is another strong point of agreement.

The current idea that a stablecoin deposit may become a PIT-38 cost event if salary data do not already cover that year is viewed as legally weak and highly vulnerable to double counting.

The reports consistently prefer this rule:

- deposits are transfers / reconciliation events
- actual PIT-38 cost should come from the underlying acquisition event
  - exchange purchase
  - card purchase
  - Polish-taxed compensation receipt

### 5. Manual proxy files are a major audit weakness
All three reports treat the manual `.txt` inputs as working papers rather than filing-grade primary evidence.

The most repeated weaknesses are:

- no raw Coinbase export
- reliance on manual Coinbase / Celsius / salary files
- incomplete ingestion of some invoice-side documents
- weak custody chain if manual summaries are standing in for real exchange or payment records

That does not mean the numbers are wrong. It means they are **harder to defend**.

---

## Partial Consensus / Open Issues

### PIT-36 for Jan-Apr 2025 is plausible, but not fully settled
The reports generally accept the current direction:

- PIT-36 is the plausible form
- `Art. 13 pkt 8` + 20% KUP is plausible
- the same receipt value can later become PIT-38 basis without this being a forbidden double deduction

But they also stress that this depends on the real contract facts. If the relationship looks more like business activity than personal-service income, the classification could shift.

So the synthesis here is:

- current PIT-36 logic looks **plausible**, not definitively settled
- 2023 and 2024 should be reviewed under the same lens if similar post-move USDC work existed then

### PIT/ZG is not settled by these reports
There is not enough clean agreement to treat PIT/ZG as resolved.

- ChatGPT 5.4 Pro and Deep Research both push back against “foreign payer = automatic PIT/ZG”
- Gemini treats PIT/ZG as mandatory for the foreign-source income side

Given that the old prompt did not let the agents inspect the actual payer / contract / source facts, this remains **unsettled** here.

### PIT-28 revenue-date criticism is likely real
Two of the reports clearly criticize the repo’s apparent “invoice issue date” rule for PIT-28.

The safest synthesis is:

- the current PIT-28 revenue-date logic is likely too crude
- business-income timing under Article 14 should be checked properly against service-completion / invoice / payment timing

### PIT-28 health deduction issue is serious, but not as well cross-confirmed
ChatGPT Deep Research makes a strong claim that the current PIT-28 logic is materially wrong because it deducts 50% health insurance from **tax** rather than from **revenue**, and estimates a materially higher annual tax if corrected.

That may well be right, but it is not as clearly repeated by the other two reports. So this issue is:

- **important and likely real**
- but not as fully consensus-backed as the pre-residency salary-USDC issue

It should be verified directly before relying on current PIT-28 outputs.

---

## What This Means For The Calculator

### What looks defensible enough to keep

- annual PIT-38 structure and carry-forward model
- crypto-to-crypto non-taxability
- post-residency crypto-compensation -> later PIT-38 basis logic
- excluding funding / withdrawal style fees
- keeping pre-residency **fiat purchase** costs in scope, subject to documentation and “not already consumed abroad” checks

### What should be treated as unsafe right now

- pre-residency salary-paid USDC inside the default PIT-38 opening pool
- deposit-derived PIT-38 cost creation
- filing-grade reliance on manual Coinbase / similar proxies without primary exports
- confidence in PIT-28 until revenue timing and health-deduction logic are rechecked

### Recommended structural split
The reports strongly support splitting the current PIT-38 opening pool into at least three legal buckets:

1. **Pre-residency documented fiat purchases**
2. **Post-residency Polish-taxed crypto compensation**
3. **Pre-residency salary / compensation paid in USDC**

Bucket 3 should not sit in the default filing chain as if it were equivalent to bucket 1.

---

## Do These Reports Answer What We Need?

### Yes, for the main strategic question
These reports do give a usable answer to the most important question:

**No, you should not treat pre-residency salary-paid USDC as a safe, ordinary PIT-38 cost bucket.**

That point is strong enough across the reports that I would treat it as the current working conclusion.

They also give a second strong answer:

**Pre-residency fiat purchases are a different and much stronger category than pre-residency salary-paid USDC.**

That is valuable and actionable.

### No, for a true implementation audit
These reports do **not** fully answer whether the implementation itself is correct, because they could not actually inspect:

- the real code
- the real normalized ledgers
- the generated JSON / markdown artifacts
- the exact source documents

So if the goal is:

- a legal direction on the risky bucket
- a decision about whether to quarantine pre-residency salary-USDC

then these reports are probably enough.

If the goal is:

- a real external audit of the actual code paths
- verification of whether the repo really implements the rules correctly
- verification of PIT-28, PIT/ZG, and normalization details against the actual files

then **yes, you should submit the 2nd prompt**.

That newer prompt is materially better because it no longer assumes the external agent can magically read local paths. It can be used properly either:

- as a pure legal audit prompt using only the summarized facts, or
- together with pasted snippets / attached artifacts if you want a real document-and-output review

---

## Recommendation

My recommendation is:

1. Treat this round as sufficient to justify **quarantining or excluding pre-residency salary-paid USDC** from the default PIT-38 carry-forward.
2. Do **not** treat this round as sufficient to sign off on the repo as filing-ready.
3. Run the **2nd prompt** if you want a real external review of the current implementation details.
4. In parallel, separately verify PIT-28 health-deduction logic and revenue-date logic before relying on the current 2025 PIT-28 number.
