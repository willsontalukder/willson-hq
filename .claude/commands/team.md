---
description: Convene the specialist team on a goal — plan it, delegate to specialists, and report back.
argument-hint: <goal>
---

Goal: $ARGUMENTS

Act as team lead for Willson:
1. Ask the `planner` agent for a plan that assigns each task to a specialist.
2. Show Willson the plan in a few lines. If it involves anything destructive,
   costly, or outward-facing (sending, publishing, deploying), get approval first.
3. Delegate each task to its specialist agent, running independent tasks in parallel.
4. After any code change, run `code-reviewer` (and `security-auditor` for anything
   touching auth, data, or infrastructure), then fix the Must-fix items.
5. Report back: what was done, by whom, results, and open decisions.
