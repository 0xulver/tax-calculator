# Phase 5 — Operating Address Reconnaissance

Goal: find where the business actually operates. The registered address (Mogilska 16 lok. 7) is a virtual office shared by multiple unrelated firms. A 10-year-old hardware business assembling and shipping custom PCs must have a real workshop, warehouse, or pickup point somewhere. Finding it adds enforceable inventory locations and a real residential address candidate for Phase 2.

**Time:** 60–120 minutes of agent runtime.
**Cost:** 0 PLN.

---

````
```prompt-for-browser-agent
You are looking for the real (non-virtual) operating address of a Polish JDG: workshop, warehouse, pickup point, or owner's residence. Use historical website snapshots, customer reviews on marketplace platforms, business directories, and DNS/WHOIS infrastructure. Passive observation only — do not place orders, do not contact the seller or any reviewer.

=== SUBJECT ===
Full name: Mateusz Szklarski-Łopata
Trading as: GPUcomputer
NIP: 8661681248
REGON: 362678345
Registered address (virtual): ul. Mogilska 16 lok. 7, 31-516 Kraków (operated by WorkDesk virtual office at https://workdesk.pl — definitively NOT a real operating premises)
Known historical address: ul. Kazimierza Wielkiego 36 lok. 3, 30-074 Kraków (from older business directories — high-probability candidate for the real earlier workshop/residence)
Website: https://www.gpucomputer.pl/
Phone (mobile): 883 109 779
Phone (landline): 12 333 77 30
Email: mateusz@gpucomputer.pl

=== TASK 1 — WAYBACK MACHINE (ARCHIVED gpucomputer.pl) ===

Goal: capture historical "Kontakt", "O nas", "Regulamin", and checkout pages that may show a real pickup address or earlier business address.

1. Open https://web.archive.org/web/*/gpucomputer.pl/*
2. The calendar view shows captures across years. Sample one capture per year from 2015 through 2026, and prioritize the most recent capture available.
3. For each sampled capture, navigate within the archived site to:
   - "Kontakt" (Contact)
   - "O nas" (About us)
   - "Gdzie jesteśmy" (Where to find us) — if exists
   - "Dostawa" (Delivery)
   - "Odbiór osobisty" (Personal pickup)
   - "Serwis" (Service)
   - "Regulamin" (Terms of service)
   - "Polityka prywatności" (Privacy policy)
4. Extract from each page:
   - All physical addresses
   - All phone numbers
   - All email addresses
   - All bank account numbers (IBANs)
   - Any references to a workshop, pickup point, warehouse
   - NIP / REGON if shown
5. Specifically flag any address that is NOT "Mogilska 16" — that's likely a real operational location.

Return Task 1 as a chronological JSON timeline:
{
  "snapshots": [
    {
      "snapshot_date": "...",
      "page": "...",
      "addresses_found": [...],
      "phones_found": [...],
      "emails_found": [...],
      "bank_accounts_found": [...],
      "english_summary": "..."
    }
  ],
  "non_mogilska_addresses": [...]
}

=== TASK 2 — GOOGLE MAPS + PHONE TRACE ===

Goal: find the listed Google Maps location, scan reviews for location clues, and reverse-search the phone number to see what address Google associates with it.

1. Open https://www.google.com/maps
2. Search: GPUcomputer Kraków
3. If a business listing appears, extract address, phone, hours, website, rating, and all reviews (up to 50 most recent).
4. Scan reviews for any mention of pickup at an address other than Mogilska 16, a workshop, a "showroom", a warehouse.
5. Also search:
   - Mateusz Szklarski Kraków
   - 883 109 779 (the phone)
   - 12 333 77 30 (the landline)
6. For the phone-number searches, the map may return an associated business or residential pin.

Return Task 2 as JSON including all reviews with English translations and any non-Mogilska address surfaced.

=== TASK 3 — ALLEGRO / CENEO / OPINEO SELLER PROFILES ===

Goal: marketplace seller profiles often show declared shipping addresses, service points, and reviewer comments mentioning real pickup locations.

1. Open https://allegro.pl
2. Search for: gpucomputer — also: Mateusz Szklarski
3. Click any matching seller account. Extract: seller name, member-since date, feedback count, listed address, city, suspension/warning notices.

4. Open https://www.ceneo.pl
5. Search: gpucomputer — also: gpucomputer.pl
6. For any shop entry, click through and extract: shop address, phone, rating, all reviews.

7. Open https://www.opineo.pl
8. Search: gpucomputer.pl
9. Extract: shop address, all reviews, dates.

10. Also try https://allegrolokalnie.pl — search the same terms.

For all platforms: read reviews specifically looking for:
- "Odbiór osobisty" (personal pickup) at a specific address
- Mentions of a workshop, "warsztat", "biuro", "salon", "siedziba"
- Distance / location complaints (e.g. "trzeba jechać do…" = had to drive to…)
- Asset-stripping or distress-sale signals

Return Task 3 as JSON with platform-by-platform breakdown.

=== TASK 4 — POLISH BUSINESS DIRECTORIES (with known direct URLs) ===

Goal: directories often cache historical addresses or list a different real address than CEIDG. Several direct profile URLs are already known for this debtor — go to those first, then search the others by name/NIP/phone as fallback.

DIRECT URLs (visit each, extract all visible data):

1. Targeo (NIP lookup): https://mapa.targeo.pl/8661681248/nip/firma
2. Targeo (address profile): https://mapa.targeo.pl/mateusz-szklarski-lopata-ul-mogilska-16-31-516-krakow~17142128/przedsiebiorstwo-firma/adres
3. Firma Godna Zaufania: https://www.firmagodnazaufania.pl/company,50850,mateusz-szklarski-lopata-gpucomputer
4. KRS-Online (indexes JDG too): https://www.krs-online.com.pl/firma/5516506-mateusz-szklarski-lopata-gpucomputer
5. Panorama Firm: https://panoramafirm.pl/ma%C5%82opolskie,,krak%C3%B3w,grzeg%C3%B3rzki,mogilska,16_lok._7/mateusz_szklarski_lopata_gpucomputer-zjpkzc_fnd.html

For each direct URL, extract: full business name, NIP, REGON, all addresses (current and historical), phone numbers, email, description, reviews, any badge/certification, page last-updated date if visible.

SEARCH-BASED fallback — open each and search by "GPUcomputer", NIP 8661681248, phone 883109779:

6. https://www.pkt.pl
7. https://aleo.com/pl
8. https://www.gowork.pl

For each, extract the same fields.

Return Task 4 as JSON, one entry per directory. Specifically flag any address other than Mogilska 16 or Kazimierza Wielkiego 36 — that would be a third, undocumented address.

=== TASK 5 — WHOIS / DNS / HOSTING HISTORY ===

Goal: find the domain registrant and any historical infrastructure that could reveal an additional email/address.

1. Open https://www.dns.pl/en/whois
   Search: gpucomputer.pl
   Extract: registrant name, registrant organization, registrant address, registrant email, name servers, registration date, expiry date.
   If "REDACTED FOR PRIVACY" record that.

2. Open https://www.whois.com/whois/gpucomputer.pl
   Extract any extra data the NASK WHOIS didn't show.

3. Open https://viewdns.info
   Run these tools for "gpucomputer.pl":
   - "Reverse Whois Lookup"
   - "IP History"
   - "Reverse IP" — to see other domains hosted on the same IP (could reveal sister sites operated by the same person)
   - "DNS Report"
   Extract all results.

4. Open https://securitytrails.com/domain/gpucomputer.pl
   If accessible without payment, capture historical DNS records. If login required, record "Login required" and stop that subtask.

Return Task 5 as JSON.

=== TASK 6 — SOCIAL MEDIA OPERATIONAL FOOTPRINT ===

Goal: posts often include location tags or photos that reveal real workshop premises.

1. Open https://www.facebook.com/search/pages/?q=gpucomputer
   Click any matching page. Extract: page name, follower count, last post date, About section (address, phone, founding date). Scan most recent 20 posts for location tags, photos of premises, distress signals (bankruptcy mentions, supplier complaints, asset sales).

2. Open https://www.facebook.com/search/people/?q=mateusz%20szklarski
   Note any public profile. Capture only publicly visible posts. Look for:
   - Workplace listed
   - Location tags
   - Photos that could show a workshop/warehouse
   - Travel or distress signals

3. Search https://www.linkedin.com/search/results/people/?keywords=Mateusz%20Szklarski%20GPUcomputer
   For any matching profile, capture: current employer, location, education, recent posts. Login wall: extract only what's public.

4. Search https://www.instagram.com/explore/tags/gpucomputer
   And https://www.tiktok.com/search?q=gpucomputer
   Capture any media with location/equipment clues.

Return Task 6 as JSON.

=== OVERALL OUTPUT ===

Combined JSON with keys "task_1_wayback", "task_2_google_maps", "task_3_marketplace_reviews", "task_4_directories", "task_5_whois_dns", "task_6_social_media", plus a top-level "summary_english" answering:
- Any non-Mogilska, non-Kazimierza-Wielkiego physical addresses surfaced?
- Any candidate residential address for the owner?
- Any signals the business is still operating physically?
- Any photos showing premises and assets?

=== CLIENT-ACTION NOTE (not for the browser agent) ===

A high-value step a browser agent cannot perform: the creditor (Magnus) should personally review their own email archive for any package-shipment notifications from the original GPUcomputer order. Polish couriers (InPost, DPD, DHL, GLS) routinely disclose the origin address or the specific automated parcel locker (Paczkomat) from which a package was first dispatched. A consistent dispatch origin in a Kraków residential or industrial district strongly indicates the debtor's real workshop or residence is within a short radius of that locker. If found, feed the address back into Phase 2 and re-run real-estate lookups for it.

=== FAILURE HANDLING ===

- Login walls (Facebook, LinkedIn, Instagram, TikTok): capture public preview only, do not log in.
- CAPTCHA: flag and continue.
- Site offline: record timestamp, continue.
- Do NOT message any reviewer, page admin, or seller.
- Do NOT impersonate a buyer or pose as a customer to extract information.

=== STOP CONDITION ===

All six tasks attempted. Return consolidated JSON.
```
````
