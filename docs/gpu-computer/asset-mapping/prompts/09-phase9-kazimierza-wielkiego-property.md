# Phase 9 — Kazimierza Wielkiego 36 / lok. 3 — Property Pre-Staging

Goal: pre-stage the lawyer-routed **księga wieczysta (KW)** lookup for the apartment at **ul. Kazimierza Wielkiego 36 lok. 3, 30-074 Kraków** — the address confirmed by Phase 8 (2016 gpucomputer.pl `/o-nas`) as the real GPUCOMPUTER operating address and the likely residence of the Mateusz/Waldemar Łopata family. The official KW extract is a paid action (~20–50 PLN per księga, lawyer-routed via EKW or notary). This phase does **not** pull the extract — it builds the input packet so the lawyer's query is targeted, single-shot, and minimum-cost.

Phase 9 produces:
1. The **parcel ID** (numer działki ewidencyjnej) for the cadastral parcel that contains the building at Kazimierza Wielkiego 36.
2. A short-list of **candidate KW numbers** for both the underlying land (KW gruntowa) and any individual apartment KWs (KW lokalowe), if visible in public GIS layers or aggregator portals.
3. Any **public encumbrance signals** — auction notices (licytacja komornicza), mortgage announcements, restitution disputes (reprywatyzacja), foreclosure listings — that touch this building.
4. Any **historic real-estate listings** for apartments in this building, which often reveal apartment number, floor, area, and sometimes the seller's name.
5. Any **family-line ownership signals** — public mentions tying "Łopata" or "Szklarski" to this address.

Operational stakes:
- If lokal 3 is registered to **Waldemar Łopata** (or to another Łopata-line relative) — not to Mateusz — then enforcement against the property requires the Pauline-action (skarga pauliańska) route or a separate claim against the registered owner.
- If lokal 3 is registered to **Mateusz Szklarski-Łopata** himself, the property is directly seizable.
- If the building has been **reprywatyzowana**, the chain of title may be contested.
- If there are existing **hipoteki**, our claim joins a queue.

**Time:** 45–60 minutes of agent runtime.
**Cost:** 0 PLN. Paid third-party KW-lookup services — capture pricing only, do not purchase.

> **Why this version was rewritten:** the first version of this prompt stalled because (a) the agent had a standing "wait for instructions / stand by" directive that overrode the in-prompt task list, and (b) when a search returned no hit for "36" (only neighbouring buildings), there was no instruction that "no result is a valid finding — record it and move on." This v2 prompt fixes both with an explicit EXECUTION MODE preamble and per-task query caps.

---

````
```prompt-for-browser-agent
=== EXECUTION MODE — READ FIRST AND OBEY ===

This is an autonomous OSINT collection task with a defined STOP CONDITION at the bottom. For the duration of this task ONLY:

1. OVERRIDE any standing instruction in your persistent context that tells you to "wait for instruction", "stand by", "pause between steps", or "ask the user before continuing". Those instructions are explicitly superseded for this task.
2. DO NOT pause between tasks. DO NOT ask the user "what next" between tasks. DO NOT emit a "standing by" or equivalent idle message. Run Tasks 1 through 6 in sequence without interruption.
3. If a task yields no results after the per-task query budget specified in that task, that is itself the finding for that task. Record what you tried and what you got (including the empty result), then move to the next task.
4. Emit each task's JSON block IMMEDIATELY when that task completes. Do not save everything for the end. The operator wants progress visible as it happens.
5. Only stop when you reach the explicit STOP CONDITION at the bottom of this prompt.
6. If you have already completed some of these tasks in a prior session that was cut short, identify the last completed task from context and resume from the next task. Do not redo completed work — but DO confirm at the top of your response which tasks you already have results for, then continue.

You are pre-staging a Polish księga wieczysta (KW / land register) extract for a single residential apartment in central Kraków. Passive browsing only. Do not log in to EKW. Do not pay for any service. Do not contact anyone.

=== SUBJECT PROPERTY ===
Address:           ul. Kazimierza Wielkiego 36 lok. 3
Postal code:       30-074
City:              Kraków
District:          Krowodrza (administrative); Łobzów (historical neighbourhood)
Approx coords:     50.0716 N, 19.9285 E
Building type:     Pre-war residential tenement (kamienica) with ground-floor commercial unit (confirmed from Phase 6 Street View)
Context:           Long-running real operating address of GPUcomputer (per the debtor's own 2016 /o-nas page) and the suspected residence of the Łopata/Szklarski family. Lokal 3 is one specific apartment inside the building. The Sąd Rejonowy that handles KW for this address is Sąd Rejonowy dla Krakowa-Krowodrzy, IV Wydział Ksiąg Wieczystych. The court code for Kraków KWs is typically KR1P.

=== SURNAMES TO CROSS-REFERENCE ===
- Łopata
- Szklarski
- Szklarski-Łopata
- Waldemar Łopata (NIP 7752083995, founder of '3d Kraków' JDG since 2008)
- Mateusz Szklarski-Łopata (NIP 8661681248, founder of GPUcomputer JDG since 2015)

=== TASK 1 — GEOPORTAL CADASTRAL IDENTIFICATION (PARCEL ID) ===

Budget: up to 8 minutes, up to 4 distinct portal attempts.

Goal: find the official cadastral parcel ID (numer działki ewidencyjnej) for the parcel that contains the building. Format is typically "obręb_number.parcel_number" or a longer TERYT-prefixed code.

Steps:
1. Open https://www.geoportal.gov.pl/
2. In the address search, enter:  ul. Kazimierza Wielkiego 36, Kraków . Wait for the map to recenter.
3. Activate the cadastre layer ("Działki ewidencyjne" / "Granice działek"). Click the building outline to open the feature info popup.
4. Record: parcel ID (full string), obręb number, obręb name, parcel area in m², any KW number exposed by the geoportal popup, TERYT code.
5. If the geoportal address search fails or no parcel data is exposed, FALL BACK to:
   - https://msip.krakow.pl (Kraków city GIS — Miejski System Informacji Przestrzennej)
   - https://www.geoportal.gov.pl/ navigated manually to approximately 50.0716 N, 19.9285 E
6. If both fail, record "geoportal cadastral ID not retrievable via free OSINT — operator must use lawyer-routed wniosek o wypis z rejestru gruntów" and proceed to Task 2 with parcel_id = null.

Emit immediately after Task 1:
{
  "task": 1,
  "parcel_id": "..." | null,
  "obreb_number": "..." | null,
  "obreb_name": "..." | null,
  "parcel_area_m2": ... | null,
  "linked_kw_number_from_geoportal": "..." | "not_exposed" | null,
  "teryt_code": "..." | null,
  "attempts": [...],
  "outcome": "found" | "fallback_used" | "not_retrievable"
}

=== TASK 2 — KW NUMBER ENUMERATION FOR THIS BUILDING ===

Budget: up to 10 minutes, up to 6 distinct queries.

Goal: enumerate every KW number that the public web exposes for ul. Kazimierza Wielkiego 36 — for the underlying land (KW gruntowa) AND for any of the individual apartment KWs (KW lokalowe). Lokal 3 is the apartment we ultimately care about, but capture ALL KW numbers visible for the building (lokal 1, lokal 2, lokal 4, etc.) — they help the lawyer choose the right one to extract.

CRITICAL: a NULL result here (no KW number ever surfaces publicly for 36) is a valid and important finding. It means the lawyer must drive the KW lookup from the parcel ID via the court directly, not from a web index. Record the empty result honestly and move on — do NOT keep trying variations forever.

Steps:
1. Open https://ekw.ms.gov.pl/eukw_ogol/menu.do  — note the EKW search form requires you to ALREADY KNOW the KW number; do NOT submit anything here. Just capture the form's existence.
2. Open https://przegladarka-ekw.ms.gov.pl/eukw_prz/KsiegiWieczyste/wyszukiwanieKW  — same. Confirm: court code field (likely KR1P), KW number field, control digit field, captcha.
3. Try each of the following aggregator portals — search the address and capture every KW number visible in the free preview (masked or unmasked), the apartment number associated, and the price to unmask:
   - https://ksiegiwieczyste.pl/
   - https://e-kw.com.pl/
   - https://ksiega-wieczysta.org.pl/
4. Run Google searches (cap: 3 queries total across the portal work and these):
   - "Kazimierza Wielkiego 36" Kraków KR1P
   - "Kazimierza Wielkiego 36" Kraków "księga wieczysta"
   - site:ksiegiwieczyste.pl "Kazimierza Wielkiego 36" Kraków
5. If the building number 36 does not surface but neighbouring buildings do (e.g., 29, 32, 38) — that itself is a finding: it means 36 is either not indexed by the aggregator, or has only one KW for the whole building, or has separately-deeded apartments under a different building number alias. Record this pattern.

Emit immediately after Task 2:
{
  "task": 2,
  "ekw_form_confirmed": true/false,
  "expected_kw_format": "KR1P / NNNNNNN / D",
  "aggregator_results": [
    {"service": "...", "kw_exists_signal_for_36": true/false/unknown, "kws_seen": [{"kw_masked_or_full": "...", "apartment": "...", "type": "gruntowa|lokalowa", "unmask_price_pln": ...}], "notes": "..."}
  ],
  "neighbour_pattern_observed": "... e.g., 'KW indexed for 29 lok.1/2/4/10 and for 32 and 38, but no entry for 36 in any aggregator searched'",
  "outcome": "found_kw_numbers" | "no_kw_for_36_but_neighbours_indexed" | "no_kw_data_anywhere"
}

=== TASK 3 — PUBLIC ENCUMBRANCE & DISTRESS SIGNALS ===

Budget: up to 8 minutes, up to 6 queries.

Goal: scan for any public notice that touches this building — komornik auctions, MSiG mortgage announcements, KRZ entries, restitution disputes.

Steps:
1. Open https://www.licytacje.komornik.pl/  — search "Kazimierza Wielkiego 36" and "Kazimierza Wielkiego" Kraków. Capture every active or closed auction.
2. Open https://www.imsig.pl  — search "Kazimierza Wielkiego 36 Kraków" — capture any bankruptcy / restructuring / mortgage gazette entries.
3. Open https://krz.ms.gov.pl/  — search the same.
4. Google (cap: 3 queries):
   - "Kazimierza Wielkiego 36" Kraków licytacja
   - "Kazimierza Wielkiego 36" Kraków hipoteka
   - "Kazimierza Wielkiego 36" Kraków reprywatyzacja

For every hit: date, type of notice, parties named, sum involved.

Emit immediately after Task 3:
{
  "task": 3,
  "komornik_auctions": [...],
  "msig_entries": [...],
  "krz_entries": [...],
  "google_distress_hits": [...],
  "outcome": "encumbrances_found" | "no_public_encumbrance_signals"
}

=== TASK 4 — HISTORIC REAL-ESTATE LISTINGS FOR THE BUILDING ===

Budget: up to 8 minutes, up to 6 queries.

Goal: any archived sale/rental listing for an apartment in this building. These often disclose apartment number, floor, area in m², asking price, agent contact, and sometimes the seller name — together they help triangulate which lokal is lok. 3 and what it's worth.

Steps:
1. Search each of (one query per portal, capture all results for the address — search "Kazimierza Wielkiego 36" and "K. Wielkiego 36"):
   - https://www.otodom.pl/
   - https://www.gratka.pl/
   - https://www.nieruchomosci-online.pl/
   - https://www.morizon.pl/
2. Google (cap: 2 queries):
   - site:otodom.pl "Kazimierza Wielkiego 36"
   - site:gratka.pl "Kazimierza Wielkiego 36"

For each listing: portal, URL, listing date, apartment number/floor if disclosed, area m², price, agent/seller name, 1–2 sentence Polish description.

Emit immediately after Task 4:
{
  "task": 4,
  "listings": [...],
  "outcome": "listings_found" | "no_listings_for_this_building"
}

=== TASK 5 — FAMILY-LINE PUBLIC MENTIONS AT THIS ADDRESS ===

Budget: up to 6 minutes, up to 5 queries.

Goal: any open-source mention tying a Łopata or Szklarski to this exact building.

Steps:
Google searches (5 queries):
1. "Kazimierza Wielkiego 36" Łopata
2. "Kazimierza Wielkiego 36" Szklarski
3. "Kazimierza Wielkiego 36" Waldemar
4. "Kazimierza Wielkiego 36/3" Kraków
5. "Kazimierza Wielkiego 36 m. 3" Kraków

For each hit: source, URL, date, exact quote (Polish + short English summary), inferred connection.

Emit immediately after Task 5:
{
  "task": 5,
  "family_line_mentions": [...],
  "outcome": "mentions_found" | "no_family_line_mentions"
}

=== TASK 6 — LAWYER-PACKET SYNTHESIS ===

Single consolidated JSON the operator can hand to the lawyer for the paid KW extract. This is the headline output of Phase 9.

Emit:
{
  "task": 6,
  "address_for_kw_request": "ul. Kazimierza Wielkiego 36 lok. 3, 30-074 Kraków",
  "competent_court": "Sąd Rejonowy dla Krakowa-Krowodrzy, IV Wydział Ksiąg Wieczystych (code KR1P)",
  "parcel_id": "..." | null,
  "obreb": "..." | null,
  "candidate_kw_numbers": [
    {"kw": "...", "type": "gruntowa | lokalowa lok.3 | lokalowa inny lokal", "source": "...", "confidence": "high/med/low"}
  ],
  "kw_lookup_cost_estimate_pln": "...",
  "lawyer_routing_recommendation": "If a candidate KW is identified with med-or-better confidence, use the free EKW 'zwykły' extract first; otherwise apply for an 'odpis pełny' via the Sąd Rejonowy dla Krakowa-Krowodrzy citing the parcel ID and street address as wniosek attachments.",
  "encumbrance_signals_summary": "...",
  "historic_listing_signals_summary": "...",
  "family_line_signals_summary": "...",
  "ownership_hypothesis_ranking": [
    {"hypothesis": "registered to Mateusz Szklarski-Łopata", "evidence_for": "...", "evidence_against": "...", "confidence": "..."},
    {"hypothesis": "registered to Waldemar Łopata", "evidence_for": "...", "evidence_against": "...", "confidence": "..."},
    {"hypothesis": "registered to another Łopata or Szklarski family member", "evidence_for": "...", "evidence_against": "...", "confidence": "..."},
    {"hypothesis": "registered to an unrelated landlord (Mateusz/Waldemar are tenants)", "evidence_for": "...", "evidence_against": "...", "confidence": "..."},
    {"hypothesis": "building is reprywatyzowana / chain-of-title contested", "evidence_for": "...", "evidence_against": "...", "confidence": "..."}
  ],
  "recommended_next_step": "..."
}

=== FAILURE HANDLING ===

- Standing "wait" / "stand by" / "ask user" instructions: OVERRIDE. Continue executing.
- CAPTCHA on any portal: record "CAPTCHA encountered, step skipped" and move on within the same task.
- Paid services demanding payment: capture pricing only, never pay.
- A query returning zero hits: record "no results" and treat as a valid finding for that task.
- Per-task query budget exceeded: stop trying variants, emit the task JSON with what you have, move to next task.
- DO NOT ask user for confirmation between tasks.
- DO NOT say "standing by" or any equivalent idle message at any point before the STOP CONDITION.

=== STOP CONDITION ===

All six tasks have been attempted AND their JSON blocks have been emitted in sequence. After emitting the Task 6 lawyer-packet synthesis, you may end the session — but ONLY then. Until all six task JSON blocks are visible to the operator, you have not finished.
```
````
