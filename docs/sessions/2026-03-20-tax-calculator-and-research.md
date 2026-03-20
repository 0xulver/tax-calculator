# Session: Tax Calculator Implementation & Tax Law Research

**Date**: March 20, 2026
**Duration**: Extended session (full day)

---

## What Was Done

### 1. Built the Crypto Tax Calculator Package

Restructured from scattered scripts into a proper Python package at `src/tax_calc/`:

**Normalizers** (exchange data -> unified format):
- `normalizers/binance.py` — Fixed 3 critical bugs:
  - Fix 5a: Buy/Spend pattern inverted asset/counterparty on sells (USDC->EUR showed as EUR->USDC)
  - Fix 5b: "Sell Crypto To Fiat" 1-second time grouping (paired rows at :55/:56 now merge)
  - Fix 5c: Sold/Revenue multi-fill aggregation (each fill got total revenue instead of its share)
- `normalizers/kraken.py` — Ported from original, no logic changes needed
- `normalizers/salary.py` — Parses Polygon USDC salary payments into cost lots

**Core Engine**:
- `cost_pool.py` — **NEW**: Implements the correct Polish annual cost pooling method (NOT FIFO). This was rewritten after research confirmed Poland does not use FIFO for crypto.
- `fifo.py` — **KEPT for reference**: The old FIFO engine still works but is not the correct Polish method. Kept in case per-transaction analysis is needed for audits.
- `nbp.py` — NBP rate client with JSON disk cache, fetches rate from day BEFORE transaction (Art. 11a)
- `prices.py` — Price resolution: NBP -> stablecoin -> CoinGecko

**Reports & CLI**:
- `pit38.py` — Generates PIT-38 Section E markdown reports with correct field numbers (poz. 34-38 for 2023-2024, poz. 36-40 for 2025)
- `cli.py` — Commands: `normalize`, `pit38`, `report`, `full`
- `__main__.py` — `python -m tax_calc`

**Tests**: 33 tests passing (test_binance_normalizer, test_kraken_normalizer, test_cost_pool, test_fifo, test_salary, test_nbp)

**Key finding from running the full pipeline**: 0 PLN tax in every year (2020-2025). Salary USDC costs create a massive cost shield. ~319K PLN carry-forward into 2026.

### 2. Analyzed Past Tax Filings

Read and analyzed the tax company's filings:
- `docs/personal-tax/2023/analysis-2023-filing.md` — PIT-37 + PIT-38 analysis
- `docs/personal-tax/2024/analysis-2024-filing.md` — PIT-37 only (no PIT-38!)
- `docs/personal-tax/2025/tax-correction-plan.md` — Full correction plan with priorities
- `docs/personal-tax/2025/additional-crypto-tax-analysis.md` — Why FIFO gains don't translate to actual tax

Key findings: Tax company used wrong form (PIT-37 instead of PIT-36), didn't file 2024 PIT-38 (breaking cost carry-forward chain), didn't pay monthly advance tax, didn't attach PIT/ZG. The barter doctrine approach (income at receipt = cost basis for PIT-38) is correct.

### 3. Conducted Extensive Tax Law Research

Created 12 research prompts in `docs/tax-law/`, sent to 4 AI research providers (ChatGPT 5.4 Pro, ChatGPT Deep Research, Perplexity, Gemini 3.1 Deep Research), and synthesized all 46 responses:

| # | Topic | Synthesis File |
|---|---|---|
| 01 | JDG ryczalt compliance | `01-jdg-business-income/synthesis-jdg-ryczalt-compliance.md` |
| 02 | USDC salary classification | `02-usdc-salary-classification/synthesis-usdc-salary-classification.md` |
| 03 | PIT-38 crypto capital gains | `03-crypto-capital-gains-pit38/synthesis-pit38-crypto-tax.md` |
| 04 | Stablecoin classification | `04-stablecoin-classification/synthesis-stablecoin-classification.md` |
| 05 | Loss carry-forward | `05-loss-carryforward/synthesis-loss-carryforward.md` |
| 06 | Late filing & corrections | `06-late-filing-corrections/synthesis-late-filing-corrections.md` |
| 07 | Filing checklist | `07-filing-checklist/synthesis-filing-checklist.md` |
| 08 | Cost basis & valuation | `08-cost-basis-valuation/synthesis-cost-basis-valuation.md` |
| 09 | Sweden->Poland transition | `09-residency-sweden-poland/synthesis-residency-transition.md` |
| 10 | General crypto framework | `10-general-crypto-tax-framework/synthesis-general-framework.md` |
| 11 | Platform losses (Celsius/BlockFi) | `11-platform-losses/synthesis-platform-losses.md` |
| 12 | DeFi, staking, airdrops | `12-defi-staking-airdrops/synthesis-defi-staking-airdrops.md` |

**Master synthesis**: `docs/tax-law/master-synthesis.md` — Pulls everything together into one reference.

### 4. Created New Research Prompts (Not Yet Researched)

| # | Topic | Prompt File |
|---|---|---|
| 13 | JDG stablecoin payments vs EUR | `13-jdg-stablecoin-payments/research-questions-jdg-stablecoin-vs-eur.md` |
| 14 | Bot trading tax implications | `14-bot-trading-tax-implications/research-questions-bot-trading-tax.md` |

These are ready to be sent to research providers but responses have not been collected yet.

### 5. Analyzed the Ironclad Finance DeFi Loss

Reviewed `docs/crypto-transactions/ironclad_loss_documentation.md` (~22.6 ETH, ~$62K loss from Ionic Money hack on Feb 4, 2025). Applied research findings:
- The hack is NOT a taxable event under Polish law
- No loss deduction available
- Original ETH acquisition costs remain in the cost pool
- The ETH -> ic-ETH conversion is the riskiest part (vault tokens likely aren't waluta wirtualna)
- Analysis provided in conversation but not written to a separate file

---

## What Remains To Be Done

### URGENT (before April 30, 2026)

1. **File 2024 PIT-38** — The most critical missing item. Check e-Urzad Skarbowy for auto-accepted PIT-38 first. File with czynny zal. This protects ~701K PLN of cost carry-forward.

2. **File 2025 PIT-38** — 15 fiat-exit events, 0 tax. Cost pool calculator output is ready.

3. **File 2025 PIT-28** — JDG ryczalt. Must be actively filed (NOT auto-accepted).

4. **File 2025 PIT-36** — Pre-JDG USDC salary income (Jan-Apr 2025, 40,500 USDC).

5. **Calculate pre-residency costs** — Extract all fiat->crypto purchases from Binance/Kraken for 2020-2022. Check against Swedish K4 returns for double-counting. Convert to PLN. Enter as `--pre-residency-costs` parameter. This could significantly increase the cost pool.

### HIGH PRIORITY (weeks after deadline)

6. **Correct 2023/2024 PIT-37 -> PIT-36** + PIT/ZG attachments.

7. **Consult ZUS specialist** — The biggest unknown financial risk. Umowa zlecenie classification implies mandatory ZUS at 30-40% of gross income. Could be 0 or 180K+ PLN depending on facts. Needs professional analysis.

8. **Collect research responses for prompts 13 and 14** — JDG stablecoin payments and bot trading implications. Synthesize when received.

### MEDIUM PRIORITY

9. **Write the Ironclad Finance analysis** to a proper document (currently only in conversation).

10. **Consider interpretacja indywidualna** (40 PLN, 3 months) for:
    - USDC salary classification under ryczalt JDG
    - Stablecoin (USDC) post-MiCA classification
    - Staking reward timing (receipt vs disposal)

11. **Sell worthless LUNA/UST dust** to crystallize indefinite cost carry-forward.

12. **Add pre-residency cost calculation** to the calculator — extract fiat->crypto from Binance/Kraken 2020-2022, verify against Swedish K4, compute PLN values.

### CODE IMPROVEMENTS

13. **Add NBP rate documentation** per transaction to calculator output (for audit trail).

14. **Handle USDC depeg** in price resolution (currently assumes 1:1 with USD).

15. **Add per-asset tracking** as secondary output alongside cost pool (defensive for audits even though not required for PIT-38).

16. **Consider bot transaction handling** in the calculator (pending research from prompt 14).

---

## Key Context for Continuing Agent

### The user's situation
- Swedish national, Polish tax resident since ~mid 2023
- JDG with ryczalt 12% for software development (established mid-2025)
- Before JDG: paid in USDC by US DeFi companies (2023-early 2025), classified as umowa zlecenie
- Active crypto since 2020: Binance, Kraken, DeFi, staking, Celsius/BlockFi losses
- Building liquidation/arbitrage bots (new activity, prompts 13-14)
- Tax company filed PIT-37 (wrong form), missed 2024 PIT-38, missed advance payments

### Critical findings from research
- Poland uses **annual cost pooling, NOT FIFO** for crypto (Art. 22 ust. 14-16, Art. 30b ust. 1b)
- Crypto-to-crypto swaps are **NOT taxable** (Art. 17 ust. 1f)
- Cost carry-forward is **unlimited** in time and amount (Art. 22 ust. 16)
- USDC salary: **barter doctrine** — income at receipt (PIT-36) + cost basis for PIT-38
- The cost pool calculator shows **0 tax every year** with ~319K PLN carry-forward
- DAC8 signed March 9, 2026 — exchanges will report to KAS starting 2027
- Staking/airdrop taxation is **actively disputed** (KIS vs courts)
- ZUS liability is the **biggest unknown** — needs specialist

### File structure
```
src/tax_calc/           — Python package (cost_pool.py is the main engine)
tests/                  — 33 passing tests
docs/tax-law/           — 14 research topic folders + master-synthesis.md
docs/personal-tax/      — 2023, 2024, 2025 folders with analyses and plans
docs/crypto-transactions/ — Exchange data, wallet info, salary payments, Ironclad loss doc
outputs/                — Calculator output (PIT-38 reports, normalized CSVs, JSON)
data/                   — NBP and CoinGecko caches
```

### Running the calculator
```bash
PYTHONPATH=src python -m tax_calc full
# or individual steps:
PYTHONPATH=src python -m tax_calc normalize
PYTHONPATH=src python -m tax_calc pit38
```

### Running tests
```bash
python -m pytest tests/ -v
```
