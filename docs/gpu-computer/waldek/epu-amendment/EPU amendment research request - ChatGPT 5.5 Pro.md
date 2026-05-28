I treated the joint-liability brief as background and used the EPU tactical prompt as the operative assignment. The fixed facts I used are: EPU case **Nc-e 552126/26**, filed **2026-04-08**, no *nakaz zapłaty* as of **2026-05-24**, Mateusz currently the sole defendant, and Waldemar proposed as a co-defendant on joint-tortfeasor / *spółka cywilna* theories.  The material background fact from the first brief is that Waldemar was allegedly the customer-facing “Waldek” on the email thread, negotiated order/delay/refund issues, and made the refund promise while Mateusz was the invoice/bank-transfer contracting party. 

## Executive answer

The tactical premise in the prompt needs correction: **under the current EPU regime, refusal to issue a payment order or a defendant’s opposition no longer transfers the case to the ordinary court; it generally causes discontinuance (*umorzenie*) of the EPU proceeding.** Current KPC art. 505³³ says that if there is no basis to issue the order, the EPU court discontinues; art. 505³⁶ says that after an effective *sprzeciw*, the EPU court discontinues to the extent the order lost force; and art. 505³⁷ §2 gives a special **three-month refiling bridge** preserving the effects of the original EPU filing for the same claim against the same defendant. ([Isap][1])

**Recommendation:** do **not** try to “amend EPU into an ordinary joint case.” That path is procedurally weak under current law, likely kills or complicates the EPU, and will not retroactively preserve the **2026-04-08** filing date against Waldemar. The better tactical move is **Path B**: keep the EPU alive against Mateusz, and file a separate ordinary action against Waldemar in **Sąd Okręgowy w Krakowie** with a simultaneous *zabezpieczenie roszczenia* motion if the Waldek email evidence is as strong as described.

---

## 1. Subjective amendment in EPU — is it even allowed?

### Practical answer

There is no clean, advantageous “amended EPU pozew adding Waldemar” route that accomplishes what you want.

A plaintiff in EPU must file pleadings **exclusively through the ICT system**; a traditional paper filing by the plaintiff is not the normal route. KPC art. 505³¹ §1 states that the plaintiff files pleadings only through the electronic system, and art. 505³² says EPU is a simplified pleading-only procedure where evidence is indicated but not attached. ([Isap][1]) The official EPU information page likewise states that plaintiffs and defendants who chose the electronic route file EPU pleadings only through the EPU ICT system; ePUAP/email are not legally effective filing channels for EPU pleadings. ([e-sad.gov.pl][2])

The theoretically relevant ordinary-procedure mechanism for adding another defendant is **KPC art. 194 §3**: if the same claim may be brought against other persons not yet in the case, the court may summon them as defendants on the plaintiff’s motion. That is *dopozwanie*, not simply “editing the pozew.” Current case law treats art. 194 §3 as discretionary, and it requires substantially the same claim and factual basis; it is used for solidary / *in solidum* liability situations, but the court is not bound to grant it. ([Isap][1])

The problem is that EPU is not designed for evidentiary evaluation of a new, contested joint-tortfeasor or implied-partnership theory. A payment order should not issue if the pleaded facts are doubtful or the claim is obviously unsuitable for order-for-payment handling; in the ordinary *postępowanie upominawcze* framework, KPC art. 499 bars issuance where the factual allegations create doubts. ([Isap][1]) Adding Waldemar on a fraud/tort or implied *spółka cywilna* theory would almost certainly make the case more fact-intensive, not less.

### What happens if you try?

Best-case procedural result: the EPU court accepts an electronic motion/pleading and either refuses to act on it in EPU or discontinues rather than issuing a joint order.

Worst-case tactical result: you lose the fastest route to an enforceable title against Mateusz, without obtaining any filing-date advantage against Waldemar.

I found no current post-2020 Supreme Court authority directly saying “an EPU plaintiff may/may not add a co-defendant by electronic amendment before *nakaz*.” The controlling answer comes from the current statutory design: EPU is electronic, simplified, evidence-light, and current failure/opposition consequences are **discontinuance**, not transfer. ([Isap][1])

---

## 2. What triggers transfer out of EPU to ordinary procedure?

### Current 2026 answer: usually not transfer — discontinuance

The prompt’s listed transfer logic is outdated for the current EPU structure.

Under current KPC:

| Event                                                                 | Current result                                                                                                                   |
| --------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| No basis to issue *nakaz zapłaty*                                     | **Discontinuance** under art. 505³³ KPC                                                                                          |
| After issuance, order cannot be served in Poland                      | Court revokes order and **discontinues**, unless plaintiff removes obstacle within a deadline up to one month, art. 505³⁴ §2 KPC |
| Defendant files effective *sprzeciw*                                  | Order loses force, and court **discontinues** as to the challenged part, art. 505³⁶ KPC                                          |
| Plaintiff refiles same claim within 3 months after EPU discontinuance | Effects of filing are preserved from the EPU filing date, but only under art. 505³⁷ §2 conditions                                |

([Isap][1])

There is a limited “transfer” provision in art. 505³⁹, but that concerns a complaint for reopening proceedings (*skarga o wznowienie postępowania*), not your normal no-order/sprzeciw scenario. ([Isap][1])

### Is there a clean plaintiff motion to transfer?

No clean statutory “wniosek o przekazanie sprawy” route appears in the current EPU provisions for your tactical purpose. The clean statutory bridge is not transfer; it is **discontinuance + refiling within three months** under art. 505³⁷ §2.

### Special warning: Mateusz’s Netherlands residence

KPC art. 505²⁸ §2 says an EPU *nakaz zapłaty* cannot be issued if service on the defendant would have to occur outside Poland. ([Isap][1]) That matters because your background facts say Mateusz’s real residence is in Eindhoven, Netherlands, although his CEIDG address is in Kraków.  A Polish lawyer should assess whether the EPU remains viable if the court knows that effective service must occur abroad. Do not paper over the foreign-residence issue in any filing.

---

## 3. Does the EPU filing date survive transfer/refiling?

### Against Mateusz: yes, conditionally, through art. 505³⁷ §2

Because current law generally discontinues rather than transfers, the key rule is KPC art. 505³⁷ §2:

If, within **three months** from EPU discontinuance, the plaintiff brings the same claim against the defendant in a non-EPU procedure, the legal effects associated with bringing the action occur from the date the EPU claim was filed. The EPU costs may also be taken into account in the later case on request. ([Isap][1])

For Mateusz, that means the **2026-04-08** EPU date should be preserved if:

1. the EPU is discontinued;
2. you file ordinary proceedings within three months of discontinuance;
3. the later claim is the same claim;
4. the later defendant is Mateusz.

### Against Waldemar: no, not retroactively to 2026-04-08

The preservation rule is framed around the same claim against the defendant from the EPU. Waldemar was not an EPU defendant on 2026-04-08. Adding him later through ordinary *dopozwanie* or a separate suit should not retroactively give you the EPU filing date against him.

This point is reinforced by Supreme Court logic on art. 194 §3 KPC. In **SN I CSK 717/18**, the Supreme Court rejected treating the original filing date against the original defendant as the interrupting act against a later-added defendant; for the added defendant, the relevant interrupting event is the motion/order adding that defendant, not the original lawsuit against someone else. ([Supreme Court][3])

### Lis pendens is also not simply “filing date”

KPC art. 192 ties several pending-litigation effects to service of the claim on the defendant, not merely to the plaintiff’s filing. ([Isap][1]) So even for Mateusz, separate concepts need to be kept apart:

| Concept                                 | Practical effect                                                                                       |
| --------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| Filing date for limitation interruption | EPU date can be preserved under art. 505³⁷ §2 if refiling conditions are met                           |
| Lis pendens                             | Generally from service of the claim, not mere filing                                                   |
| Waldemar limitation/interruption        | Starts from the separate Waldemar suit, or from a proper motion/order adding him in ordinary procedure |
| Security priority                       | Depends on the security filing/order, not on retroactive Waldemar joinder                              |

### Withdrawal is worse than discontinuance

If you withdraw the EPU claim, KPC art. 203 §2 provides that a withdrawn claim has no legal effects associated with filing. ([Standardy Prawa][4]) That is why Path C sacrifices the **2026-04-08** date more clearly than waiting for EPU discontinuance and using art. 505³⁷ §2.

---

## 4. The court fee differential

### Fee amounts for 155,000 PLN

For a 155,000 PLN monetary claim, the claim value is the principal amount; interest and costs are generally not included in the value of the dispute under KPC art. 20. ([Isap][1])

| Item                                                              |                                                                  Rule |                                                Amount |
| ----------------------------------------------------------------- | --------------------------------------------------------------------: | ----------------------------------------------------: |
| Ordinary civil claim fee                                          |                 5% of claim value for property claims over 20,000 PLN |                                         **7,750 PLN** |
| EPU fee                                                           |                                                   1/4 of ordinary fee | **1,937.50 PLN**, practically rounded under fee rules |
| Difference/credit if ordinary refiling follows EPU discontinuance | EPU fee credited under UKSC art. 19(2) when KPC art. 505³⁷ §2 applies |                        about **5,812 PLN** additional |

UKSC art. 13 sets the 5% proportional fee for property claims over 20,000 PLN, and UKSC art. 19(2) provides that EPU takes one-quarter of the fee and credits it when art. 505³⁷ §2 KPC refiling occurs. ([Isap][5])

### Does the fee scale by number of defendants?

No, not if you are asserting **one 155,000 PLN claim** for solidary / joint liability. The fee is tied to the value of the claim, not multiplied by the number of defendants. If you file separate suits, however, each suit has its own fee.

### What happens on “transfer”?

Under current law, the expected event is not transfer with a “fee differential.” It is discontinuance, then refiling. If refiling qualifies under art. 505³⁷ §2, the EPU fee should be credited toward the ordinary fee. ([Isap][1])

### What if the ordinary fee is unpaid?

If a pro se ordinary filing is not properly paid, KPC art. 130 generally allows the court to call for correction/payment within one week, with special longer timing where a foreign-resident party lacks a Polish representative. Attorney-filed underpaid pleadings can be returned more strictly, though prompt payment after return may preserve the filing date in certain situations. Electronic pleadings requiring a fee may be ineffective if filed without payment. ([Isap][1])

### Withdrawal refund

If you withdraw EPU before the claim copy is sent/served, UKSC art. 79 may allow a refund, depending on procedural status; the statute also contains partial-refund rules and minimum-fee deductions. ([Isap][5]) But refund should not drive strategy: withdrawal can destroy the legal effects of the original filing under KPC art. 203 §2. ([Standardy Prawa][4])

---

## 5. Alternative — keep EPU, file separately

### Path A — try to amend EPU adding Waldemar

| Factor               | Assessment                                                                                                                                                                     |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Procedural viability | Weak. At most, this resembles an electronic art. 194 §3 *dopozwanie* motion, not a normal EPU amendment.                                                                       |
| Expected EPU result  | Refusal/discontinuance is more likely than a joint EPU order, because Waldemar’s liability is fact-heavy.                                                                      |
| Filing-date effect   | Preserves 2026-04-08 only for Mateusz if later art. 505³⁷ §2 refiling conditions are met; not for Waldemar.                                                                    |
| Court fees           | No clean “differential on transfer.” If discontinued and refiled against Mateusz within three months, EPU fee credited; ordinary fee total remains 7,750 PLN for a 155k claim. |
| Timeline             | Likely delays the clean Mateusz track and still forces ordinary litigation.                                                                                                    |
| Litigation risk      | Highest procedural-risk-to-benefit ratio.                                                                                                                                      |

**Verdict:** not recommended.

### Path B — keep EPU against Mateusz, file separate ordinary suit against Waldemar

| Factor               | Assessment                                                                                                                                                                                                                                                                                                                  |
| -------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Procedural viability | Strongest. It avoids contaminating the EPU with a complex new theory.                                                                                                                                                                                                                                                       |
| Court                | **Sąd Okręgowy w Krakowie**, assuming Waldemar’s residence/business establishment is Kraków and the claim is 155,000 PLN. KPC art. 17(4) places property claims over 100,000 PLN in district court (*sąd okręgowy*) except EPU; venue follows residence, business establishment, contract, or tort venue rules. ([Isap][1]) |
| Fees                 | 7,750 PLN for the Waldemar ordinary suit. EPU fee against Mateusz remains sunk/active unless that case fails and is refiled.                                                                                                                                                                                                |
| Filing-date effect   | Mateusz keeps EPU timeline; Waldemar gets new filing date from the ordinary suit.                                                                                                                                                                                                                                           |
| Timeline             | EPU may still produce a fast title against Mateusz if service/order works. Waldemar suit likely 18–36+ months to first-instance judgment, but security can be sought at the start.                                                                                                                                          |
| Strategic upside     | Best chance to preserve the fast route against Mateusz while immediately pressuring Waldemar’s Polish asset base.                                                                                                                                                                                                           |
| Downside             | Two proceedings and potentially two sets of lawyer/court activity.                                                                                                                                                                                                                                                          |

**Verdict:** recommended, assuming the Waldek email evidence is strong.

### Path C — withdraw EPU, refile one ordinary suit naming both

| Factor               | Assessment                                                                                            |
| -------------------- | ----------------------------------------------------------------------------------------------------- |
| Procedural viability | Clean in ordinary procedure.                                                                          |
| Fees                 | One ordinary fee: 7,750 PLN, less any refund if EPU withdrawal qualifies; do not rely on full refund. |
| Filing-date effect   | Bad. Withdrawal risks losing the 2026-04-08 EPU effects.                                              |
| Timeline             | One coherent ordinary case, but slower than a successful EPU order against Mateusz.                   |
| Strategic upside     | Single evidentiary record and one judgment against both if you win.                                   |
| Downside             | Sacrifices the only fast-title path and may unnecessarily abandon EPU priority.                       |

**Verdict:** second-best only if a Polish litigator concludes the Mateusz EPU is doomed because lawful service must occur in the Netherlands and the case will be discontinued anyway.

---

## 6. Joinder rules — art. 195–198 KPC

### Correct joinder basis

For Mateusz + Waldemar, the right conceptual basis is **KPC art. 72 §1 pkt 1 — material co-participation (*współuczestnictwo materialne*)**, because the claim would be that the same 155,000 PLN debt/damage is owed solidarily or *in solidum* by both persons from the same transaction or same factual complex. KPC art. 72 also recognizes formal co-participation where claims are of the same type and based on similar facts; necessary co-participation applies only where the legal relationship or statute requires one judgment concerning all parties together. ([Isap][1])

### Not necessary joinder

This is not **necessary joinder**. Solidary debtors generally need not all be sued together. You can sue Mateusz alone, Waldemar alone, or both. A judgment against one does not automatically give you enforcement title against the other.

### If adding Waldemar inside an already ordinary case

The proper mechanism would generally be **KPC art. 194 §3**, not art. 193. Art. 193 governs objective amendment of the claim; adding a new defendant is party amendment / *dopozwanie*. KPC art. 194 §3 allows the court, on plaintiff’s motion, to summon other persons as defendants where the same claim can also be brought against them. ([Isap][1])

Case law emphasizes that art. 194 §3 is discretionary and requires the same demand and substantially the same factual basis; it is suited to solidary and *in solidum* liability, but the court may refuse and leave the plaintiff to file a separate action. ([Saos][6])

### Filing-date warning

For Waldemar, art. 194 §3 does not give the original Mateusz filing date. The Supreme Court in **I CSK 717/18** treated interruption against an added defendant as arising from the later *dopozwanie* act, not the original claim against another defendant. ([Supreme Court][3])

---

## 7. *Zabezpieczenie roszczenia* on filing

### Can you request security against Waldemar?

Yes. In an ordinary civil action against Waldemar, you can pair the *pozew* with a motion under KPC art. 730 and 730¹. The standard is:

1. **uprawdopodobnienie roszczenia** — making the claim plausible, not fully proven;
2. **interes prawny** — showing that lack of security would prevent or seriously hinder enforcement or frustrate the purpose of the proceeding. ([Isap][1])

For monetary claims, KPC art. 747 allows security measures including seizure of movables, wages, bank accounts, other receivables and property rights, compulsory mortgage, and restrictions on disposal of real estate. ([Isap][1])

### Which measures fit your facts?

| Measure                             | Fit                                     | Notes                                                                                                        |
| ----------------------------------- | --------------------------------------- | ------------------------------------------------------------------------------------------------------------ |
| Bank account attachment             | Strongest practical first ask           | Needs account numbers if available, e.g. Biała Lista, but court/bailiff mechanisms may also locate accounts. |
| Compulsory mortgage                 | Strong if real estate is found          | Requires identifying property/land-mortgage register.                                                        |
| Inventory/movable seizure           | Possible but more intrusive             | Court may demand stronger plausibility and proportionality.                                                  |
| Receivables from business customers | Possible if customers/receivables known | Often hard without discovery.                                                                                |
| General “freeze everything” motion  | Risky                                   | Must be specific and proportionate.                                                                          |

### Is your evidence enough?

The domain overlap alone is probably not enough. The stronger security package is:

* Waldek email thread with full headers;
* messages where Waldek negotiated specs, deadlines, delay explanations, and refund;
* the explicit refund promise;
* invoice and payment proof to Mateusz;
* proof of non-delivery and non-refund;
* Wayback/live website evidence showing Waldemar/Waldek publicly inside the GPUcomputer operation;
* CEIDG data showing Waldemar’s computer-production business and Kraków base.

On the held-fixed facts, the **joint-tortfeasor / art. 422 + art. 441 KC** theory is better for security than implied *spółka cywilna*. The *spółka cywilna* theory helps explain the operational jointness, but it asks the court to infer a partnership from conduct despite separate JDGs. The tort/security theory can focus on Waldemar’s own conduct: he allegedly negotiated, made delivery/refund representations, and promised refund.

### Deposit / *kaucja*

There is no automatic deposit for a 155,000 PLN security motion. KPC art. 739 allows the court to condition execution of security on a deposit to protect the defendant against damage caused by execution of security, but this is discretionary. ([Isap][1]) The defendant can also seek to lift security by depositing the secured sum into the Ministry of Finance deposit account under KPC art. 742. ([Isap][1])

Separate issue: if the plaintiff lacks residence/habitual stay/seat in Poland or the EU, the defendant may request security for litigation costs under KPC art. 1119, subject to exceptions. ([Isap][1]) If you are EU-resident, this is much less likely to matter; if you are outside the EU, raise it with counsel.

---

## 8. EPU portal — practical mechanics

### Paper post / ePUAP / email

For the plaintiff, no: ordinary paper post, ePUAP, and email are not the proper channels for EPU pleadings. Current KPC art. 505³¹ §1 requires plaintiff filings through the ICT system, and the official EPU information page says ePUAP/email pleadings are not legally effective in EPU. ([Isap][1])

### Login

The EPU portal supports login through login.gov.pl / electronic identity mechanisms and qualified signature routes. ([e-sad.gov.pl][2]) If you do not have Profil Zaufany or another usable login method, the practical solution is appointing a Polish lawyer who can file through their own professional access.

### Can the portal add a second defendant?

Public official materials confirm the electronic filing channel, but not enough to verify the current logged-in UI for adding a defendant to an already filed case. The safest phrasing is: **the portal may allow a free-text procedural pleading, but that is not the same as a structured amended pozew adding “Pozwany 2” with clean EPU consequences.** This should be checked in the live logged-in case view before any filing.

### Can a lawyer take over the EPU?

A Polish lawyer should not need to “take over” your login. They would normally act as *pełnomocnik* using their own professional account/access and file a power of attorney or state the authority as permitted by EPU rules. KPC art. 505³¹ contains rules on professional representatives and power-of-attorney handling in EPU. ([Isap][1]) Exact portal mechanics should be confirmed in the live system.

### Browser-agent prompt: EPU UI check

```prompt-for-browser-agent
Goal: Check whether the current e-sad.gov.pl EPU portal UI allows adding a second defendant to an already filed, pending EPU case before nakaz zapłaty.

URL: https://www.e-sad.gov.pl/

Prerequisites:
- Use only a real account authorized to view case Nc-e 552126/26.
- Do not file, sign, pay for, or submit anything.
- Do not contact the court or defendants.

Steps:
1. Log in through “Zaloguj się przez Tożsamość” / login.gov.pl or the account’s normal EPU login method.
2. Open “Moje sprawy” / “Sprawy powoda” / “Akta sprawy” for Nc-e 552126/26.
3. Look for available actions named:
   - “Złóż pismo” = file pleading
   - “Pismo procesowe” = procedural pleading
   - “Inne pismo” = other pleading
   - “Modyfikacja pozwu” = claim modification
   - “Zmiana pozwu” = claim amendment
   - “Dodaj pozwanego” = add defendant
   - “Cofnięcie pozwu” = withdrawal of claim
   - “Wniosek” = motion
4. Open, but do not submit, any draft form that might change the parties.
5. Record exact Polish field labels, especially whether there is any structured section:
   - “Dane pozwanego” = defendant details
   - “Dodaj pozwanego” = add defendant
   - “Pozwany 2” = defendant 2
   - “Wartość przedmiotu sporu” = value of dispute
   - “Opłata” = fee
6. Check whether the form requests a fee before submission.
7. Exit without clicking “Wyślij”, “Podpisz”, “Opłać”, “Zatwierdź”, or equivalent.

Return:
- Screenshots or text notes of the available actions.
- Whether the UI permits structured addition of a second defendant.
- If only free-text “inne pismo” exists, record the title field and attachment limits.
- Any warning text about EPU amendments, party changes, or fees.
```

### Browser-agent prompt: EPU FAQ/local rules check

```prompt-for-browser-agent
Goal: Verify current EPU filing-channel rules and any official FAQ guidance on amendments, dopozwanie, or party changes.

URLs:
- https://www.e-sad.gov.pl/
- https://www.lublin-zachod.sr.gov.pl/vi-wydzial-cywilny-e-sad,m,mg,193,228,333

Steps:
1. On e-sad.gov.pl, open sections such as:
   - “Informacje o portalu”
   - “EPU - Najczęściej zadawane pytania”
   - “EPU - Informacja dla powodów”
   - “Instrukcja użytkownika FrontOffice”
2. Search within pages/PDFs for:
   - “zmiana pozwu” = amendment of claim
   - “modyfikacja pozwu” = claim modification
   - “dopozwanie” = adding/summoning another defendant
   - “dodaj pozwanego” = add defendant
   - “art. 194” = party summons provision
   - “cofnięcie pozwu” = withdrawal
   - “pismo procesowe” = procedural pleading
   - “pełnomocnik” = attorney/representative
3. Confirm the rules for paper, ePUAP, and email filings.
4. Quote exact Polish text and provide English translations.
5. Do not log into any court account unless specifically authorized.

Return:
- Source URLs.
- Section names.
- Exact Polish labels/text.
- English translations.
- Any explicit statement about whether a pending EPU claim can be amended to add a defendant.
```

### Browser-agent prompt: fee verification

```prompt-for-browser-agent
Goal: Verify current court-fee amounts for a 155,000 PLN monetary claim in EPU and ordinary civil procedure.

URLs:
- https://www.gov.pl/web/sprawiedliwosc
- https://isap.sejm.gov.pl/ 
Search phrase: “Ustawa o kosztach sądowych w sprawach cywilnych tekst jednolity 2026”

Steps:
1. Find the current text/table for “opłata stosunkowa” in property claims over 20,000 PLN.
2. Find the article setting 5% fee for ordinary property claims.
3. Find the article setting one-quarter fee for EPU.
4. Find the provision crediting the EPU fee when refiling under KPC art. 505^37 §2.
5. Find the refund rule for withdrawal before service/dispatch.
6. Calculate for WPS 155,000 PLN:
   - ordinary 5% fee
   - EPU one-quarter fee
   - credited/additional amount if ordinary refiling follows EPU discontinuance

Return:
- Article numbers.
- Polish text excerpts.
- English translations.
- Calculations.
- Source URLs.
```

---

## 9. Sprzeciw deadline if you do nothing

### Deadline

In ordinary order-for-payment proceedings, the payment order instructs the defendant to satisfy the claim or challenge it within the statutory period; for service in the EU, the ordinary *upominawcze* framework uses a one-month deadline. ([Isap][1]) But EPU has its own critical limitation: an EPU order cannot issue if service would have to occur outside Poland. ([Isap][1])

For a Polish-address EPU service scenario, the usual *sprzeciw* period is commonly two weeks from service. If the court treats Mateusz as requiring service in the Netherlands, the more fundamental issue is not the exact opposition deadline; it is whether EPU can issue/stand at all.

### Does it pay to wait for Mateusz’s sprzeciw before adding Waldemar?

No, not under current law.

The old tactical idea was: “wait for *sprzeciw*, the case transfers to ordinary court, then add Waldemar there.” Current KPC instead says *sprzeciw* causes EPU discontinuance, with a three-month refiling bridge. ([Isap][1]) There is therefore no automatic Kraków ordinary case created by Mateusz’s opposition into which you can cheaply add Waldemar.

The better waiting strategy is narrower:

* **Do not disturb the EPU now.**
* **Monitor it.**
* If a *nakaz* issues and Mateusz does not oppose, enforce quickly.
* If EPU is discontinued, file against Mateusz in ordinary procedure within three months to preserve 2026-04-08 effects under art. 505³⁷ §2.
* Separately, start the Waldemar ordinary claim now if the email evidence supports it.

---

## 10. Honest bottom line

At today’s case state (**2026-05-24, EPU filed 2026-04-08, no nakaz, no sprzeciw, two months elapsed**), the recommended move is **Path B: keep the Mateusz EPU untouched and file a separate ordinary claim against Waldemar in Sąd Okręgowy w Krakowie with a simultaneous security motion**, because current EPU law does not transfer the case to ordinary procedure on no-basis or *sprzeciw*, an EPU “amendment” will not preserve the **2026-04-08** filing date against Waldemar, and trying to add Waldemar inside EPU risks sacrificing the fastest possible title against Mateusz. The next step in the next 14 days is to have a Kraków litigator convert the Waldek email thread, headers, invoice/payment proof, non-delivery/refund record, Wayback/live-site evidence, and CEIDG data into a Polish ordinary *pozew* plus KPC art. 730/747 *zabezpieczenie roszczenia* motion.

### Decision matrix

| Scenario                            | Recommended action                                                                                                                                         | Reason                                                                                                                                             |
| ----------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| Mateusz cooperative                 | Use EPU/settlement pressure first; do not abandon Waldemar evidence, but consider delaying service on Waldemar if settlement is real and secured.          | Fast voluntary recovery beats complex joint-liability litigation. Settlement should be documented, payable on short dates, and preferably secured. |
| Mateusz silent                      | Keep EPU running and file Waldemar ordinary suit now.                                                                                                      | Silence plus asset-light Mateusz makes Waldemar’s Polish asset base strategically important.                                                       |
| Mateusz contests / EPU discontinued | Refile against Mateusz within three months under art. 505³⁷ §2 and ask counsel whether to coordinate/connect with the Waldemar case if both are in Kraków. | This preserves EPU-date effects against Mateusz while letting Waldemar proceed on his own filing date.                                             |

### One-paragraph litigator-style synthesis

A Polish *windykacja* litigator would likely say: **do not try to solve Waldemar through the pending EPU.** The Waldemar theory is potentially valuable because he allegedly negotiated, delayed, and promised refund from the operational GPUcomputer address, but it is fact-heavy and belongs in ordinary proceedings with evidence and a security motion. The Mateusz EPU should be preserved as a low-cost chance at a fast enforceable title, while Waldemar should be pursued separately if the email archive really shows personal involvement and refund representations. If later the Mateusz EPU is discontinued, use the three-month art. 505³⁷ §2 bridge for Mateusz; do not rely on an EPU amendment to create retroactive priority against Waldemar.

[1]: https://isap.sejm.gov.pl/isap.nsf/download.xsp/WDU19640430296/U/D19640296Lj.pdf "https://isap.sejm.gov.pl/isap.nsf/download.xsp/WDU19640430296/U/D19640296Lj.pdf"
[2]: https://www.e-sad.gov.pl/ "https://www.e-sad.gov.pl/"
[3]: https://www.sn.pl/sites/orzecznictwo/orzeczenia3/i%20csk%20717-18-1.pdf "https://www.sn.pl/sites/orzecznictwo/orzeczenia3/i%20csk%20717-18-1.pdf"
[4]: https://standardyprawa.pl/akt/76/art/12976 "https://standardyprawa.pl/akt/76/art/12976"
[5]: https://isap.sejm.gov.pl/isap.nsf/download.xsp/WDU20051671398/U/D20051398Lj.pdf "https://isap.sejm.gov.pl/isap.nsf/download.xsp/WDU20051671398/U/D20051398Lj.pdf"
[6]: https://www.saos.org.pl/judgments/380301 "https://www.saos.org.pl/judgments/380301"
