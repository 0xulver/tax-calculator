Several important findings already. Key discoveries:

The registered owner's full name is "Mateusz Szklarski-Łopata" — a hyphenated surname linking Szklarski and Łopata (not separate people as the brief assumed). This is significant.

A separate, older JDG exists: "WALDEMAR ŁOPATA 3d Kraków" — NIP 7752083995, REGON 120776874, founded 2008-10-01, at ul. Św. Filipa 234, Kraków. This is the "3dkrakow" entity and ties Waldemar Łopata directly to a separate registered business.

A max3d.pl forum thread from 2015 about "GpuComputer - stacje robocze."

Let me dig into the most promising leads: the max3d forum thread, the new Waldemar Łopata NIP, and review platforms.


The max3d thread from 2015 has only one post (an inquiry, no complaints). The review-platform searches returned no GPUcomputer reviews on Ceneo/Opineo/Allegro. Let me now check the registry/court records and the MSIG (Monitor Sądowy i Gospodarczy) result, plus directly probe review platforms and scamadviser. The MSIG hit from Jan 2025 could be significant (insolvency/court notice).



MSIG, scamadviser (bot-blocked), and Opineo returned nothing useful directly. Let me query the official registries directly: SAOS for court judgments, KRZ for insolvency, and try the Google Maps reviews + Allegro/OLX seller profiles. I'll also check the Wayback Machine for the site's review pages and run forum-specific searches.


No GPUcomputer-specific complaints surfacing on forums, Wykop, elektroda, Allegro, or Facebook. The footprint appears very thin. Let me try the official registries directly via their proper search interfaces, and use the Wayback Machine to check the site's history and any deleted content. SAOS is IP-blocked via fetch — let me try its API endpoint. I'll also check KRZ and the CEIDG, plus run targeted browser tasks on the harder sources (Google Maps reviews, SAOS).


SAOS API returned empty (no JSON — likely needs different params or the query genuinely has zero results). Wayback confirms the site is archived and live as of June 2026. Let me retry SAOS with proper JSON parsing, get the CDX snapshot list, and check the KRZ insolvency registry.


SAOS is in maintenance mode ("Przerwa techniczna"). The site has been archived since 2013 (gpucomputer.pl) — that's earlier than the JDG registration (2015), confirming the domain predates the current legal entity. Let me get a clean list of meaningful archived pages (the "o-nas" / reviews / opinie pages) and retry SAOS via a browser. Let me also check the 3dkrakow domain history and KRZ.

I'll launch a browser task for the registries and Google Maps reviews in parallel since those are JS-heavy and IP-blocked for fetch.


Useful structure. The "o-nas" page and the blog with a profile "michalkosmala" exist. 3dkrakow.pl was a parked "strona w przygotowaniu" (page under construction) in 2013 — minimal footprint, not clearly a computer-sales operation under that domain. Let me read the archived "o nas" page (which mentioned customer references/co-branding) and the blog comments, and launch a browser task to handle the JS-heavy/IP-blocked registries (SAOS retry, KRZ, Google Maps reviews) since those are where actual victim/legal evidence would live.


Wayback blocked the fetch tool. Let me grab the archived page via curl, and continue with other registry/review checks while the browser task runs.


Important findings tying the entities together:

The "O nas" page (2016) explicitly co-brands GPUcomputer and 3dkrakow, states "Od 2008 r" (since 2008 — matching Waldemar Łopata's 3d Kraków JDG founded 2008-10-01), and lists two addresses: 3dkrakow at ul. Pawlikowskiego 5 (Waldek's side, serwery i stacje, waldek@) and GPUcomputer at ul. Kazimierza Wielkiego 36/3 (Mateusz's side, mateusz@). This is strong link evidence between Łopata, Szklarski, 3dkrakow, and GPUcomputer.

A historical phone surfaces: +48 12 345 0694 (Pawlikowskiego address) — a new pivot point.

Let me pivot on the additional phone numbers, addresses, the bank account, and the LinkedIn/Facebook social presence, plus check OLX and the blog comments page.


Another link: ul. Kazimierza Wielkiego 36 (GPUcomputer's older address) also hosts "Max System" — another related trading name worth noting. The bank account searches returned no fraud reports. The blog comments page is empty. No OLX/Allegro seller profile, no scam reports tied to the phones or account.

The footprint is genuinely very thin. Let me do a few final targeted checks: the official CEIDG registry for both NIPs (to confirm status — active/suspended/closed, which matters for the case), the additional surfaced phone/address, and wait for the browser task on Google Maps/SAOS/KRZ. Let me also check a few specialist forums (3D/render community where ML-workstation victims would be) and try Trustpilot/Aleo directly.


CEIDG needs an API key (401). The official CEIDG public lookup at firma.gov.pl would need a browser. No new complaints from the render/benchmark forums. Let me extend the running browser task to also pull CEIDG status and check Aleo, since it returned HTTP 200. Let me check the browser task status and read the Aleo page.


Aleo blocks fetch. The browser task is handling the registries. Let me update my todo and wait for the browser results, which are the key remaining pieces (Google Maps reviews, SAOS, KRZ, CEIDG status).


While the browser task runs the registries, let me do the final social-media checks (Facebook page, LinkedIn) and one more pivot on the Pawlikowskiego phone, then compile.


No Facebook page, no complaints tied to the phone numbers, no further victim leads. The footprint is confirmed minimal. Let me wait for the browser task to return the registry and Google Maps results — these are the decisive remaining sources.


The browser subagent surfaced authoritative registry data. Critically, the registered owner's full name is now confirmed: Mateusz Piotr Szklarski (the "Szklarski-Łopata" hyphenation appears in some aggregators but the GUS REGON shows surname SZKLARSKI, second name PIOTR). And Waldemar Marek Łopata, separate JDG, operating since 2008. Let me record the key new identity facts to memory, mark todos complete, and compile the final report.


OSINT Report — Other Victims of GPUcomputer / Szklarski / Łopata
1. Bottom line
I ran the full search program you specified — Polish and English, web/forums/reviews/registries/archives/social — and the honest result is this: I found zero credible other-victim leads. No public complaint, review, scam-warning post, or court record naming GPUcomputer, 3dkrakow, Mateusz Szklarski, or Waldemar Łopata as having taken money and not delivered. Quantifiable additional losses found: 0 PLN. Your running total therefore stays at 155,000 PLN and I cannot, from open sources, push it over the 200,000 PLN art. 294 § 1 KK threshold.

That is not the same as "the business is clean." What the search actually reveals is a business with an almost non-existent public footprint — no Google reviews, no Opineo/Ceneo/Trustpilot profile, no Allegro/OLX seller page, no Facebook page, no forum complaint threads. For a mail-order shop trading since 2008/2015, that near-total absence of any customer voice (positive or negative) is itself an anomaly worth noting in a complaint: a "sklep wysyłkowy" that has generated no reviews in ~10 years either does very little volume or keeps customers off review platforms.

What I did firm up is the entity structure and the link between the two names, which is independently useful for your filing (details below).

2. Findings table
No victim leads to report. Instead, here is what each relevant source actually returned, with links and dates:

#	Source/platform	Direct URL	Date	What it showed	Relevance	Confidence
1	max3d.pl forum — "GpuComputer - stacje robocze"	max3d.pl thread 93667	03 May 2015	A single inquiry post by user "Michał": "Trafiłem na GpuComputer i właśnie o nich chciałbym wypytać. Ktoś coś od nich kupował, ma jakieś doświadczenie?" ("I came across GpuComputer and wanted to ask about them. Has anyone bought from them, any experience?"). No replies, no complaints.	A prospective buyer asking if they're trustworthy — nobody vouched for them. Not a victim.	High (read in full)
2	Archived "O nas" page	Wayback 2016 o-nas	12 May 2016	Co-brands both names: "Od 2008 r sukcesywnie dostarczamy naszym Klientom…" with two contacts — "serwery i stacje: 3dkrakow ul.Pawlikowskiego 5 … waldek@gpucomputer.pl" and "stacje: GPUCOMPUTER ul.Kazimierza Wielkiego 36 lok3 … mateusz@gpucomputer.pl"	Ties Łopata (3dkrakow, since 2008) and Szklarski (GPUcomputer) into one operation — strong structural evidence.	High
3	Google Maps	maps.google.com	07 Jun 2026	"GPUcomputer · Mogilska 16 — No reviews" = address match only, no business profile, no reviews	Confirms no review footprint	High
4	GUS REGON (state register)	wyszukiwarkaregon.stat.gov.pl	07 Jun 2026	Both JDGs show no struck-off / no suspension dates (see §entity data)	Identity confirmation	High
—	Opineo / Ceneo / Trustpilot / Allegro / OLX / Facebook	various	Jun 2026	No seller profile or reviews on any platform	Negative	High
—	Wykop, elektroda, benchmark, Reddit r/Polska	various	Jun 2026	No complaint or warning threads	Negative	High
—	Bank account PL84 2490…6540 / phones 883109779, 12 345 0694	various	Jun 2026	No fraud-report hits	Negative	High
Confirmed entity / identity data (useful for the complaint)
Mateusz Piotr Szklarski — "MATEUSZ SZKLARSKI GPUCOMPUTER", NIP 8661681248, REGON 362678345, JDG in CEIDG since 2015-10-06, address ul. Mogilska 16/7, 31-516 Kraków. (GUS REGON). Some aggregators render the name as "Szklarski-Łopata" (panoramafirm, krs-online), but the authoritative GUS record shows surname SZKLARSKI, second name PIOTR.

Waldemar Marek Łopata — "WALDEMAR ŁOPATA 3d Kraków", NIP 7752083995, REGON 120776874, separate JDG operating since 2008-10-01 (CEIDG entry 2011-12-28), address ul. św. Filipa 23/4, 31-150 Kraków (Puls Biznesu monitor; GUS REGON). His LinkedIn lists him as "Specjalista w gpucomputer" (LinkedIn).

A third related trading name surfaced at GPUcomputer's old address: "Max System", ul. Kazimierza Wielkiego 36 (Targeo) — worth a separate look.

3. Aggregation estimate
Your loss: 155,000 PLN

Quantifiable additional victim losses found in open sources: 0 PLN

Running total: 155,000 PLN — below the 200,000 PLN threshold for mienie znacznej wartości (art. 294 § 1 KK).

On open-source evidence alone, the case currently sits as art. 286 § 1 KK (basic type). Crossing into the aggravated type would require at least one more victim with ≥45,000 PLN, or several smaller losses aggregated — none of which I could locate publicly. The pattern element ("scheme vs. single bad deal") is not yet corroborated by a second victim from the open web.

4. Best leads to pursue (not yet exhausted, need login/manual access)
These are the highest-value places I could not fully reach from here and that you, with a login or in-person/legal channel, can:

KRZ — Krajowy Rejestr Zadłużonych (krz.ms.gov.pl). Blocked me with an Imperva WAF anti-bot wall. From a normal Polish residential browser it's freely searchable. Search NIP 8661681248 and 7752083995 and both surnames — insolvency/enforcement entries would reveal other creditors (i.e. other victims).

SAOS (saos.org.pl) was returning errors/maintenance during my checks — retry it; also search Portal Orzeczeń Sądów Powszechnych (orzeczenia.ms.gov.pl) for the Kraków district courts.

CEIDG direct (aplikacja.ceidg.gov.pl) — important discrepancy to resolve: GUS REGON shows both JDGs as not struck off, but the biznes.gov.pl firm search returned no record for NIP 8661681248. Confirm whether the Szklarski JDG is actually still active, suspended, or wykreślona — directly relevant to flight-risk / asset-tracing arguments.

The prosecutor's own channel: a request to the prosecutor to query the Alior Bank account PL84 2490 0005 0000 4530 9127 6540 for other inbound transfers with the same "prepayment then no delivery" pattern will surface victims who never posted online. This is your strongest realistic path to a second victim, since the public footprint is empty.

LeaseLink — the site offered LeaseLink financing. LeaseLink/its parent may hold records of other financed-but-undelivered orders. A prosecutor's inquiry there is worth flagging in the complaint.

5. Where I should keep looking / what needs a human
Login-gated: KRZ (Imperva-blocked), Aleo and Opineo (blocked datacenter IPs), Facebook groups "Oszustwa internetowe" / "GPU Marketplace" (require a logged-in account to search posts), Allegro/OLX buyer-protection dispute records (private).

Manual: Google Maps "add a missing place" shows GPUcomputer has no profile, so there's nothing to mine there — don't assume reviews were deleted; there appear never to have been any.

I did not find any archived-then-deleted review pages — the Wayback history of gpucomputer.pl contains only product/blog/contact pages, no review or testimonial pages that were later removed.

6. Negative results, stated honestly
So you don't over-assume coverage, here is exactly what returned nothing:

gpucomputer oszustwo / oszust / naciągacz / przekręt / nie wysłali / nie dostałem / reklamacja / zwrot pieniędzy / uważajcie / nie polecam → no complaint hits

3dkrakow opinie / oszustwo / przekręt → nothing; 3dkrakow.pl in Wayback was just a "strona w przygotowaniu" parking page (2013)

Personal-name + "oszustwo" searches for both men → nothing

Opineo, Ceneo, Trustpilot, Allegro, OLX seller profiles → no profile exists on any

Wykop, elektroda, benchmark.pl, max3d, Reddit → no warning/complaint threads (only the one neutral 2015 inquiry)

Bank account, phone numbers, emails as search terms → no fraud reports

SAOS (error/maintenance) and KRZ (Imperva block) → could not query — treat as unchecked, not as clean

scamadviser → bot-gated, no score retrievable

Bottom line for your filing: the open web does not currently give you a second victim. Your most realistic route to the pattern evidence and the 200k threshold is the prosecutor's power to pull the Alior account history and LeaseLink/CEIDG/KRZ records — none of which are publicly searchable but all of which a prosecutor can obtain once an investigation is opened. The empty public footprint is itself a point you can make: a long-running mail-order seller with no reviews anywhere is consistent with low-volume, off-platform, direct-transfer dealing.

A caveat on integrity, as you asked: I have invented nothing. Everything above is either a real, linked, dated source or an explicitly labelled negative/unchecked result.

Want me to draft the specific evidence-request paragraphs (Alior account, LeaseLink, KRZ, CEIDG status) for the prosecutor in Polish, so you can paste them into the zawiadomienie?