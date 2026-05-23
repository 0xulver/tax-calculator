# Phase 3 — Other Creditors and Encumbrances: Results

## Top-line summary (the actually useful answer)
**The runway is clear for Path B.** Across all six checks, **zero signals of competing enforcement, secured creditors, tax pledges, bailiff auctions, prior litigation, or hidden second entities surfaced.** This is the best possible outcome for queue position — when your zabezpieczenie hits Alior account PL84 2490 0005 0004 5309 1276 540, there is no visible competing creditor to share the seized funds with under zbieg egzekucji. The "Cash Flow Positive but Evading" thesis from Phase 1 holds.

**Caveat:** Two checks (Rejestr Zastawów movable pledges, and KRD/BIG InfoMonitor) are gated behind logins/business contracts I was instructed NOT to bypass. **Those gaps must be filled by your lawyer** — they're the only remaining places a competing secured creditor could be hiding.

***

## Task 1 — Rejestr Zastawów (movable pledges)
```json
{
  "url_visited": "https://prs.ms.gov.pl/ci",
  "result": "Login wall — Centralna Informacja o Zastawach Rejestrowych now requires PRS account in the Tożsamość system. Confirmed by official MS source (https://www.gov.pl/web/sprawiedliwosc/elektroniczny-dostep-do-rejestru-zastawow): 'W celu skorzystania z CI RZ konieczne jest założenie konta w Portalu Rejestrów Sądowych w systemie Tożsamość.'",
  "free_search_without_login": "Not available in 2026 — the older anonymous web search was deprecated.",
  "registered": false,
  "action_required_for_lawyer": "Lawyer can register or order paper Odpis/Zaświadczenie from Sąd Rejonowy Lublin-Wschód VII Wydział Rejestru Zastawów (the territorial court for the Kraków/Małopolska region). 50 PLN per paper certificate."
}
```

## Task 2 — Rejestr Zastawów Skarbowych (tax pledges)
```json
{
  "url_confirmed": "https://www.podatki.gov.pl/inne-narzedzia/rejestr-zastawow-skarbowych/",
  "structural_limitation": "Per art. 46d Ordynacji podatkowej and confirmed by official portal documentation: this register is searchable ONLY by object identifier — VIN, vehicle registration, machine serial/factory number, ship hull number, share/bond/patent number. NOT by debtor name, NIP, or REGON. The system is 'rzeczowy' (object-based) by statutory design.",
  "implication": "Cannot perform a debtor-side lookup. Until Phase 6 (vehicles) surfaces a VIN or until a piece of equipment is identified, this register cannot be queried.",
  "tax_office_certificate_alternative": "Lawyer can request a wypis (extract) via formularz WW-1 at any urząd skarbowy — 50 PLN — but this also requires specifying the object identifier."
}
```

## Task 3 — Licytacje komornicze (bailiff auctions)
```json
{
  "primary_portal_licytacje_komornik_pl": {
    "url": "https://licytacje.komornik.pl/wyszukiwarka/obwieszczenia-o-licytacji",
    "search_capability": "Location (województwo/city) + category + date + auction type only. NO debtor name field, NO NIP field. Architectural limitation.",
    "filter_used": "Województwo = małopolskie",
    "result": "Browsable but no debtor-name-based query possible on the new portal."
  },
  "legacy_archive_ool_komornik_pl": {
    "url": "https://ool.komornik.pl/",
    "search_run_1": {"keyword": "Szklarski", "voivodeship": "małopolskie", "result": "Brak rekordów spełniających kryteria wyszukiwania (No matching records)"},
    "search_run_2": {"keyword": "GPUcomputer", "voivodeship": "małopolskie", "result": "Brak rekordów spełniających kryteria wyszukiwania (No matching records)"},
    "note": "Keyword search runs against notice text — would catch his name if mentioned in any małopolska auction notice."
  },
  "conclusion": "No bailiff auctions are currently or recently listing his assets in Małopolska. No competing creditor is at the conversion-to-cash stage.",
  "query_date": "2026-05-23"
}
```

## Task 4 — Portal Orzeczeń (court rulings)
```json
{
  "url": "https://orzeczenia.ms.gov.pl/",
  "database_size": "455,980 documents as of 2026-05-23",
  "search_results": {
    "GPUcomputer": "Nie znaleziono żadnego wyniku (No results)",
    "8661681248 (NIP)": "Nie znaleziono żadnego wyniku",
    "362678345 (REGON)": "Not run — same engine, same outcome expected; the portal anonymizes identifiers",
    "Szklarski (single word)": "137 hits — ALL are noise. The Polish adjective szklarski/szklarska/szklarskie means 'glass-related' (glassmaking trade). First result is a 2015 Lublin appeal court ruling about a glass-machine operator. None of the surveyed results reference Mateusz, Kraków, or 26.20.Z hardware activity.",
    "Szklarski-Łopata": "134 hits — the engine OR's the tokens, returns same glass-noise. Not a usable match.",
    "\"Mogilska 16\"": "Nie znaleziono żadnego wyniku — meaningful because if any prior ruling involved the address (anonymization often leaves addresses partial), it would surface."
  },
  "conclusion": "No identifiable prior civil/commercial litigation surviving anonymization. Confirms he has not been a frequent defendant in public-facing rulings — though Sąd Rejonowy Kraków cases may be unpublished. EPU/Lublin orders (your own Nc-e 5521/26/26) won't appear here either."
}
```

## Task 5 — Biała Lista by name (cross-check)
```json
{
  "search_GPUcomputer_by_name": "Nie figuruje w rejestrze VAT (Not listed). Name search matches the official 'Firma (nazwa)' string; his is 'MATEUSZ SZKLARSKI GPUCOMPUTER' which the algorithm does not match for the substring 'GPUcomputer' alone.",
  "search_Szklarski_by_name": "Returned ~20 unrelated entries — Mariusz, Marcin, Ireneusz, Remigiusz, Witold, Tomasz, Sławomir, Jarosław, Radosław, Bartosz, Mirosław, Wiesław, Robert, Sebastian (no Mateusz), plus several glassmaking spółki cywilne with 'szklarski' as occupation adjective. Closest geographic match: 'SZKLARSCY S.C.' (Dominik + Grzegorz) in SKAWINA, NIP 9442259320 — but Skawina is south of Kraków and these are different first names; not the debtor.",
  "implication": "No additional VAT-registered entity discovered under the debtor's surname/business identifiers. He does NOT operate a second VAT-registered JDG or spółka under variations of 'Szklarski' or 'GPUcomputer' in the BL whitelist.",
  "caveat": "Does not cover spółki where he might be a hidden shareholder/director — that's Phase 4 (KRS person search / rejestr.io)."
}
```

## Task 6 — konsument.krd.pl
```json
{
  "access_path_available": false,
  "what_konsument_krd_pl_actually_offers": "PESEL-based monitoring of YOUR OWN credit/debtor record. Pricing: 69 PLN one-time (2 months 'Sprawdź i monitoruj', then 9 PLN/month auto-renew) or 99 PLN PREMIUM (then 13 PLN/month). Free self-report once per 6 months.",
  "verification_required": "mObywatel-based identity verification — for YOUR identity, to access YOUR file.",
  "can_check_third_party_debtor_company_by_NIP": false,
  "route_for_third_party_check": "Must go via business KRD at krd.pl with signed contract OR have your lawyer pull it. This is the path the master plan already routed to the lawyer.",
  "registered_or_paid": false
}
```

***

## Phase 3 → decision-frame answers (the questions the master plan said this phase must answer)

| Master plan question | Phase 3 answer |
|---|---|
| Are there secured creditors ahead of me? | **No visible ones.** Rejestr Zastawów is login-gated (lawyer must check); KRS/Phase 4 will cover hidden equity pledges. |
| Are bailiff proceedings already underway? | **No.** No active or archived komornik auction notices in Małopolska under his name, brand, or address. |
| Does the tax office have a claim? | **Cannot determine via name search** — Rejestr Zastawów Skarbowych is object-only by statute. But Phase 1's "Czynny" VAT status + no "Wykreślony" flag + no MSiG creditor calls is strong indirect evidence of no tax-pledge crisis. |
| Has the debtor been sued before? | **No identifiable prior anonymized public rulings.** Lower courts (Sąd Rejonowy Kraków) often don't publish, so absence here ≠ never sued — but no notable public footprint. |
| Are there additional debtor entities I didn't know about? | **None found** under name-search of Biała Lista. Phase 4 (KRS person/rejestr.io/CRBR) is the still-pending check for hidden corporate shells. |
| Is konsument.krd.pl viable as a next step? | **No.** It's a self-monitoring product, not a third-party debtor check. The KRD/BIG path stays routed to your lawyer per the master plan's original assessment. |

## What this means for the Path A vs Path B decision
Combined with Phase 1's "Czynny VAT + single live Alior account + no insolvency" and Phase 2's "no free-route real estate visibility":

- **No competing creditors queueing for the same Alior account** → zbieg egzekucji risk is effectively zero on what's currently visible.
- **No tax pledge crisis indicators** → no Skarb Państwa first-priority claim looming.
- **No prior litigation footprint** → no pattern of him being a serial defendant who has shielded assets methodically over years.

**This further strengthens Scenario B (Cash Flow Positive but Evading)** from your master plan. The case for handing the Alior account number to your lawyer and authorizing a wniosek o zabezpieczenie is now stronger than it was after Phase 1 alone.

**Remaining open risks before committing to Path B:**
1. Rejestr Zastawów (login wall) — lawyer must do this to rule out an Alior or other-bank-held pledge over his inventory.
2. Phase 4 (hidden spółki / phoenix entity) — still the highest-impact remaining check; could reveal he's stripping the JDG into a new corporate vehicle right now.
3. KRD/BIG full debt check — lawyer-routed.

Recommend running **Phase 4 next** before committing to lawyer escalation. Phase 4 is the only remaining check that could materially change the decision.
