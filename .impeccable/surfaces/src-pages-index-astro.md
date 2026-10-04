---
version: 1
slug: "src-pages-index-astro"
primary_target: "src/pages/index.astro"
related_targets: []
---

# Surface: página principal (src/pages/index.astro)

Scope: the single public page of the tracker. Visitor mode: Operate (scan status, find a topic, open an indicator), with Read passages for method.
Audience: general public in Spain; job: learn whether Spain is on track with España 2050 and drill into a topic.
Proof/content: data/resultado.json (50 indicators, 63 rows), every value with year + source.
Constraints: unofficial (no government logos/logotype); status wording "Meta 2030 en línea / Al ritmo previsto / Por debajo del ritmo / Estancado o retroceso"; Spanish; static Astro on GitHub Pages.

## Direction contract

THESIS: Foresight, not a scoreboard. Each indicator is read the way the report reads the future: a path from 2019 to 2030/2040/2050, the yellow line marking the senda, and the real trajectory extended to answer "a este ritmo, ¿cuándo llegamos?". Refuses the KPI-tile dashboard.
OWN-WORLD: the España 2050 report translated to screen: steel blue #4a8aa9 fields, cyan #65b7d9, graphite #3c3c3b, signal yellow #ffd300 reserved for the senda; white pages with blue corner brackets; Bebas Neue uppercase display and numerals, IBM Plex Sans Light/Medium body; full-bleed blue chapter panels per desafío with a giant Bebas numeral; light-blue table headers like the cuadro de indicadores.
STORY: the visitor sees the country's verdict and the 50-cell map, picks a desafío or a cell, reads each indicator's line, believes it because every number carries year and source, and leaves knowing which areas are late.
FIRST VIEWPORT: full-bleed steel-blue field. Left: Bebas headline "¿Llega España a 2030?" at display scale, one-line plain answer in Plex below. Right/below: numbered 50-cell map (1-50, grouped by the 9 desafíos, cells filled by status, legend with counts) drawn on the blue like the cover's maze grid, a single yellow rule crossing the field as the senda. The primary action is the map itself: each cell jumps to its ficha.
FORM: report-as-foresight instrument (grounded list position 6; seed e50eef9d). Raises: numbered-cell catalog grid mapped 1:1 to entries with circled active state (from the convention-catalog challenger, declined); guide words in a sticky head naming the desafío and indicator range in view (from the lexicon challenger, declined).
FINISH: unreviewed and undocumented is unfinished; this build ends with the finish review, the verdict, DESIGN.md, and every shipping raster carrying its provenance
