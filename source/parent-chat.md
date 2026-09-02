# "Redesigning AI Friday website from scratch"

Verbatim transcript of the claude.ai conversation (Claude Fable 5.1, "High" effort) that produced the brief and the four direction prompts. Captured 2026-09-02. Typos in Andrew's messages are left as typed. Claude's "thinking" blocks are omitted.

---

**Andrew** *(attached the Lenny's Newsletter article as a PDF)*

Hey there! I want you to help guide the redesign of the AI Friday website. I really want to think about it from scratch.

The goal of AI Friday is to help people build more with AI. I want to help create more builders in New Orleans.

AI Friday is two primary things right now:

- A monthly meetup in New Orleans
- A slack community to share things

I also want to increasingly post or generate useful, helpful content.

But for now I've attached an article that I want to use to help drive the design.

Let me know if you agree, but I think to get there we need to do the following:

1. Start with coming up with bold, unique design language.
2. Then we choose one and you help me craft a prompt that I can use with another AI agent to build the POC
3. Then we do a creative feedback loop

This is just my rough sketch. What do think?

---

**Claude**

Your sketch is solid, and it maps almost exactly onto the article's Discover → Define → Deliver arc. A few adjustments I'd make before we start:

**Add a step zero: decide the feeling.** The article's core argument is that great design starts with an emotional response, and that your taste is what makes the output non-generic. So before I list design languages, we should be able to answer in one line: what should someone feel in the first three seconds on the AI Friday site, and what's the one thing you want them to do? "Help people build more with AI in New Orleans" is a mission, not yet a feeling. Is it "you're welcome here even if you've never written code," or "there's a real scene here and you're missing it," or "this is where serious builders in the city hang out"? Those lead to very different visual worlds.

**Step 1 works, with one caveat.** I'll go broad and shallow like the article suggests, but the value comes from your reactions, not my list. Plan to spend real time on the "I'm imagining… / this feels tacky / I want more of…" pass. That's the part nobody else can replicate.

**Step 2, I'd tweak slightly.** Beyond the single POC prompt, it's worth also using the seed-string technique to spin up 3–4 variants of the chosen direction before committing. Cheap, and it surfaces layouts you wouldn't have asked for. I'd also bake in image generation from the start rather than adding it later, since code-only gradients and shapes are the biggest AI tell.

**Step 3 is right, but plan the Deliver stage too.** The feedback loop is the critic-subagent pattern, and I can write that critic prompt for you. But the polish stage after it (cut what doesn't earn its place, hunt the tells, rewrite every line of copy by hand) will matter more for a community site than for a product landing page. AI Friday's voice is the brand. AI-sounding copy on a page inviting people to a real-life meetup would undercut the whole thing.

Two things worth deciding now:

- New Orleans is your biggest design asset and your biggest trap. Leaning into place is what will make this look unlike every other AI-community site. But the obvious cues (jazz, beads, fleur-de-lis, purple/green/gold) will read as tourist-board. We'll want a New Orleans that locals recognize and outsiders don't expect.
- You said content is coming. We shouldn't design a blog now, but the design language should have room for one so you don't rebuild in six months.

Before I generate directions, I want to nail the audience and the primary action:

1. Who is the homepage mainly trying to win over?
2. What's the single action you most want a first-time visitor to take?
3. Is anything fixed, or is this a true clean slate?

---

**Andrew**

1. That's the problem, I think all of the above! For now, we want to invite AI curious or interested people. But our initial goal is getting as many people as possible to get started building but also for people using it to get tips and tricks. It is NOT targeted at a technical audience but generally speaking more people are in knowledge work/use a computer all day.
2. Not sure yet
3. Fully clean slate

---

**Claude**

Good — that answer actually sharpens things a lot. "AI-curious knowledge workers who are afraid they're not technical enough" is a much better brief than "everyone," and it rules out the single most likely default: the dark-mode, monospace, terminal-flavored aesthetic that every AI community site drifts toward. Your audience's first fear is "this isn't for me." The design's first job is to dissolve that.

**My proposal for step zero**

Feeling: "This is for you, and it's happening here." Permission, momentum, and place, in that order. The anti-goals are just as useful: not a developer tool, not a SaaS landing page, not a tourist brochure.

Primary action: I'd pick RSVP to the next meetup, with Slack as the secondary for people who can't make it. A Slack invite is abstract; a Friday, a room, and a date in New Orleans is concrete, and a room is less intimidating than a channel full of people posting things. It also makes the site a door rather than a hub, which keeps it simple until content matters. Push back if that's wrong.

**Step 1: design languages, deliberately shallow**

Per the article, these are sparks, not specs. Some lean New Orleans, some don't. Ignore the ones that don't land.

1. Bulletin board — a corkboard of flyers, index cards, and pinned photos. The meetup is a flyer; member builds are polaroids.
2. Shotgun house — one long scrolling column, each section a room you walk through front to back.
3. Front porch — chairs, a screen door, evening light. Hospitality as the whole visual system.
4. Hand-painted shop sign — sign-painter lettering, enamel colors, the corner-store aesthetic of the city's neighborhoods.
5. Lab notebook — graph paper, marginalia, taped-in screenshots, handwritten annotations over AI outputs.
6. Recipe card — "cook with AI." Ingredients, steps, mise en place. Kitchen as the metaphor for building.
7. Community radio — schedule grid, an "on air" light, a dial. Warm, live, local.
8. Almanac — dates, tables, phases, folksy authority. Monthly rhythm baked into the structure.
9. Public library — card catalog, due-date slips, stamped cards. Knowledge that belongs to the city.
10. Transit map — meetup, Slack, and content as lines and stops on a system map.
11. Zine — photocopied, stapled, black and white with one spot color. Scrappy and honest.
12. Community garden — plots, seasons, things growing. Progress made visible over months.
13. Sub-tropical light — no metaphor, just the atmosphere: humid haze, soft washed color, late-afternoon shadows.
14. Museum wall labels — member builds as exhibits, each with a small placard. Quiet and proud.
15. Playground — big, tactile, primary-shape components. Building as play, not work.

Now the part only you can do. Pick two to four, and for each, tell me what you're picturing, what would make it feel tacky, and what you'd want more of. Even a gut "no, but I like one piece of it" is useful. Then I'll sharpen the survivors into real directions.

---

**Andrew**

My hunch is that maybe I launch multiple sessions trying a few different optoions.

Ones I love:

- Shotgun house. This is super interesting!
- Front porch. Very familier new orleans scene. Think Mardi Gras and Jazz Fest. Hanging outside with a drink.
- Hand painted shop sign. Again, very new orleans. *

---

**Claude**

Good picks, and notice what happened: you didn't pick three competing looks, you picked three *layers*. Shotgun house is a structure, front porch is a scene, and shop sign is a type system. They could be three separate sites, or one site. That makes the parallel-sessions idea even better: run each alone, plus a fourth that combines them, and see which one surprises you. (Also, your fourth bullet got cut off, so tell me if there was one more.)

Here's my sharpening of each. I'm being opinionated on purpose; disagree freely.

**Shotgun house**
One long, narrow vertical scroll where each section is a room, in the order you'd actually walk through one: front room (next meetup, the invitation), middle rooms (what people are building, what you'll learn), and the kitchen at the back (Slack, where the real conversation happens). Doorways are the section transitions, so scrolling *feels* like walking. The big fork: literal (an illustrated cross-section you move through) versus abstract (a narrow column with threshold moments between sections). Literal is more memorable and more likely to tip into cute; abstract is safer and easier to grow content into. Trap: a 3D dollhouse. Question for you: does the structure have to be *read* as a shotgun house, or is it enough that locals feel it?

**Front porch**
Late afternoon, screen door, someone's already sitting there. The hospitality is the whole system: "pull up a chair" is the CTA voice, the meetup is a thing you're invited to rather than a thing you register for. Local detail that earns it: haint blue, the pale blue that porch ceilings get painted across the city. As a primary color, it's soft, distinctive, and locals will clock it instantly without a single bead or fleur-de-lis. Photography or generated imagery should carry this, not vector illustration. Trap: stock "Southern hospitality," or the drink becoming a party. Your framing was right: hanging out, not raging. Question: is this warm and quiet, or warm and lively? That's the difference between a porch at golden hour and a porch on a parade route.

**Hand-painted shop sign**
The typographic layer. Every headline is lettered like it was painted by hand: enamel color, a drop shadow, a sign-shaped container. The month's schedule reads like a menu board. Member projects are a "specials" list. The vernacular is corner store, po-boy shop, laundromat, "COLD DRINKS," not Western saloon and not hipster café, which is where this goes wrong in about two prompts. This one lives or dies on texture, so image generation for the painted surfaces is mandatory; a display font with a text-shadow will look like a Canva template. Question: does the whole page get lettered, or is it just headlines and one big sign as the hero?

**The combined direction**
Shotgun structure, porch as the front room, signage for the type. That's potentially the AI Friday look. It's also the most complex prompt and the most likely to turn into a mess, which is exactly the kind of "there's no way this works" idea the article says to try anyway.

Answer the three questions, add anything that felt off, and I'll write the POC prompts, one per session, including the image-generation and seed-string instructions. Which agent will you build in, Claude Code?

---

**Andrew**

Q1. I'm not sure :)
Q2: Warm and lively.
Q3. I think the whole page lettered will be distracting.

Perhaps we do four prompts/version. One of each of these and then one trying to combine.

I will build with Claude Code. Again, make sure you encapsulate guidance from the article.

---

**Claude** *(produced the document "Ai friday poc prompts")*

Four direction prompts, plus a shared brief for CLAUDE.md, a critic-loop prompt, and a polish checklist, with a table at the top showing where each of the article's techniques landed.

Three decisions I made on your behalf, flag them if you disagree:

- **Shotgun house goes literal.** You weren't sure, and since you're running four sessions anyway, the bold version is the one worth seeing. The prompt requires the structure to survive if the illustration were stripped, so the abstract version is the fallback, not a separate build.
- **The tourist-trap list is explicit and hard-banned** in the shared brief (beads, fleur-de-lis, jazz iconography, purple/green/gold, French Quarter). Haint blue is the local detail I'm betting on for the porch. If there are other locals-only details you'd want in play, add them to the brief; that's your taste, not mine.
- **The critic loop caps at two iterations** before it reports back, per the article's warning about agents burning tokens chasing a score. Raise the cap only if it's converging.

Two things you'll need to fill in before pasting: the actual next meetup date and place in the shared brief, and 3–5 reference screenshots in a /refs folder for the critic (independent restaurant sites, festival posters, small-press covers; not AI community sites).

When all four come back, send me the screenshots with your gut reactions and I'll do the next sharpening round from your taste.

---

**Andrew**

Can you just go ahead and launch these sessions nad build out the folders? Why do I need to do it? And the codex CLI is logged in so it can use that for access to open AI.

---

**Claude** *(produced the zip "ai-friday-redesign")*

I can build the whole folder tree, and I'll do that now. What I can't do is launch the sessions: Claude Code has to run on your machine, logged in as you, and your Codex CLI login lives there too. My sandbox has neither. So the deal is: I build every folder, brief, prompt, and a one-command launcher; you unzip and run one script.

Unzip it anywhere and run ./launch.sh. It opens a tmux session with four windows, each already sitting in its own folder with Claude Code running its direction prompt. tmux attach -t aifriday to watch, Ctrl-b n to flip between them.

What changed from the prompt pack:

- Image generation now goes through your logged-in Codex CLI instead of an API key, so there's no .env.agents step. The brief tells each agent to stop and say so rather than fake textures with CSS if Codex isn't reachable.
- Each folder has its own CLAUDE.md, PROMPT.md, and CRITIC.md. The agents are told to write a DESIGN-NOTE.md before coding, and to screenshot, write NOTES.md, and stop when done, so they don't wander into the critic loop on their own.
- Meetup details are placeholders (Oct 2, venue TBD). Swap them in CLAUDE.md if you have real ones; otherwise leave them, they're fine for judging design.
- ./launch.sh --critic relaunches all four on the critic step once the builds are done, or you can just type "Read CRITIC.md and follow it" in any session.

The refs/ folder is optional but worth five minutes: a few screenshots of sites or posters you think are beautiful gives the critic a real baseline instead of a vibe.

When they finish, send me the screenshots/ from each and your reactions.

---

**Andrew**

k

---

**Claude**

Sounds good. Come back with the screenshots whenever they're done.

---

**Andrew**

Ctrl-b n says no more sessions. Looks like just the shotgun house session is running

---

**Claude**

The other three windows almost certainly launched and died immediately, and tmux closes a window when its command exits, so you never saw the error. Most likely cause is four Claude Code instances starting at the exact same instant and tripping over each other on first-run setup; the first one wins.

Fastest fix, without relaunching the running session. From the ai-friday-redesign folder:

```bash
for d in 02-front-porch 03-shop-sign 04-combined; do
  tmux new-window -t aifriday -n "$d" -c "$PWD/$d"
  tmux send-keys -t "aifriday:$d" 'claude "$(cat PROMPT.md)"' Enter
  sleep 3
done
```

That opens each window with a real shell first, then types the command into it, so if anything fails you'll see the error instead of a vanished window.

(A launch.sh fix using the same pattern followed.)

---

**Andrew**

I think just combined neeeds to run now, I screwed that up. Gimme a command for that.

---

**Claude**

From the ai-friday-redesign folder:

```bash
tmux new-window -t aifriday -n 04-combined -c "$PWD/04-combined" && tmux send-keys -t aifriday:04-combined 'claude "$(cat PROMPT.md)"' Enter
```

If a window named 04-combined already exists from the earlier attempt, kill it first with tmux kill-window -t aifriday:04-combined, then run the line above.

---

*(Two later messages about where the session log lives are omitted; they're housekeeping.)*
