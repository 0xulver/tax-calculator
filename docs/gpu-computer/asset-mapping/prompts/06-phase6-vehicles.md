# Phase 6 — Vehicles

Goal: identify any vehicles owned by or operationally linked to the debtor. Vehicles can be seized and auctioned by a komornik; ad listings can also reveal asset-stripping behaviour.

**Time:** 30–60 minutes of agent runtime.
**Cost:** 0 PLN.

Note: official owner-by-name lookup in CEPiK requires a formal request with Profil Zaufany login and is routed to the lawyer. This phase covers the OSINT path only.

Prerequisites: Phases 5 (operating address) sometimes surfaces a parking spot or photo of a branded vehicle. Run Phase 5 first if possible.

---

````
```prompt-for-browser-agent
You are looking for vehicles linked to a Polish JDG debtor. Use marketplace listings, business operational photos, and the official vehicle history portal (only if a registration plate or VIN has been obtained from OSINT).

=== SUBJECT ===
Full name: Mateusz Szklarski-Łopata
Trading as: GPUcomputer
NIP: 8661681248
REGON: 362678345
Registered address: ul. Mogilska 16 lok. 7, 31-516 Kraków
Phone (mobile): 883 109 779
Phone (landline): 12 333 77 30
Email: mateusz@gpucomputer.pl

If Phase 5 surfaced additional addresses (residential, workshop), use them too.

=== TASK 1 — OLX (CONSUMER MARKETPLACE) ===

Goal: find any vehicle (or high-value asset) listings tied to the debtor's name, business name, phone, or email.

1. Open https://www.olx.pl
2. In the main search bar ("Czego szukasz?" — What are you looking for?), run separate searches:
   - gpucomputer
   - GPU Computer Kraków
   - Mateusz Szklarski
   - 883109779 (phone — OLX sometimes accepts phone-number search)
3. For each results page, set "Filtry" → "Kategoria" (Filters → Category) to:
   - "Motoryzacja" (Automotive) for vehicles
   - "Elektronika" (Electronics) for hardware liquidation signals
4. For every relevant listing, extract: title, price, location, posting date, seller display name, any visible phone, any plate number visible in photos, listing URL.

Return Task 1 as JSON.

=== TASK 2 — OTOMOTO (VEHICLE-SPECIFIC MARKETPLACE) ===

1. Open https://www.otomoto.pl
2. Use the seller search if available. Otherwise use the main search:
   - gpucomputer
   - Mateusz Szklarski
3. Try the phone search: 883109779
4. For any matching listing extract: vehicle make/model, year, price, plate (if visible in photos), seller, location, listing URL.

Return Task 2 as JSON.

=== TASK 3 — ALLEGROLOKALNIE + ALLEGRO ASSETS ===

1. Open https://allegrolokalnie.pl
2. Search: gpucomputer / Mateusz Szklarski / 883109779
3. Also open https://allegro.pl and look for the seller's account listings — especially for high-value items being sold individually (computers, GPUs, equipment) at below-market prices, which would signal liquidation.

Return Task 3 as JSON.

=== TASK 4 — GOOGLE / STREET VIEW VEHICLE OSINT ===

Goal: branded delivery vehicles or business cars often appear in Street View near the operating address.

1. Open https://www.google.com/maps
2. Search for any non-virtual address surfaced in Phase 5. (If none, use the registered ul. Mogilska 16, 31-516 Kraków as a fallback — but expect nothing useful at a coworking building.)
3. Drop into Street View at the address. Pan around looking for:
   - Vehicles bearing "GPUcomputer" branding, logos, or website URL
   - Branded delivery vans
   - Cars parked consistently across multiple Street View dates
4. If any plate is readable, record it (Street View blurs plates by default but pattern-recognizable vehicles still help).

Return Task 4 as JSON: any address checked, any vehicle photographs captured, any plate fragments visible.

=== TASK 5 — HISTORIAPOJAZDU.GOV.PL (OFFICIAL VEHICLE HISTORY) ===

Goal: confirm vehicle history (insurance, inspections, accidents) for any plate or VIN found in Tasks 1–4.

PRE-CONDITION: a registration plate OR a VIN must be available. If neither was obtained, SKIP this task and report so.

For each plate/VIN obtained:

1. Open https://historiapojazdu.gov.pl
2. Find the three fields:
   - "Numer rejestracyjny" (Registration plate number)
   - "Numer VIN" (VIN)
   - "Data pierwszej rejestracji" (First registration date, format DD-MM-YYYY)
3. Enter the data. If first registration date is unknown, try common candidate years (2015–2024).
4. Click "Sprawdź pojazd" (Check vehicle).
5. Extract: make, model, year, fuel type, last inspection date, insurance status, insurance gaps, odometer history, accident/theft flags.

This portal does NOT reveal the current registered owner's name — that requires the formal CEPiK request (lawyer-routed).

Return Task 5 as JSON per plate/VIN.

=== TASK 6 — AUTOBAZA / AUTODNA (COMMERCIAL VIN-HISTORY) ===

Skip this unless explicitly authorized to spend ~49–99 PLN per VIN report. If authorized:

1. Open https://www.autodna.pl
2. Enter the VIN obtained from earlier tasks.
3. Note the price for the cheapest report tier.
4. STOP without purchasing — return the pricing summary and any free preview content.

Return Task 6 as JSON with pricing only unless purchase authorized.

=== OVERALL OUTPUT ===

Combined JSON with keys "task_1_olx", "task_2_otomoto", "task_3_allegrolokalnie", "task_4_google_streetview", "task_5_historiapojazdu", "task_6_commercial_vin_pricing", plus a top-level "summary_english" answering:
- Any vehicles confirmed linked to the debtor?
- Any signs of liquidation (high-value hardware being sold off)?
- Any plate/VIN obtained that warrants the lawyer-routed CEPiK formal request?

=== FAILURE HANDLING ===

- CAPTCHA on marketplaces: stop affected step, flag, continue.
- Login wall to see full phone numbers on OLX: capture what's public, do not log in.
- historiapojazdu.gov.pl with no plate/VIN: skip and report "No vehicle identifiers obtained".
- Do NOT contact any seller on any marketplace.

=== STOP CONDITION ===

All six tasks attempted. Return consolidated JSON.
```
````
