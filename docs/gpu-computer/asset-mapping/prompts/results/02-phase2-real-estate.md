# Phase 2 — Real Estate Discovery: Results

## Top-line summary
**No KW number was obtained for free.** Both candidate addresses (Mogilska 16 — virtual office; Kazimierza Wielkiego 36 — historical address) DO have KW entries in the ksiegiwieczyste.pl commercial dataset, but both are gated behind a **39.99 PLN per-KW paywall**. No name-based public search exists. **EKW (Task 5) cannot be run without a KW number** — skipped.

This is the structural bottleneck the master plan explicitly warned about: EKW has no name search, and every legitimate route to a KW number for an unknown owner either requires payment, requires Profil Zaufany + demonstrated legal interest (EGiB — out of scope), or only works if you already have a parcel ID that you can manually cross-reference.

**Decision implication:** Phase 2 does NOT change Path A vs Path B math on its own. To pierce this paywall economically, the cheapest move is the 39.99 PLN ksiegiwieczyste.pl unlock for **Kazimierza Wielkiego 36** (NOT Mogilska 16 — that's a multi-tenant virtual office building, the KW will be the building owner, not Mateusz). If that KW's Section II (Dział II) shows Mateusz as owner, you've found seizable real estate. If not, you've spent 40 PLN to rule out his historical address. Recommend asking your lawyer whether to authorize this 40 PLN spend before continuing.

***

## Task 0 — Name-based KW search (ksiegiwieczyste.pl / wieczyste.pl)
```json
{
  "ksiegiwieczyste_name_search_url_per_prompt": "https://ksiegiwieczyste.pl/szukaj-po-imieniu-i-nazwisku",
  "result": "404 - page does not exist. The slug has been removed.",
  "wieczyste_pl_name_search": "Not offered. Site only supports search by address, parcel number, or KW ID.",
  "ksiegiwieczyste_pl_name_search": "Not visible on home page. Only address / parcel / KW ID search available.",
  "conclusion": "No public name-based KW search is currently available on either commercial portal. This Phase 2 bottleneck does NOT disappear."
}
```

## Task 1 — MSIP Kraków
```json
{
  "status": "Not completed — login wall + portal restructuring",
  "notes": "The 'Mapa dla architektów i planistów' (architects' map) — the only MSIP composition exposing 'Struktura własności' (ownership structure) layer — requires login via Magiczny Kraków / MPI account per https://www.bip.krakow.pl/?bip_id=1&mmi=12838. Per prompt instructions: DID NOT REGISTER. The public-facing 'Mapa Geodezyjna' viewer (https://msip.krakow.pl) shows parcels but not KW numbers and not owner data.",
  "login_walls_hit": ["Magiczny Kraków / MPI account required for ownership layer"],
  "mogilska_16_parcel_id": "not extracted - login wall on relevant layer",
  "kazimierza_wielkiego_36_parcel_id": "not extracted - same"
}
```

## Task 2 — Geoportal.gov.pl
```json
{
  "status": "Tool loaded successfully; no KW data shown by design",
  "addresses_checked": ["Mogilska 16, Kraków", "Kazimierza Wielkiego 36, Kraków"],
  "result": "Geoportal national portal explicitly does not display owner names or KW numbers in the public layer (confirmed by prompt). It only provides parcel ID, area, precinct. Since both addresses are urban Kraków residential/commercial — already covered by Task 1's MSIP — no new actionable data is added here. Owner data is in EGiB which requires Profil Zaufany + legal-interest justification (explicitly out of browser-agent scope per master plan)."
}
```

## Task 3 — ksiegiwieczyste.pl address search (THE KEY RESULT)
```json
{
  "mogilska_16_krakow": {
    "matches_found": 1,
    "kw_partially_visible": "KR1P/xxxxxxxx/0 (number obscured, control digit 0 visible, 10 księgi w sąsiedztwie indicator)",
    "court_code": "KR1P (Sąd Rejonowy dla Krakowa-Podgórza w Krakowie, IV Wydział Ksiąg Wieczystych)",
    "paywall_amount_PLN": 39.99,
    "paywall_url": "https://ksiegiwieczyste.pl/op/checkout/reveal/...",
    "paid": false,
    "note": "Mogilska 16 is a multi-unit virtual-office building (WorkDesk). The KW here is almost certainly the building owner / WorkDesk-related entity, NOT Mateusz Szklarski. Low-value spend."
  },
  "kazimierza_wielkiego_36_krakow": {
    "matches_found": 2,
    "kw_partially_visible": "KR1P/xxxxxxxx/3 + 1 more",
    "court_code": "KR1P",
    "paywall_amount_PLN": 39.99,
    "paid": false,
    "note": "Historical business-registry address. Possibly his residence OR a former workshop. Higher probability of being personally owned than Mogilska. This is the cheapest viable unlock target."
  }
}
```

## Task 4 — ongeo.pl pricing
```json
{
  "raport_o_terenie_modules_relevant_to_owner_or_kw": "NONE",
  "explicit_finding": "OnGeo 'Raport o Terenie' product covers: geometric parameters, EGiB statistical data (not owner), MPZP plans, infrastructure, geology, flood risk, market transaction prices (anonymized), POI. The report does NOT include 'Numer KW' or 'Właściciel' fields per the product page.",
  "implication": "OnGeo is NOT a viable route to a KW number or owner identity. The prompt's assumption that OnGeo offers this is outdated.",
  "purchased": false
}
```

## Task 5 — EKW lookup
```json
{
  "status": "SKIPPED - no KW number obtained from Tasks 0-4",
  "reason": "EKW requires a known KW number split into court code + 8-digit number + check digit. All KW numbers from Task 3 are paywalled. No free route was found."
}
```

***

## What I'd flag for the lawyer / next decision
1. **The cheapest unlock is 39.99 PLN for the Kazimierza Wielkiego 36 KW** via ksiegiwieczyste.pl — and that's still inside the master plan's "Cost: 30–100 PLN" budget for Task 4. Worth a small spend authorization.
2. **Do NOT spend on Mogilska 16's KW** — virtual-office building, ownership will be WorkDesk or a real-estate holding co.
3. **MSIP Kraków's ownership layer requires registration** — that needs to be done by you personally (not by me per prompt) if you want a free path. The Magiczny Kraków account is free and Polish-only.
4. **The real unlock route is your lawyer + EGiB request** with legal interest — the master plan's "deliberately not covered" section. With the EPU title in hand (Path A in your master plan), your lawyer can pull EGiB owner data formally for the whole Kraków cadaster.
5. Given Phase 1 already showed **separation of property (no marital community)** and an **active live business with a single Alior account**, the Path B economics still tilt toward going to the lawyer NOW with the bank account fingerprint and skipping further OSINT spend on real estate.

**Recommended next step:** authorize me to spend up to 40 PLN on the Kazimierza Wielkiego 36 KW unlock (Task 3 paywall), or skip Phase 2 entirely and proceed to Phase 3 (other creditors / queue position) which is free and arguably more decision-critical.
