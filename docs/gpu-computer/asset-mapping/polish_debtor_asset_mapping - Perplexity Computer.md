# Polish JDG Debtor Asset Mapping: Methodology Brief

**Case:** Mateusz Szklarski-Łopata / GPUcomputer (NIP: 8661681248, REGON: 362678345)
**Debt:** 155,000 PLN | **Filed:** EPU Nc-e 552126/26, SR Lublin-Zachód, 8 April 2026
**Prepared for:** English-speaking private creditor executing lookups via agentic browser tools
**As of:** 23 May 2026

---

> **Critical legal notice — read before executing any step**
>
> All methods below are legal under Polish law and EU GDPR/RODO. None authorise deception, unauthorised system access, pretexting (posing as a customer, official, or related party to extract information), or coercive contact. A clear distinction is drawn throughout between **finding** information (lawful OSINT) and **using** it as court evidence (certified copies — *odpisy* — are required). Where a step requires a court order, Profil Zaufany authentication, bailiff (*komornik*) standing, or a signed power of attorney (*pełnomocnictwo*), the step is routed to the creditor personally, their Polish lawyer, or a paid intermediary — no browser-agent prompt is issued for it.
>
> **OGNIVO / zlecenie poszukiwania majątku:** These bank-network search mechanisms require a *tytuł wykonawczy* (enforcement title — i.e., a court judgment with a *klauzula wykonalności* enforcement clause). The creditor does not yet have one. Both tools are documented under Section D and Section K (post-judgment escalation) but are **not** OSINT alternatives at the current procedural stage.

---

## Known identifiers (carry into every prompt)

| Field | Value |
|---|---|
| Full legal trading name | Mateusz Szklarski-Łopata Gpucomputer |
| NIP | 8661681248 |
| REGON | 362678345 |
| Registered address | ul. Mogilska 16/7, 31-516 Kraków (virtual office) |
| Website | https://www.gpucomputer.pl |
| Phone (mobile) | 883 109 779 |
| Phone (landline) | 12 333 77 30 |
| Email (owner) | mateusz@gpucomputer.pl |
| Activity start | 2015-10-06 |
| PKD (primary) | 26.20.Z – Produkcja komputerów i urządzeń peryferyjnych |
| EPU case | Nc-e 552126/26, SR Lublin-Zachód |

---

## Section A — Real Estate Ownership

### A-1. Electronic Land Register Browser (ekw.ms.gov.pl)

**Ranking: #1 highest signal-per-złoty for real estate**

| Field | Detail |
|---|---|
| **Source URL** | https://przegladarka-ekw.ms.gov.pl/ |
| **Legal access** | Open — no login required to browse a known KW number |
| **Cost (PLN)** | Free to browse; 20 PLN per certified electronic extract (*odpis*) |
| **Accuracy / freshness** | Legally authoritative; updated within hours of court registry entries |
| **Time to obtain** | Instant (browsing); 1–3 days (certified PDF via ekw.ms.gov.pl order form) |
| **Caveats** | **Critical bottleneck:** the portal requires the *numer księgi wieczystej* (KW number — format XXYYY/NNNNNNN/N). There is no name-based or NIP-based search on this portal. The KW number must be obtained via one of the workarounds in A-2 through A-5 before this source is useful. System is offline every Sunday 00:00–09:00. |
| **Skip-if** | No KW number available and workarounds (A-2, A-4, A-5) return nothing. |

**BROWSER-AGENT CANNOT EXECUTE A-1 WITHOUT A KW NUMBER FROM A-2 / A-4. See those entries first.**

Once a KW number is obtained, use this prompt:

```prompt-for-browser-agent
TASK: Retrieve land register entry for a known KW number.

TARGET URL: https://przegladarka-ekw.ms.gov.pl/

INPUTS:
- KW number: [insert KW number obtained from A-2 or A-4]

STEPS:
1. Navigate to https://przegladarka-ekw.ms.gov.pl/
2. Locate the field labelled "Numer Księgi Wieczystej" (Land Register Number).
   The field has three sub-boxes: court code (e.g., KR1P), slash, sequential number, slash, check digit.
3. Enter the KW number in the three boxes.
4. Click the button labelled "Wyszukaj Księgę" (Search Register).
5. On the results page, click "Przeglądaj Księgę Wieczystą" (Browse Land Register).
6. Navigate through four sections/tabs:
   - "Dział I-O" (Section I-O): property description — address, area, parcel numbers.
   - "Dział I-Sp" (Section I-Sp): rights associated with the property.
   - "Dział II" (Section II): ownership — extract full name(s) of owner(s), share fractions, acquisition basis.
   - "Dział III" (Section III): encumbrances (rights of third parties, notices of proceedings).
   - "Dział IV" (Section IV): mortgages — creditor name, amount, currency, priority date.

EXTRACTION FORMAT (return as JSON, all values translated to English):
{
  "kw_number": "...",
  "property_address": "...",
  "property_type": "...",
  "area_sqm": ...,
  "owner_name": "...",
  "owner_share": "...",
  "co_owners": [...],
  "encumbrances_section_III": [...],
  "mortgages_section_IV": [{"creditor": "...", "amount_PLN": ..., "date": "..."}],
  "retrieved_date": "..."
}

FAILURE HANDLING:
- If the KW number is invalid → "KW number not found — re-check the source (A-2/A-4) for correct format."
- If the page shows "Trwa przerwa techniczna" (Technical break) → record timestamp and retry after 09:00 on the same day (Sunday maintenance window).
- If no data visible under any tab → check "Dział I-O" for note "Księga zamknięta" (closed register — property no longer exists or was merged).

STOP CONDITION: Extract all four sections. Stop after JSON is complete. Do not proceed further on this site.
```

---

### A-2. MSIP Kraków (Miejski System Informacji Przestrzennej)

**Ranking: #2 — yields KW number for Kraków parcels by address**

| Field | Detail |
|---|---|
| **Source URL** | https://msip.krakow.pl |
| **Legal access** | Open (free account registration required for data download; map browsing is public) |
| **Cost (PLN)** | Free |
| **Accuracy / freshness** | Based on municipal cadaster; updated periodically, not real-time. Ownership layer may lag behind EKW by weeks. |
| **Time to obtain** | Minutes (map viewing); up to 24 hours for email link to downloaded dataset |
| **Caveats** | MSIP shows parcels in Kraków city limits only. The registered address (Mogilska 16/7) is a virtual office — the debtor's personal property (if any) could be at a different address in Kraków or elsewhere. The "Struktura własności" (ownership structure) WMS layer is available but may require free account creation. UI labels are in Polish only. **Uncertainty (2026):** the login flow and composition name labels may have changed in recent MSIP redesigns — browser agent must handle login-wall gracefully. |
| **Skip-if** | Debtor has no property within Kraków city limits (likely if he lives elsewhere). |

```prompt-for-browser-agent
TASK: Find parcel and KW number data for a person at a known Kraków address, then expand to search for property registered under owner name.

TARGET URL: https://msip.krakow.pl

INPUTS:
- Known address: ul. Mogilska 16, Kraków (virtual office — expected to yield no personal ownership)
- Search names: "Szklarski" / "Mateusz Szklarski"

STEPS:
1. Navigate to https://msip.krakow.pl
2. Look for a map composition labelled "Przestrzeń miejska i planowanie" (Urban space and planning) or "Mapa dla architektów i planistów" (Map for architects and planners). Click it.
3. If a dialog appears with text "Zapoznałem się z treścią informacji" (I have read the information), tick the checkbox and click "OK".
4. In the map interface, find the search/address bar. Type "Mogilska 16, Kraków" and press Enter.
5. The map will pan to the address. Click on the parcel shown at that address.
6. Note any parcel ID (numer działki) and any KW number shown in the pop-up panel.
7. **Second attempt — name search:** Look for a layer panel or search widget labelled "Wyszukiwanie" (Search) or "Właściciel" (Owner). If a name-based owner search field exists, enter "Szklarski" and search.
8. If a login dialog appears labelled "Zaloguj się" (Log in) or "Utwórz konto" (Create account), do NOT proceed — mark this step as "Login wall encountered — route to user for account registration."

EXTRACTION FORMAT (return as JSON):
{
  "parcel_id_mogilska16": "...",
  "kw_number_mogilska16": "...",
  "owner_mogilska16": "...",
  "name_search_results": [{"owner_name": "...", "address": "...", "parcel_id": "...", "kw_number": "..."}],
  "login_wall_hit": true/false,
  "note": "..."
}

FAILURE HANDLING:
- If page does not load → "MSIP portal unavailable — retry later or proceed to A-4 (geoportal.gov.pl)."
- If no name-search functionality found → note "Name search not available in MSIP without account" and stop.
- If CAPTCHA appears → route step to user.

STOP CONDITION: Obtain at least one KW number or confirm that no parcel is found. Then stop.
```

---

### A-3. Geoportal.gov.pl / EGiB National Cadaster

**Ranking: #3 — national coverage, no name search available to public**

| Field | Detail |
|---|---|
| **Source URL** | https://www.geoportal.gov.pl |
| **Legal access** | Open for map viewing; name-based owner data requires formal wniosek to starostwo (district geodesy office) |
| **Cost (PLN)** | Free map viewing; formal data request: ~30–150 PLN depending on starostwo fees |
| **Accuracy / freshness** | Cadaster data updated by local starostwa; generally reflects current ownership within 1–3 months |
| **Time to obtain** | Map viewing: instant; formal wniosek: 7–30 days |
| **Caveats** | The public geoportal shows **parcel boundaries and identifiers** but does NOT display owner names to the public. Owner data from EGiB requires a formal *wniosek o udostępnienie danych z operatu ewidencyjnego* submitted to the starostwo właściwe (competent district office). GDPR/RODO applies — the requester must cite a legitimate legal interest (being a creditor with a pending court case is typically sufficient). |
| **Skip-if** | Skip as OSINT; useful only as a complement to MSIP (A-2) for visually identifying parcels before filing formal request. |

```prompt-for-browser-agent
TASK: Use the national geoportal to visually locate cadastral parcels at the debtor's registered address and note parcel IDs for use in a formal EGiB data request.

TARGET URL: https://www.geoportal.gov.pl

STEPS:
1. Navigate to https://www.geoportal.gov.pl
2. Click "Uruchom mapę" (Launch map) or the main map viewer link.
3. In the search bar (labelled "Wyszukaj adres lub obiekt" — Search for address or object), type "Mogilska 16, Kraków" and press Enter.
4. The map will zoom to the address. Note the parcel boundaries visible.
5. Click on the parcel at the address. A pop-up panel should show:
   - "Identyfikator działki" (parcel identifier) in format: powiat.gmina.obręb.nr
   - "Obręb" (district/precinct name)
   - Area in m²
6. Repeat for any additional address associated with the debtor (if known).
7. Do NOT attempt to look up owner name — this is not publicly available here.

EXTRACTION FORMAT (return as JSON):
{
  "address_searched": "Mogilska 16, Kraków",
  "parcel_identifier": "...",
  "obreb": "...",
  "area_sqm": ...,
  "note": "Owner name not publicly available via geoportal — use for parcel ID only"
}

FAILURE HANDLING:
- If search returns no results → try "ul. Mogilska 16 Kraków" without abbreviation.
- If map does not load → "Geoportal unavailable — retry later."

STOP CONDITION: Obtain parcel identifier(s). Stop — do not attempt owner lookup on this site.
```

---

### A-4. ongeo.pl (Commercial Cadaster Reports)

**Ranking: #4 — yields KW number and ownership snippet by address, paid**

| Field | Detail |
|---|---|
| **Source URL** | https://ongeo.pl |
| **Legal access** | Open (commercial service, account required for purchase) |
| **Cost (PLN)** | ~29–99 PLN per "Raport o Terenie" (terrain report) depending on depth |
| **Accuracy / freshness** | Pulls from EGiB and EKW; typically 1–7 days lag |
| **Time to obtain** | Minutes after purchase |
| **Caveats** | Only useful if the debtor's real property address is known. The Mogilska 16 address is a virtual office (co-working building) — a report there will show the building owner, not the debtor. Must search by any residential address discovered in Section C. Also try geo-system.com.pl as an alternative. |
| **Skip-if** | No personal residential address identified for the debtor. |

```prompt-for-browser-agent
TASK: Generate an ongeo.pl terrain report for a parcel at a known address to obtain the KW number and ownership snippet.

TARGET URL: https://ongeo.pl

INPUTS:
- Address to check: [INSERT residential address discovered in Section C — NOT Mogilska 16]

PRE-CONDITION: This prompt requires a Visa/Mastercard for payment (~29–99 PLN). Route to creditor for payment. Once creditor confirms payment capability, proceed.

STEPS:
1. Navigate to https://ongeo.pl
2. In the main search bar, type the residential address of the debtor (obtained from Section C) and select the matching suggestion.
3. The site will show a parcel highlighted on the map. Confirm it matches the expected address.
4. Click "Generuj raport" (Generate report) or "Zamów raport" (Order report).
5. Select the report type that includes "Właściciel" (Owner) and "Numer KW" (Land Register number) — typically the "Raport pełny" (Full report) option.
6. Proceed through payment. Enter creditor's card details when prompted.
7. Download the PDF report once generated (usually within 2–5 minutes).

EXTRACTION FORMAT (return as JSON):
{
  "address": "...",
  "parcel_id": "...",
  "kw_number": "...",
  "registered_owner": "...",
  "mortgage_indicator": true/false,
  "report_date": "..."
}

FAILURE HANDLING:
- If the parcel shows a different owner → note "Property not owned by debtor at this address."
- If paywall blocks content → "Payment required — route to creditor."
- If address not found → try geo-system.com.pl as alternative.

STOP CONDITION: KW number extracted or "no ownership match" confirmed. Stop.
```

---

### A-5. Formal wniosek to Starostwo Geodezji (EGiB owner lookup)

**Ranking: #5 — definitive but slow**

| Field | Detail |
|---|---|
| **Source URL** | Starostwo Powiatu Krakowskiego or właściwe starostwo for any other address |
| **Legal access** | Restricted-with-request — requires formal written application citing legal basis (art. 24 ust. 5 ustawy Prawo geodezyjne i kartograficzne) |
| **Cost (PLN)** | ~30–150 PLN per request (varies by starostwo) |
| **Accuracy / freshness** | Authoritative; reflects current EGiB as of request date |
| **Time to obtain** | 14–30 days |
| **Caveats** | The creditor must demonstrate "uzasadniony interes prawny" (justified legal interest) — a pending court case (EPU reference) satisfies this. For Kraków city, the competent office is Wydział Geodezji UMK, ul. Grunwaldzka 8, 31-526 Kraków. |
| **Skip-if** | Skip if A-2 or A-4 already yield a KW number. |

**BROWSER-AGENT CANNOT EXECUTE THIS STEP.** Route to creditor or Polish lawyer to file wniosek via ePUAP or in person.

---

### A-6. Formal wniosek o odpis z KW (certified extract once KW is known)

| Field | Detail |
|---|---|
| **Source URL** | https://ekw.ms.gov.pl (order form) |
| **Legal access** | Open — no special standing required |
| **Cost (PLN)** | 20 PLN per odpis zwykły (basic extract); 30 PLN per odpis pełny (full history) |
| **Accuracy / freshness** | Legally binding, issued as of date of order |
| **Time to obtain** | 1–3 business days (electronic PDF) |
| **Caveats** | Requires KW number. This produces the certified document needed for court proceedings, unlike the free browser view (A-1). |
| **Skip-if** | Not needed unless court evidence is required (i.e., once litigation strategy is confirmed). |

**Browser agent can assist with the order form on ekw.ms.gov.pl once a KW number is known — route to A-1 prompt first.**

---

## Section B — Vehicle Ownership

### B-1. historiapojazdu.gov.pl (UFG Vehicle History — VIN/plate lookup)

**Ranking: #1 — free, public, no login; reveals insurance history and inspection dates**

| Field | Detail |
|---|---|
| **Source URL** | https://historiapojazdu.gov.pl |
| **Legal access** | Open — no login required |
| **Cost (PLN)** | Free |
| **Accuracy / freshness** | UFG (Insurance Guarantee Fund) data; near-real-time for insurance events; inspection data from CEPiK |
| **Time to obtain** | Immediate |
| **Caveats** | Requires registration plate number OR VIN. Does NOT disclose current registered owner name — shows vehicle history events only (inspection dates, insurance periods, odometer, accident history). Useful for confirming a vehicle exists and is currently insured. Owner name requires CEPiK formal request (B-3). |
| **Skip-if** | No plate number or VIN known. |

```prompt-for-browser-agent
TASK: Search vehicle history for any vehicle associated with the debtor's business (GPUcomputer).

TARGET URL: https://historiapojazdu.gov.pl

PRE-CONDITION: This search requires a registration plate number or VIN. Collect these from:
- Google Maps Street View for Mogilska 16 Kraków (look for vehicles parked on-site bearing any signage).
- OLX / OtoMoto listings (see B-2) for any vehicles the debtor has advertised.
If no plate/VIN available, skip to B-2 first.

INPUTS (once obtained):
- Registration plate: [from B-2 or physical observation]
- VIN: [if available]
- First registration date: [if known — required only for some lookups]

STEPS:
1. Navigate to https://historiapojazdu.gov.pl
2. Find the input fields:
   - "Numer rejestracyjny" (Registration number)
   - "Numer VIN" (VIN number)
   - "Data pierwszej rejestracji" (First registration date — format RRRR-MM-DD)
3. Enter the values and click "Sprawdź pojazd" (Check vehicle).
4. The report will display:
   - Vehicle make, model, year
   - Insurance history (periods, gaps indicating possible uninsured period)
   - Technical inspection (przegląd techniczny) history
   - Odometer readings
   - Accident/theft flags

EXTRACTION FORMAT (return as JSON):
{
  "plate": "...",
  "vin": "...",
  "make_model": "...",
  "year": ...,
  "insurance_valid_to": "...",
  "last_inspection_date": "...",
  "odometer_last_km": ...,
  "accident_flag": true/false,
  "note": "..."
}

FAILURE HANDLING:
- "Nie znaleziono pojazdu o podanych danych" (Vehicle not found) → confirm plate number is correct and retry.
- If Profil Zaufany login is requested → note "Login wall — this sub-page requires authentication; use basic search instead."
- If CAPTCHA appears → route to user.

STOP CONDITION: Vehicle report extracted or "no vehicle found" confirmed. Stop.
```

---

### B-2. OLX / OtoMoto — vehicle advertisement traces

**Ranking: #2 — reveals plate numbers, vehicle details, and sometimes contact/location data**

| Field | Detail |
|---|---|
| **Source URL** | https://www.olx.pl and https://www.otomoto.pl |
| **Legal access** | Open |
| **Cost (PLN)** | Free |
| **Accuracy / freshness** | Real-time for active listings; archived pages decay after ~30 days unless archived |
| **Time to obtain** | Minutes |
| **Caveats** | Search by phone number (883 109 779 or 12 333 77 30) or email domain (@gpucomputer.pl) in seller profile search. May require OLX account to see full phone numbers. Archive lookups via Wayback Machine (Section C-1) can recover deleted ads. |
| **Skip-if** | No vehicle ads found and B-1 also returns nothing. |

```prompt-for-browser-agent
TASK: Search OLX and OtoMoto for vehicles advertised by GPUcomputer or Mateusz Szklarski.

STEP 1 — OLX:
1. Navigate to https://www.olx.pl
2. In the main search bar ("Czego szukasz?" — What are you looking for?), search for "GPUcomputer".
3. Also search for "Mateusz Szklarski".
4. Filter by category "Motoryzacja" (Automotive) if results are too broad.
5. Note any listings: vehicle type, price, registration plate (sometimes visible in photos), seller username, phone number.

STEP 2 — OtoMoto:
1. Navigate to https://www.otomoto.pl
2. In the seller search, look for a "Sprzedający" (Seller) or "Firma" (Company) search option.
3. Search for "Gpucomputer" or "Szklarski".
4. Note any listings with plate numbers visible in photos.

STEP 3 — Phone-number trace on OLX:
1. On https://www.olx.pl, search for phone number "883109779" in the search bar.
2. Note any listings from this phone number (not limited to vehicles).

EXTRACTION FORMAT (return as JSON):
{
  "olx_listings": [{"title": "...", "price_PLN": ..., "plate_visible": "...", "phone": "...", "url": "..."}],
  "otomoto_listings": [...],
  "phone_trace_results": [...]
}

FAILURE HANDLING:
- If phone number search returns no results → confirm OLX allows phone-number search (UI may have changed; if not, note "OLX phone search unavailable."
- If login required to see phone numbers → note "Login wall — phone numbers hidden; note listing URLs for manual follow-up."

STOP CONDITION: All vehicle listings found and extracted. Stop.
```

---

### B-3. CEPiK formal data request (owner name lookup by plate)

**Ranking: #3 — definitive owner identification, slow**

| Field | Detail |
|---|---|
| **Source URL** | https://www.gov.pl/web/gov/zloz-wniosek-o-udostepnienie-danych-jednostkowych-z-centralnej-ewidencji-pojazdow |
| **Legal access** | Restricted-with-request — requires Profil Zaufany login; must justify "prawnie uzasadniony interes" (legally justified interest) |
| **Cost (PLN)** | 30.40 PLN per request (+ 17 PLN if acting through an attorney) |
| **Accuracy / freshness** | Authoritative; current as of request date |
| **Time to obtain** | Up to 30 days |
| **Caveats** | From 1 January 2026, this request must be submitted via e-Doręczenia (electronic delivery) rather than traditional postal route. Profil Zaufany required. Payment to Ministerstwo Cyfryzacji, account 52 1130 1017 0020 1232 2420 0001, title "CEPiK – opłata za udostępnienie danych." The pending EPU case number (Nc-e 552126/26) constitutes a legally justified interest. |
| **Skip-if** | Skip if a komornik is already instructed — they have direct privileged CEPiK access and can search by owner name without a plate. |

**BROWSER-AGENT CANNOT EXECUTE THIS STEP** (requires Profil Zaufany authentication). Route to creditor to submit through their Polish Profil Zaufany account, or to their lawyer.

---

### B-4. autoDNA / carVertical — supplementary VIN history

| Field | Detail |
|---|---|
| **Source URL** | https://www.autodna.pl |
| **Legal access** | Open (paid) |
| **Cost (PLN)** | ~49–99 PLN per report |
| **Accuracy / freshness** | Aggregates UFG, CEPiK, European registers; generally current within days |
| **Time to obtain** | Minutes |
| **Caveats** | Useful for cross-border vehicle history (debtor imports hardware from Hong Kong — may have imported vehicles). Requires VIN from B-1 or B-2. Lower signal-per-złoty than CEPiK formal request for domestic ownership confirmation. |
| **Skip-if** | B-1 already provides adequate history detail. |

---

## Section C — Actual Operating Address

### C-1. Wayback Machine — gpucomputer.pl historical snapshots

**Ranking: #1 — free, recovers deleted contact pages and old addresses**

| Field | Detail |
|---|---|
| **Source URL** | https://web.archive.org |
| **Legal access** | Open |
| **Cost (PLN)** | Free |
| **Accuracy / freshness** | Historical; snapshot frequency varies (typically 2–10x per year for small business sites) |
| **Time to obtain** | Minutes |
| **Caveats** | Images and JavaScript-rendered content may not archive correctly. Focus on /kontakt and /o-nas pages which are likely static. The current contact page confirms Mogilska 16/7 — old snapshots may reveal prior addresses or additional phone numbers. |
| **Skip-if** | Never skip — always check, especially for deleted pages with previous addresses. |

```prompt-for-browser-agent
TASK: Retrieve all archived versions of the gpucomputer.pl contact and about pages to find historical addresses, phone numbers, and any bankruptcy announcements.

TARGET URL: https://web.archive.org/web/*/gpucomputer.pl/*

STEPS:
1. Navigate to https://web.archive.org
2. In the Wayback Machine search bar, type "gpucomputer.pl/kontakt" and press Enter.
3. The calendar view will show all archived snapshots. Note the years with most captures.
4. Click on the earliest available snapshot (expected ~2015–2016) and open it.
5. Record: address, phone number(s), email(s), NIP if shown.
6. Click on the 2020 snapshot. Record same fields.
7. Click on the 2023 snapshot. Record same fields.
8. Click on the most recent available snapshot (2025 or 2026). Record same fields.
9. Separately, search for "gpucomputer.pl/o-nas" (About us page) and repeat steps 4–8.
10. Also search for "gpucomputer.pl" (homepage) to check for any bankruptcy or restructuring notices.

EXTRACTION FORMAT (return as JSON):
{
  "snapshots": [
    {
      "url_archived": "...",
      "snapshot_date": "...",
      "address": "...",
      "phone": "...",
      "email": "...",
      "nip_shown": "...",
      "bankruptcy_notice": "..."
    }
  ]
}

FAILURE HANDLING:
- If no snapshots found → "No Wayback Machine archive for this URL — skip."
- If snapshot shows only a placeholder page → note "Placeholder only — no business data."
- If content is JavaScript-rendered and not readable → try the earliest static HTML snapshot available.

STOP CONDITION: All unique address/phone variants across snapshots extracted. Stop.
```

---

### C-2. Google Maps reviews and business listing

**Ranking: #2 — customer reviews often reveal real operating location**

| Field | Detail |
|---|---|
| **Source URL** | https://maps.google.com |
| **Legal access** | Open |
| **Cost (PLN)** | Free |
| **Accuracy / freshness** | Reviews may be 1–5 years old; business listing updated by owner |
| **Time to obtain** | Minutes |
| **Caveats** | Customer reviews sometimes contain the reviewer's neighbourhood (implying proximity to debtor's real location) or references to a physical workshop / showroom. The official listing may show a different address if the owner updated it. |
| **Skip-if** | Never skip. |

```prompt-for-browser-agent
TASK: Find GPUcomputer's Google Maps listing, extract address, phone, hours, and read all reviews for location/operational clues.

STEPS:
1. Navigate to https://maps.google.com
2. Search for "GPUcomputer Kraków".
3. If a business panel appears on the left, extract:
   - Listed address ("Adres" field)
   - Phone number
   - Website
   - Opening hours ("Godziny otwarcia")
   - Google rating and number of reviews
4. Click "Opinie" (Reviews) tab. Read all reviews (or up to 30 most recent):
   - Note any review that mentions a physical location different from Mogilska 16.
   - Note any review complaining about non-delivery, disappeared seller, or bankruptcy.
   - Note reviewer names and dates.
5. Also search for "Mateusz Szklarski Kraków" on Google Maps.
6. Check for any photos posted by users — these sometimes show a workshop/garage.

EXTRACTION FORMAT (return as JSON):
{
  "google_maps_address": "...",
  "google_maps_phone": "...",
  "rating": ...,
  "review_count": ...,
  "notable_reviews": [
    {"reviewer": "...", "date": "...", "text_english_translation": "...", "location_clue": "..."}
  ],
  "photos_showing_location": true/false,
  "bankruptcy_mentions": "..."
}

FAILURE HANDLING:
- If no listing found → try "Gpucomputer" without diacritics or "GPU computer Kraków".
- If reviews are in Polish → translate to English in the extraction output.

STOP CONDITION: All reviews scanned and any location clues noted. Stop.
```

---

### C-3. Allegro seller profile and Ceneo / Opineo reviews

**Ranking: #3 — Polish marketplace reviews reveal real operation**

| Field | Detail |
|---|---|
| **Source URL** | https://allegro.pl / https://www.ceneo.pl / https://www.opineo.pl |
| **Legal access** | Open |
| **Cost (PLN)** | Free |
| **Accuracy / freshness** | Near-real-time for active listings; reviews may be older |
| **Time to obtain** | Minutes |
| **Caveats** | If GPUcomputer sells on Allegro, the seller profile will show registered NIP, city, and feedback. A sudden drop in feedback or a "zawieszony" (suspended) account is a strong operational signal. |
| **Skip-if** | If no Allegro/Ceneo presence found. |

```prompt-for-browser-agent
TASK: Find GPUcomputer's seller profiles on Allegro, Ceneo, and Opineo; extract reviews and seller data.

STEP 1 — Allegro:
1. Navigate to https://allegro.pl
2. In the search bar ("Czego szukasz?" — What are you looking for?), search "gpucomputer".
3. Filter results by "Sprzedający" (Seller) if option available, or look for listings by seller "gpucomputer".
4. Click on the seller profile (if found). Extract:
   - Seller name and city
   - Number of transactions and feedback score
   - Date joined
   - Any suspension or warning notice
5. Also search for "Mateusz Szklarski" in the seller search.

STEP 2 — Ceneo:
1. Navigate to https://www.ceneo.pl
2. Search for "gpucomputer" in the search bar ("Szukaj produktów, sklepów" — Search products, shops).
3. If a shop entry appears, click "Sklep" (Shop) and note: address, phone, rating, number of reviews.

STEP 3 — Opineo:
1. Navigate to https://www.opineo.pl
2. Search for "gpucomputer" or "www.gpucomputer.pl".
3. Extract: shop address, rating, all reviews with dates.

EXTRACTION FORMAT (return as JSON):
{
  "allegro": {"seller_name": "...", "city": "...", "feedback_score": ..., "member_since": "...", "suspended": true/false},
  "ceneo": {"shop_address": "...", "rating": ..., "review_count": ...},
  "opineo": {"shop_address": "...", "rating": ..., "reviews": [{"date": "...", "text_english": "..."}]}
}

FAILURE HANDLING:
- If search returns no results → confirm no presence on that platform.
- If login required → note "Login wall — cannot access seller details without account."

STOP CONDITION: All three platforms checked. Stop.
```

---

### C-4. Panorama Firm, PKT.pl, Targeo — business directory traces

**Ranking: #4 — often cache old addresses; cross-reference with CEIDG**

| Field | Detail |
|---|---|
| **Source URL** | https://panoramafirm.pl / https://www.pkt.pl / https://mapa.targeo.pl |
| **Legal access** | Open |
| **Cost (PLN)** | Free |
| **Accuracy / freshness** | Scraped from public sources; may be 6–24 months stale |
| **Time to obtain** | Minutes |
| **Caveats** | Targeo already confirms NIP 8661681248, REGON 362678345, address Mogilska 16, PKD 26.20.Z. Cross-check for any additional addresses or phone numbers not in CEIDG. |
| **Skip-if** | Can be deprioritised if C-1 through C-3 yield a clear operational address. |

```prompt-for-browser-agent
TASK: Check Polish business directories for GPUcomputer to find any addresses or phone numbers not present in CEIDG.

Known confirmed data (skip if identical):
- NIP: 8661681248 | REGON: 362678345 | Address: ul. Mogilska 16/7, 31-516 Kraków

STEPS:
1. Navigate to https://panoramafirm.pl
   Search for "gpucomputer" or "Mateusz Szklarski". Extract full address and any additional phone numbers.

2. Navigate to https://www.pkt.pl
   Search for "gpucomputer kraków". Extract address and phone.

3. Navigate to https://mapa.targeo.pl
   Search for NIP "8661681248". Extract any address, phone, or email not already known.

4. Navigate to https://zumi.pl (if accessible)
   Search for "gpucomputer". Extract same fields.

EXTRACTION FORMAT (return as JSON):
{
  "panoramafirm": {"address": "...", "phone": "...", "additional_info": "..."},
  "pkt": {"address": "...", "phone": "..."},
  "targeo": {"address": "...", "phone": "...", "email": "..."},
  "new_data_vs_ceidg": "..."
}

FAILURE HANDLING:
- If any site unavailable → mark "Site unavailable" and continue to next.

STOP CONDITION: All four directories checked. Note any new address/phone vs. CEIDG. Stop.
```

---

### C-5. WHOIS and domain intelligence (gpucomputer.pl)

**Ranking: #5 — low signal for address but sometimes reveals registrant**

| Field | Detail |
|---|---|
| **Source URL** | https://www.dns.pl/en/whois and https://securitytrails.com / https://viewdns.info |
| **Legal access** | Open |
| **Cost (PLN)** | Free (basic); SecurityTrails requires free account for full history |
| **Accuracy / freshness** | NASK WHOIS is near-real-time; SecurityTrails historical data may be months to years old |
| **Time to obtain** | Minutes |
| **Caveats** | Polish .pl WHOIS via NASK (dns.pl) typically shows registrant data unless privacy protection is enabled. Privacy protection is uncommon for Polish business domains but does occur. Historical DNS data on SecurityTrails can reveal past IP addresses and nameservers, which sometimes correlate with hosting providers who have billing addresses. |
| **Skip-if** | If registrant is privacy-protected or identical to already-known data. |

```prompt-for-browser-agent
TASK: Look up WHOIS and historical DNS data for gpucomputer.pl.

STEP 1 — NASK WHOIS:
1. Navigate to https://www.dns.pl/en/whois
2. Enter "gpucomputer.pl" in the WHOIS search field and click "Search".
3. Extract: registrant name, registrant address, registrant email, registration date, expiry date, nameservers.

STEP 2 — ViewDNS:
1. Navigate to https://viewdns.info
2. Click "Reverse Whois Lookup" under "Tools". Search for "gpucomputer" or "mateusz szklarski".
3. Also run "IP History" for "gpucomputer.pl".
4. Note any IP addresses associated with the domain and the hosting provider name.

STEP 3 — SecurityTrails (if NASK yields nothing new):
1. Navigate to https://securitytrails.com
2. If free account required, note "SecurityTrails login required — route to user."
3. If accessible, search for "gpucomputer.pl" and extract historical A records and any registrant changes.

EXTRACTION FORMAT (return as JSON):
{
  "whois_registrant_name": "...",
  "whois_registrant_address": "...",
  "whois_registrant_email": "...",
  "registration_date": "...",
  "expiry_date": "...",
  "nameservers": [...],
  "hosting_ip": "...",
  "hosting_provider": "...",
  "privacy_protected": true/false
}

FAILURE HANDLING:
- If WHOIS shows "REDACTED FOR PRIVACY" → note and proceed to ViewDNS.
- If SecurityTrails requires payment → skip.

STOP CONDITION: Registrant data or "privacy protected" confirmed. Stop.
```

---

### C-6. LinkedIn / Facebook / job postings

**Ranking: #6 — operational signals, sometimes reveals real location**

| Field | Detail |
|---|---|
| **Source URL** | https://www.linkedin.com / https://www.facebook.com / https://pracuj.pl / https://nofluffjobs.com / https://justjoin.it / https://bulldogjob.pl |
| **Legal access** | Open (LinkedIn may require login for full profile) |
| **Cost (PLN)** | Free |
| **Accuracy / freshness** | LinkedIn: weeks; Facebook: real-time; job boards: current postings only |
| **Time to obtain** | Minutes |
| **Caveats** | If the debtor is still posting job listings, the business is likely still operating. Job listing cessation or deletion can signal financial distress. LinkedIn company page (if it exists) may show employee count trends. Facebook posts sometimes include location tags. |
| **Skip-if** | Covered by other steps; lower priority than A–E. |

```prompt-for-browser-agent
TASK: Search for GPUcomputer and Mateusz Szklarski on LinkedIn, Facebook, and Polish job boards.

STEP 1 — LinkedIn:
1. Navigate to https://www.linkedin.com
2. Search for "GPUcomputer Kraków" in the company search. Note any company page, employee count, and posts.
3. Search for "Mateusz Szklarski" in the people search. Note current employer, location, and any posts about business changes.
4. If login required for full profiles → extract only the public preview data visible.

STEP 2 — Facebook:
1. Navigate to https://www.facebook.com
2. Search for "Gpucomputer". Look for a business page. Note last post date, follower count, any posts about bankruptcy or supply chain issues.
3. Search for "Mateusz Szklarski". Note personal profile last activity date.

STEP 3 — Job boards:
1. Navigate to https://pracuj.pl and search for "gpucomputer". Note any active job listings and the listed location.
2. Navigate to https://nofluffjobs.com and repeat. Also try https://justjoin.it and https://bulldogjob.pl.

EXTRACTION FORMAT (return as JSON):
{
  "linkedin_company": {"exists": true/false, "employees": ..., "last_post_date": "..."},
  "linkedin_person": {"found": true/false, "current_employer": "...", "location": "..."},
  "facebook_page": {"last_post_date": "...", "follower_count": ..., "bankruptcy_mention": "..."},
  "job_listings_active": [{"board": "...", "title": "...", "location": "...", "posted_date": "..."}],
  "job_listing_cessation_date": "..."
}

FAILURE HANDLING:
- If login required for full LinkedIn → use only public data.
- If Facebook search returns no business page → note "No Facebook business page found."

STOP CONDITION: All platforms checked. Stop.
```

---

## Section D — Bank Accounts

### D-1. Biała Lista Podatników VAT (VAT White List — bank account disclosure)

**Ranking: #1 — discloses all bank accounts reported to tax authority; open and free**

| Field | Detail |
|---|---|
| **Source URL** | https://www.podatki.gov.pl/wykaz-podatnikow-vat-wyszukiwarka/ |
| **Legal access** | Open — no login required |
| **Cost (PLN)** | Free |
| **Accuracy / freshness** | Updated daily by KAS (National Revenue Administration); reflects accounts reported to tax authority as of the query date |
| **Time to obtain** | Immediate |
| **Caveats** | Only shows accounts **reported by the taxpayer for VAT payment purposes**. A debtor may have unreported personal accounts, accounts in fintech banks (Revolut, N26, Wise), or foreign accounts not listed here. Also note: the Biała Lista shows historical accounts — specify the search date carefully. The debtor is VAT-active per case context. |
| **Skip-if** | Never skip — this is the single most valuable open-source bank account source. |

```prompt-for-browser-agent
TASK: Look up Mateusz Szklarski-Łopata / GPUcomputer (NIP 8661681248) on the Polish VAT White List to obtain all disclosed bank account numbers.

TARGET URL: https://www.podatki.gov.pl/wykaz-podatnikow-vat-wyszukiwarka/

INPUTS:
- NIP: 8661681248
- Query date: today's date (format: RRRR-MM-DD)

STEPS:
1. Navigate to https://www.podatki.gov.pl/wykaz-podatnikow-vat-wyszukiwarka/
2. The page shows four search tabs/fields. Use the "NIP" field.
3. Under the NIP field, enter "8661681248".
4. In the "Stan na dzień" (Status as of date) field, enter today's date in format YYYY-MM-DD.
5. Click the "Szukaj" (Search) button below the NIP field.
6. The results panel will show:
   - Entity name ("Nazwa podmiotu")
   - NIP
   - VAT registration status (czynny = active, niezarejestrowany = not registered, wykreślony = struck off)
   - Registered bank account numbers ("Numery rachunków bankowych")
   - Registered address
7. Record ALL listed bank account numbers (IBANs).
8. Also re-run the search with the entity name: in the "Nazwa podmiotu" field (min. 5 characters), enter "Gpucomputer" and search again. Compare results.

ALSO RUN — historical check:
9. Re-run the NIP search but change the date to 2026-01-15 (date closest to the debt transaction in January 2026). Record any accounts that were listed then but are no longer listed now (indicating account closure after the dispute).

EXTRACTION FORMAT (return as JSON):
{
  "nip": "8661681248",
  "entity_name": "...",
  "vat_status_today": "...",
  "bank_accounts_today": ["PL...", "PL..."],
  "vat_status_jan2026": "...",
  "bank_accounts_jan2026": ["PL..."],
  "accounts_closed_since_jan2026": ["PL..."],
  "query_date": "..."
}

FAILURE HANDLING:
- "Nie figuruje w rejestrze VAT" (Not listed in VAT register) → critical finding — record immediately.
- "Brak połączenia z serwerem" (No server connection) → retry after 15 minutes.
- If CAPTCHA appears → route to user.
- If no bank accounts listed → record "No bank accounts on White List — may use only foreign or fintech accounts."

STOP CONDITION: Both current and January 2026 lookups complete and JSON extracted. Stop.
```

---

### D-2. Invoice archives — bank account from historical invoices

**Ranking: #2 — free, may yield accounts not on Biała Lista**

| Field | Detail |
|---|---|
| **Source URL** | Creditor's own email archive; web.archive.org; gpucomputer.pl purchase flow |
| **Legal access** | Open (own documents); open (Wayback Machine) |
| **Cost (PLN)** | Free |
| **Accuracy / freshness** | As of invoice date |
| **Time to obtain** | Minutes (own archive); varies (Wayback Machine) |
| **Caveats** | The creditor paid 155,000 PLN in January 2026 — the recipient bank account from that transfer is the most valuable asset identifier available. The creditor should already have this from their bank statement. Wayback Machine snapshots of gpucomputer.pl may show a "konto bankowe" (bank account) page or invoice template with account details. |
| **Skip-if** | Skip Wayback Machine component if creditor already has the payment destination account. |

**BROWSER-AGENT NOTE:** The creditor should first check their own January 2026 bank statement for the recipient IBAN. Once obtained, proceed to D-3.

```prompt-for-browser-agent
TASK: Check Wayback Machine for any historical page on gpucomputer.pl disclosing bank account number.

TARGET URL: https://web.archive.org/web/*/gpucomputer.pl/*

STEPS:
1. Navigate to https://web.archive.org
2. Search for "gpucomputer.pl" (all pages).
3. Look specifically for pages with titles or URLs containing: "konto", "platnosc", "przelew", "faktura" (account, payment, transfer, invoice).
4. Open any such archived pages and extract any IBAN or bank account number shown.
5. Also check archived homepage for any "Dane do przelewu" (Transfer details) section.

EXTRACTION FORMAT (return as JSON):
{
  "bank_accounts_from_website": ["PL..."],
  "source_page": "...",
  "snapshot_date": "..."
}

FAILURE HANDLING:
- If no relevant pages archived → "No bank account data found in Wayback Machine archive."

STOP CONDITION: Any IBAN found or all relevant URLs checked with no results. Stop.
```

---

### D-3. OGNIVO / komornik's formal bank account search

**THIS STEP IS NOT AVAILABLE AS OSINT.**

OGNIVO is the KIR (National Clearing House) system linking all Polish banks and credit unions (SKOKi). It allows a bailiff (*komornik sądowy*) to simultaneously query all participating banks for accounts held by a named debtor. **Participation in OGNIVO is voluntary for banks; as of 2026, most major Polish banks participate but some smaller banks and all foreign banks do not.**

**Access requirement:** A *tytuł wykonawczy* — a court judgment or payment order bearing a *klauzula wykonalności* (enforcement clause) — is required before a komornik can use OGNIVO. The creditor does not yet have this. **Do not use as OSINT.**

**Post-judgment action:** Once a *nakaz zapłaty* (payment order) from EPU is served and becomes final (or a regular court judgment is obtained), instruct a *komornik sądowy* to conduct a *zlecenie poszukiwania majątku* (asset search order) which includes OGNIVO query, CEPiK query, ZUS/KRUS query, and queries to banks not in OGNIVO. Cost: typically 300–600 PLN for the formal order, plus komornik's statutory fees on recovered amount (15% + VAT).

---

## Section E — Other Business Interests

### E-1. KRS (Krajowy Rejestr Sądowy) — search by personal name

**Ranking: #1 — reveals undisclosed corporate shareholdings**

| Field | Detail |
|---|---|
| **Source URL** | https://wyszukiwarka.ms.gov.pl (KRS search engine, Ministry of Justice) or https://prs.ms.gov.pl |
| **Legal access** | Open — no login required |
| **Cost (PLN)** | Free (browsing); 5–20 PLN per certified odpis |
| **Accuracy / freshness** | Near-real-time; KRS entries are legally binding |
| **Time to obtain** | Immediate |
| **Caveats** | As a JDG owner, Mateusz Szklarski may also appear in KRS as a *wspólnik* (partner/shareholder), *członek zarządu* (board member), or *prokurent* (authorised representative) in companies registered as sp. z o.o. or spółka jawna. Nominee arrangements are a common asset-shielding technique. **Note (2026):** KRS wyszukiwarka was accessible at wyszukiwarka.ms.gov.pl; the Portal Rejestrów Sądowych (prs.ms.gov.pl) is the primary current entry point but may require account creation for some functions. |
| **Skip-if** | Never skip — critical for detecting hidden corporate assets. |

```prompt-for-browser-agent
TASK: Search KRS (National Court Register) for any companies where Mateusz Szklarski-Łopata appears as a shareholder, board member, or authorised representative.

TARGET URL: https://wyszukiwarka.ms.gov.pl/

ALTERNATIVE URL (if above is unavailable): https://prs.ms.gov.pl/krs/strona-glowna — then navigate to KRS search section.

STEPS:
1. Navigate to https://wyszukiwarka.ms.gov.pl/
2. Select or locate the search mode for "Osoby" (Persons) rather than "Podmioty" (Entities), if such a tab exists.
   - If only entity search is available, switch to person-search mode.
   - Polish UI label: "Wyszukiwanie osób" (Person search) or "Osoba fizyczna" (Natural person).
3. Enter:
   - Imię (First name): Mateusz
   - Nazwisko (Last name): Szklarski
4. Click "Szukaj" (Search).
5. Also search for "Szklarski-Łopata" as the surname (hyphenated variant).
6. For each result returned, note:
   - Company name ("Firma")
   - KRS number
   - Role ("Funkcja"): shareholder, board member, etc.
   - Date of entry and any date of exit from the role.
7. For any company found, click through to the full KRS entry and note:
   - Company status (active/dissolved/in liquidation)
   - Registered address
   - Share capital
   - Co-shareholders/directors

EXTRACTION FORMAT (return as JSON):
{
  "companies_found": [
    {
      "company_name": "...",
      "krs_number": "...",
      "role": "...",
      "entry_date": "...",
      "exit_date": "...",
      "company_status": "...",
      "company_address": "...",
      "share_capital_PLN": ...,
      "co_directors": [...]
    }
  ],
  "search_date": "..."
}

FAILURE HANDLING:
- If the person-search mode is not available → note "KRS person search unavailable via this URL — try https://prs.ms.gov.pl"
- If site returns "Brak wyników" (No results) → confirm correct name spelling and retry with both "Szklarski" and "Szklarski-Łopata".
- If login required → note "KRS person search requires PRS account — route to lawyer."

STOP CONDITION: All companies for both name variants found and extracted. Stop.
```

---

### E-2. CRBR (Centralny Rejestr Beneficjentów Rzeczywistych)

**Ranking: #2 — discloses beneficial ownership in companies; open and free**

| Field | Detail |
|---|---|
| **Source URL** | https://podatki.gov.pl/crbr/ |
| **Legal access** | Open — no login required |
| **Cost (PLN)** | Free |
| **Accuracy / freshness** | Reporting entities must update within 14 days of changes; delays occur |
| **Time to obtain** | Immediate |
| **Caveats** | CRBR applies to companies (sp. z o.o., SA, spółki osobowe) — not to JDG. Useful for finding any company where Szklarski is an undisclosed beneficial owner even if not formally registered in KRS. The portal is in Polish only. |
| **Skip-if** | Skip if E-1 (KRS) returns no companies at all — but CRBR can catch nominee arrangements where KRS shows a nominee director, not the beneficial owner. |

```prompt-for-browser-agent
TASK: Search the Polish Central Register of Beneficial Owners (CRBR) for Mateusz Szklarski.

TARGET URL: https://podatki.gov.pl/crbr/

STEPS:
1. Navigate to https://podatki.gov.pl/crbr/
2. Find the search bar. The page may show fields for searching by:
   - NIP of the company
   - Name of the beneficial owner (beneficjent rzeczywisty)
   - Name of the company
3. Search by beneficial owner name: enter "Szklarski" in the person name field (exact label may vary — look for "Imię i nazwisko beneficjenta" or similar).
4. If a NIP-based company search is available, also enter NIP 8661681248 (the debtor's JDG NIP — may link to any companies he controls).
5. Record all entities returned.

EXTRACTION FORMAT (return as JSON):
{
  "companies_where_beneficial_owner": [
    {
      "company_name": "...",
      "nip": "...",
      "ownership_percentage": ...,
      "entry_date": "..."
    }
  ],
  "note": "..."
}

FAILURE HANDLING:
- If person-name search is not available (only NIP search) → search by NIP and note limitation.
- If "Brak danych" (No data) → note "No beneficial ownership found in CRBR."

STOP CONDITION: Search complete and results extracted. Stop.
```

---

### E-3. eZamówienia / BIP — public procurement contracts

**Ranking: #3 — reveals government contracts (income stream and asset proxy)**

| Field | Detail |
|---|---|
| **Source URL** | https://ezamowienia.gov.pl and https://www.bip.gov.pl |
| **Legal access** | Open |
| **Cost (PLN)** | Free |
| **Accuracy / freshness** | Updated upon contract award; may lag 30–60 days |
| **Time to obtain** | Minutes |
| **Caveats** | GPUcomputer (PKD 26.20.Z — computer manufacturing) may have supplied GPU workstations to universities, research institutes, or government agencies. Contract values and counterparties are public. If the debtor has an active government contract, this is both an income stream (seizable via art. 896 KPC) and evidence of solvency. |
| **Skip-if** | Low priority for small JDG; check quickly but do not invest time if no results. |

```prompt-for-browser-agent
TASK: Search Polish public procurement databases for contracts awarded to GPUcomputer or Mateusz Szklarski.

STEP 1 — eZamówienia:
1. Navigate to https://ezamowienia.gov.pl
2. Find the search section (likely "Wyszukiwarka ogłoszeń" — Announcements search or "Wyniki postępowań" — Procurement results).
3. Search for "gpucomputer" and "Szklarski" in the supplier/contractor name field.
4. Note any contracts: value, contracting authority, date, status.

STEP 2 — Biuletyn Zamówień Publicznych (BZP):
1. Navigate to https://bzp.uzp.gov.pl/
2. Search for "gpucomputer" in the "Wykonawca" (Contractor) field.
3. Note any results.

EXTRACTION FORMAT (return as JSON):
{
  "contracts_found": [
    {
      "contracting_authority": "...",
      "contract_value_PLN": ...,
      "contract_date": "...",
      "status": "active/completed"
    }
  ]
}

FAILURE HANDLING:
- If no results → "No public procurement contracts found."

STOP CONDITION: Both portals searched. Stop.
```

---

## Section F — Other Creditors and Existing Claims

### F-1. KRZ (Krajowy Rejestr Zadłużonych) — insolvency and enforcement register

**Ranking: #1 — definitive for formal bankruptcy/restructuring; open and free**

| Field | Detail |
|---|---|
| **Source URL** | https://krz.ms.gov.pl |
| **Legal access** | Open |
| **Cost (PLN)** | Free |
| **Accuracy / freshness** | Near-real-time; entries must be made within statutory deadlines after court order |
| **Time to obtain** | Immediate (when system is online) |
| **Caveats** | As of 21 May 2026, no KRZ entries were found for this debtor per case context. However, the debtor claims to have "filed for bankruptcy protection." **The lag between filing an upadłość or restrukturyzacja motion and its appearance in KRZ can be 2–8 weeks** — a negative result today does not rule out a filing made in the past 2 months. The KRZ system was experiencing a technical outage as of the date of this document (23 May 2026) — retry. Also search by NIP (8661681248), not just name, as name variants can cause misses. |
| **Skip-if** | Never skip — this is the primary insolvency register. |

```prompt-for-browser-agent
TASK: Search KRZ (National Debt Register) for Mateusz Szklarski / NIP 8661681248 to detect any insolvency, restructuring, or enforcement proceedings.

TARGET URL: https://krz.ms.gov.pl

PRE-CHECK: If the site shows "Przerwa techniczna" (Technical break) → record timestamp and retry after 2 hours. The system has scheduled and unscheduled maintenance.

STEPS (once site is accessible):
1. Navigate to https://krz.ms.gov.pl
2. Find the search interface. Likely labelled "Wyszukaj podmiot" (Search entity) or similar.
3. Search 1 — by NIP: enter "8661681248" in the NIP field. Click "Szukaj" (Search).
4. Record all results: proceeding type, court, case number, date of entry, trustee/administrator name if shown.
5. Search 2 — by name: enter "Szklarski" in the name field. Check for both "Mateusz Szklarski" and "Szklarski-Łopata".
6. Search 3 — by entity name: enter "Gpucomputer" and search.
7. For each result, note:
   - Type of proceeding: "upadłość" (bankruptcy), "restrukturyzacja" (restructuring — postępowanie układowe, sanacyjne, przyspieszony układ, układ częściowy), or "egzekucja" (enforcement, where egzekucja sądowa was discontinued due to bezskuteczność — ineffectiveness)
   - Court and case number
   - Date entered in register
   - Status: pending / closed

EXTRACTION FORMAT (return as JSON):
{
  "nip_search_results": [],
  "name_search_results": [],
  "entity_name_search_results": [],
  "any_insolvency_found": true/false,
  "any_restructuring_found": true/false,
  "search_date": "..."
}

FAILURE HANDLING:
- "Przerwa techniczna" → retry after 2 hours; if still unavailable after 24 hours → route to lawyer to check via KRZ professional portal.
- "Brak wyników" (No results) across all three searches → record as "No KRZ entries found as of [date]."

STOP CONDITION: All three searches complete. Stop.
```

---

### F-2. Portal Informacyjny Sądów Powszechnych — civil and commercial court case search

**Ranking: #2 — reveals ongoing litigation, existing judgments against the debtor**

| Field | Detail |
|---|---|
| **Source URL** | https://portal3.wroclaw.sa.gov.pl (new portal as of 1 March 2026) — note: the URL uses Wrocław Court of Appeal's infrastructure for all Polish courts |
| **Legal access** | Restricted — requires account registration (free, but requires email) |
| **Cost (PLN)** | Free (account creation required) |
| **Accuracy / freshness** | Near-real-time; updated by courts upon each procedural step |
| **Time to obtain** | Minutes once account is created |
| **Caveats** | **Access is limited:** parties to a case (and their lawyers) see full case content. Third parties can search public case data — which includes case number, parties' names, court, and hearing dates — but NOT the full content of documents. Since 1 March 2026, the old portal URL is defunct; use https://portal3.wroclaw.sa.gov.pl. Search by debtor's PESEL (unknown), NIP (8661681248), or full name. Name search may yield false positives for a common surname — verify by NIP. |
| **Skip-if** | Skip if lawyer already has portal access and has confirmed case history. |

```prompt-for-browser-agent
TASK: Search the Polish Court Information Portal for any cases involving Mateusz Szklarski or GPUcomputer (NIP 8661681248).

TARGET URL: https://portal3.wroclaw.sa.gov.pl

PRE-STEP: This portal requires a free account. If no account exists, navigate to the registration page ("Rejestracja" / Register) and create one using the creditor's email. Confirm registration via email link.

STEPS (after login):
1. Log in at https://portal3.wroclaw.sa.gov.pl
2. Navigate to "Wyszukiwanie spraw" (Case search).
3. Search 1 — by name: enter "Szklarski" in the surname field ("Nazwisko") and "Mateusz" in the first name field ("Imię"). Click "Szukaj".
4. Search 2 — by NIP: if NIP search field is available, enter "8661681248".
5. Search 3 — by company name: enter "Gpucomputer".
6. For each case found, note:
   - Case number ("Sygnatura akt")
   - Court ("Sąd")
   - Case type ("Rodzaj sprawy"): civil, commercial, enforcement
   - Case status ("Status"): pending / closed
   - Parties ("Strony"): plaintiff and defendant
   - Next hearing date ("Termin posiedzenia")
   - Judge assigned ("Sędzia referent")
7. Note separately the creditor's own EPU case: Nc-e 552126/26 — verify its current status.

EXTRACTION FORMAT (return as JSON):
{
  "cases_involving_debtor": [
    {
      "case_number": "...",
      "court": "...",
      "type": "...",
      "status": "...",
      "plaintiff": "...",
      "defendant": "...",
      "next_hearing": "...",
      "note": "..."
    }
  ],
  "epu_case_status": "...",
  "search_date": "..."
}

FAILURE HANDLING:
- If login is required and no account exists → "Portal requires account — route to user for registration and execution."
- If search returns "Brak wyników" → record as "No court cases found."
- If NIP search not available → note and use name search only.

STOP CONDITION: All three searches complete. Stop.
```

---

### F-3. KRD, ERIF BIG, BIG InfoMonitor — commercial debt registries

**Ranking: #3 — signals whether other creditors have already listed the debtor**

| Field | Detail |
|---|---|
| **Source URL** | https://krd.pl / https://www.erif.pl / https://www.big.pl |
| **Legal access** | Restricted — consumer/creditor access requires registration and identity verification; checking a third party requires demonstrating legitimate interest or being a contracting party |
| **Cost (PLN)** | Free self-check (as debtor); paid report on third party (~30–80 PLN per bureau) |
| **Accuracy / freshness** | Near-real-time for listed debts; entries must meet statutory thresholds (min. 200 PLN consumer, 500 PLN business) |
| **Time to obtain** | Minutes after account creation |
| **Caveats** | **GDPR/RODO constraint:** Checking another person's credit bureau status as a private individual requires demonstrating a legally justified purpose. Being a creditor with a pending case is generally sufficient. However, the bureau may still require submission of supporting documentation. The creditor is better positioned to make this request themselves (or via lawyer) rather than via an automated agent. If the debtor is already listed by multiple creditors, this strongly signals insolvency. |
| **Skip-if** | Low priority for OSINT — proceed if other evidence suggests multiple creditors. |

**BROWSER-AGENT NOTE:** Account creation at these bureaux requires Polish phone number verification (SMS) and identity document. Route to creditor for self-registration. Once registered, the browser agent can assist with the search form.

---

### F-4. licytacje.komornik.pl — public bailiff auction listings

**Ranking: #4 — reveals whether any komornik has already seized debtor's assets**

| Field | Detail |
|---|---|
| **Source URL** | https://licytacje.komornik.pl |
| **Legal access** | Open |
| **Cost (PLN)** | Free |
| **Accuracy / freshness** | Updated by komornik offices when auctions are scheduled; current listings are near-real-time |
| **Time to obtain** | Minutes |
| **Caveats** | Only shows assets already seized AND scheduled for auction. Failure to appear here does not mean no enforcement proceedings exist. |
| **Skip-if** | Quick check; low effort. |

```prompt-for-browser-agent
TASK: Search Polish bailiff auction portal for assets belonging to Mateusz Szklarski or GPUcomputer.

TARGET URL: https://licytacje.komornik.pl

STEPS:
1. Navigate to https://licytacje.komornik.pl
2. Find the search field(s). Likely a general text search or fields for "dłużnik" (debtor) name.
3. Search for "Szklarski", "Gpucomputer", and "8661681248" (NIP).
4. Note any auctions: asset type, location, minimum bid, bailiff contact, scheduled date.

EXTRACTION FORMAT (return as JSON):
{
  "auctions_found": [
    {
      "asset_description": "...",
      "location": "...",
      "minimum_bid_PLN": ...,
      "bailiff": "...",
      "auction_date": "..."
    }
  ]
}

FAILURE HANDLING:
- If search returns no results → "No auctions found — debtor's assets not yet under enforcement."
- If site structure differs from expected → describe what search options are actually available.

STOP CONDITION: Search complete. Stop.
```

---

### F-5. Rejestr Zastawów Rejestrowych — registered pledge register

**Ranking: #5 — reveals if any creditor already holds a registered pledge on debtor's movables**

| Field | Detail |
|---|---|
| **Source URL** | https://prs.ms.gov.pl → Centralna Informacja o Zastawach Rejestrowych (CI RZ) |
| **Legal access** | Requires free account on Portal Rejestrów Sądowych |
| **Cost (PLN)** | Free (search); fee for certified extracts (~5–20 PLN) |
| **Accuracy / freshness** | Legally authoritative; updated upon court registration of pledge |
| **Time to obtain** | Minutes once account created |
| **Caveats** | Separately, the Rejestr Zastawów Skarbowych (tax pledge register) is searchable at https://podatki.gov.pl → check if the tax authority holds a tax pledge on any of the debtor's assets. Also searchable at https://e-zastawy.ms.gov.pl (if this URL differs from PRS). |
| **Skip-if** | Low priority; useful primarily after other assets identified. |

```prompt-for-browser-agent
TASK: Search the Polish Registered Pledge Register (Rejestr Zastawów) for pledges on assets of Mateusz Szklarski / GPUcomputer (NIP 8661681248).

TARGET URL: https://prs.ms.gov.pl — navigate to Centralna Informacja (Central Information) section.

PRE-STEP: Account on Portal Rejestrów Sądowych (PRS) required. Create at prs.ms.gov.pl if not already done (uses Tożsamość system — email registration).

STEPS (after login):
1. At https://prs.ms.gov.pl, click the "Centralna Informacja" (Central Information) tile/button.
2. Select "Zastawy Rejestrowe" (Registered Pledges) from the menu.
3. In the search form, enter NIP "8661681248" in the NIP field ("NIP zastawcy" — pledgor's NIP).
4. Also search by name: "Szklarski Mateusz" in the name field ("Imię i nazwisko zastawcy").
5. Note any pledges: pledged asset description, pledgee (wierzyciel zastawniczy), value, registration date.

ALSO — Tax Pledge Register:
6. Navigate to https://podatki.gov.pl → look for "Rejestr Zastawów Skarbowych" (Tax Pledge Register).
7. Enter NIP "8661681248" and search.

EXTRACTION FORMAT (return as JSON):
{
  "registered_pledges": [
    {
      "pledged_asset": "...",
      "pledgee_name": "...",
      "secured_amount_PLN": ...,
      "registration_date": "..."
    }
  ],
  "tax_pledges": [...]
}

FAILURE HANDLING:
- If login required and no PRS account → route to user.
- If NIP search unavailable → try name search.
- "Brak wyników" → record "No registered pledges found."

STOP CONDITION: Both registers searched. Stop.
```

---

## Section G — Operational Signals

### G-1. Website traffic and ordering activity

**Ranking: #1 — reveals whether business is still genuinely operating**

| Field | Detail |
|---|---|
| **Source URL** | https://www.gpucomputer.pl (live site); https://similarweb.com (traffic); https://web.archive.org (historical) |
| **Legal access** | Open |
| **Cost (PLN)** | Free (SimilarWeb free tier limited); gpucomputer.pl open |
| **Accuracy / freshness** | Live site: current; SimilarWeb: ~1 month lag; Wayback: historical |
| **Time to obtain** | Minutes |
| **Caveats** | **Do NOT place a test order or make contact with the debtor posing as a customer.** This would constitute pretexting and is prohibited. You may, however, examine the product listings, pricing, and order process as a non-registered visitor without initiating a transaction. Check whether the cart/checkout flow is functional (an abandoned/broken checkout suggests business has stopped). |
| **Skip-if** | Never skip — critical for operational assessment. |

```prompt-for-browser-agent
TASK: Assess whether GPUcomputer is still actively operating by examining the live website and traffic data. Do NOT submit an order or make contact.

STEP 1 — Live website assessment:
1. Navigate to https://www.gpucomputer.pl
2. Note:
   - Date of most recently listed products (check product listings for "Dodano" / "Data dodania" — Date added)
   - Whether the shopping cart ("Koszyk") is functional — click "Dodaj do koszyka" (Add to cart) on a product and see if the checkout flow loads (do NOT proceed to payment or contact)
   - Whether the phone number 883 109 779 is still displayed
   - Any notice of suspension, bankruptcy, or "niedostępne" (unavailable) products
   - Website's last modification date (if visible)

2. Navigate to https://www.gpucomputer.pl/sklep (Shop page). Note total number of products listed and whether any are marked as "Niedostępny" (Unavailable) or "Brak" (Out of stock).

STEP 2 — SimilarWeb traffic:
1. Navigate to https://www.similarweb.com/website/gpucomputer.pl/
2. Note: monthly visits, traffic trend (growing/declining), traffic sources, engagement metrics.
3. Specifically note if traffic dropped sharply after January 2026 (coinciding with the debt dispute).

STEP 3 — Wayback Machine recent snapshot:
1. Navigate to https://web.archive.org/web/*/gpucomputer.pl
2. Open the most recent snapshot (2025 or 2026). Compare product count and site content to current live site.

EXTRACTION FORMAT (return as JSON):
{
  "site_live": true/false,
  "most_recent_product_date": "...",
  "cart_functional": true/false,
  "out_of_stock_products": ...,
  "bankruptcy_notice_on_site": true/false,
  "similarweb_monthly_visits": ...,
  "traffic_trend": "growing/declining/stable",
  "traffic_drop_post_jan2026": true/false,
  "assessment": "still operating / appears dormant / shutdown"
}

FAILURE HANDLING:
- If website is down (DNS failure or timeout) → record "Website offline — significant operational red flag."
- If SimilarWeb shows "Insufficient data" → note and skip traffic analysis.

STOP CONDITION: All three steps complete. Stop.
```

---

### G-2. Reddit, Wykop, Facebook — complaint mining

**Ranking: #2 — reveals multiple creditors, patterns of non-delivery, insolvency signals**

| Field | Detail |
|---|---|
| **Source URL** | https://www.reddit.com / https://www.wykop.pl / https://www.facebook.com |
| **Legal access** | Open |
| **Cost (PLN)** | Free |
| **Accuracy / freshness** | Near-real-time for posts; forum posts may be older |
| **Time to obtain** | Minutes |
| **Caveats** | Reddit (r/Poland, r/pcmasterrace_pl, r/hardware_pl) and Wykop are major Polish IT community forums where users report fraud. Facebook group "Oszuści / Scammerzy Polska" and similar consumer groups may have posts. Multiple complaints about non-delivery in early 2026 would be strong evidence of insolvency or fraud pattern. |
| **Skip-if** | Never skip — very high signal-per-minute of work. |

```prompt-for-browser-agent
TASK: Search social media and forums for complaints about GPUcomputer or Mateusz Szklarski.

STEP 1 — Reddit:
1. Navigate to https://www.reddit.com
2. Search for "gpucomputer" (all subreddits). Note any posts mentioning non-delivery, scam, or financial problems.
3. Search for "Szklarski Kraków" and "GPU computer".
4. Check these specific subreddits: r/Polska, r/pcmasterrace, and r/hardware using the site's search.

STEP 2 — Wykop:
1. Navigate to https://www.wykop.pl
2. Search for "gpucomputer". Note any posts, discussions, or "znaleziska" mentioning this company.
3. Also search for "Szklarski" and "GPU computer Kraków".

STEP 3 — Facebook groups:
1. Navigate to https://www.facebook.com
2. Search for "gpucomputer" in public groups. Note any complaints.
3. Search for "Mateusz Szklarski gpucomputer".

STEP 4 — Google search for complaints:
1. Navigate to https://www.google.com
2. Search: "gpucomputer.pl oszustwo" (gpucomputer.pl scam/fraud)
3. Search: "Szklarski GPUcomputer nie dostarczył" (Szklarski GPUcomputer failed to deliver)
4. Search: "gpucomputer opinie 2025" and "gpucomputer opinie 2026"

EXTRACTION FORMAT (return as JSON):
{
  "reddit_complaints": [{"subreddit": "...", "date": "...", "summary_english": "...", "url": "..."}],
  "wykop_complaints": [...],
  "facebook_complaints": [...],
  "google_results": [{"query": "...", "summary_english": "...", "url": "..."}],
  "total_complaints_found": ...,
  "pattern": "isolated / multiple creditors / systematic fraud"
}

FAILURE HANDLING:
- If login required for Reddit → use Google search operator: site:reddit.com gpucomputer.pl
- If Wykop requires login for search → use Google: site:wykop.pl gpucomputer

STOP CONDITION: All four steps complete. Stop.
```

---

### G-3. Asset-stripping signals on OLX / Allegro

**Ranking: #3 — selling off expensive GPU/server inventory is a major red flag**

| Field | Detail |
|---|---|
| **Source URL** | https://www.olx.pl / https://allegro.pl |
| **Legal access** | Open |
| **Cost (PLN)** | Free |
| **Accuracy / freshness** | Real-time for active listings |
| **Time to obtain** | Minutes |
| **Caveats** | A business that builds GPU workstations (unit values 30,000–300,000 PLN) suddenly liquidating inventory via OLX/Allegro at below-market prices is a key *skarga pauliańska* (art. 527 KC) trigger. Note: the debtor's current website lists RTX 5090-based workstations — check if these appear on second-hand platforms simultaneously. |
| **Skip-if** | Combine with B-2 (vehicle search) to avoid duplication. |

```prompt-for-browser-agent
TASK: Search OLX and Allegro for high-value GPU/server equipment being sold by GPUcomputer or Mateusz Szklarski at potentially distressed prices.

STEP 1 — OLX:
1. Navigate to https://www.olx.pl
2. Search for "gpucomputer" — note any listings.
3. Search for "RTX 5090 workstation Kraków" — check if any listings originate from the Kraków area with prices significantly below retail.
4. Search for phone number "883109779" — note all listings from this seller.

STEP 2 — Allegro:
1. Navigate to https://allegro.pl
2. Search for "gpucomputer" seller. Check active and completed (sold) listings.
3. In the seller profile (if accessible), look for recent bulk listings of GPU hardware.

EXTRACTION FORMAT (return as JSON):
{
  "olx_listings": [
    {"title": "...", "price_PLN": ..., "market_value_estimate_PLN": ..., "discount_pct": ..., "date": "...", "url": "..."}
  ],
  "allegro_listings": [...],
  "bulk_selling_signal": true/false,
  "below_market_pricing": true/false,
  "note": "..."
}

FAILURE HANDLING:
- If phone number search unavailable on OLX → use seller name search.
- If Allegro login required for seller profile → note "Login wall."

STOP CONDITION: Both platforms searched. Stop.
```

---

## Section H — Insolvency and Restructuring

### H-1. MSiG full-text search (Monitor Sądowy i Gospodarczy)

**Ranking: #1 — official gazette where bankruptcy/restructuring notices are published**

| Field | Detail |
|---|---|
| **Source URL** | https://prs.ms.gov.pl → Monitor Sądowy i Gospodarczy section; also https://wyszukiwarka-msig.ms.gov.pl |
| **Legal access** | Open (PRS) |
| **Cost (PLN)** | Free |
| **Accuracy / freshness** | Entries published within statutory deadlines after court orders; typically 7–21 days lag from court filing |
| **Time to obtain** | Immediate |
| **Caveats** | **Since 29 November 2025, KRS entries are no longer published in MSiG** — KRS data now flows directly to the PRS system. However, insolvency and restructuring notices (upadłość, restrukturyzacja) still require MSiG publication. As of 2022, all MSiG issues since 2016 are full-text searchable. The debtor's claim to have "filed for bankruptcy protection" would generate an MSiG entry — search specifically for: ogłoszenie upadłości (bankruptcy declaration), otwarcie postępowania restrukturyzacyjnego (opening of restructuring), wezwanie wierzycieli (creditor call). |
| **Skip-if** | Never skip — complements KRZ (F-1). |

```prompt-for-browser-agent
TASK: Search Monitor Sądowy i Gospodarczy (MSiG) for any insolvency or restructuring announcements involving Mateusz Szklarski or GPUcomputer.

TARGET URL: https://wyszukiwarka-msig.ms.gov.pl/ 
ALTERNATIVE: https://prs.ms.gov.pl → KRS → Monitor Sądowy i Gospodarczy section

STEPS:
1. Navigate to https://wyszukiwarka-msig.ms.gov.pl/
2. Find the search form. Available search criteria typically include:
   - "Nazwa podmiotu" (Entity name)
   - "NIP"
   - "Fragment tekstu" (Text fragment)
   - "Typ sprawy" (Type of case)
   - "Data od/do" (Date from/to)
3. Search 1 — by entity name: enter "Gpucomputer". Set date range from 2025-01-01 to today.
4. Search 2 — by text fragment: enter "Szklarski Mateusz". Same date range.
5. Search 3 — by NIP: enter "8661681248". Same date range.
6. For each result, extract:
   - Issue number and date ("Numer" i "Data wydania")
   - Case type ("Typ sprawy"): ogłoszenie upadłości / restrukturyzacja / inne
   - Court ("Sąd") and case number
   - Content summary (first 300 characters of announcement text, translated to English)

EXTRACTION FORMAT (return as JSON):
{
  "msig_results": [
    {
      "issue_number": "...",
      "publication_date": "...",
      "case_type_english": "...",
      "court": "...",
      "case_number": "...",
      "announcement_summary_english": "..."
    }
  ],
  "any_insolvency_publication": true/false
}

FAILURE HANDLING:
- If site shows "Przerwa techniczna" → retry after 2 hours.
- If NIP search unavailable → use name and text searches only.
- If imsig.pl (commercial MSiG aggregator) is faster → use https://www.imsig.pl/szukaj as fallback.

STOP CONDITION: All three searches complete. Stop.
```

---

### H-2. KRZ — deeper search for pre-KRZ and all proceeding varieties

*(See also F-1 — primary KRZ search. This entry covers the nuances.)*

**Polish restructuring law provides six proceeding types under Prawo restrukturyzacyjne (Restructuring Law of 2015):**

1. **Postępowanie o zatwierdzenie układu** (Arrangement approval — simplest, no court announcement required initially; may not appear in KRZ/MSiG until approved)
2. **Przyspieszone postępowanie układowe** (Expedited arrangement — KRZ entry within days of court opening)
3. **Postępowanie układowe** (Standard arrangement — KRZ entry within days)
4. **Postępowanie sanacyjne** (Rehabilitation/sanation — most complex; court order publicised immediately)
5. **Upadłość z możliwością zawarcia układu** (Bankruptcy with arrangement — rare, pre-2016 law)
6. **Upadłość obejmująca likwidację majątku** (Liquidation bankruptcy — full asset liquidation)

**Critical for this case:** The "postępowanie o zatwierdzenie układu" initiated by a nadzorca układu (arrangement supervisor) may proceed for up to 4 months without public court announcement — making it invisible to KRZ and MSiG initially. If the debtor engaged a doradca restrukturyzacyjny (restructuring advisor/licensed insolvency practitioner), this form could be underway without public records. Route this question to a lawyer who can query the Krajowa Izba Doradców Restrukturyzacyjnych (KIDR — National Chamber of Restructuring Advisors) for the name of any nadzorca appointed.

---

## Section I — Spousal Asset Situation

### I-1. Community property assessment — CEIDG declaration

**Ranking: #1 — CEIDG discloses whether debtor opted out of community property (intercyza)**

| Field | Detail |
|---|---|
| **Source URL** | https://aplikacja.ceidg.gov.pl or https://ceidg.gov.pl |
| **Legal access** | Open |
| **Cost (PLN)** | Free |
| **Accuracy / freshness** | Updated when debtor files the declaration; the absence of a declaration means statutory community property (wspólność majątkowa) applies — per case context, no intercyza declared |
| **Time to obtain** | Immediate |
| **Caveats** | Per case context: **CEIDG shows no community property regime declared.** This means statutory *wspólność majątkowa małżeńska* (marital community property) applies — IF the debtor is married. Assets acquired during marriage are joint assets and may be subject to enforcement against the debtor's share (art. 787 KPC allows enforcement against community property after supplementary title obtained from court). However, verification of marital status is not publicly searchable (see I-2). |
| **Skip-if** | Skip detailed CEIDG re-check if case context already confirms no intercyza. |

---

### I-2. USC (Urząd Stanu Cywilnego) — marital status verification

**THIS STEP CANNOT BE EXECUTED BY BROWSER AGENT OR AS OPEN OSINT.**

Polish vital records (akta stanu cywilnego — marriage certificates, USC registers) are **not publicly searchable** by third parties under Polish law (Prawo o aktach stanu cywilnego, art. 45). Access is limited to:
- The person themselves
- Persons with a direct legal interest (*interes prawny* — typically demonstrated by showing pending litigation)
- Courts, prosecutors, police, and bailiffs acting ex officio

**A private creditor cannot compel USC to disclose whether the debtor is married.** However:
- **Indirect signals:** A jointly owned property in EKW (Section A) with a spouse's name in Dział II would confirm marriage and community property regime.
- **Social media:** LinkedIn/Facebook may disclose marital status voluntarily.
- **Komornik route (post-judgment):** After obtaining a *tytuł wykonawczy*, the bailiff can request USC records.

**Practical route:** Ask the Polish lawyer to submit a formal wniosek to USC Kraków citing the pending court case (EPU Nc-e 552126/26) as the legal interest. This is a grey area — some USC offices accept creditor requests, others reject them. Budget for potential refusal and appeal.

---

### I-3. Rejestr Małżeńskich Ustrojów Majątkowych — intercyza register

**Ranking: #2 — checks for post-nuptial agreements that could shield spousal assets**

| Field | Detail |
|---|---|
| **Source URL** | Polish National Council of Notaries: https://krn.org.pl/en/notarial-registers |
| **Legal access** | Restricted — accessible to parties, courts, and persons demonstrating legal interest |
| **Cost (PLN)** | ~30–100 PLN per search (notary access fee) |
| **Accuracy / freshness** | Updated upon notarial act; real-time |
| **Time to obtain** | 1–5 business days |
| **Caveats** | The Rejestr Małżeńskich Ustrojów Majątkowych is maintained by the Polish Council of Notaries. It contains intercyza agreements (property separation agreements) between spouses. **A debtor may have signed an intercyza after the debt arose** — this is relevant to *skarga pauliańska* (art. 527 KC). Under art. 471 KRO (Family Code), an intercyza signed during financial difficulties with knowledge of the detriment to creditors can itself be attacked via skarga pauliańska within 5 years of the act. |

**BROWSER-AGENT CANNOT EXECUTE THIS STEP.** Route to the creditor's Polish lawyer to submit a formal request to the Notarial Registers system, citing the EPU case number.

---

### I-4. Skarga pauliańska timing considerations (art. 527 KC)

This is not a source but a legal framework that governs the use of findings from Sections I and J.

**Key facts:**
- **Time limit:** 5 years from the date of the fraudulent act (art. 534 KC) — any asset transfer by the debtor since January 2021 could still be challenged.
- **Presumption against close parties:** If the debtor transferred assets to a spouse, parent, or sibling, **knowledge of the intent to defraud is presumed** by law (art. 527 §3 KC) — the creditor does not need to prove they knew.
- **Trigger:** Any real estate transfer, vehicle transfer, share transfer, or significant cash gift made after (or in anticipation of) the January 2026 debt could be challenged.
- **Evidentiary need:** OSINT from Sections A, B, E, I, and J must document the timeline of asset movements relative to the debt arising. EKW Section III is particularly important — it shows the date of any ownership change.

---

## Section J — Foreign Assets and Asset Stripping

### J-1. EU Corporate Registers (European Business Registry Association)

**Ranking: #1 — checks for corporate presence in EU member states**

| Field | Detail |
|---|---|
| **Source URL** | https://e-justice.europa.eu/content_business_registers_in_member_states-106-en.do |
| **Legal access** | Open (each member state's register) |
| **Cost (PLN)** | Free to low (varies by member state) |
| **Accuracy / freshness** | Varies by jurisdiction; Germany (Handelsregister), Czech Republic (Obchodní rejstřík), Slovakia (Obchodný register) are near-real-time |
| **Time to obtain** | Minutes per jurisdiction |
| **Caveats** | Given the debtor's claimed "Hong Kong supplier collapse," check: Czech Republic, Slovakia, Germany (nearest EU jurisdictions for electronics import). Also check the EU beneficial ownership interconnection system (Business Registers Interconnection System — BRIS) which links national registers. |
| **Skip-if** | Low priority unless other evidence suggests cross-border activity. |

```prompt-for-browser-agent
TASK: Search EU business registers for any company registered under "Szklarski" or "Gpucomputer" in neighbouring EU jurisdictions.

STEP 1 — Czech Republic (Obchodní rejstřík):
1. Navigate to https://or.justice.cz/ias/ui/rejstrik
2. In the name search field ("Jméno" / Name), enter "Szklarski" and search. Also search "Gpucomputer".
3. Note any results.

STEP 2 — Slovakia (Obchodný register):
1. Navigate to https://orsr.sk/
2. Search for "Szklarski" and "Gpucomputer" in the business name and person search.

STEP 3 — Germany (Handelsregister):
1. Navigate to https://www.handelsregister.de/rp_web/mask.do?Typ=e
2. Search for "Szklarski" under "Personensuche" (Person search).

STEP 4 — BRIS (EU Business Registers Interconnection System):
1. Navigate to https://bris.europa.eu/
2. Search for "Szklarski" as a person across all connected EU registers.

EXTRACTION FORMAT (return as JSON):
{
  "czech_register_results": [...],
  "slovak_register_results": [...],
  "german_register_results": [...],
  "bris_results": [...],
  "foreign_company_found": true/false
}

FAILURE HANDLING:
- If a register is unavailable or in a non-English language → note the language barrier; do not translate speculatively.
- If login required → note and skip that jurisdiction.

STOP CONDITION: All four registers checked. Stop.
```

---

### J-2. Brussels Ia Regulation — EU cross-border enforcement

This is a legal framework note, not a database source.

If the debtor holds assets in another EU member state (discovered in J-1), the Polish court judgment obtained in the creditor's proceedings will be automatically recognised and enforceable across all EU member states under **Regulation (EU) No 1215/2012 (Brussels Ia)** without any additional *exequatur* proceeding. The judgment can be enforced directly by a bailiff in the relevant EU member state upon presentation of a standard certificate issued by the Polish court (Form I of Annex I to the Regulation). **This makes cross-border EU assets relatively easy to reach once a title is obtained — a major advantage of Path B (regular lawsuit) over EPU.**

---

### J-3. Crypto wallet traces

**Ranking: #2 within J — low-probability but worth checking given tech-company profile**

| Field | Detail |
|---|---|
| **Source URL** | Debtor website, invoices, social media profiles |
| **Legal access** | Open (public blockchain data) |
| **Cost (PLN)** | Free |
| **Accuracy / freshness** | Blockchain data: immutable and real-time |
| **Time to obtain** | Minutes to hours |
| **Caveats** | A GPU workstation company may accept cryptocurrency payments. Check: (1) gpucomputer.pl source code for any embedded wallet addresses, (2) any invoices shared by the creditor for payment instructions, (3) LinkedIn/Facebook posts mentioning crypto payment. If a wallet address is found, it can be traced on-chain for balance and transaction history. However, **Polish courts have not yet established a stable enforcement mechanism for cryptocurrency seizure** — this is cutting-edge legal territory as of 2026; route to a specialist fintech lawyer. |
| **Skip-if** | Skip if no crypto wallet indicators found in under 10 minutes. |

```prompt-for-browser-agent
TASK: Check for cryptocurrency wallet addresses in gpucomputer.pl website source code and any public business documents.

STEP 1 — Website source code:
1. Navigate to https://www.gpucomputer.pl
2. Open the browser developer tools (right-click → "View page source" or Ctrl+U).
3. Search (Ctrl+F) the source for: "bitcoin", "ethereum", "btc", "eth", "0x", "bc1", "3J", "wallet", "crypto", "blockchain", "coinbase", "binance".
4. Repeat for https://www.gpucomputer.pl/kontakt and https://www.gpucomputer.pl/sklep

STEP 2 — Google search:
1. Navigate to https://www.google.com
2. Search: "gpucomputer.pl bitcoin wallet" and "gpucomputer kryptowaluty płatność"

EXTRACTION FORMAT (return as JSON):
{
  "wallet_addresses_found": ["..."],
  "crypto_mentioned_on_site": true/false,
  "source_of_wallet_address": "..."
}

FAILURE HANDLING:
- If no crypto indicators found in 5 minutes → "No crypto wallet evidence found — skip."

STOP CONDITION: Source code checked and Google search complete. Stop.
```

---

## Section K — Integrating Analysis

### 9. Recommended Sequencing — Execution Plan

#### First Hour (Zero-Cost OSINT — browser agent executes)

| Step | Source | Expected Output |
|---|---|---|
| 1 | D-1 (Biała Lista VAT — NIP 8661681248) | Bank account numbers, VAT status |
| 2 | G-1 (gpucomputer.pl live assessment) | Is business still operating? |
| 3 | F-1 (KRZ — NIP search) | Insolvency/restructuring flag |
| 4 | H-1 (MSiG search) | Insolvency publication flag |
| 5 | C-1 (Wayback Machine — gpucomputer.pl) | Historical addresses, old phone numbers |
| 6 | E-1 (KRS person search — Szklarski) | Hidden corporate holdings |
| 7 | E-2 (CRBR — Szklarski beneficial owner) | Hidden beneficial ownership |
| 8 | F-2 (Portal Sądów — name/NIP search) | Existing judgments against debtor |
| 9 | G-2 (Reddit/Wykop/Google — complaint mining) | Multiple creditor signals |
| 10 | C-2 (Google Maps — GPUcomputer) | Operational address clues |

**Dependency:** Steps 1–10 are independent and can be parallelised across three browser-agent sessions.

---

#### First Day (Low-Cost / Moderate Effort)

| Step | Source | Dependency | Expected Output |
|---|---|---|---|
| 11 | C-3 (Allegro/Ceneo/Opineo) | None | Marketplace signals |
| 12 | C-4 (Panorama Firm/PKT.pl/Targeo) | None | Corroborating address data |
| 13 | C-5 (WHOIS + ViewDNS) | None | Domain registrant data |
| 14 | B-2 (OLX/OtoMoto vehicle traces) | None | Vehicle plate numbers |
| 15 | B-1 (historiapojazdu.gov.pl) | Plate number from Step 14 | Vehicle insurance/inspection history |
| 16 | G-3 (OLX/Allegro asset stripping) | None | Distressed liquidation signals |
| 17 | F-4 (licytacje.komornik.pl) | None | Existing enforcement actions |
| 18 | F-5 (Rejestr Zastawów) | PRS account | Existing pledges on movables |
| 19 | A-2 (MSIP Kraków) | None | KW number for Kraków parcels |
| 20 | A-3 (geoportal.gov.pl) | None | Parcel IDs for formal EGiB request |
| 21 | J-1 (EU corporate registers) | None | Cross-border companies |
| 22 | J-3 (crypto wallet trace) | None | Crypto asset indicators |
| 23 | E-3 (eZamówienia/BIP) | None | Government contracts |

---

#### First Week (Paid / Formal Routes — creditor or lawyer executes)

| Step | Source | Cost (PLN) | Time |
|---|---|---|---|
| 24 | A-1 (EKW browse — needs KW from Step 19 or 25) | Free | Immediate once KW known |
| 25 | A-4 (ongeo.pl terrain report — residential address) | 30–99 | Minutes |
| 26 | A-6 (Certified EKW extract for court use) | 20–30 | 1–3 days |
| 27 | B-3 (CEPiK formal data request — Profil Zaufany) | 30.40 | Up to 30 days |
| 28 | I-3 (Notarial intercyza register — lawyer request) | 50–100 | 1–5 days |
| 29 | A-5 (EGiB wniosek to Starostwo — any non-Kraków address) | 30–150 | 14–30 days |
| 30 | I-2 (USC marital status — lawyer request) | ~50 + refusal risk | 7–14 days |

---

### 10. Cost-Effective Stopping Points

| Cumulative spend (PLN) | Decision point |
|---|---|
| 0 (Steps 1–23) | Run all zero-cost OSINT first. If Steps 1–10 confirm: (a) bank accounts on Biała Lista, (b) no KRZ/MSiG entry, (c) business still operating → **strong signal for Path B (regular lawsuit + zabezpieczenie)**. |
| 150–300 | Add paid steps: ongeo.pl terrain report + CEPiK request + EKW certified extract. If real estate found → **file zabezpieczenie natychmiast** (immediate preservation order for hipoteka przymusowa). |
| 500–1,500 | **Commission a biuro wywiadu gospodarczego** if OSINT reveals complex picture (multiple companies, international links, asset transfers). Pricing (as of 2025): Bisnode (Dun & Bradstreet Poland): ~400–800 PLN for a standard business intelligence report; Creditreform Polska: ~300–700 PLN; Coface Poland: ~250–600 PLN; KRD wywiad ekonomiczny: ~200–500 PLN. These reports aggregate commercial databases, include payment behaviour history, and sometimes surface information not accessible via open registers. Order time: 1–5 business days. |
| 2,000–5,000 | **Commission a detektyw licencjonowany** (licensed investigator, PIDP-licensed) if physical surveillance of the operating address, identification of real workshops or warehouses, or confirmation of spousal assets is needed. Cost: typically billed at 100–300 PLN/hour or 800–2,500 PLN for a structured report on asset status. Results are legally usable as evidence in civil proceedings if obtained without illegal methods. |
| 5,000–15,000 | **Full kancelaria adwokacka (law firm) mandate** for Path B: regular lawsuit + zabezpieczenie at SR Kraków-Śródmieście. Based on research findings, the lawyer can tailor the zabezpieczenie motion (art. 730–757 KPC) to specifically target identified assets. Court fee for 155,000 PLN claim: 7,750 PLN (5% of claim value, max 200,000 PLN). Attorney's fees: 5,400–10,800 PLN minimum (statutory scale, §2 rozporządzenia Ministra Sprawiedliwości). |
| Post-judgment | **Komornik sądowy** (bailiff) for enforcement: OGNIVO query + CEPiK query + ZUS query + bank queries = typically 300–600 PLN for zlecenie poszukiwania majątku + statutory 15% + VAT on recovered amounts. Route to Komornik Sądowy właściwy dla SR Kraków-Śródmieście. |

---

### 11. Red Flags — Patterns Indicating Asset Stripping, Evasion, or Insolvency

**Imminent bankruptcy indicators:**
- KRZ/MSiG entry for *postępowanie o zatwierdzenie układu* with a nadzorca układu but no public court announcement (see H-2 — this proceeding can run 4 months in stealth)
- Biała Lista bank accounts closed or reduced between January 2026 and today (Step D-1 comparison)
- Website product listings dated pre-January 2026 (last update coinciding with debt dispute)
- Allegro seller account suspended or feedback freezing after January 2026
- Multiple complaints on Reddit/Wykop from different customers for non-delivery in early 2026

**Asset stripping / skarga pauliańska triggers (art. 527 KC):**
- Real estate transfer in EKW Dział III showing a new owner, or EKW Dział II showing a transfer between January 2025 and today — especially to a spouse or family member
- Vehicle transfers out of CEPiK in 2025–2026 (discoverable post-judgment via CEPiK formal request or komornik)
- Bulk sale of high-value GPU inventory on OLX/Allegro at below-market prices after January 2026 (G-3)
- New company registration in KRS (E-1) after the debt arose, with business profile identical to GPUcomputer — nominee arrangement
- CRBR (E-2) showing beneficial ownership in a company where debtor does not appear in KRS as director
- Intercyza signed in 2025–2026 (I-3 lookup)

**Sophisticated evasion signals:**
- WHOIS showing domain transfer or registrant change in 2025–2026 (C-5)
- Foreign company registration in a neighbouring EU state (J-1) with name or address overlap
- LinkedIn company page showing "0 employees" while website continues to take orders
- Multiple email domains (waldek@gpucomputer.pl suggests a second employee — this person may be a nominee or may have information about the real business structure; do not contact deceptively)
- Hong Kong supplier claim without documentary support — could be a pretext; no Hong Kong insolvency proceedings would affect Polish legal obligations

**Polish document markers to look for:**
- "Sąd ogłosił upadłość" or "ogłoszenie upadłości" in MSiG → formal bankruptcy
- "Otwarcie postępowania restrukturyzacyjnego" → restructuring opening
- "Nadzorca układu" (arrangement supervisor name) in any document → stealth restructuring
- "Wykreślony" in CEIDG → JDG struck off (closure)
- "Zawieszenie działalności" in CEIDG → suspended (not necessarily insolvent but significant signal)
- "Wpis do KRZ" with "egzekucja umorzona z powodu bezskuteczności" → enforcement already tried and failed (highest red flag)

---

### 12. Professional Escalation — Who Does What, at What Cost

| Question | Best resource | Typical cost (PLN) | Delivery time | Language |
|---|---|---|---|---|
| Is there real property? Where? | **Kancelaria adwokacka** (files EGiB wniosek, EKW search, MSIP) | 500–2,000 incl. fees | 5–14 days | Polish (English summary possible) |
| What vehicles does he own? | **Komornik sądowy** (post-judgment, direct CEPiK access) | 300–600 + 15% on recovery | Post-judgment only | Polish |
| What bank accounts exist? | **Komornik sądowy** (OGNIVO + bank queries post-judgment) | 300–600 + 15% on recovery | Post-judgment only | Polish |
| Is he married? What is the marital property regime? | **Kancelaria adwokacka** (USC + notarial register request) | 200–500 | 7–21 days | Polish |
| Has he transferred assets? Skarga pauliańska viable? | **Kancelaria adwokacka** or **radca prawny** (review EKW history, KRS transfers, notarial acts) | 1,000–5,000 | 2–4 weeks | Polish (English summary possible) |
| Does he have assets worth pursuing? | **Biuro wywiadu gospodarczego** (Bisnode, Coface, Creditreform, KRD Ekonomiczny) for pre-litigation intelligence | 300–800 per report | 1–5 days | Polish (sometimes English) |
| Physical address, vehicle plates, working location | **Detektyw licencjonowany** (licensed under ustawa o usługach detektywistycznych) | 800–3,000 per assignment | 3–10 days | Polish (report can be prepared in Polish for court) |
| Is this a pattern of fraud against multiple creditors? | **Detektyw + kancelaria** combined mandate; consider criminal report (zawiadomienie o podejrzeniu popełnienia przestępstwa — art. 286 KK fraud) | 2,000–8,000 | 2–6 weeks | Polish |
| Cross-border EU enforcement | **Polish adwokat** with EU/international cooperation experience; Brussels Ia allows direct enforcement | 3,000–10,000 incl. foreign lawyer costs | 2–6 months | Polish + local EU language |
| Full windykacja mandate | **Firma windykacyjna** (Vindicat, KRUK, Hoist) — typically 10–20% success fee on recovery; they absorb court and komornik costs upfront | Success fee 10–20% (~15,500–31,000 PLN on 155,000 PLN debt) | Variable | Polish |

**Strategic recommendation for this case:**
1. Execute all First-Hour OSINT steps (1–10) immediately — takes 60–90 minutes, zero cost.
2. Based on results, decide within 48 hours whether OSINT supports Path B (regular lawsuit + zabezpieczenie at SR Kraków-Śródmieście).
3. If bank accounts confirmed on Biała Lista and no KRZ/MSiG entry: **Path B is strongly indicated.** The 15,000–25,000 PLN cost estimate is recoverable from the debtor if successful.
4. Engage a Kraków-based kancelaria adwokacka or radca prawny immediately. For English-speaking creditors, firms specialising in international clients include those in Kraków's city centre (Śródmieście, near SR Kraków-Śródmieście courthouse). The lawyer should file: (a) regular pozew o zapłatę, (b) wniosek o zabezpieczenie roszczenia under art. 730 KPC targeting identified bank accounts, and (c) if real estate found, wniosek o hipotekę przymusową.
5. If KRZ/MSiG shows an active restructuring proceeding: **Path B is blocked** — zgłoszenie wierzytelności (creditor claim submission) to the restructuring administrator is the mandatory route. Engage a restructuring specialist immediately.

---

> **Disclaimer:** This document constitutes research methodology guidance only. It does not constitute legal advice. The creditor should engage a Polish-licensed adwokat or radca prawny before taking any procedural steps. Polish law, portal access rules, and registry procedures are subject to change. Where uncertainty about a 2026 detail is noted, the browser agent should describe what it actually finds rather than assume the instructions are correct.

---

*Document prepared: 23 May 2026 | Case: Nc-e 552126/26 | Debtor NIP: 8661681248*
