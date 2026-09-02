# AI Friday design sprint

One afternoon, one brief, four Claude Fable 5.1 sessions. A test of the model and of the method in Anshu Chimala's [How to turn your AI into a world-class designer](https://www.lennysnewsletter.com/p/how-to-turn-your-ai-into-a-world), run on the [AI Friday](https://aifri.day) homepage. Not a redesign; a test run.

**Site:** https://andrewedunn.github.io/aifriday-fable5.1-design/

## What's here

- `index.html` — the sprint page: how the four directions came to be, the shared brief, each session's prompt, and the four builds.
- `designs/` — the four builds, one folder each, exactly as the sessions left them (minus raw generation sources and tooling). Each has its `CLAUDE.md`, `PROMPT.md`, `CRITIC.md`, `DESIGN-NOTE.md`, `NOTES.md`, and the page itself.
- `source/parent-chat.md` — the claude.ai conversation that produced the brief and prompts, verbatim.
- `source/prompt-pack/` — the launcher and polish checklist that sat above the four folders.
- `site/` — templates, stylesheet, and the uniform hero screenshots used on the sprint page.
- `scripts/` — `sync-designs.sh` copies the builds in from the sprint folder, `shots.sh` captures screenshots with headless Chrome, `build.py` renders the page.
- `docs/plans/` — the design note for this page.

## Rebuilding after the sessions change

```sh
./scripts/sync-designs.sh          # from ~/dev/aifri-design/ai-friday-redesign by default
./scripts/shots.sh                 # needs Google Chrome and ImageMagick
python3 scripts/build.py           # needs python-markdown
python3 -m unittest discover -s tests
```

## Credits

Sprint conversation and builds: Claude Fable 5.1 (claude.ai and Claude Code). Imagery in the builds: OpenAI Codex CLI. This page and its scripts: Claude Fable 5.1 in Claude Code, from Andrew Dunn's notes. Meetup details in the builds are placeholders.
