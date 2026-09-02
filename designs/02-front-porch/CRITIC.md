I want you to improve this design. To figure out what to focus on, use a Claude Fable 5.1 subagent as a design critic.

Follow this procedure at each iteration:
- Capture a screenshot of the current design at desktop width and one at mobile width.
- Invoke the critic in a fresh context with just the screenshots and the reference images in ./refs (if any). Do not give it the code, implementation details, the design brief, or earlier critiques.
- Ask it to identify the aesthetic this design is going for, imagine how a top design studio would execute that same aesthetic for a neighborhood meetup, and outline the biggest gaps.
- If ./refs has images, ask it to rank the reference images and our screenshot together by polish and taste level. Either way, have it give our design a score out of 10 against that studio-level bar.

Give the critic this guidance in its prompt:
- Think high-level about structure and composition, then look at the fine details.
- Watch for patterns that feel overdone or obviously AI-generated and penalize them: eyebrow labels, generic gradients, excessive cards and containers, too many fonts or text styles, glow effects, decorative elements that serve no purpose, copy that overexplains.
- Watch for tourist-brochure New Orleans and penalize it hard.
- Watch for anything that would make a non-technical person feel this isn't for them.
- Provide tight, specific feedback, not vague prose.
- Be bold and opinionated, not safe.

Do at most two iterations, then stop. Save before/after screenshots to ./screenshots/ and both critiques to CRITIQUES.md so I can see whether it's converging. Do not put a target score in the critic prompt; keep its scoring objective. Use the same critic prompt each time.
