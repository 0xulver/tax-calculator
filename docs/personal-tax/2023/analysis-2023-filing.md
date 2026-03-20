# Analysis: 2023 Tax Filing

Filed late on **June 7, 2024** (deadline was April 30, 2024).
Accompanied by **czynny zal** (active regret letter) and **pismo przewodnie** (cover letter).

Tax office: **Urzad Skarbowy Warszawa-Wola**
Address: Skierniewicka 34A, 01-230 Warszawa

---

## Documents Filed

1. **PIT-37** (service income)
2. **PIT-38** (crypto capital gains)
3. **Czynny zal** (voluntary disclosure of late filing)

The czynny zal states the reason for late filing was "not intentional, but lack of awareness that in Poland income tax must be settled by 30 April." It references both PIT-37 and PIT-38 for income from "umowa zlecenie" and "sale of virtual currency."

---

## PIT-37 (2023): Service Income

### What they reported

| Field | Description | Amount |
|---|---|---|
| Poz. 67 | Revenue (umowy zlecenia, Art. 13 pkt 8) | **448,108.20 PLN** |
| Poz. 68 | Costs (20% standard deduction) | **89,621.64 PLN** |
| Poz. 85 | Taxable income (dochod) | **358,486.56 PLN** |
| Poz. 86 | Advance tax paid by payer | **0 PLN** |
| Poz. 129 | Tax base (rounded) | **358,487 PLN** |
| Poz. 130 | Tax at progressive scale | **87,115.84 PLN** |
| Poz. 137 | Tax due (rounded) | **87,116 PLN** |
| Poz. 138 | **TAX TO PAY** | **87,116 PLN** |

### How they calculated it

1. **Income source**: Classified as "dzialalnosc wykonywana osobiscie" (personally performed activity) under **Art. 13 ustawy o PIT**, specifically as umowa zlecenie (Art. 13 pkt 8).

2. **Revenue**: 448,108.20 PLN. This represents USDC salary payments from **Byte Masons LLC** (US DeFi company), converted to PLN. Input invoices show biweekly invoices of 6,000 USDC each (#7 through #32, skipping #17 = ~25 invoices). However, 25 x 6,000 = 150,000 USDC which at avg ~4.2 PLN/USD would be ~630K PLN, much more than 448K PLN. This suggests either:
   - Not all 2023 invoices were counted (some may have been for late-2022 work not yet recognized)
   - The tax company used actual USDC receipt dates rather than invoice dates to determine which payments fell in 2023
   - Some conversion rate logic reduces the total

   **My best estimate**: ~107,000 USDC was recognized as 2023 income (448,108 / ~4.18 avg USD rate), which is roughly 18 biweekly payments.

3. **Cost deduction**: Exactly 20% of revenue (89,621.64 = 448,108.20 x 0.2). This is the standard flat-rate cost deduction for umowa zlecenie under Art. 22 ust. 9 pkt 4.

4. **Tax calculation**: Progressive scale (12%/32%) with 30,000 PLN tax-free amount:
   - First 120,000 PLN: 120,000 x 12% - 3,600 (kwota wolna) = 10,800
   - Above 120,000: (358,487 - 120,000) x 32% = 238,487 x 0.32 = 76,315.84
   - Total: 10,800 + 76,315.84 = **87,115.84 PLN** (matches poz. 130)

5. **No advance tax paid** (poz. 86 = 0): The full 87,116 PLN was due at filing.

### Potential issues with PIT-37

- **Wrong form?** PIT-37 requires income backed by PIT-11/IFT-1R. A US LLC paying in USDC on Polygon almost certainly didn't issue either document. PIT-36 would be the correct form for self-reported foreign income.
- **No advance tax payments**: With a foreign payer, the taxpayer should have been making monthly advance payments themselves (Art. 44 ust. 1a). Interest on late payment would accrue from each monthly deadline.
- **No PIT/ZG attachment**: Foreign income should have PIT/ZG annex attached.
- **Classification as umowa zlecenie**: Debatable for crypto payments from a foreign company with no Polish presence and no formal written zlecenie contract.

---

## PIT-38 (2023): Crypto Capital Gains

### What they reported

| Field | Description | Amount |
|---|---|---|
| Poz. 34 | Revenue from crypto disposal | **226,115.71 PLN** |
| Poz. 35 | Costs incurred in tax year | **448,108.20 PLN** |
| Poz. 36 | Costs from prior years (undeducted) | **0 PLN** |
| Poz. 37 | Income (dochod) | **0.00 PLN** |
| Poz. 38 | Undeducted costs (carry forward) | **221,992.49 PLN** |
| Poz. 43 | **TAX DUE** | **0 PLN** |

### How they calculated it

1. **Revenue (226,115.71 PLN)**: This represents USDC-to-EUR conversions on Kraken during 2023. The input file "USDC to EUR transactions.txt" shows 16 Kraken trades from April to November 2023:

   | Date | USDC sold | EUR received | EUR fee |
   |---|---|---|---|
   | Apr 26 | 2,705.78 | 2,455.22 | 36.28 |
   | May 22 | 4,000.00 | 3,694.79 | 54.60 |
   | Jun 5 | 3,312.56 | 3,097.24 | 45.77 |
   | Jun 21 | 3,000.00 | 2,742.90 | 40.54 |
   | Jul 3 | 3,000.00 | 2,747.40 | 40.60 |
   | Jul 19 | 3,000.00 | 2,670.90 | 39.47 |
   | Aug 1 | 3,000.00 | 2,724.90 | 40.27 |
   | Aug 15 | 3,000.00 | 2,741.70 | 40.52 |
   | Aug 23 | 1,001.09 | 922.50 | 13.63 |
   | Sep 2 | 3,000.00 | 2,783.33 | 41.13 |
   | Sep 10 | 4,498.82 | 4,206.40 | 62.16 |
   | Sep 18 | 6,000.00 | 5,619.00 | 83.04 |
   | Oct 17 | 3,000.00 | 2,845.80 | 42.06 |
   | Nov 5 | 6,000.00 | 5,594.30 | 82.67 |
   | Nov 27 | 6,000.00 | 5,480.44 | 80.99 |
   | **Total** | **~54,518 USDC** | **~50,327 EUR** | **~743 EUR** |

   The 226,115.71 PLN would be the total EUR received converted to PLN using NBP rates at each transaction date. Rough check: 50,327 EUR x ~4.50 avg NBP EUR rate = ~226K PLN. This checks out.

2. **Costs (448,108.20 PLN)**: This is **exactly the same number as the PIT-37 revenue**. This is the key insight into their approach:
   - They treat receiving USDC as salary = acquiring crypto at the PLN value declared as income
   - So the cost basis of ALL USDC received in 2023 = 448,108.20 PLN
   - Under Polish PIT-38 rules, you can declare ALL acquisition costs in the year, even if you haven't disposed of all the crypto yet

3. **Net result**: Costs (448K) > Revenue (226K), so:
   - Dochod = 0 (no taxable income)
   - Undeducted costs = 448,108.20 - 226,115.71 = **221,992.49 PLN** (carries to 2024)
   - Tax = **0 PLN**

### The double-reporting logic

This is the most interesting aspect of how the tax company handled it:

```
USDC received as salary
  → PIT-37: 448K PLN taxed as service income (12%/32% progressive)
  → PIT-38: 448K PLN becomes the cost basis for when USDC is sold

USDC converted to EUR on Kraken
  → PIT-38: 226K PLN revenue from crypto disposal
  → Net: 226K revenue - 448K costs = 0 tax (excess costs carry forward)
```

**The total tax for 2023**: Only the PIT-37 income tax of **87,116 PLN** (no additional crypto tax).

This approach is internally consistent: the USDC is taxed once as income when received, and when sold, the cost basis equals the income value, so the crypto disposal is effectively tax-neutral (only producing gain/loss from PLN/EUR/USD rate movements between receipt and conversion).

### Potential issues with PIT-38

- **Is this the correct approach?** It depends on whether USDC salary should be treated as income (PIT-37) + crypto (PIT-38), or as just one of those. The "double reporting" approach taxes the receipt as income and makes the disposal tax-neutral, which seems reasonable but is not clearly established by KIS interpretations.
- **Cost basis = full salary**: They declared the ENTIRE 448K PLN as crypto costs, even though only ~54K USDC was actually sold. Under Polish PIT-38 rules this IS allowed (all acquisition costs can be declared, excess carries forward), but it creates a large carry-forward.

---

## Total Tax Burden for 2023

| Form | Tax Due | Status |
|---|---|---|
| PIT-37 | 87,116 PLN | Filed late (June 2024), with czynny zal |
| PIT-38 | 0 PLN | Filed late (June 2024), with czynny zal |
| **Total** | **87,116 PLN** | Plus potential interest on late payment |

Interest on the 87,116 PLN would accrue from May 1, 2024 (original deadline) to payment date. At ~14.5% annual rate (2024 Polish late payment interest), ~1 month late = ~1,050 PLN in interest. If monthly advance payments should have been made during 2023, the interest could be significantly higher.

---

## Notable Details

- **Different address** from 2024: Skierniewicka 34A vs Solec 24/239.1 (you moved between filings)
- **Different tax office**: Warszawa-Wola vs Trzeci US Warszawa-Srodmiescie
- **Client**: Byte Masons LLC (US-registered DeFi company)
- **Payment method**: USDC.e on Polygon to wallet 0x01C1a8D062b29dD2AC3aE49b717C02C99bADe52a
- **No other crypto disposals reported**: Only USDC→EUR conversions. No reporting of any other crypto trading activity from personal holdings (Binance, self-custody, etc.)
