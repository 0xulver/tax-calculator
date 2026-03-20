# Synthesis: Cost Basis and Valuation Rules for Crypto Tax in Poland

Sources: ChatGPT 5.4 Pro, ChatGPT Deep Research, Perplexity, Gemini 3.1 Deep Research

---

## Strong Consensus

### NBP exchange rate rule (Art. 11a)
All 4 agree on the mechanics:
- **Revenue** (Art. 11a ust. 1): NBP average rate from **last business day BEFORE the revenue date**
- **Costs** (Art. 11a ust. 2): NBP average rate from **last business day BEFORE the cost date**
- Saturday/Sunday trades: use Friday's rate (or earlier if Friday was a holiday)
- This is NOT the trade-day rate — the statute explicitly says "preceding"
- Applies to foreign fiat amounts (EUR, USD), not to crypto itself

### Annual cost pool is the primary mechanism
All 4 confirm: Polish crypto PIT uses annual aggregate revenue minus annual aggregate costs (Art. 30b ust. 1b + Art. 22 ust. 14-16). Costs are taken in the year incurred. Excess costs carry forward. This is NOT per-transaction lot matching.

### Deductible costs (Art. 22 ust. 14)

| Cost | Deductible? | All agree? |
|---|---|---|
| Fiat purchase price of crypto | Yes | Yes |
| Exchange trading fees (buy/sell) | Yes | Yes |
| Fees paid in crypto on buy/sell | Yes (if documented) | Yes |
| Mining equipment/electricity | No | Yes |
| Loan/credit interest for crypto | No | Yes |
| Crypto-to-crypto swap fees | No (Art. 23 ust. 1 pkt 38d) | Yes |
| Hardware wallets / VPNs | No | Yes |
| Withdrawal fees (exchange to wallet) | Grey zone / mostly no | Yes |
| Gas fees for transfers | Grey zone / mostly no | Yes |

### Salary USDC: income at receipt becomes cost basis for PIT-38
All 4 confirm: when USDC is received as salary and taxed as income, the PLN value recognized as income becomes the crypto acquisition cost for later PIT-38 disposal. This prevents double taxation. Supported by KIS interpretations.

### USDC valuation: use actual market value, not assumed 1:1 peg
All 4 agree: USDC is NOT legally USD. If USDC depegs (e.g., trades at 0.97 USD), use the actual market value, not an automatic 1.00 USD assumption. The practical approach for a near-peg USDC is amount x NBP USD rate, but a depeg must be respected.

### Pre-residency costs: original acquisition cost, no step-up
All 4 confirm: no market-value reset when you become a Polish tax resident. Use the original documented purchase price, converted to PLN using the NBP rate from the original purchase date. Supported by WSA Warsaw III SA/Wa 1290/24 and KIS interpretations.

### Stablecoin auto-conversions: non-taxable, carry cost through
All 4 agree: BUSD->FDUSD->USDC is crypto-to-crypto, not taxable. Historical acquisition cost transfers to the replacement token. Fees on these conversions are non-deductible.

### No formal "ewidencja walut wirtualnych" template required
Art. 30b ust. 6 requires annual reporting, not a specific register format. But you need transaction-level evidence to substantiate the annual totals.

### Records can be reconstructed, not maintained in real-time
No source found a real-time maintenance requirement. Reconstruction from exchange CSVs at filing time is acceptable if accurate and complete.

### Retention: 5 years from end of year tax was due
Art. 70 §1 Ordynacja podatkowa. For 2025 PIT-38 (due April 30, 2026): retain until December 31, 2031. But carry-forward costs may need documentation longer since the underlying cost could be used years later.

---

## The One Significant Disagreement: FIFO

This is where the sources split sharply.

### The statutory text

Art. 30b ust. 7 says FIFO applies when identification of specific units is impossible. Art. 30b ust. 7a says paragraph 7 applies "appropriately" (odpowiednio) to other Art. 30b income, including crypto under ust. 1a.

### What the sources say

| Source | FIFO for crypto? | Reasoning |
|---|---|---|
| **ChatGPT 5.4 Pro** | "FIFO is not just market practice" — Art. 30b(7a) extends FIFO to crypto. But the annual pool model still dominates in practice. "FIFO has a much narrower practical role." | Acknowledges statutory basis but says it doesn't change the annual pool computation |
| **ChatGPT Deep Research** | "FIFO is NOT explicitly mandated" for crypto. The annual aggregate model is the statutory backbone. Art. 30b(7) is for fund units. | Emphasizes the tension between statute and MF guidance |
| **Perplexity** | "No legal basis for applying FIFO" — cites KIS official guidance explicitly denying FIFO for crypto. Annual cost pool is the only method. | Most anti-FIFO position, cites KIS directly |
| **Gemini** | "The Strict Mandate of FIFO" — Art. 30b(7a) **mandates** FIFO for crypto. Per-asset, global across exchanges. "KIS has unequivocally confirmed its direct application." | Most pro-FIFO position, treats it as mandatory |

### Assessment

This is a genuine legal tension. The statute has a FIFO reference (Art. 30b ust. 7a), but official MF crypto guidance uses the annual cost pool model without mentioning FIFO. The practical impact is limited because:

1. The annual cost pool approach and FIFO produce the **same PIT-38 numbers** in most cases — both compute total revenue minus total costs for the year
2. FIFO only matters if you need to determine the cost of specific units sold, which the annual pool model doesn't require
3. Gemini's "per-asset FIFO" would only affect the per-transaction gain/loss analysis (useful for audits), not the annual totals

**For our calculator**: the cost pool approach is correct for the PIT-38 form (annual aggregates). If we want audit-defense detail, maintaining per-asset FIFO records internally is good practice but not strictly required for the filing.

---

## Minor Disagreements

### Whether airdrops/staking get cost basis of 0 or market value

| Source | Position |
|---|---|
| ChatGPT 5.4 Pro | "Pure free airdrop has no acquisition expenditure — literal basis is 0." But if separately taxed at receipt, the taxed value becomes cost basis. |
| ChatGPT Deep Research | Same nuanced view — depends on whether receipt was taxed |
| Perplexity | "Not always zero" — if taxed at receipt, that value is the cost basis |
| Gemini | KIS treats receipt as taxable (prawa majatkowe, Art. 18), and that taxed value becomes cost basis |

**Consensus**: If the airdrop/staking receipt was taxed as income at receipt (KIS approach), the taxed PLN value becomes cost basis for later disposal. If not taxed at receipt, cost basis is 0. The KIS approach (tax at receipt) is the safer path and provides a cost basis.

### Whether fiat withdrawal fees from exchange are deductible

ChatGPT Deep Research cites a 2025 KIS interpretation that **rejected** deposit/withdrawal intermediary fees as not directly tied to acquisition/disposal. Gemini also says withdrawal fees are "non-deductible." The other sources place them in the grey zone. **Safer to exclude them.**

---

## What This Means for Our Calculator

### Already correct
- NBP rate from day before transaction (our `nbp.py` uses `delta=1`)
- Annual cost pool aggregation (our `cost_pool.py`)
- Crypto-to-crypto swaps ignored
- Salary USDC enters as cost at receipt PLN value
- Pre-residency costs as `--pre-residency-costs` parameter
- Stablecoin auto-conversion cost continuity

### Should verify
- Our NBP client fetches rates correctly for weekend/holiday trades (should get Friday's rate for Saturday transactions)
- Fee handling: we include fiat trading fees as costs — this is correct. We should NOT include crypto-to-crypto swap fees or withdrawal fees.

### Could improve
- Add USDC depeg handling (currently we assume 1:1 with USD via NBP rate — should support actual market price if depegged)
- Add per-asset FIFO tracking as a secondary/audit output alongside cost pool totals (defensive measure even though not required for PIT-38 filing)

---

## Action Items

### 1. Verify NBP rate logic for weekends
Our `nbp.py` starts at `delta=1` and goes back up to 10 days. For a Saturday trade, `delta=1` = Friday. This is correct. But confirm it handles holidays properly (should skip non-business days).

### 2. Document the NBP rate used for each transaction
The synthesis confirms per-transaction NBP rate documentation is needed for audit defense. Our calculator should output which NBP rate/date was used for each revenue and cost event.

### 3. Exclude non-deductible costs
Ensure the cost pool only includes:
- Fiat purchases of crypto (EUR amount x NBP rate)
- Trading fees on buy/sell (fiat fees only)
- Salary USDC at receipt value

And excludes:
- Crypto-to-crypto swap fees
- Withdrawal/transfer fees
- Gas fees for non-disposal transfers
- Mining costs, hardware, etc.

### 4. Pre-residency costs: calculate from Swedish period
Extract all fiat->crypto purchases from Binance/Kraken for 2020-2022. Convert each to PLN using NBP rate from the day before the original purchase date. Sum = pre-residency costs to enter in the first Polish PIT-38.
