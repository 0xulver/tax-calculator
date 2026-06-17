Magnus — here's the full walk-through. The framework below is verified against the current u.k.k. (ustawa o kosztach komorniczych z 28.02.2018), the relevant KPC provisions, and the EU instruments. One caveat up front: I'm giving you the operating reality of how this runs, not a substitute for your komornik/lawyer's case-specific judgment, especially on the cross-border piece which is genuinely the hard part of your scenario.

Part 1 — The linear enforcement procedure (once you hold the tytuł wykonawczy)
Getting from nakaz to tytuł wykonawczy
In EPU, when your nakaz zapłaty becomes final (no skuteczny sprzeciw within the 2-week window from doręczenie), the e-sąd in Lublin-Zachód issues the klauzula wykonalności automatically (z urzędu) — you do not file a separate motion as you would for an ordinary court order. The court is obligated to attach the clause niezwłocznie after the order becomes prawomocny. In EPU the tytuł wykonawczy exists in electronic form with a unique code the komornik verifies in the system, so there's no paper "blue clause" document to physically carry. Tytuł egzekucyjny + klauzula = tytuł wykonawczy, and only on that basis can a komornik act.

Choosing and instructing the komornik (art. 10 u.k.s.)
You as wierzyciel have prawo wyboru komornika. The default właściwość for świadczenia pieniężne ties to the debtor's miejsce zamieszkania — but art. 10 lets you pick any komornik within the area of the same sąd apelacyjny as the territorially-proper komornik, by filing a written oświadczenie that you're using the choice right (the standard wording: "Wyboru komornika dokonuję na podstawie art. 10 ust. 3 ustawy o komornikach sądowych").

Why this matters for you: your debtor's registered seat is Kraków, so your choice pool is komorniks under the Sąd Apelacyjny w Krakowie. The lever is that you can shop for one who is genuinely fast and digitally aggressive on OGNIVO/CEPiK/EKW queries rather than accepting whoever is geographically nearest. The constraint: a chosen out-of-rewir komornik must refuse your case if (a) his backlog exceeds 6 months — unless his prior-year intake was under 1,000 cases; (b) his intake exceeded 2,500 and his prior-year skuteczność was below 35%; or (c) intake exceeded 5,000. Practical move: check the kancelaria's statistics (published via the sąd rejonowy, refreshed every 6 months) before filing, and confirm the komornik accepts z wyboru cases. Note the choice right does NOT apply to egzekucja z nieruchomości — if real estate turns up, that piece reverts to the komornik in whose rewir the property sits.

The wniosek egzekucyjny — what to load in
Attach/reference the tytuł wykonawczy and specify the egzekucja methods you authorize: z rachunków bankowych, z wierzytelności, z ruchomości, z nieruchomości, etc. Critically, given you don't have full visibility into his assets, include:

a wniosek o poszukiwanie majątku (art. 8011 KPC) — fee 100 zł — which obliges the komornik to actively hunt across the registers he can reach;

the known Alior IBAN (PL84 2490… is indeed Alior Bank's range), plus a request to run OGNIVO across all banks anyway in case he moved funds;

a request for ZUS/US queries to find any Polish employer/income.

Costs, advances, and who ultimately pays
Upfront from you: the komornik can demand zaliczki on wydatki (register queries, correspondence) — payable within a deadline not shorter than 7 days (art. 7 u.k.k.). Indicative line items: EKW query ~20 zł, poszukiwanie majątku 100 zł, US e-query ~3.17 zł (Komornik Lublin fee list, Komornik Gdańsk-Północ fee list). On a 155k claim these are small.

The główna opłata egzekucyjna: 10% of the amount actually recovered, collected by the komornik from the debtor's seized funds with first priority (art. 27 ust. 1 u.k.k.) (LexLege art. 27, BIG InfoMonitor). It comes out of recovery, not on top of your claim — i.e. the debtor bears it.

Reduced 3% rate: if the debtor voluntarily pays the komornik within one month of being served the zawiadomienie o wszczęciu egzekucji, the rate on that sum drops to 3% (art. 27 ust. 2). Note money the debtor pays directly to you (not via komornik) is not treated as "wyegzekwowane," so it doesn't trigger the komornik's percentage — relevant if he settles with you directly.

Where YOU can get stuck with fees: if you withdraw the wniosek / the case is umorzone na Twój wniosek without showing a settlement, you can owe 5% (art. 29). If you launched an "oczywiście niecelowe" egzekucja (e.g. debtor already paid or is dead and you knew), 10% falls on you (art. 30). Importantly, umorzenie z powodu bezskuteczności (the empty-pocket scenario you expect) is NOT the same as withdrawing — it does not trigger the 5%; you're at most out the wydatki you advanced.

Timeline
There's no statutory clock for recovery. Account/register queries (OGNIVO, CEPiK, EKW, ZUS, US) typically run within the first weeks. A bank zajęcie is near-instant once an account is found. Where the realistic answer in your case is that the komornik exhausts the register sweep within a few months and, finding nothing, moves toward umorzenie — see Part 2.

Part 2 — What the komornik can search and seize in Poland
The komornik runs these electronically:

Register / source	What it reveals
OGNIVO (via KIR)	Bank & SKOK accounts across all Polish banks — the master account sweep
CEPiK	Registered vehicles
CBDKW / EKW	Real estate in the land & mortgage registers; basis for a hipoteka przymusowa
PUE-ZUS	Employment/insurance — who pays his składki (i.e. a Polish employer)
US (Urząd Skarbowy)	Tax data, declared income, accounts
REGON/CEIDG (moduły niejawne), KRS, BIG	Business registration, entity links, debt registers
On seizure: once an account is found, the komornik issues a zajęcie and orders the bank not to release funds beyond the protected minimum without his consent. He can attach receivables from third parties (zajęcie wierzytelności), cash, and ruchomości, and can place a hipoteka przymusowa on any real estate that surfaces in EKW.

JDG = no subsidiarity, and this is your key structural advantage. A jednoosobowa działalność gospodarcza has no legal personality separate from Mateusz Szklarski. There is no "business estate" vs "personal estate" distinction and no corporate veil to pierce. The komornik attaches "business" and personal assets as one undifferentiated pool of his property — his private bank account, his car, his apartment, and any GPUcomputer receivables are all simply "majątek dłużnika." You don't need to choose; the single tytuł reaches everything he owns.

Part 3 — The "nothing in Poland" scenario (your expected case)
This is the realistic path: OGNIVO shows an empty/near-empty Alior account, CEPiK and EKW show no vehicles or property, ZUS/US show no Polish income because his wages are in the Netherlands.

Umorzenie wobec bezskuteczności (art. 824 § 1 pkt 3 KPC)
The komornik umarza postępowanie z urzędu when "jest oczywiste, że z egzekucji nie uzyska się sumy wyższej od kosztów egzekucyjnych" — i.e. after directing enforcement at all discoverable asset components, there's nothing yielding more than the cost of pursuing it.

What you receive: a postanowienie o umorzeniu postępowania egzekucyjnego z uwagi na bezskuteczność egzekucji. Crucially, with it the komornik returns your tytuł wykonawczy (the original, with annotation of what was recovered). Keep this postanowienie and the returned title together — they are the two documents that unlock everything below.

Strategic value of the bezskuteczność postanowienie — this is the real asset you walk away with
Tax write-off: the postanowienie o bezskuteczności is the canonical documentary basis Polish tax law accepts to write off an uncollectible receivable as koszt uzyskania przychodu / odpisać należność nieściągalną. It is the proof that udokumentowanie nieściągalności requires. (Confirm the exact treatment for your CIT/PIT posture with your accountant — but this document is precisely what they'll ask for.)

Criminal track (art. 300 KK): if you suspect he stripped or hid assets to defeat you, the bezskuteczność record is hard evidence that the egzekucja failed. Note art. 300 KK reaches even the attempt — "gdy sprawca zawiera czynność prawną z zamiarem udaremnienia lub uszczuplenia zaspokojenia wierzyciela… dopuszcza się karalnego usiłowania" even if the harmful result didn't fully materialize. A zawiadomienie o podejrzeniu popełnienia przestępstwa with the failed-enforcement file attached gives the prosecutor a ready evidentiary spine, and a criminal investigation often produces asset information civil tools couldn't reach.

Re-attempt later: umorzenie does not extinguish the debt or the title. You can return the same tytuł wykonawczy to a komornik any time his circumstances change (Polish job, inheritance, property purchase, return from NL).

Cross-border leverage: the documented Polish bezskuteczność strengthens the factual basis (uzasadnione przypuszczenie / urgency) for the EU instruments in Part 4.

Wyjawienie majątku (art. 913 KPC)
When the seized assets don't promise satisfaction, or you show enforcement didn't fully satisfy you (the bezskuteczność state), you can move to compel the debtor to file a sworn wykaz majątku — listing assets, their locations, receivables and other property rights — plus a court-administered przyrzeczenie under the prescribed rota ("Świadomy znaczenia mych słów i odpowiedzialności przed prawem zapewniam, że złożony przeze mnie wykaz majątku jest prawdziwy i zupełny").

File it at the debtor's sąd rejonowy właściwości ogólnej (file in court, not via the komornik, to avoid the relay delay).

Disclosure is obligatory and enforceable — refusal can draw grzywna and even areszt to compel compliance, and the court can refer him to the rejestr dłużników niewypłacalnych in KRS.

The honest limitation for your case: the coercive teeth (grzywna, areszt) require the court to reach him. With him living and working full-time in the Netherlands, doręczenie and physical compulsion are the practical bottleneck. The tool stays legally available, and a wykaz he does file is valuable (it can name foreign assets), but you cannot realistically jail an absent debtor in Kraków. Treat wyjawienie as most useful if/when he's physically in Poland, or as a record-building step rather than a force multiplier while he's abroad.

Limitation period on the title
A roszczenie stwierdzone prawomocnym orzeczeniem przedawnia się z upływem 6 lat (art. 125 § 1 KC; reduced from 10 years effective 9 July 2018), with the end of the period falling on 31 December of the relevant year (art. 118 zd. 2 KC) (Currenda on przedawnienie, Kancelaria Dziurkiewicz). The 6-year clock is interrupted (przerwanie biegu) by each enforcement action — so filing the wniosek egzekucyjny resets it, and it restarts after the postępowanie ends. The główna kwota runs 6 years; świadczenia okresowe (the interest) run 3 years going forward (art. 125 § 1 zd. 2). Practical upshot: don't let 6 years lapse without an enforcement act on the principal, and watch the 3-year interest window so accrued odsetki don't quietly time-bar.

Part 4 — Reaching his Dutch income from Poland (high-level)
Short answer: a Polish komornik has no reach over NL wages. Polish enforcement authority is territorial; the komornik can attach a Polish bank account or a Polish employer's payroll, but he cannot order a Dutch employer to withhold wages. To touch income or accounts in the Netherlands you need an EU instrument carried over and executed by Dutch authorities — there's no shortcut from a purely domestic Polish egzekucja. The good news under Rozporządzenie (UE) 1215/2012 (Brussels I bis): a Polish judgment with the right zaświadczenie is directly enforceable in NL without a separate exequatur. Full mechanics — Article 53 certificate, Dutch deurwaarder, translation, beslag op loon — belong in prompt 6.

Part 5 — Anti-dissipation: fastest protective step post-nakaz
Given your lawyer's view that pre-judgment civil zabezpieczenie inside EPU isn't available, your fastest realistic protective move once the nakaz issues is the Europejski Nakaz Zabezpieczenia na Rachunku Bankowym (EPGR / EAPO, Rozporządzenie (UE) 655/2014) — and it fits your facts almost perfectly because it's designed for the cross-border money-account scenario:

It freezes funds in a bank account in another Member State (here: NL), and is available only in transgraniczne sprawy — precisely your situation (Polish creditor/court, Dutch account).

It's issued bez wysłuchania dłużnika (ex parte, surprise effect) — exactly what you want against someone likely to move money.

Once you hold a wykonalne orzeczenie, you can request it even without knowing his account number, via the Article 14 mechanism asking the court to order the information authority of the executing state to identify his bank(s) — directly useful since you only know a (likely empty) Polish account.

For purely Polish assets, the post-nakaz domestic protective route is to move to enforcement immediately — the bank zajęcie itself functions as the freeze the moment an account is located, so speed of filing the wniosek egzekucyjny is your anti-dissipation tool inside Poland. The EAPO is the instrument that actually addresses the NL exposure where his real money is.

Bottom line for your case: domestic egzekucja will most likely produce a bezskuteczność postanowienie — and you should treat that document as the deliverable, not a defeat. It unlocks the tax write-off, arms the art. 300 KK track, preserves the title for 6 years of re-attempts, and underpins the EU instruments (EAPO now, Brussels I bis enforcement in NL) that are the only real path to his Dutch wages. Want me to draft the wniosek egzekucyjny (with the art. 10 choice clause + poszukiwanie majątku), or move straight into the prompt 6 cross-border execution mechanics?