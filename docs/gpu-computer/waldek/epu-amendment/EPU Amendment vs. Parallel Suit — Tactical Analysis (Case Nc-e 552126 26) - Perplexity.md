# EPU Amendment vs. Parallel Suit — Tactical Analysis
### Case Nc-e 552126/26 | Status as of 2026-05-24

**Prepared for:** Private creditor, Magnus (plaintiff pro se)
**Case facts:** EPU pozew filed 2026-04-08 against Mateusz Szklarski-Łopata (JDG GPUcomputer, NIP 8661681248) for 155,000 PLN. No nakaz zapłaty issued as of 2026-05-24. Target co-defendant: Waldemar Łopata (JDG "WALDEMAR ŁOPATA 3d Kraków", NIP 7752083995).

***

## 1. Subjective Amendment in EPU — Is It Even Allowed?

**Short answer: No. Subjective amendment (adding a co-defendant) inside a live EPU proceeding is not procedurally available via the e-sad.gov.pl portal, and attempting it will trigger dismissal/umorzenie, not transfer.**

### Statutory basis

Art. 505^28 § 1 KPC (text in force Dz.U.2026.0.468) provides that EPU applies "przepisy o postępowaniu upominawczym with modifications in this chapter." Art. 505^29 § 1 KPC explicitly **excludes** the application of "przepisów o postępowaniach odrębnych innych niż wymienione w art. 505^28 § 1" — the joinder and subjective change provisions of art. 194–198 KPC are postępowanie odrębne rules that **do not apply** in EPU.[^1]

Art. 505^31 § 1 KPC further reinforces the digital lock-in: "Powód wnosi pisma wyłącznie za pośrednictwem systemu teleinformatycznego." The EPU portal does not present any form for adding a second defendant to an open pozew. There is no equivalent of the art. 193/194 KPC "zmiana podmiotowa" workflow in the portal's current UI.[^2][^3][^1]

### What the doctrinal literature says

A ruling from Sąd Rejonowy (VIII C 1035/20) expressly held that subjective amendment of powództwo is inadmissible in simplified proceedings (postępowanie uproszczone), citing art. 505^4 § 1 KPC, and the same structural logic applies by analogy to EPU: the Sejm explicitly removed the art. 194–198 joinder machinery from EPU. The 2025 journal article in Monitor of Legal Proceedings (Beck) reviewing the landscape of pre-trial and in-trial subjective changes confirms no legislative revision has altered this position.[^4][^5]

### Available paths if amendment is refused

The procedural options after the subjective-amendment bar is hit are:
1. **Do nothing with EPU** — let it proceed to nakaz or umorzenie on its own logic, and file separately against Waldemar in Sąd Okręgowy w Krakowie.
2. **Withdraw EPU (cofnięcie pozwu)** before the nakaz issues and refile a joint ordinary pozew against both defendants.
3. **Allow or engineer EPU umorzenie** (see §2 below), then refile jointly within the 3-month window of art. 505^37 § 2 KPC.

There is **no procedural path to "amend EPU in place"** to add Waldemar without triggering exit from EPU.[^6][^1]

***

## 2. What Triggers Transfer Out of EPU to Ordinary Procedure?

**Critical update (post-7 February 2020): EPU no longer "transfers" to ordinary court — it terminates by umorzenie (dismissal). The old art. 505^33/^36 transfer mechanism was replaced on 7 February 2020 by the nowelizacja of 4 July 2019 (Dz.U.2019 poz.1469).**[^7][^6]

### Current mechanisms as of 2026-05-24

| Trigger | Article | Result |
|---------|---------|--------|
| No basis to issue nakaz zapłaty | Art. 505^33 KPC | **Umorzenie** postępowania (NOT transfer) |
| Nakaz cannot be served in Poland | Art. 505^34 § 2 KPC | Uchylenie nakazu + **umorzenie** |
| Sprzeciw by defendant | Art. 505^36 KPC | **Umorzenie** in the scope nakaz lost force |
| Skarga o wznowienie | Art. 505^39 KPC | Transfer to sąd właściwości ogólnej (the one surviving transfer mechanism) |

**There is no "wniosek o przekazanie sprawy" available to the plaintiff.** The only surviving transfer mechanism is the skarga o wznowienie route (art. 505^39), which is inapplicable pre-judgment.[^8][^1]

### How to engineer exit from EPU in order to file jointly

The cleanest self-help path is to **cofnąć pozew** (withdraw the EPU case) before the nakaz issues. This produces umorzenie, and the plaintiff may then refile jointly against both Mateusz and Waldemar in ordinary proceedings within 3 months to preserve the 2026-04-08 filing date (art. 505^37 § 2 KPC — see §3 below).[^9][^10]

Alternatively, **if the nakaz does issue**, Mateusz's sprzeciw will produce umorzenie of that nakaz (art. 505^36), and the same 3-month window opens for a fresh ordinary pozew. But waiting for sprzeciw is risky: Mateusz may not contest (especially from the Netherlands), and the nakaz could become enforceable, locking in the single-defendant trajectory.

***

## 3. Does the EPU Filing Date Survive Transfer?

**Yes — but only if the ordinary pozew is filed within 3 months of the EPU umorzenie postanowienie, AND only against the same roszczenie and the same pozwany.**

### The statutory mechanism: art. 505^37 § 2 KPC

The current text (Dz.U.2026.0.468) provides:

> "Jeżeli w terminie trzech miesięcy od dnia wydania postanowienia o umorzeniu elektronicznego postępowania upominawczego powód wniesie pozew przeciwko pozwanemu o to samo roszczenie w postępowaniu innym niż elektroniczne postępowanie upominawcze, skutki prawne, które ustawa wiąże z wytoczeniem powództwa, następują z dniem wniesienia pozwu w elektronicznym postępowaniu upominawczym."[^10]

This means that for a new ordinary pozew filed **within 3 months** of EPU umorzenie:
- **Statute of limitations (art. 118 KC / art. 123 § 1 pkt 1 KC):** Interrupted as of 2026-04-08[^11][^9]
- **Lis pendens (art. 192 KPC):** Effective from 2026-04-08[^10]
- **Interest accrual:** Procedural costs interest calculated from 2026-04-08

### Critical constraint: same roszczenie AND same pozwany

Art. 505^37 § 2 KPC back-dates the filing date only for "o to samo roszczenie" against the same "pozwanego." **If you add Waldemar as a co-defendant in the new ordinary pozew, his filing date does NOT automatically backdate to 2026-04-08.** The new claim against Waldemar starts from the date of the new ordinary pozew filing.[^9][^10]

For Mateusz, the limitation clock stopped on 2026-04-08 and can be preserved. For Waldemar, it stops only from the date of the separate/joint ordinary pozew — which, given the 3-year commercial limitation under art. 118 KC on a January 2026 contract claim, is not yet a concern (limitation runs until January 2029).

### If the 3-month window is missed

If no new pozew is filed within 3 months of the umorzenie postanowienie, the interruption effect lapses and limitation resumes running. The SN uchwała III CZP 66/13 (2013-11-21) held that even EPU umorzenie under art. 505^37 § 1 (non-payment of supplement fee) does interrupt limitation, but this ruling is non-binding at lower courts and subject to doctrinal dispute.[^12][^11]

***

## 4. The Court Fee Differential

### EPU fee

EPU fee = 1.25% × 155,000 PLN = **1,937.50 PLN** (already paid, per art. 19 ust. 2 pkt 2 UKSC).[^13][^3]

### Ordinary procedure fee

Ordinary procedure = 5% × 155,000 PLN = **7,750 PLN** (art. 13 ust. 1 UKSC). For claim >100,000 PLN, Sąd Okręgowy w Krakowie has subject-matter jurisdiction (art. 17 pkt 4 KPC as amended from 1 July 2023).[^14][^15]

### Fee differential = 3,750 PLN supplementary fee after refiling

When a new ordinary pozew is filed within the 3-month window following EPU umorzenie, the EPU fee of 1,937.50 PLN is credited against the full 5% fee per art. 505^37 § 2 KPC. The plaintiff must pay the differential: **7,750 − 1,937.50 = 5,812.50 PLN** when filing the new pozew.[^16][^17][^18]

### Refund if EPU is cofnięty before nakaz or service

Art. 79 ust. 1 pkt 1 lit. b UKSC: **full refund** of the EPU fee (1,937.50 PLN) if the pozew is cofnięty before the odpis pisma is sent to the other side (i.e., before nakaz is served). Since no nakaz has issued and the case has not moved (status 2026-05-24), cofnięcie now likely qualifies for full refund. If cofnięcie occurs after nakaz is served but before the hearing, only 50% is refunded (art. 79 ust. 1 pkt 3 lit. a UKSC).[^19][^20]

### Deadline for supplementary fee payment after umorzenie

Once the ordinary court receives the file and issues the wezwanie, the plaintiff has a **2-week deadline** to supplement the fee under art. 505^37 § 1 KPC. Failure to pay within that deadline = umorzenie of the new proceeding. In the cofnięcie/refile scenario, the plaintiff simply pays the full 5% (minus the EPU credit they apply for) when submitting the new pozew.[^21]

### Fee scale by number of defendants

The 5% fee is calculated on the **wartość przedmiotu sporu (WPS)**, not on the number of defendants. If both Mateusz and Waldemar are named in a single joint pozew for 155,000 PLN solidary liability, the fee remains 7,750 PLN — there is no per-defendant surcharge.[^14]

***

## 5. Path Comparison: A vs. B vs. C

### Path A — Engineer EPU Exit (cofnięcie or wait for umorzenie), Then Refile Joint Ordinary Pozew

**Mechanism:** Withdraw EPU while no nakaz has been served → full refund of 1,937.50 PLN → file joint pozew (Mateusz + Waldemar) at Sąd Okręgowy w Krakowie within 3 months → invoke art. 505^37 § 2 to credit EPU fee against 5% court fee → pay net 5,812.50 PLN supplement.

| Item | Estimate |
|------|----------|
| Court fee net outlay | ~5,812.50 PLN (if EPU fee credited) |
| Lawyer fee (pozew to SO Kraków) | 3,000–8,000 PLN + trial hourly |
| Legal minimum adversarial costs if lost vs. Waldemar | ~5,400 PLN (art. 99 KPC, § 2 adwokat tariff at 155k WPS) |
| Mateusz filing date preserved? | **Yes** (2026-04-08 via art. 505^37 §2) |
| Waldemar filing date | From new ordinary pozew date |
| Expected time to judgment | 18–36 months (Sąd Okręgowy Kraków backlog) |
| Limitation risk | Low (3-year runs to Jan 2029) |

**Advantage:** Single proceeding, single judgment, simplest enforcement, art. 219 KPC consolidation not needed because both defendants are in same case from the start. Waldemar's Kraków JDG assets immediately reachable.

**Risk:** You lose the EPU simplicity against Mateusz. Ordinary procedure is slower and more expensive, but provides access to Waldemar's enforcement surface.

***

### Path B — Keep EPU Against Mateusz, File Separate Ordinary Pozew Against Waldemar

**Mechanism:** Let EPU proceed to nakaz against Mateusz alone. In parallel, file independent pozew against Waldemar at Sąd Okręgowy w Krakowie.

| Item | Estimate |
|------|----------|
| EPU keeps running (1,937.50 PLN fee sunk cost) | No additional court fee for Mateusz |
| New court fee for Waldemar case | 7,750 PLN (no EPU credit applicable to a different case) |
| Total court fees | ~9,688 PLN |
| Lawyer fees | Double — two separate sets of hearings |
| Time to EPU nakaz (if issued) | 1–6 months from today (uncertain backlog at Lublin-Zachód) |
| Time to Waldemar judgment | 18–36 months |
| Two separate judgments | Yes — enforcement diverges |
| Risk: nakaz issued but Mateusz not served (abroad) | Art. 505^34 § 2: if can't be served in Poland, nakaz uchylony and EPU umorzony anyway |

**Advantage:** Fastest path to enforcement against Waldemar if his assets are at risk; preserves the EPU trajectory against Mateusz without disruption.

**Risk:** Mateusz is in the Netherlands — EPU requires service **within Poland** (art. 505^28 § 2 pkt 2 KPC: nakaz cannot be issued if service would have to occur outside the country). If Mateusz's only verifiable address is the Kraków virtual office and the EPU court finds service impossible, the EPU will likely be uchylony under art. 505^34 § 2 and umorzony — effectively forcing outcome similar to Path A but with a delay and potentially missing the 3-month refile window for Mateusz's date preservation.[^22][^8]

> **Critical flag:** Mateusz is registered at a virtual office in Kraków but actually lives in Eindhoven, NL. The EPU court will attempt service at the CEIDG-registered address. If it fails twice and the PESEL-register address does not match, or if the court discovers the nakaz needs to go abroad, the EPU collapses via art. 505^34. Plan B depends on EPU service succeeding inside Poland.

***

### Path C — Withdraw EPU, Refile Single Joint Ordinary Pozew (Both Defendants Named)

This is a variant of Path A, differing only in timing: instead of waiting for any EPU event, you immediately cofnij pozew.

| Item | Estimate |
|------|----------|
| EPU cofnięcie | Full refund of 1,937.50 PLN (before any service) |
| New ordinary court fee | 7,750 PLN (no credit since cofnięcie, not umorzenie) |
| Net cost increase vs. Path A | ~1,937.50 PLN (EPU fee lost, cannot be credited in the cofnięcie scenario) |
| Mateusz date preserved? | **No** — the new pozew date governs |

**Important nuance:** Art. 505^37 § 2 applies only after an **umorzenie postanowienie** — not after a cofnięcie. If you voluntarily cofnij EPU, the date-preservation mechanism is lost for Mateusz. You must start fresh from the new pozew date. However, since limitation on the January 2026 claim runs to January 2029, loss of the 2026-04-08 date is legally inconsequential **right now** — it only matters if significant time elapses before the new pozew.[^10]

**Recommended over Path A only if** you want to avoid even a brief umorzenie period and re-file immediately. Otherwise, Path A (let EPU be umorzony by its own logic, then refile within 3 months) is strictly superior: same ultimate result but you preserve the 2026-04-08 date for Mateusz.

***

## 6. Joinder Rules — Art. 72 KPC

### The correct basis: współuczestnictwo materialne, art. 72 § 1 pkt 1 KPC

Both joint liability theories (spółka cywilna and solidary tortfeasor) produce the same procedural classification: **współuczestnictwo materialne (substantive joinder).**

Per established SN doctrine, solidary liability always creates współuczestnictwo materialne "oparte na wspólnym obowiązku" under art. 72 § 1 pkt 1 KPC, regardless of whether the solidarity arises from the same underlying contract or from separate legal bases (e.g., art. 441 KC tortfeasor solidarity). The SN specifically confirmed: *"Zakwalifikowanie danego stosunku prawnego jako odpowiedzialności solidarnej przesądza o konieczności zakwalifikowania współuczestnictwa procesowego jako materialnego, opartego na wspólnym obowiązku."*[^23]

### Is necessary joinder (art. 72 § 2 KPC) required?

**No.** The same SN authorities establish: *"Solidarność zobowiązania nie stwarza współuczestnictwa koniecznego dłużników, ponieważ istota solidarności biernej polega na tym, że każdy z dłużników zobowiązany jest wobec wierzyciela do spełnienia całego świadczenia."* You can sue either Mateusz or Waldemar alone and obtain a fully enforceable judgment against that one defendant. Suing both together is a tactical choice, not a jurisdictional necessity.[^24][^25][^23]

### Practical framing for the pozew

In the joint ordinary pozew, the correct legal framing is:
- **Primary theory:** Współuczestnictwo materialne, art. 72 § 1 pkt 1 KPC — obowiązek solidarny wynikający z art. 441 § 1 KC w zw. z art. 422 KC (joint tortfeasor), alternatively art. 864 KC (de facto spółka cywilna)
- **Roszczenie główne:** 155,000 PLN solidarnie from both defendants with interest
- **Joinder characterisation explicitly stated** in the header of the pozew so the court does not need to resolve it

***

## 7. Zabezpieczenie Roszczenia (Interim Measures)

### Availability and standard

Under art. 730 KPC any party may request zabezpieczenie if they can **uprawdopodobnić roszczenie** (make the claim plausible, not prove it) and demonstrate **interes prawny** — risk that enforcement would be frustrated without interim measures.[^26][^27]

In your case:
- **Uprawdopodobnienie** against Waldemar: the email thread showing Waldek personally negotiated the contract, made delivery promises, and issued a written refund promise is strong uprawdopodobnienie of both the art. 422 KC participation theory and the art. 864 KC de facto partnership theory. Wayback Machine snapshots 2016–2026 showing joint business operation further support it.[^28][^26]
- **Interes prawny:** Waldemar has 17 years of continuous JDG activity, physical Kraków premises, and business inventory. However, if he learns of the litigation, there is risk he liquidates or transfers assets. This risk = interes prawny for immediate zabezpieczenie on filing.

### Specific measures available against Waldemar

1. **Zajęcie rachunków bankowych JDG** — most effective; Biała Lista provides account numbers for NIP 7752083995. This is art. 747 pkt 1 KPC zabezpieczenie.
2. **Hipoteka przymusowa** on any Kraków real property in his name — requires a property search (KW registry) first to identify the property. Hipoteka przymusowa is established by court order to the sum of the claim (up to 150% of the principal claim, per current practice).[^29]
3. **Zajęcie ruchomości** (inventory) at ul. Św. Filipa 23/4 — possible under art. 747 pkt 2 KPC but requires komornik execution; less preferred as a first step.

### Kaucja (security deposit by plaintiff)

Art. 739 § 1 KPC gives the court **discretion** (not obligation) to require the plaintiff to post a kaucja before enforcement of the zabezpieczenie order. Courts exercise this power variably. On claims of 155,000 PLN from a private individual creditor with a documented email trail and Wayback evidence, a kaucja is possible but not certain. If required, courts typically set it at 5–10% of the zabezpieczenie sum, i.e., 7,750–15,500 PLN.[^30][^31][^32]

### Timing: file zabezpieczenie motion with the pozew

Art. 730 § 2 KPC allows filing the zabezpieczenie wniosek simultaneously with the pozew (wniosek składany łącznie z pozwem). This is the recommended approach — the court considers it on the same day as the initial filing, avoiding the service delay. If filed before the pozew (ante causam), a separate registration fee applies.

**Requires a Polish pełnomocnik** to draft and file. The zabezpieczenie motion must cite specific bank account numbers (from Biała Lista) and, for hipoteka, the specific nieruchomość and KW number.

***

## 8. EPU Portal — Practical Mechanics

### Access without Profil Zaufany

The EPU portal (e-sad.gov.pl) currently offers three authentication methods:[^33][^34]
1. Profil Zaufany (Gov.pl)
2. System Tożsamość Ministerstwa Sprawiedliwości (MS Identity System) — allows expedited access within 1 hour
3. In-person registration at the court

**Art. 505^31 § 1 KPC: "Powód wnosi pisma wyłącznie za pośrednictwem systemu teleinformatycznego."** This is absolute. **There is no paper-mail fallback for plaintiffs in EPU.** A pozew or any plaintiff's pismo submitted by paper post to Sąd Rejonowy Lublin-Zachód will have no procedural effect.[^35][^2][^1]

However, **cofnięcie pozwu** (withdrawal) and the resulting termination of EPU can likely be initiated via the portal once access is obtained. Profil Zaufany can be set up remotely (online via internet banking at 23 Polish banks including PKO, Alior, mBank, BNP Paribas, etc.) without visiting Poland — this is the fastest route for a foreign-resident Polish national.[^36]

### Can a Polish pełnomocnik take over the EPU account?

Art. 505^31 § 2^2 KPC: "Pełnomocnik powołuje się na pełnomocnictwo, wskazując jego zakres oraz okoliczności wymienione w art. 87, wnosząc pierwsze pismo procesowe w sprawie." A pełnomocnik must create **their own EPU account** (tied to their own authentication). They cannot "take over" the plaintiff's existing account. Instead:[^1]
- The plaintiff must formally appoint a pełnomocnik via a pełnomocnictwo document
- The pełnomocnik then logs in under their own account and designates themselves as representative in the case
- Subsequent pisma are filed by the pełnomocnik from their account

This is a standard workflow for law firms using EPU. It is technically feasible for a Kraków lawyer to take over filing responsibilities once the pełnomocnictwo is signed and scanned.

### Adding a second defendant via the portal

The EPU portal's current workflow does not support adding a new defendant to an open case. The portal interface is designed for single-pozew workflows terminating in either nakaz or umorzenie. There is no "zmiana podmiotowa" button or form. Even if such a technical path existed, art. 505^29 § 1 KPC's exclusion of art. 194–198 KPC would make it void.[^3][^2]

### Service mechanics in EPU

Service of the nakaz to Mateusz is performed by the court, not the plaintiff. The EPU court will serve to the CEIDG-registered address (virtual office, ul. Mogilska 16 lok. 7, Kraków). This is domestic service. If Mateusz does not pick up the nakaz (awizo twice), art. 505^34 § 1 KPC applies the PESEL-register address presumption. If the PESEL registry shows a Dutch address, the court cannot apply the domestic deemed-service fiction, and the nakaz will likely be uchylony under art. 505^34 § 2 KPC — which triggers umorzenie.[^37]

***

## 9. Sprzeciw Deadline and the "Wait for Sprzeciw" Tactic

### Normal sprzeciw timeline

If nakaz issues and is served at the virtual office (Kraków domestic service), Mateusz has **2 weeks** from service to file sprzeciw. Given his Eindhoven residence, actual notice may be delayed, but the legal 2-week clock runs from formal service.

### Effect of sprzeciw: umorzenie under 2026 KPC

Under current art. 505^36 KPC: "W przypadku wniesienia sprzeciwu sąd umarza postępowanie w zakresie, w którym nakaz zapłaty utracił moc." This is **umorzenie, not transfer** — a critical change from pre-2020 law. The 3-month window of art. 505^37 § 2 then opens for the plaintiff to refile in ordinary proceedings, preserving the 2026-04-08 date against Mateusz.[^38][^39][^1]

### Does waiting for sprzeciw pay off?

**It is the cheapest path IF Mateusz actually contests.** Here is the logic:
- If Mateusz contests (sprzeciw): EPU is umorzony; plaintiff has 3 months to file ordinary pozew against both defendants, EPU date preserved for Mateusz claim, and pays only the 5,812.50 PLN differential (EPU fee credited).
- If Mateusz does NOT contest: EPU nakaz becomes enforceable → begin EAPO/komornik proceedings against Mateusz → file separate pozew against Waldemar (no date preservation benefit, but no urgency either since limitation runs to January 2029).
- If EPU nakaz cannot be served (Mateusz abroad): EPU uchylony → umorzenie → 3-month window → refile jointly.

**The wait-for-sprzeciw approach is tactically rational if:**
- Mateusz's PESEL-registered address is still in Poland (allows valid EPU service)
- The plaintiff is willing to delay Waldemar joinder by 3–6 months
- EPU proceedings cost nothing additional while waiting

**It is not rational if:**
- Waldemar is already showing signs of asset dissipation or has been alerted to the litigation
- The plaintiff needs Waldemar's Polish enforcement surface urgently
- EPU service to Mateusz is likely to fail (triggering umorzenie anyway)

***

## 10. Honest Bottom Line — Single Recommendation

**At today's case state (2026-05-24, EPU filed 2026-04-08, no nakaz, no sprzeciw, two months elapsed), the recommended move is:**

> **Obtain Profil Zaufany (via online banking) immediately, then cofnij the EPU pozew within the next 14 days. Within 3 months of the cofnięcie, file a joint ordinary pozew at Sąd Okręgowy w Krakowie naming both Mateusz Szklarski-Łopata and Waldemar Łopata as co-defendants (współuczestnictwo materialne, art. 72 § 1 pkt 1 KPC), for 155,000 PLN solidarnie, supported by a simultaneously-filed wniosek o zabezpieczenie targeting Waldemar's JDG bank accounts and any real estate. Engage a Kraków adwokat/radca prawny experienced in windykacja before the cofnięcie to ensure the ordinary pozew is drafted and ready to file without gaps.**

### Reasoning

1. **EPU service against Mateusz is high-risk** given his Eindhoven residence. The EPU court will service to the Kraków virtual office; if PESEL shows Netherlands, the nakaz will be uchylony under art. 505^34 §2 KPC and EPU umorzony. This forces exit from EPU regardless — better to control the timing.

2. **Waldemar is the enforcement surface.** His 17-year JDG, Kraków premises, and Polish residency make komornik enforcement trivially straightforward compared to cross-border EAPO proceedings against Mateusz's Dutch wages.

3. **Date preservation is manageable.** Cofnięcie (not umorzenie) loses the art. 505^37 §2 date-back privilege, but limitation on a January 2026 commercial claim under art. 118 KC runs to January 2029. There is 2+ years of margin; the 2026-04-08 date matters only for interest and costs precision, not survival.

4. **Cost:** Net out-of-pocket is ~7,750 PLN court fee + lawyer fees (estimated 8,000–15,000 PLN total for drafting, filing, and first hearing at Sąd Okręgowy Kraków level) — roughly 15,000–23,000 PLN total.

### Conditional variants

| Condition | Path |
|-----------|------|
| Mateusz is likely to contest EPU (sent written acknowledgment, has a lawyer) | Wait for sprzeciw → umorzenie → refile jointly with art. 505^37 §2 date preservation for Mateusz |
| Waldemar shows signs of asset movement (closing accounts, moving premises) | File zabezpieczenie immediately — do not wait; cofnij EPU today and file joint pozew + wniosek o zabezpieczenie on same day |
| Criminal complaint extended to Waldemar as suspect | Criminal art. 291 KPK zabezpieczenie majątkowe can attach his assets through the prosecutor — coordinate with the criminal track timing |

### Next steps in the next 14 days

1. **Activate Profil Zaufany** via online banking (PKO BP, mBank, ING, BNP Paribas, Alior — all accept remote setup for Polish nationals abroad).
2. **Engage a Kraków adwokat/radca prawny** specialising in windykacja — initial consultation to confirm the above analysis and draft the joint ordinary pozew.
3. **Commission Waldemar real property search** via KW portal (https://ekw.ms.gov.pl) or via lawyer — identify any Kraków real estate in NIP 7752083995 / name Waldemar Łopata for hipoteka przymusowa.
4. **Pull Biała Lista** for NIP 7752083995 — identify current JDG bank accounts for the bank-freeze motion.
5. **Cofnij EPU** via the portal once Profil Zaufany is active.
6. **File joint ordinary pozew** at Sąd Okręgowy w Krakowie with simultaneous zabezpieczenie motion within 3 months of cofnięcie.

***

## Browser-Agent Prompts for Follow-Up Verification

```prompt-for-browser-agent
URL: https://www.e-sad.gov.pl
Task: Confirm current EPU portal authentication options (Profil Zaufany, Tożsamość MS, in-person). Check whether the case Nc-e 552126/26 still shows active status. Confirm whether the portal's plaintiff workflow includes any form for modifying the list of defendants in an open pozew. Document the exact menu options available to a logged-in plaintiff after opening an existing case. Return screenshots or descriptions of all available action buttons.
```

```prompt-for-browser-agent
URL: https://ekw.ms.gov.pl/eukw_ogol/menu.do
Task: Search for real property (nieruchomość) registered to Waldemar Łopata, NIP 7752083995, address ul. Św. Filipa 23/4, 31-150 Kraków. Try ownership search by name: ŁOPATA WALDEMAR. Document any KW numbers, property addresses, and existing encumbrances. Return all results.
```

```prompt-for-browser-agent
URL: https://www.podatki.gov.pl/wykaz-podatnikow-vat/
Task: Search Biała Lista for NIP 7752083995 (WALDEMAR ŁOPATA 3d Kraków). Extract all bank account numbers currently registered. Return account numbers and bank names for use in a bank-freeze zabezpieczenie motion.
```

```prompt-for-browser-agent
URL: https://www.gov.pl/web/sprawiedliwosc/tabela-oplat-sadowych
Task: Confirm current court fee table for civil cases. Verify: (1) EPU fee = 1.25% of WPS per art. 19 ust. 2 pkt 2 UKSC; (2) ordinary procedure fee = 5% per art. 13 ust. 1 UKSC; (3) that for claims >100,000 PLN the competent first-instance court is sąd okręgowy per art. 17 pkt 4 KPC as in force 2026-05-24. Return the current fee table.
```

***

## Key Statutory References Quick-Sheet

| Article | Provision | Significance |
|---------|-----------|--------------|
| Art. 505^28 §1 KPC | EPU applies postępowanie upominawcze rules with modifications | Founding article |
| Art. 505^29 §1 KPC | Art. 194–198 KPC (subjective change) NOT applicable in EPU | **Bars adding Waldemar inside EPU** |
| Art. 505^31 §1 KPC | Plaintiff files ONLY via system teleinformatyczny | No paper filing by plaintiff |
| Art. 505^33 KPC | No basis for nakaz → umorzenie (NOT transfer) | Post-2020 change |
| Art. 505^34 §2 KPC | Cannot serve abroad → uchylenie nakazu + umorzenie | Service risk for Mateusz |
| Art. 505^36 KPC | Sprzeciw → umorzenie | Post-2020 change |
| Art. 505^37 §2 KPC | Refile within 3 months → date backdates to EPU filing | **Date preservation mechanism** |
| Art. 72 §1 pkt 1 KPC | Substantive joinder (solidary liability = materialne) | Correct joinder basis |
| Art. 72 §2 KPC | Konieczne joinder — NOT applicable to solidary debtors | No compulsory joinder |
| Art. 118 KC | 3-year limitation on commercial claims | Runs to Jan 2029 |
| Art. 123 §1 pkt 1 KC | Pozew interrupts limitation | Preserved via art. 505^37 §2 |
| Art. 441 §1 KC | Solidary liability of joint tortfeasors | Primary theory vs. Waldemar |
| Art. 422 KC | Participation liability (aider/inducer) | Legal basis for Waldemar's tort liability |
| Art. 864 KC | Solidary liability of spółka cywilna partners | Secondary theory |
| Art. 730–739 KPC | Zabezpieczenie roszczenia | Interim measures |
| Art. 79 UKSC | Fee refund on cofnięcie | Full refund before service |
| Art. 17 pkt 4 KPC | Sąd Okręgowy competent for WPS >100,000 PLN | Kraków SO is correct court |

***

*Note: This analysis reflects Polish civil procedure as in force on 2026-05-24 (KPC Dz.U.2026.0.468 t.j., UKSC as amended through 2025). The critical procedural reform (EPU → umorzenie, not transfer) took effect 7 February 2020 (nowelizacja Dz.U.2019 poz.1469). All references to "transfer to sąd właściwości ogólnej" in pre-2020 commentary are obsolete. This analysis is a research map for the plaintiff and their lawyer — it is not a legal opinion and does not substitute for advice from a licensed Polish adwokat or radca prawny.*

---

## References

1. [Rozdział 1. Elektroniczne postępowanie upominawcze - ArsLege](https://arslege.pl/kodeks-postepowania-cywilnego/k14/s673/) - Dz.U.2026.0.468 t.j. , Rozdział 1. Elektroniczne postępowanie upominawcze, Kodeks postępowania cywil...

2. [Rozpatrywanie spraw online i kontaktowanie się z sądami ...](https://e-justice.europa.eu/topics/court-procedures/civil-cases/online-processing-cases-and-e-communication-courts/pl_pl)

3. [EPU w praktyce, czyli jak skutecznie odzyskać pieniądze bez ...](https://kaczmarski.pl/strefa-wiedzy/epu-w-praktyce-czyli-jak-skutecznie-odzyskac-pien) - Do złożenia pozwu potrzebny jest podpis elektroniczny – może to być profil zaufany lub kwalifikowany...

4. [Treść orzeczenia VIII C 1035/20 - Portal Orzeczeń Sądów ...](https://orzeczenia.ms.gov.pl/content/$N/152510150004003_VIII_C_001035_2020_Uz_2021-01-19_001) - ... niedopuszczalna jest podmiotowa zmiana powództwa – nie stosuje się przepisów art. 194 - 196 i ar...

5. [W kwestii przedmiotowej i podmiotowej zmiany powództwa](https://czasopisma.beck.pl/pl/czasopisma/mop/archiwum/2025/4/w-kwestii-przedmiotowej-i-podmiotowej-zmiany-powodztwa) - Artykuł zawiera omówienie dopuszczalności przedmiotowej i podmiotowej zmiany powództwa pod kątem ewe...

6. [Zmiany w kpc – Co zmieniło się w zakresie EPU](https://i-rs.pl/zmiany-w-kpc-co-zmienilo-sie-w-zakresie-epu/) - Ustawą z dnia 4 lipca 2019 r. o zmianie ustawy - Kodeks postępowania cywilnego oraz niektórych innyc...

7. [Ma być sprawniej, ale drożej - Zmiany zasady procedowania](https://kancelarierp.pl/ma-byc-sprawniej-ale-drozej/) - Umorzenie postępowania będzie obligatoryjne przy braku podstaw do wydania nakazu zapłaty lub wniesie...

8. [Elektroniczne postępowanie upominawcze w sprawach niespornych ...](https://gov.legalis.pl/elektroniczne-postepowanie-upominawcze-w-sprawach-niespornych-jako-alternatywa-dla-zwyklego-procesu/) - Umorzenie EPU pociąga za sobą konieczność rozstrzygnięcia o zwrocie kosztów postępowania. W związku ...

9. [Umorzenie postępowania w EPU a przedawnienie](https://pamietnikwindykatora.pl/umorzenie-postepowania-w-epu-a-przedawnienie/) - pomagamy od 2010 roku

10. [Art. 505 [37]. KPC - Kodeks postępowania cywilnego - ArsLege](https://arslege.pl/umorzenie-elektronicznego-postepowania-upominawczego/k14/a9657/) - Art. 505 [37] Kodeks postępowania cywilnego (KPC) . § 1. W przypadku umorzenia postępowania każda ze...

11. [Umorzenie postępowania po przekazaniu z EPU a przerwanie ...](https://www.windykacja.pl/wiadomosci,umorzenie-postepowania-po-przekazaniu-z-epu-a-przerwanie-biegu-przedawnienia-.html) - ... art. 505[37] k.p.c. dochodzi bez oświadczenia powoda o niepopieraniu żądania pozwu, któremu zost...

12. [[PDF] III CZP 66-13.pdf - Sąd Najwyższy](http://www.sn.pl/sites/orzecznictwo/Orzeczenia2/III%20CZP%2066-13.pdf) - podstawie art. 505. 37 § 1 in fine k.p.c. pozew wniesiony nie wywołuje skutków materialnych, to istn...

13. [Uzupełnienie opłaty sądowej od pozwu po przekazaniu sprawy z EPU sądowi ...](https://www.windykacja.pl/poradnik,poradnik-dla-wierzycieli,uzupelnienie-oplaty-sadowej-od-pozwu-po-przekazaniu-sprawy-z-epu-sadowi-wlasciwosci-ogoln.html) - W elektronicznym postępowaniu upominawczym powód wnosi 1/4 opłaty stosunkowej od pozwu tj. 1,25% war...

14. [Granica właściwości rzeczowej sądów cywilnych – jak zmienia się ...](https://porady.pl/granica-wlasciwosci-rzeczowej-sadow-cywilnych-jak-zmienia-sie-kwota-graniczna-i-co-to-oznacza-dla-stron-postepowania/) - Od 1 lipca 2023 r. kwota stanowiąca granicę właściwości rzeczowej pomiędzy sądem rejonowym a sądem o...

15. [Zmiany w przepisach dotyczących właściwości sądu na podstawie ...](https://palestra.pl/pl/czasopismo/wydanie/8-2023/artykul/zmiany-w-przepisach-dotyczacych-wlasciwosci-sadu-na-podstawie-ustawy-z-9.03.2023-r.-o-zmianie-ustawy-kodeks-postepowania-cywilnego-oraz-niektorych-innych-ustaw) - Przedmiotem niniejszego artykułu jest analiza zmian odnoszących się do właściwości sądu dokonanych n...

16. [Sporna kwestia opłat po przekazaniu sprawy przez EPU [OPINIA]](https://serwisy.gazetaprawna.pl/orzeczenia/artykuly/8059115,oplaty-sadowe-po-przekazaniu-sprawy-przez-epu-wykladnia-przepisow.html) - Zmienione przepisy dotyczące elektronicznego postępowania upominawczego (EPU) zaczęły obowiązywać od...

17. [Elektroniczne postępowanie upominawcze (EPU) - co zrobić po ...](https://adwokatztorunia.pl/elektroniczne-postepowanie-upominawcze-(epu)---co-zrobic-po-umorzeniu-sprawy) - Adwokaci z naszej kancelarii w Toruniu posiadają 11 lat doświadczenia w sprawach o zapłatę przed sąd...

18. [Wykorzystanie opłaty po umorzeniu w epu - jak to zrobić?](https://jakzrozumiecprawnika.pl/wykorzystanie-oplaty-po-umorzeniu-postepowania-w-epu-jak-to-zrobic/) - Wykorzystanie opłaty po umorzeniu w epu (elektronicznym postępowaniu upominawczym). Epu umorzenie po...

19. [Zwrot opłaty sądowej w razie cofnięcia pozwu po wydaniu ...](https://smmlegal24.pl/zwrot-oplaty-sadowej-w-razie-cofniecia-pozwu-po-wydaniu-nakazu-zaplaty-ale-przed-przeprowadzeniem-posiedzenia-wyznaczonego-na-rozprawe-z-uwagi-na-brak-mozliwosci-doreczenia-nakazu-zaplaty-pozwanemu/) - Tytułowe zagadnienie nie jest oczywiste i rozstrzygane jest niejednolicie przez doktrynę i orzecznic...

20. [Ustawa z dnia 28 lipca 2005 r. o kosztach sądowych w ...](https://www.gov.pl/web/sprawiedliwosc/ustawa-z-dnia-28-lipca-2005-r-o-kosztach-sadowych-w-sprawach-cywilnych-tj-dzu-z-2020-r-poz-755)

21. [Opłata od pozwu w EPU po przekazaniu sprawy sądowi właściwości ogólnej](https://www.dauerman.com.pl/publikacje/oplata-od-pozwu-w-epu-po-przekazaniu-sprawy-sadowi-wlasciwosci-ogolnej)

22. [NIEDOPUSZCZALNOŚĆ EPU, JAKO JEDNA Z PRZYCZYN ...](https://i-rs.pl/niedopuszczalnosc-epu-jako-jedna-z-przyczyn-przekazania-sprawy-do-sadu-wlasciwosci-ogolnej/) - Elektroniczne postępowanie upominawcze (EPU) wprowadzono do procedury cywilnej na podstawie przepisó...

23. [Współuczestnictwo materialne przy zobowiązaniu solidarnym](https://standardyprawa.pl/standardy/14879) - Najważniejsze fragmenty wyroków! Współuczestnictwo materialne i formalne (art. 72 § 1 k.p.c.): Współ...

24. [Art. 72. Współuczestnictwo materialne, formalne i konieczne](https://standardyprawa.pl/akt/76/art/12802)

25. [Art. 72. KPC - Rodzaje współuczestnictwa w sprawie - ArsLege](https://arslege.pl/rodzaje-wspoluczestnictwa-w-sprawie/k14/a7700/) - Art. 72 Kodeks postępowania cywilnego (KPC) . § 1. Kilka osób może w jednej sprawie występować w rol...

26. [Treść orzeczenia XXVI GCo 3/13](https://orzeczenia.warszawa.so.gov.pl/content/$N/154505000007827_XXVI_GCo_000003_2013_Uz_2013-01-21_001) - Należy zauważyć, że do udzielenia zabezpieczenia nie jest konieczne udowodnienie roszczenia, wystarc...

27. [Treść orzeczenia VIII Gz 309/17](https://orzeczenia.szczecin.so.gov.pl/content/$N/155515000004027_VIII_Gz_000309_2017_Uz_2017-07-28_001) - 730 § 1 k.p.c.). Nie będzie można uznać roszczenia za prawdopodobne, jeżeli w świetle nie budzących ...

28. [[PDF] ISTOTA I FORMY ILOŚCIOWYCH PRZEKSZTAŁCEŃ ... - CEJSH](https://cejsh.icm.edu.pl/cejsh/element/bwmeta1.element.ceon.element-29cabe2a-e139-321b-a082-8c919dde1e0e/c/pdf-01.3001.0012.6921.pdf) - Taką formę zmiany przewiduje art. 193 § 2 k.p.c.. Zmiana powództwa w formie kumulacji doprowadza już...

29. [Hipoteka przymusowa: w kwocie czy do kwoty? Poznaj kluczowe różniceatoffice.pl › hipoteka-przymusowa-w-kwocie-czy-do-kwoty-poznaj-kluczo...](https://atoffice.pl/hipoteka-przymusowa-w-kwocie-czy-do-kwoty-poznaj-kluczowe-roznice) - Zrozum różnice między "hipoteka przymusowa w kwocie" a "do kwoty". Dowiedz się, jak ustala się wysok...

30. [Kaucja na zabezpieczenie roszczenia odszkodowawczego ...](https://standardyprawa.pl/standardy/3602) - Po ustanowieniu przez sąd kaucji obowiązany znajduje się w zakresie swojego roszczenia odszkodowawcz...

31. [Cennik](https://tckancelaria.eu/wp-content/uploads/Cennik.pdf)

32. [Art. 739. KPC - Kodeks postępowania cywilnego - LexLege](https://lexlege.pl/kpc/art-739/) - § 1. Wykonanie postanowienia o udzieleniu zabezpieczenia sąd może uzależnić od złożenia przez uprawn...

33. [System EPU – Elektroniczne Postępowanie Upominawcze](https://www.e-sad.gov.pl/Subpage.aspx?page_id=49)

34. [System EPU – Elektroniczne Postępowanie Upominawcze](https://www.e-sad.gov.pl/Subpage.aspx?page_id=38)

35. [Elektroniczna Skrzynka Podawcza ePUAP](https://www.bialystok.sr.gov.pl/zalatw-sprawe-przez-internet/elektroniczna-skrzynka-podawcza) - Strona Sądu Rejonowego w Białymstoku pełniąca funkcję biuletynu informacji publicznej.

36. [Strona główna - Profil zaufany - Portal Gov.pl](https://www.gov.pl/web/profilzaufany)

37. [[PDF] Rozpatrywanie spraw online i kontaktowanie się z sądami przez ...](https://e-justice.europa.eu/pdf-export/2621_pl)

38. [Treść orzeczenia III Cz 1138/20](https://orzeczenia.gliwice.so.gov.pl/content/$N/151515000001503_III_Cz_001138_2020_Uz_2021-03-23_001) - Zgodnie z art. 505 k.p.c. w przypadku wniesienia sprzeciwu sąd umarza postępowanie w zakresie, w któ...

39. [Treść orzeczenia XXIII Gz 390/21](https://orzeczenia.warszawa.so.gov.pl/content/$N/154505000006927_XXIII_Gz_000390_2021_Uz_2021-07-16_002) - Treść do orzeczenia w sprawie XXIII Gz 390/21 z dnia 20 sierpnia 2021, wydanego przez Sąd Okręgowy w...

