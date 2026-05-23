# Asset and Liability Mapping — Research Brief

## Who this is for

External research agents (LLM-based or human) tasked with helping me identify the best methods, sources, and procedures for mapping the **assets, debts, and operational status of a Polish JDG (jednoosobowa działalność gospodarcza) debtor**. The output of this research will determine a near-term strategic legal decision (described below). The deliverable is **not** a guess at the debtor's actual assets — it is a practical, ranked methodology I can execute (or commission) to find them.

## Context — the case

I am a private individual creditor pursuing a **155,000 PLN** debt against a Polish JDG sole proprietorship.

**Debtor identification:**

- Name: **Mateusz Szklarski** (operating as "GPUcomputer")
- Business form: **JDG** (sole proprietorship — unlimited personal liability, no corporate veil)
- CEIDG status: Active since **2015-10-06** (~10 years of trading)
- Registered address: A **virtual office** in Kraków (confirmed by multiple businesses registered at the same address)
- VAT status: Active on the white list (biała lista podatników VAT)
- KRZ (Krajowy Rejestr Zadłużonych): No entries under NIP or name as of **2026-05-21**
- Marital property regime: No community property per CEIDG
- Website: https://www.gpucomputer.pl/
- NIP and REGON: available in the attached CEIDG extract

**The debt:**

- January 2026: I paid 155,000 PLN for a custom-built computer ordered via gpucomputer.pl
- Seller delayed repeatedly, then **agreed to a full refund** (confirmed in writing)
- No refund was made
- Pre-court demand for payment served and delivered
- **8 April 2026:** I filed a payment claim in EPU (Elektroniczne Postępowanie Upominawcze) at Sąd Rejonowy Lublin-Zachód, case **Nc-e 552126/26**
- Debtor stated via email that he "filed for bankruptcy protection" following the collapse of a Hong Kong supplier — but no entry in KRZ corroborates this as of 2026-05-21
- EPU case has shown no movement to date

**Current legal posture:**

- One Kraków lawyer has advised **withdrawing the EPU and filing a regular civil lawsuit at SR Kraków-Śródmieście** bundled with a *wniosek o zabezpieczenie roszczenia* under art. 730–757 KPC (precautionary attachment targeting bank accounts), citing the procedural incompatibility between EPU and zabezpieczenie
- Estimated additional cost: 5,000–8,000 PLN net lawyer fees + ~7,750 PLN court fee + komornik execution costs (~1,000+ PLN)
- Other lawyers consulted are still responding

## The strategic decision this research supports

The choice is between:

**Path A — Stay with EPU.** Wait for the EPU court to issue a *nakaz zapłaty* (estimated 6–12 more months). Accept high probability that the debtor files *sprzeciw* (objection), triggering automatic transfer to the regular Kraków court and restart as a full lawsuit. Eventually enforce whatever judgment results via komornik.

**Path B — Withdraw EPU and file regular lawsuit with zabezpieczenie.** Withdraw EPU (recover ~75% of the EPU court fee), file new lawsuit at SR Kraków-Śródmieście bundled with the zabezpieczenie motion. Goal: get a komornik freeze on debtor's bank accounts within 1–4 weeks of filing — months before any final judgment.

**The decisive factor is whether the debtor has findable, enforceable assets that would still exist by the time a judgment is enforceable.** Specifically:

- If he owns **real estate in his own name** → both paths can eventually capture it via *hipoteka przymusowa*; zabezpieczenie's speed advantage is smaller because real estate cannot vanish.
- If he has **liquid bank balances and easily-shiftable assets** → these will move in 6–12 months; zabezpieczenie urgency is real.
- If he has **effectively no recoverable assets** → both paths yield low recovery; spending 15–25k PLN on zabezpieczenie is wasted.
- If he is genuinely about to file **upadłość konsumencka** → a zabezpieczenie obtained within 2 months of the bankruptcy filing date can be **clawed back** under art. 81 PU.
- If he already has **multiple existing creditors** queuing up → I am racing them for position, and zabezpieczenie urgency increases.

I need to determine the actual asset and liability picture before committing the 15–25k PLN of Path B.

## Executor model and language constraint

**Critical: I do not speak Polish.** I can read English, and I can paste Polish text into translators, but I cannot fluently navigate a Polish-language web portal, fill in forms that use Polish field labels, interpret error messages, or distinguish between similar Polish legal terms in real time.

The actual data-gathering will therefore be executed by a **browser-using agent** — most likely one of:

- **OpenAI Atlas** (agentic browser)
- **Perplexity Comet** (agentic browser)
- **Claude in Chrome** (the Anthropic browser extension that drives the live page)
- Or a comparable agentic browser/automation tool

These agents can read and interact with Polish-language pages, but they need **precise, self-contained instructions** to do so reliably. They are not domain experts on Polish public registries. They will fail silently or hallucinate if the instructions are vague.

**Therefore your research output must, for each source, include a ready-to-paste browser-agent prompt** that the agent can execute end-to-end without further help from me. Treat the browser agent as a competent but non-specialist operator who needs:

- The exact URL to open
- The exact sequence of clicks, field entries, and selections
- The Polish field labels and button labels (with English translations in parentheses)
- The exact input values to use (e.g., "Enter `Mateusz Szklarski` in the field labeled `Imię i nazwisko / Nazwa`")
- What success looks like (what page or response indicates the result)
- What failure modes look like, and how to recover or escalate (e.g., "If the page returns `Brak wyników` (no results), record that and stop")
- What to extract and return to me, in what format (always English-translated)
- Any login, captcha, or paywall it will hit, and how to handle each

Where a source requires actions a browser agent cannot perform (e.g., uploading a notarized power of attorney, paying with a Polish bank transfer, signing with a Profil Zaufany, physically appearing at a starostwo), say so explicitly and flag that the step needs me, my lawyer, or a paid intermediary.

## What we already know and have tried

- **CEIDG extract** (attached PDF): active since 2015-10-06, no community property, broad PKD codes, no phone/email/website on file, no entries about suspension or insolvency, no marital property regime declared
- **Virtual office** registration confirmed by name-overlap with multiple unrelated businesses at the address
- **VAT whitelist**: active
- **KRZ**: no entries under NIP or name as of 2026-05-21
- **Księgi Wieczyste** online portal (ekw.ms.gov.pl): requires KW number; no name-based or address-based search available
- **Website** gpucomputer.pl is live
- **Pre-court demand** for payment was delivered (proof of receipt available)
- **One email from debtor** acknowledging the debt and citing the Hong Kong supplier collapse as justification for "bankruptcy protection"

## What I need you to research

For each of the categories below, identify the best methods/sources for an individual creditor (or a lawyer acting for me) to obtain reliable information. Distinguish open-data sources, restricted sources requiring formal request, and sources accessible only via court or komornik.

### A. Real estate ownership

I need to determine whether the debtor owns any real estate in Poland (residence, investment property, commercial premises, land).

Specifically address:
- How to find KW numbers starting only from a person's name and known addresses, when the central Księgi Wieczyste portal does not allow name-based search
- Use of MSIP Kraków geoportal, geoportal.gov.pl, EGiB (Ewidencja Gruntów i Budynków), ePUAP, and commercial services (ongeo.pl, geo-system.com.pl, others)
- *Wniosek o ujawnienie księgi wieczystej* or other formal requests — who can file, what's required
- Whether ZUS, US, notaries, or starostwa keep searchable name-to-property links
- Cost and lead time of commercial real estate background services
- Whether a komornik, lawyer, or notary has privileged name-based real estate search access
- How a *zlecenie poszukiwania majątku* by a komornik covers real estate
- Realistic accuracy and freshness of each source

### B. Vehicle ownership

Specifically:
- CEPiK access — what is public, what requires standing (e.g., konkretny interes prawny)
- Indirect sources: OLX/OtoMoto listing history tied to phone, email, or business name
- Commercial vehicle history services (historiapojazdu.gov.pl, autobaza.pl, autoDNA, others)
- Whether VIN lookups can be reverse-queried by owner name
- Komornik access to CEPiK via the standard *poszukiwanie majątku* request

### C. Actual operating address / business premises

The registered address is a virtual office. The business must operate somewhere if it is still operating.

Specifically:
- Archive.org / Wayback Machine snapshots of gpucomputer.pl (historical contact and "find us" pages)
- Customer review platforms (Google Maps, Allegro, Ceneo, Trustpilot, Opineo) for mentions of pickup, service, or shipping addresses
- Polish business directories with historical address data (Panorama Firm, PKT.pl, Bisnode, Dun & Bradstreet PL)
- Social media: LinkedIn (the owner), Facebook (the business), Instagram, YouTube, TikTok, GitHub
- WHOIS and historical DNS for gpucomputer.pl (domaintools.com, securitytrails.com, viewdns.info)
- Courier/logistics traces: GLS/InPost/DPD/DHL package origin disclosures
- Industry associations or B2B directories (Krajowa Izba Gospodarcza, branżowe portale IT)
- Job listings on Pracuj.pl, NoFluffJobs, JustJoin, Bulldogjob — historical postings reveal real workplaces

### D. Bank accounts

Komornik can query all banks via OGNIVO once enforcement is active, but a starting hint accelerates this.

Specifically:
- Biała lista podatników VAT — what account numbers are disclosed for a VAT-registered JDG
- Account numbers visible in past invoices, archived terms of service, website checkout/payment pages, or PayU/Przelewy24 redirects
- Whether OGNIVO is accessible to anyone other than komorniks (it is not — confirm)
- Whether a commercial bureau of intelligence can hint at the bank without a komornik request

### E. Other business interests, shareholdings, partnerships

Specifically:
- KRS (Krajowy Rejestr Sądowy) searches by personal name for board membership or shareholding in any sp. z o.o., sp.k., or other registered entities
- CRBR (Centralny Rejestr Beneficjentów Rzeczywistych) — beneficial ownership disclosures
- Partnerships visible from supplier/customer disclosures, joint ventures, government tender records (BIP, eZamówienia)
- Whether the debtor controls assets through nominee directors, family members, or affiliated entities

### F. Other creditors and existing claims against the debtor

This is critical. Multiple existing creditors signals impending insolvency and competition for assets.

Specifically:
- KRD (Krajowy Rejestr Długów) — access process and cost for an individual creditor with a documented claim
- ERIF, BIG InfoMonitor, KBIG (Krajowe Biuro Informacji Gospodarczej) — comparable services, access, cost
- Public court records / *portal informacyjny sądów powszechnych* for prior litigation as defendant
- Komornik proceedings — searchable in any public registry?
- *Licytacje komornicze* portal (licytacje.komornik.pl) — has anything been listed against him?
- ZUS and US (Urząd Skarbowy) debts — disclosed anywhere publicly?
- Mortgages and pledges — visible only if KW numbers are obtained
- *Rejestr Zastawów* (RZ) — pledges over movables, accessible at ms.gov.pl
- BIK (Biuro Informacji Kredytowej) — accessible only to the debtor himself; any workarounds for creditors with standing?
- Pattern over time — has KRD-style registration grown recently?

### G. Operational signals / business health

Specifically:
- Is the business still active commercially (taking new orders)? — test by attempting a quote request from a fresh email
- Recent customer complaints suggesting non-delivery (Reddit, Wykop, Facebook groups, Trustpilot, Allegro feedback, Ceneo opinie, sądu konsumenckiego claims)
- Recent equipment sales by the business on OLX, Allegro, or used-hardware forums (asset stripping signal)
- Recent employment posts or removals (job site activity)
- Web traffic and engagement trend (Similarweb, Ahrefs, SEMrush free tiers)
- Social media activity decay or sudden uptick
- Owner's personal social media — travel patterns, lifestyle signals, distress signals
- Press mentions, sponsorships, trade-show appearances over past 12 months

### H. Insolvency / restructuring filings (deeper than KRZ)

KRZ is the current consolidated register, but check:
- Historical bankruptcy filings before KRZ went live (1 December 2021)
- *Restrukturyzacja* proceedings (sanacja, przyspieszone postępowanie układowe, postępowanie układowe, uproszczone postępowanie restrukturyzacyjne)
- MSiG (Monitor Sądowy i Gospodarczy) full-text search — emsig.ms.gov.pl — for name, NIP, REGON, and business name
- Whether the debtor's "filed for bankruptcy protection" statement could refer to a pending filing not yet entered in any public register, and what the lag between filing and registration is in practice
- Whether a *wniosek dłużnika o ogłoszenie upadłości* is publicly visible before the court rules on it

### I. Spousal asset situation

CEIDG shows no community property — meaning unmarried, widowed, or there is a *rozdzielność majątkowa* (separation of property) regime.

Specifically:
- Public sources for marital status, if any
- USC (Urząd Stanu Cywilnego) access rules for third parties
- *Rejestr Małżeńskich Ustrojów Majątkowych* — does it exist as a public registry?
- Spousal asset visibility — what is recoverable vs. shielded under Polish family-property law if separation of property was established before or after the debt arose
- *Skarga pauliańska* (actio pauliana, art. 527 KC) — what timing and evidence is needed to challenge transfers to family members

### J. Foreign assets / asset-stripping risk

Specifically:
- Signals of foreign bank accounts or asset transfers (residency changes, foreign business filings, EU corporate registers)
- Cross-border enforcement implications under Brussels Ia Regulation
- Cryptocurrency exposure: blockchain analysis from any wallet hints found on the website, in invoices, or in social media

## What I'm asking you to produce

For each category (A–J), deliver one or more **source entries**. Each source entry must contain:

1. **Source name and URL** (or institution name if not a web resource)
2. **Legal access status** — open data / restricted with request / lawyer-only / komornik-only / requires writ
3. **Cost** — approximate, in PLN
4. **Accuracy and freshness** — how reliable, how up-to-date
5. **Time to obtain** — realistic
6. **Caveats / risks** — false negatives, jurisdiction issues, GDPR/RODO considerations
7. **Browser-agent prompt** — a ready-to-paste, self-contained instruction block that I can hand to an agentic browser (Atlas / Comet / Claude in Chrome) which will then perform the lookup without further help from me. Each prompt must include:
   - Exact starting URL
   - Step-by-step navigation in numbered form
   - Polish field/button labels with English translation in parentheses, e.g. `the field labeled "Numer NIP" (NIP number)`
   - Exact input values to type (use the subject identifiers from this brief)
   - Decision branches (e.g., "if the result table is empty, …")
   - What to extract and return to me, translated into English
   - Failure handling: captcha, login wall, paywall, session expiry, no-results page, geo-blocking
   - Stop condition / when to escalate back to me
8. **Skip-if-not-applicable conditions** — when this source is not worth running (e.g., "skip if category A produced no real estate")

If a source cannot be executed by a browser agent (requires Profil Zaufany login, physical visit, signed PoA, court order, etc.), state this clearly in place of the prompt and route the step to me, my lawyer, or a paid intermediary.

Then add an integrating section:

9. **Recommended sequencing — as a runnable plan** — order the browser-agent prompts into a numbered execution sequence I can hand to the agent in one batch, so the first hour, first day, and first week of investigation are each a self-contained, runnable script. Specify dependencies (e.g., "Step 7 needs the KW number found in Step 3").
10. **Cost-effective stopping points** — at what cumulative OSINT spend is it better to commission a komornik enquiry, biuro wywiadu gospodarczego report, or detektyw than to continue browser-agent investigation
11. **Red flags to look for** — patterns indicating asset stripping, imminent bankruptcy, sophisticated debtor evasion, or coordination with prior failed entities (described in English, with the Polish terms or document markers that would surface them)
12. **Professional escalation** — which professional (kancelaria adwokacka, komornik, detektyw licencjonowany, biuro wywiadu gospodarczego, firma windykacyjna) for which question, what each typically costs and delivers, and whether their work product comes back in Polish only or with English translation

## Useful primitives the agent may not know

- **Zlecenie poszukiwania majątku** — a creditor can commission a komornik to query banks (OGNIVO), ZUS, US, CEPiK, Centralna Baza Danych Ksiąg Wieczystych, and other registers. Costs ~100 PLN flat plus a 10% komornik fee on recovered amounts. **Requires an enforcement title** (*tytuł wykonawczy*), which I do not yet have. Therefore not usable until either the EPU produces a nakaz or a zabezpieczenie is granted in the regular court.
- **Biuro wywiadu gospodarczego** — commercial intelligence bureaus (e.g., Bisnode Polska, Coface, Creditreform, KRD's wywiad ekonomiczny add-on, Skarbiec) compile open and licensed-data reports. Typically 500–3,000 PLN per subject, 1–5 business days.
- **Detektyw licencjonowany** — licensed private investigator under the *ustawa o usługach detektywistycznych*. Can do lawful observation and asset mapping. Typically 200–500 PLN/hour.
- **Lawyer-assisted queries** — the lawyer I retain can submit *zapytania* to certain registers and prepare the evidentiary basis for the zabezpieczenie motion. Some queries are accessible only with active legal mandate.

Recommend when each of these is the right escalation point relative to DIY OSINT.

## Output format

Structured markdown response. For each category A–J, use a consistent subheading with the per-source entries ranked from highest signal-per-złoty to lowest. Each source entry must include the browser-agent prompt as specified above. Conclude with the integrating "Recommended investigation plan" section (items 9–12 above).

The browser-agent prompts should be formatted as **fenced code blocks** so I can copy them verbatim into the agentic browser. Example shape:

````
```prompt-for-browser-agent
Open https://example.gov.pl

1. On the homepage, find and click the link labeled "Wyszukaj podmiot" (Search entity).
2. In the field labeled "Imię i nazwisko" (Full name), type: Mateusz Szklarski
3. Click the button labeled "Szukaj" (Search).
4. If the result page shows "Brak wyników" (No results), record "No results" and stop.
5. If results appear, for each row extract: name, NIP, address, status.
6. Translate all extracted fields to English and return them as a JSON object.

If you hit a CAPTCHA, stop and report "CAPTCHA blocking — needs human".
If the page requires login via Profil Zaufany, stop and report "Profil Zaufany required — cannot proceed".
```
````

Length target: thorough but not exhaustive. Prefer concrete sources, URLs, and executable prompts over generic advice. Where you are uncertain (e.g., whether a register accepts third-party queries in 2026, or whether a portal's UI labels have changed), say so explicitly rather than guessing — the browser agent will fail if instructions reference fields that no longer exist.

## Constraints

- All methods must be legal under Polish law and EU GDPR/RODO
- No suggestions involving deception, unauthorized access, social engineering of the debtor or third parties, pretexting, or coercive contact
- Distinguish clearly between data accessible to anyone, data accessible to an interested party with formal request, and data accessible only via court or komornik
- Distinguish carefully between **finding** information (lawful OSINT) and **using** it as court evidence (which may require formal certified copies)
