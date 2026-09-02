# DESIGN-NOTE — 01 Shotgun House

## The idea in one line
The page is a shotgun house. You come in off the sidewalk, walk straight back through five
rooms, and end up in the kitchen, which is where the conversation actually is.

## Why a shotgun house is the right container
A shotgun house has no hallway. Every room opens into the next, in a line, and you cannot
skip one. That is the same promise the site is making: there is one way through, it is short,
and nobody is gatekeeping the door. It is also the most ordinary building in New Orleans —
you feel it as a local, not as a visitor. No wrought iron, no beads, no Quarter.

The other true thing about a shotgun: the middle is dark. There are no side windows, so the
only light in the middle rooms comes through the doorways. The house gets dim as you go back,
and then the kitchen is the brightest room in the building because it has a back door. That
is a gift for this brief. The scroll can literally get darker and quieter through the middle
and then open up when you arrive at the Slack.

---

## Seed
A 192-character alphanumeric string. Read as six 32-character chunks. What it decided:

| Signal in the string | Design decision |
|---|---|
| 192 characters, 6 chunks of 32 | Six zones (5 rooms + back step). Base spacing module is 32. Content column is 32rem. |
| Digits sum to **191** | Accent hue **191°** — Gulf South porch-ceiling blue ("haint blue"). Real vernacular, not souvenir. |
| Complement of 191 is **11°** | Primary action hue **11°** — the brick-persimmon of a painted shutter. RSVP is the only thing on the page in this color. |
| 77 uppercase / 77 lowercase / 38 digits | Two typefaces at exactly equal presence, plus a third *style* (not a third font) carrying ~20% of the text: letterspaced small caps for facts. |
| Longest digit run is **66** | Every doorway opening is **66%** of the wall width. Same aperture, five times. |
| Exactly **4 doubled characters** (`kk`, `66`, `oo`, `cc`) | Exactly four interior doorways. Each double is a *pair of the same character*, so each doorway is built as a pair: head casing above, threshold strip below. |
| Gaps between those doubles: 38 / 6 / 27 / 43 / 78 | Doorway rhythm is uneven. Second room is the shortest section on the page; the kitchen is the deepest. You get through the middle fast and then the house lets you stand still. |
| Uppercase density per chunk: 47 / 38 / 44 / 34 / 41 / 38 | Wall paint lightness per room, in order. Room four is the darkest paint in the house — so the kitchen doorway is the single brightest threshold you pass through. |

---

## Palette
Everything is a paint chip or a material. Nothing is a UI color.

```
--ink        #23180F   warm near-black, the color of old cypress trim
--ink-soft   #5A4835
--paper      #F4EADA   front room wall — cream, low west light on it
--putty      #DCCBAD   second room wall
--sage       #AFB8A2   third room wall, a green-gray that gets dim
--umber      #3B2E23   fourth room wall — the dark middle, warm not black
--umber-deep #241C14
--kitchen    #EFF0E4   kitchen wall — the brightest surface in the house
--haint      #9BC4CD   hue 191. porch ceilings, links, small marks
--persimmon  #BA4D34   hue 11. RSVP only.
--cypress    #9A6A3C   floorboards
--yard       #C9CE84   the green-gold coming in the back door
```

Rule: the persimmon appears **twice** on the whole page (RSVP at the top, RSVP in the footer).
The haint blue is the only other accent and it never sits next to the persimmon.

There is no dark mode. Rooms three and four are dark *rooms*, not a dark theme — warm umber
walls with cream ink, the way a room looks at 5:30 in October.

## Light, room to room
1. **Front room** — bright. Low west light through the open front door, raking across the wall.
2. **Second room** — softer, no direct light, warm bounce.
3. **Third room** — dim. The projects sit in it like objects on a table you have to lean toward.
4. **Fourth room** — darkest. The paint is the darkest in the house.
5. **Kitchen** — flooded. Back door open, green light off the yard.
6. **Back step** — outside, evening.

## Type
Two faces, equal weight, per the 77/77 split.

- **Fraunces** (variable, `SOFT` up, `WONK` on) — the date, the room headings, and one spoken
  line per room. It is a Windsor-lineage face; it reads like lettering someone painted on a
  transom, not like a brand font.
- **Libre Franklin** — body, buttons, everything factual. Franklin Gothic lineage: American
  newsprint and neighborhood flyers. Warm, plain, not a tech sans.
- The third voice is a *style*, not a font: Libre Franklin 500 at 0.75rem, 0.16em tracking,
  uppercase — used only for dates, addresses, and the footer. Roughly a fifth of the words.

No monospace anywhere. No third family.

## Architecture of the page
Narrow single column, max 32rem of text inside a 46rem house. Full-bleed on mobile.
Outside the house on desktop is a dark warm neutral: you are looking down the length of it.

Sequence: **front door → room → doorway → room → doorway → room → doorway → room → doorway →
kitchen → back door → back step.**

Each doorway is a full-bleed image band: the current room's wall, a 66%-wide opening dead
center, casing around it, floorboards running through, and the next room's light showing in
the opening. Every doorway is photographed from the same height, dead-on, so the four of them
in sequence read as one continuous walk. The apertures get brighter as you go back, and the
last one is blinding compared to the room it sits in.

Navigation is a small line-drawn floorplan — five rooms in a row — pinned at the edge. It
fills in as you walk. It is the only nav on the page, and it is the "you are here."

## The illustration is removable
If every image were deleted, what survives: a narrow single column; six sections in fixed
order; each section on a flat paint color from the same palette, stepping darker through the
middle and bright at the end; a hairline threshold rule and a 66%-wide gap at every section
break; the same type hierarchy; the kitchen still arriving as the brightest, widest, last
room; RSVP still the only persimmon thing on the page. The metaphor is carried by sequence,
color, and width. The pictures make it physical, they don't make it legible.

## Imagery to generate (Codex CLI)
Deadpan, frontal, unstyled — closer to architectural typology photography than to interiors
editorial. No people, no props, no staging, no lens flare, no vignette. Every image gets the
exact hex codes above in its prompt so the set coheres.

1. Front door, head-on from the sidewalk, transom above, door open, plain lit wall visible
   through the opening (the hero — the invitation is set inside that light).
2. Five wall surfaces, one per room, each with its light already in the image.
3. Cypress floorboards running away from camera.
4. Four doorways, identical framing, increasing light through the aperture.
5. The view out the back door: screen door, back steps, fig and banana, late green light.

Depth comes from layering these on scroll — wall, then floor, then casing — at slightly
different rates, so the doorways have thickness. Reduced-motion turns it off.

## What I am refusing
No eyebrow labels. No cards with borders on the projects — they sit directly on the wall.
No gradients standing in for light; if light is in the picture it was generated as light.
No glow. No hero video. No "features." No stock smiling faces. Nothing that would make a
lawyer in Mid-City think this site was built for programmers.

## The first three seconds
Through the open front door: **Friday, October 2. 5:30pm. New Orleans.** and a persimmon
button that says *Save me a seat*. Invited, happening, here — in that order, in one glance.
