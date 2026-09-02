# DESIGN-NOTE — AI Friday

Written before any code. Direction, constraints, and the rules that keep three ideas from fighting.

---

## The problem this design has to solve

Three ideas were handed to me at once: a **house** (structure), a **porch** (feeling), and **hand-painted signs** (voice).
Any one of them could eat the page. Run all three at full volume and you get a themed restaurant.

So each gets exactly one job, and is forbidden from doing anyone else's:

| Idea | Its one job | What it is explicitly not allowed to do |
|---|---|---|
| **The house** | Sequence. It orders the page and marks the transitions. | It does not supply mood, and it does not supply color. No shutters, no gingerbread, no cute floorplan diagram. |
| **The porch** | Feeling. It makes the first screen warm and occupied. | It does not persist. It is spent in the first screen and does not follow you inside. |
| **The signs** | Voice. They are the headers and nothing else. | They never appear in body copy, buttons, labels, captions, or decoration. |

### How they hand off

The handoff is **light**, and it runs one direction only.

1. **Porch → House.** The hero is a photograph of a real porch at golden hour. You leave it by walking through the first doorway. After that door, the porch scene is gone for good — no more people, no more sky, no more furniture. What survives the doorway is a single color: **haint blue**, demoted from *sky* to *trim*. Inside the house, haint blue is only ever paint on a door frame, a baseboard, and the door-line. That demotion is the whole handoff. The feeling becomes structure.
2. **House → Signs.** The house decides *where* a sign hangs (one per room, on the wall beside the door you just came through) and *how big*. The house never decides what a sign says.
3. **Signs → Porch.** One exception, and only one: the big painted board on the porch. It is the loudest object on the page and it is allowed to be, because it is doing the porch's job and the signs' job at the same moment — which is the only moment the page can afford it.

If any of the three starts doing a second job, it gets cut back. Notes in NOTES.md on where that happened.

---

## Structure: the shotgun house

A shotgun house is one room deep and several rooms long, with every door in a line. There is no hallway. To reach the back you walk through every room. That is a scroll.

**Six rooms, front to back:**

| # | Room | Section | Light |
|---|---|---|---|
| 1 | Front porch | The invitation | Golden hour tipping into blue hour |
| 2 | Front room | What AI Friday is | Warm lamplight, shutters half-closed |
| 3 | Middle room | What people are building | Cool side light from a window |
| 4 | Back room | What you'll walk away with | Dimmer, evening settling in |
| 5 | Kitchen | Join the Slack | One bright overhead bulb. The brightest room in the house. |
| 6 | Back step | Footer | Outside again. Blue hour. Dark. |

The light is the clock. You arrive at golden hour and leave after dark, which is how a good Friday actually goes.

### The signature: the shot line

Every door in a shotgun is aligned — that is the whole joke the house is named for. So **one vertical line runs the full height of the page at a fixed x-position**, and every doorway aperture is centered on it. Off-center, not middle: the door sits at **3/8 from the left**, content in the 5/8. Real shotguns put the doors to one side.

The line is hairline-thin, haint blue, and it never breaks. It is the only element that touches all six rooms. Scroll and you are tracking down it.

### Doorways are real, not dividers

The transition between rooms is a generated image of an actual door frame — jambs, header, casing, and the next room's light visible through the opening. Two uprights and a lintel. You pass *through* it, which means the next room's color starts inside the aperture and floods out as you scroll. A horizontal rule would have been the lazy version; the point is that a doorway has a thickness and a wall has a far side.

**Room 5 (kitchen) has no doorway before it — it has a screen door.** Different image, brighter light, because you can hear people in there before you get there.

---

## Scene: the porch

First screen only. Golden hour into blue hour. A porch on a New Orleans street, ceiling painted haint blue, a few people already sitting, **one empty chair**, a bare bulb just coming on, music implied from somewhere down the block.

The empty chair is the argument. It is the entire pitch made without a sentence: *there is a seat and nobody is in it.* The RSVP under it says **Pull up a chair**.

Photographic, generated, not illustrated. Not a stock-photo crowd. Three or four people, seen loosely, not looking at the camera, not performing fun. Ordinary evening.

**No French Quarter.** No balconies, no ironwork, no beads, no brass. This is a residential block — clapboard, a fern, a step, a car parked in front. New Orleans as a place people live, not a place people visit.

---

## Type: hand-painted shop signage

**Vernacular: corner store, po-boy shop, laundromat.** Not saloon, not farmhouse, not café. That distinction is real and it lives in the letterform:

- A saloon sign is a **Clarendon slab** with heavy brackets — wanted posters, western. Rejected.
- A farmhouse sign is a **script or a rustic serif**. Rejected.
- A café sign is a **thin geometric or a wobbly hand-script**. Rejected.
- A New Orleans corner-store sign is **American gothic — Franklin Gothic and its cousins** — very bold, slightly condensed, all caps, painted with a brush onto plywood or straight onto the wall, with a hard offset shadow and no blur. That is the alphabet a commercial sign painter actually reaches for.

So:

- **Display / signs — Libre Franklin 800–900, all caps, tight tracking.** Franklin Gothic's open-source descendant. Set on generated painted board surfaces so the brushwork, weathering, and edges are real photographic texture rather than a filter. Hard offset shadow in enamel red, no blur — a sign-painting convention, not a CSS effect.
- **Body — Karla, regular and medium, sentence case, generous leading.** Humanist grotesque with slightly odd terminals. Warm, plain, readable, and pointedly *not* techy. Nothing here says "developer."

Two families. That is all. Weight, case, scale, and the painted board carry the contrast — the way a sign painter got contrast, with one alphabet and a bigger brush.

**Sign sizes step 5 : 4 : 3.** The big porch board, the room signs, the small painted labels. A 3-4-5 triangle is the square a carpenter uses to frame a house, so the signage is proportioned by the same tool that built the walls behind it.

**Where signs are banned:** buttons, body copy, project names, footer, captions, numerals, navigation. If it is not a room header, it is Karla.

---

## Color

Haint blue is primary — the pale blue New Orleans paints porch ceilings, traditionally to keep spirits out and honestly to keep wasps from nesting.

| Token | Hex | Role |
|---|---|---|
| `--haint` | `#A6C6CD` | Primary. Porch ceiling in room 1; door frames, baseboards, and the shot line everywhere after. |
| `--dusk` | `#2C4557` | Blue hour. Body text, the back step, deep shadow. |
| `--lamp` | `#E9A13B` | The bulb. Golden hour. Used sparingly and always as *light*, never as a fill. |
| `--cream` | `#F4EAD8` | Signwriter's ground. Painted board, page paper. |
| `--enamel` | `#B2402F` | Sign-paint red. Lettering shadow and the RSVP. One button, one color. |

**Five colors. No green, no purple, no gold.** Partly because those are the tourist palette and the brief bans them. Partly because a palette with a deliberate hole in it holds together better than one that covers the wheel — the same reason the porch has an empty chair.

---

## Copy

Short, plain, spoken. The reader is a paralegal, a teacher, a restaurant manager. They already suspect this is not for them, so the copy's only job is to remove that suspicion and then get out of the way.

- No "unlock," "empower," "supercharge," "journey," "community-driven."
- No em-dash cadence. Short sentences and periods.
- Sentence case everywhere except signs.
- Say the concrete thing. "Twelve people's availability in ten minutes" beats "streamline scheduling."
- Every line is a placeholder. A human rewrites all of it.

**The first three seconds, in order:**
1. *You're invited* — an empty chair and the words "pull up a chair."
2. *This is happening* — a date on a painted board: Friday, October 2, 5:30.
3. *It's here* — a New Orleans porch you can tell is a New Orleans porch without a single postcard cue.

---

## Motion

Very little, and all of it serves one metaphor: walking.

- Rooms lift and settle slightly as you enter them. That is it.
- Doorway apertures move at a fractionally different rate than their walls, so passing through a door has depth. Small enough that you feel it and do not notice it.
- The sign settles onto the porch once, on load, and never moves again.
- No parallax anywhere else, no counters, no scroll-jacking, no reveal-on-scroll for individual words.
- `prefers-reduced-motion` turns all of it off and the page still works, because the sequence is in the document, not in the JavaScript.

---

## What I am refusing to build

- A dark mode. Anti-goal, and also: the page already gets dark. That is the ending.
- A features grid. The projects are a list on a wall, not cards.
- Eyebrow labels above headings.
- A floorplan diagram, a scroll-progress house icon, or any device that explains the metaphor. If the house needs a legend, the house failed.
- Any texture, surface, or light made from CSS gradients, box-shadows, or filters. Surfaces are photographed. The only shadow in the CSS is the sign painter's hard offset, which is lettering, not lighting.
- A second display face, a third color temperature, or a fourth idea.
