---
name: spec
description: Use when interview notes exist in .plans/, an idea has been discussed enough to build, or the user says "write the spec", "spec this out", "write a PRD", "turn this into a spec", or "make this buildable".
allowed-tools: AskUserQuestion, Read, Write, Edit, Glob, Grep
---

# Spec

A spec an agent builds without a question and a reader gets in 30 seconds. Decide; do not interview.

## 1. Gather

1. Read the newest `.plans/*-interview.md`, else the conversation. Neither? Suggest `interview` and stop.
2. If `.plans/<topic>-spec.md` exists, revise it and keep the user's decisions.
3. Skim the repo; use its names. Note hard constraints, stated user behavior, who builds and pays.

## 2. Decide the gaps

- Default every gap; never break a hard constraint or invent facts about people.
- Mark guesses `(assumed)` inline. Dates as "week 3" unless given. Unknown baseline: give the method and who sets it.
- Seeded data never counts toward a metric; show which real cycles fit its window.
- Each extra user step gets a fallback (auto-confirm after N days).
- Keep all that was asked, add nothing; extras go to Later.
- Settle edges: empty, duplicate, no response, failed external call. A failed step shows Retry, never a half-made message. Dedupe never blocks a demo rerun.

Ask one question at most, only if a wrong guess changes architecture or v1 scope; give your pick.

## 3. Write

Save to `<cwd>/.plans/<topic>-spec.md`. 1-2 pages; thin sections get one line; no "TBD".

```markdown
# <Name>: spec
Source: <file or conversation>, <date>

## Summary
<What, for whom; the success metric; the biggest risk.>

## Problem
<Who, how often, what they do today.>

## Success metrics
| Metric | Target | By when | How measured |
|---|---|---|---|
Guardrail: <must not worsen, threshold>.
Not success: <vanity numbers>.

## Scope
- **In (v1):** ...
- **Out (v1):** <item>: <why>
- **Later:** ...

## Core flow
1. <User does X, sees Y>
Edge states: <each, and what the user sees>

## Requirements
| ID | Requirement | Priority | How to check |
|---|---|---|---|

## Technical notes
Data: <tables, typed columns>.
Invariants: <server-enforced rules, each with a test>.
Off switch: <flag; data when off>.

## Risks
| Risk | Check by | If it fails |
|---|---|---|

## Decisions to confirm
| Decision | Why | Who confirms |
|---|---|---|

## Build phases
### Phase 1: <name> (~<hours>)
Covers: R1, R2
Done when: <command or clicks, what you see>
Cut first if late: <R#>
```

Rules per part:
- **Metrics:** 1-3 plus a guardrail, each with number, date, and a requirement that logs it.
- **Out:** 3+ with reasons, naming the tempting features.
- **Requirements:** 8-12 pass/fail behaviors ("shows 'Card declined', keeps the form", not "fast"). P0 core flow, P1 v1 worse without, P2 cut first. AI prompt rules are one.
- **Risks:** one that could change a requirement gates a phase. A demo gets a fallback recording.
- **Decisions:** only the 3-6 that change the build.
- **Phases:** 2-5, each leaves something running; Phase 1 is the thinnest end-to-end path; hours fit capacity. Cut first: costliest P2, never a promise.
- **Done when:** an outsider checks it in the running app in 5 minutes.

## 4. Check before saving

1. Recompute every number; money gets an invariant.
2. No default breaks a constraint or misstates a person; guesses are marked; the timeline holds the metric's window.
3. No edge state sends what it should not.
4. Every P0 and P1 is in a phase; Phase 1 could start now.
5. Cut every sentence a builder would not miss.

## 5. Reply and hand off

Give the path, summary, phases, riskiest decision, and what you left out.

Human gate: the user approves the spec before any code. Then hand off to `build`: each phase becomes a PROGRESS.md part checked by **Done when**.

<instructions>$ARGUMENTS</instructions>
