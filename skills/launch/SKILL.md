---
name: launch
description: Use when a finished build is about to be shown or shipped, such as demo day, hackathon judging, a portfolio piece, a public launch, a README, or a launch post, or when the user asks how to present, demo, or announce a project.
---

# Launch

Get a finished build ready for strangers. Make only what the deadline needs; length costs the user time. The user sees only launch work: no process notes, approvals, agent talk or self-review.

## 1. Readiness check (run it)

Start the app clean and walk the core flow in the running app. List what works and what breaks, with exact errors. Look for leaked keys, crashes under real use (more users, a phone, a cold start) and claims the data can't back.

Per blocker, take the cheapest option: fix (30-45 min max), guard (cap users, hide the button, a "waking up" state), or cut it. Give each fix a visible pass condition, e.g. "a $9 test purchase flips the account to paid, then refund".

## 2. Pitch line

One sentence: **<Product> helps <user> <do job> by <how>, unlike <current alternative>.** If it fits a competitor too, it is too generic.

## 3. Pick the pieces

| Situation | Pieces |
| --- | --- |
| Live demo, judging | demo script with failure ladder, 3 likely questions with honest answers |
| Repo, portfolio | README, one resume or post line |
| Public launch | README, launch post, metrics |

Get the user's OK on the pitch line and pieces first. Skip roadmaps, risk tables and 90-day plans unless asked.

## 4. Write the pieces in full

Deliver finished text, never an outline.

**Demo script** (2-3 min): the problem in one line, then the core flow live (not landing page or login) with exact clicks and inputs, the hard part, the result. **Failure ladder**, in order: refresh, then seeded or pre-generated data, then hotspot, then a recorded video of every step. If people open it on their own time, keep it awake with an uptime ping or paid tier.

**README:** pitch line, screenshot, what it does (3-5 bullets), copy-paste run steps, the full `.env.example` with placeholder values, stack, credits by role, and known limits stated plainly. Run them in a fresh clone.

**Launch post:** the user's problem, what it does, one proof point that is measured today, a link, one ask. Under 150 words for social. Stagger channels: one per day, the main one first. Read it out loud and cut anything that sounds like an ad.

**Metrics (1-3):** where to read each, today's baseline, the number that means it worked. Fire each event once and confirm it shows up.

## 5. Final check

Have a second agent that has not seen the build follow the README and script literally. Fix:

- **Broken commands:** fails as written.
- **False claims:** numbers not measured, "users love it", "fast". Replace with what is true, or a bracketed gap the user must fill.
- **Invented facts:** origin stories, anecdotes, names, features nobody planned. Use `[Your name]` and mark hooks "replace with your real story".
- **Leaked secrets:** keys, tokens, `.env` values, emails, internal URLs, in the pieces and in git history. A leaked key gets rotated, not just deleted.

If a fix may slip, add a fallback line ("works in Chrome; Safari fix coming"). The user runs the demo live once before showing anyone.

## After the event

Note what broke and what got asked. Project facts go in the repo's CLAUDE.md, preferences in memory, process changes in this skill.
