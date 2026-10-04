---
name: Senda España 2050
description: Independent tracker of the 50 España 2050 objectives, drawn as the report's own foresight lines.
colors:
  blue: "#4a8aa9"
  blue-deep: "#23617f"
  blue-ink: "#1f6f93"
  cyan: "#65b7d9"
  graphite: "#3c3c3b"
  yellow: "#ffd300"
  paper: "#ffffff"
  page: "#f4f8fb"
  sky: "#e3eef5"
  sky-line: "#c4d9e6"
  hair: "#dbe5ec"
  ink: "#1d2124"
  ink-2: "#4b5459"
  muted: "#6c767c"
  on-blue: "#ffffff"
  on-blue-2: "#e3f0f6"
  s-enlinea: "#26804a"
  s-senda: "#2f7ea3"
  s-lento: "#e07b39"
  s-lento-ink: "#2b1d10"
  s-retroceso: "#c43d36"
  s-nodata: "#9aa3a8"
typography:
  display:
    fontFamily: "Bebas Neue, Oswald, Arial Narrow, sans-serif"
    fontSize: "clamp(64px, 10.5vw, 148px)"
    fontWeight: 400
    lineHeight: 0.86
    letterSpacing: "0.005em"
  numeral:
    fontFamily: "Bebas Neue, Oswald, Arial Narrow, sans-serif"
    fontSize: "clamp(96px, 14vw, 190px)"
    fontWeight: 400
    lineHeight: 0.78
  headline:
    fontFamily: "Bebas Neue, Oswald, Arial Narrow, sans-serif"
    fontSize: "clamp(34px, 4.6vw, 62px)"
    fontWeight: 400
    lineHeight: 0.92
    letterSpacing: "0.005em"
  title:
    fontFamily: "Bebas Neue, Oswald, Arial Narrow, sans-serif"
    fontSize: "24px"
    fontWeight: 400
    lineHeight: 1
    letterSpacing: "0.03em"
  figure:
    fontFamily: "Bebas Neue, Oswald, Arial Narrow, sans-serif"
    fontSize: "30px"
    fontWeight: 400
    lineHeight: 1
    letterSpacing: "0.01em"
    fontFeature: "tnum"
  body:
    fontFamily: "IBM Plex Sans, Segoe UI, system-ui, sans-serif"
    fontSize: "16px"
    fontWeight: 300
    lineHeight: 1.55
  body-strong:
    fontFamily: "IBM Plex Sans, Segoe UI, system-ui, sans-serif"
    fontSize: "16px"
    fontWeight: 500
    lineHeight: 1.3
  label:
    fontFamily: "IBM Plex Sans, Segoe UI, system-ui, sans-serif"
    fontSize: "12.5px"
    fontWeight: 500
    lineHeight: 1.3
  caption:
    fontFamily: "IBM Plex Sans, Segoe UI, system-ui, sans-serif"
    fontSize: "12px"
    fontWeight: 300
    lineHeight: 1.3
rounded:
  none: "0px"
  flag: "2px"
  cell: "3px"
  pill: "999px"
spacing:
  gutter: "clamp(16px, 4vw, 48px)"
  maxw: "1240px"
  row: "15px"
  col-gap: "14px"
  section: "clamp(40px, 6vw, 72px)"
  chapter-pad: "clamp(26px, 4vw, 48px)"
components:
  chip:
    backgroundColor: "{colors.paper}"
    textColor: "{colors.ink}"
    rounded: "{rounded.pill}"
    padding: "5px 12px 5px 6px"
  chip-pressed:
    backgroundColor: "{colors.sky}"
    textColor: "{colors.ink}"
    rounded: "{rounded.pill}"
  chip-on-blue:
    backgroundColor: "transparent"
    textColor: "{colors.on-blue}"
    rounded: "{rounded.pill}"
    padding: "5px 12px 5px 6px"
  chip-on-blue-pressed:
    backgroundColor: "{colors.paper}"
    textColor: "{colors.ink}"
    rounded: "{rounded.pill}"
  map-cell:
    backgroundColor: "{colors.s-nodata}"
    textColor: "{colors.on-blue}"
    rounded: "{rounded.cell}"
    size: "30px"
  table-head:
    backgroundColor: "{colors.sky}"
    textColor: "{colors.blue-ink}"
    typography: "{typography.label}"
    padding: "10px"
  indicator-row:
    backgroundColor: "{colors.paper}"
    textColor: "{colors.ink}"
    padding: "15px"
  chapter-panel:
    backgroundColor: "{colors.blue}"
    textColor: "{colors.on-blue}"
    padding: "clamp(26px, 4vw, 48px)"
  ficha:
    backgroundColor: "{colors.blue-deep}"
    textColor: "{colors.on-blue}"
    padding: "clamp(20px, 3vw, 34px)"
  flag:
    backgroundColor: "transparent"
    textColor: "{colors.ink-2}"
    rounded: "{rounded.flag}"
    padding: "0 5px"
  formula:
    backgroundColor: "{colors.sky}"
    textColor: "{colors.ink}"
    typography: "{typography.title}"
    padding: "12px 16px"
  tooltip:
    backgroundColor: "{colors.graphite}"
    textColor: "{colors.on-blue}"
    rounded: "{rounded.cell}"
    padding: "8px 11px"
  footer:
    backgroundColor: "{colors.graphite}"
    textColor: "#e9ecee"
---

# Design System: Senda España 2050

## Overview

**Creative North Star: "The Report Reads the Future"**

The site is the 2021 *España 2050* report translated to screen: full-bleed steel-blue fields, white sheets laid on a pale blue page, Bebas Neue capitals for every headline and figure, IBM Plex Sans Light for the reading voice. Its job is foresight, not scoring. Each indicator is a line from 2019 toward 2030, 2040 and 2050, with the yellow senda showing where the country should be and the real trajectory extended to answer "a este ritmo, ¿cuándo llegamos?".

Density is that of a printed indicator table: tight rows, small labels, big condensed numerals, and generous blue chapter panels that set the pace between desafíos. The cover carries an original isometric maze (generated, seeded, in cyan, steel and graphite) clipped on a diagonal, with a single yellow bar crossing the field as the senda. Depth is almost entirely tonal (blue field, white sheet, deep-blue lámina); the system is flat and square.

The world rejects the KPI-tile dashboard: indicators live as rows in a cuadro and open into a deep-blue ficha with a prospective chart, never as floating cards.

**Key Characteristics:**
- Full-bleed steel-blue cover and chapter panels; white sheets with a steel-blue corner bracket.
- Bebas Neue capitals for headlines, giant chapter numerals and all headline figures; Plex Sans 300 body.
- Signal yellow marks the senda, the 2030 destination and the active/focused thing.
- Five fixed status colors, always paired with a distinct icon shape and a label or count.
- Square, flat surfaces; radius only on small interactive tokens.
- Every figure carries its year and source in small Plex beneath it.

## Colors

A report palette: cool steel and cyan fields, graphite ground, one hot signal yellow, and a separate five-step status scale.

### Primary
- **Report Steel Blue** (blue): the cover and every desafío chapter panel, the corner bracket, the scrollbar thumb, the `theme-color`. It is a field color, laid edge to edge.
- **Lámina Deep Blue** (blue-deep): the opened ficha sheet under an indicator row and the knockout stroke behind chart labels.
- **Table Ink Blue** (blue-ink): links, table-head text, row numerals, guide words and section headings on white. In dark mode it lightens to a readable sky tint.

### Secondary
- **Maze Cyan** (cyan): the giant chapter numerals and the top faces of the cover maze. Never body text.

### Tertiary
- **Signal Yellow** (yellow): the senda (cover bar, chart path, the marker in each progress track, meta rings in the chart), the "a 2030?" and "España 2050" emphasis in the headline and wordmark, the ficha status heading on deep blue, the active-cell ring, `:focus-visible` outline and `::selection`.

### Neutral
- **Report Graphite** (graphite): footer ground, tooltip, the maze's shadow faces, the outline around the yellow senda marker.
- **Sheet White** (paper): cuadro and método sheets, the sticky guide.
- **Pale Page** (page): the page behind the sheets.
- **Table Sky** (sky): table head, progress-track rail, formula box, pressed chip, row hover tint.
- **Sky Rule** (sky-line): chip borders, flags, track ticks.
- **Hairline** (hair): row dividers and the guide's bottom rule.
- **Ink / Ink 2 / Muted** (ink, ink-2, muted): primary text, secondary text and sub-labels, year/source captions.
- **On-Blue / On-Blue 2** (on-blue, on-blue-2): text on steel and deep blue; the softer tint for captions and secondary lines on blue.

### Status scale
- **En línea** (s-enlinea) green, check mark. **Al ritmo** (s-senda) blue, diagonal arrow. **Por debajo** (s-lento) orange with dark ink (s-lento-ink) for contrast, right arrow. **Retroceso** (s-retroceso) red, down arrow. **Sin dato** (s-nodata) grey, dash.

### Named Rules
**The Signal Yellow Rule.** Yellow means "the senda, the destination, or the thing you are on": the path, the 2030 emphasis, the active cell, focus and selection. It is never a fill for panels, never a status color, never decoration.

**The Five Statuses Rule.** The five status colors are a closed scale used only for status (map cells, icons, progress bars). Every status mark pairs color with its icon shape and a label or count; color alone never carries meaning.

**The Dark Mirror Rule.** Dark mode keeps the blue fields and swaps the sheets to graphite tones (paper #3c3c3b on page #323231), lightens blue-ink and lifts the status scale; it is a full token remap, toggled by `prefers-color-scheme` or `data-theme`.

## Typography

**Display Font:** Bebas Neue (with Oswald, Arial Narrow)
**Body Font:** IBM Plex Sans (with Segoe UI, system-ui)

**Character:** The report's condensed capitals for anything that should be read as a headline or a number, against a light, even Plex reading voice. Bebas is set at weight 400 only; Plex runs 300 body, 400 UI, 500 emphasis, 600 for the verdict's lead and chip counts.

### Hierarchy
- **Display** (Bebas 400, clamp(64px, 10.5vw, 148px), 0.86): the cover question only. Emphasis is a color change to yellow, never italic.
- **Numeral** (Bebas 400, clamp(96px, 14vw, 190px), 0.78; 88px on mobile): the cyan desafío number in each chapter panel.
- **Headline** (Bebas 400, clamp(34px, 4.6vw, 62px), 0.92): chapter titles; método heading at clamp(38px, 5vw, 60px).
- **Title** (Bebas 400, 22-34px, 1.0, 0.02-0.06em tracking): map heading, ficha heading, guide words, wordmark, formula.
- **Figure** (Bebas 400, 26-30px, 1.0, tabular): row numerals, "hoy" values, "a este ritmo" years, ficha dl values.
- **Body** (Plex 300, 16px, 1.55): reading text; 15-15.5px inside panels; max 62-70ch. The cover verdict runs clamp(18px, 1.7vw, 22px) at 30ch.
- **Body strong** (Plex 500, 16px, 1.3): indicator names, `strong`/`b`.
- **Label** (Plex 500, 12.5px): table head; chips at 13-14px/400.
- **Caption** (Plex 300-400, 11-12px): year · source lines under figures, chart ticks, dt labels.

### Named Rules
**The Bebas Figures Rule.** Every headline number is Bebas: values, targets, years of arrival, numerals. Units sit beside it in small Plex 400 (13px), and the year/source sits beneath it in 12px Plex muted. Only "%" stays glued to the number.

**The Light Voice Rule.** Running text is Plex Sans 300; emphasis steps to 500, not to a second face or italic.

## Layout

A single column of full-bleed bands and centered sheets. Content width is 1240px (maxw) with a fluid gutter of clamp(16px, 4vw, 48px).

- **Cover:** full-bleed steel blue. Maze strip (clamp(120px, 17vw, 250px) tall, clipped by a diagonal polygon) under the top bar; then a two-column grid (1fr / 1.08fr): headline and verdict left, 50-cell map right. Collapses to one column at 1020px, where the yellow senda bar widens to cross the full field.
- **Sticky guide:** a white bar pinned to the top (58px min) naming the desafío and objective range in view, with status filter chips at right.
- **Desafío:** full-bleed blue chapter panel (numeral column + title/counts), then a white cuadro sheet at maxw with a corner bracket, starting clamp(16px, 2.4vw, 28px) below. Sections are spaced clamp(40px, 6vw, 72px).
- **Cuadro grid:** eight columns (46px numeral, 2.4fr name, 1.15fr hoy, .8fr meta, minmax(150px, 1.4fr) progress track, 1fr estado, 1.05fr ritmo, 22px chevron), 14px gaps, 15px row padding. At 860px it becomes a named-area card per row (numeral left; name/chevron, hoy + meta, track, estado/ritmo stacked), and the meta column folds into the hoy line.
- **Ficha:** two columns (1.25fr chart / 1fr text) on deep blue; one column under 860px, its four-figure dl dropping to two.
- **Método and footer:** two-column grids collapsing to one at 860px.

## Elevation & Depth

Flat. Depth is tonal: steel-blue field, white sheet on a pale page, deep-blue lámina under an opened row. Only two things float, and only they cast shadows.

### Shadow Vocabulary
- **Guide shelf** (`box-shadow: 0 6px 16px -14px rgba(10, 40, 60, .5)`): the sticky guide over scrolling content.
- **Tooltip lift** (`box-shadow: 0 8px 20px -8px rgba(0,0,0,.4)`): the map-cell tooltip.

### Named Rules
**The Flat Sheet Rule.** Panels, sheets, rows, chips and cards never cast shadows. A surface separates by color and hairline, or it does not separate.

## Shapes

Square by default: bands, sheets, chapter panels, ficha, formula box and table head have no radius. Radius is reserved for small interactive tokens: map cells (3px), flags (2px), tooltip (3px), chips (pill). The active map cell is marked by a yellow ring (circle, 2.5px) offset 6px around the square.

The recurring silhouette is the **report corner**: a 26px L-bracket of 7px steel-blue strokes at the top-left of every white sheet. The cover's diagonals (maze clip, the -3.5deg yellow bar) are the only angled forms.

## Components

### Status Icon
A 20-unit circle filled with the status color and a white 2.2-stroke round-capped mark (check, diagonal arrow, right arrow, down arrow, dash); the Por debajo mark uses dark ink. Sizes 16px (guide, chapter counts) and 18px (rows, legend). On blue grounds the disc gets a 1.5px white or on-blue ring.

### Chips (status filters)
- **Style:** pill, 1px sky-line border, white ground, Plex 400 14px; leading status icon, label, then a 600 tabular count. 13px and tighter in the guide.
- **State:** hover darkens the border to steel blue; pressed (`aria-pressed`) fills sky with a steel-blue border and 500 weight. On the blue cover they invert: transparent with a 55%-white border, pressed fills white with ink text.
- **Mobile guide:** under 860px the guide chips collapse to icon + count, the label kept as visually hidden text, and "Ver todos" is dropped.
- **Clear:** "Ver todos" is an underlined blue-ink text button, shown only while a filter is active.

### Map Cell (signature)
A 30px square (27px mobile, 3px radius) filled with its status color, the objective number in Plex 500 11.5px, a 1.5px inset white ring. Hover lifts 2px; non-matching cells dim to 16% under a filter; the active cell gets the yellow ring. Cells sit in rows by desafío behind a white Bebas desafío numeral. A graphite tooltip names the objective on hover and focus.

### Cuadro (indicator table)
White sheet with corner bracket; sky table head in blue-ink label type; rows separated by hairlines, hover tints sky at 55%. Each row is a disclosure (`details`) with a rotating chevron (90deg, 0.3s ease-out).

### Progress Track (signature)
Domain -100% to +150% of the way to 2030. A 6px sky rail spans 0 to 100% between two sky-line ticks; a 6px bar in the status color runs from 0 to current progress (leftward when negative); the senda marker is a 6 by 22px yellow block with a 1.5px graphite outline. Out-of-domain values print as an 11px percentage at the track end.

### Ficha and Prospective Chart (signature)
Deep-blue lámina: chart left, text right. The chart (560 by 250 viewBox) draws faint white gridlines, the yellow senda (4px) through yellow-ringed meta points at 2030/2040/2050, the real trajectory in white (3px, drawn on open over 0.9s) and its dotted extension (2/6 dash, fades in after 0.7s), a white "hoy" rule, and value labels knocked out with a deep-blue paint-order stroke. The text column opens with the status in yellow Bebas, then a four-figure dl on 22%-white rules, then plain-language paragraphs, note, source link and alternates. Animations are off under reduced motion.

### Chapter Panel
Full-bleed steel blue; giant cyan numeral bottom-aligned beside the Bebas title; status counts with icons in Plex 400 15px; a "Avanza más / Va peor" line in on-blue-2.

### Navigation
Top bar on the cover: Bebas wordmark (26px, 0.06em) with "España 2050" in yellow, Plex 400 15px links in white, underline on hover. Links elsewhere are blue-ink with 1px underline at 3px offset, thickening to 2px on hover. Focus everywhere is a 3px yellow outline at 2px offset.

### Flags
Inline 11.5px Plex tags ("Dato aproximado", "Otra fuente", "Reescalado a la base") with a 1px sky-line border and 2px radius, under the indicator name.

## Do's and Don'ts

### Do:
- **Do** lay the steel blue (#4a8aa9) edge to edge for the cover and every chapter; put detail on white sheets at 1240px with the 7px corner bracket.
- **Do** set every headline figure in Bebas with its unit in small Plex and its year and source beneath it.
- **Do** keep yellow (#ffd300) for the senda, the 2030 destination, the active cell and focus.
- **Do** pair every status color with its icon shape and a label or count, including on mobile where labels become visually hidden text.
- **Do** open indicator detail into the deep-blue ficha with the prospective chart: senda in yellow, reality in white, extension dotted.
- **Do** remap all tokens for dark mode rather than overriding components one by one.

### Don't:
- **Don't** render indicators as separate KPI tiles or cards; they are rows in a cuadro.
- **Don't** use yellow as a status color, a panel fill or decoration.
- **Don't** add shadows to sheets, rows, chips or panels; only the sticky guide and tooltip float.
- **Don't** round sheets, bands or panels; radius belongs to cells, flags, tooltip and pills only.
- **Don't** italicize display type; emphasis in Bebas is a color change.
- **Don't** use the Government of Spain coat of arms, ministry or ONPE logos, or the official "ESPAÑA 2050" logotype; the maze is the project's own generated illustration.
