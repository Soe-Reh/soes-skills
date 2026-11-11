---
name: build
description: Use when an approved spec exists in .plans/ and the user says "build it", "run autonomously", "keep going without asking", or "continue from PROGRESS.md".
---

# Build

Build an approved spec part by part. Loops burn the user's usage limit, so re-run only when a check fails.

## 1. Start or resume

1. Find the spec (`.plans/*-spec.md`). Not there or not approved: stop and run `spec`.
2. If `PROGRESS.md` exists, trust it over the chat. Done parts stay done. Resume at **Next**.
3. Otherwise run the existing tests once as a baseline, so old failures are not blamed on new work.
4. Create `PROGRESS.md`. Each spec phase becomes a part and its **Done when** line becomes the check:

```markdown
# PROGRESS - spec: .plans/<name>-spec.md
Baseline: <tests/tsc result before any change>
Next: <one concrete action>

## Parts
- [ ] 1. <phase> | owns: <files> | needs: <part or owner action> | check: <command> | risk: low/high

## Rulings
- <decision> | why | cost if wrong

## Owner only (blocks only the part listed)
- <action> | part N

## Not checked
- <item>
```

5. Fix traps in the plan before any code:
   - Shared file: run those parts in order.
   - A part needs a later one: reorder, write it under **needs**.
   - A vague or manual check ("instant"): swap in a number or a script.
   - Spec contradicts itself: take the safe default, log a ruling, add an owner confirm.
   - Oversized phase: split it.
   - **High** risk: auth, data access, money, public exposure, migrations.

6. If the work has to match or beat something (a site, an app), study it before designing. Capture it with Playwright screenshots, pull its design tokens with `skillui` if you have it, and write what you learned to `research/`. Sites that block bots: use a Wayback snapshot or ask the user to save the page. Never get around a bot wall.

## 2. Build each part

- One subagent per part. At most **2 at once**, only on disjoint files and when the time saved beats the merge step.
- Model by risk: strongest for high risk, mid-tier for clear parts, cheapest for mechanical edits.
- Give it only: spec path and part, files it owns and must not touch, what earlier parts changed, the check.
- It spawns no agents and returns 5 lines: status, files, check output, deviations, unverified.
- If blocked, change something (context, smaller part, stronger model). Never resend the same prompt.

## 3. Verify by running it

Re-run the check yourself. Never trust pasted output.

| Work | Proof |
|------|-------|
| Logic, API, CLI | Run the tests or command, read the output |
| Anything a user sees | Smoke test the running app: click the real path, screenshot, read the console |
| Access rules | Log in as a second user, confirm they see nothing |
| Config | Change the value, show the output change |

## 4. Review only high-risk parts

Low risk: done when the check passes. High risk: one blind `critic` on the spec part and diff, bar 8/10.

- 8+: done, log the score.
- Below 8: one fix round on concrete defects, re-run the check. No second review.
- Still failing after that: plateau. Log it under **Not checked**, block dependents, move on.
- Style notes are logged, never fixed.

Commit each done part on a branch (repo's commit rules) and log the hash.

## 5. Keep going

Decide, log a ruling, continue. Ask only for:

- logins, API keys, billing, payments
- anything public: deploy, post, email, push to main
- anything destructive: deleting data, migrating real data
- a ruling on who can see user data

Block only the part that needs it. Update **Next** after every step.

## 6. Hand over

1. One end-to-end smoke test of the whole app. No final critic.
2. Give the user a link or command to try it live. Their try is the last gate before shipping.
3. Report: what works and how to see it, real scores, what failed, what waits on the owner, what was **not checked**.

## 7. Learn

Save up to 3 lessons where they belong, not in the report:

- Project fact or command: `CLAUDE.md`
- User preference: memory
- A step this skill got wrong: an edit to this skill
