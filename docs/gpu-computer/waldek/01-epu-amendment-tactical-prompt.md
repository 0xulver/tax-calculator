# EPU Amendment vs. Parallel Suit — Tactical Research Prompt

## Purpose

Drilled, focused sub-prompt for the procedural question that gates the entire
joint-liability strategy. The broader legal-grounds question is in
`00-joint-liability-research-brief.md`. Run this one separately because the
answer is time-sensitive and binary enough that a high-density tactical query
will outperform a sprawling brief.

Target agents: ChatGPT 5.5 Pro, Perplexity Pro, Gemini 3.1 Deep Research.
Length budget for each output: 1,500–3,500 words. Tactical, not academic.

---

## The question in one sentence

I have a pending EPU case (Nc-e 552126/26, Sąd Rejonowy Lublin-Zachód, filed
2026-04-08) against a single defendant (Mateusz Szklarski-Łopata). The court
has not issued a *nakaz zapłaty* yet. I want to add a co-defendant (Waldemar
Łopata) on a joint-tortfeasor / spółka-cywilna theory. **Can I do that
inside EPU without losing my filing date, and if not, what is the right
procedural move?**

## Facts the agent must hold fixed

- Case: **Nc-e 552126/26**
- Court: **Sąd Rejonowy Lublin-Zachód w Lublinie, VI Wydział Cywilny**
  (the centralised EPU court for all of Poland)
- Filing date: **2026-04-08**
- Status as of 2026-05-24: **no nakaz zapłaty issued**, no sprzeciw, no
  procedural order visible to me. The case has effectively not moved.
- Plaintiff: me, private individual creditor (Polish national, resident
  abroad)
- Defendant currently named: Mateusz Szklarski-Łopata (JDG GPUcomputer, NIP
  8661681248), CEIDG-registered at a virtual office in Kraków, physically
  resident in Eindhoven NL since October 2022
- Defendant I want to add: Waldemar Łopata (JDG "WALDEMAR ŁOPATA 3d Kraków",
  NIP 7752083995), Kraków-resident, active 17+ years, same vertical
- Claim value: 155,000 PLN principal + statutory interest + costs
- Theory for adding Waldemar: see `00-joint-liability-research-brief.md` —
  primarily art. 422 + art. 441 KC joint tortfeasor liability, with a
  secondary spółka-cywilna theory under art. 860 + art. 864 KC

## Exactly what I need answered

### 1. Subjective amendment in EPU — is it even allowed?

Cite the controlling provisions (art. 505^28 et seq. KPC and the procedural
rules of the EPU portal). EPU is designed for fast, document-only,
*nakaz zapłaty* against one or more named defendants on the basis of the
pozew alone. The plaintiff cannot generally amend the *podmiotowy zakres
sporu* (subjective scope of dispute) mid-proceeding **without triggering a
procedural consequence**. Specifically:

- Can I file an amended pozew adding Waldemar via the EPU portal at this
  stage?
- If yes, on what form, with what fee, in what time window relative to the
  current status of the case?
- If no, is the only path to: (a) withdraw EPU and file fresh in ordinary
  procedure, (b) wait for the nakaz to issue against Mateusz then sue
  Waldemar separately, or (c) get the case transferred to ordinary
  procedure (sąd właściwy według właściwości ogólnej) where amendment is
  freely allowed under art. 193 KPC?

### 2. What triggers transfer out of EPU to ordinary procedure?

Under what mechanism does an EPU case get kicked to the ordinary court:

- Art. 505^33 KPC — court refuses to issue nakaz and transfers
- Art. 505^36 KPC — sprzeciw by defendant
- Plaintiff's own initiative — is there a *wniosek o przekazanie sprawy*?

If I want the case to go to ordinary procedure precisely so I can add
Waldemar there, what is the cleanest procedural move? Filing an
amendment adding Waldemar is itself one of the listed transfer triggers in
the doctrinal commentary I've skimmed — I want this confirmed against the
current 2026 KPC.

### 3. Does the EPU filing date survive transfer?

If the case is transferred to the Kraków ordinary court, what counts as the
**date of bringing the suit** (*wniesienie pozwu*) for purposes of:

- Statute of limitations (art. 118 KC, 3-year commercial limitation)
- Interruption of limitation (art. 123 § 1 pkt 1 KC)
- Lis pendens (art. 192 KPC)
- Priority of *zabezpieczenie roszczenia*
- Interest accrual on procedural costs

Specifically: does the 2026-04-08 EPU filing date carry over, or does it
reset to the date the ordinary court receives the file?

### 4. The court fee differential

EPU fee was 1.25 % of the claim (≈ 1,937 PLN for 155k). Ordinary procedure
fee is 5 % (≈ 7,750 PLN). On transfer:

- Does the plaintiff have to pay the differential? (Yes, presumably — art.
  19 / 20 / 28 of the *Ustawa o kosztach sądowych w sprawach cywilnych*.)
- Within what deadline?
- What happens if the differential is not paid — does the case dismiss?
- If both defendants are named in the ordinary case, does the fee scale by
  number of defendants or stay flat at 5 % of claim value?

### 5. Alternative — keep EPU, file separately

Compare the cost and timeline of two alternative paths:

**Path A — Amend EPU adding Waldemar:**
1. Submit amended pozew via EPU portal naming both defendants
2. EPU court likely refuses to issue joint nakaz and transfers under art.
   505^33 KPC
3. Kraków ordinary court takes the case; plaintiff pays the 3.75 % fee
   differential
4. Ordinary procedure: defendant service, first hearing, evidence phase,
   judgment

**Path B — Keep EPU against Mateusz, file separate pozew against
Waldemar:**
1. EPU proceeds against Mateusz alone. If nakaz issues, enforcement starts
   against Mateusz's thin Polish surface + EAPO against Dutch wages
2. In parallel, file a fresh pozew against Waldemar in Sąd Okręgowy w
   Krakowie (claim > 100k → okręgowy jurisdiction) with 5 % fee (7,750
   PLN)
3. Two judgments emerge on different timelines
4. Optional: motion under art. 219 KPC to connect the cases — declined
   because they're at different courts

**Path C — Withdraw EPU, refile a single ordinary pozew naming both:**
1. *Cofnięcie pozwu* in EPU (with consequences for the 1,937 PLN fee
   already paid — is it refundable per art. 79 UKSC?)
2. Fresh pozew in Sąd Okręgowy w Krakowie naming both, 5 % fee
3. Single proceeding, single judgment, simplest enforcement
4. Risk: lose the 2026-04-08 filing date entirely

For each path, produce:
- Net out-of-pocket cost (court fees, lawyer fees, lost EPU fee)
- Expected calendar time to judgment
- Filing-date / limitation impact
- Litigation risk relative to the other paths

### 6. Joinder rules — art. 195–198 KPC

If Waldemar is named, what is the correct joinder basis under KPC?

- **Współuczestnictwo materialne (substantive joinder, art. 72 § 1 pkt 1
  KPC)** — joint liability arises from the same legal relationship.
  Applies to spółka cywilna theory and to solidary tortfeasor theory.
- **Współuczestnictwo formalne (formal joinder, art. 72 § 1 pkt 2 KPC)** —
  same type of claim arising from similar factual basis.
- **Współuczestnictwo konieczne (necessary joinder, art. 72 § 2 KPC)** —
  both must be sued together. Probably NOT applicable here (solidary
  liability is several, not necessary).

Confirm the right basis. Confirm whether necessary joinder would in fact
require me to sue both for the judgment to be effective.

### 7. Zabezpieczenie roszczenia (interim measures) on filing

When the new ordinary pozew is filed naming Waldemar, can it be paired with
a motion under art. 730 KPC for *zabezpieczenie roszczenia* against
Waldemar's assets? Specifically:

- Bank account freeze on his JDG operating accounts (Biała Lista numbers)
- Mortgage entry (*hipoteka przymusowa*) on any Kraków real property
  registered in his name
- Inventory seizure at his ul. Św. Filipa 23/4 premises

Standard requires *uprawdopodobnienie roszczenia* + *interes prawny*. What
deposit (*kaucja*) does the court typically require for 155k? Is the
domain-overlap + email-thread + Wayback evidence sufficient
*uprawdopodobnienie* for the tortfeasor theory, or only for the
spółka-cywilna theory?

### 8. The EPU portal — practical mechanics

The EPU runs on a dedicated portal (e-sad.gov.pl). The login is by Profil
Zaufany, which I do not currently have. Walk through:

- Whether the original plaintiff can submit amendments by paper post to
  Sąd Rejonowy Lublin-Zachód VI Wydział Cywilny if they cannot log in to
  the portal
- Whether the portal supports adding a second defendant by amending the
  open pozew (filtered through the agent's understanding of the actual
  2026 portal UI, not pre-2020 commentary)
- Whether the portal will accept the second defendant if the second
  defendant has been served by ordinary post — service in EPU is by court
  to defendant, plaintiff does not control it
- Whether a Polish lawyer (pełnomocnik) appointed at this stage can take
  over the EPU portal account or must use his own

### 9. Sprzeciw deadline if I do nothing

If the nakaz zapłaty does eventually issue against Mateusz alone, he has
**2 weeks** to file *sprzeciw* from the date of service. Service to an
Eindhoven address will follow the EU Service Regulation timeline. If he
files sprzeciw, the case transfers to the sąd właściwy według właściwości
ogólnej (Kraków). At THAT point, can I expand the case to include Waldemar
under art. 193 § 1 KPC (przedmiotowa zmiana powództwa) — and is that the
*procedurally cheapest* moment to do so?

This is the key tactical question: **does it pay to wait for Mateusz's
sprzeciw before adding Waldemar?**

### 10. Honest bottom line

End the response with **a single explicit recommendation** in the form:

"At today's case state (2026-05-24, EPU filed 2026-04-08, no nakaz, no
sprzeciw, two months elapsed), the recommended move is __________ because
__________, and the next step in the next 14 days is __________."

If the recommendation is conditional, state the condition explicitly:
"if X is true, then path A; if Y, then path B."

## Output format

Structured markdown, headings 1–10 mirroring the questions above. Cite
articles of KPC, KC, UKSC by article and paragraph. Cite any Sąd Najwyższy
ruling that turns the answer on a recent decision (e.g., post-2020 rulings
on EPU subjective amendment). Where the answer depends on a regulation
change in the 2023/2024 KPC amendments (and there were several), say so
explicitly with the amendment date.

Browser-agent prompts where useful (specifically for: checking whether the
EPU portal currently allows the amendment in question; checking Sąd
Rejonowy Lublin-Zachód local rules; checking the current cost-of-justice
table at https://www.gov.pl/web/sprawiedliwosc) should be in fenced blocks
marked ` ```prompt-for-browser-agent ` so I can copy-paste them verbatim
into Atlas / Comet / Claude in Chrome.

## Hard constraints

- The answer must be specific to **Polish civil procedure as in force on
  2026-05-24**, not pre-2020 EPU rules and not generic "European civil
  procedure" answers.
- If the agent does not know the current state of a procedural rule, it
  must say so and surface the rule it is uncertain about, not paper over
  the gap.
- The answer must distinguish **what I can do without a lawyer** (file
  amendments via EPU portal myself once I get Profil Zaufany) from
  **what requires a Polish pełnomocnik** (court appearances, complex
  motions, zabezpieczenie roszczenia drafting).
