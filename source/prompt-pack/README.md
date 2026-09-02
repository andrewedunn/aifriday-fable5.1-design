# AI Friday redesign — four parallel POCs

Four Claude Code sessions, one design direction each. Every folder is self-contained: CLAUDE.md (shared brief), PROMPT.md (the direction), CRITIC.md (feedback loop), and refs/ for reference screenshots.

## Run
1. Optional: drop 3–5 reference screenshots into ./refs (good restaurant sites, festival posters, book covers; not AI-community sites).
2. `./launch.sh` — opens a tmux session with four windows, each already running its prompt. Attach with `tmux attach -t aifriday`.
3. Don't steer mid-build. When a session says it's done, look at its screenshots/ and NOTES.md.
4. In each session, type: `Read CRITIC.md and follow it.` (Or relaunch everything on the critic step with `./launch.sh --critic`.)
5. Send the before/after screenshots and your gut reactions back to Claude for the next sharpening round.
6. Polish the survivor(s) using POLISH.md.

## Before launching
CLAUDE.md contains placeholder meetup details (Oct 2, 2026, venue TBD). Replace them if you have real ones; otherwise the agents will use the placeholders.

## Directions
- 01-shotgun-house — structure: one long walk through the rooms, literal architecture
- 02-front-porch — scene: warm lively evening, haint blue, "pull up a chair"
- 03-shop-sign — type: hand-painted corner-store signage for headlines only
- 04-combined — all three, each given exactly one job
