## Criminal analysis: how Waldek can fit art. 286 § 1 KK despite Mateusz’s invoice/account

The theory is not “Waldek is liable because he is related to Mateusz” or “because he used an email address.” The theory is: **Waldek personally controlled the communications that induced or maintained the transaction, presented facts about delivery/refund/suppliers, and may have used Mateusz’s JDG as the formal payment shell.** If that is proved, the invoice and bank account being Mateusz’s do **not** block criminal liability.

Art. 286 § 1 KK covers causing another person to make an unfavourable property disposition by deception, exploitation of error, or inability to understand the act, for the purpose of obtaining a financial benefit. The benefit need not be for the offender personally; KK art. 115 § 4 defines financial/personal benefit as a benefit for oneself **or for another person**. So money landing in Mateusz’s account does not exclude Waldek if Waldek caused the payment by deception. ([Isap][1])

One qualification note: **155,000 PLN is below the 200,000 PLN threshold for “mienie znacznej wartości,”** so on this transaction alone the base qualification is art. 286 § 1 KK, not aggravated art. 294 § 1 KK, unless the prosecution aggregates other transactions/victims or finds a larger covered scheme. ([Isap][1])

### 1. Art. 286 § 1 KK: the fraud element

For fraud, the hard issue is usually not non-delivery itself, but **intent and deception at the time of inducing the payment**. Supreme Court case law treats fraud as an intentional, directional offence: the perpetrator must intentionally and purposefully cover not only the deception but also causing the unfavourable disposition of property. ([Supreme Court][2]) Courts also distinguish fraud from mere contractual non-performance: failure to pay or deliver is not automatically fraud; intent is inferred from the full circumstances, including the real possibility of fulfilling promises, finances, prior obligations, and the realism of assurances. ([Saos][3])

Applied to Waldek:

| Element                             | How Waldek fits on your facts                                                                                                                                                                                                           | Strength / caveat                                                                                                                                                                                                                                        |
| ----------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Deception / wprowadzenie w błąd** | If Waldek wrote the commercial assurances, delivery explanations, customs/supplier statements, or availability statements, he is not merely a background helper; he is the person who communicated the allegedly false factual picture. | Strongest if his messages preceded payment or directly caused you to wait/pay/accept the deal. Post-payment emails are still evidence of control and intent, but weaker for proving the original taking unless tied back to pre-payment representations. |
| **Unfavourable disposition**        | Your 155,000 PLN transfer for an undelivered workstation is the disposition.                                                                                                                                                            | Clear as to loss; the issue is causation and intent.                                                                                                                                                                                                     |
| **Causation**                       | Prosecutor must connect Waldek’s representations to your decision to pay or continue the transaction.                                                                                                                                   | Preserve the full timeline: first contact, offer, proforma, payment, promised delivery, refund promises.                                                                                                                                                 |
| **Purpose of financial benefit**    | Benefit could be to Mateusz’s JDG, to Waldek, to both, or to another person.                                                                                                                                                            | Art. 115 § 4 KK avoids the “but the account was Mateusz’s” defence.                                                                                                                                                                                      |
| **Intent at transaction stage**     | Contradictory explanations — “customs cleared” versus “Hong Kong supplier bankrupt / paid parts never arrived” — can support inference that at least one factual story was false.                                                       | Prosecutor must test whether the statements were knowingly false, not merely mistaken or based on supplier chaos.                                                                                                                                        |

The **root mailbox point is important**. If Waldek controlled both `waldek@gpucomputer.pl` and `gpucomputer@gpucomputer.pl`, then the deception was not necessarily “Mateusz’s firm speaking through an unknown employee.” It can be argued that **Waldek was the operational voice of GPUcomputer**, including the mailbox that an ordinary buyer would treat as the seller’s official address. That supports charging him as the person who performed the deception, not merely as someone adjacent to the seller.

### 2. Art. 18 § 1 KK: co-perpetration / directing perpetration

Art. 18 § 1 KK covers not only the person who commits the act alone, but also the person who acts **jointly and in agreement** with another, and the person who directs another’s execution of the offence or orders it by exploiting dependence. ([Isap][1])

Polish Supreme Court case law allows co-perpetration even where one person does not personally perform every statutory “verb” of the offence, but his role must be a necessary or very important condition of the other person’s execution under the agreement. Passive knowledge or acceptance is not enough. ([Supreme Court][4]) The Supreme Court has also accepted that a person can act jointly and in agreement even without personally carrying out the final executive act, where his conduct ensures the execution of the agreed criminal attack. ([Supreme Court][5])

For Waldek, the **co-perpetration theory** would be:

Mateusz supplies the formal JDG, proforma invoice, NIP, and bank account; Waldek supplies the operational business identity, customer dealings, technical explanations, delivery/refund promises, and possibly the false factual narrative. If both roles were agreed, even tacitly, each can be responsible for the whole art. 286 § 1 fraud.

Facts supporting “panowanie nad czynem” / practical control:

* **Control of the customer-facing channel:** `waldek@` plus apparent control of `gpucomputer@`.
* **Control of the company narrative:** Waldek gave the customs/supplier/refund explanations.
* **Control of refund communications:** he personally promised or repeated refund assurances.
* **Operational reality:** Mateusz living and working full-time in the Netherlands makes it plausible that Waldek was the de facto operator in Poland.
* **Business identity overlap:** 3dkrakow co-branding on gpucomputer.pl since 2016 supports long-term operational integration, not a one-off outsider role.
* **Possible division of roles:** Mateusz as formal seller; Waldek as the person who conducted the transaction.

The weak point is **proof of agreement with Mateusz**. Co-perpetration requires at least a tacit understanding. The current facts support suspicion, but the prosecutor would still need evidence such as bank flows, access permissions, internal communications, who issued/approved the proforma, who controlled the domain/mail hosting, and whether Mateusz knowingly allowed Waldek to run sales under his JDG.

**Sprawstwo kierownicze** is possible but harder. It would require showing that Waldek directed Mateusz’s acts — for example, told him to issue the proforma, receive funds, not refund, or maintain the business shell. Your facts presently show Waldek as de facto operator; they do not yet prove that he directed Mateusz. So the stronger primary theory is **co-perpetration or direct perpetration through the deception**, with directing perpetration as a theory to investigate.

### 3. Art. 18 § 3 and § 2 KK as fallbacks

**Pomocnictwo — art. 18 § 3 KK.** If the prosecutor cannot prove Waldek was a co-perpetrator, he can still be treated as a helper if he intentionally facilitated Mateusz’s fraud by providing the customer channel, technical story, false supplier/customs information, delay/refund narrative, website identity, or operational infrastructure. Art. 18 § 3 requires intent that another person commit the offence and conduct facilitating it; art. 19 § 1 provides punishment within the range for the principal offence, though art. 19 § 2 allows extraordinary mitigation for assistance. ([Isap][1])

The main caveat: **after-the-fact concealment alone is not the same as assistance in committing the original fraud** unless it was part of the plan, promised beforehand, or caused a further property disposition. If Waldek’s only provable role were post-payment delay emails, that is weaker. But if he controlled the deal before payment or the delay emails were part of an agreed method to keep the money and avoid refund, the assistance theory becomes stronger.

**Podżeganie — art. 18 § 2 KK.** This is weaker on your current facts. It would require proof that Waldek induced Mateusz to commit the fraud — for example, “use your JDG and account; I will handle the customer.” You do not yet have direct evidence of inducement. It should be pleaded only as an investigative fallback.

### 4. Art. 20 and art. 21 § 2 KK

Art. 20 KK says each participant is liable within the limits of his own intent/negligence, independently of the others. Art. 21 § 1–2 KK deals with personal circumstances: generally they affect only the person concerned, but if a personal circumstance is an element of the offence and another participant knew of it, it can affect that participant too. ([Isap][1])

For basic art. 286 § 1 KK, this is mostly not decisive. Fraud is not an offence requiring the perpetrator to be the JDG owner, VAT taxpayer, bank-account holder, or invoice issuer. Therefore, Waldek does **not** need to be VAT-registered, the formal seller, or the account holder to be liable. What matters is whether he intentionally participated in causing the deceptive property disposition.

The fact that Waldek is not VAT-registered is useful mainly as background: it may support the theory that he operated behind Mateusz’s formal business identity, but it does not itself prove fraud.

---

## Evidence needed to charge Waldek

To present charges, the procedural threshold is that the data available when the investigation starts or gathered during it **sufficiently justify suspicion that a specific person committed the act**. KPK art. 313 § 1 then requires a decision presenting charges, identification of the suspect, the act, and legal qualification. ([Isap][6])

| What prosecutor must prove                                    | Your current evidence                                                                                                | What should be secured / requested                                                                                                                                                                   |
| ------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Waldek authored or controlled the relevant communications** | `waldek@` correspondence; near-identical refund promise from `gpucomputer@` at 13:10 and `waldek@` at 13:11.         | Full `.eml` files with headers; server logs; SMTP/IMAP login IPs; hosting records; domain admin records; device seizures; who had passwords to both mailboxes.                                       |
| **Waldek used the official GPUcomputer identity**             | Root mailbox control; GPUcomputer domain; 3dkrakow co-branding on gpucomputer.pl.                                    | Hosting panel logs; website CMS/admin logs; historic and current domain records; invoices for hosting/domain; archive captures with dates.                                                           |
| **Waldek made statements material to your payment**           | His personal dealings and explanations.                                                                              | All pre-payment emails/chats/calls; quote/config discussions; statements about stock, supplier, customs, delivery time, refund policy. This is the critical group.                                   |
| **The statements were false or misleading**                   | Contradictory stories: customs cleared on 24.02.2026 versus supplier bankruptcy / parts never arrived on 13.05.2026. | Customs/import documents; shipping tracking; supplier invoices; bank transfers to supplier; proof of Hong Kong supplier bankruptcy; purchase orders; correspondence with supplier.                   |
| **Intent existed at the time of obtaining the money**         | Non-delivery, no refund, contradictory explanations, de facto operation, Mateusz abroad.                             | Bank-account analysis; whether funds were spent on parts; whether there were other victims; prior complaints; debts/enforcement; inventory; supplier reality; cash withdrawals/transfers to Waldek.  |
| **Agreement or role division with Mateusz**                   | Mateusz abroad; Waldek operating the transaction; same business identity; probable family link.                      | Communications between Mateusz and Waldek; who issued proforma 2/01-2026; who accessed bank account; transfers between them; who handled refunds; whether Mateusz authorized Waldek to use the firm. |
| **Financial benefit**                                         | Payment to Mateusz’s JDG; possible operational benefit to Waldek not yet traced.                                     | Bank statements; transfers from Mateusz to Waldek; cash withdrawals; purchases for 3dkrakow/Waldek; tax/accounting records.                                                                          |
| **Damage**                                                    | 155,000 PLN paid; workstation undelivered; refund promised but not made.                                             | Transfer confirmation; proforma; final demand; proof no delivery/refund; correspondence after missed delivery.                                                                                       |

The most important gap is whether Waldek made **pre-payment** representations. If he did, the case against him becomes materially stronger. If all provable Waldek communications are after payment, they still show control, concealment, and possible consciousness of guilt, but the prosecutor will need more evidence tying him to the original inducement.

---

## Civil bridge: how criminal findings turn into recovery against Waldek

### 1. Art. 422 KC + art. 441 § 1 KC: tort route bypassing contract privity

Your lawyer’s objection is correct for a **pure contract claim**: the sale/refund claim is against Mateusz as the formal seller. But tort liability is different.

Art. 415 KC creates general liability for culpably causing damage. Art. 422 KC extends liability beyond the direct tortfeasor to a person who induced the damage, helped cause it, or knowingly benefited from it. Art. 441 § 1 KC provides that where several persons are liable for damage caused by a tort, their liability is solidary. ([Isap][7])

So if Waldek is found to have co-perpetrated or intentionally assisted the fraud, he can become a **solidary tort debtor** for the 155,000 PLN, even though he was not your contractual counterparty. The legal move is:

**contract claim against Mateusz** → not enough for Waldek
**fraud/tort finding against Waldek** → art. 415/422 KC liability
**same indivisible loss caused by several participants** → art. 441 § 1 KC solidarity

For “knowingly benefited,” the Supreme Court requires actual knowledge: the person must know he is benefiting from another’s tort. Suspicion or negligence is not enough. ([Supreme Court][8]) This is why tracing money to Waldek is important but not sufficient by itself; the evidence should also show he knew the money came from the wrongful transaction.

### 2. Art. 46 KK: restitution directly in the criminal judgment

Art. 46 § 1 KK allows the criminal court, upon conviction, to order the offender to repair the damage in whole or in part; on the victim’s motion, the court orders it while applying civil-law rules. If determining the duty is significantly difficult, the court may instead award a nawiązka up to 200,000 PLN. ([Isap][1]) Under KPK art. 49a, the victim may file the art. 46 motion up to the close of the main trial. ([Isap][6])

If Waldek is convicted as co-perpetrator or helper in the fraud that caused your 155,000 PLN loss, the criminal court can order **Waldek personally** to repair the damage. It can also order restitution solidarily with Mateusz. The Supreme Court has expressly held that art. 46 § 1 KK may be imposed as a solidary obligation of co-perpetrators to repair the damage. ([Supreme Court][9])

Practical point: include the art. 46 request already in the zawiadomienie, and later repeat it formally if the case reaches indictment/trial.

### 3. Art. 11 KPC: prejudicial effect of a criminal conviction

Art. 11 KPC provides that findings of a final criminal conviction as to commission of the offence bind the civil court. It also says that a person who was not accused may still rely in civil proceedings on circumstances excluding or limiting civil liability. ([Isap][10])

This is the core bridge:

* If **Waldek is convicted**, a later civil court cannot simply re-decide that he did not commit the offence described in the conviction.
* If the conviction’s operative part states that Waldek, acting with Mateusz, caused your 155,000 PLN adverse disposition, that becomes powerful in civil court.
* If **only Mateusz is convicted**, and Waldek was not accused, art. 11 KPC does not bind Waldek in the same way. He can still argue in civil court that he did not participate, did not cause damage, lacked intent, or did not benefit.

Supreme Court case law treats the binding effect as covering the offence’s elements and circumstances stated in the operative part of the criminal judgment, including in fraud cases the extent of the unfavourable property disposition where it is part of the offence’s factual description. ([Supreme Court][11])

This is why naming Waldek early matters: it increases the chance that any later criminal judgment addresses his role directly, rather than leaving you with only evidentiary material against Mateusz.

---

## Civil theories against Waldek without waiting for conviction

These are possible, but their strength depends heavily on pre-payment evidence and money tracing.

| Theory                                             |                                                                  Strength now | What makes it stronger                                                                                                           | Main weakness                                                                                                                                                                         |
| -------------------------------------------------- | ----------------------------------------------------------------------------: | -------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Direct tort/deceit — art. 415 KC**               | Medium if Waldek made pre-payment false statements; weak if only post-payment | Emails showing he induced the payment with false availability/supplier/delivery claims                                           | Court may view it as a failed contract unless intentional deception is proved.                                                                                                        |
| **Art. 422 KC helper/inducer**                     |                                                                Medium-to-weak | Proof he intentionally facilitated Mateusz’s taking: controlled domain/mail, gave false info, handled customer to secure payment | Mere employee/agent communication is not enough; assistance must relate to causing the damage.                                                                                        |
| **Art. 422 KC knowing beneficiary**                |                               Weak now; potentially strong after bank tracing | Transfers from Mateusz/JDG to Waldek; spending the 155k for Waldek/3dkrakow; proof he knew the source                            | Actual knowledge is required, not just family/business proximity.                                                                                                                     |
| **Unjust enrichment — art. 405/410 KC**            |                                      Weak unless money/benefit reached Waldek | Bank records showing Waldek received proceeds or a direct economic benefit without basis                                         | You paid Mateusz’s JDG, so enrichment is initially Mateusz’s unless traced onward. ([Isap][7])                                                                                        |
| **Firmanctwo / using another’s business identity** |                  Useful as evidentiary narrative; weak as private civil claim | Proof Waldek ran the real business behind Mateusz’s name/NIP                                                                     | Statutory firmanctwo is primarily a tax-liability concept: Ordynacja podatkowa art. 113 concerns solidary liability for tax arrears, not a buyer’s private refund claim. ([Isap][12]) |
| **“De facto operator” / działanie faktyczne**      |                                                   Evidentiary, not standalone | Helps prove tort, co-perpetration, or knowing benefit                                                                            | Being the practical operator does not automatically create personal civil liability without tort/enrichment proof.                                                                    |

The cleanest civil route without conviction is **art. 415 KC direct deceit**, but only if you can show Waldek personally made false statements before or at the point of payment. Without that, the stronger strategy is to use the criminal investigation to obtain evidence unavailable to you privately: bank records, server logs, supplier records, customs documents, and internal communications.

---

## Should the zawiadomienie name Waldek from the outset?

Yes. Name him from the outset, but do it in a disciplined way: not as a conclusory accusation, but as a person whose conduct gives rise to a justified suspicion of co-perpetration or, alternatively, assistance.

KPK art. 303 frames the opening of an investigation around a suspected offence and legal qualification, not only around the person named by the victim; the prosecutor can investigate the act and identify participants. ([Isap][6]) Still, if you do not name Waldek, the case may be treated too narrowly as a failed contract with Mateusz’s JDG, and volatile electronic evidence may not be secured in time.

Recommended formulation:

> Zawiadamiam o podejrzeniu popełnienia przestępstwa z art. 286 § 1 k.k. na moją szkodę przez Mateusza Szklarskiego oraz osoby z nim współdziałające, w szczególności Waldemara Łopatę, który według posiadanych przeze mnie dowodów faktycznie prowadził znaczną część kontaktów handlowych, posługiwał się adresem [waldek@gpucomputer.pl](mailto:waldek@gpucomputer.pl), miał dostęp do skrzynki [gpucomputer@gpucomputer.pl](mailto:gpucomputer@gpucomputer.pl), składał obietnice zwrotu środków oraz przedstawiał sprzeczne wyjaśnienia dotyczące rzekomej odprawy celnej i dostawcy z Hongkongu. Wnoszę o zbadanie jego roli jako współsprawcy z art. 18 § 1 k.k., ewentualnie pomocnika z art. 18 § 3 k.k. lub podżegacza z art. 18 § 2 k.k.

Include specific evidence requests:

* secure full contents and logs for `waldek@gpucomputer.pl` and `gpucomputer@gpucomputer.pl`;
* secure mail-server, hosting, domain, and CMS/admin logs;
* obtain raw email headers from your messages;
* check login IPs and devices for both mailboxes;
* obtain Mateusz’s business bank statements and trace transfers to Waldek or cash withdrawals;
* verify who issued proforma 2/01-2026 and who had access to the bank account;
* require supplier/customs proof for the “customs cleared” statement and proof of the alleged Hong Kong supplier bankruptcy;
* verify Mateusz’s Netherlands employment/residence and who operated the Kraków business day-to-day;
* identify other customers/victims.

The downside of naming Waldek is that, if phrased too aggressively, it can look speculative. The fix is simple: attach the evidence, use “uzasadnione podejrzenie,” and ask the prosecutor to verify his role. The upside is much greater: it preserves the path to art. 46 KK restitution against him personally and to art. 11 KPC binding effect in a later civil case.

**Concrete recommendation:** name **both Mateusz and Waldek** now, with Mateusz as the formal seller/account holder and Waldek as suspected de facto operator/co-perpetrator, plus “inne ustalone osoby.” Plead art. 286 § 1 KK as the core offence, art. 18 § 1 KK as the main participation theory for Waldek, and art. 18 § 3 / § 2 KK as fallbacks.

[1]: https://isap.sejm.gov.pl/isap.nsf/download.xsp/WDU19970880553/U/D19970553Lj.pdf "https://isap.sejm.gov.pl/isap.nsf/download.xsp/WDU19970880553/U/D19970553Lj.pdf"
[2]: https://www.sn.pl/sites/orzecznictwo/OrzeczeniaHTML/ii%20kk%20113-16-1.docx.html "https://www.sn.pl/sites/orzecznictwo/OrzeczeniaHTML/ii%20kk%20113-16-1.docx.html"
[3]: https://www.saos.org.pl/judgments/490822 "https://www.saos.org.pl/judgments/490822"
[4]: https://www.sn.pl/sites/orzecznictwo/Orzeczenia1/II%20KK%20162-11.pdf "https://www.sn.pl/sites/orzecznictwo/Orzeczenia1/II%20KK%20162-11.pdf"
[5]: https://www.sn.pl/sites/orzecznictwo/Orzeczenia1/V%20KK%20351-03.pdf "https://www.sn.pl/sites/orzecznictwo/Orzeczenia1/V%20KK%20351-03.pdf"
[6]: https://isap.sejm.gov.pl/isap.nsf/download.xsp/WDU19970890555/U/D19970555Lj.pdf "https://isap.sejm.gov.pl/isap.nsf/download.xsp/WDU19970890555/U/D19970555Lj.pdf"
[7]: https://isap.sejm.gov.pl/isap.nsf/download.xsp/WDU19640160093/U/D19640093Lj.pdf "https://isap.sejm.gov.pl/isap.nsf/download.xsp/WDU19640160093/U/D19640093Lj.pdf"
[8]: https://www.sn.pl/sites/orzecznictwo/OrzeczeniaHTML/iii%20czp%2089-17.docx.html "https://www.sn.pl/sites/orzecznictwo/OrzeczeniaHTML/iii%20czp%2089-17.docx.html"
[9]: https://www.sn.pl/sites/orzecznictwo/Orzeczenia1/I%20KZP%2040-00.pdf "https://www.sn.pl/sites/orzecznictwo/Orzeczenia1/I%20KZP%2040-00.pdf"
[10]: https://isap.sejm.gov.pl/isap.nsf/download.xsp/WDU19640430296/U/D19640296Lj.pdf "https://isap.sejm.gov.pl/isap.nsf/download.xsp/WDU19640430296/U/D19640296Lj.pdf"
[11]: https://www.sn.pl/sites/orzecznictwo/OrzeczeniaHTML/i%20csk%20571-16-1.docx.html "https://www.sn.pl/sites/orzecznictwo/OrzeczeniaHTML/i%20csk%20571-16-1.docx.html"
[12]: https://isap.sejm.gov.pl/isap.nsf/download.xsp/WDU19971370926/U/D19970926Lj.pdf "https://isap.sejm.gov.pl/isap.nsf/download.xsp/WDU19971370926/U/D19970926Lj.pdf"
