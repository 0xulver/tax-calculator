# PIT-36 Personal Income Report -- 2025

Generated: 2026-04-13 22:58
Income type: **Personal services (Art. 13 pkt 8 ustawy o PIT)**
Source: USDC salary payments on Polygon blockchain (pre-JDG)

## Tax Calculation Summary

| Item | Amount |
| --- | ---: |
| Total USDC received | 40,500.00 USDC |
| **Gross income (przychod)** | **162,735.75 PLN** |
| Cost deduction 20% (koszty uzyskania) | -32,547.15 PLN |
| **Taxable income (dochod)** | **130,188.60 PLN** |
| Kwota wolna (tax-free amount) | -30,000.00 PLN |
| **Tax base (podstawa obliczenia)** | **100,189.00 PLN** |
| Tax rate | 12% (up to 120K) / 32% (above 120K) |
| **Tax due (podatek nalezny)** | **14,060.00 PLN** |

## Tax Calculation Detail

- First 90,000.00 PLN at 12% = 10,800.00 PLN
- Remaining 10,189.00 PLN at 32% = 3,260.48 PLN
- Total: **14,060.00 PLN**

> **Note**: JDG ryczalt income (PIT-28) is completely separate from PIT-36.
> The two tax systems do not interact. JDG income does NOT push this
> income into a higher bracket. (Art. 9 ust. 1a, Art. 30c ustawy o PIT)

---

## Payment Details

| # | Date | USDC Amount | NBP USD/PLN Rate | PLN Value | Polygon Tx |
| ---: | --- | ---: | ---: | ---: | --- |
| 1 | 2025-01-02 | 6,000.00 | 4.1012 | 24,607.20 | 0xdd817a48c3a14a... |
| 2 | 2025-01-15 | 6,000.00 | 4.1658 | 24,994.80 | 0x70015236c27b42... |
| 3 | 2025-02-04 | 6,000.00 | 4.1352 | 24,811.20 | 0x6c77c0d2753738... |
| 4 | 2025-02-17 | 6,000.00 | 3.9720 | 23,832.00 | 0x5142a10fd1b00b... |
| 5 | 2025-03-03 | 6,000.00 | 3.9993 | 23,995.80 | 0xb429bb41e87d57... |
| 6 | 2025-03-17 | 6,000.00 | 3.8509 | 23,105.40 | 0xf44ddccd34127b... |
| 7 | 2025-04-01 | 4,500.00 | 3.8643 | 17,389.35 | 0x91327e5e3da784... |
| | **TOTAL** | **40,500.00** | | **162,735.75** | |

## Verification

- Sum of payments = gross income: 162,735.75 = 162,735.75 -- YES
- Gross income x 20% = cost deduction: 162,735.75 x 0.20 = 32,547.15
- Gross - costs = taxable: 162,735.75 - 32,547.15 = 130,188.60
- Taxable - kwota wolna = tax base: 130,188.60 - 30,000.00 = 100,189.00

Each payment's PLN value = USDC amount x NBP USD mid-rate from last business day before payment date.
Verify any rate at: `https://api.nbp.pl/api/exchangerates/rates/a/USD/{RATE_DATE}/?format=json`

---

## Monthly Advance Payments (Zaliczki)

Under Art. 44 ust. 1a, income from a foreign payer requires self-paid monthly advances by the 20th of the following month.

| Month | Income (PLN) | Cumulative Income | Advance Due (PLN) | Due Date |
| --- | ---: | ---: | ---: | --- |
| 2025-01 | 49,602.00 | 49,602.00 | 1,162.00 | 2025-02-20 |
| 2025-02 | 48,643.20 | 98,245.20 | 4,670.00 | 2025-03-20 |
| 2025-03 | 47,101.20 | 145,346.40 | 4,521.00 | 2025-04-20 |
| 2025-04 | 17,389.35 | 162,735.75 | 3,707.00 | 2025-05-20 |
| **TOTAL** | | | **14,060.00** | |

**If advances were not paid monthly, interest accrues from each due date at ~14.5% annual rate.**

---

## Cross-Reference: PIT-38 Cost Basis

The same 162,735.75 PLN appears as **cost basis** on PIT-38
(salary USDC acquisition costs). This is the barter doctrine: income taxed at
receipt becomes the cost basis for later crypto disposal. When USDC is sold for
EUR, the PIT-38 gain/loss is only the difference between the sale PLN value and
this 162,735.75 PLN cost basis -- typically near zero.
