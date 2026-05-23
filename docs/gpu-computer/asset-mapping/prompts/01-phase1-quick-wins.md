# Phase 1 — Quick Wins (VAT whitelist, KRZ, MSiG, CEIDG)

**Run this first.** Free, fast, and one of these results (KRZ bankruptcy entry) can completely change the strategy.

**Time:** 15–30 minutes of agent runtime.
**Cost:** 0 PLN.

Paste the entire block below into your browser agent (Atlas, Comet, Claude in Chrome).

---

````
```prompt-for-browser-agent
You are investigating a Polish JDG sole proprietor on behalf of a creditor with a 155,000 PLN claim. Your job is to extract specific data from four Polish government portals and return everything translated to English. Do NOT register, log in, pay anything, or contact the subject. Open-data lookups only.

=== SUBJECT ===
Full name: Mateusz Szklarski-Łopata
Trading as: GPUcomputer / MATEUSZ SZKLARSKI GPUCOMPUTER
NIP: 8661681248
REGON: 362678345
Registered address: ul. Mogilska 16 lok. 7, 31-516 Kraków
Website: https://www.gpucomputer.pl/

=== TASK 1 — VAT WHITELIST (BIAŁA LISTA PODATNIKÓW VAT) ===

Goal: extract all bank accounts the debtor has declared to the Polish tax office, plus current VAT status.

1. Open https://www.podatki.gov.pl/wykaz-podatnikow-vat-wyszukiwarka
2. The page shows several search modes as tabs or radio buttons. Select the one labeled "NIP".
3. In the NIP field, type exactly: 8661681248
4. There is a date field labeled "Stan na dzień" (Status as of date). Leave it at today's default.
5. Click the button labeled "Szukaj" (Search).
6. The result panel will appear. Extract every field shown, including ALL bank account numbers under "Numery rachunków bankowych" (Bank account numbers). Multiple accounts may be listed.
7. Repeat the search with the date field set to 2026-01-15 (the date closest to when the debt arose). Compare bank account lists — record any accounts that existed in January but have since been removed.
8. If the page returns "Nie figuruje w rejestrze VAT" (Not listed in VAT register) or "Podmiot nie jest zarejestrowany jako podatnik VAT", record exact text and timestamp.
9. CRITICAL: if the status shown is "Wykreślony" (Struck off), flag this as a TERMINAL INDICATOR at the top of the output — it means the tax authority has either detected fraud, recorded continuous nil returns, or the debtor has formally ceased trading. Mark "wykreslony_terminal_indicator": true in the JSON.

Return for Task 1, as JSON with English keys:
{
  "vat_status_today": "...",
  "entity_name_shown": "...",
  "registered_address_shown": "...",
  "bank_accounts_today": ["PL...", "PL..."],
  "bank_accounts_2026_01_15": ["PL...", "PL..."],
  "accounts_closed_since_january": ["PL..."],
  "query_date": "..."
}

=== TASK 2 — KRZ (KRAJOWY REJESTR ZADŁUŻONYCH) — INSOLVENCY REGISTER ===

Goal: confirm whether any bankruptcy, restructuring, or failed-enforcement proceeding has been registered against the debtor. THIS IS THE MOST IMPORTANT SEARCH — if anything is found, stop and report immediately before proceeding to Tasks 3 and 4.

1. Open https://krz.ms.gov.pl
   (If it redirects, follow to https://prs.ms.gov.pl/krz)
2. Find the public search area, typically labeled "Portal Publiczny" (Public Portal), "Wyszukiwarka" (Search engine), or "Tablica obwieszczeń" (Notice board).
3. Run four separate searches, recording results from each:
   - By NIP: 8661681248
   - By REGON: 362678345
   - By name: Mateusz Szklarski
   - By business name: GPUcomputer
4. For each result, extract:
   - Type of proceeding (look for Polish terms: "upadłość" = bankruptcy, "restrukturyzacja" = restructuring, "wniosek o ogłoszenie upadłości" = bankruptcy petition, "umorzenie egzekucji" = discontinued enforcement, "postępowanie sanacyjne" = sanation, "przyspieszone postępowanie układowe" = accelerated arrangement)
   - Case signature (sygnatura akt)
   - Court name
   - Filing date and any later dates
   - Status
   - Trustee or supervisor name if shown
5. If all four searches return "Brak wyników" (No results), record that explicitly with today's date.

CRITICAL: If ANY result appears for ANY of the four search terms, mark the entire Task 2 output with the flag "KRZ_HIT": true at the top of the JSON, and include a one-sentence English summary at the top.

Important caveat to remember when interpreting "No results": under art. 27 Prawa Upadłościowego, a Polish court has up to 2 months from a bankruptcy petition filing to issue a ruling, and the public KRZ entry only appears AFTER the court formally processes the filing. So "no KRZ result" today does NOT prove no petition has been filed — it only proves no petition has been processed and registered yet. Cross-check with Task 3 (MSiG) for any preliminary court announcements that might pre-empt the KRZ entry.

Return for Task 2 as JSON with English keys.

=== TASK 3 — MSiG (MONITOR SĄDOWY I GOSPODARCZY) — OFFICIAL GAZETTE ===

Goal: catch insolvency, restructuring, liquidation, or creditor-call notices, including older entries that may not be in KRZ.

1. Open https://wyszukiwarka-msig.ms.gov.pl
   (Alternative URL if needed: https://emsig.ms.gov.pl/)
2. The form has these field labels (translate as needed):
   - "Nazwa podmiotu" (Entity name)
   - "Numer KRS" (KRS number) — leave blank, the debtor is JDG not KRS
   - "NIP"
   - "Tekst w pozycji" (Text in item)
   - "Tekst w treści" (Text in content)
   - "Typ ogł./sprawy" (Announcement/case type) — leave blank to capture all
3. Run five separate searches:
   - Nazwa podmiotu: Mateusz Szklarski
   - Nazwa podmiotu: GPUcomputer
   - Nazwa podmiotu: MATEUSZ SZKLARSKI GPUCOMPUTER
   - NIP: 8661681248
   - Tekst w treści: Szklarski Mateusz
4. For each result extract: publication date, issue/item number, court, full notice text, notice type. Specifically flag any entry typed as:
   - "Upadłość" (Bankruptcy)
   - "Restrukturyzacja" (Restructuring)
   - "Ogłoszenie upadłości" (Bankruptcy declaration)
   - "Wezwanie wierzycieli" (Creditor call)
   - "Umorzenie postępowania" (Discontinued proceeding)
5. Translate the full notice text of any flagged entry to English.
6. Pagination: if results span multiple pages, walk through all pages.

Return for Task 3 as JSON, grouped by search term. Flag any insolvency hits at the top.

=== TASK 4 — CEIDG VERIFICATION (CURRENT BUSINESS STATUS) ===

Goal: confirm the JDG is still active or learn if it has been suspended/deregistered.

1. Open https://prod.ceidg.gov.pl/ceidg/ceidg.public.ui/Search.aspx
   (If the URL has changed, search for "Wyszukiwarka CEIDG" or open https://www.biznes.gov.pl/ and click the company search link.)
2. In the NIP field, type: 8661681248
3. Click the search button (likely "Szukaj").
4. Open the matching entry.
5. Extract:
   - Full business name
   - Status (look for "Aktywny" = active, "Zawieszony" = suspended, "Wykreślony" = struck off / deleted)
   - Activity start date
   - Latest update date
   - Registered address
   - Correspondence address
   - Additional places of business (if shown)
   - All PKD codes (activity classification)
   - Any insolvency or restructuring annotation
   - Marital property regime note
6. Translate all field labels and status values to English.

Return for Task 4 as JSON.

=== OVERALL OUTPUT ===

Return one JSON object with keys "task_1_vat_whitelist", "task_2_krz", "task_3_msig", "task_4_ceidg", plus a top-level "summary_english" key containing 3-5 sentences in plain English summarizing the most important findings, especially any insolvency signal.

=== FAILURE HANDLING ===

- If CAPTCHA appears anywhere: stop that task, record the URL and step number, mark "captcha_blocking": true, and continue with the next task.
- If a portal is offline (e.g. "Trwa przerwa techniczna" = Technical break): record the message and timestamp; KRZ/EKW maintenance is typically Sunday 00:00–09:00.
- If a portal asks for login or Profil Zaufany: record "Login required" and stop that specific task — do NOT create an account.
- If a search returns no results, record "Brak wyników" verbatim plus the English translation "No results" and continue.
- Do not retry more than once per blocker.

=== STOP CONDITION ===

Return the combined JSON once all four tasks are attempted. If Task 2 (KRZ) yields any hit, return immediately after Task 2 without proceeding to Tasks 3 and 4 — the result needs human review first.
```
````
