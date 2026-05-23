# Phase 3 — Other Creditors and Encumbrances

Goal: detect whether other creditors are already executing against the debtor, whether his movable assets are pledged, and whether he has tax debts. This shapes my queue position and recovery probability.

**Time:** 15–30 minutes of agent runtime.
**Cost:** 0 PLN.

Note: KRD and BIG InfoMonitor are not included here because they require contractual business-account access. They are routed to your lawyer separately.

---

````
```prompt-for-browser-agent
You are checking whether a Polish JDG debtor already has other creditors enforcing against him, pledges over his movables, or active bailiff auctions. Open-data sources only.

=== SUBJECT ===
Full name: Mateusz Szklarski-Łopata
Trading as: GPUcomputer
NIP: 8661681248
REGON: 362678345
Kraków-based JDG

=== TASK 1 — REJESTR ZASTAWÓW (REGISTER OF PLEDGES OVER MOVABLES) ===

Goal: find any registered pledges (zastawy rejestrowe) over the debtor's machinery, equipment, vehicles, inventory, or business assets. These pledges give the pledgee priority over my unsecured claim.

1. Open https://prs.ms.gov.pl
2. On the homepage, find the section/tile labeled "Centralna Informacja" or "Rejestr Zastawów" (Pledge Register). Click it.
3. If a "Tożsamość" (Identity) account registration prompt appears for paid certificates, do NOT register — record "Certificate requires account, skip" and continue with the free query.
4. Free query section — look for a search form. Enter:
   - NIP: 8661681248
   - Then a separate search by name: Mateusz Szklarski
5. For any pledge entry returned, extract:
   - "Zastawca" (Pledgor) name
   - "Zastawnik" (Pledgee — i.e. the secured creditor)
   - Description of pledged asset
   - Pledge value
   - Registration date
   - Pledge serial number

Return Task 1 as JSON.

=== TASK 2 — REJESTR ZASTAWÓW SKARBOWYCH (TAX PLEDGE REGISTER) ===

Goal: check whether the tax office (Urząd Skarbowy) holds a statutory pledge over the debtor's assets for unpaid tax debts.

1. Open https://www.podatki.gov.pl and search the page for "rejestr zastawów skarbowych" (tax pledge register), or go directly to https://rzs.mf.gov.pl if that URL is live in 2026.
2. Find the public search form.
3. Search by NIP: 8661681248.
4. Search by name: Mateusz Szklarski.
5. For any entry returned, extract: subject of pledge, amount, date, tax authority.

Return Task 2 as JSON. If the portal is not findable, search Google for "rejestr zastawów skarbowych wyszukiwarka" and follow the official .gov.pl link.

=== TASK 3 — LICYTACJE KOMORNICZE (BAILIFF AUCTION LISTINGS) ===

Goal: detect if a bailiff has already seized and listed any of the debtor's assets for public auction. Presence here means at least one other creditor has an enforcement title and the komornik is actively converting assets to cash.

1. Open https://licytacje.komornik.pl/wyszukiwarka/obwieszczenia-o-licytacji
2. Find any search/filter form. Run separate searches:
   - Name field: Mateusz Szklarski
   - Name field: GPUcomputer
   - If a city/voivodeship filter is available: Kraków / Małopolskie
   - NIP if a field accepts it: 8661681248
3. For each listing extract: debtor name, asset type and description, location, court / komornik name, case signature, auction date, starting price.
4. Also check the legacy archive at https://ool.komornik.pl for older listings (pre-2026-02-27).

Return Task 3 as JSON.

=== TASK 4 — PORTAL ORZECZEŃ (COURT RULINGS DATABASE) ===

Goal: find prior anonymized court rulings involving the debtor. Even though Polish court rulings are anonymized for privacy, identifiers (NIP, specific addresses, business name fragments) can sometimes survive and confirm prior litigation.

1. Open https://orzeczenia.krakow.so.gov.pl/a (Kraków Regional Court rulings portal)
2. Locate the advanced search form ("Wyszukiwanie zaawansowane" = Advanced search).
3. In the field labeled "Treść orzeczenia" (Content of the ruling), enter: GPUcomputer
4. If a court selector exists labeled "Sąd" (Court), select "Sąd Rejonowy dla Krakowa-Krowodrza" and "Sąd Rejonowy dla Krakowa-Śródmieścia".
5. Click "Szukaj" (Search).
6. Record any rulings returned. For each: date, case signature, court, brief English summary of subject matter.
7. Repeat searches in "Treść orzeczenia" with:
   - 8661681248 (the NIP — sometimes survives anonymization in fact patterns)
   - 362678345 (REGON)
   - Mateusz Szklarski
   - Szklarski-Łopata
   - Mogilska 16
8. Also try the national portal: https://orzeczenia.ms.gov.pl — same searches.
9. If results count is zero, record "No anonymized court rulings found containing the search terms".

Return Task 4 as JSON.

=== TASK 5 — TAX OFFICE WHITELIST CROSS-CHECK ===

Goal: secondary confirmation by querying the Biała Lista by name (not NIP) — this can reveal additional entities under the same person.

(If Phase 1 already ran the NIP query on Biała Lista, this task adds the name-based query.)

1. Open https://www.podatki.gov.pl/wykaz-podatnikow-vat-wyszukiwarka
2. Select the search mode "Nazwa podmiotu" (Entity name) — must be at least 5 characters.
3. Type: GPUcomputer — search.
4. Then type: Szklarski — search.
5. Record any entities returned that I may not have known about, beyond the primary JDG.

Return Task 5 as JSON.

=== TASK 6 — konsument.krd.pl (KRD CONSUMER ACCESS PATH) ===

Goal: KRD's main portal (krd.pl) requires a business contract, but konsument.krd.pl is the consumer-facing path for individuals with documented claims. Check what's accessible.

1. Open https://konsument.krd.pl
2. Look for any "Sprawdź dłużnika" (Check a debtor) or "Sprawdź firmę" (Check a company) link without requiring full account setup.
3. If the site allows a one-off lookup with payment (typically ~30 PLN), record:
   - What identifier(s) can be searched (NIP / name / both)
   - The lookup cost
   - Whether identity verification via mObywatel or verified bank transfer is required upfront
4. DO NOT register an account, do NOT pay, do NOT begin identity verification.
5. The goal here is purely to confirm the procedure cost and whether identity verification will be needed.

Return Task 6 as JSON: { "access_path_available": "...", "cost_PLN": ..., "verification_required": "...", "notes": "..." }

=== OVERALL OUTPUT ===

Combined JSON with keys "task_1_pledges_movable", "task_2_tax_pledges", "task_3_komornik_auctions", "task_4_portal_orzeczen", "task_5_vat_whitelist_name_search", "task_6_konsument_krd_access", plus a top-level "summary_english" sentence-paragraph answering:
- Are there secured creditors ahead of me?
- Are bailiff proceedings already underway?
- Does the tax office have a claim?
- Has the debtor been sued before?
- Are there additional debtor entities I didn't know about?
- Is the konsument.krd.pl path viable as a next step?

=== FAILURE HANDLING ===

- CAPTCHA: stop affected task, flag, continue with next task.
- Login wall on paid certificate sections: do NOT register; the free query is what I want.
- If "rejestr zastawów skarbowych" URL has changed, search Google for the current official location.
- No results = positive finding; record explicitly with today's date.

=== STOP CONDITION ===

All six tasks attempted. Return consolidated JSON.
```
````
