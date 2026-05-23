## PHASE 5 REPORT: Operating Address Reconnaissance

> **Note (saved 2026-05-23):** The source paste was truncated mid-sentence at the end of `task6_social_media.instagram_matt_renton.citation`. Tasks 7+ (if any), the closing of `task6_social_media`, and any top-level summary / decision-frame section are missing. Content below is verbatim from what was provided.

```json
{
  "phase": 5,
  "title": "Operating Address Reconnaissance",
  "subject": {
    "name": "Mateusz Szklarski-Łopata",
    "trading_as": "GPUcomputer",
    "NIP": "8661681248",
    "REGON": "362678345"
  },

  "task1_wayback": {
    "snapshots": [
      {
        "snapshot_date": "2016-12-31",
        "page": "/kontakt-z-nami/",
        "addresses_found": [],
        "phones_found": [],
        "emails_found": [],
        "bank_accounts_found": [],
        "english_summary": "Only a contact form, no operational data."
      },
      {
        "snapshot_date": "2019-10-25",
        "page": "/o-nas/ (About us)",
        "addresses_found": ["ul. Mogilska 16/7, 30-074 Kraków (NOTE: postcode 30-074 is the Kazimierza Wielkiego district, NOT the real 31-516 Mogilska postcode — likely a typo carried over from the older Kazimierza Wielkiego 36/3 address)"],
        "phones_found": ["+48 12 333 77 30 (landline)", "+48 883 109 779 (mobile)"],
        "emails_found": ["waldek@gpucomputer.pl (configurations / a second person named Waldek)", "mateusz@gpucomputer.pl"],
        "bank_accounts_found": [],
        "english_summary": "Mentions two brand names: 'GPUCOMPUTER' (stations) and '3dkrakow' (servers). Reveals a second person 'Waldek' as a partner/contact for configurations.",
        "screenshot": "[screenshot:6]"
      },
      {
        "snapshot_date": "2025-02-12",
        "page": "/kontakt",
        "addresses_found": ["ul. Mogilska 16/7, 31-516 Kraków (correct postcode)"],
        "phones_found": ["+48 883 109 779", "+48 12 333 77 30"],
        "emails_found": ["gpucomputer@gpucomputer.pl", "waldek@gpucomputer.pl", "mateusz@gpucomputer.pl"],
        "bank_accounts_found": [],
        "english_summary": "Current contact page shows only the virtual office address — no pickup point, no workshop, no IBAN.",
        "screenshot": "[screenshot:3]"
      }
    ],
    "non_mogilska_addresses": ["None directly disclosed in archived /kontakt or /o-nas. The 30-074 postcode anomaly hints at residual ties to ul. Kazimierza Wielkiego 36 lok. 3 (postcode 30-074)."],
    "regulamin_status": "404 — no Terms of Service page ever archived (significant — a 10-year-old e-commerce site should have one; likely they ran B2B-only or never published consumer terms)."
  },

  "task2_google_maps": {
    "GPUcomputer_Kraków": {
      "result": "NO business listing exists on Google Maps for 'GPUcomputer'. Search returned only unrelated competitor PC shops (Progress Systemy, GOODFIX, Bit Computer, ArtiComp).",
      "screenshot": "[screenshot:8]"
    },
    "phone_883_109_779": {
      "result": "Google Maps could not find this phone — no associated business or residential pin.",
      "screenshot": "[screenshot:9]"
    },
    "actionable": "Total absence of a Google Maps presence is itself a red flag — a 10-year-old hardware vendor with NO map listing strongly implies pure e-commerce/dropship operation with no customer-visit premises."
  },

  "task3_marketplace_reviews": {
    "allegro": {"result": "Bot block returned blank page; no public seller profile found via user search.", "reviews": []},
    "ceneo": {"result": "'Brak wyników dla frazy wyszukiwania gpucomputer' — no shop entry, no product listings.", "screenshot": "[screenshot:11]"},
    "opineo": {"result": "404 / no profile.", "screenshot": "[screenshot:13]"},
    "allegrolokalnie": {"result": "Not searched separately — Allegro main returned nothing"},
    "english_summary": "ZERO marketplace footprint. For a 10-year-old PC-builder business this is highly atypical. Suggests B2B/direct-sale-only model, OR business has scaled down to near-zero retail activity."
  },

  "task4_directories": {
    "targeo": {
      "result": "NIP query returned only unrelated 'Serwis Ogumienia GRES B.Kluka' in Kudowa-Zdrój. The direct profile URL provided is dead; no current Targeo listing for the debtor.",
      "screenshot": "[screenshot:15]"
    },
    "firmagodnazaufania": {
      "url": "https://www.firmagodnazaufania.pl/company,50850,mateusz-szklarski-lopata-gpucomputer",
      "verification_date": "2025-11-18",
      "address_listed": "ul. Kazimierza Wielkiego 36 lok. 3, 30-074 Kraków",
      "NIP": "8661681248",
      "REGON": "362678345",
      "founded": "2015",
      "english_summary": "MAJOR FINDING — this directory STILL LISTS the historical Kazimierza Wielkiego 36/3 address as the current operating address (verified Nov 2025). Corroborates the user's prior intelligence and strongly suggests this was/is the real workshop or owner's residence prior to the move to the Mogilska virtual office.",
      "screenshot": "[screenshot:14]"
    },
    "krs_online": {
      "url": "https://www.krs-online.com.pl/firma/5516506-mateusz-szklarski-lopata-gpucomputer",
      "address_listed": "Mogilska 16 lok. 7, 30-074 Kraków, woj. małopolskie (note 30-074 anomaly again)",
      "phone_listed": "+48 531 061 452 (THIRD PREVIOUSLY-UNKNOWN MOBILE NUMBER)",
      "PKD": "26.20.Z (Production of computers and peripheral devices)",
      "reviews": 0,
      "english_summary": "Discloses an additional mobile +48 531 061 452 — distinct from the user's known +48 883 109 779. This is a high-value enforcement lead (new bank-account fingerprint, possible Revolut/iKonto linked to this number).",
      "screenshot": "[screenshot:17]"
    },
    "panoramafirm": {
      "direct_url": "404 (listing removed/expired)",
      "cached_via_search": "ul. Mogilska 16 lok. 7, 31-516 Kraków Grzegórzki; phone '531 061...' confirms the new mobile",
      "screenshot": "[screenshot:19]",
      "citation": "[web:24]"
    },
    "aleo": {"result": "'Niestety, nie znaleźliśmy pasujących wyników dla 8661681248' — no profile.", "screenshot": "[screenshot:20]"},
    "pkt": {"result": "No specific listing surfaced via search."},
    "gowork": {"result": "No employer profile / no employee reviews."},
    "oneplace_marketplanet": {
      "url": "https://oneplace.marketplanet.pl/baza-firm/-/bc/company/61989/mateusz-szklarski-gpucomputer",
      "address_listed": "ul. Mogilska 16 lok. 7, 31-516 Kraków",
      "english_summary": "B2B procurement directory listing — registered for public-tender visibility, suggests subject targets corporate/government buyers.",
      "citation": "[web:21]"
    },
    "oceniamy.to": {
      "address_listed": "ul. Mogilska 16/7, 31-516 Kraków",
      "citation": "[web:30]"
    },
    "third_undocumented_addresses": ["None — only Mogilska 16/7 and Kazimierza Wielkiego 36/3 surfaced. No third workshop/warehouse located."]
  },

  "task5_whois_dns": {
    "dns_pl_nask": "Login/CAPTCHA gate; for .pl domains registered by natural persons NASK redacts registrant data — typical result would be REDACTED FOR PRIVACY.",
    "whois_com": "CAPTCHA block — Security Check (I'm not a robot). Stopped per policy. [screenshot:33]",
    "viewdns_info": "Cloudflare CAPTCHA / 'Performing security verification' — bot block. Stopped per policy. [screenshot:34]",
    "securitytrails": "Not attempted (typically login-walled).",
    "english_summary": "WHOIS infrastructure tasks BLOCKED by anti-bot defences across all three providers. RECOMMEND: client run `whois gpucomputer.pl` from a local terminal or use https://who.is/whois/gpucomputer.pl — those typically return registrant email (REDACTED but admin-c handle is sometimes visible) and the hosting IP. The reverse-IP lookup is the most valuable subtask still pending."
  },

  "task6_social_media": {
    "facebook_page_gpucomputer": {
      "url": "https://www.facebook.com/gpucomputer/",
      "likes": 7,
      "description": "Stacje Robocze i serwery. Najnowsze technologie w przystępnych cenach.",
      "english_summary": "Essentially dormant — only 7 likes after 10 years of business. No location tags, no asset photos visible publicly. Page is effectively abandoned.",
      "citation": "[web:48][web:49]"
    },
    "facebook_personal_mateusz_szklarski_982": {
      "url": "https://www.facebook.com/mateusz.szklarski.982/",
      "data": {
        "location": "Lives in Kraków, Poland",
        "college": "Akademia Górniczo-Hutnicza w Krakowie (AGH University of Science and Technology)",
        "high_school": "Technikum kolejowe w Krakowie (Railway Technical School Kraków)"
      },
      "english_summary": "HIGH-CONFIDENCE match to the debtor (Kraków + AGH technical background fits the IT-hardware JDG profile). Beyond About info, full posts blocked by login wall.",
      "screenshot": "[screenshot:59]",
      "citation": "[web:52]"
    },
    "instagram_matt_renton": {
      "url": "https://www.instagram.com/matt_renton/",
      "display_name": "Mateusz Szklarski",
      "metrics": "1,068 posts, 1,837 followers, 4,578 following",
      "story_highlights": ["Travis 26.08.24 (Travis Scott concert Warsaw 26 Aug 2024)", "FLC 2023", "MelQui", "No..."],
      "recent_posts": "Concert photography (Zuco103, club venues)",
      "english_summary": "MODERATE-confidence match (name only — Szklarski not Szklarski-Łopata). Lifestyle signals: active concert-going (Travis Scott PL Tour, FLC festival 2023) — indicates discretionary spend on entertainment/travel despite the unpaid 155k PLN debt. Login wall blocks deeper post analysis.",
      "screenshot": "[screenshot:47]",
      "citation
```

**[TRUNCATED — source paste cut off here mid-string. Anything after this point (close of `task6_social_media`, additional tasks, summary, decision-frame) was not received.]**
