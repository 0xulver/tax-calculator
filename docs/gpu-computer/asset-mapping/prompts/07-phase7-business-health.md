# Phase 7 — Business Health

Goal: determine whether the business is still operating commercially or is winding down. A live, order-taking, customer-facing business is in a different recovery scenario than a defunct shell. This phase also captures the customer-complaint footprint (which can support both civil leverage and criminal-track decisions in `docs/gpu-computer/crime-law/`).

**Time:** 60–90 minutes of agent runtime.
**Cost:** 0 PLN.

---

````
```prompt-for-browser-agent
You are assessing whether a Polish JDG hardware retailer is still actively operating. Look at the live website, marketplace activity, social media, hiring activity, web traffic, and complaint footprint. Passive browsing only — do not place orders, do not submit any form, do not contact anyone.

=== SUBJECT ===
Full name: Mateusz Szklarski-Łopata
Trading as: GPUcomputer
NIP: 8661681248
REGON: 362678345
Website: https://www.gpucomputer.pl/

=== TASK 1 — LIVE WEBSITE TEST ===

Goal: confirm whether the site is up, whether ordering is functional, and capture all bank/legal/contact data.

1. Open https://www.gpucomputer.pl/
2. Fully load the homepage. Record HTTP status and any error banners.
3. Navigate the menu and visit each of:
   - "Konfiguruj komputer" or "Konfigurator" (PC configurator) — if present
   - "Sklep" / "Produkty" (Shop / Products) — pick any one product page
   - "Kontakt" (Contact)
   - "O nas" (About us)
   - "Regulamin" (Terms of service)
   - "Polityka prywatności" (Privacy policy)
   - "Dostawa" (Delivery)
   - "Płatności" (Payments)
   - "Serwis" (Service)
   - "Zwroty / Reklamacje" (Returns / Complaints)
4. On a product page or via the configurator, ATTEMPT to add a product to cart. Record whether the "Add to cart" button is functional and whether the cart page loads with the item. Do NOT proceed to checkout. Do NOT enter any personal data or payment information.
5. From the "Regulamin" and "Polityka prywatności" pages, extract the full company identification section:
   - Legal name (likely "MATEUSZ SZKLARSKI GPUCOMPUTER" or "Mateusz Szklarski-Łopata Gpucomputer")
   - NIP
   - REGON
   - Address(es)
   - Bank account numbers (look for "Numer konta", "Rachunek bankowy", "Numer rachunku")
   - Payment processor names (PayU, Przelewy24, Tpay, BLIK, PayPal, Stripe)
   - Courier names
6. Check the homepage and any visible blog/news section for posts about insolvency, supplier issues, closure, "zawieszona działalność" (suspended business), "ogłoszenie upadłości" (bankruptcy declaration), or supply-chain announcements.
7. Note any banner at the top of the site such as "Tymczasowo nie przyjmujemy zamówień" (We are temporarily not accepting orders).

Return Task 1 as JSON:
{
  "site_up": true/false,
  "http_status": ...,
  "ordering_functional": true/false,
  "addresses_in_regulamin": [...],
  "bank_accounts_in_regulamin": [...],
  "payment_processors": [...],
  "couriers": [...],
  "insolvency_or_closure_notice": "...",
  "most_recent_blog_post_date": "...",
  "screenshots_taken": "..."
}

=== TASK 2 — SIMILARWEB / WEB TRAFFIC TREND ===

Goal: web traffic trajectory signals operational health. A sharp drop after January 2026 (when the debt arose) would indicate the business stopped operating.

1. Open https://www.similarweb.com/website/gpucomputer.pl/
2. Extract: estimated monthly visits over the past 6 months, traffic sources breakdown, bounce rate, engagement.
3. Compute the trend: rising / flat / declining. Note any abrupt drop.
4. If Similarweb shows "Insufficient data" or hides the trend behind a paywall, record exactly what's free and stop without paying.

Return Task 2 as JSON.

=== TASK 3 — JOB BOARDS — HIRING SIGNALS ===

Goal: active hiring suggests ongoing operations; sudden cessation of postings is a distress signal.

Open each board and search for "gpucomputer" and "Mateusz Szklarski":

1. https://www.pracuj.pl
2. https://nofluffjobs.com
3. https://justjoin.it
4. https://bulldogjob.pl
5. https://www.olx.pl (Praca section)

For each active or recently removed listing, extract: title, location, posted date, status (active / closed), employer name. Note especially:
- Recent active listings → business is operating
- Removed listings within the last 2 months → could be deletion linked to financial distress
- Listings showing a non-Mogilska work location → reveals real operating address

Return Task 3 as JSON.

=== TASK 4 — CUSTOMER COMPLAINT FOOTPRINT ===

Goal: aggregate the public complaint pattern about non-delivery and refund failures. This builds the evidence base for both civil leverage and the criminal-law angle (see `docs/gpu-computer/crime-law/`).

1. Open https://www.google.com
   Run these Google searches and capture top 10 results each:
   - "gpucomputer.pl" oszustwo
   - "gpucomputer.pl" "nie odesłał" OR "nie wysłał" OR "nie zwrócił"
   - "gpucomputer.pl" zwrot pieniędzy
   - "GPUcomputer" reklamacja
   - "Mateusz Szklarski" gpucomputer opinia
   - site:wykop.pl gpucomputer
   - site:reddit.com gpucomputer
   - site:reddit.com/r/Polska gpucomputer

2. Open https://www.reddit.com/search/?q=gpucomputer&sort=new
   Capture posts in r/Polska, r/Polski, r/PolskiePC, r/AskPolska — any that mention non-delivery, refund failures, or scam allegations.

3. Open https://www.wykop.pl/szukaj/wpisy/?q=gpucomputer
   Same — capture any negative posts, warnings to community.

4. Open https://www.opineo.pl and https://www.ceneo.pl
   Search "gpucomputer" — capture latest reviews, especially 1-2 star reviews with date stamps.

5. Open https://www.trustpilot.com
   Search "gpucomputer.pl"

6. Open https://www.gowork.pl
   Search "gpucomputer"

For each relevant complaint, extract: platform, URL, date, author display name, short English summary of the complaint, original Polish quote (1–2 sentences max), amount of money involved if mentioned.

Categorize complaints:
- "non_delivery" — paid but never received
- "refund_failure" — received refund agreement but no money
- "delivery_delay" — late but eventually delivered
- "warranty_failure"
- "quality_complaint"
- "other"

Return Task 4 as JSON.

=== TASK 5 — SOCIAL MEDIA ENGAGEMENT TIMELINE ===

(Quick recap from Phase 5 with a different lens — operational tempo, not address discovery.)

1. https://www.facebook.com/search/pages/?q=gpucomputer
2. https://www.instagram.com/explore/tags/gpucomputer
3. https://www.linkedin.com/search/results/companies/?keywords=gpucomputer

For any matching page, record:
- Date of most recent public post
- Posting frequency over the last 12 months (rough estimate)
- Whether posting has dropped off
- Any post text mentioning supplier issues, closure, supply chain, layoffs, business changes

Return Task 5 as JSON.

=== OVERALL OUTPUT ===

Combined JSON with keys "task_1_live_website", "task_2_similarweb", "task_3_job_boards", "task_4_complaints", "task_5_social_engagement", plus a top-level "summary_english" of 4-6 sentences answering:
- Is the business still operating commercially? (yes / partial / no)
- Is ordering functional?
- Is there a complaint pattern consistent with multiple non-deliveries (signalling I'm one of many creditors)?
- Are there visible distress signals (traffic drop, hiring stopped, social media gone quiet, public warnings)?
- Any new bank accounts or addresses surfaced via the live website that weren't in Phase 1?

=== FAILURE HANDLING ===

- CAPTCHA: flag and continue.
- Login walls on Facebook/Instagram/LinkedIn: capture public preview only.
- Similarweb paywall: capture free preview, do not pay.
- Do NOT submit any form, place any order, or send any message.
- Do NOT contact reviewers, page admins, or sellers.

=== STOP CONDITION ===

All five tasks attempted. Return consolidated JSON.
```
````
