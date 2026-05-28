# Waldek (Waldemar Łopata) — Joint Liability Strategy

Research and prompt bundle for the strategic question that emerged from
Phase 8 of the asset mapping: now that Waldemar Łopata is identified as
the on-the-ground Kraków operator of GPUcomputer with his own active 17-year
JDG (NIP 7752083995, "WALDEMAR ŁOPATA 3d Kraków"), can he be added to or
attached via the existing 155k PLN claim that currently runs only against
Mateusz Szklarski-Łopata?

## Strategic frame

Mateusz is asset-light and lives in Eindhoven working a factory production
line. Waldemar runs an active Polish JDG out of Kraków with his own
infrastructure. **Without reaching Waldemar, realistic recovery is likely
poor.** Three independent legal routes might reach him:

1. **Joint tortfeasor liability** (KC art. 422 + 441) or implied
   spółka cywilna (KC art. 860 + 864) — put him on the judgment from the
   start as a co-defendant
2. **Actio pauliana** (KC art. 527–534) — attack specific transfers between
   the two JDGs once judgment against Mateusz exists
3. **Criminal co-perpetration** (KK art. 18 + 286) — expand the
   not-yet-filed criminal complaint to include him as suspect; triggers
   art. 291 KPK asset freeze once charges issue

Each has different evidentiary, procedural, and timing tradeoffs. The
existing EPU case (Nc-e 552126/26, filed 2026-04-08, no nakaz yet)
constrains the choice — amending in EPU likely kicks the case to ordinary
procedure and loses the EPU speed advantage.

## Prompt files

| # | File | Purpose | Run via |
|---|---|---|---|
| 00 | `00-joint-liability-research-brief.md` | Comprehensive brief on the legal theories of joint liability (spółka cywilna, art. 422 KC, agency, etc.) | ChatGPT 5.5 Pro, Perplexity Pro, Gemini Deep Research — each independently, then cross-synthesize |
| 01 | `01-epu-amendment-tactical-prompt.md` | Drilled procedural question: can the EPU be amended to add Waldemar, or is a parallel ordinary suit the right move? Time-sensitive | Same three agents — short focused outputs |
| 02 | `02-asset-flow-and-actio-pauliana-prompt.md` | Drilled prompt on actio pauliana and on what counts as a fraudulent transfer between two informally cooperating JDGs | Same three agents |

After each is run through the three agents, the four-output bundle should
be cross-synthesized into a single decision document on the model of
`docs/gpu-computer/crime-law/synthesis-criminal-law-angle.md`.

## What this bundle deliberately does not cover

- **OSINT on Waldemar himself** — already covered by Phase 8 of the
  asset-mapping run. See `docs/gpu-computer/asset-mapping/prompts/results/08-phase8-waldek-partner.md`.
- **Whether the Kazimierza Wielkiego 36/3 property is in the Łopata
  family** — Phase 9 of the asset-mapping run is testing this; results
  will be referenced by the actio-pauliana brief once back.
- **Selection of a specific Kraków lawyer** — separate task. See
  `docs/gpu-computer/followup-lawyer-search.md` for the engagement-side
  workflow.
- **Browser-agent action prompts to gather more evidence on Waldemar** —
  Phase 8 closed at "sufficient evidence" by user instruction. Add only
  if a research output flags a specific evidentiary gap.

## Next steps after research

1. Run each of the three prompts through ChatGPT 5.5 Pro, Perplexity Pro,
   and Gemini 3.1 Deep Research. Save outputs in this directory with
   filenames matching the existing pattern (e.g.
   `Joint Liability Research - ChatGPT 5.5 Pro.md`).
2. Write the cross-synthesis at `synthesis-joint-liability.md` mirroring
   the structure of `../crime-law/synthesis-criminal-law-angle.md`.
3. Take the synthesis and the existing asset-mapping findings to a
   Kraków litigator. The lawyer decides on amendment vs. parallel suit
   vs. actio pauliana sequencing.
