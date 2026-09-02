Read CLAUDE.md first.

Build the AI Friday homepage as a shotgun house.

The page is one long vertical scroll, and every section is a room, in the order you'd actually walk through one from the street:

- Front room: the invitation. Next meetup date, place, RSVP. This is the first thing you see through the front door.
- Second room: what AI Friday is.
- Third room: what people are building.
- Fourth room: what you'll walk away with.
- Kitchen, at the very back: the Slack. That's where the real conversation happens, and it's the last room in the house.
- Back step: footer.

Doorways are the section transitions. Scrolling should feel like walking through the house, not paging through a website. Go literal: illustrate the architecture, the thresholds, the changing light as you move deeper in. This is the bold version and I want to see it. But the structure must still work if the illustration were removed: the narrow single column, the sequence of rooms, and the sense of arriving at the kitchen should survive on their own.

Seed-string decisions: exact palette, type pairing, how the light changes room to room, wall texture, the rhythm of the doorways.
Imagery to generate: doorframes, floorboards, wall texture, the view out the back door. Consider layering images with subtle depth or parallax so the rooms feel physical.

Break the rules of what a homepage looks like, but it still has to work as a homepage.

Follow this procedure:
1. Generate a long, random alphanumeric string using a shell script. Use it as inspiration for every decision the brief doesn't already make. Look beyond the surface for subpatterns, special numbers, anything that inspires you. Don't reveal the string in the design.
2. Write DESIGN-NOTE.md defining the creative direction before writing any code.
3. Generate the imagery with the Codex CLI as described in CLAUDE.md. Do not fake textures, light, or surfaces with CSS gradients, box shadows, or filters.
4. Build it. Verify frame-by-frame in the browser at mobile and desktop widths.
5. Screenshot, write NOTES.md, and stop.

The first three seconds should say: you're invited, this is happening, it's here.
