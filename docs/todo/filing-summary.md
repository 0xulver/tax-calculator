# Tax Filing Summary -- What Needs to Be Done

**Date**: April 16, 2026
**Deadline**: April 30, 2026 (14 days)

---

## Current Bottom Line

| Form | Year | Type | Tax Due | Already Paid | Net Effect |
| --- | --- | --- | ---: | ---: | ---: |
| PIT-38 korekta | 2023 | Crypto capital gains | 0 PLN | 0 PLN | 0 PLN |
| PIT-38 korekta / zalegle zeznanie | 2024 | Crypto capital gains | 0 PLN | 0 PLN | 0 PLN |
| PIT-38 | 2025 | Crypto capital gains | 0 PLN | 0 PLN | 0 PLN |
| PIT-36 | 2025 | Pre-JDG USDC salary | 14,060 PLN | 0 PLN | 14,060 PLN |
| PIT-28 | 2025 | JDG ryczalt | 29,211 PLN | 32,288 PLN | -3,077 PLN |
| **TOTAL NEW TAX / REFUND** | | | | | **~10,983 PLN to pay** |

Additionally:
- **Interest on missed PIT-36 zaliczki**: ~500-1,000 PLN
- **Swedish late fees**: up to ~3,750 SEK per year for 2023-2024 if Skatteverket issued returns

---

## PIT-38 Carry-Forward Chain

This is the current calculator output after adding the Celsius/Simplex and Coinbase purchases and replacing the old FTX placeholder with the real FTX ledger:

| Tax Year | PIT-38 Carry-Forward |
| --- | ---: |
| 2022 -> 2023 | 668,757.92 PLN |
| 2023 -> 2024 | 960,686.74 PLN |
| 2024 -> 2025 | 663,243.77 PLN |
| 2025 -> 2026 | 589,298.07 PLN |

This chain only stays coherent if the filings are submitted in order:

1. **PIT-38 korekta for 2023**
2. **PIT-38 korekta / zalegle zeznanie for 2024**
3. **PIT-38 for 2025**

If 2023 is not corrected first, the 2024 prior-year cost field will not match the 2023 carry-forward. If 2024 is not filed before 2025, the 2025 prior-year cost field will not match the 2024 carry-forward.

---

## Documents To File By April 30, 2026

### 1. PIT-38 korekta for 2023 -- file first

| PIT-38 Field | Amount (PLN) |
| --- | ---: |
| Poz. 34 -- Revenue | 411,143.91 |
| Poz. 35 -- Costs incurred in 2023 | 703,072.73 |
| Poz. 36 -- Costs from prior years | 668,757.92 |
| Poz. 37 -- Income | 0.00 |
| Poz. 38 -- Carry-forward to 2024 | 960,686.74 |
| **Tax due** | **0 PLN** |

Source: `outputs/pit38_report_2023.md`

### 2. PIT-38 for 2024 -- file second

Use **korekta** if e-Urząd shows an auto-accepted zero PIT-38 for 2024. Use **zalegle zeznanie** if no 2024 PIT-38 exists in the system.

| PIT-38 Field | Amount (PLN) |
| --- | ---: |
| Poz. 34 -- Revenue | 785,508.57 |
| Poz. 35 -- Costs incurred in 2024 | 488,065.61 |
| Poz. 36 -- Costs from prior years | 960,686.74 |
| Poz. 37 -- Income | 0.00 |
| Poz. 38 -- Carry-forward to 2025 | 663,243.77 |
| **Tax due** | **0 PLN** |

Source: `outputs/pit38_report_2024.md`

### 3. PIT-38 for 2025 -- file third

| PIT-38 Field | Amount (PLN) |
| --- | ---: |
| Poz. 36 -- Revenue | 271,316.95 |
| Poz. 37 -- Costs incurred in 2025 | 197,371.25 |
| Poz. 38 -- Costs from prior years | 663,243.77 |
| Poz. 39 -- Income | 0.00 |
| Poz. 40 -- Carry-forward to 2026 | 589,298.07 |
| **Tax due** | **0 PLN** |

Source: `outputs/pit38_report_2025.md`

### 4. PIT-36 for 2025 (pre-JDG USDC salary)

| Item | Amount |
| --- | ---: |
| Gross income | 162,735.75 PLN |
| Cost deduction (20%) | -32,547.15 PLN |
| Taxable income | 130,188.60 PLN |
| Kwota wolna | -30,000.00 PLN |
| Tax base | 100,189.00 PLN |
| **Tax due** | **14,060 PLN** |

Should include **PIT/ZG** annex for foreign-source income from the US payer.

Source: `outputs/pit36_report_2025.md`

### 5. PIT-28 for 2025 (JDG ryczalt)

| Item | Amount |
| --- | ---: |
| Total revenue | 267,794.30 PLN |
| Tax before health deduction | 32,135 PLN |
| Health insurance deduction (50%) | -2,923.84 PLN |
| **Tax due** | **29,211 PLN** |
| Monthly payments already made | 32,288.14 PLN |
| **Expected overpayment / refund** | **-3,077.14 PLN** |

Source: `outputs/pit28_report_2025.md`

---

## Cash Needed

| Item | Amount |
| --- | ---: |
| PIT-36 tax due | 14,060 PLN |
| PIT-28 refund | -3,077 PLN |
| PIT-38 tax due (2023-2025 combined) | 0 PLN |
| **Net new tax to pay** | **~10,983 PLN** |
| PIT-36 late-interest estimate | ~500-1,000 PLN |
| **Total with interest** | **~11,500-12,000 PLN** |

---

## Recommended Filing Sequence

1. **PIT-38 korekta 2023**
2. **PIT-38 2024** (korekta if auto-accepted, otherwise first filing)
3. **PIT-38 2025**
4. **PIT-36 2025**
5. **PIT-28 2025**

PIT-36 and PIT-28 are operationally independent of PIT-38, but the three PIT-38 forms should be filed as one chain in the order above.

For exact PIT-38 entry steps, see `docs/todo/pit38-filing-guide.md`.

---

## Already Filed / Known Issues

| Year | Form | Current Status | Problem |
| --- | --- | --- | --- |
| 2023 | PIT-37 | Filed late with czynny zal | Wrong form; should be PIT-36 + PIT/ZG |
| 2023 | PIT-38 | Filed, but with old carry-forward | Needs korekta to 960,686.74 PLN |
| 2024 | PIT-37 | Filed by tax company | Wrong form; should be PIT-36 + PIT/ZG |
| 2024 | PIT-38 | No manual filing yet | Check e-Urząd for zero auto-acceptance before choosing korekta vs first filing |
| 2025 | PIT-36 / PIT-38 / PIT-28 | Not yet filed | Must file by April 30, 2026 |

---

## Lower-Priority Corrections After April 30

| Action | Expected Tax Impact |
| --- | ---: |
| Correct 2023 PIT-37 -> PIT-36 + PIT/ZG | 0 PLN expected |
| Correct 2024 PIT-37 -> PIT-36 + PIT/ZG | 0 PLN expected |
| File Swedish self-corrections for 2023-2024 | 0 SEK tax, possible late fees |
| Verify pending Fantom salary transactions | Documentation / evidence only |
