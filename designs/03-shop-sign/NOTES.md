# NOTES

I generated a 128-character random string and read it for structure rather than surface:
its 1:6 letter-to-digit ratio set the discipline rule that only about one line in six on
this page is painted lettering, its near-even upper/lowercase split set signs-versus-body
weighting, its two doubled letters (JJ, XX) decided that the hard painted drop shadow
appears in exactly two places, and its digit gaps (long runs of 25 and 23 punctuated by
tight 2,2 pairs) became the vertical rhythm of clusters and quiet stretches. I wrote
DESIGN-NOTE.md from that, then generated the hero sign first with the Codex CLI and
sampled the real palette out of the returned pixels, so the CSS tokens are the paint
rather than a guess at it. Seven more surfaces followed: four section slats, a blank
price board, a plaster wall, and later a squarer second hero for phones. Nothing on the
page uses a CSS gradient, box-shadow, or filter to imitate material. Where copy has to
stay editable (the run of show, the specials) the board is the generated image and the
text on top is plain Libre Franklin, which is what a real price list looks like anyway.
Four things only surfaced in the browser and got fixed there: the wall tiled with a
visible seam (rebuilt as a mirrored tile), a 74rem page left a dead right half (pulled to
62rem), all four signs shared one width so their painted letters came out different sizes
(each board is now cut to its word count), and the maker credits read as template eyebrow
labels in letterspaced caps (now sentence case). Contrast is 5.8:1 at worst, no image is
missing alt text, and there is no horizontal overflow at 390, 768, or 1440.

Next, in order: the wide hero sign is the one asset that has to be regenerated every
month, so I would write the prompt that produces it into a short README and check the
date band renders cleanly for a two-digit day. I would build a real RSVP destination
rather than the `#` placeholder and decide whether the venue line becomes a live field.
The specials could carry a small painted price tag per project instead of a red sans
number, which would be more of the same idea, though it is also exactly the kind of extra
accessory worth removing. And I would look hard at the two long quiet sections on desktop:
they are correct per the direction, but a second opinion should confirm they read as
confidence rather than as an unfinished right column.
