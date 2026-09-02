Read CLAUDE.md first.

Build the AI Friday homepage using hand-painted shop signage as the type system.

The vernacular is New Orleans corner store, po-boy shop, laundromat, neighborhood grocery: enamel color on wood or brick, lettering done by a sign painter, a drop shadow that was painted not rendered, "COLD DRINKS" and "OPEN" and hand-lettered price boards. It is NOT Western saloon, NOT rustic farmhouse, NOT hipster café. If it starts to feel like a coffee shop chalkboard, it's wrong.

Signage is for headlines only. One big painted sign is the hero: the next meetup, painted like it's hanging over a shop door. Each section header is a smaller painted sign. The month's schedule reads like a menu board. Member projects are the "specials." Everything else, body copy, buttons, form fields, footer, is set in a clean, quiet sans-serif with plenty of air. The signs are the personality; the rest of the page gets out of their way. Lettering the whole page would be exhausting; don't.

This direction lives or dies on texture. Every painted surface must be generated: the sign boards, the painted lettering, the wear at the edges, the wood or brick behind it. A display font with a CSS text-shadow will look like a template and is not acceptable. Generate the signs as images, or generate the surfaces and composite live text over them if the copy needs to stay editable; explain which you chose and why in DESIGN-NOTE.md. Generate the hero sign first and let it set the palette.

Seed-string decisions: the enamel palette, sign shapes, surface material, the sans-serif pairing, layout rhythm.

Follow this procedure:
1. Generate a long, random alphanumeric string using a shell script. Use it as inspiration for every decision the brief doesn't already make. Look beyond the surface for subpatterns, special numbers, anything that inspires you. Don't reveal the string in the design.
2. Write DESIGN-NOTE.md defining the creative direction before writing any code.
3. Generate the imagery with the Codex CLI as described in CLAUDE.md. Do not fake textures, light, or surfaces with CSS gradients, box shadows, or filters.
4. Build it. Verify frame-by-frame in the browser at mobile and desktop widths.
5. Screenshot, write NOTES.md, and stop.

The first three seconds should say: you're invited, this is happening, it's here.
