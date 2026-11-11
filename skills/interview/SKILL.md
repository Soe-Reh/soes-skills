---
name: interview
description: Use when the user has a product idea, feature, or side project that is not built yet, or says "interview me", "grill me", "help me think this through", "I have an idea", "is this worth building", or "poke holes in this" before any spec or code exists.
allowed-tools: AskUserQuestion, Read, Glob, Grep, Write, Agent, WebFetch, WebSearch
---

# Interview

Ask only questions whose answer changes what gets built. No code. Output: one notes file a coding agent can build from.

## 1. Look before you ask

Read the repo, CLAUDE.md and `.plans/`; never ask what a file answers. Open any named link and give a 3-line verdict, or say what blocked you. Restate the idea in 2 lines.

## 2. Round 1: their situation

Open questions, no pre-filled answers:
1. **Today:** what they do now and where it breaks.
2. **Success:** one number, by when, judged by whom.
3. **Buyer:** who pays, how much, first named users.
4. **Capacity:** who builds, hours a week, what already overlaps.

Vague answer: push once with an example, then move on.

## 3. Test the premise first

- **Window:** metric can't read out by the deadline? Add a proxy.
- **Evidence:** "said they'd pay" < workaround < paid. Get the next rung.
- **Buyer vs users:** if they differ, recruit one real buyer.
- **Readable:** both arms log it; traffic can detect the lift.
- **Harm:** health, legal, money inputs go to a human; shared links get per-person tokens.
- **Repeat chore:** make it one tap.

Weak premise: say so, say what would change your mind, offer a reframe. Never weaken the user's goal: a proxy stays secondary, a dropped goal goes in Decisions.

## 4. Rounds 2-3: decisions

2-4 questions a round, 2-4 concrete options each, **your recommendation first** with a one-line reason. Hunt late surprises: weeks-long approvals, look-alike states, data changing while saved. Size scope to the builder's hours. End each round with only what changed plus vetoable defaults. Stop when nothing open would change v1.

## 5. When the user hands it back

| User says | You do |
|---|---|
| "you decide" on one | Pick; log made by interviewer |
| "you decide" on all | One round of one-way doors only (money, data, auth); decide the rest |
| "skip it" / "write it" | At most 1-2 one-way doors, then write |
| A full plan | Run step 3, ask only the gaps |

## 6. Save the notes

Write `<cwd>/.plans/<topic>-interview.md` once, every heading kept ("None" if empty).

```markdown
# <Topic>: interview notes
Date: <YYYY-MM-DD> | Status: ready to build

## One-liner
## Problem and today's workaround
## Users and buyer
## Success
- Primary (user's own bar): <metric, threshold, by when, judged by whom>
- Secondary or proxy: <optional>
- Test: <arms, population, smallest detectable lift, pass/fail>
## Constraints
## Premise checks
- <check>: <result, or test with pass/fail and date>
## V1 scope
## Out of scope
## Build
- Data: <entities, key fields>
- Routes: <route: purpose, who sees it>
- Logic: <signatures, one worked example>
- States: | State | Trigger | User sees |
- Guards: <inputs routed to a human, outputs rejected>
- Events: <logged for the metric>
- Acceptance tests: <given/when/then per screen and guard>
- Plan: <weeks back from deadline, ordered cut list>
## Gotchas
## Decisions
| Decision | Chosen | Why | Made by (user / interviewer) |
## Open questions
- <question>: <blocks what>, <who answers>
```

## 7. Hand off

Reply with path, one-liner, biggest risk, first step. Offer once: "Run the spec skill on these notes next?"
