Read CLAUDE.md first.

Build the AI Friday homepage combining three ideas into one design. This is the ambitious one and it may not work. Try it anyway.

Structure: a shotgun house. One long vertical scroll where each section is a room in the order you'd walk through one: front room (the invitation), middle rooms (what AI Friday is, what people are building, what you'll walk away with), kitchen at the back (the Slack), back step (footer). Doorways are the transitions. Scrolling should feel like walking through the house.

Scene: the front room is a front porch on a warm, lively evening. Golden hour into blue hour, a few people already there, an empty chair, music from down the block. The RSVP is "pull up a chair." Haint blue, the pale blue of the city's porch ceilings, is the primary color. As you move deeper into the house the light changes and the scene gives way to the rooms.

Type: hand-painted shop signage for headlines only. Corner store, po-boy shop, laundromat vernacular; not saloon, not farmhouse, not café. One big painted sign at the front announces the next meetup. Each room's header is a smaller sign. Everything else is a clean, quiet sans-serif.

The risk here is clutter: three ideas fighting for attention. Resolve it by giving each idea one job. The house is the structure and nothing else. The porch is the feeling and lives mostly in the first screen. The signs are the voice and appear only as headers. If any of them tries to do more than its job, cut it back. Explain in DESIGN-NOTE.md how the three hand off to each other, and in NOTES.md what fought with what.

Imagery to generate: the porch scene, the architectural surfaces, the painted signs.

Follow this procedure:
1. Generate a long, random alphanumeric string using a shell script. Use it as inspiration for every decision the brief doesn't already make. Look beyond the surface for subpatterns, special numbers, anything that inspires you. Don't reveal the string in the design.
2. Write DESIGN-NOTE.md defining the creative direction before writing any code.
3. Generate the imagery with the Codex CLI as described in CLAUDE.md. Do not fake textures, light, or surfaces with CSS gradients, box shadows, or filters.
4. Build it. Verify frame-by-frame in the browser at mobile and desktop widths.
5. Screenshot, write NOTES.md, and stop.

The first three seconds should say: you're invited, this is happening, it's here.
