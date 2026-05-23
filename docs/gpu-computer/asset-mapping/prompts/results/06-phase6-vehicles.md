## PHASE 6 REPORT: Vehicles & High-Value Asset Reconnaissance

```json
{
  "phase": 6,
  "title": "Vehicles & High-Value Asset Reconnaissance",
  "subject": {"name": "Mateusz Szklarski-Łopata", "trading_as": "GPUcomputer", "NIP": "8661681248"},

  "task1_olx": {
    "queries_run": [
      {"q": "gpucomputer", "url": "https://www.olx.pl/oferty/q-gpucomputer/", "result_count": 70, "english": "70 unrelated PC listings from Rumia, Trąbki Wielkie, Sochaczew, Piła, Szubin — none in Kraków, no branded items. Pure keyword collisions.", "screenshot": "[screenshot:2]"},
      {"q": "883109779", "url": "https://www.olx.pl/oferty/q-883109779/", "result_count": 0, "english": "Zero listings — phone never used on OLX.", "screenshot": "[screenshot:3]"},
      {"q": "531061452", "url": "https://www.olx.pl/oferty/q-531061452/", "result_count": 0, "english": "Zero listings — second mobile (discovered Phase 5) also unused on OLX.", "screenshot": "[screenshot:4]"}
    ],
    "vehicles_found": [],
    "liquidation_signals": "NONE. No GPUs, no workstations, no PC parts being individually sold off at below-market prices under the debtor's known phones."
  },

  "task2_otomoto": {
    "query": "gpucomputer",
    "url": "https://www.otomoto.pl/osobowe/q-gpucomputer",
    "result_count": 0,
    "english": "0 ogłoszeń — 'Niczego nie znaleźliśmy' (We found nothing). No vehicles listed by the debtor on Poland's main car marketplace.",
    "screenshot": "[screenshot:5]"
  },

  "task3_allegrolokalnie_allegro": {
    "allegrolokalnie": {"url": "https://allegrolokalnie.pl/oferty?string=gpucomputer", "result": "Search URL silently redirected to homepage — no public seller profile or listings discoverable for 'gpucomputer' on AllegroLokalnie.", "screenshot": "[screenshot:6]"},
    "allegro_main": {"url": "https://allegro.pl/listing?string=gpucomputer&order=qd", "result_count_keyword": 121, "result_seller_match": 0, "english": "121 generic keyword matches (products with 'gpu computer' in title), but NO listing identifiable as the debtor's seller account. Allegro user/seller search bot-blocked in Phase 5. No liquidation signals.", "screenshot": "[screenshot:7]"}
  },

  "task4_google_street_view": {
    "address_1": {
      "address": "ul. Kazimierza Wielkiego 36, 30-074 Kraków (Krowodrza district)",
      "source": "Phase 5 EV-05-03 — verified by FirmaGodnaZaufania (Nov 2025)",
      "street_view_observations": "Residential tenement (kamienica) with small ground-floor commercial premises (red signage above door). One silver compact car parked in front (Skoda Fabia / VW Polo class — make uncertain). Plate not readable (Google blurs). No branded 'GPUcomputer' vehicle, no logo signage on the building exterior. Building is a typical pre-war Kraków residential block with retail/workshop on ground floor — fully consistent with the hypothesis that this is the owner's residence + small workshop / pickup point.",
      "vehicles_with_plates": [],
      "branding_visible": false,
      "screenshot": "[screenshot:9]"
    },
    "address_2_fallback": {
      "address": "ul. Mogilska 16, 31-516 Kraków",
      "street_view_observations": "Large modern office building near Rondo Mogilskie (next to Unity Tower, Court of Appeals, Sąd Apelacyjny). Ground floor 'Suntek' signage. No GPUcomputer branding. As expected for the WorkDesk virtual-office address — heavy foot traffic, multiple unrelated tenants.",
      "vehicles_with_plates": [],
      "screenshot": "[screenshot:11]"
    }
  },

  "task5_historiapojazdu": {
    "status": "SKIPPED",
    "reason": "No registration plate or VIN obtained in Tasks 1–4. Pre-condition not met."
  },

  "task6_autodna_pricing": {
    "status": "SKIPPED",
    "reason": "No VIN obtained. Also no purchase authorization — would not run even with VIN."
  },

  "actionable_intelligence": {
    "vehicles_confirmed_linked": "NONE — no marketplace listings under any of the debtor's three phone numbers, no branded vehicles on Street View at either address, no operational photos found.",
    "liquidation_signals": "NONE detected via OSINT marketplaces. Either the business is NOT distress-selling its inventory, OR it is using channels invisible to OSINT (B2B direct, EU export, crypto-payment).",
    "plate_or_vin_for_lawyer_routed_CEPiK": "NOT AVAILABLE — no OSINT path produced an identifier. The official CEPiK owner-by-name lookup (via Profil Zaufany, lawyer-routed) is the ONLY remaining channel to determine whether the debtor owns any registered vehicle.",
    "client_action": "Instruct lawyer to file a CEPiK owner-by-name request (wniosek o udostępnienie danych z CEPiK, art. 80c ust. 2 ustawy Prawo o ruchu drogowym) citing the EPU writ as legitimate interest. Cost ~30 PLN, turnaround 2–4 weeks. This is the only realistic way to confirm/deny vehicle ownership for the seizure file.",
    "path_evaluation": "Reinforces Path A (Stay EPU + Hollow-Shell sole-trader profile). The TOTAL ABSENCE of marketplace footprint combined with active Instagram lifestyle spend (Travis Scott concert, FLC festival per Phase 5) strengthens the 'cash-flow positive but evading via off-marketplace channels' hypothesis."
  },

  "escalation_triggers": "None met."
}
```
