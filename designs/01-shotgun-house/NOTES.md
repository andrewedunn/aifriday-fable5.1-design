# NOTES

I built the page as an actual walk: a narrow column of five rooms with a photographed doorway
between each one, and the light dropping as you go back until the kitchen door opens and the
whole thing brightens. A 192-character seed string set the decisions the brief left open — the
digits sum to 191, which I read as hue 191° and turned into the haint-blue accent, with its
complement at 11° reserved for the two RSVP buttons; the four doubled characters in the string
became the four interior doorways, and the uneven gaps between them became the room depths, so
the second room is the shortest section on the page and the kitchen is the deepest. Everything
material was generated with the Codex CLI as photographs rather than faked in CSS: five wall
surfaces, four doorways shot from the same height so they read as one continuous walk, the
front door from the sidewalk, and the view out the back. I graded each doorway's near wall onto
the exact colour of the tiled wall it butts against, using a curve that lifts midtones without
clipping, so the seam between photo and wall disappears and the kitchen aperture can blow out
without going pure white. Verification was frame-by-frame in a headless browser at six viewport
sizes, plus scripted checks: that the RSVP clears the fold everywhere (it failed at 1280×800 and
375×667 until I made the hero height viewport-aware), that every text colour passes AA against
the wall behind it (one attribution line failed at 4.23:1, fixed), that the parallax actually
moves and stops under `prefers-reduced-motion`, and that the structure survives with every image
blocked — with the photographs gone you still get the narrow column, five rooms stepping through
cream, putty, sage, umber and kitchen-white, and a 66%-wide aperture of the next room's colour at
each threshold. Two bugs the screenshots caught that reading the code would not have: the wall
tiles were rendering at roughly three times the texture scale of the photographs, and the mobile
floorplan bar collapsed to zero height because its span went inline.

**What I'd do next.** The thresholds are the honest cost of this idea — the page is ten screens
at desktop, and four of them are doorways, so I'd test whether people actually walk it or bail
after room two, and be ready to shorten doorways two and three further. The dark surround on
desktop is doing less work than it should; I'd either narrow the house and treat the outside as
a real material, or let the walls bleed full-width and keep only the text narrow. The floorplan
nav is the piece I'm least sure of — it earns its place as the only navigation and the "you are
here," but it's also the one element a non-technical visitor might not read as clickable, so it
wants a hover state and probably a label that persists. I'd also shoot a second front-door frame
so the hero doesn't have to be cropped so tightly on phones, and get real venue copy in, since
"Venue TBD" is currently carrying weight the design shouldn't have to absorb.
