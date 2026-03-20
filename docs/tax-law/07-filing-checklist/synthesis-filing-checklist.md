# Synthesis: Complete Tax Filing Checklist (2023-2025)

Sources: ChatGPT 5.4 Pro, ChatGPT Deep Research, Perplexity, Gemini 3.1 Deep Research

---

## Consensus: What Forms Are Needed Per Year

### 2023

| Form | Required? | All 4 agree? |
|---|---|---|
| **PIT-38** | YES — crypto disposals + acquisition costs | Yes |
| PIT-36 | Only if non-crypto income existed (the USDC salary income was reported on PIT-37 already) | Yes |
| PIT-37 | Already filed (by tax company, but wrong form) | — |
| PIT-28 | No — no JDG in 2023 | Yes |

### 2024

| Form | Required? | All 4 agree? |
|---|---|---|
| **PIT-38** | YES — **not filed, needs filing urgently** | Yes |
| PIT-36 or PIT-37 | Already filed (PIT-37, should be corrected to PIT-36) | — |
| PIT-28 | No — no JDG in 2024 | Yes |

### 2025

| Form | Required? | All 4 agree? |
|---|---|---|
| **PIT-38** | YES — crypto disposals + cost carry-forward | Yes |
| **PIT-28** | YES — JDG ryczalt income | Yes |
| **PIT-36** | YES (likely) — pre-JDG USDC salary income (Jan-Apr) | Yes |
| PIT-37 | No (no Polish payer) | Yes |
| PIT-36L | No (JDG chose ryczalt, not liniowy) | Yes |

**2025 is a 3-form year**: PIT-38 + PIT-28 + PIT-36. These are independent returns covering different income categories — they don't merge or replace each other.

---

## Consensus: Key Rules

### PIT-38 must be filed even with zero revenue
All 4 sources unanimously confirm: if you incurred crypto acquisition costs OR had crypto disposals, PIT-38 is mandatory — even if the result is 0 tax. Filing preserves the cost carry-forward chain.

### Pre-JDG income cannot go on PIT-28
All sources agree: JDG ryczalt starts from the CEIDG registration date. Income earned before that (Jan-Apr 2025 USDC) must be on PIT-36, taxed at progressive rates (12%/32%). It cannot be retroactively pulled into ryczalt.

### The dzialalnosc nierejestrowana threshold is blown
40,500 USDC over 4 months = ~10K USDC/month. The 2025 limit for unregistered activity is 3,499.50 PLN/month. Each payment (~24K PLN) massively exceeds this. All sources agree this income cannot be treated as unregistered activity.

### Crypto trading is VAT-exempt
Per the CJEU Hedqvist ruling (C-264/14), exchanging crypto for fiat is a financial service exempt from VAT. No VAT filing required for personal crypto trading.

### DAC8 is coming — exchanges will report
DAC8 was signed into Polish law March 9, 2026. Starting 2027 (for 2026 data), Binance and Kraken will report Polish customer transaction data to KAS. This makes filing past returns urgently important — act before the data flows.

### Multiple returns for the same year is normal
It's standard in Poland to file PIT-38 + PIT-28 + PIT-36 all for the same year. They cover different "income buckets" and don't interact.

---

## Disagreements

### 1. Is PIT/ZG required with PIT-38?

| Source | Position |
|---|---|
| ChatGPT 5.4 Pro | PIT/ZG only if foreign-source income is reported AND foreign tax was paid; since Binance/Kraken income is crypto capital gains where no foreign tax is paid, PIT/ZG may not be strictly needed |
| ChatGPT Deep Research | PIT/ZG is for foreign-source income — if crypto was traded on foreign exchanges, it depends on whether the income is classified as "foreign-source" |
| **Perplexity** | **YES — PIT/ZG is required for all PIT-38 years** because Binance and Kraken are foreign exchanges |
| **Gemini** | **YES — mandatory PIT/ZG annex** for every year with transactions on foreign exchanges |

**Assessment**: Perplexity and Gemini are more aggressive about PIT/ZG. The safe approach is to include it — worst case it shows zero foreign tax paid and proporcjonalne odliczenie method. It's a harmless addition. ChatGPT 5.4 Pro's more nuanced view (PIT/ZG when foreign tax methods apply) is technically more precise, but the practical advice is the same: include it.

### 2. Health insurance deductibility under ryczalt

| Source | Position |
|---|---|
| ChatGPT 5.4 Pro | 50% of paid health contributions deductible from revenue |
| ChatGPT Deep Research | 50% deductible from revenue |
| **Perplexity** | "Health insurance contributions are NOT deductible from income under ryczalt" |
| Gemini | 50% deductible from gross taxable revenue |

**Assessment**: Perplexity is wrong here. The other 3 sources (and the JDG synthesis from topic 01) confirm: ryczalt taxpayers CAN deduct 50% of paid health insurance from revenue (Art. 11 ust. 1a ryczalt act). This was confirmed in the synthesis from topic 01 as well.

### 3. Crypto loss carry-forward mechanics

| Source | Position |
|---|---|
| ChatGPT 5.4 Pro | Correctly uses Art. 22 ust. 16 cost surplus (no time limit, no cap) |
| ChatGPT Deep Research | Same — cost surplus, not Art. 9 loss |
| Perplexity | Mentions "carry forward for up to 5 years" and "50% cap" — **incorrectly applies Art. 9 ust. 3 rules** |
| Gemini | Mentions Art. 9(3) and "5-year" rule but also references Art. 22 and cost surplus — **inconsistent** |

**Assessment**: Perplexity and Gemini's crypto loss sections contain errors (applying the standard Art. 9 ust. 3 loss rules to crypto). As confirmed unanimously in the loss carry-forward synthesis (topic 05), crypto uses Art. 22 ust. 16 with NO time limit and NO annual cap. This is a known common misconception.

---

## Complete Filing Calendar

### Deadlines

| Tax Year | Form | Original Deadline | Status |
|---|---|---|---|
| 2023 | PIT-38 | Apr 30, 2024 | LATE — file with czynny zal |
| 2023 | PIT-36 korekta (replace PIT-37) | Apr 30, 2024 | LATE — lower priority |
| 2024 | PIT-38 | Apr 30, 2025 | **LATE — URGENT, file now** |
| 2024 | PIT-36 korekta (replace PIT-37) | Apr 30, 2025 | LATE — lower priority |
| 2025 | PIT-38 | **Apr 30, 2026** | Due in 6 weeks |
| 2025 | PIT-28 | **Apr 30, 2026** | Due in 6 weeks |
| 2025 | PIT-36 | **Apr 30, 2026** | Due in 6 weeks |

### Monthly/Recurring (already in progress for JDG)

| Obligation | Deadline | Notes |
|---|---|---|
| Ryczalt monthly payment | 20th of following month | Already being paid |
| ZUS contributions | 20th of following month | Already being paid |
| VAT-UE (if EU clients) | 25th of following month | Not applicable (no EU clients) |
| ZUS annual health reconciliation | April DRA, due May 20, 2026 | First year |

---

## Action Items

### IMMEDIATE (this week)

1. **Check e-Urzad Skarbowy** for auto-accepted PIT-38s for 2023 and 2024
2. **File 2024 PIT-38** (correction or first filing) with czynny zal — this protects the cost carry-forward chain for 2025
3. **Calculate PIT-38 numbers** for 2023 and 2024 using the cost pool calculator

### BEFORE APRIL 30, 2026

4. **File 2025 PIT-38** — crypto disposals + cost carry-forward
5. **File 2025 PIT-28** — JDG ryczalt income (must be actively filed — NOT auto-accepted)
6. **File 2025 PIT-36** — pre-JDG USDC salary income (Jan-Apr 2025)
7. **Include PIT/ZG** annexes where applicable (safe to attach to PIT-38 for foreign exchanges)

### AFTER APRIL 30 (lower priority corrections)

8. **File 2023 PIT-37 -> PIT-36 korekta** + PIT/ZG
9. **File 2024 PIT-37 -> PIT-36 korekta** + PIT/ZG
10. **Address ZUS question** for pre-JDG periods (specialist needed)

### NOT NEEDED

- PIT-36L (you chose ryczalt, not liniowy)
- PIT-37 for 2025 (no Polish payer)
- PIT-16A (not on karta podatkowa)
- VAT filings for crypto trading (VAT-exempt per Hedqvist)
- ORD-W1 or other foreign account reporting (not required for exchange accounts)
