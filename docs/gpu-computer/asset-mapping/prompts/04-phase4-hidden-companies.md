# Phase 4 — Hidden Companies and Beneficial Ownership

Goal: detect any limited-liability company (sp. z o.o.), partnership (sp.k., spółka jawna), or other registered entity where the debtor is a shareholder, board member, proxy, or beneficial owner. JDG owners under financial pressure commonly park valuable assets behind nominee-fronted corporate vehicles.

**Time:** 30–60 minutes of agent runtime.
**Cost:** 0 PLN for free queries; rejestr.io may have paid tiers — skip those.

---

````
```prompt-for-browser-agent
You are searching Polish corporate registers for any company where a JDG debtor appears as a shareholder, officer, proxy, or beneficial owner. Open-data, free-tier only.

=== SUBJECT ===
Full name: Mateusz Szklarski-Łopata
Trading as: GPUcomputer (JDG, NIP 8661681248, REGON 362678345)

Search both surname variants:
- Szklarski
- Szklarski-Łopata

=== TASK 1 — KRS (KRAJOWY REJESTR SĄDOWY) — PERSON-BASED SEARCH ===

Goal: find any registered company where the debtor holds any role.

1. Open https://wyszukiwarka-krs.ms.gov.pl
   (Alternative entry: https://prs.ms.gov.pl/krs/strona-glowna and navigate to KRS search)
2. Look for a search mode toggle between "Podmioty" (Entities) and "Osoby" (Persons) — or a separate person-search tab labeled "Wyszukiwanie osób" (Person search) or "Osoba fizyczna" (Natural person).
3. Run two separate searches:
   - Imię (First name): Mateusz / Nazwisko (Surname): Szklarski
   - Imię: Mateusz / Nazwisko: Szklarski-Łopata
4. For each company returned, extract:
   - Company name (Firma / Nazwa)
   - KRS number
   - NIP of the company
   - REGON of the company
   - Role of Mateusz Szklarski in the company (zarząd = management board, wspólnik = partner/shareholder, prokurent = proxy, likwidator = liquidator)
   - Date of entry into role
   - Date of exit (if shown)
   - Company status (aktywny / w likwidacji / wykreślony — active / in liquidation / struck off)
5. For each company found, click through to the company entry and extract:
   - Registered address
   - Share capital (Kapitał zakładowy)
   - Co-shareholders / co-directors
   - Any insolvency notation
   - Any encumbrances
6. If the person-search mode does not exist or returns "no results" for either variant, record exactly what was attempted.

Return Task 1 as JSON with one entry per company.

=== TASK 2 — REJESTR.IO CROSS-REFERENCE ===

Goal: catch person-company links that the official KRS person search may miss. Free tier only — do not pay.

1. Open https://rejestr.io
2. In the search bar, type: Mateusz Szklarski — press Enter.
3. Look at the results. If a filter exists to show "Osoby" (Persons) vs "Podmioty" (Entities), use it.
4. For each person match shown, click through and note the companies/entities they are linked to.
5. Also search:
   - Mateusz Szklarski-Łopata
   - 8661681248 (the NIP)
   - GPUcomputer
6. For each entity result extract:
   - Entity name
   - KRS number
   - NIP
   - Role of Mateusz Szklarski (if shown)
   - Dates
   - Status
7. If full person-company links require paid subscription, record the price and stop the paid step — capture what's free.

Return Task 2 as JSON.

=== TASK 3 — CRBR (CENTRAL REGISTER OF BENEFICIAL OWNERS) ===

Goal: catch beneficial ownership in companies where Szklarski may not be the formally listed director but is the real owner.

1. Open https://crbr.podatki.gov.pl/adcrbr/#/
   (Alternative: https://crbr.podatki.gov.pl/)
2. Find the public search section, typically labeled "Wyszukaj" (Search) or "Rejestr CRBR".
3. If the portal accepts a beneficial-owner name search, enter:
   - Imię (First name): Mateusz
   - Nazwisko (Last name): Szklarski
   - Also try: Szklarski-Łopata
4. Many CRBR person searches require date of birth or PESEL. If those fields are mandatory and you do not have them, record "Person search requires PESEL/DOB — cannot proceed without identifiers" and try the NIP search instead.
5. For each linked company, the entry will show:
   - Company name
   - Company NIP / KRS
   - Beneficial owner(s) — beneficjenci rzeczywiści
   - Role / control basis
   - Ownership percentage
   - Date of entry / update
6. Also try entering the JDG NIP 8661681248 to see if it cross-references any company.

Return Task 3 as JSON.

=== TASK 4 — KRS OFFICIAL VERIFICATION OF FOUND ENTITIES ===

Goal: confirm any companies found in Tasks 1–3 via the official KRS entity record.

1. For each entity found, open https://prs.ms.gov.pl/krs and search by KRS number (preferred) or NIP.
2. Open the entity. Download or view:
   - "Odpis aktualny" (Current extract)
   - "Odpis pełny" (Full extract), if available without payment
3. Confirm:
   - Status
   - Registered address
   - Management board members
   - Shareholders/partners
   - Proxies (prokurenci)
   - Any insolvency / liquidation entries
   - Specifically: confirm Mateusz Szklarski appears in the role claimed by the earlier source

Return Task 4 as JSON, one entry per verified company.

=== TASK 5 — eZAMÓWIENIA + ONEPLACE (PUBLIC PROCUREMENT TRACES) ===

Goal: detect whether GPUcomputer (or any linked entity) has supplied to public institutions. Procurement records expose declared bank accounts and operational addresses.

1. Open https://ezamowienia.gov.pl/mp-client/search/list
2. Run searches:
   - GPUcomputer
   - gpucomputer.pl
   - 8661681248 (the NIP)
   - Mateusz Szklarski
3. For each result, extract: contracting authority, contract title, date, value, awarded contractor name and address, any bank account number in the award documentation.

4. Also open the direct OnePlace marketplace profile (known to exist for this debtor):
   https://oneplace.marketplanet.pl/baza-firm/-/bc/company/61989/mateusz-szklarski-gpucomputer
   Extract: full company data, declared address, contact info, any associated tender history, declared bank accounts.

Return Task 5 as JSON.

=== TASK 6 — VIES (EU CROSS-BORDER VAT VERIFICATION) ===

Goal: detect whether the debtor is authorized for intra-community supply within the EU. Given the debtor's claimed Hong Kong supplier relationship, cross-border financial infrastructure is plausible — VIES registration would confirm the EU side of that and signals foreign banking infrastructure that OGNIVO cannot reach.

1. Open https://ec.europa.eu/taxation_customs/vies/#/vat-validation
2. In the "Member State" dropdown, select "PL (Poland)".
3. In the "VAT Number" field, enter: 8661681248
4. Click "Verify".
5. Record the status:
   - "Yes, valid VAT number" → debtor is authorized for intra-EU transactions; investigate further whether they have used this for foreign banking
   - "No, invalid VAT number" → no EU intra-community authorization

Return Task 6 as JSON: { "vies_status": "...", "implications_for_cross_border_recovery": "..." }

=== OVERALL OUTPUT ===

Combined JSON with keys "task_1_krs_person_search", "task_2_rejestr_io", "task_3_crbr", "task_4_krs_entity_verification", "task_5_ezamowienia_oneplace", "task_6_vies", plus a top-level "summary_english" of 3-5 sentences identifying:
- Any companies the debtor holds a role in
- **PHOENIX MANEUVER RED FLAG**: specifically flag any newly-formed sp. z o.o. (established late 2025 or 2026) operating at a different address with identical or related PKD codes (26.20.Z = computer production, 46.51.Z = wholesale computer trade). This pattern is the classic asset-shielding move where a JDG owner drains capital into a new liability-shielded vehicle.
- Whether any of those companies are themselves in insolvency
- Whether VIES suggests cross-border banking exposure

=== FAILURE HANDLING ===

- CAPTCHA: stop the affected step, flag, continue.
- Login wall (KRS PRS may require account for full extract): use free preview and note what's gated.
- CRBR person search requires PESEL/DOB: skip person search, do NIP cross-search only.
- Paid tier on rejestr.io: capture free preview, do not pay.

=== STOP CONDITION ===

All six tasks attempted. Return consolidated JSON.
```
````
