# Analysis: 2024 Tax Filing

Filed by the tax company (timing unclear, likely near April 30, 2025 deadline).

Tax office: **Trzeci Urzad Skarbowy Warszawa-Srodmiescie**
Address: Solec 24 m. 239.1, 00-403 Warszawa (new address, moved from Skierniewicka)

---

## Documents Filed

1. **PIT-37** (service income) -- the only tax form filed for 2024
2. **NO PIT-38** was filed for crypto capital gains

---

## PIT-37 (2024): Service Income

### What they reported

| Field | Description | Amount |
|---|---|---|
| Poz. 67 | Revenue (umowy zlecenia, Art. 13 pkt 8) | **479,092.64 PLN** |
| Poz. 68 | Costs (20% standard deduction) | **95,818.53 PLN** |
| Poz. 85 | Taxable income (dochod) | **383,274.11 PLN** |
| Poz. 86 | Advance tax paid by payer | **0 PLN** |
| Poz. 129 | Tax base (rounded) | **383,274 PLN** |
| Poz. 130 | Tax at progressive scale | **95,047.68 PLN** |
| Poz. 137 | Tax due (rounded) | **95,048 PLN** |
| Poz. 138 | **TAX TO PAY** | **95,048 PLN** |

### How they calculated it

1. **Income source**: Same classification as 2023 -- "dzialalnosc wykonywana osobiscie" (Art. 13), specifically umowa zlecenie (Art. 13 pkt 8).

2. **Revenue**: 479,092.64 PLN. This represents USDC salary payments from two clients:
   - **Byte Masons LLC**: Invoices #34-#52 (skipping #47), roughly 18 invoices x 6,000 USDC = 108,000 USDC (Jan-Sep 2024)
   - **Conclave**: Invoice #57 for 12,000 USDC (Dec 16, 2024)
   - Possibly invoices #53-#56 from Oct/Nov 2024 (not in the input folder, but the total suggests they exist)
   - Total: ~120,000 USDC. At avg ~4.0 PLN/USD = ~480K PLN. This matches 479,092.64 PLN very closely.

3. **Cost deduction**: 95,818.53 PLN = exactly 20% of 479,092.64. Standard umowa zlecenie deduction.

4. **Tax calculation**: Progressive scale with 30,000 PLN tax-free amount:
   - First 120,000 PLN: 120,000 x 12% - 3,600 = 10,800
   - Above 120,000: (383,274 - 120,000) x 32% = 263,274 x 0.32 = 84,247.68
   - Total: 10,800 + 84,247.68 = **95,047.68 PLN** (matches poz. 130)

5. **No advance tax paid** (poz. 86 = 0): The full 95,048 PLN was due at filing.

### Comparison with 2023

| | 2023 | 2024 | Change |
|---|---|---|---|
| Revenue | 448,108.20 PLN | 479,092.64 PLN | +7% |
| Costs (20%) | 89,621.64 PLN | 95,818.53 PLN | +7% |
| Dochod | 358,486.56 PLN | 383,274.11 PLN | +7% |
| Tax due | 87,116 PLN | 95,048 PLN | +9% |

The revenue increase is primarily from: (a) more USDC invoiced, (b) Conclave's 12K USDC invoice, and (c) slightly different NBP USD rates.

---

## Missing PIT-38 for 2024

### What SHOULD have been filed

The tax company did NOT file a PIT-38 for 2024. This is a significant omission because:

1. **Undeducted costs from 2023**: The 2023 PIT-38 declared 221,992.49 PLN in undeducted acquisition costs that should carry forward to 2024. Without a 2024 PIT-38, these costs have nowhere to go.

2. **Crypto disposals in 2024**: Our tax calculator found several crypto-to-fiat events in 2024:
   - **Binance "Sell Crypto To Fiat"** events in Oct-Nov 2024 (ETH -> EUR: ~0.575 ETH + ~1.33 ETH)
   - Possibly USDC -> EUR conversions on Kraken or Binance
   - These should have been reported on PIT-38 as crypto disposal revenue

3. **USDC salary as crypto cost basis**: Following the same logic as 2023, the 479,092.64 PLN in USDC received should be declared as crypto acquisition costs on PIT-38. Without doing this, the cost basis is lost -- when this USDC is eventually converted to EUR, there would be no cost to offset against the revenue.

### What the missing PIT-38 should contain (estimated)

| Field | Description | Estimated Amount |
|---|---|---|
| Poz. 34 | Revenue from crypto disposal | TBD (USDC->EUR + ETH->EUR conversions) |
| Poz. 35 | Costs incurred in 2024 | ~479,092.64 PLN (salary USDC) |
| Poz. 36 | Costs from prior years | 221,992.49 PLN (from 2023 PIT-38) |
| Poz. 37 | Income | Likely 0 (costs > revenue) |
| Poz. 38 | Undeducted costs carry forward | Large (likely 500K+ PLN) |

### Why this matters

Without a 2024 PIT-38:
- The 221,992.49 PLN carry-forward from 2023 is stranded
- The 479K PLN in 2024 USDC acquisition costs are not declared
- Any 2024 crypto disposals (ETH->EUR, USDC->EUR) are unreported
- When this USDC is eventually sold in 2025, there will be no cost basis, potentially triggering a massive phantom gain

**This needs to be corrected with a korekta (correction) filing that adds a PIT-38 for 2024.**

---

## Potential Issues (Same as 2023, Plus New Ones)

### Carried over from 2023
1. **PIT-37 is likely the wrong form** -- should be PIT-36 for foreign payer income without PIT-11/IFT-1R
2. **No advance tax payments** -- monthly zaliczki should have been self-calculated and paid
3. **No PIT/ZG attachment** for foreign income
4. **Umowa zlecenie classification** questionable for USDC payments from US companies

### New for 2024
5. **No PIT-38 filed** -- crypto disposals unreported, cost basis lost
6. **Two clients (Byte Masons + Conclave)** -- both paying in USDC. The regularity and scale (~40K PLN/month, multiple clients) strengthens the argument this is de facto business activity (dzialalnosc gospodarcza), not personal services (umowa zlecenie)
7. **Invoice payment dates**: Many 2024 invoices show "Paid on: March 14, 2025" -- if using accrual basis (invoice date = revenue date), this is fine. But if the tax company used cash basis, these might not be 2024 income at all.

---

## Total Tax Burden for 2024

| Form | Tax Due | Status |
|---|---|---|
| PIT-37 | 95,048 PLN | Filed (likely on time) |
| PIT-38 | 0 PLN (estimated) | **NOT FILED -- needs correction** |
| **Total** | **95,048 PLN** | |

---

## Summary: What the Tax Company Did Across Both Years

### Their approach
1. Treat USDC salary as **personal service income** (umowa zlecenie) on PIT-37
2. Apply **20% flat-rate cost deduction** (standard for zlecenie)
3. Tax at **progressive rates** (12%/32%) with zero advance payments
4. On PIT-38 (2023 only): declare the same USDC amount as **crypto acquisition cost**, making crypto disposals effectively tax-neutral
5. Carry forward excess costs

### What they got right
- The overall approach of treating USDC salary as income + crypto cost basis is internally consistent
- The tax calculations are arithmetically correct
- They filed the czynny zal for 2023 (proper voluntary disclosure)
- The 20% cost deduction is standard for the classification they chose

### What they likely got wrong
- **PIT-37 instead of PIT-36**: No PIT-11/IFT-1R from foreign payer
- **No monthly advance tax payments**: Creates interest liability
- **No PIT/ZG**: Foreign income annex missing
- **No PIT-38 for 2024**: Major omission
- **No reporting of other crypto activity**: Only USDC->EUR conversions were reported on PIT-38. Any other crypto trading (BTC, ETH, DOT, etc. on Binance/Kraken) from personal holdings was not included.
- **Classification may be wrong**: Could be dzialalnosc gospodarcza rather than umowa zlecenie, especially given the regularity, multiple clients, and high amounts.
