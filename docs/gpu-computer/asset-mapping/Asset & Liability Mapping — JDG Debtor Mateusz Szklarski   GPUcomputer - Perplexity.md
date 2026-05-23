# Asset & Liability Mapping — JDG Debtor Mateusz Szklarski / GPUcomputer

**Prepared for:** Private individual creditor — 155,000 PLN claim, EPU case Nc-e 552126/26  
**Debtor:** Mateusz Szklarski (trading as "GPUcomputer" / "Mateusz Szklarski-Łopata Gpucomputer")  
**NIP:** 8661681248 | **REGON:** 362678345 | **Address on file (virtual office):** ul. Mogilska 16 lok. 7, 31-516 Kraków  
**Date of this brief:** May 2026  

***

## Preliminary Note on Legal Architecture

A JDG (jednoosobowa działalność gospodarcza) carries unlimited personal liability — the debtor's private and business assets are legally unified. No corporate veil exists. Every source below therefore targets Mateusz Szklarski as a natural person, not a corporate entity. The enforcement title (*tytuł wykonawczy*) is not yet in hand; therefore the komornik's OGNIVO/bank-query and formal *zlecenie poszukiwania majątku* channels are unavailable today but are described fully for use once a *nakaz zapłaty* or *postanowienie o zabezpieczeniu* is obtained.[^1][^2]

**Critical bankruptcy-clawback note:** Under art. 127 §3 of the Polish Insolvency Law (*Prawo upadłościowe*), any *zabezpieczenie* (precautionary attachment) obtained within **two months** before the date a bankruptcy petition is filed is automatically void (*bezskuteczne z mocy prawa*) in relation to the bankruptcy estate. This is the core risk of Path B. The debtor claims he "filed for bankruptcy protection," but no KRZ entry has appeared as of 2026-05-21. Polish practitioners report a real-world lag of **days to a few weeks** between a filing date and KRZ registration; however, the filing date is what triggers the two-month window, not the KRZ display date. Accordingly, the most urgent task is verifying the true filing date via KRZ and MSiG before committing to Path B.[^3]

***

## A. Real Estate Ownership

**Strategic weight:** High. Real estate cannot be physically moved; if the debtor owns property, a *hipoteka przymusowa* (forced mortgage) survives even a long enforcement timeline. Finding KW numbers is therefore the single highest-value OSINT step.

### A1 — Biała Lista VAT (White List) — Bank Accounts & Address
| Attribute | Detail |
|---|---|
| **URL** | https://www.podatki.gov.pl/wykaz-podatnikow-vat-wyszukiwarka |
| **Legal access** | Open data — no login required |
| **Cost** | Free |
| **Accuracy / Freshness** | Updated daily on business days; data reflects what the taxpayer declared to the Tax Office[^4][^5] |
| **Time to obtain** | Instant |
| **Caveats** | Foreign bank accounts are not visible[^4]. Only business accounts declared to the Tax Office via NIP-7/NIP-8 filing and confirmed through STIR are shown[^5]. The address shown is the registered address, not necessarily the real one. |

```prompt-for-browser-agent
Open https://www.podatki.gov.pl/wykaz-podatnikow-vat-wyszukiwarka

1. The page loads a search form in Polish. You will see a field labeled "Podaj NIP, REGON, nazwę lub numer rachunku bankowego" (Enter NIP, REGON, name, or bank account number).
2. In that field, type exactly: 8661681248
3. Below the search field you will see a date selector labeled "Wybierz datę" (Select date). Leave it set to today's date (it defaults to the current day).
4. Click the blue button labeled "Szukaj" (Search).
5. The results section should display a card for "MATEUSZ SZKLARSKI GPUCOMPUTER". Extract and return to me ALL of the following fields exactly as shown:
   - "Nazwa" (Name)
   - "NIP"
   - "Status VAT" (VAT status)
   - "Numer rachunku bankowego" (Bank account number(s)) — this is critical; there may be multiple accounts listed
   - "Adres" (Address)
   - Any dates shown (registration, deregistration)
6. If the page shows "Brak wyników" (No results) or "Podmiot nie jest zarejestrowany jako podatnik VAT" (Entity not registered as VAT taxpayer), record that text exactly and stop.
7. If a CAPTCHA appears, stop and report "CAPTCHA blocking — needs human".
8. Return all extracted data as a JSON object with English-translated field names.
```

***

### A2 — Commercial KW Number Look-Up Services (Address → KW Number)
| Attribute | Detail |
|---|---|
| **Services** | wieczyste.pl, skaner.com, ksiegiwieczyste.pl |
| **Legal access** | Open to anyone; commercial paid services |
| **Cost** | ~30–50 PLN per address query[^6] |
| **Accuracy / Freshness** | Based on scraped/archived EGiB+KW data; reasonably current but may lag weeks behind court entries |
| **Time to obtain** | Instant to 24 hours |
| **Caveats** | Geoportal.gov.pl was fined by UODO (data protection authority) in 2020 for exposing KW numbers; the main national geoportal no longer shows KW numbers due to RODO enforcement[^7]. Commercial services operate on archived datasets that were scraped before the restriction[^8]. The KW number itself is free to use on ekw.ms.gov.pl once obtained[^9][^10]. |

The debtor's CEIDG-registered address is ul. Mogilska 16 lok. 7, 31-516 Kraków (virtual office). Run the lookup on that address. Also run on any real operational addresses discovered in Category C.[^11][^12]

```prompt-for-browser-agent
TASK 1 — wieczyste.pl lookup

Open https://www.wieczyste.pl

1. On the homepage you will see a search field at the top. The field may be labeled "Wyszukaj po adresie, ID działki lub numerze KW" (Search by address, plot ID, or KW number).
2. In the search field, type: Mogilska 16, 31-516 Kraków
3. Press Enter or click the search/magnifying-glass button.
4. If results appear, extract for each result:
   - Full KW number (format: XX1Y/NNNNNNNN/Z, e.g. KR1P/00123456/7)
   - Owner name shown (if visible)
   - Property type / address
5. If no results appear, record "No results for Mogilska 16 Kraków" and proceed to TASK 2.
6. If the site requires payment or registration to view owner names, stop at the KW number and report it to me — do not pay.
7. If a CAPTCHA appears, stop and report "CAPTCHA blocking — needs human".

TASK 2 — ksiegiwieczyste.pl lookup

Open https://ksiegiwieczyste.pl

1. Find the section labeled "Szukaj po adresie" (Search by address).
2. In the city/locality field ("Miejscowość"), begin typing: Krakow (or Kraków) and select "Kraków" from the dropdown.
3. In the street field ("Ulica"), type: Mogilska
4. In the building number field ("Numer domu"), type: 16
5. In the apartment/unit field ("Numer lokalu"), type: 7
6. Click "Szukaj" (Search).
7. Extract all KW numbers returned and the corresponding property descriptions.
8. If no results, record that and stop.
9. Return results as a JSON list. If either service asks for payment to see owner details, record the KW number only and stop.
```

***

### A3 — EKW (Electronic Land Register) — View KW Contents
Once a KW number is found via A2 or other sources, the KW itself is publicly and freely viewable on the Ministry of Justice portal.[^9][^10][^13]

```prompt-for-browser-agent
PREREQUISITE: You need a valid KW number (e.g. KR1P/00123456/7) from step A2.
If no KW number was found in A2, skip this step and escalate to me.

Open https://przegladarka-ekw.ms.gov.pl/eukw_prz/KsiegiWieczyste/wyszukiwanieKW?komunikaty=true&kontakt=true&okienkoSerwisowe=false

1. You will see a form with three fields for the KW number components, labeled:
   - "Kod wydziału" (Court department code) — e.g. KR1P
   - "Numer księgi wieczystej" (KW number) — the 8-digit number
   - "Cyfra kontrolna" (Check digit) — single digit
2. Enter the three components from the KW number found in A2 (e.g. for "KR1P/00123456/7": code=KR1P, number=00123456, digit=7).
3. Click "Wyszukaj księgę" (Search for register).
4. The KW will open. Navigate to the following sections (tabs at the top) and extract all text:
   - "Dział I-O" (Section I-O) — property description and location
   - "Dział II" (Section II) — OWNER (właściciel) name(s) and ownership share. This is the critical section.
   - "Dział III" (Section III) — encumbrances, third-party rights, claims
   - "Dział IV" (Section IV) — mortgages (hipoteki)
5. Return ALL text from Sections II, III, and IV in English translation.
6. If the property in Section II is owned by someone other than Mateusz Szklarski, record the owner name and stop.
7. If the page shows "Nie ma takiej księgi wieczystej" (No such land register), record that and report to me.
8. Note: The portal is unavailable every Sunday 00:00–09:00 CEST for maintenance.
```

**Skip condition:** Skip A3 if A2 returns no KW numbers.

***

### A4 — Geoportal.gov.pl — Plot Identification (Indirect)
| Attribute | Detail |
|---|---|
| **URL** | https://mapy.geoportal.gov.pl/imap/ |
| **Legal access** | Open data |
| **Cost** | Free |
| **Accuracy** | Plot IDs are current; KW links were removed after UODO penalty[^7][^14] |
| **Caveats** | Cannot search by owner name. Use only to visually identify plots at known addresses (virtual office, operational addresses from C). Plot ID (*identyfikator działki*) obtained here can then be used to order a KW lookup from commercial services (A2). |

```prompt-for-browser-agent
Open https://mapy.geoportal.gov.pl/imap/

1. In the search bar at the top, type the address: ul. Mogilska 16, Kraków and press Enter or select from suggestions.
2. The map will navigate to that location. Click on the land parcel/plot that contains the building.
3. A popup or left panel should appear showing "Informacje o wybranej działce" (Information about the selected plot). Extract:
   - "Identyfikator działki" (Plot identifier) — a numeric code like 126101_8.0014.AR_17.50/2
   - "Numer działki" (Plot number)
   - "Obręb" (District/precinct)
   - "Powierzchnia" (Area)
4. Repeat for any other known physical address of the debtor found in Category C.
5. Return all plot identifiers found. Do NOT attempt to find KW numbers here — that functionality was removed.
6. If the panel shows no plot information on click, try clicking directly on the building footprint.
7. If the map does not load or shows an error, stop and report "Geoportal not loading".
```

***

### A5 — Lawyer-Assisted / Komornik Real Estate Search
| Attribute | Detail |
|---|---|
| **Method** | Formal request (*zapytanie*) from komornik to Centralna Baza Danych Ksiąg Wieczystych under *zlecenie poszukiwania majątku* |
| **Legal access** | **Komornik-only; requires enforcement title** (*tytuł wykonawczy*) |
| **Cost** | ~100 PLN flat fee + 10% of recovered amount; komornik can search by PESEL/NIP across the entire national KW database |
| **Time** | 1–5 business days |
| **Caveats** | Not available until EPU yields a *nakaz zapłaty* (and debtor does not object) or a regular court issues any enforceable order. If Path B succeeds and a *postanowienie o zabezpieczeniu* is obtained, the appointed komornik can immediately query the KW database by name/PESEL as part of executing the precautionary attachment. |

**This step CANNOT be executed by a browser agent.** Route to your komornik once an enforcement title or zabezpieczenie order is in hand.

***

## B. Vehicle Ownership

**Strategic weight:** Medium. Vehicles are mobile assets. A komornik can seize and auction them. Commercial GPU-building businesses frequently own equipment vehicles or high-value delivery vehicles.

### B1 — Biała Lista / CEIDG (Indirect)
Already covered in A1. Check CEIDG for declared use of vehicle under PKD activities — no direct vehicle data.

### B2 — historiapojazdu.gov.pl (VIN-Based Vehicle History)
| Attribute | Detail |
|---|---|
| **URL** | https://historiapojazdu.gov.pl |
| **Legal access** | Open data; free |
| **Cost** | Free[^15] |
| **Accuracy** | Draws from CEPiK (Centralna Ewidencja Pojazdów i Kierowców), insurer databases, and inspection databases[^16] |
| **Caveats** | Requires VIN + registration plate + first registration date. Cannot search by owner name. Only useful if you already know the vehicle's VIN or plate from other OSINT (delivery photos, social media, etc.). Does not disclose current owner name in the public view. |

**Skip condition:** Skip unless a specific vehicle VIN or plate is found in Category C OSINT.

```prompt-for-browser-agent
PREREQUISITE: You need a VIN number and/or plate number found via Category C OSINT (e.g. from a delivery photo, social media post, or listing).
If no VIN/plate was found, skip this step.

Open https://historiapojazdu.gov.pl

1. You will see three fields:
   - "Numer rejestracyjny" (Registration plate number)
   - "Numer VIN"
   - "Data pierwszej rejestracji" (First registration date) — format DD-MM-YYYY
2. Enter the plate and VIN found in OSINT. For first registration date, if unknown, try common years (2015, 2016, etc.).
3. Click "Sprawdź pojazd" (Check vehicle).
4. Extract all information shown: make, model, year, fuel type, mileage history, inspection dates, insurance status, accident history.
5. If the result shows "Brak danych" (No data) or "Podane dane są nieprawidłowe" (Data incorrect), the plate/VIN may be wrong — record and stop.
6. Return a full English translation of the results.
```

***

### B3 — CEPiK — Owner-Name Vehicle Search (Restricted)
| Attribute | Detail |
|---|---|
| **URL** | https://www.cepik.gov.pl |
| **Legal access** | **Restricted.** Requires demonstrated *konkretny interes prawny* (specific legal interest). Accessible via formal written request with supporting documentation[^17]. |
| **Cost** | Nominal administrative fee |
| **Caveats** | Not self-service online. A creditor with a documented claim can apply, but the process is bureaucratic. More efficiently accessed by the komornik via *zlecenie poszukiwania majątku* once an enforcement title exists. |

**This step requires a formal written request — cannot be executed by a browser agent.** Route to your lawyer to prepare the *wniosek o udzielenie informacji z CEPiK*.

***

### B4 — OLX / OtoMoto / Allegro — Ad History Search
| Attribute | Detail |
|---|---|
| **Legal access** | Open data |
| **Cost** | Free |
| **Caveats** | Ads are often deleted after sale. Useful for identifying makes/models/plates if photos were published. Also can reveal distress selling of business equipment. |

```prompt-for-browser-agent
TASK 1 — OLX ad search for GPUcomputer

Open https://www.olx.pl

1. In the main search bar, type: gpucomputer and press Enter.
2. Review all results. For each listing, extract: title, price, location, date, seller name/username, and any contact info visible.
3. Click "Filtry" (Filters) and set "Sprzedawca" (Seller) to "Prywatny i Firmowy" if not already set.
4. Repeat the search with: Mateusz Szklarski
5. Repeat with: GPU Computer Kraków
6. For any listing showing computer hardware being sold in bulk or at unusually low prices, note it as a potential asset-stripping signal.
7. If no results are found for any query, record "No results" for each.

TASK 2 — Allegro seller search

Open https://www.allegro.pl

1. In the search bar, type: gpucomputer and press Enter.
2. Click on "Sprzedawcy" (Sellers) tab if available, or look for seller accounts matching the name.
3. Also search: Mateusz Szklarski
4. For any matching seller account, note: username, feedback count, items currently listed, any items recently sold (hardware, GPUs, peripherals in bulk).
5. Extract all visible contact or address information.
6. Return findings as a JSON list.
```

***

## C. Actual Operating Address / Business Premises

The CEIDG address (ul. Mogilska 16 lok. 7, 31-516 Kraków) is confirmed as a virtual office shared by multiple unrelated businesses. The debtor's real assembly, storage, or operating location is a key unknown.[^18][^11]

### C1 — Wayback Machine / Archive.org — Historical Website Snapshots
| Attribute | Detail |
|---|---|
| **URL** | https://web.archive.org/web/*/gpucomputer.pl |
| **Legal access** | Open data |
| **Cost** | Free |
| **Accuracy** | Dependent on crawl frequency. Most sites are archived monthly or more often. |
| **Caveats** | The debtor may have removed address info from the current site. Historical snapshots often contain "Kontakt" (Contact) pages with physical addresses. |

```prompt-for-browser-agent
Open https://web.archive.org/web/*/https://www.gpucomputer.pl/

1. You will see a calendar-style timeline showing snapshots of gpucomputer.pl across years (2015–2026).
2. Starting with the earliest available snapshot (2015–2016), click on any highlighted date to open the archived version of the site.
3. On the archived site, find and click the page labeled "Kontakt" (Contact) or similar (may also appear as "O nas" — About Us, or "Gdzie jesteśmy" — Where to find us).
4. Extract ALL address information, phone numbers, email addresses, and map embeds visible on that page.
5. Repeat for snapshots approximately every 6–12 months (2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, early 2026).
6. Pay special attention to any address that is NOT "Mogilska 16" — that would be the real operational address.
7. Also check the "Regulamin" (Terms of service) and "Polityka prywatności" (Privacy policy) pages for any physical address or company data.
8. Return a chronological JSON list of all unique addresses and contact data found across all snapshots.
9. If the Wayback Machine shows "This page has not been archived" for gpucomputer.pl, record that and stop.
10. If a CAPTCHA or rate-limit appears, wait 30 seconds and retry once. If it persists, stop and report.
```

***

### C2 — Google Maps / Review Platforms — Customer-Reported Locations
| Attribute | Detail |
|---|---|
| **Services** | Google Maps, Ceneo.pl, Opineo.pl, Trustpilot |
| **Legal access** | Open data |
| **Cost** | Free |
| **Caveats** | Customer reviews sometimes mention pickup addresses, warehouse locations, or service visits. |

```prompt-for-browser-agent
TASK 1 — Google Maps

Open https://www.google.com/maps

1. In the search bar, type: gpucomputer.pl Kraków and press Enter.
2. If a business listing appears, click on it and extract: full address, phone number, website, hours, all visible reviews.
3. In the reviews, look for any mention of pickup location, warehouse, service address, or any address other than Mogilska 16.
4. Also search: GPUcomputer Mateusz Szklarski
5. Repeat for: GPU Computer Kraków

TASK 2 — Ceneo opinie

Open https://www.ceneo.pl

1. In the search bar, type: gpucomputer and press Enter.
2. Find any seller profile for gpucomputer or Mateusz Szklarski. Click on it.
3. Extract: seller name, address if shown, feedback score, all visible reviews.
4. Read through reviews for any mention of physical location, pickup, service address.

TASK 3 — Opineo

Open https://www.opineo.pl

1. Search for: gpucomputer.pl
2. If a profile exists, extract all reviews mentioning physical locations or addresses.
3. Return all findings as JSON with source, date, and quoted text of relevant reviews.
```

***

### C3 — WHOIS and DNS History — gpucomputer.pl
| Attribute | Detail |
|---|---|
| **URL** | https://securitytrails.com/domain/gpucomputer.pl/history/a (free tier allows limited lookups)[^19][^20] |
| **Legal access** | Open data |
| **Cost** | Free (limited); SecurityTrails Basic plan ~$50/month for full history |
| **Caveats** | Polish .pl domains registered via NASK. Registrant contact data is often privacy-protected but sometimes reveals the registrant's email or address. Historical IP addresses can be traced to hosting providers that may show billing addresses or geolocation. |

```prompt-for-browser-agent
TASK 1 — Current WHOIS for gpucomputer.pl

Open https://www.whois.com/whois/gpucomputer.pl

1. The page will show the current WHOIS record for gpucomputer.pl.
2. Extract ALL fields including: Registrant Name, Registrant Organization, Registrant Address, Registrant Email, Name Servers, Registration Date, Last Updated.
3. If fields show "REDACTED FOR PRIVACY" or similar, record that.
4. Copy the full raw WHOIS text.

TASK 2 — DNS/IP history via SecurityTrails (free tier)

Open https://securitytrails.com/domain/gpucomputer.pl/dns

1. You may need to create a free account (email only, no credit card). If prompted to register, create an account with a temporary email if possible, or stop and report "Login required — needs human to register".
2. If you can view the DNS records without login, note all A records (IP addresses) associated with gpucomputer.pl over time.
3. For each unique IP address found, note it for further hosting lookup.
4. Return all IP addresses found and dates associated.

TASK 3 — viewdns.info reverse IP lookup

Open https://viewdns.info/reverseip/?host=gpucomputer.pl&t=1

1. The page will show all domains hosted on the same IP as gpucomputer.pl.
2. Extract the full list of co-hosted domains — these may reveal other business entities operated by the same person.
3. Return the full domain list.
```

***

### C4 — Panorama Firm / PKT.pl / Business Directories
| Attribute | Detail |
|---|---|
| **URLs** | https://panoramafirm.pl, https://pkt.pl, https://www.firmagodnazaufania.pl |
| **Legal access** | Open data |
| **Cost** | Free |
| **Caveats** | These directories often contain historical address data. The Panorama Firm entry already confirmed the Mogilska 16 address and a phone number (531 061 452)[^18]. |

```prompt-for-browser-agent
TASK 1 — Panorama Firm

Open https://panoramafirm.pl

1. In the search bar, type: Mateusz Szklarski GPUcomputer and press Enter.
2. Click on the matching result.
3. Extract ALL visible data: address, phone, email, website, categories, description.
4. Note: The visible phone number 531 061 452 is already known — but check if there is additional contact info, or a different address.
5. Check if there are any comments/reviews with location mentions.

TASK 2 — Firma Godna Zaufania

Open https://www.firmagodnazaufania.pl/company,50850,mateusz-szklarski-lopata-gpucomputer

1. This is a direct URL to the debtor's profile. Load it.
2. Extract all visible data including: full address, phone, email, NIP, REGON, founding date, any certifications or badges, and any comments.
3. Return all data as JSON.

TASK 3 — KRS-Online profile

Open https://www.krs-online.com.pl/firma/5516506-mateusz-szklarski-lopata-gpucomputer

1. Load the page and extract all data shown: NIP, REGON, registered address, activity codes, persons, and any linked entities.
2. Return as JSON.
```

***

## D. Bank Accounts

**Strategic weight:** Critical. Bank account freezing is the primary goal of Path B (*zabezpieczenie*).

### D1 — Biała Lista VAT — Bank Account Numbers (See A1 above)

This is the **single most important open-data step**. The White List (biała lista podatników VAT) publicly discloses all business bank accounts declared by VAT-registered entities to the Polish Tax Office. The account numbers shown are exactly those the komornik would freeze. **Execute A1 prompt immediately — bank account numbers may already be public.**[^4][^21]

The White List shows only:
- Polish PLN business accounts (rachunki rozliczeniowe)
- VAT-split accounts (*rachunki VAT*)
- Accounts reported through STIR to the Tax Administration

It does **not** show: foreign accounts, personal savings accounts, fintech/Revolut accounts held under a Lithuanian IBAN, or accounts not reported to the Tax Office.[^22][^4]

***

### D2 — Past Invoices, Order Confirmations, Terms of Service
| Attribute | Detail |
|---|---|
| **Source** | Wayback Machine snapshots of gpucomputer.pl (see C1) |
| **Legal access** | Open data |
| **Cost** | Free |
| **Caveats** | Pre-2019 invoices may show a different bank account. Check archived "Regulamin" (Terms), "Cennik" (Price list), and checkout pages for hard-coded IBANs. |

**Embed into the C1 Wayback Machine prompt above**: specifically request extraction of any IBAN or bank account numbers visible on archived regulamin, payment, or checkout pages.

***

### D3 — OGNIVO (Bank Network Query)
| Attribute | Detail |
|---|---|
| **Access** | **Komornik-only.** OGNIVO is operated by Krajowa Izba Rozliczeniowa (KIR) and is exclusively accessible to enforcement officers (*komornicy sądowi*) and certain administrative bodies[^22][^23][^24] |
| **How it works** | A single OGNIVO query instantly locates all accounts across all participating Polish banks and triggers simultaneous freezing notifications[^22] |
| **Cost** | For the creditor: included in standard enforcement fee structure |
| **Caveats** | Foreign-registered banks (Revolut Lithuania) and accounts with no Polish branch may not be visible[^22]. A *postanowienie o zabezpieczeniu* (precautionary injunction) from the civil court immediately enables the komornik to execute via OGNIVO — this is the key argument for Path B. |

**This step CANNOT be executed by a browser agent.** It requires a komornik with an active enforcement title or *postanowienie o zabezpieczeniu*.

***

## E. Other Business Interests, Shareholdings, Partnerships

### E1 — KRS (National Court Register) — Name Search for Company Affiliations
| Attribute | Detail |
|---|---|
| **URL** | https://ekrs.ms.gov.pl/web/wyszukiwarka-krs/strona-glowna/ |
| **Legal access** | Open data; free[^25][^26] |
| **Cost** | Free |
| **Accuracy** | Real-time data from the official register |
| **Caveats** | The official KRS API partially anonymizes names (showing "M*** S*****" format). The official search by person's full name is possible via the public portal for persons listed in KRS roles. Third-party services like rejestr.io[^27] and apify.com/regdata/krs-fullnames-scraper[^28] offer de-anonymized lookups at small cost. A JDG debtor who also controls an sp. z o.o. (LLC) would be traceable this way. |

```prompt-for-browser-agent
TASK 1 — Official KRS search by person name

Open https://ekrs.ms.gov.pl/web/wyszukiwarka-krs/strona-glowna/

1. You will see a search form. Look for a tab or section labeled "Osoby" (Persons) or "Wyszukaj osobę" (Search for a person). If there is a toggle between "Podmioty" (Entities) and "Osoby" (Persons), select "Osoby".
2. In the name field ("Imię i nazwisko" or "Nazwisko"), type: Szklarski
3. In the first name field ("Imię"), type: Mateusz
4. Click "Szukaj" (Search).
5. The results should show any companies (sp. z o.o., sp.k., SA, etc.) where Mateusz Szklarski appears as a board member (zarząd), partner (wspólnik), proxy (prokurent), or liquidator (likwidator).
6. For each result, extract: company name, KRS number, NIP, role of Mateusz Szklarski, date of entry, current status.
7. If no results appear, try variations: searching surname only "Szklarski" to catch all first-name variants.
8. If the page shows "Brak wyników" (No results), record that.
9. Return all results as a JSON list.

TASK 2 — rejestr.io cross-reference

Open https://rejestr.io

1. In the search bar, type: Mateusz Szklarski and press Enter.
2. Filter results if possible to show persons (not just companies).
3. Extract any company affiliations, roles, dates of entry and exit.
4. Also search: 8661681248 (the NIP) to find any cross-entity connections.
5. Return all findings as JSON.
```

***

### E2 — CRBR (Central Register of Beneficial Owners)
| Attribute | Detail |
|---|---|
| **URL** | https://crbr.podatki.gov.pl/adcrbr/#/ |
| **Legal access** | Open data; free[^29][^30][^31] |
| **Cost** | Free |
| **Accuracy** | Entities must report within 7 days of KRS entry; updated on entity changes |
| **Caveats** | CRBR covers only KRS-registered entities (sp. z o.o., sp.k., SA, etc.) — not JDG itself. But if the debtor is a beneficial owner of any such entity, it will appear here. Searchable by PESEL, NIP, or name+date of birth[^29]. |

```prompt-for-browser-agent
Open https://crbr.podatki.gov.pl/adcrbr/#/

1. The page is in Polish. Find the search section labeled "Wyszukaj beneficjenta" (Search for a beneficiary) or similar.
2. You have three options for searching beneficiaries. Use option 3 (name + date of birth) if PESEL is unknown:
   - Field "Imię" (First name): Mateusz
   - Field "Nazwisko" (Last name): Szklarski
   - For date of birth: This is unknown. Try leaving it blank or entering approximate years (check if the field is mandatory). If mandatory and you have the debtor's approximate age (the AGH Kraków graduation suggests early-to-mid 30s in 2026), try birth years 1990–1996.
3. Click "Szukaj" (Search).
4. If results appear, for each match extract: full name, PESEL (if shown), name of company, NIP of company, type of ownership/control, percentage share.
5. Also search by NIP: 8661681248 (this will search for entities linked to the JDG, though CRBR mainly covers KRS entities).
6. If the page shows "Brak wyników" (No results), record that and stop.
7. If a CAPTCHA or session timeout occurs, refresh and retry once.
8. Return all results as JSON.
```

***

### E3 — eZamówienia — Public Procurement Records
| Attribute | Detail |
|---|---|
| **URL** | https://ezamowienia.gov.pl/mp-client/search/list |
| **Legal access** | Open data |
| **Cost** | Free |
| **Caveats** | If GPUcomputer supplied hardware to any public institution (schools, hospitals, government offices), procurement records are public. These may reveal the debtor's real bank account (as declared in procurement documents) and operational address. |

```prompt-for-browser-agent
Open https://ezamowienia.gov.pl/mp-client/search/list

1. Find the search bar labeled "Wyszukaj" (Search) or "Szukaj ogłoszenia" (Search for announcement).
2. Type: GPUcomputer and press Enter.
3. Also search: gpucomputer.pl
4. Also search: 8661681248
5. Also search: Mateusz Szklarski
6. For each result found, extract: contracting authority, contract title, date, value, awarded contractor name and address.
7. If no results, record "No public procurement records found" and stop.
8. Return as JSON.
```

***

## F. Other Creditors and Existing Claims

**Strategic weight:** Critical for understanding your position in any queue.

### F1 — KRZ (Krajowy Rejestr Zadłużonych) — Deep Search
| Attribute | Detail |
|---|---|
| **URL** | https://krz.ms.gov.pl or https://prs.ms.gov.pl |
| **Legal access** | Open data; free[^32][^33][^34] |
| **Cost** | Free |
| **Accuracy** | As of 2026: KRZ covers bankruptcy, restructuring, and failed enforcement proceedings. Lag between court filing and KRZ display: typically **days to a few weeks** for *wniosek o ogłoszenie upadłości* (bankruptcy petition). |
| **Caveats** | A bankruptcy petition filed by the debtor is entered in KRZ but there is a processing lag. The absence of a KRZ entry as of 2026-05-21 does NOT guarantee no petition exists — it may be pending processing. |

```prompt-for-browser-agent
Open https://krz.ms.gov.pl

1. The homepage will show a search form. Look for a field labeled "Imię i nazwisko / Nazwa" (Name) or "Dane podmiotu" (Entity data).
2. In the name field, type: Mateusz Szklarski
3. Also fill in if there is a NIP field: 8661681248
4. Click "Szukaj" (Search).
5. If results appear, for each entry extract:
   - Type of proceeding (upadłość = bankruptcy, restrukturyzacja = restructuring, umorzenie egzekucji = discontinued enforcement)
   - Case signature (sygnatura akt)
   - Court name
   - Filing date
   - Status
6. If the page shows "Brak wyników" (No results), record that with today's date and stop.
7. Also repeat the search using: GPUcomputer (the business name)
8. Also search by NIP only: 8661681248
9. Return all results as JSON. This is the MOST IMPORTANT SEARCH — if any bankruptcy entry appears, report to me immediately before proceeding.
```

***

### F2 — MSiG (Monitor Sądowy i Gospodarczy) — Full-Text Gazette Search
| Attribute | Detail |
|---|---|
| **URL** | https://wyszukiwarka-msig.ms.gov.pl |
| **Legal access** | Open data; free[^35][^36] |
| **Cost** | Free |
| **Accuracy** | MSiG is the official gazette where all court announcements are published — bankruptcy declarations, restructuring notices, creditor calls, enforcement cancellations |
| **Caveats** | Covers all periods including pre-KRZ (before December 2021). Also, a pending *wniosek dłużnika o ogłoszenie upadłości* that has not yet been ruled upon may already have an MSiG announcement if the court issued any interim order. |

```prompt-for-browser-agent
Open https://wyszukiwarka-msig.ms.gov.pl

1. You will see a search form with the following fields (use all of them in separate searches):
   - "Nazwa podmiotu" (Entity name)
   - "Numer KRS" (KRS number) — leave blank for JDG
   - "NIP"
   - "Tekst w treści" (Text in content)

SEARCH 1: In "Nazwa podmiotu", type: Mateusz Szklarski → Click "Szukaj" (Search)
SEARCH 2: In "NIP", type: 8661681248 → Click "Szukaj"
SEARCH 3: In "Nazwa podmiotu", type: GPUcomputer → Click "Szukaj"
SEARCH 4: In "Tekst w treści", type: Szklarski Mateusz → Click "Szukaj"

For each search:
- If results appear, for each entry extract: publication date, type of announcement (typ sprawy), text/summary of the announcement, court, case reference.
- Pay special attention to entries with types: "Upadłość" (Bankruptcy), "Restrukturyzacja" (Restructuring), "Ogłoszenie upadłości" (Bankruptcy declaration), "Wezwanie wierzycieli" (Creditor call).
- If results span multiple pages, extract all pages.
- If no results: record "No MSiG entries" for each search.
5. Return all findings chronologically as JSON.
```

***

### F3 — KRD (Krajowy Rejestr Długów) — Debtor Listing Check
| Attribute | Detail |
|---|---|
| **URL** | https://krd.pl |
| **Legal access** | Checking a third-party's debts requires a business subscription OR can be done via a commercial partner; individual creditors can add a debtor but checking others' records requires business account[^37][^38] |
| **Cost** | Business subscription required; basic reports ~30–69 PLN per query[^39]; business account signup required |
| **Accuracy** | Entries are voluntary (creditor-initiated); absence of entry does not mean no debts exist[^37] |
| **Caveats** | An individual (private creditor) can register as a business user through KRD to get checking access. Alternatively, you can add the debtor yourself (69 PLN fee, pre-demand letter required — which you already have)[^40][^41] |

```prompt-for-browser-agent
Open https://krd.pl

1. Look for a section or button labeled "Sprawdź firmę" (Check a company) or "Weryfikacja kontrahenta" (Check a contractor).
2. Click on it. You may be asked to log in or create an account. If a login wall appears, stop and report "KRD login required — needs human to register and pay for access".
3. If there is a free basic search (sometimes available without login for basic status), enter:
   - NIP: 8661681248
   - Or name: Mateusz Szklarski
4. Extract any information visible about debts, entries, or status.
5. If the page asks for payment or account creation to see results, record "Login/payment required" and stop.
6. Return whatever is visible at the free tier.
```

**For full access:** Register a business account at krd.pl (requires a Polish NIP — may need your lawyer's NIP or a Polish intermediary). Alternatively, use the BIG InfoMonitor (big.pl) which has similar functionality.

***

### F4 — BIG InfoMonitor — Debt Register Check
| Attribute | Detail |
|---|---|
| **URL** | https://www.big.pl |
| **Legal access** | Business subscription required; companies and individuals with documented claims can subscribe[^42][^43][^44] |
| **Cost** | Individual/company report ~30–35 PLN per check; business subscription from ~120 PLN/month |
| **Accuracy** | Covers BIG registry + BIK bank data (for subscribers with paper contract) |
| **Caveats** | BIG InfoMonitor also has access to BIK (credit bureau) data for paying subscribers — giving partial insight into credit history |

This step requires your lawyer or a Polish business intermediary to set up a BIG account. **Cannot be fully automated by a browser agent without a registered account.**

***

### F5 — Licytacje Komornicze — Active Enforcement Listings
| Attribute | Detail |
|---|---|
| **URL** | https://licytacje.komornik.pl |
| **Legal access** | Open data; free |
| **Cost** | Free |
| **Caveats** | If other creditors have already obtained enforcement titles and the komornik has seized assets, those assets appear here for public auction. Presence confirms other enforcement proceedings are active. |

```prompt-for-browser-agent
Open https://licytacje.komornik.pl/wyszukiwarka/obwieszczenia-o-licytacji

1. Look for a search or filter form.
2. In any name/owner field, search for: Mateusz Szklarski
3. Also search: GPUcomputer
4. Also filter by city: Kraków (look for a "Miasto" or "Województwo" — select Małopolskie/Kraków).
5. Extract any listings showing assets tied to the debtor: address, asset description, court/komornik name, case signature.
6. Also check the legacy site for older listings: https://ool.komornik.pl (the page mentions pre-2026-02-27 listings are there).
7. If no results, record "No active enforcement auctions found".
8. Return as JSON.
```

***

### F6 — Rejestr Zastawów (Pledge Register)
| Attribute | Detail |
|---|---|
| **URL** | https://prs.ms.gov.pl → Centralna Informacja section |
| **Legal access** | Open; query by NIP; certificates require registration and a small fee[^45][^46] |
| **Cost** | Free to query; ~20 PLN for an official zaświadczenie (certificate) |
| **Accuracy** | Shows registered pledges (*zastawy rejestrowe*) over movables (machinery, vehicles, stock). Does not show tax pledges (*zastawy skarbowe*) — those are on a separate Ministry of Finance register. |

```prompt-for-browser-agent
Open https://prs.ms.gov.pl

1. On the homepage, look for a section or tile labeled "Centralna Informacja" or "Rejestr Zastawów" (Pledge Register).
2. Click on it.
3. You may need to create an account in the "Tożsamość" (Identity) system. If prompted, stop and report "Account registration required — needs human".
4. If a free query is available without login:
   - Enter NIP: 8661681248
   - Or enter name: Mateusz Szklarski
5. Extract any pledge entries showing: pledgor name, pledgee (creditor) name, description of pledged asset, registration date, value.
6. If no results, record "No registered pledges found for this NIP".
7. Return as JSON.
```

Also check the tax pledge register (*Rejestr Zastawów Skarbowych*) at https://www.podatki.gov.pl (search for *rejestr zastawów skarbowych*) by entering NIP 8661681248.

***

### F7 — Portal Informacyjny Sądów Powszechnych — Prior Litigation
| Attribute | Detail |
|---|---|
| **URL** | https://portal.wroclaw.sa.gov.pl/#/login (this URL covers all Polish appellate circuits)[^47][^48] |
| **Legal access** | Restricted. Requires account registration with **in-person identity verification** at a court Punkt Informacyjny (Information Point)[^48] |
| **Cost** | Free |
| **Caveats** | Once registered, allows checking all cases where the person is a party — revealing prior creditors who have already sued. This is high-value but requires physical presence at a Polish court. Route to your lawyer. |

**This step requires physical presence at a Polish court — cannot be done by a browser agent.** Route to your Kraków lawyer, who can register and search.

***

## G. Operational Signals / Business Health

### G1 — Live Website Test — Is Business Still Accepting Orders?

```prompt-for-browser-agent
Open https://www.gpucomputer.pl

1. Fully load the site. Extract the homepage text.
2. Navigate to any product page or "Konfiguruj komputer" (Configure computer) / ordering section.
3. Attempt to add a product to the cart or start a custom PC configurator (do NOT complete any purchase or enter payment data).
4. Check if the cart/order process is functional or shows errors.
5. Find and record any "Kontakt" (Contact) page — phone number, email, address, contact form.
6. Check if the website shows any notice of suspension, insolvency, or closure ("zawieszona działalność", "ogłoszenie upadłości", or similar).
7. Find the "Regulamin" (Terms of Service) page. Extract the full company data section (usually at the top) including any IBAN/bank account numbers.
8. Find the "Polityka prywatności" (Privacy policy). Extract company identification data.
9. Check if there are any recent news posts, blog entries, or announcements with dates.
10. Return: (a) whether ordering appears to be functional (yes/no), (b) all contact info found, (c) all company identification data, (d) any bank account numbers found in regulamin, (e) any announcements.
```

***

### G2 — Social Media Search

```prompt-for-browser-agent
TASK 1 — Facebook

Open https://www.facebook.com/search/pages/?q=gpucomputer

1. Review all page results. Click on any matching "GPUcomputer" or "GPU Computer" page.
2. Extract: page name, number of followers, last post date, all visible posts from 2025–2026.
3. Check "About" (O stronie) section for: address, phone, website, founding date.
4. Look for any posts about insolvency, closure, supplier problems, or asset sales.

Open https://www.facebook.com/mateusz.szklarski.982/ (this profile was found in search results)

5. Extract any public posts visible, location, recent activity (last 6 months).
6. Look for signals: travel posts, high-value purchases, distress posts, mentions of bankruptcy or business closure.

TASK 2 — LinkedIn

Open https://www.linkedin.com/pub/dir/Mateusz/Szklarski

1. Review profiles. Look for a Mateusz Szklarski based in Kraków, with IT/hardware background, possibly with AGH (Akademia Górniczo-Hutnicza) education noted on Facebook.
2. If found, extract: current employer, past employers, location, education, connections count.
3. Note any current employment listed (would indicate personal income = garnishable).

TASK 3 — Instagram / TikTok

Search: gpucomputer on https://www.instagram.com
Search: gpucomputer on https://www.tiktok.com

4. Extract any recent posts with location tags or business activity from 2025–2026.
5. Return all findings as JSON.
```

***

### G3 — Similarweb / Web Traffic — Business Activity Indicator

```prompt-for-browser-agent
Open https://www.similarweb.com/website/gpucomputer.pl/

1. Extract all visible traffic data: monthly visits (last 3–6 months trend), traffic sources, bounce rate, engagement.
2. Note especially the trend line — is traffic rising, stable, or declining?
3. A sharp traffic decline after January 2026 (when the debt arose) would suggest the business stopped operating.
4. Return all visible metrics.
5. If Similarweb shows "Insufficient data" or "< 5K visits/month", record that.
```

***

### G4 — Recent Complaints — Customer Reports of Non-Delivery

```prompt-for-browser-agent
TASK 1 — Reddit / r/Polska

Open https://www.reddit.com/search/?q=gpucomputer&restrict_sr=false&sort=new

1. Review all results. Look for complaints about non-delivery, refund problems, or fraud from gpucomputer.pl.
2. Filter to last 12 months if possible.
3. Extract: post date, username, summary of complaint, any order amounts mentioned.

TASK 2 — Wykop.pl

Open https://www.wykop.pl/szukaj/#q=gpucomputer

1. Search for: gpucomputer
2. Extract any negative posts, complaints, warnings to community about this seller.
3. Also search: Szklarski gpucomputer

TASK 3 — Google Search for Complaints

Open https://www.google.com
Search: "gpucomputer.pl" oszustwo (fraud)
Search: "gpucomputer.pl" "nie odesłał" OR "nie wysłał" (didn't return / didn't ship)
Search: "gpucomputer.pl" zwrot (refund)

4. Extract all relevant complaint posts, consumer forum threads, or news articles from 2025–2026.
5. Return all findings as JSON.
```

***

## H. Insolvency / Restructuring Filings (Deeper)

### H1 — KRZ (already covered in F1 — run first)

### H2 — MSiG (already covered in F2 — run concurrently)

### H3 — Understanding the Bankruptcy Filing Lag

Polish practice notes: Under art. 21 *Prawa upadłościowego*, a debtor who is insolvent must file a bankruptcy petition within 30 days of becoming insolvent. Once filed, the court issues a decision (*postanowienie*) within a few weeks. The KRZ entry is typically created at the filing stage (not the ruling stage), but manual processing can cause delays of days to a couple of weeks. **The key legal risk under art. 127 §3 PU is the filing date, not the KRZ display date.**[^3]

If the debtor's email (claiming "filed for bankruptcy protection") was sent in, say, March 2026, and a KRZ entry appeared in mid-May 2026 after a month of processing, a *zabezpieczenie* obtained in April 2026 could fall within the 2-month clawback window even though no KRZ entry was visible at the time of filing the lawsuit.

**Practical implication:** Before committing to Path B, your lawyer should make a formal inquiry to SR Kraków-Śródmieście (or SR Kraków for consumer bankruptcy) asking whether any *wniosek o ogłoszenie upadłości* (bankruptcy petition) has been filed under NIP 8661681248 or by Mateusz Szklarski. Courts are not required to proactively disclose this, but your lawyer can file a formal query with reference to pending litigation.

### H4 — Uproszczone Postępowanie Restrukturyzacyjne (UPR)
This restructuring procedure, introduced in 2020, does not require a court filing to commence — the debtor publishes a UPR announcement in MSiG and appoints a supervisor. If a UPR has been opened, it will appear in **MSiG** but may not yet be in KRZ. The MSiG search in F2 will catch this.[^49]

***

## I. Spousal / Family Asset Situation

### I1 — CEIDG Entry Analysis
CEIDG shows no marital property community (*wspólność majątkowa*), which means one of:
1. The debtor is **unmarried** (the most common reason for no entry)
2. There is a formal **rozdzielność majątkowa** (separation of property agreement)
3. A court-ordered separation exists

If unmarried: no spousal assets to trace.  
If separated by agreement: the separation must be in a notarial deed. A separation established *after* the debt arose (after January 2026) is challengeable under **art. 125 PU** (voidable in bankruptcy within 1 year of filing) and under **art. 527 KC** (actio pauliana).

### I2 — Facebook / Social Media — Marital Status
The Facebook profile found at https://www.facebook.com/mateusz.szklarski.982/ shows the debtor living in Kraków with AGH education. Social media may reveal relationship status and family photos that help determine whether a partner exists and whether assets were transferred.[^50]

### I3 — USC (Civil Registry Office) — Marital Records
| Attribute | Detail |
|---|---|
| **Access** | **Restricted.** USC records are not public. Only the person themselves, close relatives, or parties with court authorization can obtain marriage certificates[^9] |
| **Route** | Your lawyer can apply for a certified extract on the basis of documented legal interest in ongoing litigation. This is a formal procedure, typically taking 2–4 weeks. |

**Cannot be executed by a browser agent.** Route to your lawyer.

### I4 — Skarga Pauliańska (Actio Pauliana — Art. 527 KC)
| Attribute | Detail |
|---|---|
| **Purpose** | Challenge transfers of assets to family members or third parties made with intent to defraud creditors[^51][^52] |
| **Requirements** | (1) Creditor's claim existed at time of transfer; (2) Transfer rendered debtor insolvent or more insolvent; (3) Debtor acted with awareness of creditor harm; (4) Third party knew or should have known[^52][^53] |
| **Presumptions** | If the third party is a family member (*osoba bliska*), knowledge is legally presumed[^52] |
| **Limitation period** | 5 years from the date of the challenged transaction (art. 534 KC) |
| **Red flags triggering this** | Real estate transfers to family members visible in KW (Section III or change in Section II owners after January 2026); vehicle transfers visible in used-car ads; business asset transfers to new entities visible in KRS/CRBR |

***

## J. Foreign Assets / Asset-Stripping Risk

### J1 — EU Business Registry Cross-Check
| Attribute | Detail |
|---|---|
| **Tool** | European Business Register (EBR): https://www.ebr.org |
| **Legal access** | Open data |
| **Cost** | Free (basic search) |
| **Caveats** | The debtor mentions a "Hong Kong supplier." Check if he has any registered entity in HK, UK, DE, or other EU countries. |

```prompt-for-browser-agent
TASK 1 — European Business Register

Open https://www.ebr.org

1. Click "Search" and enter: Mateusz Szklarski
2. Select country: try Poland (as cross-check), then Germany, Czech Republic, Slovakia, UK.
3. Extract any registered entities, addresses, or roles found.

TASK 2 — Companies House UK

Open https://find-and-update.company-information.service.gov.uk/

1. Search: Mateusz Szklarski
2. Search: GPUcomputer
3. Extract any results.

TASK 3 — OpenCorporates (multi-country)

Open https://opencorporates.com

1. In the search bar, type: Mateusz Szklarski
2. Filter to exclude Poland (already covered). Check results from other countries.
3. Also search: GPUcomputer
4. Return all findings as JSON.
```

***

### J2 — Cryptocurrency Exposure
| Attribute | Detail |
|---|---|
| **Sources** | gpucomputer.pl (check for crypto payment options in live site and Wayback archives); social media (crypto wallet QR codes or addresses in photos); invoice templates in PDFs found on Wayback Machine |
| **Caveats** | GPU assembly businesses have a natural overlap with crypto mining. If a wallet address is found, blockchain explorers (Etherscan, Blockchain.info) can show current balances. Polish law enforcement can seek exchange KYC data, but individual creditors cannot. |

Include in the G1 prompt: "Check payment options on gpucomputer.pl — does the site offer cryptocurrency payment? If yes, extract any wallet addresses."

***

## Recommended Investigation Plan

### Sequencing — Execution Order

The following sequence is designed to maximize signal per hour and ensure that high-value steps run first while low-cost browser steps run in parallel.

| Priority | Step | Dependency | Agent or Human |
|---|---|---|---|
| **HOUR 1 — Run all in parallel** | | | |
| 1 | A1 — Biała Lista VAT (NIP 8661681248) | None | Browser agent |
| 2 | F1 — KRZ search by name + NIP | None | Browser agent |
| 3 | F2 — MSiG full-text search (4 queries) | None | Browser agent |
| 4 | E1 — KRS person search | None | Browser agent |
| 5 | E2 — CRBR beneficial owner search | None | Browser agent |
| 6 | G1 — Live website test (gpucomputer.pl) | None | Browser agent |
| 7 | C1 — Wayback Machine (gpucomputer.pl, all years) | None | Browser agent |
| **HOUR 2 — Based on Hour 1 results** | | | |
| 8 | A2 — Commercial KW lookup (Mogilska 16 + any new addresses from C1) | C1 addresses | Browser agent |
| 9 | G4 — Customer complaints (Reddit, Wykop, Google) | None | Browser agent |
| 10 | G2 — Social media (Facebook, LinkedIn, Instagram) | None | Browser agent |
| 11 | C2 — Google Maps / Ceneo / Opineo | None | Browser agent |
| 12 | C3 — WHOIS + DNS history | None | Browser agent |
| 13 — **If KW number found in A2** | A3 — EKW viewer | A2 | Browser agent |
| 14 | F5 — Licytacje komornicze search | None | Browser agent |
| **DAY 1 END — Results assessment meeting with lawyer** | | | |
| 15 | B4 — OLX/Allegro equipment listings | None | Browser agent |
| 16 | G3 — Similarweb traffic trend | None | Browser agent |
| 17 | J1 — EU/UK business registries | None | Browser agent |
| 18 | C4 — Business directory check | None | Browser agent |
| 19 | F6 — Rejestr Zastawów (pledge register) | None | Browser agent |
| 20 | E3 — eZamówienia public procurement | None | Browser agent |
| **WEEK 1 — Human/lawyer-assisted** | | | |
| 21 | F3 / F4 — KRD / BIG InfoMonitor subscription | Lawyer NIP or intermediary | Human + browser |
| 22 | I2 — Facebook social media analysis for marital/family info | G2 results | Browser agent |
| 23 | A4 — Geoportal plot ID (for any real address found) | C1/C2 addresses | Browser agent |
| 24 | Portal Informacyjny Sądów — prior litigation search | **Requires in-person court visit** | Lawyer |
| 25 | B3 — CEPiK formal vehicle query | Lawyer letter | Lawyer |

***

### Cost-Effective Stopping Points

**After Hour 1 (cost: 0 PLN browser OSINT):**
If F1/F2 shows an active bankruptcy filing OR no assets are found in A1 (no declared bank accounts) AND KRZ/MSiG shows nothing, consider whether the cost of further investigation is justified. At this point you have zero-cost intelligence.

**After Day 1 (cost: 30–200 PLN for A2 KW lookups + optional KRD/BIG check):**
Assess: Did you find real estate, bank accounts, or a real operating address? If yes, this strongly favors Path B. Proceed to professional escalation.

**Stopping point for browser OSINT — escalate to biuro wywiadu gospodarczego when:**
- All obvious browser OSINT has been exhausted (Wayback Machine, registries, social media)
- KW numbers have not been found by commercial services
- Social media provides no physical address
- Total spend is approaching ~300–500 PLN

At that threshold, a biuro wywiadu gospodarczego (commercial intelligence bureau) report will typically cover: EGiB real estate check, KW lookup by PESEL, vehicle registry check, KRD/BIG/ERIF combined scan, KRS/CRBR, and business address verification. Cost: **500–3,000 PLN, delivered in 1–5 business days**. Services: Creditreform Polska (creditreform.pl), Bisnode Polska, Coface, Dun & Bradstreet PL, KRD's wywiad ekonomiczny add-on.[^54][^55][^56]

**Escalate to detektyw licencjonowany when:**
- You need confirmed physical observation of the debtor's real operating address
- You need photo evidence of vehicles registered at that address
- Browser OSINT provided a candidate address but you need physical confirmation
- Cost: **200–500 PLN/hour**, typically 4–8 hours for an address confirmation = 800–4,000 PLN

***

### Red Flags — Asset Stripping and Sophisticated Evasion

The following patterns, if found, should be immediately flagged to your lawyer as potential bases for:
- **Skarga pauliańska** (art. 527 KC) against third-party recipients
- **Art. 127–128 PU** clawback claims (voidable transactions within 1 year of bankruptcy filing)
- **Emergency application** to court to add the third-party asset to the *zabezpieczenie* scope

| Red Flag | Polish Document Marker | Where Found |
|---|---|---|
| Real estate transferred after January 2026 | Dział II KW: date of *wpis* (entry) post-Jan 2026; or Dział III: *roszczenie pauliańskie* | A3 (EKW viewer) |
| Real estate transferred to family member (spouse, parent, sibling) | Dział II KW: new owner with different surname but matching address | A3 |
| Separation of property agreement (*rozdzielność majątkowa*) filed recently | USC record or notarial act post-January 2025 | Lawyer inquiry, art. 125 PU |
| New KRS entity formed after debt arose (January 2026+) | KRS entity with founding date 2026 + debtor as shareholder | E1 (KRS) |
| Business assets (GPU stock, equipment) listed for sale in bulk at low prices | Allegro/OLX bulk hardware listings from debtor account | B4 / G4 |
| Bank accounts closed or changed after January 2026 | Biała Lista showing accounts deleted + new ones added after Jan 2026 | A1 |
| Sudden website shutdown or "under construction" message | gpucomputer.pl returns 404 or placeholder | G1 |
| Courier returns or known address ceased operations | Wayback Machine showing last address update, combined with social media going dark | C1 / G2 |
| Other creditors already in queue with komornik proceedings | Licytacje komornicze listings for Kraków with debtor name | F5 |
| MSiG listing of *wezwanie wierzycieli* (creditor call) from UPR | MSiG type: "Restrukturyzacja" + "wezwanie wierzycieli" | F2 |
| Email claim of "bankruptcy protection" contradicted by zero KRZ entry | Gap between debtor's claim and empty KRZ | F1 |
| Hong Kong supplier invoked as force majeure | Supplier identified through WHOIS / website / social media; check if supplier company exists at all | C3 / J1 |

***

### Professional Escalation — Who Does What

| Question | Professional | Cost | Output Language |
|---|---|---|---|
| Does he own real estate by name? (systematic national search) | **Biuro wywiadu gospodarczego** (e.g. Creditreform) or **komornik** (after enforcement title) | 500–3,000 PLN (bureau); ~100 PLN + 10% (komornik) | Polish report; usually with English summary on request from international bureaus |
| Is there an undisclosed bankruptcy petition? | **Lawyer** — formal court inquiry to SR Kraków | Included in lawyer's mandate fee | Polish; lawyer translates key findings |
| What vehicles does he own? (by name/PESEL) | **Komornik** (after enforcement title) or **CEPiK formal request via lawyer** | ~100–200 PLN | Polish certificate |
| Prior litigation history as defendant | **Lawyer** — Portal Informacyjny after in-person identity verification | Included in mandate | Polish |
| What bank accounts does he have? | **Komornik** via OGNIVO (requires enforcement title or *postanowienie o zabezpieczeniu*) | Included in enforcement fee | Digital komornik report |
| Physical operating address confirmation | **Detektyw licencjonowany** (licensed PI) | 200–500 PLN/hour; 800–4,000 PLN for full assignment | Polish written report with photos |
| Asset transfer challenge (pauliana) | **Kancelaria adwokacka / radcy prawnego** | Included in case mandate | Polish pleadings |
| Commercial credit intelligence report | **Creditreform** (creditreform.pl), **Bisnode Polska**, **KRD wywiad ekonomiczny** | 500–3,000 PLN | Polish (Creditreform sometimes provides English) |

**Recommendation on escalation timing:**

1. Complete all Hour 1 browser OSINT (free) before spending anything.
2. If A1 (Biała Lista) shows active bank accounts and F1/F2 shows no bankruptcy → this strongly favors Path B and the additional 15–25k PLN cost is well-justified.
3. If no bank accounts appear in A1 and no real estate in A2, commission a **biuro wywiadu gospodarczego** report (500–2,000 PLN) before committing to Path B — the report will systematically search PESEL-linked real estate and BIG/KRD/ERIF.
4. The **detektyw** step is warranted specifically if: (a) you found a candidate real operational address via Wayback/Google Maps/social media, and (b) you need confirmed physical evidence that business assets (GPU servers, assembled computers, equipment) are present at that address for the *wniosek o zabezpieczenie* to specifically target those assets.

***

*All methods in this report are legal under Polish law and GDPR/RODO. No deception, unauthorized access, social engineering, or coercive contact with the debtor is involved. Open-data OSINT findings are informational; formal use as court evidence requires certified copies obtained through official channels.*

---

## References

1. [Central Register and Information on Business Activity (CEIDG)](https://www.kkz.com.pl/en/2025/06/16/central-register-and-information-on-business-activity-ceidg/) - It is a public register that collects information about individuals running businesses and partners ...

2. [CEIDG – Polish-Ukrainian Chamber of Commerce](https://pol-ukr.com/en/ceidg/) - CEIDG provides, among others, the following data: name and surname, NIP, REGON, entrepreneur's addre...

3. [Art.127 i 128 PrUpN - i-kancelaria](https://www.i-kancelaria.pl/artykuly/art-127-i-128-prupn/) - Art. 127. 1. Bezskuteczne w stosunku do masy upadłości są czynności prawne dokonane przez upadłego w...

4. [The White List – how to check key data and a bank account of VAT ...](https://crido.pl/en/blog-taxes/the-white-list-how-to-check-key-data-and-a-bank-account-of-vat-taxpayer-in-poland/) - The White List is a register of taxpayers which is in place since 09.2019 (available on the website:...

5. [Wykaz podatników VAT - wyszukiwarka - Podatki.gov.pl](https://podatki-arch.mf.gov.pl/wykaz-podatnikow-vat-wyszukiwarka/) - Wykaz podatników VAT - wyszukiwarka. Serwis Ministerstwa Finansów.

6. [How can you find out ownership of property in Poland](https://www.reddit.com/r/poland/comments/blnt93/how_can_you_find_out_ownership_of_property_in/) - How can you find out ownership of property in Poland

7. [RODO: Kolejna kara za geoportal](https://biznes.gazetaprawna.pl/artykuly/1489733,geoportal-rodo-puodo-numery-ksiag-wieczystych-kara.html) - Główny geodeta kraju nie ma prawa udostępniać w internecie numerów ksiąg wieczystych – uznał prezes ...

8. [Does Poland have any "land registry" map? - Reddit](https://www.reddit.com/r/poland/comments/1fa41nc/does_poland_have_any_land_registry_map/) - If you know exact lot number (“księga wieczysta”), you might get more detailed information at https:...

9. [Elektroniczne Księgi Wieczyste - Ministerstwo Sprawiedliwości](https://www.gov.pl/web/sprawiedliwosc/elektroniczna-ksiega-wieczysta) - Na portalu Elektroniczne Księgi Wieczyste dostępnym na stronie https://ekw.ms.gov.pl/ możesz: bez lo...

10. [Księgi wieczyste EK, Ekw MS | 797 014 014 - Pewny Lokal](https://pewnylokal.pl/porady/ksiegi-wieczyste-ekw) - Kompleksowy audyt prawny nieruchomości. Księgi wieczyste online — ekw.gov. Treść ksiąg wieczystych j...

11. [Firma Mateusz Szklarski-łopata Gpucomputer - Dane z KRS](https://www.krs-online.com.pl/firma/5516506-mateusz-szklarski-lopata-gpucomputer) - Zobacz NIP, REGON oraz KRS firmy Mateusz Szklarski-łopata Gpucomputer. Zapoznaj się z opiniami klien...

12. [8661681248 Mateusz Szklarski-Łopata Gpucomputer](https://mapa.targeo.pl/8661681248/nip/firma) - NIP: 8661681248, Mateusz Szklarski-Łopata Gpucomputer - dane firmy i pobieranie odpisu KRS za darmo

13. [Rejestry nieruchomości w państwach UE - European e-Justice Portal](https://e-justice.europa.eu/topics/registers-business-insolvency-land/land-registers-eu-countries/pl_pl) - Księgi wieczyste są jawne i każdy może je przeglądać po podaniu numeru księgi wieczystej. ... ekw.ms...

14. [Geoportal pod lupą UODO - GDPR.pl - ochrona danych osobowych ...](https://gdpr.pl/aktualnosci/geoportal-pod-lupa-uodo) - W ostatnim czasie zaobserwować można spore zamieszanie wokół Geoportalu, tj. aplikacji internetowej ...

15. [Sprawdź historię pojazdu - Gov.pl - Portal Gov.pl](https://www.gov.pl/web/gov/sprawdz-historie-pojazdu) - Co musisz zrobić · Wejdź na stronę usługi Historia Pojazdu. · Wpisz numer rejestracyjny, numer VIN i...

16. [Sprawdzenie auta po VIN za darmo - Historia Szkód](https://historiaszkod.pl/blog/2024/09/09/sprawdzenie-auta-po-vin-za-darmo-historia-pojazdu-i-historia-szkod-czym-sie-roznia/) - Jeśli chcesz za darmo sprawdzić samochód po VIN, masz do wyboru dwie strony. To rządowa strona Histo...

17. [Obtain CEPIK Driver Data Poland – Legal Access & Support](https://bsiw.legal/obtaincepikdriverdatapoland/) - We help foreign entities retrieve CEPIK driver data Poland for enforcement of fines and parking tick...

18. [Mateusz Szklarski-Łopata Gpucomputer](https://panoramafirm.pl/ma%C5%82opolskie,,krak%C3%B3w,grzeg%C3%B3rzki,mogilska,16_lok._7/mateusz_szklarski_lopata_gpucomputer-zjpkzc_fnd.html) - Drukarki i urządzenia peryferyjne ✦ Mateusz Szklarski-Łopata Gpucomputer ➤ Kraków, ul. Mogilska (woj...

19. [Look Up DNS History With SecurityTrails](https://help.webhostinghub.com/hc/en-us/articles/11101458588695-Look-Up-DNS-History-With-SecurityTrails) - SecurityTrails enables you to explore complete current and historical data for any internet assets, ...

20. [SecurityTrails | SecurityTrails: Data Security, Threat Hunting, and Attack Surface Management Solutions for Security Teams](https://securitytrails.com) - SecurityTrails enables you to explore complete current and historical data for any internet assets. ...

21. [White list of VAT taxpayers - Wirtualne Biuro Kraków](https://wb.krakow.pl/en/biala-lista/) - Biała lista podatników VAT – Rejestr podatników VAT, z którego korzystają przedsiębiorcy prowadzący ...

22. [Zajęcie Konta w OGNIVO 2026: jak Komornik Znajduje Banki?](https://mamdlugi.pl/ognivo-tutaj-komornik-zajmuje-rachunek-bankowy/) - Komornik, działając przez polski system OGNIVO, nie jest w stanie automatycznie namierzyć i zająć ko...

23. [Co to jest system Ognivo i jak działa? | SMART Bankier.pl](https://www.bankier.pl/smart/co-to-jest-system-ognivo-i-jak-dziala) - Jednym z najważniejszych zastosowań aplikacji Ognivo jest poszukiwanie majątku dłużnika w ramach pos...

24. [OGNIVO | Komornik Sądowy - Łukasz Wiśniewski](https://www.komorniklimanowa.pl/8/ognivo) - Komornik Sądowy jest uprawniony do ustalenia majątku dłużnika, z którego może być poprowadzona egzek...

25. [National Court Register (KRS) | Department for Foreigners](https://migrant.poznan.uw.gov.pl/en/slownik-pojec/national-court-register-krs) - In the registry, you can check the following: current company status, company headquarters, chairman...

26. [National Court Register (KRS) - getsix](https://getsix.eu/resources/doing-business-in-poland/national-court-register/) - Additionally, on the website https://wyszukiwarka-krs.ms.gov.pl/, you can search for entities listed...

27. [Szukaj w KRS](https://rejestr.io) - Sprawdź wygodnie aktualne i historyczne dane o spółkach, fundacjach, stowarzyszeniach i osobach. Zna...

28. [Poland KRS Board Members & Shareholders Scraper - Apify](https://apify.com/regdata/krs-fullnames-scraper) - Get full, non-anonymized board member and shareholder names from Poland's National Court Register (K...

29. [Centralny Rejestr Beneficjentów Rzeczywistych – Wikipedia, wolna encyklopedia](https://pl.wikipedia.org/wiki/Centralny_Rejestr_Beneficjent%C3%B3w_Rzeczywistych)

30. [Centralny Rejestr Beneficjentów Rzeczywistych - CRBR - iAML](https://www.iaml.com.pl/wiedza/centralny-rejestr-beneficjentow-rzeczywistych/) - Od 13 października 2019: Centralny Rejestr Beneficjentów Rzeczywistych – jawny i nieodpłatny rejestr...

31. [Informacje publiczne w ogólnodostępnych źródłach – Centralny Rejestr Beneficjentów Rzeczywistych](https://informacjapubliczna.org/news/centralny-rejestr-beneficjentow-rzeczywistych/) - Po analizie Krajowego Rejestru Sądowego (KRS), Centralnej Ewidencji i Informacji o Działalności Gosp...

32. [Krajowy Rejestr Zadłużonych - Ministerstwo Sprawiedliwości - Gov.pl](https://www.gov.pl/web/sprawiedliwosc/krajowy-rejestr-zadluzonych)

33. [FAQ - Ministerstwo Sprawiedliwości - Portal Gov.pl](https://www.gov.pl/web/sprawiedliwosc/faq3)

34. [Polish National Debtors Register is now operational!](https://rkkw.pl/en/aktualnosci/polish-national-debtors-register-is-now-operational/) - Registered User Portal – in which, after registration, you can submit applications and procedural wr...

35. [Wyszukiwarka MSiG](https://wnioski-msig.ms.gov.pl)

36. [Monitor Sądowy i Gospodarczy - Ministerstwo Sprawiedliwości](https://wyszukiwarka-msig.ms.gov.pl) - Monitor Sądowy i Gospodarczy. A; A; A. Wyszukiwanie ogłoszeń. Pobierz monitor. Nazwa podmiotu. Numer...

37. [Czym jest Krajowy Rejestr Długów? Jak sprawdzić KRD za darmo?](https://www.bankier.pl/smart/krajowy-rejestr-dluznikow-krd-jak-sprawdzic-baza-krd) - Możliwość sprawdzenia siebie w KRD za darmo. Zasadniczo informacje i raporty przechowywane w Krajowy...

38. [Aplikacja KRD Mobile. Sprawdzanie firm i monitoring kontrahentów](https://krd.pl/aplikacja-krd-mobile-sprawdzanie-firm) - Aplikacja KRD Mobile (dalej Aplikacja KRD) to narzędzie, które umożliwia przedsiębiorcom szybkie spr...

39. [[PDF] Cennik serwisu ERIF dla konsumentów](https://erif.pl/wp-content/uploads/cennik-serwisu-dla-konsumentow_2025.pdf) - BIURO INFORMACJI GOSPODARCZEJ INFOMONITOR S.A.. 30,00 PLN. KRAJOWE BIURO INFORMACJI GOSPODARCZEJ S.A...

40. [Ile kosztuje wpisanie dłużnika do KRD i jakie są dodatkowe ...](https://przekredytowani.pl/ile-kosztuje-wpisanie-dluznika-do-krd-i-jakie-sa-dodatkowe-oplaty) - Ile kosztuje wpisanie dłużnika do KRD? Sprawdź, jakie są dodatkowe opłaty i jak rejestracja wpływa n...

41. [Dopisz dłużnika do KRD BIG S.A. Zgłoś wpis do BIG.](https://krd.pl/oferta-krd/dopisz-dluznika) - Klient nie płaci? Dopisz dłużnika do biura informacji gospodarczej i zwiększ szanse na odzyskanie na...

42. [BIG InfoMonitor](https://www.big.pl) - BIG InfoMonitor – sprawdzanie kontrahentów w Rejestrze Dłużników, monitoring firm, dostęp do danych ...

43. [infomonitor.pl](https://www.infomonitor.pl) - Chcę pobrać raport z BIG InfoMonitor; Chcę sprawdzać firmy i konsumentów; Chcę wysłać wezwanie do za...

44. [Jak zamówić raport BIG o sobie? | BIG.pl - BIG InfoMonitor](https://www.big.pl/baza-wiedzy/raport-o-sobie) - Do rejestru dłużników i ty moższ zostać wpisany.Czy Twoje dane przypadkiem tam nie trafiły? Jak zamó...

45. [Elektroniczny dostęp do Rejestru Zastawów - Gov.pl](https://www.gov.pl/web/sprawiedliwosc/elektroniczny-dostep-do-rejestru-zastawow) - W celu skorzystania z CI RZ konieczne jest założenie konta w Portalu Rejestrów Sądowych w systemie T...

46. [Udzielanie informacji, wydawanie odpisów i zaświadczeń z Rejestru ...](https://arch-bip.ms.gov.pl/pl/rejestry-i-ewidencje/rejestr-zastawow/udzielanie-informacji-wydawanie-odpisow-i-zaswiadczen-z-rejestru-zastawow/) - Udzielaniem informacji, wydawaniem odpisów i zaświadczeń z rejestru zastawów zajmuje się Centralna I...

47. [Portal Informacyjny Sądów Powszechnych](https://warszawapraga.so.gov.pl/artykul/171/114/portal-informacyjny-sadow-powszechnych) - Informacje ogólne Portal Informacyjny umożliwia pełnomocnikom i innym osobom uprawnionym i upoważnio...

48. [Portal informacyjny / Sądy w internecie /](https://osrodkipomocy.ms.gov.pl/pl/sady-w-internecie/portal-informacyjny/)

49. [Nowa wyszukiwarka o głoszeń i obwieszczeń publikowanych w ...](https://www.gov.pl/web/sprawiedliwosc/nowa-wyszukiwarka-o-gloszen-i-obwieszczen-publikowanych-w-monitorze-sadowym-i-gospodarczym) - na stronie https://prs.ms.gov.pl/ w zakładce KRS została udostępniona wyszukiwarka ogłoszeń i obwies...

50. [Mateusz Szklarski - Facebook](https://www.facebook.com/mateusz.szklarski.982/) - Mateusz Szklarski ; 󱜏. Lives in Kraków, Poland ; 󱜧. Studied at Akademia Górniczo-Hutnicza w Krakowie...

51. [Skarga pauliańska 2026: co to jest i jak się bronić](https://kancelariamw.pl/skarga-paulianska-co-to-jest/) - Przesłanki skargi pauliańskiej (actio pauliana) znajdziemy w art. 527 k.c. Muszą wystąpić łącznie. B...

52. [Actio Pauliana – aplikacje prawnicze - Edukacja prawnicza](https://www.edukacjaprawnicza.pl/actio-pauliana-aplikacje-prawnicze/) - Przepis art. 527 KC określa przesłanki wystąpienia z roszczeniami przez pokrzywdzonych wierzycieli. ...

53. [Skarga pauliańska – podstawowy instrument ochrony wierzyciela ...](https://codozasady.pl/p/skarga-paulianska-podstawowy-instrument-ochrony-wierzyciela-przed-niewyplacalnoscia-dluznika) - Art. 527 § 1 k.c. (podstawowy przepis regulujący skargę pauliańską) stanowi: Gdy wskutek czynności p...

54. [Wywiadownia sprawdzi wiarygodność](https://businessandbeauty.pl/wywiadownia-sprawdzi-wiarygodnosc/) - Celem każdego przedsiębiorcy prowadzącego działalność gospodarczą jest minimalizacja ryzyka współpra...

55. [Tajemnice po rozsądnych cenach](https://www.rp.pl/opinie-ekonomiczne/art14005581-tajemnice-po-rozsadnych-cenach) - Nowego kontrahenta czy partnera w interesach można dokładnie sprawdzić już za kilkaset złotych

56. [Wywiadownia gospodarcza, raporty handlowe, wywiad gospodarczy, raporty gospodarcze, sprawdzanie firm zagranicznych, windykacja międzynarodowa i krajowa, windykacja masowa, wyjawienie majątku, wyjawienie nieruchomości i ruchomości, certyfikaty wiarygodności firm, poszukiwania dłużnika, detektyw gospodarczy. | Creditreform Polska Sp. z o.o.](http://www.creditreform.pl)

