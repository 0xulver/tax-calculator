# Session: April 16, 2026 -- Added Fiat Purchases + System State

## What Was Done This Session

### Added FTX, Coinbase, and Celsius fiat purchases to the PIT-38 calculator

These are all pre-Poland-residency (2020-2021) fiat-to-crypto purchases that are deductible as acquisition costs under Polish PIT-38 (per WSA Warsaw III SA/Wa 1290/24).

| Source | Currency | Transactions | Fiat Total | PLN Value |
|--------|----------|---:|---:|---:|
| Celsius/Simplex | SEK | 6 | 43,537.80 SEK | 19,681.99 PLN |
| Coinbase | EUR | 5 | 2,630.00 EUR | 11,989.28 PLN |
| FTX | EUR | 2 | 1,350.14 EUR | 6,101.83 PLN |

### Code changes made (all uncommitted)

1. **`src/tax_calc/models.py`** -- Added `asset` and `fiat_currency` fields to `FIFOLot` dataclass (defaults: "USDC", "USD" for backward compat)

2. **`src/tax_calc/normalizers/salary.py`** -- Made the parser currency-aware:
   - Added `source_name` parameter to `parse_salary_payments()` and `_parse_payment()`
   - Parser now detects currency from amount line (USDC/USDT -> USD rate, EUR -> EUR rate, SEK -> SEK rate)
   - Sets `asset`, `fiat_currency`, `source` on FIFOLot based on parsed data

3. **`src/tax_calc/cost_pool.py`** -- Updated salary lot injection:
   - Uses `lot.fiat_currency` and `lot.asset` instead of hardcoded "USD"/"USDC"
   - Only adds to `salary_years` set when `"salary" in lot.source` (fiat purchases don't trigger stablecoin deposit dedup)
   - Dynamic `price_method` and `notes` based on whether it's salary vs purchase

4. **`src/tax_calc/pit38.py`** -- Updated `_categorize_cost()`:
   - Matches `"salary" in event.source` instead of `== "polygon_salary"`
   - New category `"Fiat purchases (EXCHANGE)"` for purchase sources

5. **`src/tax_calc/cli.py`** -- Added 3 new files to `--salary` defaults in both `pit38` and `full` subcommands:
   - `ftx-purchases.txt`, `coinbase-purchases.txt`, `celsius-simplex-purchases.txt`
   - Added source name detection from filename in `cmd_pit38()`

6. **Data files created** (all in `docs/crypto-transactions/`):
   - `ftx-purchases.txt` -- 2 EUR deposits, May-Jun 2021
   - `coinbase-purchases.txt` -- 5 EUR purchases (SNX/AAVE), Mar-Jun 2021
   - `celsius-simplex-purchases.txt` -- 6 SEK purchases (CEL), Dec 2020-Jan 2021

All files use the standard URL/date/amount block format so the existing parser handles them.

### Tests: all 7 pass (`python -m pytest tests/test_cost_pool.py -x -q`)

---

## Current Calculator Output (as of this session)

```
2020: carry-forward -> 274,399 PLN
2021: carry-forward -> 570,495 PLN
2022: carry-forward -> 643,323 PLN
2023: carry-forward -> 935,153 PLN
2024: carry-forward -> 637,710 PLN
2025: carry-forward -> 563,627 PLN (to 2026)
Tax due: 0 PLN in ALL years
```

Run with: `PYTHONPATH=src python -m tax_calc pit38`

---

## Filing Summary (Deadline: April 30, 2026)

See `docs/todo/filing-summary.md` for full details. Key numbers:

| Form | Year | Tax Due | Status |
|------|------|---:|---|
| PIT-38 korekta | 2023 | 0 PLN | Not filed -- needs correction |
| PIT-38 korekta | 2024 | 0 PLN | Not filed -- **FILE FIRST** |
| PIT-38 | 2025 | 0 PLN | Not filed |
| PIT-36 | 2025 | 14,060 PLN | Not filed (pre-JDG USDC salary) |
| PIT-28 | 2025 | 29,211 PLN | Not filed (JDG ryczalt, ~3,077 PLN refund expected) |

**Filing order matters**: PIT-38 2024 korekta first, then 2025 PIT-38 (carry-forward chain).

**Total new tax to pay**: ~10,983 PLN + ~500-1,000 PLN interest on late zaliczki.

---

## What Needs to Be Done Next (Priority Order)

### 1. Commit all changes to git
There are many uncommitted changes spanning multiple sessions. The `.env` file (contains ETHERSCAN_API_KEY) should NOT be committed.

### 2. Update filing-summary.md with latest numbers
The filing summary was written April 14 and the carry-forward numbers have changed since then (added Celsius/Coinbase/FTX costs). The PIT-38 field values need updating:

- 2024 Poz. 36 (costs prior years) changed because 2023 carry-forward changed
- 2025 Poz. 38 (costs prior years) changed because 2024 carry-forward changed
- All carry-forward amounts shifted up by ~37.8K PLN

### 3. Write a filing guide with exact form field numbers
The user needs to actually enter numbers into e-Deklaracje. Write a step-by-step guide with exact PIT-38 position numbers (Poz. 34-40 for 2023, Poz. 34-40 for 2024, Poz. 36-40 for 2025).

### 4. Verify Fantom transactions
When FTMScan comes back online, verify the 19 tx hashes in `docs/crypto-transactions/2022-fantom-salary.txt` (currently "pending-verification").

### 5. Parse Conclave PDF invoices
7 PDFs in `docs/invoices/2025/invoices-conclave/` -- not yet parsed. Would help cross-reference PIT-36 salary amounts.

### 6. Lower priority corrections (after April 30)
- Correct 2023/2024 PIT-37 -> PIT-36 + PIT/ZG (wrong form, same numbers)
- Swedish sjalvrattelse for 2023-2024 (zero returns, may incur late fees)

---

## Key Architecture Notes for Next Agent

### How the cost pool works
Polish PIT-38 does NOT use FIFO. It's annual cost pooling:
- Sum all fiat spent on crypto in the year = costs
- Sum all fiat received from selling crypto = revenue
- If costs > revenue: income = 0, excess carries forward
- Carry-forward is unlimited in duration

### How salary lots avoid double-counting
USDC received as salary is a cost (at NBP USD rate on receipt date). The same USDC later gets deposited to an exchange (Binance/Kraken) and appears as a "deposit" in exchange data. To avoid counting it twice, `salary_years` tracks which years have salary data, and stablecoin deposits in those years are skipped.

Fiat purchases (FTX/Coinbase/Celsius) do NOT trigger this dedup -- they set `"purchase"` in their source name, not `"salary"`.

### File layout
- `src/tax_calc/cost_pool.py` -- Core PIT-38 engine
- `src/tax_calc/pit38.py` -- Markdown report generator
- `src/tax_calc/pit36.py` -- PIT-36 calculator (pre-JDG salary)
- `src/tax_calc/pit28.py` -- PIT-28 ryczalt calculator (JDG invoices)
- `src/tax_calc/cli.py` -- CLI entry point
- `src/tax_calc/normalizers/salary.py` -- Parses salary/purchase block files
- `src/tax_calc/normalizers/binance.py` -- Normalizes Binance CSVs
- `src/tax_calc/normalizers/kraken.py` -- Normalizes Kraken CSVs
- `docs/crypto-transactions/` -- All salary and purchase data files
- `docs/todo/filing-summary.md` -- Master filing guide
- `outputs/` -- Generated reports and JSON results

### Running the system
```bash
PYTHONPATH=src python -m tax_calc pit38     # PIT-38 only
PYTHONPATH=src python -m tax_calc full      # normalize + pit38
python -m pytest tests/ -x -q              # run tests
```

### Important context
- User moved to Poland: April 12, 2023
- First Polish tax year: 2023
- JDG (sole proprietorship) started: May 2025
- Pre-JDG salary (Jan-Apr 2025): taxed as PIT-36, NOT ryczalt
- ETHERSCAN_API_KEY is in `.env` (for Polygon/Etherscan API calls)
- The user's tax company filed 2023-2024 using PIT-37 (wrong form, should be PIT-36 + PIT/ZG for foreign income)
