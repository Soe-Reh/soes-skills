# soes-skills

The skills I use to go from an idea to something shipped, packaged for Claude Code.

## Install

```sh
claude plugin marketplace add Soe-Reh/soes-skills
claude plugin install soes-workflow@soes-skills
```

Restart Claude Code, then try:

```text
/soes-workflow:interview a shared grocery list for roommates
```

## What's inside

| Command | What it does |
| --- | --- |
| `/soes-workflow:interview` | Asks about your idea before anything gets built. It checks the premise first, then asks only what changes the build, and saves notes to `.plans/` |
| `/soes-workflow:spec` | Turns those notes into a spec with real numbers for success, what's in and out, and build phases that each end in a check you can run |
| `/soes-workflow:build` | Builds the spec phase by phase, keeps `PROGRESS.md` up to date, and tests the running app. Say "Continue from PROGRESS.md." in a new session to pick up where it stopped |
| `/soes-workflow:critic` | Blind review for the people who will actually see the work. Verdict first, then the 3 fixes that matter and what to keep |
| `/soes-workflow:launch` | Gets a finished project ready to show: demo script with a backup plan, a README that runs, a short post |
| `/soes-workflow:learn` | At the end of a session, saves what's worth keeping to `CLAUDE.md`, memory, or a skill |
| `/soes-workflow:explain` | Rewrites a technical idea in clear, precise language for whoever is reading it |
| `/soes-workflow:frontend-design` | UI that doesn't look templated. By [Anthropic](https://github.com/anthropics/skills/tree/main/skills/frontend-design) |
| `/soes-workflow:better-ui` | Polish for surfaces, icons, and motion. By [Jakub Krehel](https://github.com/jakubkrehel/skills) |
| `/soes-workflow:animate` | Interface animation with a purpose. By [Emil Kowalski](https://github.com/emilkowalski/skills) |

You don't have to type the commands. Skills fire on their own when a request matches, so "interview me about this idea" works too.

## How I use it

```
interview → spec → build → critic → launch → learn
```

What I've learned building this way:

- Study what you want to beat before designing. I screenshotted reference sites with Playwright and pulled their design systems with skillui.
- Write every decision in `PROGRESS.md`. When a session ran out, a new one picked up from there.
- Run two agents at a time at most. Seven at once burned my usage limit in about 25 minutes.
- Pick a realistic bar early. I started at 9/10 and lowered it to 7.5. The extra rounds cost a lot and barely moved the result.
- Look at the output yourself before paying for a review.

## What I use with it

The same marketplace lists three plugins I use alongside these. Each one installs from its author's repo:

```sh
claude plugin install superpowers@soes-skills   # brainstorming, TDD, debugging (Jesse Vincent)
claude plugin install ponytail@soes-skills      # keeps code changes small (Dietrich Gebert)
claude plugin install i-have-adhd@soes-skills   # short answers that start with the next step (Ayoub Ghriss)
```

Other tools I use:

- [21st.dev](https://21st.dev): components and interactions to adapt into your own design
- [skillui](https://skillui.vercel.app): pulls a site's colors, type, and spacing into a design skill
- [Playwright](https://playwright.dev): screenshots reference sites and records the build for review
- [Stageshow](https://github.com/benjitaylor/skills) by Benji Taylor: product demos that look like the real app

## Other agents

```sh
npx skills add Soe-Reh/soes-skills
npx skills add Soe-Reh/soes-skills --skill spec
```

## Credits

My skills, manifests, and docs are [MIT](LICENSE). `frontend-design` (Apache-2.0), `better-ui`, and `animate` (MIT) are unchanged copies with their own licenses. See [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).
