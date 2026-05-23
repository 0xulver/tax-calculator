# Czynny Zal For PIT-38 Correction And Late Filing

Date: 2026-04-27

Status: updated synthesis after external-agent review by:

- `Czynny Zal PIT-38 Analysis - ChatGPT 5.5 Pro.md`
- `Polish Tax Correction and Active Regret - Gemini 3.1 Deep Research.pdf`

This is decision support, not formal legal advice. If the tax office has already
contacted the taxpayer about PIT-38, crypto, capital gains, foreign assets, or
if any corrected PIT-38 position shows tax due, consult a Polish doradca
podatkowy and, for penal-fiscal exposure, an adwokat/radca prawny handling KKS.

## Facts Assumed

- The taxpayer became Polish tax resident during 2023.
- A 2023 PIT-38 was filed, but it used the wrong crypto/cost-basis and
  carry-forward position.
- No manual 2024 PIT-38 was filed, unless e-Urzad Skarbowy / Twoj e-PIT shows
  an auto-accepted or otherwise submitted PIT-38 for 2024.
- The current repo filing posture is:
  - 2023 PIT-38: correction, tax due `0 PLN`, carry-forward `825,656.90 PLN`.
  - 2024 PIT-38: correction if an auto-accepted PIT-38 exists; otherwise late
    first filing, tax due `0 PLN`, carry-forward `528,067.97 PLN`.
  - 2025 PIT-38: normal timely annual filing, tax due `0 PLN`,
    carry-forward `472,061.65 PLN`.
- The taxpayer used a tax company after moving to Poland and told them about
  working in crypto, but the full PIT-38 crypto transaction/cost reconstruction
  was not completed then.

## Bottom Line

The external reports agree on the core legal split:

- **2023** is primarily an **art. 16a KKS correction** case because a PIT-38
  return already exists and the remediation is a legally effective correction.
- **2024** depends on e-US status:
  - if no PIT-38 exists, file a **late first PIT-38** and use **art. 16 KKS
    czynny zal**;
  - if a PIT-38 was auto-accepted or already submitted, file a **correction** and
    art. 16a becomes the primary protection.
- A single active-regret notice may still conservatively describe the whole
  2023-2024 cleanup, but it should not over-admit tax evasion and should not
  blame the tax company.
- **2025 should not be part of the offence narrative** because, as of
  `2026-04-27`, the filing deadline has not passed. File it normally by
  `2026-04-30`.

The biggest update from the external reports is wording strategy: **do not name,
blame, or materially describe the tax company in the active regret unless a
Polish adviser intentionally chooses that strategy.** The previous draft's
professional-assistance paragraph is now considered too risky because KKS art. 9
§3 can extend responsibility to a person handling another person's financial
affairs, and art. 16 requires disclosure of cooperating persons. A short
personal explanation based on new residency, language/procedure difficulty, and
misunderstanding of separate PIT-38 crypto cost carry-forward rules is safer.

## What Art. 16 Czynny Zal Protects Against

KKS art. 16 says the offender is not punishable for a fiscal offence or fiscal
misdemeanor if, after the act, they notify the prosecuting authority and disclose
the material circumstances, especially cooperating persons.

Conditions:

- file before the authority has clearly documented knowledge of the offence;
- file before official revealing actions have started, such as checking
  activities, search, or audit, unless that action gave no basis to start a
  proceeding;
- disclose material circumstances;
- disclose cooperating persons, if any;
- if the act reduced a public-law receivable, pay it in full within the deadline
  set by the authority.

It does **not**:

- cancel the duty to file or correct PIT-38;
- cancel tax or late-payment interest if any tax is due;
- prove the crypto cost basis is substantively correct;
- prevent a later tax audit;
- protect facts or years that were not disclosed.

For this repo's current PIT-38 posture, the filed corrections/returns show
`0 PLN` tax due. That means the immediate role of czynny zal is penal-fiscal
risk management for late/misreported compliance, not arrears payment.

## What Art. 16a KKS Adds

KKS art. 16a is the cleaner mechanism for an already-filed wrong return. It says
a person is not punishable for a prohibited act concerning filing a declaration
or sending a book if, after the act, a legally effective correction is filed for
the obligation whose incorrect performance constituted the act.

Payment condition: if the act caused public-law underpayment, the amount must be
paid promptly, no later than the deadline set by the financial
preparatory-proceeding authority.

Limit: art. 16a does not apply if, before the correction, preparatory
proceedings were started or the offence was revealed in ongoing preparatory
proceedings.

Applied here:

- 2023 PIT-38 correction: art. 16a is primary.
- 2024 PIT-38 correction, if auto-accepted/already submitted: art. 16a is
  primary.
- 2024 late first filing, if no return exists: art. 16a does not apply because
  there is no return to correct; use art. 16.

## Year-By-Year Mechanism Table

| Year / status | Filing type | Likely KKS issue on current facts | Primary protection | Required action |
| --- | --- | --- | --- | --- |
| 2023 PIT-38 already filed but wrong | `korekta zeznania PIT-38` | Wrong declaration/carry-forward data; art. 56 underpayment risk is weaker if tax remains `0 PLN`, but a false carry-forward can still matter for later years. | Art. 16a KKS. Optional inclusion in one art. 16 narrative is conservative. | File legally effective PIT-38 correction; pay promptly if any receivable is later determined. |
| 2024: no PIT-38 exists | Late first PIT-38 / `zalegle zeznanie` | Art. 56 §4 late declaration risk can exist even without tax underpayment. Art. 54/56 §1 underpayment exposure is weaker if tax due is truly `0 PLN`. | Art. 16 KKS. | Submit active regret before, or essentially simultaneously with, the late PIT-38; then file the late PIT-38 immediately. |
| 2024: PIT-38 auto-accepted or otherwise submitted | `korekta PIT-38` | Same correction posture as 2023. | Art. 16a KKS. Optional inclusion in art. 16 notice is conservative. | Confirm status in e-US, file correction, keep proof of prior return and correction. |
| 2025 before `2026-04-30` | Ordinary timely PIT-38 | No offence if filed by deadline. | Neither art. 16 nor art. 16a needed. | File normally using corrected 2024 carry-forward. |

## Why Zero Tax Does Not End The Issue

External reports agree that `0 PLN` tax reduces the seriousness of the
underpayment analysis, but it does not make the compliance issue disappear.

- PIT-38 crypto reporting is not only a tax-payment form. It also preserves and
  rolls forward unused virtual-currency costs.
- Art. 56 §4 KKS separately addresses late filing of declarations even where the
  taxpayer otherwise disclosed the subject or basis.
- Wrong or missing carry-forward fields can create latent future underpayment
  exposure if they later suppress taxable income.

So the corrected `0 PLN` result is helpful, but the late/misreported filing
still deserves formal cleanup.

## Tax Company / Professional Help: Updated Strategy

The external reports disagree in tone, but they point in the same practical
direction: **do not make the tax company part of the active-regret narrative
unless advised by counsel.**

Why:

- KKS art. 9 §3 can treat a person handling another person's financial affairs
  under contract or factual performance as a perpetrator-like responsible person.
- Art. 16 requires disclosure of cooperating persons. If the active regret says
  the preparer was told about crypto and failed to handle it, the authority may
  ask who prepared the return and whether that person cooperated in the act.
- That can turn a simple voluntary correction into a multi-party dispute where
  the tax company defends itself by arguing the taxpayer provided incomplete
  information.

Recommended approach for the filed notice:

- Internalize the explanation: new resident, foreign-language/procedure
  difficulty, misunderstanding of Poland's separate PIT-38 crypto cost and
  carry-forward mechanics.
- Do **not** write that the tax company forgot, failed, was busy, or did not ask
  enough questions.
- Prefer not to mention the tax company at all in the submitted czynny zal.
- Keep private evidence of the tax-company relationship and communications in
  the file in case the authority later asks.

If a preparer reference is absolutely needed, make it minimal and neutral, for
example: "Korzystałem z zewnętrznej pomocy przy przygotowaniu rozliczeń, jednak
niniejsze zawiadomienie składam we własnym imieniu po samodzielnym
zidentyfikowaniu nieprawidłowości." Do not name the firm in the initial notice
unless a Polish adviser chooses that route.

## Art. 10 Mistake Of Law

Do not frame the active regret as an art. 10 KKS defence.

Lack of understanding as a foreign/new Polish resident can be useful factual
context, but art. 10 requires subjective/legal analysis of mistake and
culpability. The purpose of art. 16/art. 16a is to avoid that fight by curing the
filing failure. The notice should therefore say the taxpayer misunderstood the
rules as factual background, not argue that no offence occurred because the
mistake was legally justified.

## Timing And Authority Knowledge

The key timing risk is art. 16 §5: active regret is ineffective if submitted
after the enforcement authority already has clearly documented knowledge or has
started official actions aimed at revealing the offence.

External research adds useful nuance:

- A missing 2024 PIT-38 entry in the system should not by itself equal clearly
  documented knowledge of a crypto PIT-38 offence.
- A wrong 2023 PIT-38 sitting in the system should not by itself prove the
  authority already knows the offence.
- PIT-8C is usually not an immediate issue for crypto because crypto exchanges
  generally do not issue PIT-8C/PIT-11 for users.
- DAC8/CARF will increase future crypto reporting visibility. It is not a reason
  to panic about 2023-2024 being already known, but it supports filing promptly
  before automated data matching becomes stronger.

Practical rule: do not call or visit the office to discuss the issue before the
formal notice is filed. Check e-US status silently, prepare the filings, then
submit.

## Filing Order

The external reports differ:

- ChatGPT 5.5 recommends: submit czynny zal first, then immediately file the
  PIT-38 correction/late filing in the same session or same day.
- Gemini recommends: file PIT-38 corrections/late filing first, obtain UPOs,
  then submit active regret attaching those UPOs.

Synthesis:

- For **2023 correction** and **2024 correction** cases, art. 16a means filing
  the correction itself is already the primary protection. UPO/status 200 for
  the correction is important.
- For a **true missing 2024 late first filing**, art. 16 is primary. Filing the
  late PIT-38 before the active regret may create an argument that the authority
  learned of the late filing from the return before receiving the notice.
- Therefore the safer general sequence is:
  1. Prepare all filings first.
  2. Check e-US `Historia deklaracji` / `Zlozone dokumenty` for 2024 PIT-38
     status.
  3. Submit the active-regret notice through e-Urzad Skarbowy or the correct
     e-Delivery channel.
  4. Immediately submit 2023 correction and 2024 late filing/correction.
  5. Confirm each declaration has status `200` and download UPO.
  6. File 2025 normally before `2026-04-30`.

If the system forces attachments or a Polish adviser wants the UPOs attached to
the active regret, perform the active regret and PIT filings in one uninterrupted
session and document timestamps carefully.

## Electronic Filing Channel

Use e-Urzad Skarbowy or the competent authority's e-Delivery channel. Do not use
ordinary ePUAP for this in 2026 unless a Polish adviser confirms a specific
exception. Current MF guidance says that from `2026-01-01`, ePUAP submissions by
individuals/private entities to tax/KAS authorities generally are not treated as
effectively filed, except where special rules allow ePUAP.

Keep:

- active-regret submission confirmation;
- 2023 PIT-38 correction UPO/status `200`;
- 2024 PIT-38 late filing/correction UPO/status `200`;
- 2025 PIT-38 UPO/status `200`;
- screenshots of 2024 e-US status before remediation;
- PDFs/copies of all filed forms;
- repo cost-basis workpapers and exchange/source evidence;
- private tax-company correspondence, not necessarily attached.

## Jurisdiction / Tax Office

The stronger official PIT rule is the office competent by the taxpayer's place
of residence on the filing date. ChatGPT 5.5 and the PIT Act art. 45 source
support this. Gemini said year-end residence for the relevant year; treat that
as a weaker point for this PIT-38 filing context unless a Polish adviser
confirms a special procedural rule for active regret. Practically, use the
current-residence office in e-US unless the portal or adviser directs otherwise.

## Suggested Direction For Revised Filing Text

Do not paste the old draft unchanged. It contains a professional-assistance
paragraph that external research now flags as risky.

For final copy/paste text with no bracketed placeholders, use:

- `docs/tax-law/18-czynny-zal-pit38/ready-to-submit-czynny-zal.md`

A safer Polish concept is:

```text
Działając na podstawie art. 16 § 1 Kodeksu karnego skarbowego, a z ostrożności procesowej również w zakresie art. 16a § 1 Kodeksu karnego skarbowego, zawiadamiam o nieprawidłowym wykonaniu obowiązków podatkowych dotyczących zeznań PIT-38 za lata 2023 i 2024 w zakresie odpłatnego zbycia walut wirtualnych, kosztów uzyskania przychodów oraz kosztów niepotrąconych przenoszonych na kolejne lata.

Za 2023 r. złożyłem już zeznanie PIT-38. Po ponownej rekonstrukcji historii transakcji oraz kosztów nabycia walut wirtualnych ustaliłem, że zeznanie nie wykazywało prawidłowo przychodów, kosztów poniesionych w roku podatkowym oraz kosztów z lat ubiegłych / kosztów niepotrąconych przechodzących na kolejny rok. Składam korektę zeznania PIT-38 za 2023 r. Zgodnie ze składaną korektą podatek do zapłaty z PIT-38 za 2023 r. wynosi 0 zł, a kwota kosztów niepotrąconych do wykazania w roku następnym wynosi 825 656,90 zł.

[2024: wstawić właściwy wariant po sprawdzeniu e-Urzędu Skarbowego: zaległe zeznanie, jeśli PIT-38 nie istnieje, albo korekta, jeśli PIT-38 został złożony lub automatycznie zaakceptowany.]

Nieprawidłowości wynikały z tego, że po przeniesieniu miejsca zamieszkania do Polski w 2023 r. nie rozumiałem jeszcze w pełni zasad odrębnego rozliczania walut wirtualnych w PIT-38, w tym obowiązku wykazywania przychodów, kosztów oraz kosztów przenoszonych na kolejny rok także wtedy, gdy podatek do zapłaty wynosi 0 zł.

Po wykryciu nieprawidłowości, przed kontaktem organu podatkowego w tej sprawie, niezwłocznie porządkuję rozliczenia i składam właściwe zeznania lub korekty. Według składanych zeznań / korekt za lata 2023 i 2024 nie powstaje podatek do zapłaty z PIT-38. Jeżeli organ ustali wymagalną należność publicznoprawną związaną z opisanymi nieprawidłowościami, zobowiązuję się uiścić ją niezwłocznie, nie później niż w terminie wyznaczonym przez właściwy organ.

Według mojej wiedzy przed złożeniem niniejszego zawiadomienia organ ścigania nie miał wyraźnie udokumentowanej wiadomości o opisanych nieprawidłowościach ani nie rozpoczęto wobec mnie czynności służbowych zmierzających do ich ujawnienia.

Według mojej wiedzy w popełnieniu czynu zabronionego nie współdziałały inne osoby.

Zawiadomienie dotyczy rozliczeń za lata 2023-2024. Zeznanie PIT-38 za 2025 r. zostanie złożone w ustawowym terminie.

Proszę o przyjęcie niniejszego zawiadomienia jako zawiadomienia, o którym mowa w art. 16 § 1 Kodeksu karnego skarbowego. W zakresie składanych korekt wskazuję również, że korekty są składane jako prawnie skuteczne korekty deklaracji dotyczące obowiązków, których nieprawidłowe wykonanie zostało opisane powyżej.
```

Do not include bracketed variants in the final filed version. First check e-US,
then submit a single clean text.

## Red Flags Requiring Adviser Review

Stop and consult a Polish adviser before filing if any of these are true:

- any KAS/tax-office letter, e-US message, phone call, summons, audit notice, or
  `czynnosci sprawdzajace` has already happened;
- e-US shows unclear/multiple 2024 PIT-38 documents;
- the corrected `0 PLN` tax position is fragile or likely to become positive;
- the cost basis depends on large unsupported pre-residency/imported basis;
- trading could be characterized as business/professional activity rather than
  private PIT-38 investing;
- the taxpayer wants to name or blame the tax company;
- the tax company had a formal mandate and specific knowledge of the PIT-38
  crypto facts;
- any fiscal-penal/preparatory proceedings may already be pending.

## Source Notes

External source files integrated:

- `docs/tax-law/18-czynny-zal-pit38/Czynny Zal PIT-38 Analysis - ChatGPT 5.5 Pro.md`
- `docs/tax-law/18-czynny-zal-pit38/Polish Tax Correction and Active Regret - Gemini 3.1 Deep Research.pdf`

Official/high-authority sources checked or relied on:

- KKS consolidated text, Dz.U. 2025 poz. 633:
  https://api.sejm.gov.pl/eli/acts/DU/2025/633/text.pdf
- e-Urzad service list including czynny zal:
  https://www.podatki.gov.pl/e-urzad-skarbowy/pytania-i-odpowiedzi/informacje-ogolne/2-jakie-sprawy-moga-zalatwic-w-e-urzedzie-skarbowym/
- MF 2026 e-submission/ePUAP warning:
  https://podatki.gov.pl/aktualnosci/zmiany-w-zasadach-skladania-podan-utrwalonych-w-postaci-elektronicznej-do-organow-podatkowych-i-organow-kas/
- UPO/status 200 guidance:
  https://www.podatki.gov.pl/narzedzia/jak-pobrac-urzedowe-poswiadczenie-odbioru-upo/
- PIT Act art. 45 source for filing-date office rule:
  https://sip.lex.pl/akty-prawne/dzu-dziennik-ustaw/podatek-dochodowy-od-osob-fizycznych-16794311/art-45
- MF PIT-38 2025 guidance:
  https://www.podatki.gov.pl/twoj-e-pit/pit-38-za-2025-rok/
- MF crypto-disposal guidance:
  https://www.podatki.gov.pl/podatki-osobiste/pit/informacje-podstawowe/co-jest-opodatkowane/zbycie-kryptowalut/

Repo sources:

- `docs/todo/filing-summary.md`
- `docs/todo/pit38-filing-guide.md`
- `docs/tax-law/06-late-filing-corrections/synthesis-late-filing-corrections.md`
