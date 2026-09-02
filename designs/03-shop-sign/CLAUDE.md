# AI Friday — design brief

AI Friday exists to help people in New Orleans build more with AI. We want to create more builders in this city. Today it is two things: a monthly meetup in New Orleans, and a Slack community where people share what they're making. Later it will also publish useful content, so the design should have room for that without featuring it now.

## Who this is for
AI-curious knowledge workers: people who use a computer all day, are interested in AI, and are not developers. Many of them quietly assume "this isn't for me." Some already use AI and want tips and tricks. This site is NOT aimed at a technical audience.

## The feeling
"This is for you, and it's happening here."
Permission, momentum, and place, in that order. Someone should feel invited within three seconds.

## Actions
Primary: RSVP to the next meetup. It is a real Friday, a real room, a real date.
Secondary: Join the Slack.
The site is a door, not a hub. Keep it to one page.

## Placeholder facts (the owner will replace these)
Next meetup: Friday, October 2, 2026, 5:30pm. Venue: TBD, New Orleans.
Slack: link to "#" for now.
Member projects: invent 3–4 plausible ones built by non-developers (a lawyer's intake bot, a teacher's lesson generator, a restaurant's scheduling helper, etc.).

## Sections (minimum)
1. The invitation: next meetup date, place, and a one-line reason to come. This is the hero.
2. What AI Friday is, in a few sentences.
3. What people are building: 3–4 short example projects from members.
4. What you'll walk away with: 3 concrete things a first-timer gets.
5. Join the Slack.
6. Footer: location, contact, socials.

## Anti-goals
- Not a developer tool. No dark mode, no monospace, no terminal or code aesthetics.
- Not a SaaS landing page. No "features" grid, no pricing-page rhythm.
- Not a tourist brochure. Do NOT use: Mardi Gras beads, fleur-de-lis, jazz iconography, masks, purple/green/gold, Bourbon Street, "Big Easy," "laissez les bons temps rouler," or any French Quarter imagery. New Orleans should be felt the way a local feels it, not sold the way a visitor sees it.

## Copy
Write real copy, not lorem ipsum, so the design can be judged. But treat every line as a placeholder: a human will rewrite all of it. Keep it short and plain. No em-dash-heavy AI cadence, no "unlock," "empower," "supercharge," "journey," or "community-driven."

## Image generation
Use the Codex CLI for image generation. It is already installed and logged in; make sure it bills the subscription, not an API key. If it isn't available, stop and tell me rather than faking imagery with CSS. Save generated assets in ./assets/.

## Tech
A single static page: index.html, styles.css, script.js, assets/. No framework, no build step. We are evaluating the design, not the stack. Must look right on mobile and desktop. Verify your work frame-by-frame in a browser (use a headless browser or Playwright screenshots if no display is available), not just by reading the code.

## Working agreement
- Write a short DESIGN-NOTE.md before coding, describing the creative direction.
- When the build is done, screenshot desktop and mobile into ./screenshots/, write a one-paragraph NOTES.md on what you tried and what you'd do next, then stop and wait. Do NOT run CRITIC.md until asked.
