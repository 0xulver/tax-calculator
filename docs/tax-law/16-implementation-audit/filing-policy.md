# Filing Policy: Pre-Residency Crypto Cost Pool

Status: working internal filing policy as of 2026-04-16.

Purpose: translate the topic 16 audit into an actionable PIT-38 position for the Sweden -> Poland move.

## Bottom Line

The default filing position should be:

- keep documented **pre-residency fiat-to-crypto purchases**
- keep **post-residency crypto remuneration** that Poland taxed on receipt
- keep taxable trade/disposal fees
- exclude **pre-residency salary / compensation paid in USDC**
- exclude deposit-only cost creation and funding / withdrawal fees

That means the current repo result should be treated as an **aggressive** PIT-38 position, not the default one, because it still includes the pre-residency salary-USDC bucket.

## Why This Split

The narrow statutory anchor is still Article 22(14) PIT: costs of virtual-currency disposal are documented expenses directly incurred to acquire the virtual currency, plus disposal-related costs. Article 22(15)-(16) then lets excess costs roll forward to the next year.

The official MF crypto guidance uses the same narrow framing:

- acquisition cost is tied to **incurring expenditure**
- crypto-to-crypto is not taxable
- costs not directly related to acquisition / disposal should not be recognized

That framework clearly fits:

- fiat purchases on exchanges / card processors
- sale-related exchange fees
- Polish-taxed post-residency crypto remuneration, where Poland already recognized the receipt value on the income side and later basis prevents double taxation

It does **not** clearly fit pre-residency salary paid in USDC. That bucket is factually provable, but the hard part is the legal bridge: Poland did not tax the receipt when it happened, so the basis-creation step is much less explicit than for post-residency crypto remuneration.

## Filing Buckets

### 1. Keep In Default PIT-38

- Documented pre-residency fiat purchases from Coinbase / Celsius-Simplex / FTX / exchange spot buys, if they were not already consumed or deducted abroad.
- Post-residency USDC remuneration that Poland taxed on receipt and that later entered PIT-38 only on disposal.
- Taxable trade fees on buy / sell rows and direct disposal-side exchange costs.

### 2. Exclude From Default PIT-38

- Pre-residency salary or other compensation paid in USDC.
- Stablecoin deposits treated as if the deposit itself creates PIT-38 cost.
- Funding fees, withdrawal fees, and similar non-disposal transfer costs.
- Any manual proxy row that cannot be backed by primary evidence if challenged.

### 3. Aggressive / Optional Bucket

- Pre-residency salary / compensation paid in USDC can only sit here.
- Use it only if you intentionally choose an aggressive position and ideally after obtaining an individual interpretation.
- Keep it separated from the default pool in workpapers; do not let the calculator merge it silently into the default filing result.

## What This Means Numerically

Current repo position, which still keeps the pre-residency salary-USDC bucket:

- 2025 prior-year PIT-38 costs: `663,243.77 PLN`
- 2025 carry-forward to 2026: `589,298.07 PLN`
- 2025 PIT-38 tax due: `0.00 PLN`

Safe-default recalculation, keeping documented pre-residency fiat purchases but excluding the pre-residency salary files:

- 2025 prior-year PIT-38 costs: `104,877.64 PLN`
- 2025 carry-forward to 2026: `30,931.94 PLN`
- 2025 PIT-38 tax due: `0.00 PLN`

Difference:

- 2025 carry-forward decreases by `558,366.13 PLN`

Gross excluded salary-cost rows currently feeding the pool:

- `503,901.67 PLN` from 2022 salary rows
- `183,681.60 PLN` from Jan-Mar 2023 salary rows before the `2023-04-12` move
- gross total excluded bucket: `687,583.27 PLN`

That gross number is larger than the 2025 carry-forward delta because `129,217.14 PLN` of that bucket was already absorbed by 2022-2023 disposal revenue before reaching the 2025 carry-forward.

## Safe-Default PIT-38 Chain

If the default filing position excludes pre-residency salary-USDC but keeps documented pre-residency fiat purchases, the PIT-38 chain becomes:

### 2023

- `Poz. 34`: `411,143.91 PLN`
- `Poz. 35`: `519,391.13 PLN`
- `Poz. 36`: `294,073.39 PLN`
- `Poz. 37`: `0.00 PLN`
- `Poz. 38`: `402,320.61 PLN`

### 2024

- `Poz. 34`: `785,508.57 PLN`
- `Poz. 35`: `488,065.61 PLN`
- `Poz. 36`: `402,320.61 PLN`
- `Poz. 37`: `0.00 PLN`
- `Poz. 38`: `104,877.64 PLN`

### 2025

- `Poz. 36`: `271,316.95 PLN`
- `Poz. 37`: `197,371.25 PLN`
- `Poz. 38`: `104,877.64 PLN`
- `Poz. 39`: `0.00 PLN`
- `Poz. 40`: `30,931.94 PLN`

## Practical Filing Recommendation

If filing now without an individual interpretation:

1. Treat the **safe-default** PIT-38 result as the baseline filing position.
2. Keep a separate workpaper for the excluded pre-residency salary-USDC bucket and its evidence package.
3. If you want to preserve the larger pool, do that only as a conscious aggressive position, not by default.
4. If the larger pool matters materially, submit an individual interpretation request focused specifically on the pre-residency salary-USDC facts.

## What Does Not Change

This policy changes the PIT-38 opening pool only.

It does **not** itself change:

- post-residency USDC treatment on PIT-36 / later PIT-38
- JDG PIT-28 classification
- the separate need to re-check PIT-28 revenue timing and health-insurance deduction logic
- the separate open question around PIT/ZG

## Source Anchors

- Official MF crypto guidance: https://www.podatki.gov.pl/podatki-osobiste/pit/informacje-podstawowe/co-jest-opodatkowane/zbycie-kryptowalut/
- PIT Act consolidated text dated 2025-02-10, especially Art. 22 ust. 14-16: https://isap.sejm.gov.pl/isap.nsf/download.xsp/WDU20250000163/T/D20250163L.pdf
- KIS interpretation on imported pre-residency purchase costs, `0113-KDIPT2-3.4011.205.2025.2.NM`: https://www.inforlex.pl/dok/tresc%2CFOB0000000000006932617%2CInterpretacja-indywidualna-z-dnia-30-kwietnia-2025-r-Dyrektor-Krajowej-Informacji-Skarbowej-sygn-0113-KDIPT2-3-4011-205-2025-2-NM.html
- KIS interpretation on crypto remuneration basis, `0115-KDIT1.4011.22.2025.1.MR`: https://www.inforlex.pl/dok/tresc%2CFOB0000000000006885875%2CInterpretacja-indywidualna-z-dnia-4-marca-2025-r-Dyrektor-Krajowej-Informacji-Skarbowej-sygn-0115-KDIT1-4011-22-2025-1-MR.html
