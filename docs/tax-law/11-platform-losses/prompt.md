# Research: Tax Treatment of Losses from Collapsed Crypto Platforms (Celsius, BlockFi)

## Context

The taxpayer had funds locked on two platforms that went bankrupt:

- **Celsius Network**: Filed for bankruptcy in July 2022. The taxpayer had BTC and possibly DOT deposited. Some partial recovery may have occurred through bankruptcy proceedings.
- **BlockFi**: Filed for bankruptcy in November 2022. The taxpayer had BTC deposited.

The taxpayer was a Swedish tax resident when these platforms collapsed, but is now a Polish tax resident. The funds were originally deposited from self-custody wallets or other exchanges.

Known wallet addresses (from wallets.txt):
- Celsius BTC: bc1qvvreqkvs03l86eheelqs8j3wvy6mx2ul0rjz7r
- Celsius DOT: 12cH7rXQPZkwy5KbbNvGqgnmS75CSn1EUjrHno6ymBP9KYUq
- Another Celsius DOT: 15iv67DkPLWdBpFSWz1tzsJfjpz5mgr46sDBpaD6j4zNYyDF
- BlockFi BTC: 3GV34TNcQUS53MimCWd8rMjKLxJF3C6Qoj

## Questions

### Can Losses Be Claimed?
1. Under Polish crypto tax law, can losses from platform bankruptcies be deducted? Is there a legal basis?

2. The crypto was deposited to the platform (transferred from self-custody). At what point does the "loss" occur for tax purposes:
   - When the platform files for bankruptcy?
   - When the platform stops allowing withdrawals?
   - When a court formally declares funds unrecoverable?
   - When partial bankruptcy distribution is received (confirming partial loss)?

3. Is depositing crypto to a custodial platform considered a "disposal" under Polish law? If so, was it already taxed?

4. If the loss occurred in 2022 (while in Sweden), can it be claimed in Poland at all?

### FIFO Implications
5. If BTC was deposited to Celsius and never recovered: should the FIFO lots for that BTC be removed from the tracker? Or kept with zero value?

6. If partial recovery occurred (e.g., received 30% of BTC back from bankruptcy): how should the FIFO lots be adjusted?

7. From a practical standpoint, should the crypto sent to Celsius/BlockFi be treated as:
   a) Still in the FIFO queue (optimistic -- awaiting recovery)?
   b) Consumed/lost (removed from FIFO)?
   c) Something else?

### Documentation
8. What documentation would be needed to claim the loss? Bankruptcy court documents? Platform statements?

9. Is there a specific form or field on PIT-38 for platform bankruptcy losses?

## Desired Output

Clear guidance on whether and how to account for Celsius/BlockFi losses in the Polish tax system, including FIFO implications and any available deductions.
