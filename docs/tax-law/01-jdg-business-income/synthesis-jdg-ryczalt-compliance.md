# Synthesis: JDG Ryczalt Business Income Reporting

Sources: ChatGPT 5.4 Pro, Perplexity, ChatGPT Deep Research, Gemini 3.1 Deep Research

---

## Consensus (All 4 sources agree)

### Tax Rate & Base
- **12% flat tax on gross revenue** (not profit) for IT/software services under Art. 12 ust. 1 pkt 2b of the ryczalt act
- **No cost deductions** — equipment, software, travel, etc. are not deductible (Art. 12 ust. 2)
- Rate depends on **PKWiU classification** (actual service type), not just PKD code. Core programming/software dev = 12%. Some peripheral IT activities (pure QA/testing) could qualify for 8.5%
- **50% of paid health insurance contributions** can reduce ryczalt revenue (Art. 11 ust. 1a) — this is the only meaningful deduction

### EUR -> PLN Conversion
- EUR revenue must be converted to PLN using the **NBP average (mid) rate from the last business day BEFORE the revenue recognition date** (Art. 11a ust. 1 PIT act)
- Revenue recognition date follows Art. 14 ust. 1c: **earliest of** service completion, invoice date, or payment date
- For monthly billing contracts: Art. 14 ust. 1e moves it to the **last day of the settlement period** stated in the contract/invoice
- New for 2025: optional **cash method** election (Art. 14c / Art. 6 ust. 1g ryczalt act) — if elected, payment date becomes revenue date

### Monthly Obligations
- Pay 12% of monthly revenue by the **20th of the following month** to your mikrorachunek podatkowy (PPE payment code)
- December tax due by **20 January**
- **No monthly tax declaration** — just the bank transfer. You calculate the amount yourself from your ewidencja przychodow (revenue register)
- ZUS social + health contributions paid separately by **20th of the following month** via PUE ZUS

### Annual Filing
- Annual return: **PIT-28**, filing window **15 February - 30 April** of the following year (2025 tax year -> by 30 April 2026)
- Reports: total annual revenue by rate, statutory deductions (social ZUS contributions, 50% health insurance), computed ryczalt, amounts already paid, and any over/underpayment
- Filed via Twoj e-PIT / e-Urzad Skarbowy electronically

### ZUS (Social Insurance)
- **Ulga na start**: first 6 full calendar months — exempt from social contributions, but must pay health insurance
- **Preferencyjne**: next 24 months — social contributions on reduced base of 30% of minimum wage (1,399.80 PLN in 2025, total ~443 PLN/month with voluntary sickness)
- If JDG starts mid-month, the 6-month clock starts from the next full month

### Health Insurance (Skladka Zdrowotna) 2025
- Fixed monthly amounts based on annual revenue tiers:

| Annual Revenue | Monthly Contribution 2025 |
|---|---|
| Up to 60,000 PLN | 461.66 PLN |
| 60,001 - 300,000 PLN | 769.43 PLN |
| Over 300,000 PLN | 1,384.97 PLN |

- Annual reconciliation via ZUS DRA, due by **20 May** of the following year

### FX Differences (Roznice Kursowe)
- FX differences DO apply under ryczalt (Art. 6 ust. 1c ryczalt act -> Art. 24c PIT act)
- **Positive FX difference** (EUR weakened between invoice and payment): increases taxable revenue
- **Negative FX difference** (EUR strengthened): decreases taxable revenue
- FX differences taxed at the same 12% rate
- **No year-end revaluation** of held EUR — FX events only crystallize on realized events (payment receipt, conversion, outflow)

### Ryczalt vs Crypto (PIT-38)
- Completely separate tax streams. **No interaction, no cross-offsetting**
- Ryczalt = PIT-28, Crypto = PIT-38
- Crypto losses cannot reduce ryczalt income. Ryczalt cannot produce a "loss" (revenue-based)

### VAT
- VAT exemption threshold: **200,000 PLN in 2025** (prorated for mid-year start), rising to **240,000 PLN from 2026**
- EU B2B IT services: must register for **VAT-UE** (via VAT-R form) before first transaction
- VAT-UE registration does NOT remove your VAT exemption
- Invoices to EU clients: no Polish VAT, annotation "reverse charge / art. 28b"
- **VAT-UE** summary filing due by **25th of the following month** (only for months with EU transactions)

---

## Disagreements Between Sources

### 1. JPK_V7 obligation for VAT-exempt JDG with VAT-UE

| Source | Position |
|---|---|
| ChatGPT 5.4 Pro | VAT-exempt + VAT-UE does NOT require JPK_V7 |
| Perplexity | No JPK_V7 if VAT-exempt |
| ChatGPT Deep Research | VAT-exempt = no JPK_VAT obligation; VAT-UE is separate |
| **Gemini** | **Claims JPK_V7 IS required** even if VAT-exempt, because intra-community commerce triggers it |

**Assessment:** Gemini appears to be the outlier. The other three sources, citing official guidance from podatki.gov.pl, agree that VAT-UE alone does not create a JPK_V7 obligation for VAT-exempt taxpayers. This is the majority and better-sourced position. However, this is worth confirming with your accountant since getting it wrong means either unnecessary filing or a compliance gap.

### 2. PIT-28 month-by-month breakdown

| Source | Position |
|---|---|
| **Perplexity** | PIT-28 does NOT require month-by-month — only annual totals per rate |
| ChatGPT 5.4 Pro | PIT-28 includes a section showing ryczalt for each month or quarter |
| ChatGPT Deep Research | PIT-28 includes month/quarter breakdown section |
| Gemini | Does not explicitly address |

**Assessment:** The PIT-28 form does contain a section for monthly/quarterly amounts. Perplexity's statement is misleading — the form has both annual totals AND a per-period breakdown.

### 3. Which rate for FX difference at payment receipt

| Source | Position |
|---|---|
| Perplexity | Bank's exchange rate on payment date (faktycznie zastosowany kurs) |
| ChatGPT Deep Research | Actual rate where applicable; NBP average if no actual rate |
| Gemini | NBP rate from last working day before receipt for the transactional FX; bank spot rate for own-funds conversion |

**Assessment:** The law (Art. 24c) uses "faktycznie zastosowany kurs" (actually applied rate) where one exists. If payment arrives in EUR to an EUR account (no conversion), there's no "actually applied rate" — you use the NBP average. If you convert EUR to PLN via the bank, the bank's actual rate applies. All sources agree on the principle; they just explain it differently.

### 4. PKD 2025 reclassification

Only **Gemini** discusses the PKD 2025 update — the old 62.01.Z code has been split into 62.01.A (game programming) and 62.01.B (other programming). Existing JDGs must update their CEIDG registration. The other sources don't mention this. The 12% ryczalt rate is unaffected since it follows PKWiU, not PKD.

---

## Key Takeaways for Your Situation

1. **Your JDG ryczalt at 12% is straightforward** — you invoice in EUR, convert at NBP rate, pay 12% monthly by the 20th, file PIT-28 annually. No cost deductions (except 50% of health insurance).

2. **FX tracking matters** — every EUR payment received and every EUR->PLN conversion in your bank creates FX events. You should track: (a) the NBP rate at invoice time, (b) the actual rate at payment receipt, (c) the rate when converting EUR to PLN. The differences adjust your taxable revenue.

3. **You likely need VAT-UE registration** if your client is an EU company. This adds a monthly VAT-UE filing by the 25th for any month with EU B2B services. It does NOT require JPK_V7 (majority position) and does NOT remove your VAT exemption.

4. **Health insurance tier will escalate quickly** — at your revenue level (likely >300K PLN/year), you'll be in the top tier (1,384.97 PLN/month) within a few months.

5. **Crypto and JDG are completely firewalled** — your PIT-38 crypto losses cannot help your JDG tax, and vice versa.

---

## Action Items

1. **Check your PKD code in CEIDG** — if you registered before 2025 with 62.01.Z, update to 62.01.B (Other programming activity) per the PKD 2025 changes. (Low urgency but do it to avoid algorithmic mismatch.)

2. **Register for VAT-UE** if not already done and your client is EU-based. File VAT-R update. This should have been done before the first EU service.

3. **Set up monthly compliance rhythm:**
   - By 20th: pay 12% ryczalt to mikrorachunek + pay ZUS via PUE ZUS
   - By 25th: file VAT-UE (if EU clients that month)
   - Keep ewidencja przychodow updated with each invoice (EUR amount, NBP rate, PLN amount)

4. **Track FX differences** — when you receive EUR payments and when you convert EUR to PLN in your bank. These adjust your monthly taxable revenue.

5. **Confirm with your accountant:** Does your VAT-exempt + VAT-UE status require JPK_V7? (Probably not per 3 of 4 sources, but worth confirming.)

6. **For PIT-28 filing (by 30 Apr 2026):** gather all monthly revenue records, FX differences, ZUS contribution receipts, and health insurance paid (for the 50% deduction).
