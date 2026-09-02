# DESIGN-NOTE — AI Friday

## The scene

7:15 p.m. on a Friday in early October. The sun went down at 6:49, so the west end
of the street still has satsuma in it and everything else has already gone blue.
A double shotgun in the Bywater, chalky pale-yellow clapboard, shutter-green
shutters, a deep full-width porch on four turned columns. The beadboard ceiling is
painted haint blue. One bare warm bulb just came on. Four people on the porch,
mid-conversation, one of them laughing. A round enamel table with a sweating
pitcher of iced tea, mismatched glasses, a bowl of satsumas, a notebook.

And one empty chair, turned slightly out toward the steps.

That chair is the whole brief. You're invited, it's happening, it's here.

## What the seed decided

A 192-character random string set the calls the brief left open. The readings I used:

- **Time of evening.** The digit stream carries `1915` — 19:15. Twenty-six minutes
  after sunset on October 2 in New Orleans. Golden hour has tipped; blue hour has
  landed but hasn't finished. Every image is lit at that exact minute.
- **Type scale.** The digits sum to 142 → **1.414** (√2) for the display steps, and
  the literal run `1125` → **1.125** for the text steps. A dual-ratio scale: quiet
  through the reading sizes, dramatic at the top.
- **Circles.** The digit stream opens `314`. The porch table is round, and it's the
  only round thing on the page.
- **Three doubled letters** (`pp`, `JJ`, `zz`) → exactly three photographs beyond the
  hero. No more. Empty space is fine on a porch.
- **House.** A *double* shotgun rather than a single: two front doors, one shared
  porch. The building itself is the argument that there's room for one more.

## Colour — haint blue is the ground, not an accent

The obvious move is a cream page with a warm accent. That's the default, and it
would make haint blue a decorative swatch. Instead the **page itself is the porch
ceiling**: pale haint blue is the field you read on top of, top to bottom, and the
warm colours are the light falling on it.

| token | value | what it is |
|---|---|---|
| `--haint` | pale chalky blue | the ceiling. The page ground. |
| `--haint-deep` | dusty blue | rules, quiet type, the second button |
| `--porch-paint` | warm chalky off-white | clapboard. Reading panels and the invitation card. |
| `--satsuma` | ripe orange | the sky at 7:15 and the one primary action |
| `--shutter` | dark blue-green | shutter paint. All body type, and the night footer. |
| `--cypress` | warm mid-brown | porch decking. Hairlines, captions, small print. |

No black, no pure white. Nothing purple, gold, or Mardi Gras. Exact hexes get
sampled off the hero once it exists — the photo sets the palette, not the other way
around.

## Type

Two families, six styles total. Nothing technical, nothing monospaced.

- **Newsreader** for display and for the invitation. A low-contrast bookish serif
  with a real italic — it reads like a printed invitation, not like a fashion
  masthead. Set light and large. The italic carries the asides.
- **Work Sans** for body, labels, and buttons. Plain, friendly, unfussy. The voice
  of somebody talking to you on a step, not a brand talking at you.

Scale: 17px base. Text 13.4 / 15.1 / 17 / 19.1 (×1.125). Display 24 / 34 / 48 / 68 / 96 (×1.414).
Spacing: 4px base — 4, 8, 12, 16, 24, 32, 48, 64, 96, 144.
Radius: 3px everywhere. Painted wood and paper have edges. No pills, no glow, no cards-within-cards.

## The signature: the invitation card

One memorable object. Sitting over the hero photograph is a small warm-white card
with the date set large in Newsreader, the time and place underneath, and the two
actions on it. It reads as a physical thing somebody left on the empty chair for
you. It's where all the boldness is spent; everything below it is quiet.

## How the sections sit on the porch

The page is a slow walk from the sidewalk to the door.

```
  ┌──────────────────────────────────────┐
  │  HERO — from the bottom of the steps │  full-bleed photo, 7:15pm
  │        ┌───────────────┐             │  the invitation card sits low-left
  │        │ FRI  OCT 2    │             │  Pull up a chair / Come by anytime
  │        │ 5:30pm · NOLA │             │
  │        └───────────────┘             │
  ├──────────────────────────────────────┤
  │  THE TOP STEP — what this is         │  haint ground, type only, wide margins
  ├──────────────────────────────────────┤
  │  THE TABLE — what people are making  │  one photo of the tabletop + 4 entries
  │  ── no card grid. Rules and names.   │
  ├──────────────────────────────────────┤
  │  THE THRESHOLD — what you leave with │  3 things, big serif numerals, no icons
  ├──────────────────────────────────────┤
  │  THE CEILING — come by anytime       │  full-bleed haint beadboard + bulb
  │                                      │  the Slack invitation
  ├──────────────────────────────────────┤
  │  THE SIDEWALK — footer, later, dark  │  shutter green, contact, socials
  └──────────────────────────────────────┘
```

Four photographs total: the porch, the table, the ceiling, the empty chair at the
end of the night. All photographic, all lit at 7:15, all generated — no CSS
standing in for light or surface.

## Voice

Hospitality, not registration. "Pull up a chair," not "Register now." "Come by
anytime," not "Join our community." Short lines, plain verbs, second person. Never
explains what AI is. Never suggests you need to already know anything.

## Anti-goals, held

No dark mode, no monospace, no terminal. No feature grid, no pricing rhythm, no
eyebrow labels, no gradients, no glow. No beads, no fleur-de-lis, no jazz, no masks,
no purple-green-gold, no Bourbon Street, no French Quarter. This is a house
somebody lives in, on a street where people know each other.
