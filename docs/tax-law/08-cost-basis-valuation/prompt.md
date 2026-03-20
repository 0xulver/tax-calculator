# Research: Cost Basis and Valuation Rules for Crypto Tax in Poland

## Context

The taxpayer needs to compute FIFO cost basis for crypto disposals across multiple years. Crypto was acquired through various means (exchange purchases, salary payments, staking rewards, airdrops, DeFi). Disposals are primarily crypto-to-EUR conversions on Binance and Kraken. This research focuses on the exact legal requirements for valuing transactions in PLN.

## Questions

### NBP Exchange Rate Rules
1. Article 11a ust. 2 ustawy o PIT states that foreign currency amounts should be converted using NBP mid-rate from the last business day preceding the day of income receipt. Confirm this applies to crypto transactions. What is the exact wording?

2. When selling USDC for EUR on Binance:
   - The "income" is EUR received. Must this be converted at NBP EUR mid-rate from the last business day BEFORE the trade date?
   - Or can the trade-day rate be used?
   - What if the trade happens on a Saturday -- which NBP rate applies?

3. When determining cost basis for USDC received as salary payment:
   - USDC is pegged to USD. Should the cost basis use NBP USD rate?
   - From which date -- the day before receiving the USDC?
   - What if USDC was not exactly 1:1 with USD on that day (depegged)?

4. For crypto purchased with EUR on an exchange: cost basis = EUR amount x NBP EUR rate from the day before purchase?

5. Does the "last business day before" rule apply to BOTH revenue and cost basis? Or is the rule different for each?

### What Counts as "Koszt Uzyskania Przychodu" (Deductible Cost)
6. Under Art. 22 ust. 14-16 ustawy o PIT (or Art. 30b -- check which), what costs are deductible for crypto:
   - Original purchase price of the crypto being sold?
   - Exchange trading fees?
   - Exchange withdrawal fees?
   - Blockchain network fees (gas)?
   - Fees paid in crypto (e.g., fee deducted in the same token)?
   - VPN or hardware wallet costs?

7. If crypto was received for free (airdrop, staking reward), is the cost basis zero? Or is it the market value at receipt?

8. If crypto was received as payment for services (USDC salary): the cost basis for crypto tax purposes is the PLN value at which it was (or should have been) declared as income?

### FIFO Specifics
9. Does Polish law explicitly mandate FIFO? Or is it just the commonly accepted method? Legal reference?

10. Is FIFO applied per-asset (separate queue for BTC, ETH, USDC, etc.) or across all crypto combined?

11. If the taxpayer held crypto before becoming a Polish tax resident: is the cost basis the original acquisition price (in PLN equivalent), or the market value at the time of becoming a Polish resident?

12. How should cost basis work for crypto that went through a "stablecoin auto-conversion" (e.g., Binance converting BUSD to FDUSD to USDC automatically)?

### Record-Keeping Requirements
13. Art. 30b ust. 6 mentions an "ewidencja walut wirtualnych" (virtual currency register). What must this register contain?

14. What level of detail is required? Per-transaction records? Or just annual totals?

15. Must the register be maintained in real-time, or can it be reconstructed from exchange records when filing?

16. Are exchange-provided CSV exports and trade confirmations sufficient documentation?

17. For how long must records be retained?

## Desired Output

Exact valuation rules with:
- Legal references (article/paragraph level)
- Worked examples showing correct PLN conversion for different transaction types
- List of deductible vs non-deductible costs
- Record-keeping requirements and format
