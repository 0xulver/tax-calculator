# Phase 1 Quick Wins — Results for GPUcomputer / Mateusz Szklarski (NIP 8661681248)

## Summary (English)
The debtor's JDG is **fully active and operational** across all four registers. **No insolvency or restructuring signals** were found anywhere (KRZ clean, MSiG clean, CEIDG shows no bankruptcy annotation, VAT status "Czynny"/Active). One declared bank account exists on Biała Lista — same on both 23-05-2026 and 15-01-2026 (no accounts closed since January). This profile is consistent with **Scenario B (Cash Flow Positive but Evading)** from your master plan — Path B (zabezpieczenie on live operating account) appears viable.

***

## Task 1 — VAT Whitelist (Biała Lista) [podatki-arch.mf.gov](https://podatki-arch.mf.gov.pl/wykaz-podatnikow-vat-wyszukiwarka/)
```json
{
  "vat_status_today": "Czynny (Active) — as of 23-05-2026",
  "entity_name_shown": "MATEUSZ SZKLARSKI",
  "registered_address_shown": "MOGILSKA 16/7, 31-516 KRAKÓW",
  "nip": "8661681248",
  "regon": "362678345",
  "krs": "-",
  "date_of_vat_registration": "2015-10-14",
  "bank_accounts_today": ["84 2490 0005 0004 5309 1276 540"],
  "bank_accounts_2026_01_15": ["84 2490 0005 0004 5309 1276 540"],
  "accounts_closed_since_january": [],
  "wykreslony_terminal_indicator": false,
  "query_date": "2026-05-23"
}
```
Note: The IBAN displayed is **PL84 2490 0005 0004 5309 1276 540** — this corresponds to **Alior Bank** (sort code 2490). Single declared account only. The "zero declared bank accounts" escalation trigger is **not** met, but a single-account fingerprint is still a relatively thin attack surface for komornik enforcement.

## Task 2 — KRZ (Krajowy Rejestr Zadłużonych) [krz.ms.gov](https://krz.ms.gov.pl/#!/application/KRZPortalPUB/1.9/KrzRejPubGui.WyszukiwaniePodmiotow?params=JTdCJTdE&itemId=item-2&seq=0)
```json
{
  "krz_hit": false,
  "searches_run": [
    {"type": "NIP 8661681248 (osoba fizyczna prowadząca działalność)", "result": "Nie zostały znalezione żadne pozycje (No items found)"},
    {"type": "Name: Mateusz Szklarski", "result": "Nie zostały znalezione żadne pozycje"},
    {"type": "Firma: GPUcomputer", "result": "Nie zostały znalezione żadne pozycje"}
  ],
  "summary": "No bankruptcy, restructuring, or failed-enforcement proceedings registered against the debtor in KRZ.",
  "caveat": "Per art. 27 PU, a court has up to 2 months to process a bankruptcy petition — so a freshly-filed petition could still be invisible. MSiG (Task 3) cross-check is also clean.",
  "query_date": "2026-05-23"
}
```

## Task 3 — MSiG (Monitor Sądowy i Gospodarczy) [wyszukiwarka-msig.ms.gov](https://wyszukiwarka-msig.ms.gov.pl/)
```json
{
  "msig_hit": false,
  "searches_run": [
    {"criterion": "Nazwa podmiotu: GPUcomputer", "result": "Brak wyników (No results)"},
    {"criterion": "Nazwa podmiotu: Mateusz Szklarski", "result": "Brak wyników"},
    {"criterion": "NIP: 8661681248", "result": "Brak wyników"},
    {"criterion": "Tekst w treści: Szklarski Mateusz", "result": "Brak wyników"}
  ],
  "date_range_searched": "2021-05-06 to 2026-05-23",
  "summary": "No insolvency, restructuring, liquidation, or creditor-call notices found in the MSiG official gazette."
}
```

## Task 4 — CEIDG [aplikacja.ceidg.gov](https://aplikacja.ceidg.gov.pl/ceidg/ceidg.public.ui/SearchDetails.aspx?Id=fdec08ca-5249-465b-bee3-36e5d4246463)
```json
{
  "full_business_name": "MATEUSZ SZKLARSKI GPUCOMPUTER",
  "entrepreneur": "MATEUSZ SZKLARSKI",
  "status": "Aktywny (Active)",
  "activity_start_date": "2015-10-06",
  "date_of_strike_off": null,
  "suspension": null,
  "registered_address": "ul. Mogilska 16/7, 31-516 Kraków, woj. małopolskie",
  "correspondence_address": "ul. Mogilska 16/7, 31-516 Kraków-Śródmieście",
  "additional_places_of_business": null,
  "nip": "8661681248",
  "regon": "362678345",
  "citizenship": "Polska",
  "pkd_primary": "26.20.Z (Produkcja komputerów i urządzeń peryferyjnych — Production of computers and peripherals)",
  "pkd_all": ["26.20.Z","46.42.Z","46.51.Z","47.24.Z","47.41.Z","47.42.Z","47.43.Z","47.59.Z","47.91.Z","56.10.A","56.10.B","58.21.Z","62.01.Z","62.02.Z","62.09.Z","63.11.Z","63.12.Z","64.19.Z","69.20.Z","82.19.Z","95.11.Z"],
  "marital_property_community": "Nie (No — separation of property)",
  "bankruptcy_restructuring_annotation": null,
  "succession_manager": null,
  "procurators": null,
  "contact_email_on_record": null,
  "contact_phone_on_record": null
}
```

***

## Key observations / flags for next phases
- **No terminal indicators triggered.** Continue to Phases 2–7.
- **Marital property: separation ("Nie").** This is meaningful for Phase 2 — any real estate would be in his name alone, not joint with spouse, so EKW lookups will be cleaner. It also forecloses the easy "asset is in wife's name" defense, but a deed-of-donation skarga pauliańska risk remains.
- **Wide PKD scope** (retail 47.xx, food service 56.10.A/B, legal 69.20.Z, cleaning 95.11.Z) — unusually broad for a 26.20.Z hardware JDG. Worth flagging to your lawyer; may indicate the entity has been repurposed or kept "open" for opportunistic invoicing.
- **Single Alior Bank account** is the only komornik attack point currently disclosed. Compare against the bank account that appeared on the original GPUcomputer invoice/order confirmation — if it differs, that's a smoking gun (undeclared account).
- **CEIDG correspondence address** = same Mogilska 16/7 virtual office. Phase 5 (real operating address) becomes important.

Recommended next step per master plan: run **Phase 3 (other creditors)** and **Phase 5 (real operating address)** in parallel — both are independent and high-value given this profile.
