# Synthesis: Late Filing and Corrections for PIT-38 in Poland

Sources: ChatGPT 5.4 Pro, ChatGPT Deep Research, Perplexity, Gemini 3.1 Deep Research

---

## Broad Consensus (All 4 agree on core mechanics)

### You CAN still file — no hard cutoff
A PIT-38 can be filed at any time up to the statute of limitations (5 years from end of year the tax was due). There is no mechanism that bars late filing.

### First filing vs korekta — check Twoj e-PIT first
- If **no PIT-38 exists** for that year → filing now is a **late first-time filing** (not a korekta)
- If a PIT-38 was **auto-accepted** by Twoj e-PIT (system auto-accepts zero returns after April 30) → your filing is a **korekta** (correction of the auto-accepted one)

**Critical action**: Log into e-Urzad Skarbowy and check "Zlozone dokumenty" to see if auto-accepted PIT-38s exist for 2023 and 2024. This determines which legal track you're on.

### Czynny zal (Art. 16 KKS) provides immunity from penal-fiscal punishment
- An **effective** czynny zal means the perpetrator is **not punishable** for the disclosed offense
- It does NOT eliminate the tax or interest — only the criminal/fine exposure
- Must be filed **before** the authority has documented knowledge or started detection activities
- Can be filed electronically via e-Urzad Skarbowy
- Must disclose: what was omitted, tax years, circumstances, whether anyone else was involved
- Tax + interest must be paid in full

### Art. 16a KKS (correction safe harbor) is the alternative for korekta scenarios
If you're correcting an existing return (not filing for the first time), Art. 16a provides no-punishment protection when a legally effective correction is filed + tax is paid promptly. Some practitioners file czynny zal alongside korekta anyway for maximum protection.

### Interest runs from day after original deadline
- 2023 PIT-38: interest from **May 1, 2024**
- 2024 PIT-38: interest from **May 1, 2025**
- Current rate: **10.50% per year** (as of March 5, 2026)
- Rate has changed multiple times — must calculate per-subperiod using historical rates
- Reduced 50% rate is **NOT available** (requires correction within 6 months of deadline — window has passed)
- Self-calculate and pay without waiting for a demand from the office
- Use MF interest calculator at podatki-arch.mf.gov.pl

### Statute of limitations

| Tax Year | Payment Deadline | Statute Expires |
|---|---|---|
| 2023 | April 30, 2024 | December 31, 2029 |
| 2024 | April 30, 2025 | December 31, 2030 |

Both years are well within the window. Note: opening penal-fiscal proceedings can **suspend** the limitation period.

### PIT-38 is independent from PIT-36/PIT-37
Filing or correcting PIT-38 does not affect PIT-36/PIT-37 (they're separate returns). If PIT-36/37 also needs correction, file separate korekty for those.

### No limit on number of corrections
You can file as many corrections as needed until the statute expires. Each correction supersedes the prior one.

### Everything can be done electronically
- PIT-38: via Twoj e-PIT or e-Deklaracje
- Czynny zal: via e-Urzad Skarbowy ("Zawiadomienie o popelnieniu czynu zabronionego")
- Payment: to mikrorachunek podatkowy (generate at podatki.gov.pl/generator-mikrorachunkow)
- Installment request (RAT-ZW): via e-Urzad Skarbowy

### Do NOT contact the tax office informally before filing
All sources agree: visiting or calling the tax office before submitting the formal czynny zal could give them "documented knowledge" of the offense, which makes czynny zal ineffective. File first, talk later.

---

## Where Sources Disagree

### 1. Whether the 2023 and 2024 PIT-38 amounts actually owe tax

This is the most consequential disagreement — and it stems from different assumptions about the underlying numbers:

| Source | Assumption | Tax due for 2023 | Tax due for 2024 |
|---|---|---|---|
| ChatGPT 5.4 Pro | Uses cost pool analysis — salary costs exceed revenue | **0 PLN** | **0 PLN** |
| ChatGPT Deep Research | Similar analysis, notes cost pool approach | **Likely 0 PLN** | **Likely 0 PLN** |
| Perplexity | Assumes 146K PLN net gain from FIFO analysis → 19% tax | **~27,740 PLN** | **~570 PLN** |
| Gemini | Same FIFO assumption as Perplexity | **~27,740 PLN** | **~570 PLN** |

**Assessment**: Perplexity and Gemini are using the FIFO-based calculator numbers (146K and 3K gains), which we now know are incorrect for Polish PIT-38. Under the correct cost pool method, costs exceed revenue every year → 0 tax. However, this depends on whether the salary USDC is accepted as a deductible cost on PIT-38 (the barter doctrine from synthesis 02). If it is (which KIS interpretations support), then no tax is owed. If it isn't, the numbers could be different.

**This is the single most important question for late filing**: if 0 tax is owed, then czynny zal is simpler (no payment required), interest is 0, and the penal exposure is about the administrative failure to file, not about unpaid tax.

### 2. Penalty classification for 2023

| Source | 2023 classification | Reasoning |
|---|---|---|
| ChatGPT 5.4 Pro | Above the misdemeanor threshold → fiscal crime territory | ~27K PLN tax > 5x minimum wage |
| Perplexity | Przestepstwo skarbowe (fiscal crime) | Same reasoning |
| Gemini | Przestepstwo skarbowe (fiscal crime) | Same reasoning |
| ChatGPT Deep Research | Notes the threshold is "non-trivial" | Same direction |

All agree IF 27K PLN tax is owed, 2023 is above the fiscal crime threshold. But if tax is 0 (cost pool), the offense is only the administrative failure to file — which is a much less serious matter.

### 3. The installment + czynny zal tension

Gemini uniquely identifies a dangerous interaction: if you file czynny zal + RAT-ZW (installment request) simultaneously, and the installment request is denied, the czynny zal becomes void because the payment condition (Art. 16 §2) wasn't met. The other sources mention installments as an option but don't flag this trap as strongly.

**Takeaway**: If you need installments, pay everything you can first to satisfy the czynny zal condition, then request installments for the remainder.

### 4. The auto-acceptance question

Perplexity and Gemini flag that Twoj e-PIT **auto-accepts** PIT-38 returns (with zeros) if the taxpayer doesn't act by April 30. This means your "missing" PIT-38 might actually already exist as a zero-value auto-accepted return — making your filing a **korekta** rather than a first-time late filing. ChatGPT 5.4 Pro and Deep Research mention this possibility but less prominently.

**This matters because**: korekta is covered by Art. 16a (correction safe harbor), which may be simpler than Art. 16 czynny zal. Both are protective, but they're different legal mechanisms.

---

## Estimated Financial Exposure

### If tax owed = 0 PLN (cost pool approach, our analysis)

| Item | Amount |
|---|---|
| Tax due | 0 PLN |
| Interest | 0 PLN |
| Fines (with czynny zal) | 0 PLN |
| **Total** | **0 PLN** (just need to file the forms) |

The only obligation is the administrative filing itself + czynny zal for the late filing offense.

### If tax owed = ~28K PLN (Perplexity/Gemini FIFO assumption)

| Item | Amount |
|---|---|
| 2023 tax | ~27,740 PLN |
| 2023 interest (to Mar 2026) | ~7,000 PLN |
| 2024 tax | ~570 PLN |
| 2024 interest | ~61 PLN |
| Fines (with czynny zal) | 0 PLN |
| **Total** | **~35,371 PLN** |

---

## Interest Rate History (for calculations)

| Period | Annual Rate |
|---|---|
| Before May 8, 2025 | 14.50% |
| May 8 - Jul 2, 2025 | 13.50% |
| Jul 3 - Sep 3, 2025 | 13.00% |
| Sep 4 - Oct 8, 2025 | 12.50% |
| Oct 9 - Nov 5, 2025 | 12.00% |
| Nov 6 - Dec 3, 2025 | 11.50% |
| Dec 4, 2025 - Mar 4, 2026 | 11.00% |
| **Mar 5, 2026 onwards** | **10.50%** |

---

## Action Items (in order of execution)

### Step 1: Check e-Urzad Skarbowy (TODAY)
Log in and check "Zlozone dokumenty" for 2023 and 2024. Did Twoj e-PIT auto-accept PIT-38 returns? This determines first-filing vs korekta.

### Step 2: Determine actual tax owed
Using the cost pool calculator + salary USDC costs, compute the actual PIT-38 figures. If costs > revenue (which our calculator shows), tax = 0 for both years. Confirm this before filing.

### Step 3: Prepare PIT-38 for 2023 and 2024
- Use correct form version for each year
- Include all crypto disposal revenue AND all acquisition costs (including salary USDC)
- Include carry-forward from prior years
- If auto-accepted zero returns exist: mark as korekta

### Step 4: Prepare czynny zal
- Art. 16 KKS for first-time late filings
- Art. 16a KKS if correcting auto-accepted returns (file czynny zal anyway for safety)
- Template provided by ChatGPT 5.4 Pro (included above)
- File from your own e-Urzad account (not via advisor's account)

### Step 5: Pay tax + interest (if any) to mikrorachunek
- If tax = 0: no payment needed, but still file the returns + czynny zal
- If tax > 0: pay same day as filing, use MF calculator for exact interest
- Do NOT request installments unless absolutely necessary (conflicts with czynny zal)

### Step 6: File everything on the same day
- Pay first (if any tax due)
- File PIT-38 corrections via Twoj e-PIT
- File czynny zal via e-Urzad Skarbowy general correspondence
- Save all UPO (confirmation receipts)

### Step 7: Do this BEFORE April 30, 2026
The 2024 PIT-38 carry-forward feeds into the 2025 PIT-38 filing. Get the corrections done before the 2025 filing deadline.

---

## Czynny Zal Template (from ChatGPT 5.4 Pro)

```
[City], [Date]

Naczelnik [competent Urzad Skarbowy]
[address]

[Full name]
[address]
PESEL: [PESEL]

ZAWIADOMIENIE O POPELNIENIU CZYNU ZABRONIONEGO
(czynny zal - art. 16 Kodeksu karnego skarbowego)

Dzialajac na podstawie art. 16 § 1 Kodeksu karnego skarbowego,
zawiadamiam o popelnieniu czynu zabronionego polegajacego na
niezlozeniu w terminie zeznan PIT-38 za:
- 2023 r. (termin zlozenia: 30.04.2024 r.),
- 2024 r. (termin zlozenia: 30.04.2025 r.),

do ktorych bylem zobowiazany w zwiazku z przychodami/kosztami
z odplatnego zbycia walut wirtualnych.

Przyczyna uchybienia bylo [brief truthful explanation, e.g.:
bledne rozumienie obowiazkow po zmianie rezydencji podatkowej
ze Szwecji / niepelna ewidencja transakcji / poleganie na
zewnetrznej firmie podatkowej ktora nie zlozyla PIT-38].

Obecnie samodzielnie ujawniam to uchybienie, zanim - wedlug
mojej wiedzy - organ powzial o nim wyraznie udokumentowana
wiadomosc lub rozpoczal czynnosci zmierzajace do ujawnienia
tego czynu.

Istotne okolicznosci:
1. PIT-38 za 2023 r. nie zostal zlozony w terminie.
2. PIT-38 za 2024 r. nie zostal zlozony w terminie.
3. Zalegle zeznania PIT-38 skladam rownoczesnie z niniejszym
   zawiadomieniem.
4. [If tax due: Zalegly podatek wraz z nalezymi odsetkami
   zostal zaplacony na mikrorachunek podatkowy.]
   [If no tax due: Z zeznan nie wynika zaleglosc podatkowa.]

W popelnieniu czynu nie wspoldzialaly inne osoby.

Wnosze o uznanie niniejszego zawiadomienia za skuteczne
w rozumieniu art. 16 KKS.

Zalaczniki:
- PIT-38 za 2023 r.
- PIT-38 za 2024 r.
- [Payment confirmation if applicable]

[Signature]
```
