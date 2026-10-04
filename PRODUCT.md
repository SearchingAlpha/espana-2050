# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

## Stack

Astro (chosen by the user), static output, published on GitHub Pages from a public repository (GitHub account SearchingAlpha).

## Users

General public in Spain interested in public policy, without technical or statistical training. They arrive wanting a plain answer to "is Spain on track with the goals it set itself?" and then drill into the topics they care about (education, jobs, climate, housing).

## Product Purpose

Independent tracker of the 50 quantified objectives in the report *España 2050: Fundamentos y propuestas para una Estrategia Nacional de Largo Plazo* (Oficina Nacional de Prospectiva y Estrategia, May 2021). For each indicator it compares the latest official data point with a straight-line path from the report's starting value (taken as 2019) to its 2030 target, and classifies it. Success: a citizen understands in seconds how the country is doing overall and can see, for any indicator, where it stands, how it moved, and where the number comes from.

## Positioning

No official or public follow-up of all 50 España 2050 indicators exists. This site is the only one that re-measures every indicator against the report's own definitions, with each data point sourced, and says plainly where the comparison is approximate.

## Operating Context

- Source report: `lamoncloa.gob.es` PDF (678 pages); indicator table on pp. 44-47 and definitions in the annex.
- Data: Eurostat API, INE, OECD (incl. PISA 2025), MITECO, REE, IMSERSO, FUNDAE, MIVAU, Eurobarometer. Collected 2026-10-04.
- Data is refreshed manually by re-running the scripts in `scripts/` and rebuilding; not live.

## Capabilities and Constraints

- 50 indicators across 9 challenges ("desafíos"); some have sub-parts (PISA subjects, company sizes, age bands) and some have alternative data rows.
- Statuses (user-confirmed wording rule: never say a goal is "cumplida/met", because 2050 has not arrived):
  - progress ≥ 100% of the way to the 2030 target → "Meta 2030 en línea" (already at the 2030 level)
  - progress ≥ expected for the data year → on pace
  - progress > 0 but below expected → behind pace
  - progress ≤ 0 → stalled or going backwards
- Comparability flags per data point: exact / approximate (proxy) / different source; rescaled values when the series was revised.
- Must not present itself as an official government product.

## Brand Commitments

- Visual identity must follow the original *España 2050* report (user instruction).
- Independent and unofficial: do not use the Government of Spain coat of arms, ministry or ONPE logos, or the official "ESPAÑA 2050" logotype; state independence clearly.
- Language: Spanish.

## Evidence on Hand

- `data/resultado.json`: 63 data rows with value, year, source URL, comparability and notes.
- `data/datos_A..D.json`: raw research per challenge group.
- `scripts/analisis.py`, `scripts/build_data.py`: classification and page-data build.
- No testimonials, endorsements, or institutional backing exist; never imply any.

## Product Principles

1. Plain answer first, detail on demand.
2. Every number carries its year and its source.
3. Say where the comparison is weak; never overstate.
4. Reaching a 2030 level early is not "achieving" the goal; wording stays honest about time.
5. Independent, not official.

## Accessibility & Inclusion

Audience is general public: readable at phone width, status never conveyed by color alone, works in light and dark, keyboard operable.
