# DESIGN-NOTE — AI Friday

## The one-line direction

A corner store that happens to be about AI. The signs do the talking; the rest of the
page is a clean sheet of paper taped to the wall next to them.

## What the vernacular actually is

Not a saloon, not a farmhouse, not a chalkboard. The reference is the **neighborhood
grocery on a New Orleans corner**: a painted board bolted over the door with the name on
it, a smaller board underneath with today's fact, and a price list in the window where
the numbers were hand-lettered by whoever owned the place. Enamel paint on wood, over a
plaster wall that has been repainted six times. The lettering is confident and slightly
irregular. The drop shadow is a second pass of paint at a hard offset, never a blur.

Three things that keep it honest:
- **The shadow is opaque and offset, never soft.** A sign painter loads a brush; they
  don't render a Gaussian.
- **Nothing is level.** Signs are mounted by a person on a ladder. Half a degree off is
  correct; three degrees is a costume.
- **Wear is at the edges and the bolts**, where weather and hands actually get to it, not
  sprayed evenly over the face like a filter.

## Seed-string decisions

A 128-character random string was generated and read for structure. What it decided:

- **107 letters to 21 digits (~1:6).** That is the discipline metric for the whole page:
  roughly one line in six is painted lettering. Everything else is quiet sans. If the
  ratio creeps up, the page is over-lettered and gets cut back.
- **56 uppercase to 51 lowercase — nearly even, uppercase slightly ahead.** Signs are
  all-caps and get the visual weight; body copy is sentence case and gets the volume.
  Neither wins outright.
- **Exactly two doubled letters in 128 characters (JJ, XX).** A doubled letter *is* a
  painted drop shadow. So: the drop shadow is a hard two-color offset, and it appears in
  exactly two places on the page — the hero sign and the specials sign. The other signs
  are flat with an outline only.
- **The digit gaps run 13, 2, 2, 8, 25, 3, 4, 3, 2, 2, 12, 23, 1, 7 …** — tight pairs
  separated by long empty stretches, with two very long gaps (25 and 23). That is the
  layout rhythm literally: **clusters of three or four short items, then a long quiet
  run of prose with nothing in it.** Two of those quiet runs are the longest blocks on
  the page.
- **3 and 5 tie as the most frequent digits (four each).** Three enamel colors, five
  values total. Three items in the takeaway list, and the run-of-show reads in
  half-hour and 30-minute steps.
- **Digit sum 95, first digit 3, last digit 9.** Base type size 18px, scale steps at
  15 / 18 / 21 / 26 / 34 / 46. Sign rotations come off the digit stream in tenths of a
  degree: -0.3°, +0.6°, -0.5°, +0.3°.

## Palette — enamel

Three enamels and two neutrals. These are the intent going into generation; the hero
sign is generated first and the final tokens are sampled from it, so the CSS matches the
paint rather than the paint matching the CSS.

| token | sampled | where it came from |
|---|---|---|
| `--red` | `#8e1512` | The hero board's painted ground. |
| `--navy` | `#033671` | The date band across the hero. |
| `--blue` | `#0241a2` | The brighter cobalt on the section slats. Links and the schedule times. |
| `--ochre` | `#e7a533` | "NEW ORLEANS" on the hero, and the SPECIALS lettering. |
| `--bone` | `#e3d5b8` | The cream the letters are filled with. |
| `--wall` | `#e4dac0` | Average of the generated plaster wall. |
| `--soot` | `#1f2228` | The painted drop shadow. Not #000. |

Every value above was pulled out of the generated images with an eyedropper after
the fact. The CSS matches the paint; the paint did not match a CSS spec.

Explicitly not in the palette: purple, kelly green, and metallic gold, in any
combination. That trio is the tourist tell. Ochre earns its place because it is the
color of a price board, and it is used in exactly two places.

## Surface

Two materials, and only two.

1. **The wall** — flat chalky painted plaster, sun-bleached bone, rolled over older
   paint. It runs the full page. It is deliberately quiet: it has to hold body copy at
   18px with plenty of air without fighting it.
2. **The board** — painted wood with grain, chipped edges, and visible bolt heads. Only
   the signs and the two panels are board.

Wood over brick. The corner groceries in this city are wood buildings; brick reads
warehouse, and warehouse reads tech office.

## Type

**Display: generated painted lettering.** Not a font.

**Text: Libre Franklin**, one family, three weights (400 / 500 / 700). Franklin Gothic is
the American vernacular grotesque — the lineage that sign shops copied out of catalogs
for eighty years. Using its descendant for the body means the quiet text is a distant
relative of the loud text instead of a contrast for its own sake. It also has the plain,
slightly awkward, non-corporate quality this needs. One webfont family total.

## Images vs. live text — and why

Split by how often the copy changes:

- **Fully generated images:** the hero sign and the four section signs. There are two
  hero signs, a wide 3:1 board for desktop and a squarer 4:3 board for phones, swapped
  with `<picture>`. A 3:1 sign shrunk to 335px reads as a badge, not as something hanging
  over a door, and the first three seconds are the whole job. Short, stable,
  all-caps copy that must be unmistakably hand-painted. Real HTML text ships alongside
  them for screen readers and for when images fail.
- **Generated surface, live text on top:** the run-of-show board and the specials panel.
  This copy changes every month, and the owner has to be able to edit it in the HTML
  without regenerating anything. Critically, the live text on those boards is set in
  Libre Franklin, *not* dressed up to look painted — a sans-serif price list on a painted
  board is what the real thing looks like. Nothing on this page fakes a brush.
- **Generated background:** the wall.

No CSS gradient, box-shadow, or filter is used to simulate paint, light, wear, or
material anywhere on the page.

## Layout rhythm

Following the digit gaps:

```
  ┌──────────────────────────────────────────────┐
  │            [ H E R O   S I G N ]             │   loud
  │   AI FRIDAY / FRI OCT 2 · 5:30 / NEW ORLEANS │
  │   one plain line + RSVP        [ run of show │
  │                                  price board]│
  ├──────────────────────────────────────────────┤
  │  [what this is]                              │
  │  one column of prose, 56ch, nothing in it    │   long quiet run  (gap 25)
  ├──────────────────────────────────────────────┤
  │  [SPECIALS]                                  │
  │  ┌ board ────────────────────────────────┐   │
  │  │ item · who · one line                 │   │   tight cluster of 4  (2,2)
  │  │ item · who · one line                 │   │
  │  └───────────────────────────────────────┘   │
  ├──────────────────────────────────────────────┤
  │  [what you get]                              │
  │  three short things, close together          │   tight cluster of 3
  ├──────────────────────────────────────────────┤
  │  [the slack]  one paragraph, one button      │   long quiet run  (gap 23)
  ├──────────────────────────────────────────────┤
  │  footer, small, plain                        │
  └──────────────────────────────────────────────┘
```

On mobile the signs shrink but never crop, and the run-of-show board moves under the
hero rather than beside it. The wall keeps running.

## Signature element

**The run of show, set as a price board.** Times down the left in a column, leader dots,
items on the right — the thing in the window that tells you exactly what you are walking
into at 6:15 before you commit to walking in at 5:30. It is the piece of the page that
answers "this isn't for me" with a schedule instead of a reassurance.

## The first three seconds

Sign says **AI FRIDAY, NEW ORLEANS** — it's here.
Sign says **FRI OCT 2 · 5:30** — this is happening.
One plain sentence under it says you don't need to write code — you're invited.

## What is deliberately absent

No dark mode. No monospace. No feature grid. No eyebrow labels. No cards with borders
around every paragraph. No icons. No gradient anywhere. No second display font. No beads,
no fleur-de-lis, no wrought iron, no jazz.


## Built, and what changed on contact

Four things only showed up once it was in a browser:

1. **The wall tiled with a visible horizontal seam.** Fixed by mirroring the generated
   plaster into a 1800px tile, so the join has nothing to line up against.
2. **At 74rem the page had a dead right half.** Pulled to 62rem. The quiet runs are still
   quiet, but now they read as margin rather than as an unfinished layout.
3. **Every sign was the same width, so "SPECIALS" had much larger letters than
   "WHAT THIS IS".** Now each board's width is set by its letter count, which is how a
   sign shop cuts a board, and the painted cap-height matches across all four.
4. **The maker credits were set in letterspaced caps and read as template eyebrow
   labels.** Now plain sentence case.
