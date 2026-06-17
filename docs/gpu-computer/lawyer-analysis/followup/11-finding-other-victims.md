# Prompt 11 — Finding other victims of GPUcomputer / Mateusz Szklarski / Waldek Łopata

## Role
You are an OSINT investigator and Polish-market consumer-fraud researcher. Your
job is to find **other customers of GPUcomputer who lost money or were deceived**
— people who paid and got nothing, got something different from what they
ordered, were strung along with excuses, were refused refunds, or who publicly
warn others that the business is a scam. Search exhaustively across the open web,
Polish-language sources, marketplaces, review sites, social media, forums, and
court/registry records. Report every lead with a verbatim quote, a direct URL,
a date, and an honest confidence rating.

## Why this matters (the goal)
I (Magnus Brantheim) paid GPUcomputer **155,000 PLN** for an ML workstation that
was never delivered and never refunded. I am building a criminal fraud case
(art. 286 § 1 KK). Two things make finding other victims decisive:

1. **It converts "a deal that went bad" into a scheme.** A single non-delivery
   reads to a Polish prosecutor as a civil dispute (spór cywilny) and tends to
   be screened out. A *pattern* of identical conduct against multiple customers
   is the strongest possible proof of fraudulent intent (zamiar bezpośredni) at
   the moment of contracting — it is what gets an investigation opened.
2. **It can cross the 200,000 PLN threshold.** Polish law treats fraud against
   *mienie znacznej wartości* (property of significant value, **> 200,000 PLN**)
   as an aggravated type under **art. 294 § 1 KK**, punishable by 1–10 years
   (vs. up to 8 for the basic type). My 155k plus even one more victim with
   ≥45k PLN — or several smaller losses aggregated in one investigation — pushes
   the total over that line and raises the case's priority and gravity.

So: **every other victim you find, of any amount, has value.** Small losses
aggregate; large losses cross the threshold; even non-monetary deception
(bait-and-switch, fake stock, fake reviews) corroborates the pattern.

## The target (identifying details)
- **Business name:** GPUcomputer (also written "GPU computer", "GPUComputer").
- **Website:** gpucomputer.pl (store page gpucomputer.pl/sklep).
- **Legal form:** JDG (Polish sole proprietorship / jednoporządkowa działalność
  gospodarcza), registered in CEIDG.
- **Registered owner:** **Mateusz Szklarski**. NIP **PL8661681248**.
- **De facto operator:** **Waldemar Łopata** ("Waldek"), who runs the
  @gpucomputer.pl mailboxes (incl. waldek@gpucomputer.pl) and day-to-day
  dealings; not the registered owner; not VAT-registered.
- **Address (virtual office):** ul. Mogilska 16/7, 31-516 Kraków.
- **Prior / related branding:** **"3dkrakow"** — co-branding present on the site
  since 2016; a likely earlier or parallel trading name. Search it as a separate
  entity.
- **Phones seen on the site:** +48 883 109 779; +48 12 350 6665 / 12 3337730.
- **Emails:** gpucomputer@gpucomputer.pl, waldek@gpucomputer.pl,
  mateusz@gpucomputer.pl.
- **Products:** custom PC / ML workstations, GPU render nodes, CPU workstations,
  servers; mail-order only ("sklep wysyłkowy"), DPD/UPS shipping, LeaseLink
  financing offered.

## Search strategy — be exhaustive, search in Polish and English

Run searches in **Polish first** (this is a Kraków business and most victims will
be Polish). Use these query families and adapt:

**Scam / complaint searches (Polish):**
- `gpucomputer oszustwo`, `gpucomputer oszust`, `gpucomputer naciągacz`,
  `gpucomputer uważajcie`, `gpucomputer nie polecam`, `gpucomputer opinie`,
  `gpucomputer.pl opinie`, `gpucomputer reklamacja`, `gpucomputer zwrot pieniędzy`,
  `gpucomputer nie wysłali`, `gpucomputer nie dostałem`, `gpucomputer przekręt`
- Same set for `3dkrakow` / `3d krakow` / `3dkrakow.pl`.
- Personal-name searches: `Mateusz Szklarski oszustwo`, `Mateusz Szklarski
  GPUcomputer`, `Waldemar Łopata oszustwo`, `Waldek GPUcomputer`,
  `Szklarski Mateusz NIP 8661681248`.

**Where to look (check each explicitly and report what each returned):**
- **Google / Bing / DuckDuckGo** web + maps. Pull the **Google Maps / Google
  Business** reviews for GPUcomputer and for the Mogilska 16/7 listing — read
  every negative review and quote it.
- **Review platforms:** Opineo, Ceneo (seller reviews), Trustpilot, Allegro
  seller ratings & negative comments, OLX seller profile, Facebook
  page/reviews, Google reviews.
- **Polish forums & communities:** Wykop.pl, PCLab/ppe/benchmark.pl forums,
  Reddit (r/Polska, r/polishgaming, r/buildapcsales, r/pcmasterrace),
  elektroda.pl, optyczne/fotograficzne forums (render workstations), dev/ML
  communities.
- **Scam-warning registries (Polish):** the police/UOKiK scam lists, "fałszywe
  sklepy" lists, BIK/Bezpieczny e-commerce style warnings, scam-checker sites
  (e.g. scamadviser, similar Polish equivalents), and any "ostrzeżenia przed
  oszustami" threads.
- **Court & registry records:** SAOS (System Analizy Orzeczeń Sądowych,
  saos.org.pl) for any judgment naming Szklarski / Łopata / GPUcomputer;
  Krajowy Rejestr Zadłużonych (KRZ) for insolvency/enforcement entries; e-court
  / Lublin EPU mentions; CEIDG history for the JDG.
- **Social media:** Facebook (the business page AND personal profiles, public
  posts/comments warning others), LinkedIn, X/Twitter, YouTube comments,
  Instagram.
- **Wayback Machine / archive.today:** archived versions of the site, of any
  review pages later deleted, and of any complaint threads.

**Pivot on what you find.** If a victim names a different alias, account number,
phone, email, or trading name, search that too. Bank account
**PL84 2490 0005 0000 4530 9127 6540** (Alior) is associated with the business —
search it. Look for repeated phrasing ("dostawca z Hongkongu", "towar odprawiony
przez urząd celny", refund-in-14-days promises) that matches the excuses I was
given — identical scripts across victims are strong evidence.

## What counts as a relevant finding (rank these)
1. **A named or contactable person who lost money** (paid, no delivery / no
   refund) — highest value. Capture amount, date, what they ordered, how they
   were strung along, and any contact handle.
2. **A public complaint/review describing deception** (bait-and-switch, fake
   stock, fake insurance, ignored reclamations) even without a clear amount.
3. **A scam warning / "uważajcie" post** naming the business or the people.
4. **A court/registry record** (judgment, EPU order, KRZ entry, debt) involving
   the same persons or NIP.
5. **Pattern corroboration** — repeated excuse-scripts, deleted reviews,
   suspicious 5-star review bursts, multiple disputed transactions.

## For every lead, report (table + notes)
| # | Source/platform | Direct URL | Date | Who (handle/name) | Amount (PLN) | What happened (verbatim quote in original language + EN translation) | How to contact them | Confidence (high/med/low) + why |

Then for each: note whether the conduct **matches my pattern** (prepayment →
non-delivery → excuses → no refund), and whether the person seems reachable to
give a witness statement.

## Output format
1. **Bottom line:** how many credible other-victim leads found, rough total of
   any quantifiable losses, and whether the pattern looks systematic.
2. **Ranked findings table** (above).
3. **Aggregation estimate:** my 155k + the quantifiable found losses = running
   total, and whether it plausibly crosses 200,000 PLN (art. 294 § 1 KK).
4. **Best leads to contact** — the 3–5 most promising, reachable victims and how
   to approach them.
5. **Where I should keep looking** — platforms/queries not yet exhausted, and
   any places that require a login/manual check you couldn't fully access.
6. **Negative results, stated honestly** — which searches returned nothing, so I
   know the footprint's true size and don't assume coverage that didn't happen.

## Integrity rules
- **Quote, link, date everything.** No paraphrased "I saw a complaint" without a
  URL. If you cannot verify, label it clearly as unverified.
- **Do not fabricate victims, reviews, amounts, or quotes.** A small number of
  real leads is worth far more than a long invented list — this feeds a criminal
  complaint and inventions would destroy its credibility.
- **Distinguish the two trading names** (GPUcomputer vs 3dkrakow) and note when a
  finding ties them together.
- **Flag deleted/archived content** (Wayback) separately from live content.
- Do not contact anyone; only find and report. I will decide on outreach.
