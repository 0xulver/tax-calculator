# PIT-38 Filing Guide -- 2023, 2024, 2025

Use this guide when entering the crypto figures into the official PIT-38 forms.

Source of truth:
- `outputs/pit38_report_2023.md`
- `outputs/pit38_report_2024.md`
- `outputs/pit38_report_2025.md`

---

## Before You Start

1. Log into e-Urząd Skarbowy and check `Zlozone dokumenty`.
2. Confirm whether a PIT-38 already exists for 2023 and 2024.
3. Choose filing mode:
   - **2023**: this is a **korekta** of the already-filed PIT-38.
   - **2024**: use **korekta** if a zero PIT-38 was auto-accepted; otherwise use **zalegle zeznanie**.
   - **2025**: this is the normal annual **PIT-38** filing for 2025.
4. File the three years in order: **2023 -> 2024 -> 2025**.

---

## PIT-38 For 2023

Use the PIT-38 form for tax year 2023. In the crypto section (`Waluty wirtualne`, Section E), enter:

| Field | Value |
| --- | ---: |
| Poz. 34 | 411,143.91 |
| Poz. 35 | 702,974.04 |
| Poz. 36 | 643,322.55 |
| Poz. 37 | 0.00 |
| Poz. 38 | 935,152.67 |

Meaning:
- `Poz. 34`: revenue from crypto disposals
- `Poz. 35`: costs incurred in 2023
- `Poz. 36`: costs carried from earlier years
- `Poz. 37`: income
- `Poz. 38`: undeducted costs carried to 2024

Expected outcome: **0 PLN tax due**

---

## PIT-38 For 2024

Use the PIT-38 form for tax year 2024. In the crypto section (`Waluty wirtualne`, Section E), enter:

| Field | Value |
| --- | ---: |
| Poz. 34 | 785,508.57 |
| Poz. 35 | 488,065.61 |
| Poz. 36 | 935,152.67 |
| Poz. 37 | 0.00 |
| Poz. 38 | 637,709.71 |

Meaning:
- `Poz. 36` must match the **2023 carry-forward** above
- `Poz. 38` becomes the prior-year cost figure for 2025

Expected outcome: **0 PLN tax due**

---

## PIT-38 For 2025

Use the PIT-38 form for tax year 2025. In the crypto section (`Waluty wirtualne`, Section E), enter:

| Field | Value |
| --- | ---: |
| Poz. 36 | 271,316.95 |
| Poz. 37 | 197,234.37 |
| Poz. 38 | 637,709.71 |
| Poz. 39 | 0.00 |
| Poz. 40 | 563,627.13 |

Meaning:
- `Poz. 38` must match the **2024 carry-forward** above
- `Poz. 40` is the amount carried into 2026

Expected outcome: **0 PLN tax due**

---

## Quick Cross-Checks

Use these checks before submitting:

| Year | Check |
| --- | --- |
| 2023 | `702,974.04 + 643,322.55 - 411,143.91 = 935,152.67` |
| 2024 | `488,065.61 + 935,152.67 - 785,508.57 = 637,709.71` |
| 2025 | `197,234.37 + 637,709.71 - 271,316.95 = 563,627.13` |

If any carry-forward value does not match the prior year, stop and fix the earlier form first.

---

## Submission Notes

- Save the UPO / confirmation after each submission.
- File all three PIT-38 forms before working on the PIT-36/PIT-28 package.
- The PIT-38 forms in this chain all show **zero tax due**. The non-zero cash payment in this filing season comes from **PIT-36**, partly offset by the **PIT-28** overpayment.
