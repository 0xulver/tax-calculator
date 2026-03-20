# Research: JDG Stablecoin Payments vs EUR Bank Transfers

## Context

A Polish tax resident operates a JDG (Jednoosobowa Dzialalnosc Gospodarcza) registered under PKD 62.01.B (software development), taxed under ryczalt od przychodow ewidencjonowanych at 12%. The JDG invoices a single foreign B2B client for software development services.

The client has offered the option to pay either:
- **Option A**: EUR via regular SEPA bank transfer to the JDG's Polish business bank account
- **Option B**: Stablecoins (USDC or USDT) on-chain (e.g., Polygon, Ethereum, Arbitrum) to the developer's wallet

The developer currently receives EUR (Option A) and pays 12% ryczalt monthly. The developer has prior experience receiving USDC payments before establishing the JDG (in early 2025, as personal income classified as umowa zlecenie / Art. 13 pkt 8), and has deep familiarity with crypto markets.

The developer's tax research has established:
- Stablecoins (USDC/USDT) are classified as "waluta wirtualna" under Polish AML law
- Crypto-to-crypto swaps are non-taxable
- Crypto-to-fiat conversion is a taxable disposal on PIT-38
- Under the "barter doctrine" (KIS interpretations), receiving crypto as payment for services creates income at receipt, with the receipt value becoming the cost basis for later PIT-38 disposal
- The developer already has a large crypto cost pool carry-forward (~319K PLN)

## Questions

### Revenue Recognition and Ryczalt Calculation

1. If the JDG invoices 10,000 USD and receives 10,000 USDC on-chain, how is ryczalt revenue recognized?
   - Is the revenue date the invoice date, service completion date, or USDC receipt date?
   - What PLN value is used? NBP USD rate from the day before revenue date? Or actual market value of USDC at receipt?
   - Is the 12% ryczalt calculated on this PLN amount?

2. If the client pays in USDC but the invoice is denominated in USD or EUR, does the invoice currency or the payment medium determine the PLN conversion?

3. Does it matter whether the invoice says "payable in USDC" vs "payable in USD (settlement in USDC)"? Does the contractual framing affect tax treatment?

4. For ryczalt purposes, is there any difference between receiving EUR via bank vs USDC on-chain? The 12% tax on gross revenue should be the same — but are there hidden complications?

### The PIT-38 Layer (Crypto Disposal)

5. Under the barter doctrine, receiving USDC as JDG business income creates TWO tax events:
   - PIT-28: ryczalt on the service revenue at receipt
   - PIT-38: crypto disposal when USDC is later converted to EUR/PLN

   Is this double-reporting correct for a JDG on ryczalt? Does the ryczalt receipt value become the PIT-38 cost basis?

6. If the developer converts USDC to EUR immediately after receipt (same day), is the PIT-38 gain/loss essentially zero (only micro FX movement)?

7. If the developer HOLDS the USDC for weeks/months before converting (e.g., waiting for a better EUR/PLN rate), does the FX movement between receipt and conversion become taxable on PIT-38?

8. If the developer uses the USDC to buy other crypto (e.g., ETH for DeFi), is that a non-taxable crypto-to-crypto swap, meaning the USDC is never "disposed of" for PIT-38 purposes?

### FX and Accounting Complications

9. With EUR bank payments, FX differences (roznice kursowe) arise between invoice date and payment date. With USDC, do the same FX difference rules apply? Or is it handled differently because USDC is crypto, not fiat?

10. Does the ewidencja przychodow (revenue register) need to record USDC payments differently from EUR payments?

11. Are there any VAT implications that differ between EUR and USDC payments? (The JDG is currently VAT-exempt under the 200K PLN threshold.)

### Practical Advantages and Disadvantages

12. What are the concrete tax ADVANTAGES of receiving USDC over EUR for a JDG on ryczalt?
    - Does the cost basis mechanism on PIT-38 create any tax optimization opportunities?
    - Can holding USDC and converting strategically reduce overall tax?
    - Does the large existing crypto cost pool (~319K PLN carry-forward) change the calculus?

13. What are the concrete tax DISADVANTAGES or risks?
    - Double reporting burden (PIT-28 + PIT-38)?
    - Documentation requirements?
    - Audit risk from mixing business income with crypto?
    - Risk of reclassification of the JDG activity?

14. Are there any KIS interpretations specifically about a JDG on ryczalt receiving payment in stablecoins/crypto?

### Cash Flow and Banking

15. If the developer receives USDC and converts to EUR on Binance/Kraken, then withdraws EUR to the business bank account — does the bank withdrawal create any additional tax events or reporting obligations?

16. Are there any AML/compliance issues with a JDG receiving on-chain payments? Does the business need to register as a crypto service provider?

## Desired Output

A clear comparison table showing the complete tax journey for both options:
- Option A: Client pays EUR -> JDG bank account -> ryczalt 12%
- Option B: Client pays USDC -> wallet -> (optional hold) -> convert to EUR on exchange -> withdraw to bank -> ryczalt 12% + PIT-38

Include: total tax burden comparison, compliance burden comparison, risk assessment, and practical recommendation for a developer with the described setup.
