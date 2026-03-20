# Synthesis: Tax Classification of Stablecoins (USDC, USDT) in Poland

Sources: ChatGPT 5.4 Pro, ChatGPT Deep Research, Perplexity, Gemini 3.1 Deep Research

---

## Full Consensus (All 4 agree)

### USDT is unambiguously "waluta wirtualna"
Tether has no EMI license, is not authorized under MiCA, and does not qualify as electronic money. USDT clearly meets the AML Act definition of virtual currency. No dispute from any source.

### Crypto-to-crypto swaps remain tax-neutral
All sources confirm that exchanging one waluta wirtualna for another (BTC->ETH, BTC->USDT, USDT->USDC) is NOT a taxable event under Art. 17 ust. 1f. Only disposal for fiat/goods/services/settling liabilities is taxable.

### Stablecoin->fiat (EUR/PLN) IS the taxable event
Converting USDC or USDT to EUR on Binance/Kraken triggers the 19% crypto capital gains tax on PIT-38. Revenue = EUR received x NBP EUR rate from last business day before conversion.

### Revenue is calculated from EUR received, not USD value
When you sell USDC for EUR, the revenue in PLN is: EUR amount x NBP EUR/PLN rate. NOT USDC amount x NBP USD/PLN rate. The actual fiat received determines revenue.

### The barter/salary doctrine: income at receipt = cost basis for PIT-38
All sources confirm: USDC received as salary is taxed as income at receipt. That same PLN value then becomes the cost basis when the USDC is later sold on PIT-38. This prevents double taxation. Multiple KIS interpretations cited:
- 0115-KDIT1.4011.745.2025.3.MN (Nov 2025): stablecoin salary = income at receipt + cost basis
- 0114-KDIP3-1.4011.51.2025.1.AK (Mar 2025): IT contractor crypto salary = business income + cost basis
- 0115-KDIT1.4011.22.2025.1.MR (Mar 2025): employee crypto bonus = income + cost basis

### Binance auto-conversions (BUSD->FDUSD->USDC) are tax-neutral
All tokens involved qualify as waluta wirtualna, so each leg is a crypto-to-crypto swap. No taxable event. Cost basis carries through.

### Wallet transfers are not taxable
Moving USDC from Polygon wallet to Binance/Kraken = self-transfer. No disposal, no tax event.

---

## The One Big Issue: USDC After MiCA

This is where the sources diverge — not on the practical treatment, but on the **legal risk**.

### The problem

| Fact | Implication |
|---|---|
| Circle got an EU EMI license on June 30, 2024 | USDC is formally an "e-money token" (EMT) under MiCA |
| MiCA Art. 48(2) says EMTs are "electronic money" | USDC = pieniadz elektroniczny under EU law |
| Polish AML definition of waluta wirtualna **excludes** electronic money | Literal reading: USDC falls OUTSIDE waluta wirtualna |
| Polish crypto-assets law (ustawa o rynku kryptoaktywow) was vetoed TWICE | Dec 2025 + Feb 2026 by President Nawrocki |
| The vetoed law would have **saved** USDC by keeping EMTs as waluta wirtualna for tax | This fix never entered into force |

### Where sources differ on the risk

| Source | Current status | Risk assessment |
|---|---|---|
| ChatGPT 5.4 Pro | USDT = yes. USDC = "yes in practice, but no longer beyond doubt on pure literal analysis after MiCA" | **Medium** — recommends individual interpretation |
| ChatGPT Deep Research | USDC continues to appear as waluta wirtualna in tax interpretation practice post-MiCA. But Art. 22(14) "wydatki" wording creates a **separate cost basis risk** for salary USDC | **Medium-High** on cost basis; **Low-Medium** on classification itself |
| Perplexity | USDC is in a "legally grey zone." Cites specific KIS verbal response (Feb 2025) saying MiCA doesn't affect tax. Cites March 2026 binding interpretation confirming neutrality. But the USDC EMI problem is "real" | **Medium** — recommends interpretacja indywidualna |
| Gemini | The vetoed law was designed to solve this. KIS has issued binding interpretations confirming stablecoins remain waluta wirtualna despite MiCA. The "deliberate legal dualism" between AML law and tax law protects taxpayers | **Low-Medium** — confident that current practice is safe |

### The practical consensus

Despite the theoretical legal tension, **all 4 sources agree on the practical advice: continue treating USDC as waluta wirtualna for Polish PIT purposes.** This is:
- What KIS is doing in practice
- What the legislative intent was (even though the law was vetoed)
- What all practitioners are doing
- What makes economic sense (reclassifying would create chaos)

The risk is real but currently low — it would only materialize if KIS reversed its position or a court took a literal reading, neither of which has happened.

---

## Minor Disagreement: Salary USDC Cost Basis

ChatGPT Deep Research raises a unique concern the others don't:

The PIT Act's cost rule (Art. 22 ust. 14) defines deductible crypto costs as "documented expenses directly incurred to acquire virtual currency" (**wydatki**). When you receive USDC as salary, you didn't "spend" anything to acquire it — it was payment for services. So there's a strict-reading risk that the cost basis is **0 PLN** even though you already paid income tax on the receipt.

| Source | Position on salary USDC cost basis |
|---|---|
| ChatGPT 5.4 Pro | Cost = PLN value at receipt (citing KIS interpretations) |
| **ChatGPT Deep Research** | **Raises the risk** that strict Art. 22(14) "wydatki" reading could give cost = 0 PLN. Calls it "a genuine ambiguity/risk" |
| Perplexity | Cost = PLN value at receipt (citing multiple KIS interpretations) |
| Gemini | Cost = PLN value at receipt ("Phase 2: value transfer" doctrine) |

**Assessment**: 3 of 4 sources say the salary value becomes cost basis, supported by multiple KIS interpretations. ChatGPT Deep Research's concern is theoretically valid (the statute says "wydatki" = expenses, and receiving salary isn't an "expense"), but KIS has consistently ruled the opposite way. This is a low-probability risk, but it's worth noting in case the legal landscape changes.

---

## Key Takeaways for Your Situation

### 1. Your current approach is correct
Treating USDC as waluta wirtualna, making crypto-to-stablecoin swaps non-taxable, and treating USDC->EUR as the taxable disposal — this is the right approach for 2023-2025.

### 2. The salary barter doctrine works in your favor
USDC received as salary = income at receipt (PIT-36). That value becomes cost basis for PIT-38. The USDC->EUR conversion is then nearly tax-neutral (only FX movement). KIS explicitly endorses this.

### 3. USDC vs USDT risk differential
USDT has zero classification risk. USDC has a theoretical risk post-MiCA (after June 30, 2024). For transactions before that date, there's no issue at all. For transactions after, current KIS practice still treats USDC as waluta wirtualna.

### 4. The vetoed law matters as legislative intent
Even though the ustawa o rynku kryptoaktywow was vetoed twice, its text shows the government's intent was to keep EMTs within waluta wirtualna for tax purposes. This strengthens the argument that current practice is correct.

### 5. No change needed in our calculator
Our cost pool calculator already treats all stablecoins (USDC, USDT, BUSD, FDUSD) as waluta wirtualna. Crypto-to-stablecoin swaps are ignored. Only stablecoin->fiat creates revenue. This is correct.

---

## Action Items

### No immediate action needed on classification
Continue treating USDC as waluta wirtualna. This is what KIS does, what practitioners do, and what our calculator does.

### Consider an interpretacja indywidualna (40 PLN)
For future protection, especially given the USDC post-MiCA uncertainty, requesting a binding KIS interpretation for your specific flow (USDC salary on Polygon -> transfer to exchange -> convert to EUR) would provide legal certainty. Two sources recommend this. It takes ~3 months and costs 40 PLN.

### Monitor the third legislative attempt
The ustawa o rynku kryptoaktywow needs to pass before July 1, 2026 (MiCA CASP licensing deadline). If a third version passes with the EMT tax preservation clause, the USDC risk disappears entirely. If it fails again, the uncertainty continues but KIS practice is unlikely to change.

### Document BUSD->FDUSD->USDC auto-conversions
Keep Binance records showing these were involuntary platform-initiated conversions. This supports the non-taxable treatment even if classification questions arise later.
