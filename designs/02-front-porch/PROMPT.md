Read CLAUDE.md first.

Build the AI Friday homepage as a front porch on a warm, lively evening.

Not a party. A porch where a few people are already sitting, someone's laughing, there's music coming from somewhere down the block, and there's an empty chair waiting for you. Golden hour tipping into blue hour. The whole page is that scene, and the interface is hospitality: the RSVP is "pull up a chair," the Slack is "come by anytime," the meetup is something you're invited to, not something you register for.

Local detail to build around: haint blue, the pale blue that porch ceilings are painted across the city. Make it the primary color. It's distinctive and quiet and locals will recognize it without a single cliché. Pair it with the warm colors of evening light, wood, and whatever is in people's glasses.

The imagery must be photographic or painterly. No vector illustration, no flat icons. The porch should feel like a real place with real light. Lively means people, movement, warmth. It does not mean a crowd, beads, or a bar.

Generate the hero image first and let it dictate the palette and composition of everything below it. Generate supporting imagery for the other sections only where it adds warmth; empty space is fine on a porch. The page needs a real system beneath the scene: consistent type, spacing, and components that carry the same warmth without the photo doing all the work.

Seed-string decisions: secondary palette, type pairing, exact time of evening, style of the house, what's on the table, how the sections are arranged on or around the porch.

Follow this procedure:
1. Generate a long, random alphanumeric string using a shell script. Use it as inspiration for every decision the brief doesn't already make. Look beyond the surface for subpatterns, special numbers, anything that inspires you. Don't reveal the string in the design.
2. Write DESIGN-NOTE.md defining the creative direction before writing any code.
3. Generate the imagery with the Codex CLI as described in CLAUDE.md. Do not fake textures, light, or surfaces with CSS gradients, box shadows, or filters.
4. Build it. Verify frame-by-frame in the browser at mobile and desktop widths.
5. Screenshot, write NOTES.md, and stop.

The first three seconds should say: you're invited, this is happening, it's here.
