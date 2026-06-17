---
name: zus-dra-monthly
description: File the monthly ZUS DRA for the Agentic DeFi JDG (ryczałt, preferential ZUS) in ePłatnik via browser automation, then archive the official PDF. Use when the user wants to "do the DRA", "file ZUS for <month>", submit the monthly social/health declaration, or download a DRA PDF. Covers browser setup, the clone-from-previous flow, the wypadkowe-base and Fundusz-Pracy gotchas, and PDF capture.
---

# Monthly ZUS DRA filing (Agentic DeFi JDG)

Files one monthly ZUS DRA in the legacy **ePłatnik** app and saves the official
4-page PDF to `docs/zus/dra/<year>/`. The płatnik signs with Profil Zaufany — the
agent prepares and verifies everything up to the signature, never signs.

Payer: **Magnus Brantheim / AGENTIC DEFI, NIP 7011256557**, ZUS account
`11 6000 0002 0260 0170 1125 6557`. Scheme: **ryczałt 12%**, **preferential ZUS
(kod 05 70)**, **no chorobowe**, **no Fundusz Pracy**.

> Real official filing. Go step by step, **verify every value with a readable
> screenshot (clip, not full-page)**, and stop at the signature. Two clone
> gotchas WILL bite if skipped — see step 5 (wypadkowe) and step 6 (FP).

## 0. Inputs to gather first

- **This month's invoice(s)** in `docs/invoices/<year>/` → EUR amount + issue date.
- **NBP EUR mid-rate** from the last business day before the invoice issue date
  (revenue recognised on invoice date). Use `src/tax_calc/nbp.py` or
  `api.nbp.pl/api/exchangerates/rates/a/EUR/<date>/?format=json`.
- **Prior cumulative revenue** = box 13 of last month's DRA (in `docs/zus/dra/`).
- **New cumulative revenue** = prior cumulative + (this month's EUR × NBP rate),
  rounded to 2dp. This is the only figure that changes month to month.
- Confirm the **health bracket** of the new cumulative (see Constants). If it
  crosses **300 000 PLN**, the health składka jumps — recompute, don't assume.

## 1. Browser setup (reuse > relaunch > recreate)

```bash
bash .claude/skills/zus-dra-monthly/scripts/setup-browser.sh 9224
```

Chrome blocks remote-debugging on the real Default profile, so we use a dedicated
copy at `~/.chrome-zus-copy` and **reuse it every month** (don't delete/recreate).
First run copies the Default profile (needs your main Chrome closed). ZUS sessions
expire between months, so **you log in via Profil Zaufany each time** — expected.

Helper (use the mise python that has playwright):
```bash
PY=~/.local/share/mise/installs/python/latest/bin/python
ZP=.claude/skills/zus-dra-monthly/scripts/zus.py
$PY $ZP status        # check where the page is
```
Tell the user to log in via Profil Zaufany; wait until `status` shows the
`platnik/dashboard`. Optionally open eZUS **Składki i salda → Saldo** to check
for arrears before filing (see `docs/zus/` notes).

## 2. Open the wizard

eZUS left menu **ePłatnik** → it opens the classic app (`eplMain.npi`). Then:
`Kreatory` → **`Obsługa rozliczenia`** → welcome screen → **Dalej**.

```bash
$PY $ZP click "Kreatory"; $PY $ZP click "Obsługa rozliczenia"; $PY $ZP click "Dalej"
```

## 3. Mode = clone from previous

Step "Wybór trybu obsługi rozliczenia", 3 radios:
0 = nowy komplet, **1 = na podstawie danych z poprzedniego (USE THIS)**, 2 = korekta.
The płatnik always clones from the previous month.
```bash
$PY $ZP radio 1; $PY $ZP click "Dalej"
```

## 4. General options — verify, don't edit

Step "Ogólne opcje deklaracji". The clone auto-fills; confirm with `audit`/`get`:
- Miesiąc / Rok = the month you're filing (auto-incremented).
- "Płatnik opłaca składki wyłącznie za siebie" = checked.
- `deklaracjaDochoduNajnizszejPodstawy` (Mały ZUS Plus) = **unchecked**.
- Wypadkowe rate = **1,67**.
Then **Dalej**.

## 5. Income/health step — update revenue, fix wypadkowe ⚠️

Step "Deklaracja dochodu, formy opodatkowania" (krok 3 z 5).

a. **Update the ryczałt cumulative revenue** (holds last month's value):
```bash
$PY $ZP set "Suma przychodów w bieżącym roku" "252746,70"   # <- new cumulative
```
b. Click **Oblicz** in the ryczałt section, then **OK** on the confirm dialog:
```bash
$PY $ZP click "Oblicz"; $PY $ZP dialog "OK"
```
c. **GOTCHA — wypadkowe base resets to 0,00 (red) on clone.** Fix it to the
   preferential base, then re-audit:
```bash
$PY $ZP set "Podstawa wymiaru składki na ubezpieczenie wypadkowe" "1441,80"
$PY $ZP audit          # expect NO "ERR" lines
$PY $ZP clip /tmp/bases.png 1800 144 712 270   # READ it to verify visually
```
   Expect: emer-rent 1 441,80 · wypadkowe 1 441,80 · chorobowe 0 · zdrowotna
   9 228,64 · revenue = new cumulative · zdrowotna składka 830,58. Then **Dalej**.

## 6. Zestawienie — decline Fundusz Pracy ⚠️

Step "Zestawienie" (krok 4 z 5). A popup asks **"Czy naliczać składkę na Fundusz
Pracy?"** — preferential payers **do NOT pay FP → click Anuluj** (the dialog's,
not the wizard's):
```bash
$PY $ZP dialog "Anuluj"
```
Verify the tabs (clip + read): **Należne składki** → emer 281,44 / rent 115,34 /
chorobowe 0 / wypadkowe 24,08 (social 420,86); **Należne składki cz. II** →
zdrowotna **830,58**, **Fundusz Pracy 0,00**. Total **1 251,44**. Then **Dalej**.

## 7. Verify, send, sign

Step "Utworzenie i walidacja" (krok 5 z 5):
```bash
$PY $ZP click "Weryfikuj"      # status of the ZUS DRA row must become OK
$PY $ZP click "Wyślij i zakończ"
```
A "Autoryzacja usługi biznesowej" dialog offers signature methods. **STOP — hand
to the user**: they click **"Podpis ePUAP..."** (Profil Zaufany), authenticate,
and sign. Success popup: **"Dokumenty zostały wysłane."** (click OK).

## 8. Confirm + archive the PDF

Confirm: `Dokumenty ubezpieczeniowe → Dokumenty wysłane` shows the DRA with
status **OK** and a send timestamp.

Download the official PDF (ePłatnik prints client-side; the real PDF is served at
`downloadFile.npi`):
1. Select the DRA row → **Podgląd** (opens the form viewer iframe).
2. In the form toolbar click **Drukuj** (it's inside frame `dokumentySformalizowane`).
   A "Wydruk dokumentu" viewer loads the PDF from `downloadFile.npi?exportType=preview`.
3. Fetch the bytes through the authenticated session:
```bash
$PY $ZP fetch-pdf "docs/zus/dra/<year>/Deklaracja rozliczeniowa ZUS DRA 01 <MM>-<YYYY>.pdf"
```
Verify: 4 pages A4; page 3 shows the new revenue + 830,58 and a **blank** Section
XII (no annual reconciliation in a normal month). Save under `docs/zus/dra/<year>/`.

## 9. Remind about payment (filing ≠ paying)

DRA filing does not move money. Remind the user to transfer to the ZUS account by
the **20th** (→ next business day if weekend): the month's **1 251,44** plus any
arrears. Income tax (ryczałt) goes to the **mikrorachunek** separately.

---

## Constants (2026 — re-check each January)

| Item | Value |
| --- | ---: |
| Min wage | 4 806 → preferential base 30% = **1 441,80** |
| Social total / month | **420,86** (emer 281,44 · rent 115,34 · wyp 24,08; chorobowe 0) |
| Avg wage (health 100%) | 9 228,64 → middle-bracket składka **830,58** |
| Health 60% bracket (≤60k) | base 5 537,18 → 498,35 |
| Health 180% bracket (>300k) | base 16 611,55 → 1 495,04 |
| Brackets | ≤60 000 · 60 000–300 000 · >300 000 (cumulative yearly revenue) |
| Kod tytułu | 05 70 00 · wypadkowe rate 1,67% · deadline code 6 |

## Dojo/automation gotchas (why the helper exists)

- Buttons: click by **ARIA role / `.dijitButtonText`**, never the off-screen
  `input.dijitOffScreen` (it won't fire the handler).
- Modal **underlays intercept clicks** — use `dialog "LABEL"` for dialog buttons,
  and distinguish the dialog's *Anuluj/OK* from the wizard's.
- `Drukowanie / podgląd` on the list prints the **list**; for the single document
  you must open it (Podgląd) first — its toolbar lives in an **iframe**.
- Full-page screenshots are unreadable (≈5096px) — always **`clip`** the region
  and Read it before trusting/typing a value.
- The form is rendered client-side; `Drukuj` calls `window.print()`. The PDF is
  only retrievable from the **`downloadFile.npi`** frame URL (helper `fetch-pdf`).

## Teardown (optional)

Keep `~/.chrome-zus-copy` for next month. To stop the browser:
`pkill -f 'remote-debugging-port=9224'`. The user's real Chrome is untouched.
