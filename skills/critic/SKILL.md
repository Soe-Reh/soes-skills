---
name: critic
description: Use when work needs an honest outside judgment before it ships, when choosing between versions, or when the user asks for a harsh, blind, unbiased, or peer review, a second opinion, or a score against a bar. Works on specs, pages, apps, READMEs, pitches, resumes, and code changes.
---

# Critic

Two blind reviewers who stand in for the real audience, judged against a bar set first. One round.

## 1. Set the frame

Ask one question only if the audience is unclear.

- **Audience**: who really judges this (recruiter, first-time user, maintainer, investor).
- **Bar**: pass score out of 10. Default 8.
- **Mode**: one version, or 2 to 4 versions to compare.

## 2. Build the blind packet

1. Make a new, empty folder outside the project. A nearby `v2.md` gives the answer away.
2. Copy in only the work a real reviewer would see. For code, the diff plus changed paths.
3. Strip names, "v2", "new", dates, and hints of a favorite.
4. Comparisons: label A, B, C in random order (`shuf`); keep the key outside.
5. Running app: include the URL; reviewers use it live (main path, one bad input).

## 3. Run 2 reviewers

Launch 2 parallel subagents with different audience personas:

| Work | Persona 1 | Persona 2 |
| --- | --- | --- |
| Spec or plan | engineer who builds it | skeptical exec |
| Page or app | first-time user | hands-on tester |
| README | stranger installing it | maintainer |
| Pitch, resume | target reader in a hurry | skeptic |
| Code change | maintainer | security reviewer |

No subagent tool: do both passes yourself and do not mention it.

Each reviewer reads only the packet and checks:

- Contradictions between sections, numbers, and promises.
- Failure states: errors, bad input, a job that fails or data that goes stale, a user whose situation changes.
- Claims with no number or proof, and marketing language where a plain sentence belongs.
- Success targets: is there a number to hit?

Each returns a score per version and problems ranked P0 (blocks shipping) to P2, each with location, why it hurts this audience, and a paste-ready fix ("author to supply" if only the author has the fact).

**Rules:** every problem points to a spot in the work. Search the packet before calling something missing. No guesses about the business. Legal points are "likely; confirm with counsel". Never keep something that causes a problem you found. Fewer real problems beat padding. No repeated per-finding template.

## 4. Report

Unblind after scoring; use the lower score. A problem both raise is a must-fix; one reviewer's taste is a suggestion. Write for the author: no personas, reviewer count, method, or tools.

```
Verdict: Not ready for <deadline> as written; fixable in <effort>.
Fix first:
1. [P0] <where>: <problem>. Fix: <paste-ready change>.
2. ...
3. ...
Also: <P1/P2 items, one line each>
Keep: <what works, specific>
Could not check: <one line>
```

Pass: "Ready for <audience>" plus P1s. Comparisons add `Scores: A 8, B 6.5, C 7. Pick A: <reason>.` One verdict, top to bottom.

## 5. Stop

One round; the author decides what to fix. Re-review only if asked or after fixing a FAIL, with a fresh packet and the rejected fixes listed. Cap: two rounds.

## 6. Learn, quietly

A repeat mistake gets one line where it is read next time: CLAUDE.md (project rules), memory (user taste), or this skill (process gap). Never in the report.

