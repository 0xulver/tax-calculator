# ZUS + ryczałt — June 2026 payment run

**Prepared:** 2026-06-17
**Płatnik:** Magnus Brantheim, AGENTIC DEFI, NIP 7011256557
**ZUS składkowy account:** `11 6000 0002 0260 0170 1125 6557`
**Scheme in 2026:** ryczałt od przychodów ewidencjonowanych (12%); ZUS *preferencyjne
składki* (kod 05 70, base = 30% of min wage); chorobowe NOT paid; no Fundusz Pracy.

This note covers two separate things that both must be paid around the **22 June 2026**
deadline (20 June is a Saturday → rolls to Mon 22 June):

1. The **May 2026** monthly obligations (income tax + ZUS) triggered by invoice `2026-005`.
2. A **769,43 zł health-insurance arrears** that surfaced from the **2025 annual health
   reconciliation** — unrelated to May, but due now.

---

## TL;DR — what to pay

| # | What | Amount | To | Deadline |
| --- | --- | ---: | --- | --- |
| 1 | 2025 health arrears + interest | **827,43 zł** | ZUS acct …1125 6557 | pay today (17 Jun) |
| 2 | May 2026 ZUS (społeczne 420,86 + zdrowotna 830,58) | **1 251,44 zł** | ZUS acct …1125 6557 | 22 Jun |
| 3 | May 2026 ryczałt income tax | **10 466 zł** | tax mikrorachunek (different acct) | 22 Jun |

ZUS allocates payments **oldest-debt-first**, so clearing the 827,43 arrears first means
the 1 251,44 actually lands on May (instead of being eaten by the old debt).

---

## Part 1 — May 2026 obligations (invoice 2026-005)

### Revenue recognition

- Invoice `2026-005`, issued **05-05-2026**, work period Apr 2026, **20 500 EUR**
  (10 000 EUR for 20 days + 10 500 EUR contract-signing bonus, NovaFusion SA).
- This repo / prior filings recognise ryczałt revenue on **invoice issue date**, so 005 is
  **May 2026** revenue (invoice `2026-006`, issued 07-06, is June). Confirmed against the
  April DRA cumulative figure (see Evidence) — invoices 001–004 only.
- **Paid in USDC, not EUR** (see Part 3). This does NOT change the revenue figure: the
  invoice is denominated in EUR, so revenue = EUR amount × NBP EUR mid-rate.

### Income tax — ryczałt 12%

| Item | Value |
| --- | ---: |
| Revenue 20 500 EUR × NBP EUR **4,2544** (04-05-2026) | **87 215,20 PLN** |
| × 12% | 10 465,82 |
| **Ryczałt to pay (rounded to whole zł)** | **10 466 PLN** |

Computed on **gross** revenue, matching 2025 monthly practice (the 50% health deduction is
trued up in the annual PIT-28; that produced the 504,14 PLN refund for 2025). Optionally the
monthly base can be reduced by społeczne paid (420,86) + 50% of health (415,29) →
86 379,05 × 12% = **10 365 PLN**; either reconciles in the annual return. Pay to the **tax
mikrorachunek**, symbol **PPR**.

### ZUS — May 2026

| Component | Base | Amount |
| --- | ---: | ---: |
| Emerytalne 19,52% | 1 441,80 | 281,44 |
| Rentowe 8,00% | 1 441,80 | 115,34 |
| Wypadkowe 1,67% | 1 441,80 | 24,08 |
| Chorobowe (opted out) | — | 0,00 |
| **Społeczne subtotal** | | **420,86** |
| Zdrowotna 9% | 9 228,64 | **830,58** |
| **ZUS total** | | **1 251,44 PLN** |

Health stays in the **middle bracket** (60k–300k): cumulative 2026 revenue through May =
165 531,50 (April DRA) + 87 215,20 = **252 746,70 PLN** (< 300 000).

> **Watch ahead:** at ~42k zł/month you cross **300 000 zł** cumulative around **Jul–Aug
> 2026**; above it the health base jumps to 180% of avg wage → **~1 495 zł/month**.

### How to fill the May DRA

Identical to April except two fields (PUE auto-fills the rest from kod 05 70):

- Section XI **field 13** (Suma przychodów w bieżącym roku): **252 746,70**
- Section XI **field 16** podstawa zdrowotna **9 228,64**, **field 17** składka **830,58**
- Section X: kod **0570 00**; podst. emer./rent. **1 441,80**; chorobowe **0,00**;
  wypadkowe **1 441,80**; zdrowotna **9 228,64**
- Section IX.02 (do zapłaty): **1 251,44**

---

## Part 2 — the 769,43 zł health arrears (2025 annual reconciliation)

### What ZUS shows

Health-insurance account (UZ) is in arrears by **769,43 zł**; social (FUS) is fully paid.
The arrears is two periods:

| Period | Owed (UZ) | What it is |
| --- | ---: | --- |
| **04.2025** | 461,66 zł | April 2025 monthly health — never paid |
| **04.2026** | 307,77 zł | Extra top-up from the *revised* 2025 annual reconciliation |
| **Total** | **769,43 zł** | + 58,00 zł interest = **827,43 zł** |

### Why it is owed (and why it is correct)

How ryczałt health works: monthly health is **provisional**, charged at whichever revenue
bracket your running yearly total has reached. After year-end you **reconcile** the whole
year at the bracket your *final* annual revenue lands in, applied to every insured month;
shortfall = top-up.

2025 brackets (avg wage **8 549,18**): low 60% → base 5 129,51 → **461,66/mo**;
middle 100% → base 8 549,18 → **769,43/mo**. 2025 annual revenue **267 794,30** → middle.

What happened to this account:

1. April 2026 DRA did the 2025 reconciliation over **8 months** (May–Dec) → annual składka
   6 155,41, top-up **307,74**, which was **paid** inside the 1 559,18 on 18-05-2026.
2. The reconciliation was then **revised to 9 months** — **April 2025 added** as the first
   insured month (kod **05 40 = ulga na start**, health-only). That:
   - made **April 2025's own 461,66** due (it had never been paid), and
   - raised the annual top-up to **615,51**; minus the 307,74 already paid leaves the extra
     **307,77** booked to 04.2026.
   - Revised annual: base 76 942,62 (= 8 549,18 × 9), składka 6 924,84, sum-of-monthly
     6 309,33, top-up 615,51.

**Why April 2025 is genuinely owed even though the company was registered 18-04-2025:**

- The health contribution is **monthly and indivisible** (*miesięczna i niepodzielna*) —
  it is **never prorated** for a partial first month. Registering on the 18th still owes the
  **full** April health.
- **Ulga na start** (first 6 months) waives **social only — NOT health**. So health was due
  every month from April 2025; it simply was not paid (the start-relief made it feel like
  "no ZUS," but only the social half was free). Kod 05 40 on the April 2025 record confirms
  the health-only status.

Conclusion: legitimate, no relief available. Pay it.

### Interest

ZUS "Oblicz odsetki" (paid 17-06-2026): arrears 769,43 + interest **58,00** = **827,43 PLN**.
Interest rounds to whole złoty and grows ~0,30/day, so paying today vs. on the 22nd does not
change the 827,43 figure.

---

## Part 3 — payment was in USDC (stablecoin), not EUR

- Settled on-chain in **USDC** on **12 May 2026**: 23 894 USDC + a 1 USDC test transfer.
  - Payment tx: `0xd9d573c4732e5788c0103fff7694e81b157ab64ff27d9d8f1bd6a89e655aa3e6`
  - Test tx: `0x9a3d40e6327c1b9812836207bc6032992a88d5cb139aa477fe104a41c3cf0353`
  - Wallet on invoice: `0x798a76F27EbaE7a375491077c2f430A7211406a3`
- **Service revenue stays EUR-based** (invoice is in EUR) → 87 215,20 PLN, as in Part 1.
  USDC is *waluta wirtualna*, not *waluta obca*, so it is not the conversion basis.
- **No immediate crypto tax**: receiving USDC for a service is *acquiring* virtual currency,
  not disposing of it — the 19% VC regime (art. 17 PIT) triggers only on later disposal.
- **Future PIT-38 (waluty wirtualne)** consequence when the USDC is converted/spent. Cleanest
  cost basis = the revenue already taxed, **87 215,20 PLN**. For reference, 23 894 USDC at the
  NBP USD rate on 11-05-2026 (3,6007) ≈ 86 035 PLN. Keep the tx hashes as settlement evidence.
  Cost-basis treatment of crypto-received-for-services is contested — confirm with accountant.

---

## Evidence / data sources

All figures above trace to:

**ZUS PUE / eZUS front-end** (pulled 2026-06-17 via an authenticated browser session on the
Płatnik profile; screenshots saved in `evidence/2026-06-17/`):

- *Dashboard* (`/ezus/obszar-platnika/platnik/dashboard`): "Do zapłaty **−769,43 zł**" as of
  16.06.2026; account `11 6000 0002 0260 0170 1125 6557`.
  → `evidence/2026-06-17/01-dashboard-saldo-769.43.png`
- *Składki i salda → Saldo bieżące* (16.06.2026): Ogółem −769,43; FUS **0,00**; UZ **−769,43**;
  FP/FS/FGŚP 0,00; Odsetki za zwłokę **−58,00**.
  → `evidence/2026-06-17/02-saldo-biezace-UZ-breakdown.png`
- *Składki i salda → Należne składki i wpłaty*: period **04.2026 = 307,77**,
  **04.2025 = 461,66** (sum 769,43); Wpłaty: **1 559,18 on 18-05-2026**.
  → `evidence/2026-06-17/03-nalezne-skladki-04.2025-04.2026.png`
- *Oblicz odsetki* (data zapłaty 17-06-2026): arrears 769,43 + odsetki 58,00 = **827,43**.
  → `evidence/2026-06-17/04-oblicz-odsetki-827.43.png`

**ZUS DRA 01 04/2026** (paper, `docs/zus/dra/Deklaracja rozliczeniowa ZUS DRA 01 04-2026.pdf`,
filed 18-05-2026):

- Społeczne 420,86 (emer 281,44 / rent 115,34 / chor 0,00 / wyp 24,08); zdrowotna do
  przekazania **1 138,32** (= 830,58 May-bracket monthly + 307,74 annual top-up).
- Cumulative revenue (box XI.13) **165 531,50**; podstawa zdrowotna 9 228,64; kod **0570**.
- Block XII (2025 annual reconciliation, original): revenue 267 794,30; base 68 393,44;
  roczna składka 6 155,41; sum monthly 5 847,67; dopłata **307,74**.

**ZUS "Raport synchronizacji kartotek" popup** (records as of 9 June 2026 ODP sync):

- `2025-04 Ryczałt … 5129,51 461,66 DRA 0540` → April 2025 health-only (ulga na start), 461,66.
- `2026-04 Ryczałt 165531,50 9228,64 830,58 DRA 0570`.
- Annual recon (revised): `267794,30 / 76942,62 / 6924,84 / 6309,33 / **615,51**`.

**NBP table A mid-rates** (verified against `api.nbp.pl`):

- EUR 04-05-2026 = **4,2544** (table 084/A/NBP/2026) → revenue conversion.
- USD 11-05-2026 = **3,6007** → USDC value context only.

**Invoice:** `docs/invoices/2026/2026-005_novafusion_work-2026-04_20500eur-incl-bonus.pdf`.

### Reference constants (2026)

- Min wage 4 806 → preferential base 30% = **1 441,80**; społeczne **420,86/mo**.
- Avg wage 9 228,64 → health: 60% bracket 498,35 · 100% bracket **830,58** · 180% bracket
  1 495,04. Thresholds 60 000 / 300 000 zł cumulative annual revenue.

---

## Open items

- [x] **Paid 2026-06-17** (receipts in `docs/payments/2026/`):
      arrears **827,43** (`...zus_health-arrears-2025...`), May ZUS **1 251,44**
      (`...zus_skladki-2026-05...`), ryczałt **10 466** (`...us_ryczalt-pit28-2026-05...`).
- [x] **Filed May 2026 DRA** 2026-06-17 22:22 (status OK, UPO issued);
      PDF in `docs/zus/dra/2026/`.
- [ ] Track USDC cost basis (87 215,20 PLN) for future PIT-38 when converted.
- [ ] Confirm with accountant: (a) monthly społeczne/health deduction choice for the
      advance; (b) crypto-received-for-services cost basis.
