# Research: Tax Treatment of USDC Salary Payments Before Having a Company in Poland

## Context

A Polish tax resident (since ~2023) has been receiving payment for software development work in USDC (a stablecoin) on the Polygon blockchain. This has happened in two separate periods:

### Period 1: Full year 2024 (already filed)

In 2024, the taxpayer worked for a **US-registered DeFi company** (no Polish entity, no Polish tax presence) as a software developer. The taxpayer was paid in USDC on the Polygon blockchain throughout 2024. The taxpayer did NOT have a JDG (sole proprietorship) during 2024.

A Polish tax company was hired to prepare the 2024 tax return. They filed a **PIT-37** with the following:

- **Section E, Row 3**: "Dzialalnosc wykonywana osobiscie" (Art. 13 ustawy)
- **Poz. 67** (przychody z umow zlecenia, Art. 13 pkt 8): **479,092.64 PLN**
- **Poz. 68** (koszty uzyskania): **95,818.53 PLN** (exactly 20% of revenue -- the standard umowa zlecenie deduction)
- **Dochod**: **383,274.11 PLN**
- **Tax calculated** (progressive scale 12%/32%): **95,048 PLN**
- **Advance tax paid by payer (zaliczka pobrana przez platnika)**: **0 PLN**
- **Full tax to pay at filing**: **95,048 PLN**
- **Tax office**: Trzeci Urzad Skarbowy Warszawa-Srodmiescie
- **No PIT-38** was filed for crypto gains/losses in 2024
- **No attachments** (PIT/O, PIT/ZG, etc.) were included

The filed PIT-37 is available at: `/home/ulver/code/ai/tax-calculator/docs/personal-tax/pit.pdf`

### Period 2: Early 2025 (not yet filed)

In early 2025, BEFORE establishing a JDG, the taxpayer continued receiving USDC payments (now from a different client). Amounts:

- Jan 2, 2025: 6,000 USDC
- Jan 15, 2025: 6,000 USDC
- Feb 4, 2025: 6,000 USDC
- Feb 17, 2025: 6,000 USDC
- Mar 3, 2025: 6,000 USDC
- Mar 17, 2025: 6,000 USDC
- Apr 1, 2025: 4,500 USDC

Total: 40,500 USDC (~160,000-165,000 PLN at the time)

Some or all of this USDC was later converted to EUR on exchanges (Binance, Kraken) and withdrawn to a bank account.

After this period, the taxpayer established a JDG with ryczalt 12% and began invoicing in EUR.

### Swedish precedent

The taxpayer previously lived in Sweden. The Swedish tax authority (Skatteverket) ruled that receiving USDC as salary is **salary income** (not crypto capital gains), and required it to be declared as employment/service income at receipt time.

---

## Critical Questions About the 2024 Filing (Already Submitted)

### Was PIT-37 the correct form?

1. **PIT-37 is specifically for income reported on PIT-11, PIT-11A, PIT-40A, PIT-R, or IFT-1R** (as stated in the form header). Did the US DeFi company issue any of these documents? If they are a foreign entity with no Polish presence, they almost certainly did NOT issue a PIT-11. Did they issue an IFT-1R? An IFT-1R is issued by Polish entities paying non-residents, so this also seems wrong.

2. **If no PIT-11 or IFT-1R was issued**, should the correct form have been **PIT-36** instead of PIT-37? PIT-36 is for income where the taxpayer self-reports (including foreign income not covered by PIT-11).

3. If PIT-37 was the wrong form, does the filing need to be corrected (korekta)? What are the implications?

### Was the income classification correct?

4. The tax company classified the income as **"umowa zlecenie" (Art. 13 pkt 8)** -- a civil-law contract for personal services. Is this the correct classification for:
   - A foreign client (US DeFi company) with no Polish presence?
   - Payment made in cryptocurrency (USDC), not in fiat?
   - No formal written contract, or a B2B services agreement?

5. Could this income instead be classified as:
   - **Dzialalnosc gospodarcza (business activity)** -- since it was regular, recurring, organized work for profit? If so, the taxpayer should have registered a JDG.
   - **Inne zrodla (other sources, Art. 20)** -- catch-all category?
   - **Przychod z walut wirtualnych (crypto income)** -- if the "payment" is viewed as the taxpayer receiving crypto, not service income?

6. The 20% cost deduction (koszty uzyskania przychodow) was applied. Is this correct for Art. 13 pkt 8 income from a foreign payer? The standard 20% applies to umowa zlecenie, but are there any limitations?

### Were advance tax payments required?

7. **No advance tax (zaliczka) was paid during 2024** (poz. 66 = 0). For umowa zlecenie with a Polish payer, the payer withholds advance tax. But with a foreign payer who doesn't withhold, **was the taxpayer obligated to make monthly advance tax payments themselves** (Art. 44 ust. 1a ustawy o PIT)?

8. If monthly advance payments WERE required and were NOT made, what are the consequences? Interest on late payments? Penalties?

9. The full 95,048 PLN was paid at filing time. Does paying the full amount at filing (instead of monthly advances) trigger automatic interest charges?

### Should a PIT/ZG (foreign income annex) have been attached?

10. Since the payer is a US company, should **PIT/ZG** (Informacja o wysokosci dochodow/strat z zagranicy) have been attached to the filing?

11. Does the Poland-USA double taxation treaty affect this? Which article applies to personal services income / freelance income?

### Was the tax company potentially wrong?

12. Given that:
    - PIT-37 was used (possibly wrong form for foreign payer)
    - No advance tax was paid during the year
    - No PIT/ZG attachment for foreign income
    - The income was paid in USDC (cryptocurrency), not fiat
    - There was no Polish PIT-11 or IFT-1R document backing the filing
    - The classification as umowa zlecenie for a US company paying in crypto is unusual

    **How likely is it that the tax company made errors?** Is this a niche case where most tax companies wouldn't have the expertise? What should be corrected?

13. If corrections are needed to the 2024 PIT-37, can they be filed now? Would a korekta (correction) replace it, or would a new PIT-36 need to be filed alongside?

---

## Critical Questions About 2025 (Not Yet Filed)

### Classification of the pre-JDG income

14. For Jan-Apr 2025 USDC payments received BEFORE establishing the JDG: should the same approach as 2024 be used (personal services income)? Or should it be reported differently?

15. If the JDG was established in, say, April/May 2025: can the pre-JDG income be reported through the JDG retroactively? Or must it remain personal income on PIT-36/37?

16. Since the taxpayer established a JDG shortly after, does the regular pattern of USDC payments (biweekly, ~$6K each, from one client) indicate that this was **de facto business activity** (dzialalnosc gospodarcza) even before registration? What are the consequences of not having been registered?

### When is the taxable event?

17. Under Polish tax law, how is payment received in cryptocurrency (specifically stablecoins like USDC) for services classified? Is it:
    a) Regular income from personal services taxed at PIT progressive rates (12%/32%) at receipt?
    b) Crypto capital gains (19% flat on PIT-38) at conversion to fiat?
    c) Both? (income tax at receipt + capital gains at conversion?)
    d) Something else?

18. Is receiving USDC in exchange for services treated the same as receiving USD/EUR? Or does the fact that it's cryptocurrency change the classification?

19. If the income is taxed at receipt (like Sweden), what PLN value should be used? NBP mid-rate for USD from the last business day before receipt? Market price of USDC?

20. If taxed at receipt as income: when USDC is later sold for EUR, is there an additional capital gains event? What would the cost basis be? (Presumably the PLN value already declared as income?)

### Interaction with crypto capital gains (PIT-38)

21. In 2025, the taxpayer also converted USDC to EUR on exchanges (creating taxable events on PIT-38). If the USDC was received as salary and already taxed as income at receipt, the cost basis for PIT-38 should equal the value declared as income. This would make the USDC->EUR conversion nearly tax-neutral (only FX movement between receipt and conversion). **Is this understanding correct?**

22. If the tax company's 2024 approach was wrong and the USDC should have been classified as crypto income (PIT-38) instead of personal services income (PIT-37), then:
    - The 2024 revenue of 479,092.64 PLN would need a cost basis (the original acquisition cost of the USDC)
    - But the USDC was received for free (as payment) -- what cost basis?
    - This would result in ~479K PLN taxable at 19% = ~91K PLN (similar to the 95K already paid)
    - But the form and classification would be completely different

### The Swedish precedent

23. In Sweden, Skatteverket classified USDC salary as employment income (not crypto). Does Polish law have a similar position? Are there any official interpretations (interpretacje indywidualne) from the Director of KIS (Krajowa Informacja Skarbowa) on paying for services in cryptocurrency?

24. If Poland takes the same position as Sweden (income at receipt), does this mean:
    - Pay income tax on the PLN equivalent at receipt time
    - The cost basis for crypto purposes equals the value already taxed as income
    - So the later USDC->EUR conversion is nearly tax-neutral on PIT-38?

---

## ZUS and Social Insurance

25. For 2024 (no JDG, income from US company): were there any **ZUS (social insurance) obligations**? If classified as umowa zlecenie with a foreign payer, who pays ZUS? Did the tax company handle this?

26. For early 2025 (pre-JDG): same question about ZUS obligations.

27. If the taxpayer should have been paying ZUS and wasn't, what are the consequences? Can it be corrected retroactively?

---

## Desired Output

This is the MOST IMPORTANT research document for the taxpayer's situation. The research agent should:

1. **Evaluate the 2024 PIT-37 filing** -- was it correct or does it need correction?
2. **Determine the correct classification** of USDC salary payments under Polish law, with legal references
3. **Assess whether advance tax payments** should have been made in 2024 and the consequences of not making them
4. **Provide clear guidance for 2025 filing** of pre-JDG USDC income
5. **Explain the interaction between service income and PIT-38 crypto gains** for the same USDC
6. **Reference any KIS interpretations** about crypto payments for services
7. **Assess ZUS obligations** for both periods

If the answer is ambiguous, present all plausible interpretations with their legal basis and risk level. Flag which issues are most urgent for correction.
