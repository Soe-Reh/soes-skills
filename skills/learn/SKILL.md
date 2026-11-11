---
name: learn
description: Use when a session or project wraps up, or the user says "learn", "what did we learn", "retro", "self-improve", "remember this for next time", or complains that the agent looped, retried, or burned too many tokens or too much time.
---

# Learn

Turn this session into a few durable rules, each in the one place that will apply it next time. Keep this pass cheap.

## 1. Gather evidence

1. Use the current conversation. If it starts from a summary, read only the compacted part of the session transcript (newest `.jsonl` under `~/.claude/projects/<project>/`) by grepping user messages.
2. Read the homes once: project `CLAUDE.md` (and nested ones), the memory index `MEMORY.md`, and the `description` line of each skill in this plugin. Open a skill body only when a lesson points at it.

## 2. Scan, highest value first

1. **Corrections**: the user said no, stop, actually, or fixed your work.
2. **Waste**: the same command, fix, file read, or subagent run three or more times; a review loop that ran rounds past the bar; a big read that a grep would have answered. Count it and fix the cause (missing info, vague stop rule, no check).
3. **Repeated asks**: guidance the user gave twice.
4. **Confirmed approaches**: something that worked and will be needed again.
5. **Failures**: what broke, and what worked instead.
6. **Preferences**: style, naming, tool choices the user stated.

## 3. Filter

Keep a lesson only if it is stable, non-obvious, actionable as one rule, and not already covered. It is covered when an existing rule, followed, would have prevented the problem. A rule that exists but was ignored needs to be sharper or moved, not copied. Drop one-offs, task state, and bugs fixed this session. If nothing survives, say so and stop.

## 4. Route each lesson to one home

| Home | Gets |
|---|---|
| Automated check (lint, hook, test) | Mechanical rules a tool can decide from the code. Write no prose rule for these. |
| A skill in this plugin | Anything that corrects or sharpens how a skill runs: a skipped step, a bad default, a missing stop rule. |
| Project `CLAUDE.md` | Project decisions and pointers (commands, paths, conventions). Keep it short; it loads every session. |
| User memory | Personal preferences and gotchas with no skill home. |

Ties: skill beats CLAUDE.md and memory. Decisions go to CLAUDE.md, discovered quirks to memory. A multi-step procedure goes to a skill, with a one-line pointer in CLAUDE.md.

## 5. Show the plan, then write

1. Print a table: lesson, exact file, append or edit in place, and the one-line rule text. Wait for approval. Write nothing before it.
2. Apply only approved rows. Edit in place over appending, match the file's tone, state the rule, not the incident. Keep personal details out of files that are shared or published.
3. Report what changed in one line per file.
