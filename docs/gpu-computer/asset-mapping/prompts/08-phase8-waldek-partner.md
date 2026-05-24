# Phase 8 — Waldek (Business Partner / Co-operator)

Goal: identify the second person embedded in GPUcomputer — the "Waldek" who controls `waldek@gpucomputer.pl` (configurations / sales) and was attached to the **+48 12 333 77 30** landline and the **+48 883 109 779** mobile in the 2019 `/o-nas` snapshot, alongside a second brand "3dkrakow". The debtor (Mateusz Szklarski-Łopata) has been resident in Eindhoven since October 2022 (Phase 7a). That means whoever is fielding inbound orders, configuring builds, talking to LeaseLink, and handling Kraków pickups is almost certainly Waldek — or someone working for him. This phase determines who Waldek is, what role he plays, whether he has his own assets/business footprint, whether he shares a surname (and possibly property) with Mateusz, and whether the "3dkrakow" brand is a separate live operation worth investigating.

Operational stakes:
- If Waldek is a **relative** (especially a parent — "Łopata" is the rarer half of the debtor's hyphenated surname and may belong to that side of the family), the Kazimierza Wielkiego 36/3 property surfaced in Phase 5 may belong to him, not Mateusz. Enforcement reach against a family-held property is materially different from reach against the debtor's own property.
- If Waldek is a **co-owner not on the JDG paperwork**, that's a nominee structure relevant to fraudulent-transfer (skarga pauliańska) analysis and to the criminal-track file in `docs/gpu-computer/crime-law/`.
- If Waldek runs **"3dkrakow"** as a separate active business, it is a candidate vehicle for inventory parking or revenue re-routing.
- If Waldek is just an **employee**, that still matters: it tells us GPUcomputer has a real, on-the-ground operator in Kraków, which strengthens Path A (Stay EPU) over Path B (Withdraw zabezpieczenie).

**Time:** 60–90 minutes of agent runtime.
**Cost:** 0 PLN.

---

````
```prompt-for-browser-agent
You are identifying a second person ("Waldek") embedded in a Polish JDG hardware retailer. The primary owner is a Polish national who has been living and working in the Netherlands since October 2022, so day-to-day Kraków operations are being run by someone else. Your job is to find out who Waldek is, his full legal name, his relationship to the owner, his role in the business, whether he runs any business of his own, and whether he is the real-world controller of the Kraków premises and the "3dkrakow" second brand. Passive browsing only — do not place orders, do not submit any form, do not contact anyone.

=== SUBJECTS ===

Primary debtor (already mapped — context only):
- Full name: Mateusz Szklarski-Łopata
- Trading as: GPUcomputer (JDG)
- NIP: 8661681248
- REGON: 362678345
- Current residence: Eindhoven, Netherlands (since Oct 2022)
- Polish registered address: ul. Mogilska 16/7, 31-516 Kraków (virtual office)
- Suspected real Kraków operating address: ul. Kazimierza Wielkiego 36 lok. 3, 30-074 Kraków

Target of THIS phase:
- Display name: "Waldek" (Polish diminutive — formal first name is almost certainly "Waldemar")
- Known email: waldek@gpucomputer.pl
- Role indicated on /kontakt and /o-nas pages: "Configurations" / "serwery i stacje" (server and workstation configuration)
- Phone numbers historically published alongside his email: +48 12 333 77 30 (Kraków landline) and +48 883 109 779 (mobile)
- Second brand mentioned next to him in the 2019 `/o-nas` snapshot: "3dkrakow"

Surname hypotheses to test (in priority order):
1. Łopata — matches the rarer half of the debtor's hyphenated surname → likely-relative hypothesis (father, uncle, brother)
2. Szklarski — matches the other half of the debtor's hyphenated surname → also relative
3. Other surname entirely → unrelated business partner / employee
4. Same hyphenation (Szklarski-Łopata) → sibling

=== TASK 1 — DIRECT PROFILE-FOR-WALDEK ON GPUCOMPUTER WEBSITE AND WAYBACK ===

Goal: extract any place where Waldek's full name, role, or contact information is published.

1. Open https://www.gpucomputer.pl/kontakt and https://www.gpucomputer.pl/o-nas
   Record every name, role, email, and phone listed for any person other than Mateusz. Capture exact Polish text.
2. Crawl the rest of the live site for any "Zespół" / "Team" / "O firmie" / "Pracownicy" / "Kontakt handlowy" / "Sprzedaż" subpage.
3. Open the Wayback Machine calendar for the domain:
   https://web.archive.org/web/*/gpucomputer.pl
   Open at least four snapshots spread across the years (2017, 2019, 2022, 2024) for each of `/kontakt`, `/o-nas`, `/zespol`, `/firma`, and the homepage. For every snapshot record:
   - Full name(s) shown for Waldek (any year may finally print his surname)
   - Role description
   - Direct phone (look for both landline 12-prefix and any mobile)
   - Email
   - Any photo (note presence, do not download)
4. Especially look for an older snapshot where the business may have been listed under a different legal name or partnership form — e.g., "Waldemar X i Mateusz Szklarski s.c." (civil-law partnership) which would be a major finding.

Return Task 1 as JSON:
{
  "waldek_full_name_found": "...",
  "waldek_role_text_pl": "...",
  "waldek_role_text_en": "...",
  "waldek_emails": [...],
  "waldek_phones": [...],
  "snapshots_reviewed": [{ "url": "...", "year": ..., "extract": "..." }],
  "older_legal_form_evidence": "..."
}

=== TASK 2 — REVERSE-PHONE LOOKUP ON THE KRAKÓW LANDLINE +48 12 333 77 30 ===

Goal: a Kraków landline is registered to a specific premises and (usually) a specific subscriber. If we can tie this number to a name or street address, that anchors Waldek geographically.

1. Run all of the following queries in a fresh Google session. Capture the top 10 results for each:
   - "12 333 77 30"
   - "+48 12 333 77 30"
   - "123337730"
   - "12 333 77 30" gpucomputer
   - "12 333 77 30" Kraków
   - "12 333 77 30" 3dkrakow
2. Open the following reverse-phone directories and search the number:
   - https://panoramafirm.pl (search the number directly)
   - https://www.pkt.pl
   - https://www.zumi.pl
   - https://www.google.com/maps/search/12+333+77+30
   - https://nomerogram.ru/numbers/pl/12333.html (Russian phone DB — sometimes catches what PL directories scrub)
3. For each hit, record: directory name, listed subscriber name, listed address, listed business category, date of listing if shown.
4. Special focus: if any directory lists a *different* business name at this landline (e.g., a different shop, a different person), capture that — this is the strongest single lead in this phase.

Return Task 2 as JSON listing every distinct (name, address, source) tuple found for the number.

=== TASK 3 — THE "3DKRAKOW" SECOND BRAND ===

Goal: 3dkrakow appeared next to Waldek's email in the 2019 about-us snapshot. Determine whether this brand has its own domain, its own legal owner, its own active commerce, and whether it points back to Waldek or to a third party.

1. Try each of these candidate domains and record HTTP status, page title, listed company name, NIP, and contact info:
   - https://www.3dkrakow.pl
   - https://3dkrakow.pl
   - https://www.3dkrakow.com
   - https://3dkrakow.com
   - https://www.3d-krakow.pl
   - https://3d-krakow.pl
2. For any domain that resolves:
   - Capture the full /kontakt, /o-nas, /regulamin pages — extract owner name, NIP, REGON, addresses, bank accounts, phones, emails.
   - Open the Wayback Machine for that domain and capture the same fields from the oldest available snapshot AND the most recent snapshot, to see if ownership changed hands.
3. Run the WHOIS lookups (free tiers only — do not pay):
   - https://www.dns.pl/cgi-bin/en_whois.pl (for .pl domains)
   - https://lookup.icann.org/lookup
   - https://who.is
   For each domain that resolves, record registrar, creation date, expiry, registrant if visible (will likely be redacted, but record that fact).
4. Run Google searches:
   - "3dkrakow" Mateusz
   - "3dkrakow" Waldek
   - "3dkrakow" NIP
   - "3dkrakow" Łopata
   - "3dkrakow" Szklarski
   - "3dkrakow" Kraków
5. Check CEIDG for any active or historic JDG named "3dkrakow" or "3D Kraków" or similar:
   https://aplikacja.ceidg.gov.pl/CEIDG/CEIDG.Public.UI/Search.aspx
6. Check KRS for any company with "3D" + "Kraków" or "3dkrakow" in its name:
   https://wyszukiwarka-krs.ms.gov.pl

Return Task 3 as JSON:
{
  "domains_tested": [{ "domain": "...", "resolves": true/false, "owner_identification": "..." }],
  "ceidg_match": "...",
  "krs_match": "...",
  "ownership_continuity_with_gpucomputer": "yes / no / inconclusive — explain",
  "is_3dkrakow_a_live_separate_business": "..."
}

=== TASK 4 — CEIDG NAME SEARCH FOR WALDEMAR ŁOPATA AND WALDEMAR SZKLARSKI ===

Goal: catch any independent JDG that Waldek runs. If he owns a separate JDG, his own NIP and address come out — and we then know whether that JDG operates from the same Kraków property.

1. Open https://aplikacja.ceidg.gov.pl/CEIDG/CEIDG.Public.UI/Search.aspx
2. Run each of the following name searches (Imię = first name, Nazwisko = surname). For each, capture every result with city = Kraków OR voivodeship = Małopolskie:
   - Imię: Waldemar / Nazwisko: Łopata
   - Imię: Waldemar / Nazwisko: Szklarski
   - Imię: Waldemar / Nazwisko: Szklarski-Łopata
   - Imię: Waldek / Nazwisko: Łopata    (CEIDG sometimes accepts diminutives)
   - Imię: Waldek / Nazwisko: Szklarski
3. For each match (Kraków/Małopolskie only), record: full name, NIP, REGON, business name, address, PKD codes, status (aktywna/zawieszona/wykreślona), date of entry into CEIDG, date of suspension/cessation if any. Flag any PKD overlap with 26.20.Z (computer production) or 46.51.Z (wholesale computer trade) or 47.41.Z (retail computer trade).

Return Task 4 as JSON with one entry per matched JDG.

=== TASK 5 — KRS / REJESTR.IO PERSON SEARCH FOR WALDEMAR ===

Goal: catch any sp. z o.o. or spółka cywilna where Waldek is a partner / director / proxy / beneficiary.

1. Open https://wyszukiwarka-krs.ms.gov.pl
   Run the same five name variants from Task 4 in the "Osoby" / person-search mode (if available). For each company returned, extract: company name, KRS number, NIP, role, dates, status, registered address, co-shareholders.
2. Open https://rejestr.io
   Search each of:
   - Waldemar Łopata
   - Waldemar Szklarski
   - Waldemar Szklarski-Łopata
   - 3dkrakow
   Free tier only.
3. Open https://crbr.podatki.gov.pl/adcrbr/#/
   If a name-only beneficial-owner search is offered, run the same three full-name variants. If PESEL/DOB is mandatory, record "blocked — needs PESEL" and skip.

Return Task 5 as JSON.

=== TASK 6 — SOCIAL MEDIA AND LINKEDIN PROFILE FOR WALDEK ===

Goal: find Waldek as a person — surname, photo, place of residence, employment history, age range. Especially valuable: any LinkedIn entry listing GPUcomputer as employer, since that will print his full surname.

1. LinkedIn search (do not log in — use public results only):
   - https://www.google.com/search?q=site:linkedin.com/in+gpucomputer+waldemar
   - https://www.google.com/search?q=site:linkedin.com/in+gpucomputer+waldek
   - https://www.google.com/search?q=site:linkedin.com/in+%22gpucomputer%22
   For each result, open the public preview and capture: full display name, headline, location, current employer, education, listed skills.
2. Facebook search:
   - https://www.facebook.com/search/people/?q=Waldemar+Łopata+Kraków
   - https://www.facebook.com/search/people/?q=Waldemar+Szklarski+Kraków
   - https://www.facebook.com/search/people/?q=Waldek+gpucomputer
   Capture display name, public city, public workplace, profile-photo presence (do not download).
3. Instagram, Twitter/X — light-touch only:
   - https://www.google.com/search?q=site:instagram.com+waldemar+łopata
   - https://www.google.com/search?q=site:x.com+waldemar+łopata+kraków
4. Cross-check any profile found against the email pattern `waldek@gpucomputer.pl` — see if the same person has used "waldek" as a username elsewhere.

Return Task 6 as JSON with one entry per candidate profile, ranked by confidence (high/medium/low) with the criterion stated.

=== TASK 7 — KAZIMIERZA WIELKIEGO 36 — PROPERTY OWNERSHIP HYPOTHESIS ===

Goal: test the hypothesis that the Kazimierza Wielkiego 36/3 address surfaced in Phase 5 is a family-held property registered to Waldek (or to a parent with the surname Łopata or Szklarski), not to Mateusz. We are not pulling KW extracts here — that's a Phase 2 / lawyer-routed action. We are doing OSINT context only.

1. Open https://www.google.com/maps/place/ul.+Kazimierza+Wielkiego+36,+30-074+Kraków
   Confirm the building type (kamienica / tenement / mixed-use) from Street View; capture any visible business/residential signage.
2. Run Google searches:
   - "Kazimierza Wielkiego 36" Łopata
   - "Kazimierza Wielkiego 36" Szklarski
   - "Kazimierza Wielkiego 36" Kraków lokal 3
   - "Kazimierza Wielkiego 36" Waldemar
   - "ul. Kazimierza Wielkiego 36/3" Kraków
3. Check whether the building or any apartment in it has appeared in real-estate listings (otodom, gratka, nieruchomosci-online, morizon). If so, capture the listing date, price, and any owner/agent name shown.
4. Check the publicly indexed PESEL-less name databases / death notices / obituaries (gazetawyborcza.pl/nekrologi, nekrologi.wyborcza.pl, nekrologi.net) for Łopata or Szklarski entries linked to Kraków / Krowodrza. (Sensitive — capture only what's already public.)

Return Task 7 as JSON. Be explicit that this does NOT establish title — only context.

=== TASK 8 — RELATIONSHIP HYPOTHESIS SYNTHESIS ===

Goal: combine everything from Tasks 1–7 into a single confidence-ranked statement about who Waldek is and what he is to Mateusz.

Produce a single JSON object:
{
  "waldek_full_legal_name": "...",
  "confidence": "high/medium/low",
  "evidence_basis": "...",
  "relationship_to_debtor": "father / uncle / brother / cousin / unrelated business partner / employee / unknown",
  "relationship_confidence": "...",
  "shared_address_with_debtor": "yes/no/unknown",
  "independent_business_footprint": "yes/no — details",
  "controls_3dkrakow_brand": "yes/no/unknown — details",
  "asset_recovery_implications": [
    "...",
    "..."
  ],
  "path_a_vs_path_b_impact": "..."
}

=== FAILURE HANDLING ===

- CAPTCHA on Google / Facebook / Instagram: flag and continue.
- Login walls: capture only public preview, never log in or create an account.
- Paid tier on rejestr.io / panoramafirm / pkt: capture free preview only.
- CRBR name search blocked by PESEL requirement: record and skip.
- WHOIS redactions: record "registrant redacted by registrar" and move on — do not pay for unmasking services.
- Do NOT contact Waldek, do NOT send email to waldek@gpucomputer.pl, do NOT call the landline.

=== STOP CONDITION ===

All eight tasks attempted. Return consolidated JSON with the Task 8 synthesis at the top level so the legal-team reader sees the headline answer first.
```
````
