# Phase 2 — Real Estate Discovery

Goal: find any land or property owned by the debtor. Real estate is the most durable asset class — it cannot be moved or hidden quickly, and a *hipoteka przymusowa* (forced mortgage) obtained later still works on it. Finding any KW number changes the Path A vs Path B math significantly.

**Time:** 30–90 minutes of agent runtime.
**Cost:** Free for Tasks 1–3. Task 4 (commercial report) is optional and costs ~30–100 PLN.

The bottleneck: the official land register (EKW) requires a KW number, but the central portal has no name-based search. Tasks 1–4 are different routes to obtaining a KW number. Task 5 then queries the KW once known.

---

````
```prompt-for-browser-agent
You are investigating real estate possibly owned by a Polish JDG debtor. The central land register (EKW) requires a known KW number — there is no name-based search. Your job is to obtain a KW number from any of the alternate sources in Tasks 1–4, then look it up in Task 5.

=== SUBJECT ===
Full name: Mateusz Szklarski-Łopata
Trading as: GPUcomputer / MATEUSZ SZKLARSKI GPUCOMPUTER
NIP: 8661681248
REGON: 362678345
Registered address: ul. Mogilska 16 lok. 7, 31-516 Kraków (virtual office operated by WorkDesk — building NOT owned by debtor)
Known historical address (from older business directories): ul. Kazimierza Wielkiego 36 lok. 3, 30-074 Kraków — check both as a property and as a potential residence/workshop

If Phase 5 surfaces additional addresses, search those too.

=== TASK 0 — NAME-BASED LAND REGISTER SEARCH (ksiegiwieczyste.pl person search) ===

Goal: this is the only known name-based public search for KW numbers, scraping commercial datasets. If this works, the entire Phase 2 bottleneck disappears.

1. Open https://ksiegiwieczyste.pl/szukaj-po-imieniu-i-nazwisku
2. The form asks for personal details. Fill in:
   - "Nazwisko" (Last name): Szklarski
   - "Imię" (First name): Mateusz
   - "Miejscowość" (City/Town): Kraków
3. Click "Szukaj" (Search) or equivalent button.
4. Wait for results. The page may obscure KW numbers behind a paywall (e.g. shows "KR1P/000…XXX") with a payment prompt for full disclosure.
5. Extract:
   - Number of matches found
   - Any partially-visible KW numbers
   - Listed cities for each match
   - URL of any payment/unlock page
6. DO NOT pay automatically. If a partial KW appears for free, capture it; if a paywall blocks the full number, record the price and stop.
7. Repeat the search with surname variant: Szklarski-Łopata
8. Try the same search on https://www.wieczyste.pl if it has a person-search mode.

Return Task 0 as JSON:
{
  "name_search_matches": ...,
  "partial_kw_numbers": [...],
  "cities_listed": [...],
  "payment_url": "...",
  "payment_amount_PLN": ...
}

FAILURE HANDLING:
- If CAPTCHA appears, stop and report "CAPTCHA blocking — needs human".
- If the page structure has changed and the fields are not visible, stop and report "UI changed, fields not found".

=== TASK 1 — MSIP KRAKÓW (KRAKÓW CITY SPATIAL INFORMATION SYSTEM) ===

Goal: find KW number for any parcel in Kraków linked to the debtor's address, and use the map's name-search if available.

1. Open https://msip.krakow.pl
2. Look for a map composition labeled "Mapa dla architektów i planistów" (Map for architects and planners) or "Przestrzeń miejska i planowanie" (Urban space and planning). Click it.
3. If a notice appears with text "Zapoznałem się z treścią informacji" (I have read the information), tick the checkbox and click "OK".
4. In the search/address bar within the map, type: Mogilska 16 Kraków — press Enter.
5. The map zooms in. Click on the parcel/building at that address.
   ALSO REPEAT for: Kazimierza Wielkiego 36 Kraków (the older historical address)
6. A pop-up panel appears — extract:
   - "Numer działki" (Plot number)
   - "Obręb" (Cadastral precinct)
   - "Identyfikator działki" (Plot identifier, format powiat.gmina.obręb.nr)
   - Any visible KW number
   - "Struktura własności" (Ownership structure) if shown
   - Building tenancy notes if shown
7. Look for a sidebar layer panel or search widget labeled "Wyszukiwanie" (Search) or "Właściciel" (Owner). If a name-based owner search exists, enter: Szklarski. If no such field is visible without login, skip.
8. If a "Zaloguj się" (Log in) or "Utwórz konto" (Create account) wall appears for any layer, do NOT register — record "Login wall — needs human" and continue.
9. If additional debtor addresses from Phase 5 are available, repeat steps 4–7 for each.

Return Task 1 as JSON:
{
  "mogilska_16_parcel_id": "...",
  "mogilska_16_kw_number": "...",
  "mogilska_16_ownership_note": "...",
  "name_search_results": [{"owner": "...", "address": "...", "parcel_id": "...", "kw_number": "..."}],
  "login_walls_hit": [...]
}

=== TASK 2 — NATIONAL GEOPORTAL (geoportal.gov.pl) ===

Goal: visual confirmation and parcel ID for any address outside Kraków city limits.

1. Open https://mapy.geoportal.gov.pl/imap/
   (Alternative: https://www.geoportal.gov.pl — click "Uruchom mapę" / Launch map)
2. In the search bar labeled "Wyszukaj adres lub obiekt" (Search for address or object), enter: ul. Mogilska 16, Kraków — press Enter.
3. Click on the parcel that contains the building. A pop-up shows "Informacje o wybranej działce" (Information about the selected plot).
4. Extract: identifier, area in m², precinct, district.
5. The portal does NOT show owner names — this is by design. Do not attempt owner lookup here.
6. Repeat for any additional addresses passed in.

Return Task 2 as JSON with one entry per address.

=== TASK 3 — KSIEGIWIECZYSTE.PL (commercial address → KW lookup) ===

Goal: address-to-KW lookup via a commercial scraped dataset.

1. Open https://ksiegiwieczyste.pl
2. Find the section labeled "Szukaj po adresie" (Search by address).
3. In the form:
   - "Miejscowość" (Locality): begin typing "Krakow" and select Kraków from the dropdown
   - "Ulica" (Street): Mogilska
   - "Numer domu" (Building number): 16
   - "Numer lokalu" (Apartment number): 7
4. Click "Szukaj" (Search).
5. Extract all KW numbers and property descriptions returned.
6. Try also https://www.wieczyste.pl with the same address.
7. If either site requests payment or registration to show the KW number, stop and record what's free vs paid. Do NOT pay automatically. (If a free preview shows a KW number, capture it.)
8. If any other addresses from Phase 5 are available, repeat with each.

Return Task 3 as JSON.

=== TASK 4 — ONGEO.PL (commercial paid fallback — DO NOT PURCHASE UNLESS AUTHORIZED) ===

Goal: paid commercial report that includes KW number and ownership snippet. Only relevant if Tasks 1–3 produced nothing and the user has authorized spending up to ~99 PLN.

1. Open https://ongeo.pl
2. Search for the same addresses checked in Tasks 1–3.
3. For each address, note what report types are offered and their prices (typically 29–99 PLN for "Raport o terenie" / Terrain report).
4. Specifically note which report option includes "Właściciel" (Owner) and "Numer KW" (KW number).
5. Do NOT make a purchase. Report back the cheapest option that would give KW + owner data, and stop.

Return Task 4 as JSON: address-by-address availability and pricing summary.

=== TASK 5 — EKW (ELECTRONIC LAND REGISTER — once a KW number is known) ===

Goal: read the actual register entry to see ownership, mortgages, encumbrances.

If no KW number was obtained from Tasks 1–4, SKIP Task 5 and report "No KW number found; EKW lookup not possible."

If at least one KW number was obtained:

1. Open https://przegladarka-ekw.ms.gov.pl/eukw_prz/KsiegiWieczyste/wyszukiwanieKW
2. The form has three sub-fields for the KW number:
   - "Kod wydziału" (Court division code) — e.g. KR1P
   - "Numer księgi wieczystej" (Land register number) — 8-digit number
   - "Cyfra kontrolna" (Check digit) — single digit
3. Split the KW number you obtained (format: CODE/NUMBER/DIGIT, e.g. KR1P/00123456/7) into the three boxes accordingly.
4. Click "Wyszukaj księgę" (Search register).
5. On the result page, click "Przeglądaj księgę wieczystą" (Browse land register).
6. Walk through these tabs and extract everything visible (translate Polish to English):
   - "Dział I-O" (Section I-O): property description, address, area, parcel numbers
   - "Dział I-Sp" (Section I-Sp): rights associated with the property
   - "Dział II" (Section II): OWNER (właściciel) name(s) and ownership share fractions — CRITICAL.
     **Specifically flag any acquisition basis containing "Umowa Darowizny" (Deed of Donation) to a family member with a recent date** — that's a classic asset-shielding move that triggers a skarga pauliańska (fraudulent transfer challenge) under art. 527 KC.
   - "Dział III" (Section III): encumbrances, third-party rights, notices of proceedings
   - "Dział IV" (Section IV): MORTGAGES (hipoteki) — creditor name, amount, currency, priority date
7. If the page returns "Nie ma takiej księgi wieczystej" (No such land register), record that and try the next KW number if any.
8. Note: the portal is offline Sundays 00:00–09:00 CEST for maintenance.

Return Task 5 as JSON, one entry per KW number:
{
  "kw_number": "...",
  "property_address": "...",
  "property_type": "...",
  "area_sqm": ...,
  "owner_name": "...",
  "owner_share": "...",
  "co_owners": [...],
  "section_III_encumbrances": [...],
  "section_IV_mortgages": [{"creditor": "...", "amount_PLN": ..., "currency": "...", "priority_date": "..."}],
  "retrieved_date": "..."
}

=== OVERALL OUTPUT ===

Return one JSON object with keys "task_1_msip", "task_2_geoportal", "task_3_ksiegiwieczyste", "task_4_ongeo_pricing", "task_5_ekw_results", plus a top-level "summary_english" of 3-5 sentences explaining whether the debtor appears to own any real estate, whether any mortgages already encumber it, and any login walls or paywalls encountered.

=== FAILURE HANDLING ===

- CAPTCHA: stop the affected step, mark "captcha_blocking": true, continue.
- Login wall: record exactly what registration is required, do NOT register.
- Paywall on commercial KW lookups (Task 3, 4): record the free preview if any and stop without paying.
- Portal offline: record timestamp and message.
- If a KW lookup returns owner data that does NOT match Mateusz Szklarski-Łopata, record the actual owner (this still has value — it confirms which addresses are NOT owned by the debtor).

=== STOP CONDITION ===

Return the consolidated JSON once Tasks 1–4 are attempted and Task 5 is run for every KW number found (or skipped with explanation if none were found).
```
````
