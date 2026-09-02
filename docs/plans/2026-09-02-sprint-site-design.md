# Sprint site design

Date: 2026-09-02. Status: approved by default (autonomous run); Andrew can revise.

## Purpose
A public, static page that documents one afternoon's design sprint: Claude Fable 5.1
building four AI Friday homepage directions with the method from Anshu Chimala's
"How to turn your AI into a world-class designer" (Lenny's Newsletter, 2026-09-01).
It is a test of the model and the method, not a redesign announcement. The page's
single job: let a reader follow brief → ideas → prompts and click into the four
live builds.

## Structure (one page)
1. Masthead and the wall: title, framing paragraph, four framed screenshots.
2. How we got to four: the claude.ai conversation, condensed, with verbatim quotes.
   Step zero (the feeling), fifteen sparks, Andrew's three picks, the sharpening
   into three layers plus a combined fourth, and the answers that shaped the prompts.
3. The brief: CLAUDE.md, collapsible. Critic prompt and polish checklist alongside,
   marked as not yet run.
4. The four directions: each an exhibit with a placard (name, layer, seed size,
   type, images), the verbatim prompt (collapsible), and links to the live design,
   the design note, and the build notes.
5. What's next and credits.

## Design system
Direction borrowed from spark #14 on Claude's own list, "museum wall labels": the
designs are exhibits, each with a placard. Quiet and proud.
- Wall #EEEDE8, sheet #FBFBF9, ink #1B1A17, ink-2 #625F58, rule #D5D2CA,
  haint #A6C6CD with #2F6A78 for link text. Haint blue is the one accent because it
  is the thread running through three of the four builds.
- Type: Bricolage Grotesque (variable, optical sizes) for everything. Display sizes
  carry the personality; text sizes stay plain. No monospace.
- Signature: the wall. Four framed screenshots hung in a row under the title.
- Motion: hover and focus only. Native <details> for collapsibles. No JS required.

## Tech
- Static HTML + CSS at the repo root; GitHub Pages serves main branch root.
- `scripts/sync-designs.sh` copies the four builds from the sprint folder into
  `designs/`, excluding raw generation sources and tooling, and converts screenshots
  to WebP.
- `scripts/build.py` renders `site/template.html` plus the Markdown in `designs/`
  and `source/` into `index.html` and per-design `notes.html`, using python-markdown.
- `tests/test_site.py` checks that the built site's local links resolve and every
  design has an index page. Run: `python3 -m unittest discover -s tests`.

## Out of scope
Rewriting any design. Running the critic loop. Replacing placeholder meetup facts.
