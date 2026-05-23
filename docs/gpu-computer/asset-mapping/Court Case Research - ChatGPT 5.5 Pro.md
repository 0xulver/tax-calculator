# Asset and liability mapping plan for the GPUcomputer debt case

I treated the attached brief as the research specification: the goal is not to guess the debtor’s assets, but to produce a lawful, executable methodology for finding asset, liability, insolvency, and business-health signals before choosing between staying in EPU and moving to a regular lawsuit with *zabezpieczenie roszczenia*. 

Use these identifiers in every search, after verifying them against your official CEIDG extract:

* Debtor/person: **Mateusz Szklarski**
* Business: **MATEUSZ SZKLARSKI GPUCOMPUTER / GPUcomputer**
* NIP: **8661681248**
* REGON: **362678345**
* Registered address: **ul. Mogilska 16 lok. 7, 31-516 Kraków**
* Website: **gpucomputer.pl**

Those identifiers also appear in public business-index pages, but the CEIDG PDF should remain the authoritative source for execution. ([GoWork][1])

Do not use deception, fake buyer identities, social engineering, unauthorized access, or pressure on third parties. Treat screenshots and public-page extracts as investigation leads; for court use, your lawyer should obtain official extracts, certified copies, or evidence in a form acceptable to the court.

---

## A. Real estate ownership

### A1. Official Electronic Land and Mortgage Register — EKW

**Source / URL:** `https://ekw.ms.gov.pl/`
**Access status:** Open data only if you already have the KW number. No public name-based search.
**Cost:** Viewing is free; official extracts/certificates are paid.
**Accuracy / freshness:** Highest legal reliability once a KW number is known.
**Time to obtain:** Immediate after KW number is known.
**Caveats / risks:** Not useful for finding property from a name alone. KW numbers are treated as personal data in Polish data-protection practice, so commercial KW-number hunting should be purpose-limited and documented. The official EKW portal itself says you need the electronic KW number; if you do not know it, you obtain it from the land-and-mortgage division of the district court competent for the property location. ([Gov.pl][2])
**Skip if:** No KW number has been found from A2–A4 or from documents.

```prompt-for-browser-agent
Open https://ekw.ms.gov.pl/

Subject:
- Mateusz Szklarski
- Business: MATEUSZ SZKLARSKI GPUCOMPUTER
- NIP: 8661681248
- REGON: 362678345

1. On the homepage, look for and click "Przeglądanie księgi wieczystej" (Browse land and mortgage register).
2. If you do not have a KW number, stop immediately and return:
   "EKW cannot be searched by person name or address. KW number required."
3. If a KW number was provided by an earlier step, enter it into the KW-number fields. Polish labels may include:
   - "Kod wydziału" (court division code)
   - "Numer księgi wieczystej" (land and mortgage register number)
   - "Cyfra kontrolna" (check digit)
4. Click "Wyszukaj księgę" (Search register) or the equivalent search button.
5. If the page shows no register or an invalid number message, record the exact Polish error and translate it to English.
6. If the register opens, extract:
   - KW number
   - property type
   - address / cadastral parcel
   - owners and ownership shares from "Dział II" (Section II)
   - mortgages from "Dział IV" (Section IV)
   - warnings/claims from "Dział III" (Section III)
7. Translate all extracted fields to English.
8. Return results as JSON with keys:
   kw_number, property_address, owners, section_III_claims, section_IV_mortgages, screenshots_taken, caveats.

If CAPTCHA appears, stop and report "CAPTCHA blocking — needs human".
If the portal offers a paid official extract, do not buy it unless instructed; report the fee and document type.
```

---

### A2. MSIP Kraków and geoportal address/parcel triage

**Source / URLs:**
`https://msip.krakow.pl/`
`https://geoportal.gov.pl/`

**Access status:** Open map data for parcels/buildings; owner-level personal data is restricted.
**Cost:** Usually free for map triage; official EGiB documents cost extra.
**Accuracy / freshness:** Good for identifying parcels and administrative property context; not enough to prove ownership.
**Time to obtain:** 15–60 minutes for known addresses.
**Caveats / risks:** MSIP/geoportals may show parcels, buildings, ownership structure categories, and sometimes KW-related hints, but personal owner/rightholder data is usually restricted. Kraków MSIP describes EGiB as including land/building/local data and owners/rightholders, but access to personal data and some EGiB data is restricted or paid. ([Miejski System Informacji Przestrzennej][3])
**Skip if:** You have no candidate property address beyond the virtual office; still run once for the registered address to confirm virtual-office context.

```prompt-for-browser-agent
Open https://msip.krakow.pl/

Subject:
- Known registered address: ul. Mogilska 16 lok. 7, 31-516 Kraków
- Business: MATEUSZ SZKLARSKI GPUCOMPUTER
- NIP: 8661681248

1. Look for "Mapa" (Map), "Przejdź do mapy" (Go to map), or "MSIP Obserwatorium".
2. Open the map.
3. Use the search box labeled "Szukaj" (Search), "Adres" (Address), or similar.
4. Search for: "Mogilska 16 Kraków".
5. If the map finds the building, click the parcel/building.
6. Extract:
   - parcel number, if shown: "numer działki" (parcel number)
   - precinct: "obręb" (cadastral precinct)
   - address
   - any KW number, if visible
   - ownership category if shown, e.g. "struktura własności" (ownership structure)
   - whether the building appears to be a multi-tenant office or virtual-office location.
7. Do not attempt to bypass restricted personal-owner data.
8. Repeat the same process for any real operating address found in later steps.
9. Return results in English as JSON:
   address, parcel_number, precinct, kw_number_if_visible, ownership_category, notes, screenshots_taken.

If the map fails to load, try https://geoportal.gov.pl/ and search the same address.
If no parcel/KW data is visible, record "No public KW/owner data visible from map".
If login or paid EGiB access is required, stop and report exactly what is required.
```

---

### A3. Formal EGiB request to municipality/starostwo

**Source / institution:** EGiB — *Ewidencja Gruntów i Budynków*, municipality/starostwo competent for the property location. For Kraków: City of Kraków geodesy/EGiB office.
**Access status:** Restricted with legal-interest request; normally lawyer-assisted.
**Cost:** Usually tens of PLN per extract/map/document, calculated by the office.
**Accuracy / freshness:** High for cadastral and owner/rightholder data, but not a substitute for KW legal-title review.
**Time to obtain:** Several days to several weeks.
**Caveats / risks:** Documents without owner data may be available broadly, but extracts containing owners/rightholders require ownership, public authority status, operator status, or a documented legal interest and legal basis. A creditor’s claim may support legal interest, but a lawyer should frame it. ([Warszawa 19115][4])
**Skip if:** No candidate address/parcel has been found.

**Browser-agent prompt:** Not directly executable to completion because it may require identity, signature, attachments, and legal-interest proof. Use this handoff instead:

```prompt-for-browser-agent
Open the official website of the municipality/starostwo for the property address found earlier.

Goal:
Find the official procedure page for obtaining EGiB documents with owner/rightholder data for a parcel/address.

Subject:
- Creditor claim against Mateusz Szklarski / MATEUSZ SZKLARSKI GPUCOMPUTER
- NIP: 8661681248
- Candidate property address or parcel number: [insert from earlier step]

1. Search within the office website for:
   - "EGiB wypis z rejestru gruntów" (EGiB extract from land register)
   - "wypis i wyrys" (extract and map excerpt)
   - "interes prawny" (legal interest)
   - "właściciel" (owner)
2. Extract:
   - office name and department
   - exact procedure title
   - required form name
   - whether owner data is included
   - fee schedule
   - accepted submission methods: "osobiście" (in person), "pocztą" (post), "ePUAP", "Profil Zaufany"
   - required attachments proving legal interest
   - email/phone/contact page
3. Do not submit the application.
4. Return a lawyer handoff note in English:
   "EGiB request package needed: form, court claim/demand proof, proof of legal interest, fee, submission method."

If the site requires Profil Zaufany or login, stop and report "Formal signed request required — lawyer/client action needed".
```

---

### A4. Commercial KW/address/property-intelligence services

**Source / examples:** `https://ongeo.pl/`, `https://ksiegiwieczyste.pl/`, `https://hipoteki.pl/`, commercial real-estate intelligence providers.
**Access status:** Commercial; legality depends on purpose and processing basis.
**Cost:** Commonly about 20–150 PLN per address/report; broader reports cost more.
**Accuracy / freshness:** Variable. Useful lead generation, not court evidence.
**Time to obtain:** Immediate to 1 business day.
**Caveats / risks:** False positives and stale KW/address associations are possible. Use only for legitimate creditor investigation and verify all results through official EKW.
**Skip if:** You already have official KW numbers from EGiB, documents, or komornik.

```prompt-for-browser-agent
Open https://ongeo.pl/

Subject:
- Mateusz Szklarski
- Business: GPUcomputer
- Known registered address: ul. Mogilska 16 lok. 7, 31-516 Kraków
- Any real operating addresses found earlier: [insert]

1. Use the search field labeled "Adres" (Address), "Wpisz adres" (Enter address), or similar.
2. Search the registered address first: "Mogilska 16, Kraków".
3. Look for report options mentioning:
   - "księga wieczysta" (land and mortgage register)
   - "numer księgi wieczystej" (KW number)
   - "raport o nieruchomości" (property report)
   - "działka" (parcel)
4. Do not purchase automatically. Record:
   - available report types
   - price
   - whether the report claims to include KW number
   - whether payment/login is required.
5. Repeat for any non-virtual operating address found later.
6. If a low-cost report is available and the user has pre-authorized payment, buy only the address/KW report, not subscriptions.
7. If a KW number is obtained, immediately verify it in the official EKW portal.

Return:
- searched_address
- commercial_service
- price
- report_claims
- kw_number_if_obtained
- verification_status
- caveats.

If paywall appears, stop unless payment authorization was explicitly given.
If the service asks for personal data beyond email/payment, report and stop.
```

---

### A5. Komornik *zlecenie poszukiwania majątku* for real estate

**Source / institution:** Court bailiff — *komornik sądowy*.
**Access status:** Komornik-only after an enforcement title or after an enforceable security order, depending on procedural posture.
**Cost:** Statutory asset-search fee is commonly 100 PLN, plus advances and enforcement fees; confirm with the chosen bailiff.
**Accuracy / freshness:** High compared with OSINT; may query official systems, including bank, ZUS/US, CEPiK, and land-register-related databases.
**Time to obtain:** Days to weeks after the enforceable title/security order and application.
**Caveats / risks:** Not available now unless you obtain a usable title/order. This is one of the main practical reasons Path B may matter if you need speed. The official komornik guidance confirms a 100 PLN fee for asset search in the standard enforcement context. ([komornik.lubartow.pl][5])
**Skip if:** No enforceable title or security order exists.

```prompt-for-browser-agent
This step is not executable by a browser agent.

Prepare a lawyer/komornik handoff note:

"After obtaining an enforceable payment order, judgment, or enforceable security order, ask the komornik to perform 'zlecenie poszukiwania majątku' (asset search). The request should include searches for:
- OGNIVO bank accounts
- ZUS payer/employment data
- Urząd Skarbowy tax/refund data
- CEPiK vehicle data
- Centralna Baza Danych Ksiąg Wieczystych / real estate indicators
- debtor summons for asset disclosure.

Subject:
Mateusz Szklarski / MATEUSZ SZKLARSKI GPUCOMPUTER
NIP: 8661681248
REGON: 362678345
Known address: ul. Mogilska 16 lok. 7, 31-516 Kraków
Debt: 155,000 PLN plus costs/interest."

Stop condition:
Route to lawyer/komornik after court order. Do not attempt this through public web pages.
```

---

## B. Vehicle ownership

### B1. CEPiK formal data request

**Source / URL:** `https://www.gov.pl/web/gov/uzyskaj-dane-z-centralnej-ewidencji-pojazdow-i-kierowcow`
**Access status:** Restricted request with legal interest; online submission requires trusted/eID/qualified signature or postal filing.
**Cost:** 30.40 PLN for third-party data request; own data is free.
**Accuracy / freshness:** Official.
**Time to obtain:** Days to several weeks.
**Caveats / risks:** You cannot reverse-search vehicles from a name casually. The request must show a concrete legal interest and identify the person/vehicle as required by the form. Use lawyer assistance. ([Gov.pl][6])
**Skip if:** You are not ready to submit a formal signed request or you prefer to wait for komornik search.

```prompt-for-browser-agent
Open https://www.gov.pl/web/gov/uzyskaj-dane-z-centralnej-ewidencji-pojazdow-i-kierowcow

Goal:
Prepare, but do not submit, a CEPiK third-party data request checklist.

Subject:
- Mateusz Szklarski
- Business: MATEUSZ SZKLARSKI GPUCOMPUTER
- NIP: 8661681248
- REGON: 362678345
- Legal basis: creditor with documented 155,000 PLN civil claim; filed EPU case Nc-e 552126/26; pre-court demand delivered.

1. Read the page sections:
   - "Kto może uzyskać dane" (Who can obtain data)
   - "Co musisz przygotować" (What you must prepare)
   - "Ile zapłacisz" (How much you pay)
   - "Jak złożyć wniosek" (How to submit application)
2. Extract:
   - official form name
   - fee amount
   - payment account/instructions
   - whether "interes prawny" (legal interest) is required
   - whether Profil Zaufany/eID/qualified signature is required
   - postal address if postal submission is allowed
3. Do not file anything.
4. Return an English checklist for the lawyer/client.

If the page requires login before showing the form, report "Login/signature required".
If a PDF form is available, provide its title and what fields it asks for.
```

---

### B2. HistoriaPojazdu.gov.pl and commercial vehicle-history services

**Source / URLs:** `https://historiapojazdu.gov.pl/`, `https://www.autodna.pl/`, `https://www.autobaza.pl/`
**Access status:** Open only if you already know vehicle identifiers.
**Cost:** Official history is free; commercial VIN reports vary.
**Accuracy / freshness:** Official history is reliable for the queried vehicle; it is not an owner-name reverse search.
**Time to obtain:** Immediate.
**Caveats / risks:** Requires registration number, VIN, and first registration date for the public official service; commercial services generally cannot lawfully reverse-query owner by name. ([Gov.pl][7])
**Skip if:** No VIN/registration number is found from invoices, photos, social media, or listings.

```prompt-for-browser-agent
Open https://historiapojazdu.gov.pl/

Use only if a vehicle registration number, VIN, and first registration date have been found.

1. Click or locate fields labeled:
   - "Numer rejestracyjny" (Registration number)
   - "Numer VIN" (VIN number)
   - "Data pierwszej rejestracji" (Date of first registration)
2. Enter the known vehicle data exactly.
3. Click "Sprawdź pojazd" (Check vehicle).
4. Extract:
   - make/model
   - year
   - technical inspection status
   - insurance status
   - ownership/registration events if shown
   - whether any warning appears.
5. Return the report in English.

If any of the three required identifiers is missing, stop and return "Cannot query official vehicle history without registration number, VIN, and first registration date."
If CAPTCHA/login appears, report the blocker.
```

---

### B3. OLX/Otomoto/Allegro vehicle and equipment listing OSINT

**Source / URLs:** `https://www.olx.pl/`, `https://www.otomoto.pl/`, `https://allegro.pl/`, `https://allegrolokalnie.pl/`
**Access status:** Open/public listings.
**Cost:** Free unless paid archive tools are used.
**Accuracy / freshness:** Medium; listings can be deleted and seller names may not identify the debtor.
**Time to obtain:** 1–3 hours.
**Caveats / risks:** Do not contact sellers deceptively. Use only public pages and cached search results.
**Skip if:** No phone/email/username/address leads exist.

```prompt-for-browser-agent
Search public listing sites for vehicle or high-value equipment signals.

Subject search terms:
- "GPUcomputer"
- "gpucomputer.pl"
- "Mateusz Szklarski"
- "8661681248"
- "362678345"
- "Mogilska 16 Kraków"
- any phone/email found on invoices, website, or archived pages.

1. Open https://www.olx.pl/
2. Search each term above. Use category filters only if obvious:
   - "Elektronika" (Electronics)
   - "Motoryzacja" (Automotive)
   - "Komputery" (Computers)
3. Repeat at:
   - https://www.otomoto.pl/
   - https://allegro.pl/
   - https://allegrolokalnie.pl/
4. For each potential match, extract:
   - listing title
   - price
   - seller name/username
   - location
   - phone/email if publicly visible without contacting
   - listing date
   - URL
   - why it appears connected to the subject.
5. Do not message, call, or impersonate a buyer.
6. Return only matches with a clear connection, and mark weak matches as "unconfirmed".

If the site blocks scraping or shows CAPTCHA, stop and report.
```

---

### B4. Komornik CEPiK query

**Source / institution:** Komornik through standard asset search or enforcement activity.
**Access status:** Komornik-only after title/security order.
**Cost:** Part of asset-search/enforcement advances.
**Accuracy / freshness:** High.
**Time to obtain:** Days to weeks after instruction.
**Caveats / risks:** Not available for DIY pre-judgment OSINT.
**Skip if:** No enforceable title/security order.

```prompt-for-browser-agent
This step is not executable by a browser agent.

Prepare a komornik instruction:
"Please query CEPiK for vehicles registered to Mateusz Szklarski / MATEUSZ SZKLARSKI GPUCOMPUTER, NIP 8661681248, REGON 362678345, as part of asset search/enforcement."

Route to lawyer/komornik after an enforceable title or security order.
```

---

## C. Actual operating address / business premises

### C1. Official CEIDG / Biznes.gov verification

**Source / URL:** `https://www.biznes.gov.pl/` and CEIDG search
**Access status:** Open for public business data; filings require login.
**Cost:** Free.
**Accuracy / freshness:** Official for registered business status and disclosed addresses; does not prove actual operating premises.
**Time to obtain:** Immediate.
**Caveats / risks:** CEIDG may show only registered/correspondence addresses and not warehouse, workshop, or pickup locations.
**Skip if:** Never; use as baseline.

```prompt-for-browser-agent
Open https://www.biznes.gov.pl/

Subject:
- NIP: 8661681248
- REGON: 362678345
- Name: Mateusz Szklarski
- Business: GPUcomputer

1. Find the search function labeled "Wyszukiwarka firm" (Company search) or "Znajdź firmę" (Find a company).
2. Search first by NIP: 8661681248.
3. If no result, search by REGON: 362678345.
4. If still no result, search by name: "Mateusz Szklarski".
5. Open the matching CEIDG entry.
6. Extract:
   - full business name
   - NIP
   - REGON
   - status: "aktywny" (active), "zawieszony" (suspended), "wykreślony" (deleted)
   - start date
   - registered address
   - correspondence address
   - additional places of business, if any
   - PKD codes
   - insolvency/restructuring notes, if any
   - marital property note, if shown.
7. Translate to English and return as JSON.
8. Mark whether any address looks like a real operating location or only a virtual office.

If login is requested for public search, stop and report.
```

---

### C2. Wayback Machine snapshots of gpucomputer.pl

**Source / URL:** `https://web.archive.org/`
**Access status:** Open.
**Cost:** Free.
**Accuracy / freshness:** Good for historical pages; incomplete and sometimes missing scripts/images.
**Time to obtain:** 30–90 minutes.
**Caveats / risks:** Archived content is not proof that a location is current.
**Skip if:** Never; this is high signal-per-złoty.

```prompt-for-browser-agent
Open https://web.archive.org/

Target domain:
https://www.gpucomputer.pl/
Also test:
http://gpucomputer.pl/
https://gpucomputer.pl/

1. Enter "gpucomputer.pl" in the Wayback search field.
2. Review captures from 2015 to 2026, prioritizing:
   - 2026
   - 2025
   - 2024
   - captures around major website changes.
3. Open pages likely labeled:
   - "Kontakt" (Contact)
   - "O nas" (About us)
   - "Regulamin" (Terms)
   - "Dostawa" (Delivery)
   - "Serwis" (Service)
   - "Odbiór osobisty" (Personal pickup)
   - "Polityka prywatności" (Privacy policy)
4. Extract every address, phone, email, bank account number, company name, NIP, REGON, social link, pickup location, service location, and warehouse reference.
5. For each extracted item, record:
   - archived URL
   - capture date
   - original Polish text
   - English translation
   - whether it suggests a real operating address.
6. Return results as a timeline.

If an archived page is broken, try adjacent dates.
If no captures exist, return "No useful Wayback captures".
```

---

### C3. Current website legal, checkout, payment, and shipping pages

**Source / URL:** `https://www.gpucomputer.pl/`
**Access status:** Open public website.
**Cost:** Free.
**Accuracy / freshness:** High for current public claims, but website content can be misleading or stale.
**Time to obtain:** 30–60 minutes.
**Caveats / risks:** Do not place an order, pay money, or submit false information. Passive browsing only.
**Skip if:** Website is down; still record downtime.

```prompt-for-browser-agent
Open https://www.gpucomputer.pl/

Subject:
- GPUcomputer
- Mateusz Szklarski
- NIP: 8661681248

1. Browse public pages only. Do not create an account, do not place an order, do not pay.
2. Look for pages/menu items:
   - "Kontakt" (Contact)
   - "O nas" (About us)
   - "Regulamin" (Terms)
   - "Polityka prywatności" (Privacy policy)
   - "Dostawa" (Delivery)
   - "Płatności" (Payments)
   - "Serwis" (Service)
   - "Zwroty" (Returns)
   - "Koszyk" (Cart), but do not complete checkout.
3. Extract:
   - addresses
   - phone numbers
   - email addresses
   - bank account numbers
   - payment processor names, e.g. PayU, Przelewy24, Tpay
   - courier names
   - pickup/service/warehouse references
   - business terms showing responsible legal entity.
4. Test only whether products appear orderable by viewing product pages and cart availability. Do not submit a fake quote request.
5. Return a JSON object:
   current_status, pages_checked, contact_details, payment_details, addresses, orderability_signal, screenshots_taken, caveats.

If the site is down, record HTTP/browser error and timestamp.
If CAPTCHA appears, stop and report.
```

---

### C4. Reviews, business directories, and map mentions

**Source / URLs:** Google Maps, `https://www.gowork.pl/`, `https://aleo.com/pl`, `https://panoramafirm.pl/`, `https://www.pkt.pl/`, `https://www.ceneo.pl/`, `https://www.opineo.pl/`, Trustpilot, Wykop, Reddit.
**Access status:** Open/public.
**Cost:** Free.
**Accuracy / freshness:** Medium; useful for leads and complaint patterns, not dispositive proof.
**Time to obtain:** 2–4 hours.
**Caveats / risks:** Reviews can be fake, outdated, or misattributed.
**Skip if:** Never; high-value for finding real pickup/service addresses and current complaints.

```prompt-for-browser-agent
Search public reviews and directories for operating-address and complaint signals.

Search terms:
- "GPUcomputer"
- "GPU Computer"
- "gpucomputer.pl"
- "Mateusz Szklarski"
- "8661681248"
- "362678345"
- "GPUcomputer opinie"
- "GPUcomputer Kraków"
- "GPUcomputer Mogilska"
- "GPUcomputer zwrot" (refund)
- "GPUcomputer oszustwo" (scam)
- "GPUcomputer nie wysłał" (did not ship)
- "GPUcomputer reklamacja" (complaint/warranty)

1. Use Google search and site-specific searches for:
   - Google Maps
   - GoWork
   - Aleo
   - Panorama Firm
   - PKT.pl
   - Ceneo
   - Opineo
   - Trustpilot
   - Wykop
   - Reddit
   - Facebook public pages/groups only.
2. For each relevant result, extract:
   - platform
   - URL
   - date
   - author display name, if public
   - address mentioned
   - phone/email mentioned
   - complaint type: non-delivery, refund delay, warranty, pickup, service, other
   - exact Polish quote, maximum one or two short sentences
   - English translation
3. Separate:
   - "Address leads"
   - "Recent non-delivery/refund complaints"
   - "Positive current-operation signals"
   - "Weak/unconfirmed matches"
4. Do not message reviewers or join private groups.
5. Return the result as an English table.

If a platform requires login, only use publicly visible information and report "login required for more".
If the result is about a different company, mark "excluded — wrong entity".
```

---

### C5. Social media, job listings, and professional profiles

**Source / URLs:** LinkedIn, Facebook, Instagram, YouTube, TikTok, GitHub, Pracuj.pl, NoFluffJobs, JustJoin, Bulldogjob.
**Access status:** Public profile/listing data only.
**Cost:** Free to low-cost if using search tools.
**Accuracy / freshness:** Medium.
**Time to obtain:** 2–4 hours.
**Caveats / risks:** Do not friend/follow/message under a false identity.
**Skip if:** Never; run as OSINT.

```prompt-for-browser-agent
Search public social and job platforms only.

Subject terms:
- "GPUcomputer"
- "gpucomputer.pl"
- "Mateusz Szklarski"
- "8661681248"
- "362678345"
- "GPUcomputer Kraków"

1. Search Google for each term with:
   - site:linkedin.com
   - site:facebook.com
   - site:instagram.com
   - site:youtube.com
   - site:tiktok.com
   - site:github.com
   - site:pracuj.pl
   - site:nofluffjobs.com
   - site:justjoin.it
   - site:bulldogjob.pl
2. For each relevant public result, extract:
   - profile/page/listing URL
   - visible name
   - visible location
   - dates of recent activity
   - workplace/premises/address clues
   - employee/contractor names only if publicly tied to GPUcomputer
   - photos showing premises, vehicles, inventory, or trade events.
3. Do not log into private accounts unless the user already has their own account and the page is public to that account.
4. Do not contact anyone.
5. Return results grouped as:
   - confirmed business accounts
   - possible owner accounts
   - job listings
   - premises/inventory clues
   - weak matches.

If login wall blocks content, record the URL and blocker.
```

---

### C6. WHOIS, DNS, and historical infrastructure

**Source / URLs:** `https://viewdns.info/`, `https://securitytrails.com/`, DomainTools, `https://whois.domaintools.com/`, NASK WHOIS for `.pl`.
**Access status:** Some open, some paid.
**Cost:** Free to 100+ PLN/month depending on provider.
**Accuracy / freshness:** Useful for emails, historical IPs, hosting, and old DNS; personal registrant data often redacted.
**Time to obtain:** 30–90 minutes.
**Caveats / risks:** DNS hosting rarely proves asset ownership.
**Skip if:** No need for historical emails/servers.

```prompt-for-browser-agent
Investigate public DNS/WHOIS history for gpucomputer.pl.

1. Open https://viewdns.info/
2. Use tools:
   - "Reverse Whois" if available
   - "DNS Report"
   - "Reverse IP"
   - "IP History"
3. Search domain: gpucomputer.pl
4. Repeat at https://securitytrails.com/ if accessible without paid login.
5. Search NASK WHOIS for "gpucomputer.pl".
6. Extract:
   - registrar
   - name servers
   - historical IP addresses
   - MX/mail servers
   - public emails, if any
   - dates of changes
   - related domains, if clearly connected.
7. Return as English timeline.

If paid account is required, report the provider, data promised, and price; do not pay unless pre-authorized.
If registrant is redacted, record "registrant redacted".
```

---

## D. Bank accounts

### D1. VAT whitelist — *Biała lista podatników VAT*

**Source / URL:** `https://www.podatki.gov.pl/wykaz-podatnikow-vat-wyszukiwarka`
**Access status:** Open.
**Cost:** Free.
**Accuracy / freshness:** High for VAT registration and disclosed settlement accounts; data/API are updated daily/working-day cycle.
**Time to obtain:** Immediate.
**Caveats / risks:** Absence of an account does not mean absence of bank accounts. It may show only accounts reported for tax-settlement purposes. The public search supports NIP/REGON/name/account searches and shows VAT/account fields. ([Podatki Archive][8])
**Skip if:** Never; highest signal-per-złoty bank lead.

```prompt-for-browser-agent
Open https://www.podatki.gov.pl/wykaz-podatnikow-vat-wyszukiwarka

Subject:
- NIP: 8661681248
- REGON: 362678345
- Name: MATEUSZ SZKLARSKI GPUCOMPUTER

1. Locate the search form with fields such as:
   - "Numer NIP" (NIP number)
   - "REGON"
   - "Nazwa podmiotu" (Entity name)
   - "Numer konta" (Account number)
   - "Stan na dzień" (Status as of date)
   - button "Szukaj" (Search)
2. Search by NIP: 8661681248.
3. Set "Stan na dzień" (Status as of date) to today's date if required.
4. Click "Szukaj" (Search).
5. If no result, repeat by REGON: 362678345.
6. Extract:
   - taxpayer status: active/exempt/not registered
   - full name/entity name
   - NIP
   - REGON
   - address
   - bank account numbers shown
   - date checked
   - result/request identifier if displayed.
7. Repeat for historical relevant dates if the page allows:
   - 2026-01-01
   - 2026-04-08
   - today's date.
8. Return results as JSON and translate status labels to English.

If CAPTCHA appears, stop and report.
If the page says "Nie figuruje..." (does not appear), record exact message and date.
```

---

### D2. Invoices, website terms, archived pages, checkout/payment redirects

**Source / URLs:** Your own invoice/order emails; gpucomputer.pl; Wayback; payment pages.
**Access status:** Open or your own documents.
**Cost:** Free.
**Accuracy / freshness:** High if from invoice/payment instruction; medium if archived.
**Time to obtain:** 30–90 minutes.
**Caveats / risks:** A payment processor page may hide the merchant’s bank. Do not make a payment.
**Skip if:** Never; you likely have the original payment documents.

```prompt-for-browser-agent
Use only documents and pages lawfully available to the user.

Inputs:
- User's invoice/order confirmation/payment instruction, if provided
- https://www.gpucomputer.pl/
- Wayback snapshots of gpucomputer.pl

1. Review the user's invoice/order documents if available.
2. Extract any Polish bank account number ("numer rachunku", "rachunek bankowy", "konto bankowe").
3. Extract payment processor names: PayU, Przelewy24, Tpay, PayPal, Stripe, BLIK, bank transfer.
4. On current and archived website pages, search for:
   - "rachunek"
   - "konto"
   - "bank"
   - "przelew"
   - "płatność"
   - "regulamin"
5. If checkout pages are accessible, add a product to cart only if no payment/order is submitted.
6. Do not complete checkout or submit a fake order.
7. Return:
   - account_number
   - bank inferred from account prefix, if confidently known
   - source document/page
   - date of source
   - whether source is current or archived.

If payment would be required to reveal more, stop and report.
```

---

### D3. OGNIVO

**Source / institution:** KIR OGNIVO through komornik/public-sector access.
**Access status:** Not available to private creditors or browser agents. Komornik/court/public-sector use.
**Cost:** Komornik advance/fee; varies.
**Accuracy / freshness:** High for identifying Polish bank accounts during enforcement/security execution.
**Time to obtain:** Days after komornik instruction.
**Caveats / risks:** A creditor cannot directly use OGNIVO. Polish komornik templates and legal-practice materials commonly include OGNIVO among standard account-search tools. ([komornikrzeszow2.pl][9])
**Skip if:** No enforceable title/security order.

```prompt-for-browser-agent
This step is not executable by a browser agent.

Prepare this instruction for lawyer/komornik:
"After obtaining an enforceable title or enforceable security order, please use OGNIVO to identify all Polish bank accounts of Mateusz Szklarski / MATEUSZ SZKLARSKI GPUCOMPUTER, NIP 8661681248, REGON 362678345, and immediately seize/freeze accounts as permitted by the title/order."

Stop. Route to lawyer/komornik.
```

---

### D4. Commercial intelligence bank hints

**Source / examples:** Coface, Dun & Bradstreet Poland, Creditreform, KRD economic intelligence, local *biuro wywiadu gospodarczego*.
**Access status:** Commercial; some require a contract and legitimate interest.
**Cost:** Roughly 500–3,000 PLN per subject for a business-intelligence report; this range is also in your research brief. 
**Accuracy / freshness:** Medium; may identify bank/account clues from invoices, disclosures, or payment data, but cannot replace OGNIVO.
**Time to obtain:** 1–5 business days.
**Caveats / risks:** Ask explicitly whether bank-account hints are included and whether the report is GDPR-compliant.
**Skip if:** VAT whitelist and your own invoice already identify usable accounts and you are moving to komornik.

```prompt-for-browser-agent
Search for Polish business-intelligence providers that can produce a lawful report on a JDG debtor.

Subject:
- Mateusz Szklarski / MATEUSZ SZKLARSKI GPUCOMPUTER
- NIP: 8661681248
- REGON: 362678345

1. Search web for:
   - "wywiad gospodarczy NIP raport"
   - "Coface raport o firmie Polska"
   - "Creditreform raport o firmie"
   - "Dun Bradstreet Polska raport"
   - "KRD wywiad gospodarczy"
2. For each provider, extract:
   - product name
   - price or quote requirement
   - delivery time
   - whether JDG subjects are covered
   - whether bank-account/payment clues are included
   - whether English report is available
   - whether proof of legal interest is required.
3. Do not purchase.
4. Return a ranked shortlist of 3 providers.

If a provider requires a sales call, record contact details and stop.
```

---

## E. Other business interests, shareholdings, partnerships

### E1. Rejestr.io / commercial person-linked KRS search

**Source / URL:** `https://rejestr.io/`
**Access status:** Commercial/open hybrid.
**Cost:** Free snippets; paid subscriptions/reports for full person links.
**Accuracy / freshness:** Good for leads; verify all entities in official KRS/CRBR.
**Time to obtain:** 15–60 minutes.
**Caveats / risks:** Person-name matches can be false positives. Rejestr.io advertises searches by organization identifiers and linked persons, including person-name search. ([Rejestr.io][10])
**Skip if:** You already have a full official list of entities from lawyer/komornik.

```prompt-for-browser-agent
Open https://rejestr.io/

Subject search terms:
- "Mateusz Szklarski"
- "MATEUSZ SZKLARSKI GPUCOMPUTER"
- "8661681248"
- "362678345"
- "GPUcomputer"

1. Use the search field.
2. Search "Mateusz Szklarski".
3. Record all person/entity matches, but mark them unverified until official KRS/CRBR verification.
4. Search "8661681248" and "362678345".
5. For each entity result, extract:
   - entity name
   - KRS number
   - NIP
   - REGON
   - role of Mateusz Szklarski if shown: board member, shareholder, partner, proxy, beneficiary
   - dates of role
   - status: active, deleted, liquidation, insolvency.
6. Return a list of potential linked entities and the reason for each match.

If paid login is required for person links, report price/subscription and stop unless payment authorized.
```

---

### E2. Official KRS / PRS verification

**Source / URL:** `https://prs.ms.gov.pl/krs`
**Access status:** Open for entities; no account required for ordinary search/extracts.
**Cost:** Free for online extracts.
**Accuracy / freshness:** Official for KRS entities.
**Time to obtain:** Immediate once entity/KRS/NIP is known.
**Caveats / risks:** Official KRS is excellent for verifying entities but not always convenient for broad person-name searches. Shareholder details are not always visible for all company types in a way that solves asset control. The official KRS page says everyone can search the register and obtain current/full information without an account. ([Gov.pl][11])
**Skip if:** No linked KRS entities were found in E1 or other sources.

```prompt-for-browser-agent
Open https://prs.ms.gov.pl/krs

Verify entities found from Rejestr.io or other searches.

1. Look for "Wyszukiwarka KRS" (KRS search engine).
2. Search each known entity by:
   - "Numer KRS" (KRS number), if known
   - "NIP", if known
   - "REGON", if known
   - "Nazwa" (Name), if identifiers are missing.
3. Open the matching entity.
4. Download or view:
   - "Odpis aktualny" (current extract)
   - "Odpis pełny" (full extract), if available.
5. Extract:
   - entity name
   - KRS, NIP, REGON
   - status
   - registered address
   - management board
   - partners/shareholders if shown
   - proxies: "prokurenci"
   - insolvency/liquidation notes.
6. Specifically look for "Mateusz Szklarski" in roles.
7. Return translated summary and attach URLs/screenshots.

If no entity is found, record "No official KRS match".
```

---

### E3. CRBR — Central Register of Beneficial Owners

**Source / URL:** `https://crbr.podatki.gov.pl/`
**Access status:** Open for searches, but person search may require PESEL or birth-date data.
**Cost:** Free.
**Accuracy / freshness:** Official declarations, but depends on correctness of filings.
**Time to obtain:** Immediate for known entity identifiers.
**Caveats / risks:** Best used for linked companies found through KRS/Rejestr.io. CRBR is intended to disclose beneficial ownership, and official information says any person may access beneficial-owner identity data; declarations are submitted by authorized representatives under liability rules. ([Portal Podatkowy][12])
**Skip if:** No KRS/company entities linked to the debtor have been found.

```prompt-for-browser-agent
Open https://crbr.podatki.gov.pl/

Goal:
Check beneficial ownership for any linked companies found earlier.

1. Click "Wyszukaj" (Search) or "Rejestr CRBR" (CRBR register).
2. For each linked company, search by:
   - "NIP" (Tax ID), or
   - "KRS" (National Court Register number), or
   - "Nazwa" (Name), depending on available fields.
3. If the portal offers a beneficiary/person search, do not guess PESEL. Use only lawfully known identifiers.
4. Extract:
   - company name
   - NIP/KRS
   - beneficial owners: "beneficjenci rzeczywiści"
   - roles/control basis
   - dates of entries/updates
   - whether Mateusz Szklarski appears.
5. Translate to English and return JSON.

If the portal requires PESEL/date of birth not known to the user, stop and report "Person search requires identifiers not available".
If CAPTCHA/login appears, report blocker.
```

---

### E4. Public procurement, BIP, eZamówienia, and B2B traces

**Source / URLs:** `https://ezamowienia.gov.pl/`, BIP pages, OnePlace, business directories.
**Access status:** Public for tender/award notices; commercial aggregators may require login.
**Cost:** Free to paid.
**Accuracy / freshness:** Medium to high for formal awards; useful for customer/supplier relationships.
**Time to obtain:** 1–3 hours.
**Caveats / risks:** Absence of tenders does not indicate absence of business.
**Skip if:** Business appears purely consumer/retail and time is limited.

```prompt-for-browser-agent
Search public procurement and B2B sources.

Subject terms:
- "GPUcomputer"
- "MATEUSZ SZKLARSKI GPUCOMPUTER"
- "8661681248"
- "362678345"
- "Mateusz Szklarski"

1. Open https://ezamowienia.gov.pl/
2. Search notices for the subject terms.
3. Use Google for:
   - "GPUcomputer zamówienie publiczne"
   - "8661681248 BIP"
   - "362678345 BIP"
   - "GPUcomputer eZamówienia"
   - "GPUcomputer OnePlace"
4. Extract any:
   - tender participation
   - award notices
   - customer names
   - contract values
   - delivery addresses
   - dates
   - linked entities/partners.
5. Translate results to English and rank by relevance.

If a commercial aggregator requires payment, record price and stop.
```

---

## F. Other creditors and existing claims

### F1. KRZ — National Register of Debtors / insolvency and restructuring portal

**Source / URL:** `https://prs.ms.gov.pl/krz` or `https://krz.ms.gov.pl/`
**Access status:** Public portal is open/free for disclosed proceedings and notices; filing/party access requires account.
**Cost:** Free for public search.
**Accuracy / freshness:** Official for published entries, but absence of an entry does not prove no filing exists at the very earliest stage.
**Time to obtain:** Immediate.
**Caveats / risks:** Search by NIP, REGON, name, and business name. KRZ public access is described as free and public; it publishes disclosed bankruptcy/restructuring/enforcement information and notices. KRZ notices can include information that a bankruptcy/restructuring petition was entered into the court repertory, which can be an early warning signal. ([serwis-uslugirozwojowe.parp.gov.pl][13])
**Skip if:** Never; repeat weekly until decision.

```prompt-for-browser-agent
Open https://prs.ms.gov.pl/krz
If redirected, use https://krz.ms.gov.pl/

Subject:
- Mateusz Szklarski
- MATEUSZ SZKLARSKI GPUCOMPUTER
- GPUcomputer
- NIP: 8661681248
- REGON: 362678345

1. Find the public search area, often labeled:
   - "Portal Publiczny" (Public Portal)
   - "Wyszukiwarka" (Search engine)
   - "Tablica obwieszczeń" (Notice board)
   - "Postępowania" (Proceedings)
2. Search by NIP: 8661681248.
3. Search by REGON: 362678345.
4. Search by name: "Mateusz Szklarski".
5. Search by business name: "GPUcomputer".
6. For each hit, extract:
   - proceeding type: bankruptcy, restructuring, enforcement, ban, other
   - court
   - case reference
   - date of notice
   - debtor identifier
   - trustee/supervisor if shown
   - current status.
7. Look specifically for Polish terms:
   - "upadłość" (bankruptcy)
   - "restrukturyzacja" (restructuring)
   - "wniosek o ogłoszenie upadłości" (bankruptcy petition)
   - "postępowanie sanacyjne" (sanation proceeding)
   - "przyspieszone postępowanie układowe" (accelerated arrangement proceeding)
   - "postępowanie układowe" (arrangement proceeding)
   - "umorzenie" (discontinuance)
8. If no results, return "No KRZ public entries found for the searched identifiers as of [date/time]."

If login is required for detailed files, report "Public hit found but registered-user access required".
If CAPTCHA appears, stop and report.
```

---

### F2. MSiG — Monitor Sądowy i Gospodarczy

**Source / URL:** `https://emsig.ms.gov.pl/`
**Access status:** Open search.
**Cost:** Free for search; printed/certified materials may cost.
**Accuracy / freshness:** Official notices; especially useful for older or non-KRZ notices.
**Time to obtain:** 30–90 minutes.
**Caveats / risks:** Search interface fields include name, KRS, NIP, text-in-position, text-in-content, and announcement/case type. Run all identifiers. ([MSIG Wyszukiwarka][14])
**Skip if:** Never; run alongside KRZ.

```prompt-for-browser-agent
Open https://emsig.ms.gov.pl/

Subject search values:
- "Mateusz Szklarski"
- "MATEUSZ SZKLARSKI GPUCOMPUTER"
- "GPUcomputer"
- "8661681248"
- "362678345"

1. Locate the search form. Field labels may include:
   - "Nazwa podmiotu" (Entity name)
   - "Numer KRS" (KRS number)
   - "NIP" (Tax ID)
   - "Tekst w pozycji" (Text in item)
   - "Tekst w treści" (Text in content)
   - "Typ ogł./sprawy" (Announcement/case type)
2. Search by NIP: 8661681248.
3. Search by REGON/name in text fields if REGON field is absent.
4. Search exact name: "Mateusz Szklarski".
5. Search business name: "GPUcomputer".
6. For each result, extract:
   - issue/date
   - item number
   - court/entity
   - full notice text
   - notice type
   - whether it indicates bankruptcy, restructuring, liquidation, enforcement, summons, creditor notice, or company linkage.
7. Translate relevant notices to English.
8. Return results grouped by identifier used.

If no results, report "No MSiG results for [identifier]".
If a PDF opens, extract the relevant notice only, not the whole issue.
```

---

### F3. BIG / KRD / ERIF / BIG InfoMonitor / KBIG debt databases

**Source / URLs:**
`https://krd.pl/`
`https://www.big.pl/`
`https://erif.pl/`
`https://kbig.pl/`

**Access status:** Restricted/contractual. Checking and reporting debts depends on creditor status, documentation, debtor type, and legal basis.
**Cost:** Varies; individual reports and aggregator checks may be tens to hundreds of PLN; creditor accounts/contracts cost more.
**Accuracy / freshness:** Medium to high for debts reported to that specific BIG; false negatives are common because not all creditors report.
**Time to obtain:** Same day to several days.
**Caveats / risks:** For KRD business-debtor entry, statutory conditions include a business debtor, claim from a legal relationship, at least 500 PLN, at least 30 days overdue, and prior warning/demand naming the bureau. BIG InfoMonitor explains different routes for individuals and businesses, including that an individual creditor usually needs an enforceable judgment/title to report a debtor. ([info.krd.pl][15])
**Skip if:** You are not ready to create accounts/verify identity; still price-check first.

```prompt-for-browser-agent
Research debt-bureau checking/reporting options; do not register or submit debtor data yet.

Subject:
- Mateusz Szklarski / MATEUSZ SZKLARSKI GPUCOMPUTER
- NIP: 8661681248
- Debt: 155,000 PLN
- Creditor: private individual

1. Open:
   - https://krd.pl/
   - https://www.big.pl/
   - https://erif.pl/
   - https://kbig.pl/
2. For each, look for:
   - "Sprawdź firmę" (Check a company)
   - "Dopisz dłużnika" (Add debtor)
   - "Dla konsumentów" (For consumers)
   - "Dla przedsiębiorców" (For businesses)
   - "cennik" (price list)
   - "warunki dopisania dłużnika" (conditions for adding debtor)
3. Extract:
   - whether a private individual creditor can check a JDG by NIP
   - whether a private individual creditor can report the debtor before judgment
   - whether an enforceable title is required
   - minimum debt amount
   - overdue period
   - required warning letter wording
   - cost
   - delivery time.
4. Do not create an account and do not enter debtor data unless the site clearly offers a one-off public business report without submitting a debt.
5. Return an English comparison table.

If identity verification, contract, or payment is required, report exact requirement and stop.
```

---

### F4. Public court/litigation records

**Source / URLs:** Portal Informacyjny Sądów Powszechnych, SAOS, court judgment portals.
**Access status:** Portal Informacyjny is for parties/authorized users, not a general public defendant-name search. SAOS/judgment portals are public but often anonymized.
**Cost:** Usually free; lawyer time for authorized access.
**Accuracy / freshness:** Low for broad OSINT; high for your own case once linked.
**Time to obtain:** Minutes for open searches; days for account/authorization.
**Caveats / risks:** Do not expect a public by-name litigation history. Portal Informacyjny provides authorized remote access to court case information/documents rather than a broad public people search. ([warszawapraga.so.gov.pl][16])
**Skip if:** You only want public data and time is short.

```prompt-for-browser-agent
Search open judgment databases only; do not attempt unauthorized court-portal access.

Subject terms:
- "Mateusz Szklarski"
- "GPUcomputer"
- "8661681248"
- "362678345"

1. Search Google for:
   - "Mateusz Szklarski sąd"
   - "GPUcomputer sąd"
   - "8661681248 sąd"
   - "362678345 sąd"
2. Search SAOS or public judgment portals if available.
3. Extract only public results:
   - court
   - case number
   - date
   - party names if not anonymized
   - subject matter
   - link.
4. Do not infer identity from anonymized initials unless identifiers match.
5. Return "No reliable public litigation matches" if only anonymized/weak results appear.

If a Portal Informacyjny login page appears, stop and report "Authorized court-portal access only".
```

---

### F5. Licytacje komornicze

**Source / URL:** `https://licytacje.komornik.pl/`
**Access status:** Open public auction notices.
**Cost:** Free.
**Accuracy / freshness:** Good for listed auctions, but only shows assets already in auction.
**Time to obtain:** 15–45 minutes.
**Caveats / risks:** Absence of auction listing does not mean no enforcement proceedings. The portal publishes official bailiff auction notices across property and movable categories. ([Obwieszczenia Licytacji][17])
**Skip if:** Never; quick check.

```prompt-for-browser-agent
Open https://licytacje.komornik.pl/

Subject:
- Mateusz Szklarski
- GPUcomputer
- NIP: 8661681248
- REGON: 362678345
- Kraków
- Mogilska 16

1. Search the portal for:
   - "Szklarski"
   - "GPUcomputer"
   - "8661681248"
   - "Kraków"
2. Check categories:
   - "Nieruchomości" (Real estate)
   - "Ruchomości" (Movables)
   - vehicles/equipment categories if available.
3. For any result, extract:
   - auction type
   - debtor name if shown
   - asset description
   - location
   - estimated value
   - auction date
   - komornik name
   - case reference.
4. If no results, return "No public bailiff auction listings found as of [date/time]."
5. If the site links to the older OOL portal, follow it and repeat searches.

If search is unavailable, use site search via Google: site:licytacje.komornik.pl Szklarski GPUcomputer 8661681248
```

---

### F6. Rejestr Zastawów — registered pledges over movables/rights

**Source / URL:** `https://www.gov.pl/web/sprawiedliwosc/rejestr-zastawow`
**Access status:** Formal request; generally available through court/register process.
**Cost:** Official fees include roughly 10–20 PLN depending on information/extract/certificate type.
**Accuracy / freshness:** Official for registered pledges; does not cover unregistered security interests.
**Time to obtain:** Days to weeks unless e-service is available.
**Caveats / risks:** Need correct debtor identifiers and request type. Official fee page lists request types and fees for extracts/certificates/information. ([Gov.pl][18])
**Skip if:** No indication of financed equipment/vehicles/inventory and time is limited; otherwise low-cost useful check.

```prompt-for-browser-agent
Open https://www.gov.pl/web/sprawiedliwosc/rejestr-zastawow

Goal:
Prepare a Rejestr Zastawów request checklist for pledges registered against the debtor.

Subject:
- Mateusz Szklarski / MATEUSZ SZKLARSKI GPUCOMPUTER
- NIP: 8661681248
- REGON: 362678345

1. Locate information about:
   - "wniosek DW" forms
   - "odpis" (extract)
   - "zaświadczenie" (certificate)
   - "informacja" (information)
   - fees: "opłaty"
2. Extract:
   - correct form/request type for checking whether a debtor appears in the pledge register
   - fee amount
   - payment method
   - submission method
   - whether ePUAP/Profil Zaufany is required.
3. Do not submit the request.
4. Return an English checklist for lawyer/client.

If the request can be submitted online only after login/signature, report "Signed formal request required".
```

---

### F7. ZUS and Urząd Skarbowy arrears

**Source / institution:** ZUS, tax office, komornik queries.
**Access status:** Not generally public for a private creditor. Komornik/lawyer route after title/security or special legal basis.
**Cost:** Komornik/legal costs.
**Accuracy / freshness:** High if obtained officially.
**Time to obtain:** Days to weeks after authorized request.
**Caveats / risks:** Do not attempt to obtain tax/social-security information informally.
**Skip if:** No legal title/security or lawyer route.

```prompt-for-browser-agent
This step is not executable by a browser agent.

Prepare a professional handoff note:
"Ask lawyer/komornik whether ZUS and Urząd Skarbowy queries can be made after obtaining an enforceable title/security order. Objective: identify arrears, refunds, employer/payer data, and competing public-law creditors for Mateusz Szklarski / MATEUSZ SZKLARSKI GPUCOMPUTER, NIP 8661681248."

Stop. Route to lawyer/komornik.
```

---

## G. Operational signals / business health

### G1. Current commercial activity and orderability

**Source / URL:** `https://www.gpucomputer.pl/`
**Access status:** Open public pages only.
**Cost:** Free.
**Accuracy / freshness:** Good signal, but not conclusive.
**Time to obtain:** 30 minutes.
**Caveats / risks:** Do not send a fake quote request. If a test inquiry is needed, it should be truthful and sent by you or your lawyer, not by an agent pretending to be an ordinary customer.
**Skip if:** Website is offline; record downtime.

```prompt-for-browser-agent
Open https://www.gpucomputer.pl/

Goal:
Assess passive public signs of current trading without deception.

1. Check whether the website loads.
2. Record date/time.
3. Check:
   - product pages
   - stock/availability labels: "dostępny" (available), "brak" (unavailable), "na zamówienie" (on order)
   - cart function, but do not submit an order
   - contact page
   - recent blog/news/social links
   - terms/payment/shipping pages.
4. Extract whether the business appears to be accepting new orders.
5. Do not create a fake account, do not send a quote request, do not pay.
6. Return:
   - website_up: yes/no
   - orderability_signal: strong/medium/weak/none
   - evidence URLs
   - screenshots_taken
   - caveats.
```

---

### G2. Recent complaint monitoring

**Source / URLs:** Google, Wykop, Reddit, Facebook public content, Trustpilot, Opineo, Ceneo, GoWork, Allegro feedback.
**Access status:** Public content only.
**Cost:** Free.
**Accuracy / freshness:** Medium; strongest when multiple recent independent complaints align.
**Time to obtain:** 2–5 hours initially; then weekly monitoring.
**Caveats / risks:** Complaints are allegations, not proof.
**Skip if:** Never; it directly informs insolvency and competing-creditor risk.

```prompt-for-browser-agent
Search for recent complaints and non-delivery/refund reports.

Search terms:
- "GPUcomputer opinie"
- "GPUcomputer zwrot"
- "GPUcomputer reklamacja"
- "GPUcomputer nie wysłał"
- "GPUcomputer brak zwrotu"
- "GPUcomputer oszustwo"
- "gpucomputer.pl opinie"
- "Mateusz Szklarski GPUcomputer"
- "8661681248 opinie"

1. Use Google and platform searches.
2. Prioritize results from 2025 and 2026.
3. Extract:
   - platform
   - URL
   - date
   - complaint summary
   - whether complaint mentions non-delivery, refund, bankruptcy, supplier collapse, police, court, chargeback, or other creditors
   - exact short Polish phrase and English translation.
4. Group by month.
5. Flag clusters of 3+ complaints in a short period.
6. Do not contact complainants.

If private group/login required, record the group/page name only and do not join unless user instructs with a lawful reason.
```

---

### G3. Equipment-sale / asset-stripping signals

**Source / URLs:** OLX, Allegro, Allegro Lokalnie, Facebook Marketplace public listings, Elektroda, mining/hardware forums.
**Access status:** Public listings only.
**Cost:** Free.
**Accuracy / freshness:** Medium; seller attribution must be strong.
**Time to obtain:** 2–4 hours.
**Caveats / risks:** Selling inventory can be normal business, not necessarily asset stripping. Focus on distressed bulk sales, below-market liquidation, and sudden changes.
**Skip if:** No username/phone/email/address leads.

```prompt-for-browser-agent
Search public marketplace listings for liquidation or equipment-sale signals.

Search terms:
- "GPUcomputer"
- "gpucomputer.pl"
- "Mateusz Szklarski"
- "8661681248"
- any phone/email found from website/invoices
- "GPUcomputer RTX"
- "GPUcomputer komputer"
- "GPUcomputer serwer"
- "GPUcomputer mining"

1. Search OLX, Allegro, Allegro Lokalnie, public Facebook Marketplace results, and Google.
2. Look for:
   - bulk GPU sales
   - server/workstation liquidation
   - "likwidacja" (liquidation)
   - "wyprzedaż" (clearance sale)
   - "pilnie" (urgent)
   - repeated high-value items by same seller.
3. Extract only listings clearly linked by business name, phone, email, address, or unique branding.
4. Return:
   - listing URL
   - item
   - price
   - seller/location
   - date
   - linkage evidence
   - asset-stripping risk: low/medium/high.
5. Do not message sellers.
```

---

### G4. Traffic, SEO, and social activity trend

**Source / URLs:** Similarweb, Ahrefs free tools, SEMrush, Google indexed cache/search, social pages.
**Access status:** Open/free tiers; paid tiers optional.
**Cost:** Free to paid.
**Accuracy / freshness:** Approximate; useful trend signal only.
**Time to obtain:** 1–2 hours.
**Caveats / risks:** Low-traffic sites may have unreliable metrics.
**Skip if:** You already have stronger direct evidence.

```prompt-for-browser-agent
Assess public web-activity trend for gpucomputer.pl.

1. Open free traffic/SEO tools:
   - Similarweb website analysis
   - Ahrefs free website checker
   - SEMrush free domain overview, if available
2. Query domain: gpucomputer.pl
3. Extract:
   - estimated traffic trend
   - top countries
   - top pages/keywords if visible
   - last crawl/index clues
   - major drops or increases.
4. Search Google:
   - site:gpucomputer.pl
   - "gpucomputer.pl" after:2025-01-01
5. Check public social pages for last post/activity date.
6. Return a concise trend summary with caveat that these are estimates.
```

---

## H. Insolvency / restructuring deeper than KRZ

### H1. KRZ insolvency and restructuring repeat search

Use F1, but repeat weekly and immediately before any Path B filing.

**Additional search terms:**
`upadłość`, `restrukturyzacja`, `układ`, `sanacja`, `wniosek dłużnika`, `obwieszczenie`, `repertorium`.

**Why:** The debtor’s statement that he “filed for bankruptcy protection” could mean a real but not-yet-visible filing, a returned/defective filing, a restructuring idea, or a false/exaggerated statement. KRZ is the current public register, but the very earliest procedural state may not be obvious to a lay searcher. KRZ notices about a petition entering the repertory can be early warnings. ([WKB Lawyers][19])

```prompt-for-browser-agent
Repeat the KRZ search from F1, but focus only on insolvency/restructuring.

1. Search KRZ by:
   - NIP 8661681248
   - REGON 362678345
   - "Mateusz Szklarski"
   - "GPUcomputer"
2. In results, look for:
   - "wniosek o ogłoszenie upadłości" (bankruptcy petition)
   - "ogłoszenie upadłości" (declaration of bankruptcy)
   - "postępowanie restrukturyzacyjne" (restructuring proceeding)
   - "postępowanie sanacyjne" (sanation proceeding)
   - "układ" (arrangement)
   - "doradca restrukturyzacyjny" (restructuring adviser)
   - "syndyk" (trustee)
3. If a hit appears, extract full notice data and flag as urgent.
4. If no hit, return "No public KRZ insolvency/restructuring entry found as of [date/time]."
```

---

### H2. Historical MSiG insolvency/restructuring search

Use F2, with a focus on notices before KRZ’s current system and older publication practice.

**Access status:** Open.
**Cost:** Free.
**Accuracy / freshness:** Official for published notices; older data can be harder to search.
**Time to obtain:** 1–2 hours.
**Caveats / risks:** JDG personal insolvency and business notices may be split across name/NIP/business-name searches.
**Skip if:** Never; low cost.

```prompt-for-browser-agent
Open https://emsig.ms.gov.pl/

Focus on insolvency/restructuring terms.

1. Search each identifier:
   - "Mateusz Szklarski"
   - "GPUcomputer"
   - "8661681248"
   - "362678345"
2. In text fields, combine with:
   - "upadłość"
   - "restrukturyzacja"
   - "układ"
   - "sanacja"
   - "likwidacja"
3. Extract all matching notices.
4. Translate and classify:
   - bankruptcy
   - restructuring
   - enforcement
   - company linkage
   - unrelated.
5. Return "No historical MSiG insolvency notices found" only after all identifiers were searched.
```

---

### H3. Registered-user KRZ / lawyer monitoring

**Source / institution:** KRZ registered-user portal, lawyer access, bankruptcy court.
**Access status:** Requires account, signature, or party/attorney status.
**Cost:** Lawyer time.
**Accuracy / freshness:** Higher than public-only browsing once a proceeding exists or your claim is filed in that proceeding.
**Time to obtain:** Days.
**Caveats / risks:** Not a general private spy tool. Use only when a proceeding is found or lawyer has procedural basis.
**Skip if:** No public KRZ/MSiG signal and lawyer advises no basis.

```prompt-for-browser-agent
This step is not executable by a browser agent.

Prepare lawyer handoff:
"Please verify whether any bankruptcy or restructuring petition concerning Mateusz Szklarski / MATEUSZ SZKLARSKI GPUCOMPUTER, NIP 8661681248, is pending but not obvious from public KRZ search. If public KRZ hit exists, obtain registered-user access to case files/notices and advise whether art. 81 PU clawback risk affects planned zabezpieczenie."

Stop. Route to lawyer.
```

---

## I. Spousal asset situation

### I1. CEIDG marital-property notation

**Source / URL:** CEIDG/Biznes.gov entry.
**Access status:** Open if shown in CEIDG extract.
**Cost:** Free.
**Accuracy / freshness:** Official for declared CEIDG field, but it does not prove full marital status.
**Time to obtain:** Immediate.
**Caveats / risks:** “No community property” may mean unmarried, widow(er), divorced, or marital-property separation. Your attached brief already flags that CEIDG shows no community property. 
**Skip if:** Never; include in baseline.

```prompt-for-browser-agent
Use the CEIDG/Biznes.gov result from C1.

1. In the CEIDG entry, look for fields related to:
   - "wspólność majątkowa małżeńska" (marital community property)
   - "małżeńska wspólność majątkowa" (marital community property)
   - "rozdzielność majątkowa" (separation of property)
2. Extract the exact Polish wording.
3. Translate it to English.
4. Return:
   - field_present: yes/no
   - exact_wording
   - English_translation
   - caveat: CEIDG does not establish full marital history.
```

---

### I2. USC civil-status records

**Source / institution:** Urząd Stanu Cywilnego — civil registry office.
**Access status:** Restricted; spouse/close family/legal representative/person with legal interest/court/public authority may obtain extracts.
**Cost:** Administrative fee, plus lawyer time.
**Accuracy / freshness:** Official civil-status record.
**Time to obtain:** Days to weeks.
**Caveats / risks:** A creditor may need to show legal interest; this is lawyer territory. USC procedure pages require legal-interest documentation for third parties. ([Gov.pl][20])
**Skip if:** No evidence suggests spousal transfers or property.

```prompt-for-browser-agent
This step is not executable by a browser agent.

Prepare lawyer handoff:
"Assess whether creditor has 'interes prawny' (legal interest) to request USC records or other civil-status confirmation for Mateusz Szklarski, given 155,000 PLN claim and potential enforcement/spousal-asset issue. If yes, prepare formal request with proof of claim and legal basis."

Do not attempt to obtain civil-status data through informal sources.
```

---

### I3. No public matrimonial-property registry; KW/CEIDG/KRS clues only

**Source / institution:** Legal assessment via lawyer; KW/CEIDG/KRS documents.
**Access status:** No general public registry for matrimonial-property agreements.
**Cost:** Lawyer time.
**Accuracy / freshness:** Depends on documents found.
**Time to obtain:** Case-dependent.
**Caveats / risks:** Polish sources indicate there is no general registration system for matrimonial-property agreements; relevant clues may appear in CEIDG/KRS/KW depending on context. ([Orka2][21])
**Skip if:** No property/spouse issue appears.

```prompt-for-browser-agent
This step is not executable as a standalone registry search.

When KW, CEIDG, or KRS documents are found:
1. Search within each document for:
   - "wspólność ustawowa" (statutory community property)
   - "rozdzielność majątkowa" (separation of property)
   - "majątek osobisty" (personal property)
   - "małżonek" (spouse)
2. Extract exact Polish wording and translate.
3. Flag any property co-owned with a spouse or transferred to a spouse/family member.
4. Return to lawyer for analysis.
```

---

### I4. *Skarga pauliańska* — challenging transfers to family/third parties

**Source / legal route:** Civil Code art. 527 KC and lawyer investigation.
**Access status:** Court/lawyer route; OSINT can only identify suspicious transfers.
**Cost:** Lawyer/court costs.
**Accuracy / freshness:** Depends on evidence.
**Time to obtain:** Months to years if litigated.
**Caveats / risks:** Requires proof of debtor’s act harming creditors and statutory knowledge/bad-faith elements; family transfers can be especially relevant but must be evidenced. Polish legal materials describe art. 527 KC as a route for creditors harmed by transfers to third parties. ([Sip Lex][22])
**Skip if:** No transfer/property trail is found.

```prompt-for-browser-agent
Do not file anything. Prepare an evidence-triage note.

1. From KW/EGiB/KRS/CRBR/review/social findings, list any transfers after January 2026 involving:
   - spouse
   - family members
   - newly formed companies
   - affiliated entities
   - gifts/sales below market value.
2. For each, record:
   - asset
   - transfer date
   - transferor/transferee
   - source document
   - why timing may matter.
3. Return to lawyer under heading:
   "Possible skarga pauliańska evidence — unverified".

Do not accuse anyone; classify as investigation leads only.
```

---

## J. Foreign assets / asset-stripping risk

### J1. EU business-register search through e-Justice / BRIS and national registers

**Source / URL:** `https://e-justice.europa.eu/` business registers / BRIS.
**Access status:** Public search; some national documents are paid.
**Cost:** Free search to paid extracts.
**Accuracy / freshness:** Official or semi-official depending on national register.
**Time to obtain:** 1–4 hours for EU triage.
**Caveats / risks:** Name matches can be false positives; verify with identifiers, addresses, date of birth only if lawfully available. EU business registers are interconnected and searchable through the e-Justice/BRIS framework. ([e-justice.europa.eu][23])
**Skip if:** No foreign clues from website, invoices, supplier story, DNS, or social media.

```prompt-for-browser-agent
Open https://e-justice.europa.eu/

Subject terms:
- "Mateusz Szklarski"
- "GPUcomputer"
- "gpucomputer"
- "8661681248"
- "MATEUSZ SZKLARSKI GPUCOMPUTER"

1. Find the European business-register search / BRIS function.
2. Search by business name and person name where supported.
3. Prioritize countries suggested by evidence:
   - Poland
   - Hong Kong only through separate HK registry if supplier clues exist
   - Czech Republic
   - Slovakia
   - Germany
   - United Kingdom
   - Estonia/Lithuania/Netherlands if digital-business clues appear.
4. For each possible match, extract:
   - country
   - company name
   - register number
   - status
   - registered address
   - officers/shareholders if shown
   - source URL
   - strength of match: strong/medium/weak.
5. Return only matches with clear linkage or mark weak matches clearly.

If a country register requires payment, record price and document type; do not pay unless authorized.
```

---

### J2. Hong Kong supplier / foreign-company clue verification

**Source / URLs:** Hong Kong Companies Registry e-Search / ICRIS, OpenCorporates, supplier websites, invoice records.
**Access status:** Open to paid, depending on registry.
**Cost:** Free snippets to paid extracts.
**Accuracy / freshness:** Official if registry extract obtained.
**Time to obtain:** 1–3 hours for triage.
**Caveats / risks:** The debtor’s “Hong Kong supplier collapse” explanation is not enough to identify assets; this is for corroboration and linked-entity risk only.
**Skip if:** No supplier name, invoice, email domain, or foreign entity clue exists.

```prompt-for-browser-agent
Use this only if a Hong Kong supplier name, email domain, invoice, or company clue is available.

Inputs:
- Supplier/company name: [insert if known]
- Email/domain: [insert if known]
- Debtor statement about Hong Kong supplier collapse.

1. Search Google for the supplier/company name in quotes.
2. Search OpenCorporates for the supplier/company.
3. Search the Hong Kong Companies Registry e-Search / ICRIS if accessible.
4. Extract:
   - company name
   - registration number
   - status
   - incorporation/dissolution dates
   - directors/shareholders if publicly available
   - whether Mateusz Szklarski, GPUcomputer, or gpucomputer.pl appears.
5. Do not assume connection without documentary evidence.
6. Return:
   - corroborated_supplier_exists: yes/no/unclear
   - insolvency/dissolution signal
   - linkage evidence.

If registry payment is required, report price and stop.
```

---

### J3. Cross-border enforcement and European Account Preservation Order

**Source / legal route:** Brussels Ia Regulation; European Account Preservation Order — Regulation 655/2014.
**Access status:** Lawyer/court route.
**Cost:** Lawyer/court/enforcement costs; varies by country.
**Accuracy / freshness:** Legal procedure, not OSINT.
**Time to obtain:** Case-dependent.
**Caveats / risks:** Useful only if there is a credible foreign bank-account or asset lead. Regulation 655/2014 creates a procedure for preserving funds in a debtor’s bank account in another EU Member State, but it excludes some areas including insolvency and has procedural conditions. ([EUR-Lex][24])
**Skip if:** No foreign bank-account lead.

```prompt-for-browser-agent
This step is not executable by a browser agent.

Prepare lawyer handoff:
"Assess whether a European Account Preservation Order is available if evidence suggests Mateusz Szklarski / GPUcomputer holds bank accounts in another EU Member State. Identify target country, known/likely bank, debt amount, urgency, and relationship to Polish proceedings."

Stop. Route to cross-border enforcement lawyer.
```

---

### J4. Cryptocurrency wallet OSINT

**Source / URLs:** Website, invoices, payment pages, social media, public blockchain explorers.
**Access status:** Open only if wallet addresses are lawfully found.
**Cost:** Free to paid analytics.
**Accuracy / freshness:** Blockchain is accurate for transactions, but identity attribution is weak without off-chain evidence.
**Time to obtain:** 30 minutes to several hours after wallet discovery.
**Caveats / risks:** A wallet address alone does not prove ownership unless tied to invoice, website, email, or admitted payment channel.
**Skip if:** No wallet address or crypto payment method is found.

```prompt-for-browser-agent
Use only if a cryptocurrency wallet address is found on invoices, gpucomputer.pl, archived pages, or public social media.

1. Record the exact source of the wallet address.
2. Identify chain if obvious:
   - BTC
   - ETH/ERC-20
   - USDT/TRC-20
   - other.
3. Open the appropriate public blockchain explorer.
4. Extract:
   - wallet address
   - first seen date
   - last transaction date
   - current balance
   - high-level transaction volume
   - exchange deposit addresses if publicly labeled.
5. Do not claim the debtor owns the wallet unless the source ties it to GPUcomputer/Mateusz Szklarski.
6. Return:
   wallet, chain, source_linking_wallet_to_subject, balance, activity_summary, confidence.
```

---

# Recommended investigation plan

## First hour — zero-cost public registry and bank lead triage

Run these in order:

1. **C1 CEIDG/Biznes.gov baseline** — confirm status, addresses, PKD, marital-property field.
2. **D1 VAT whitelist** — extract all disclosed VAT settlement accounts and date-stamped status.
3. **F1/H1 KRZ** — search NIP, REGON, name, business name.
4. **F2/H2 MSiG** — search NIP, name, business name for historical insolvency/restructuring/enforcement notices.
5. **E1 Rejestr.io quick search** — look for linked companies/person roles.
6. **F5 Licytacje komornicze** — check whether assets are already in public auction.
7. **C3 current website** — identify current orderability, addresses, bank/payment clues.

**Immediate escalation trigger:** any KRZ/MSiG hit for *upadłość*, *restrukturyzacja*, *wniosek o ogłoszenie upadłości*, or multiple recent creditor complaints should go to your lawyer the same day.

---

## First day — OSINT expansion and low-cost paid checks

Run these after the first-hour baseline:

1. **C2 Wayback Machine** — historical contact, pickup, bank, terms, and warehouse clues.
2. **C4 reviews/directories** — address and creditor-complaint pattern.
3. **G2 complaint monitoring** — focus on 2025–2026 refund/non-delivery clusters.
4. **G3 marketplace/equipment-sale searches** — check asset-stripping signals.
5. **C5 social/job OSINT** — premises, staff, events, current activity.
6. **A2 MSIP/geoportal** — for registered address and any real address discovered.
7. **A4 commercial KW/address reports** — only for candidate real addresses, not random name fishing.
8. **E2 official KRS and E3 CRBR** — verify any linked entities found in E1.
9. **F6 Rejestr Zastawów checklist** — prepare low-cost formal check if equipment financing/pledges seem plausible.
10. **F3 BIG/KRD/ERIF/BIG InfoMonitor options** — compare access/cost; do not report the debtor until statutory conditions and warning-letter requirements are checked by counsel.

---

## First week — formal requests and professional escalation

1. **Lawyer review of all OSINT leads** — classify which are court-usable and which need certified documents.
2. **A3 EGiB requests** — only for specific candidate parcels/addresses.
3. **B1 CEPiK request** — if lawyer agrees your claim supports legal interest or if waiting for komornik is too slow.
4. **F6 Rejestr Zastawów request** — low-cost way to check registered pledges.
5. **D4 commercial intelligence report** — if public OSINT finds ongoing trade, bank hints, real address, or connected entities.
6. **Licensed detective** — if the key missing fact is actual premises/inventory/vehicle presence, and public searches stall.
7. **Path B decision memo** — lawyer compares evidence of liquid assets/competing creditors/insolvency risk against the 15–25k PLN expected incremental spend described in your brief. 

---

# Cost-effective stopping points

**0–300 PLN:** Complete public OSINT, VAT whitelist, KRZ/MSiG, current/archived website, reviews, licytacje, Rejestr.io snippets, and possibly one or two low-cost property/address checks. Stop DIY if you have no real address, no bank account beyond payment processor, no linked entities, and no fresh complaints.

**300–1,000 PLN:** Buy narrowly targeted reports only: commercial KW/address reports for real addresses, one business-intelligence snapshot, or debt-database checks. Do not keep buying broad reports unless each result produces a new actionable lead.

**1,000–3,000 PLN:** Commission a proper *biuro wywiadu gospodarczego* report if the debtor appears operational but assets remain unclear. This is usually better than more browser searching once public sources are exhausted.

**3,000 PLN+:** Move to lawyer-led evidence and procedural strategy. If the only asset path requires OGNIVO/CEPiK/ZUS/US/CBDKW, browser OSINT is no substitute for a title/security order and komornik.

**15,000–25,000 PLN Path B spend:** More justified if you find bank accounts, ongoing new-order intake, real premises/inventory, recent asset sales, multiple creditor complaints, or signs that other creditors are moving. Less justified if the only confirmed asset is stable real estate, or if KRZ/MSiG/BIG signals show advanced insolvency with no reachable assets.

---

# Red flags to look for

* **Insolvency/restructuring:** `wniosek o ogłoszenie upadłości`, `ogłoszenie upadłości`, `restrukturyzacja`, `postępowanie sanacyjne`, `przyspieszone postępowanie układowe`, `układ`, `syndyk`, `nadzorca sądowy`, `doradca restrukturyzacyjny`.
* **Enforcement pressure:** `licytacja komornicza`, `zajęcie wierzytelności`, `zajęcie rachunku bankowego`, `umorzenie egzekucji z powodu bezskuteczności`.
* **Asset stripping:** sudden marketplace sales of GPUs/workstations/servers, `likwidacja`, `wyprzedaż`, `pilnie sprzedam`, below-market bulk sales, disappearing product pages, removal of pickup/service address.
* **Competing creditors:** clusters of recent reviews mentioning `brak zwrotu`, `nie wysłał`, `oszustwo`, `wezwanie do zapłaty`, `policja`, `sąd`, `chargeback`.
* **Evasion signals:** address changes to virtual offices, website terms changing legal entity/payment account, linked new company with similar brand, spouse/family property transfers after January 2026.
* **Court-evidence gap:** leads exist only in screenshots/reviews but not in official extracts. Flag these as intelligence, not proof.

---

# Professional escalation map

**Kancelaria adwokacka / radca prawny**
Best for: Path A/B decision, *wniosek o zabezpieczenie*, formal EGiB/CEPiK/USC requests, bankruptcy-risk analysis, evidence admissibility.
Typical cost: hourly or fixed; your brief cites 5,000–8,000 PLN net lawyer fees plus court/enforcement costs for the contemplated Path B. 
Output language: Polish by default; bilingual counsel can provide English summaries.

**Komornik sądowy**
Best for: OGNIVO bank search, CEPiK, ZUS/US, real-estate database indicators, execution or security enforcement.
When: after enforceable title or enforceable security order.
Typical cost: asset-search fee/advances plus statutory enforcement fees.
Output language: Polish.

**Biuro wywiadu gospodarczego**
Best for: consolidated asset/liability/business-health report, linked entities, addresses, payment-risk indicators.
Typical cost: 500–3,000 PLN, 1–5 business days, matching the range in your brief. 
Output language: Polish; English summary may be available if requested.

**Detektyw licencjonowany**
Best for: lawful observation of actual premises, inventory, vehicles, delivery activity, and real operating address.
Typical cost: 200–500 PLN/hour, as noted in your brief. 
Output language: Polish report; English translation usually extra.

**Firma windykacyjna**
Best for: pre-enforcement negotiation, structured demands, BIG reporting workflows, settlement pressure.
Caution: ensure no unlawful pressure, harassment, or reputational-risk tactics. Use only firms comfortable with court-grade documentation.

**Notary/geodesist/property researcher**
Best for: KW/EGiB document handling once you have a property address/parcel.
Caution: they generally do not have a general lawful “search all property by person name” tool for private curiosity; use legal-interest route.

**Cross-border enforcement lawyer**
Best for: foreign bank/account leads, European Account Preservation Order, Brussels Ia enforcement, foreign company-register interpretation.
Use only after a concrete foreign lead appears.

[1]: https://www.gowork.pl/mateusz-szklarski-gpucomputer%2C23195872/dane-kontaktowe-firmy "https://www.gowork.pl/mateusz-szklarski-gpucomputer%2C23195872/dane-kontaktowe-firmy"
[2]: https://www.gov.pl/web/sprawiedliwosc/elektroniczna-ksiega-wieczysta "https://www.gov.pl/web/sprawiedliwosc/elektroniczna-ksiega-wieczysta"
[3]: https://msip.krakow.pl/dataset/1310 "https://msip.krakow.pl/dataset/1310"
[4]: https://warszawa19115.pl/-/wydawanie-wypisu-wypisu-i-wyrysu-wyrysu-z-ewidencji-gruntow-i-budynkow "https://warszawa19115.pl/-/wydawanie-wypisu-wypisu-i-wyrysu-wyrysu-z-ewidencji-gruntow-i-budynkow"
[5]: https://www.komornik.lubartow.pl/przepisy/20-poszukiwanie-maj%C4%85tku-d%C5%82u%C5%BCnika.html "https://www.komornik.lubartow.pl/przepisy/20-poszukiwanie-maj%C4%85tku-d%C5%82u%C5%BCnika.html"
[6]: https://www.gov.pl/web/cepik/wniosek-o-udostepnienie-danych "https://www.gov.pl/web/cepik/wniosek-o-udostepnienie-danych"
[7]: https://www.gov.pl/web/gov/sprawdz-historie-pojazdu "https://www.gov.pl/web/gov/sprawdz-historie-pojazdu"
[8]: https://podatki-arch.mf.gov.pl/wykaz-podatnikow-vat-wyszukiwarka/ "https://podatki-arch.mf.gov.pl/wykaz-podatnikow-vat-wyszukiwarka/"
[9]: https://komornikrzeszow2.pl/WNIOSEK%20EGZEKUCYJNY%20PDF.pdf "https://komornikrzeszow2.pl/WNIOSEK%20EGZEKUCYJNY%20PDF.pdf"
[10]: https://rejestr.io/ "https://rejestr.io/"
[11]: https://www.gov.pl/web/sprawiedliwosc/wyszukiwarka-krs1 "https://www.gov.pl/web/sprawiedliwosc/wyszukiwarka-krs1"
[12]: https://crbr.podatki.gov.pl/ "https://crbr.podatki.gov.pl/"
[13]: https://serwis-uslugirozwojowe.parp.gov.pl/component/content/article/84453%3Akrajowy-rejestr-zadluzonych-w-postepowaniach-restrukturyzacyjnych "https://serwis-uslugirozwojowe.parp.gov.pl/component/content/article/84453%3Akrajowy-rejestr-zadluzonych-w-postepowaniach-restrukturyzacyjnych"
[14]: https://wyszukiwarka-msig.ms.gov.pl/ "https://wyszukiwarka-msig.ms.gov.pl/"
[15]: https://info.krd.pl/Klient/Warunki-ustawowe "https://info.krd.pl/Klient/Warunki-ustawowe"
[16]: https://warszawapraga.so.gov.pl/artykul/171/114/portal-informacyjny-sadow-powszechnych "https://warszawapraga.so.gov.pl/artykul/171/114/portal-informacyjny-sadow-powszechnych"
[17]: https://licytacje.komornik.pl/ "https://licytacje.komornik.pl/"
[18]: https://www.gov.pl/web/sprawiedliwosc/udzielanie-informacji-z-rejestru-zastawow2 "https://www.gov.pl/web/sprawiedliwosc/udzielanie-informacji-z-rejestru-zastawow2"
[19]: https://wkb.pl/wkb-legal-alert-postepowania-upadlosciowe-i-restrukturyzacyjne-od-1-grudnia-2021-tylko-elektronicznie/ "https://wkb.pl/wkb-legal-alert-postepowania-upadlosciowe-i-restrukturyzacyjne-od-1-grudnia-2021-tylko-elektronicznie/"
[20]: https://www.gov.pl/web/gov/uzyskaj-odpis-aktu-stanu-cywilnego-urodzenia-malzenstwa-zgonu "https://www.gov.pl/web/gov/uzyskaj-odpis-aktu-stanu-cywilnego-urodzenia-malzenstwa-zgonu"
[21]: https://orka2.sejm.gov.pl/INT7.nsf/main/7878F294 "https://orka2.sejm.gov.pl/INT7.nsf/main/7878F294"
[22]: https://sip.lex.pl/akty-prawne/dzu-dziennik-ustaw/kodeks-cywilny-16785996/art-527 "https://sip.lex.pl/akty-prawne/dzu-dziennik-ustaw/kodeks-cywilny-16785996/art-527"
[23]: https://e-justice.europa.eu/topics/registers-business-insolvency-land/business-registers-search-company-eu_en "https://e-justice.europa.eu/topics/registers-business-insolvency-land/business-registers-search-company-eu_en"
[24]: https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX%3A32014R0655 "https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX%3A32014R0655"
