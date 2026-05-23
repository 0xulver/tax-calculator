# Browser-Agent Investigation Plan — GPUcomputer / Mateusz Szklarski

This folder contains seven browser-agent prompts that together map the assets, debts, hidden interests, operating reality, and business health of the JDG debtor against whom I hold a 155,000 PLN claim. Each prompt is self-contained and can be pasted verbatim into Atlas, Comet, Claude in Chrome, or any comparable agentic browser.

I do not speak Polish. Every prompt contains the Polish UI labels translated to English in parentheses, and every prompt instructs the agent to return all extracted text in English translation.

---

## Subject identifiers (carry into every prompt)

| Field | Value |
|---|---|
| Full legal name | Mateusz Szklarski-Łopata |
| Trading as | GPUcomputer / MATEUSZ SZKLARSKI GPUCOMPUTER |
| NIP | 8661681248 |
| REGON | 362678345 |
| Registered address | ul. Mogilska 16 lok. 7, 31-516 Kraków (virtual office) |
| Website | https://www.gpucomputer.pl/ |
| Phone (mobile) | 883 109 779 |
| Phone (landline) | 12 333 77 30 |
| Email (owner) | mateusz@gpucomputer.pl |
| Activity start | 2015-10-06 |
| PKD primary | 26.20.Z – Produkcja komputerów i urządzeń peryferyjnych |
| EPU case | Nc-e 552126/26, SR Lublin-Zachód, filed 2026-04-08 |
| Debt | 155,000 PLN |

Each prompt re-states these so they can be run in isolation.

---

## Phase sequence and rationale

| Phase | File | Purpose | Cost | Time | Why run in this order |
|---|---|---|---|---|---|
| 1 | `01-phase1-quick-wins.md` | VAT whitelist (bank accounts!), KRZ, MSiG, CEIDG verification | Free | 15–30 min | Highest signal-per-złoty; if KRZ shows a bankruptcy filing, the whole strategy changes immediately. |
| 2 | `02-phase2-real-estate.md` | MSIP Kraków, geoportal, commercial KW lookups, EKW once KW is known | Free + optional 30–100 PLN | 30–90 min | Real estate is the most durable asset class and cannot be moved. Finding any KW number changes Path A vs Path B math. |
| 3 | `03-phase3-other-creditors.md` | Rejestr Zastawów (pledges), Licytacje komornicze (auctions), tax pledge register | Free | 15–30 min | Reveals whether other creditors are already executing, which signals queue position and recovery probability. |
| 4 | `04-phase4-hidden-companies.md` | KRS person search, rejestr.io, CRBR, eZamówienia | Free | 30–60 min | Detects hidden corporate interests where the debtor may be parking assets behind nominee directors. |
| 5 | `05-phase5-operating-address.md` | Wayback Machine, Google Maps, Allegro/Ceneo/Opineo reviews, business directories, WHOIS/DNS | Free | 60–120 min | Locates the real workshop/warehouse beyond the virtual office. |
| 6 | `06-phase6-vehicles.md` | OLX/OtoMoto/AllegroLokalnie listings, historiapojazdu.gov.pl if a VIN is found | Free | 30–60 min | Vehicles are seizable; ads may also reveal asset stripping. |
| 7 | `07-phase7-business-health.md` | Live website ordering test, LinkedIn/Facebook, job boards, customer complaints, Similarweb | Free | 60–90 min | Determines whether the business is still operating commercially or is winding down. |

**Total realistic OSINT cost:** 0–150 PLN. **Total realistic time:** 4–8 hours of agent runtime.

---

## How to run

Pick a browser agent (Atlas, Comet, Claude in Chrome). For each phase:

1. Open the file (`01-phase1-quick-wins.md`, etc.).
2. Copy the entire `prompt-for-browser-agent` block to the agent.
3. Let the agent execute. Capture the JSON response.
4. Paste the response into a `responses/` subfolder named after the phase (e.g. `responses/phase1-quick-wins.json`).
5. Apply the **escalation triggers** below before moving to the next phase.

Phases 1, 3, 4, 7 are independent and can be run in any order. Phases 2 and 5 produce data each other can consume (a real residential address from Phase 5 makes Phase 2's real-estate lookup more useful at a second address). Phase 6 depends partly on Phase 5 (a plate seen at a real address). The simplest order is to run Phase 1 first, then Phases 3 and 5 in parallel, then 2, 4, 6, 7.

---

## Escalation triggers — stop and reassess before running more phases

**Stop immediately and contact your lawyer if any of these surface:**

| Trigger | Source | Why it matters |
|---|---|---|
| KRZ shows any bankruptcy or restructuring filing under the debtor's name, NIP, or REGON | Phase 1 | Path B zabezpieczenie within 2 months of filing date is clawed back under art. 127 §3 PU. The whole strategy changes — likely shift to filing as a creditor in the bankruptcy proceeding. |
| MSiG full-text search returns any "wniosek o ogłoszenie upadłości" or "restrukturyzacja" entry | Phase 1 | Same as above; MSiG can show entries that haven't propagated to KRZ yet. Important because under art. 27 PU the court has up to 2 months to rule on a bankruptcy petition, meaning a filed-but-unprocessed petition may be invisible in KRZ but already starting the 2-month clawback clock. |
| Biała Lista shows VAT status as "Wykreślony" (struck off) | Phase 1 | TERMINAL INDICATOR — tax authority has detected fraud, recorded continuous nil returns, or debtor has formally ceased trading. Recovery probability collapses. |
| Biała Lista shows zero declared bank accounts | Phase 1 | Komornik bank seizure becomes guesswork; foreign or fintech accounts likely. |
| Rejestr Zastawów shows secured creditors with priority | Phase 3 | Your unsecured claim is junior to all of them. |
| Licytacje komornicze shows active auctions against the debtor | Phase 3 | Other creditors are already enforcing; under *zbieg egzekucji* rules, your subsequent zabezpieczenie merely queues you for proportionate distribution (*podział sumy uzyskanej z egzekucji*), drastically reducing your effective recovery. |
| EKW (real estate) reveals existing mortgages matching prior creditors | Phase 2 | Confirms multi-creditor distress. |
| EKW Section II shows "Umowa Darowizny" (Deed of Donation) to a family member with a recent date | Phase 2 | Classic asset-shielding move. Triggers a *skarga pauliańska* (fraudulent transfer) case under art. 527 KC — a separate 2–3 year lawsuit you'd have to bring. Flag to lawyer immediately. |
| KRS surfaces a newly-formed sp. z o.o. (established late 2025 or 2026) with identical PKD codes (26.20.Z or 46.51.Z) operating at a different address | Phase 4 | **Phoenix maneuver**: debtor is draining capital from the JDG into a new liability-shielded corporate vehicle. Civil recovery against the JDG becomes increasingly hollow as assets migrate. |

If any of the above hit, do not spend more time on Phases 5–7 until the lawyer has reassessed.

---

## Decision frame — the two stopping points

Once Phases 1, 3, and 7 are in, you should be able to slot the result into one of two scenarios:

### Scenario A — "Hollow Shell"
**Signals:** website defunct or showing closure notice; zero or stale bank accounts on Biała Lista; multiple recent customer complaints showing systemic non-delivery; no real estate found in Phase 2; possibly already a KRZ/MSiG entry; possibly already a phoenix sp. z o.o. in Phase 4.

**Conclusion:** the JDG has been stripped. Spending 15–25k PLN on Path B (withdraw + zabezpieczenie) is throwing good money after bad — komornik will freeze empty accounts. **Remain in Path A (EPU), accept the procedural delay, minimize further spend.** The EPU title (if and when it materializes) is at least durable for 6 years and can be refreshed; resell or hold for opportunistic enforcement later.

### Scenario B — "Cash Flow Positive but Evading"
**Signals:** website fully operational and accepting orders; Biała Lista shows current active bank accounts; no KRZ entry; no phoenix sp. z o.o. yet; possibly some real estate in own name; few or no other creditors visible in Phase 3.

**Conclusion:** the JDG is alive and revenue-generating but specifically evading your debt. **Path B is highly viable.** Halt OSINT, escalate to a lawyer, and hand them the Phase 1 bank account numbers as ammunition for a tightly-drafted *wniosek o zabezpieczenie*. The freeze will hit live operating accounts and create immediate negotiation pressure.

### Ambiguous middle
If the picture is partial — e.g. business alive but accounts thin, or one creditor visible but not many — feed everything to the lawyer and let them frame the cost-benefit. Don't try to decide alone.

---

## What this plan deliberately does NOT cover

The following high-value sources require actions a browser agent cannot perform. They are listed here so they don't drop off the radar — route each to your lawyer or to yourself for manual action.

| Source | Why a browser agent can't do it | Who can |
|---|---|---|
| OGNIVO (bank account discovery across all Polish banks) | Komornik-only access; requires enforcement title | Komornik after EPU nakaz or court zabezpieczenie order |
| Formal *zlecenie poszukiwania majątku* (komornik asset search) | Requires enforcement title | Komornik after enforcement title obtained |
| CEPiK formal data request (vehicles by owner name) | Requires Profil Zaufany login + payment + legal-interest justification | You via Profil Zaufany, or your lawyer |
| EGiB formal data request (owner data from cadaster) | Requires signed wniosek + legal-interest documentation + payment | Your lawyer |
| Portal Informacyjny Sądów (party access to pending cases) | Requires in-person identity verification at a Polish court | Your Kraków lawyer |
| BIK credit history | Available only to debtor himself | N/A — debtor will never disclose |
| KRD/BIG full debt check | Requires business account contract (KRD) or consumer identity verification via mObywatel (konsument.krd.pl) | Your lawyer, paid intermediary, or you personally via konsument.krd.pl with mObywatel |
| BIG InfoMonitor debt check | Business subscription | Your lawyer |
| Certified extracts (odpis) for court use | Court-form ordering, payment | Your lawyer when civil case is filed |
| Courier/Paczkomat dispatch origin tracing | Requires access to creditor's own email archive (shipment notifications from the original GPUcomputer order) | You — manually grep your inbox for InPost, DPD, DHL, GLS dispatch notifications; the origin Paczkomat/depot often points to the debtor's real workshop |
| USC (marital status / spousal property regime confirmation) | Requires demonstrated legal interest; cannot be done by browser agent | Your lawyer, or licensed *detektyw* observation, or the komornik phase of enforcement |

The browser-agent investigation produces leads. The certified evidence step is downstream and handled by counsel.

---

## What to do with the results

Once all seven phases have run, the consolidated picture should answer:

1. **Does he have real estate?** (Phase 2 EKW result)
2. **Are there other creditors ahead of me?** (Phase 3 + Phase 2 mortgages)
3. **Is he hiding assets in companies?** (Phase 4)
4. **Where does the business actually operate?** (Phase 5)
5. **What's his bank account fingerprint?** (Phase 1 Biała Lista + Phase 5 website footer/regulamin)
6. **Is the business still alive?** (Phase 7)
7. **Has he already filed for bankruptcy?** (Phase 1 KRZ + MSiG)

With these answers, the Path A (stay-EPU) vs Path B (withdraw + zabezpieczenie) decision becomes data-driven rather than speculative.
