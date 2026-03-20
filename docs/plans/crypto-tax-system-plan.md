# Crypto Tax System — Implementation Plan

**Goal:** Accurately compute Polish PIT-38 crypto tax declarations for 2025 (current filing deadline), then correct 2023 and 2024.

**Date:** 2026-03-19

---

## Context

Polish tax rules for crypto:
- **Taxable event:** crypto → fiat, crypto → goods/services
- **NOT taxable:** crypto → crypto swaps, wallet transfers, staking receipt
- **Cost basis method:** FIFO (First-In, First-Out)
- **Tax rate:** 19% flat on net profit
- **Loss carry-forward:** up to 5 years
- **Exchange rate:** NBP mid-rate from the last business day before the transaction date
- **Form:** PIT-38 (annual)

Tax years in scope:
- **2020–2022:** User was Swedish tax resident (Skatteverket). These years matter only for establishing FIFO cost basis that carries forward into Polish years.
- **2023:** First year in Poland. PIT-38 was not filed correctly — needs correction (korekta).
- **2024:** Second year in Poland. PIT-38 was not filed correctly — needs correction.
- **2025:** Current filing year. Deadline approaching.

Data sources:
- Binance transaction exports 2020–2025 (~3200 rows)
- Kraken ledger exports 2020–2025 (~1278 rows across 6 yearly files)
- On-chain wallet activity (EVM, Solana, Sui, BTC, DOT, KSM)
- Polygon salary payments (USDC from Conclave, 2025)
- ClearStar invoices (EUR, paid via bank)

---

## Current Bugs & Issues

### Bug 1: Binance sells are inverted (CRITICAL)

**Symptom:** 13 of 15 Binance fiat-exit events in 2025 are invisible to the FIFO calculator.

**Root cause:** The exchange normalizer classifies USDC→EUR sells as:
```
tx_type=sell, asset=EUR, counterparty_asset=USDC
```
The FIFO calculator then sees `asset=EUR`, hits the `if asset in FIAT: continue` guard, and skips the event.

**Correct output should be:**
```
tx_type=sell, asset=USDC, counterparty_asset=EUR
```

**Impact:** 2025 report shows ~16,700 PLN revenue instead of ~275,000 PLN. Same bug affects all years.

**Where:** `exchange_normalizer.py`, Binance trade grouping logic (lines 248–380). The `"Sell Crypto To Fiat"` operation produces paired rows (one for crypto sold, one for fiat received). The grouping logic puts both in the `sells` list and doesn't correctly identify which side is the asset vs the counterparty.

### Bug 2: Zero cost basis on exchange deposits (CRITICAL)

**Symptom:** 2024 shows 678,599 PLN revenue with only 1,236 PLN cost basis. Real gain should be near zero (USDC ≈ $1).

**Root cause:** When crypto is deposited from a wallet to an exchange, the FIFO tracker creates a lot with `cost_pln=0` (or CoinGecko price if `--use-api` is set, but that path isn't used for stablecoins since they're not in CoinGecko map meaningfully).

**Correct behavior:** Deposits should either:
1. Match against a corresponding withdrawal from a known wallet (carrying cost basis through), or
2. For stablecoins received as salary, use the PLN value at receipt time (NBP USD rate × amount).

**Impact:** Massively inflates capital gains across 2023–2025. All USDC/USDT sold on exchanges appears as pure profit.

### Bug 3: No salary↔cost basis link

**Symptom:** 40,500 USDC received on Polygon in 2025 as salary has no connection to the FIFO lots used when that USDC is deposited to Binance/Kraken and sold for EUR.

**Correct behavior:** USDC received as JDG business income is already taxed as income. For PIT-38 purposes, its acquisition cost = PLN value at receipt date (NBP USD mid-rate × USDC amount). This cost basis should flow through deposit→exchange→sell.

### Bug 4: Static exchange rates

All outputs currently use hardcoded approximations (`EUR≈4.30`, `USD≈3.95`). Polish tax law requires the NBP mid-rate from the last business day before each transaction. The `--use-api` flag for the FIFO calculator exists but produces incorrect results due to bugs 1–3 above.

### Bug 5: Loss carry-forward built on bad data

The 2022 mega-loss of -1,192,148 PLN and 2021 gain of 129,318 PLN are computed with bugs 1–3 active. The loss carry-forward that currently wipes out 2023–2025 tax is unreliable. This needs to be recomputed after all fixes.

---

## Architecture Decision: Restructure as a proper Python project

The current scripts live in `docs/crypto-transactions/` alongside data files. They share logic (decimal parsing, CSV writing, price resolution) but each script duplicates it. Before adding more complexity, restructure into a proper project.

### Proposed structure

```
tax-calculator/
├── src/
│   └── tax_calc/
│       ├── __init__.py
│       ├── models.py              # Transaction, FIFOLot, TaxEvent dataclasses
│       ├── constants.py           # FIAT, STABLECOINS, asset maps, etc.
│       ├── nbp.py                 # NBP exchange rate client (with disk cache)
│       ├── prices.py              # Price resolution (NBP, CoinGecko, stablecoin logic)
│       ├── normalizers/
│       │   ├── __init__.py
│       │   ├── base.py            # UnifiedTransaction schema, shared helpers
│       │   ├── binance.py         # Binance CSV normalizer (fixed)
│       │   ├── kraken.py          # Kraken CSV normalizer
│       │   ├── onchain.py         # On-chain wallet tx normalizer
│       │   └── salary.py          # Salary/income source annotator
│       ├── fifo.py                # FIFO tracker and cost basis engine
│       ├── deposit_matcher.py     # Match exchange deposits ↔ wallet withdrawals
│       ├── pit38.py               # PIT-38 report generator
│       └── cli.py                 # Unified CLI entry point
├── data/                          # Symlink or move from docs/crypto-cex-transactions
│   ├── binance/
│   ├── kraken/
│   ├── wallets.txt
│   ├── config.json
│   └── salary/                    # Salary payment records
│       └── polygon_2025.csv
├── outputs/                       # Generated reports
├── tests/
│   ├── test_normalizers.py
│   ├── test_fifo.py
│   ├── test_deposit_matcher.py
│   └── fixtures/                  # Small representative test data
├── docs/
│   └── plans/
└── pyproject.toml
```

---

## Implementation Phases

### Phase 1: Fix core accuracy for 2025 filing

This is the minimum needed to file a correct 2025 PIT-38. Everything else can wait.

#### Step 1.1: Set up project structure
- Create `src/tax_calc/` package with `pyproject.toml`
- Move shared constants and helpers into `constants.py` and `models.py`
- Keep old scripts in `docs/crypto-transactions/` as reference until migration is complete

#### Step 1.2: Fix Binance normalizer
- Rewrite the Binance trade grouping logic
- For `"Sell Crypto To Fiat"` paired rows: the entry with negative change is the asset sold (USDC/USDT), the entry with positive change is the fiat received (EUR)
- For `"Buy Crypto With Fiat"` and `"Buy Crypto With Card"`: similar fix
- For `"Binance Convert"`: already handled correctly (positive=received, negative=spent)
- Handle edge cases: multiple fills at same timestamp, partial fills, fee entries
- Write tests against known 2025 Binance data (13 sells documented in `binance_fiat_exit_overview_2025.md`)

#### Step 1.3: Fix Kraken normalizer
- Review and verify Kraken logic is correct (appears mostly OK based on output)
- Ensure `"receive"` and `"spend"` types (instant buy/sell) are handled correctly
- Write tests

#### Step 1.4: Build salary/income cost basis annotator
- Parse Polygon salary payment records (the `2025-polygon-payments.txt` has 7 payments)
- For each USDC salary receipt, compute PLN value using NBP USD mid-rate from last business day before receipt
- Generate FIFO lots with proper cost basis: `source=salary, date=receipt_date, amount=USDC, cost_pln=amount×NBP_USD_rate`
- These lots feed into the FIFO tracker before exchange deposits are processed

#### Step 1.5: Build deposit↔withdrawal matcher
- Goal: when USDC appears as a deposit on Binance, trace it back to the wallet withdrawal that sent it
- Match by: asset, approximate amount (minus network fees), and timing (deposit shortly after withdrawal)
- When matched, the deposit inherits cost basis from the source lot instead of getting `cost_pln=0`
- For the 2025 flow this is straightforward: Polygon salary → wallet → Binance deposit → sell for EUR
- For older years this is harder (more wallets, more chains, DeFi interactions)

#### Step 1.6: Integrate NBP live rates
- Build an NBP rate client with disk-based cache (avoid re-fetching same dates)
- For each transaction, fetch PLN rate for the counterparty currency (EUR, USD) using the **last business day before** the transaction date
- Replace all `approx_*` resolution methods with live NBP data
- Cache format: simple JSON file `{(currency, date): rate}` persisted to `data/nbp_cache.json`

#### Step 1.7: Recompute and validate 2025
- Run full pipeline: normalize → annotate salary → match deposits → FIFO → PIT-38
- Cross-validate against `binance_fiat_exit_overview_2025.md` (15 events, ~63,900 EUR gross)
- Cross-validate against Polygon payment records (40,500 USDC)
- Verify total revenue, cost basis, and net gain make sense
- Generate final PIT-38 report for 2025

**Expected 2025 outcome:** Revenue ≈ 275,000 PLN (63,900 EUR × ~4.30). Cost basis ≈ 270,000 PLN (stablecoins at acquisition value). Net gain ≈ small amount from EUR/PLN exchange rate movements. Tax ≈ low or offset by any prior losses.

---

### Phase 2: Correct 2023 and 2024

#### Step 2.1: Trace 2023–2024 salary/income sources
- Identify all salary/income USDC payments for 2023 and 2024
- Run wallet tracker for 2023–2024 on Polygon (where salary was received)
- Cross-reference with invoice records in `docs/invoices/`
- Compute cost basis for each income receipt

#### Step 2.2: Trace on-chain flows for 2023–2024
- Run wallet tracker for all known wallets for 2023–2024
- Build deposit↔withdrawal matching for those years
- The main flow is likely: salary USDC on Polygon → deposit to Kraken → sell for EUR
- Verify against Kraken tax events in those years

#### Step 2.3: Recompute 2023 and 2024 with fixes
- Run the full corrected pipeline for 2023 and 2024
- Compare with the buggy outputs to understand the delta
- Generate corrected PIT-38 reports (korekta)

#### Step 2.4: Handle 2020–2022 for FIFO chain
- Even though these are Swedish tax years, we need correct FIFO lots for cost basis that carries into 2023+
- Recompute with fixed normalizers
- Verify the 2022 mega-loss (likely inflated by zero-cost-basis bug)
- Recalculate loss carry-forward

---

### Phase 3: Complete wallet coverage and edge cases

#### Step 3.1: Verify and add missing wallets
- Cosmos (ATOM): ~297 ATOM withdrawn to self-custody in early 2022, later deposited 353 ATOM to Kraken. Need the cosmos1... address.
- Terra (LUNA/UST): Heavy DeFi activity 2021–2022, Anchor Protocol usage. Chain collapsed May 2022. Need Terra Station address for historical records.
- Monero (XMR): 0.42 XMR withdrawn from Kraken Nov 2022. Privacy chain — can only find address from Kraken withdrawal history or email.
- Second Solana wallet: 2025 SOL withdrawals from Binance likely went to a different wallet than "Old Solana".
- Additional EVM/Sui wallets: Lower priority, may already be covered by existing 4 EVM wallets.

#### Step 3.2: Handle collapsed/locked assets
- **Terra LUNA/UST collapse (May 2022):** The ~44K UST and ~3.5K LUNA in Anchor Protocol became near-worthless. This is a real capital loss that should be claimed.
- **Celsius BTC:** Funds locked in bankruptcy. May be partially recoverable. Track as unrealized loss until resolution.
- **BlockFi BTC:** Same as Celsius.
- **LUNA2 airdrop:** Received post-collapse, deposited 69 LUNA2 to Kraken and sold. This is already in the data.

#### Step 3.3: Handle DeFi positions
- Polkadot staking rewards (DOT.S) — already captured by Kraken
- Kusama crowdloan participation — contributed KSM, received parachain tokens (ACA, KAR)
- Fantom DeFi activity (Reaper strategist wallet)
- These may generate additional FIFO lots that need to be accounted for

#### Step 3.4: Bitcoin UTXO tracking
- BTC uses UTXO model; Electrum wallet may have many change addresses
- Current wallets.txt has 4 Electrum addresses but BTC wallets generate new addresses per transaction
- May need to use Electrum's xpub or address list export for complete tracking
- Lower priority if BTC was mostly held (not sold) during Polish tax years

---

## Validation Strategy

For each tax year, cross-validate the computed results against:

1. **Exchange fiat exit totals:** Sum of all EUR received from crypto sells should match bank deposit records
2. **Exchange withdrawal/deposit pairs:** Every exchange deposit should trace to a wallet withdrawal (or external source)
3. **FIFO lot inventory sanity:** Remaining lots at end of year should roughly match actual holdings
4. **NBP rate spot checks:** Pick a few transactions and manually verify the PLN conversion
5. **Stablecoin cost basis:** Selling USDC/USDT for EUR should produce near-zero gain (just FX movement), not 100% gain

---

## Open Questions

1. **2020–2022 Swedish tax obligations:** Were crypto taxes declared in Sweden? If gains were already taxed there, how does that interact with Polish FIFO cost basis?
2. **JDG income overlap:** Is the Polygon USDC salary already being declared as JDG business income on PIT-36? If so, the PIT-38 cost basis for that USDC should equal the declared income amount.
3. **Korekta filing process:** What's the process for filing corrected PIT-38 for 2023 and 2024? Any penalties or interest?
4. **Gifted crypto (Chloe's Celsius DOT):** How should gifted crypto be handled under Polish tax law? Cost basis transfers from giver, or is it different?
5. **Celsius/BlockFi bankruptcy claims:** Any distributions received? Any formal loss recognition events?
6. **Terra collapse:** Is there a mechanism under Polish tax law to claim capital loss on assets that became worthless without a disposal event?
7. **Kraken saved withdrawal addresses:** Can you export the full list? This would immediately resolve the Cosmos and Monero wallet discovery.
