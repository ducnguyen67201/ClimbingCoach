---
name: climbing-day-adjust
description: Update a climbing journey and current weekly plan when a planned climbing day changes. Use when Codex is asked to swap climbing days, skip a day, move a session, climb harder, climb softer, downgrade to recovery, add an extra hard day, or adjust a 3-day climbing week based on fatigue, schedule, skin, pain, or motivation.
---

# Climbing Day Adjust

## Overview

Use this skill to change the current weekly climbing plan without rebuilding the whole week from scratch. Preserve the goal of three useful climbing days per week unless the user explicitly asks for a different week.

## Default Files

- Prefer `/Users/ducmac/Desktop/workspace/climbingcoach/journey.md` when it exists.
- If the user gives another path, use that path.
- If the journey path is unclear, use `/Users/ducmac/Desktop/workspace/climbingcoach/climbing-plan/scripts/find_journey.py`.
- Read `references/day-adjustment-rules.md` before modifying the plan.
- After editing, run `/Users/ducmac/Desktop/workspace/climbingcoach/climbing-plan/scripts/quality_check.py` against the repo or edited document.

## Workflow

1. Read the current plan and the recent `Past Week Log`.
2. Identify the requested adjustment type: skip, swap, harder, softer, recovery, or extra.
3. Check recovery signals: skin, finger pain, shoulder pain, sleep, soreness, and last hard session.
4. Update only the affected day and downstream recovery spacing unless the whole plan is now stale.
5. Keep the weekly load coherent: avoid stacking max finger strength, hard board climbing, and heavy pulling on consecutive days.
6. Add a dated entry under `## Plan Adjustment Log` describing what changed and why.
7. If useful, run `scripts/record_adjustment.py` to create or append the log entry, then manually update the affected plan bullets.
8. Tell the user the new plan for the changed day and the next session to do.

## Adjustment Types

- **Skip**: mark the day as skipped, preserve the most important stimulus later in the week if recovery allows, and reduce accessories.
- **Swap**: move one planned day to another date while keeping hard days separated by at least one rest or easy day.
- **Harder**: increase intensity only when recovery is good. Progress one variable: grade, load, or number of quality attempts.
- **Softer**: reduce intensity but keep skill value. Use technique volume, easy mileage, mobility, or recovery work.
- **Recovery**: replace climbing with mobility, walking, light antagonist work, or full rest.
- **Extra**: add only low-impact movement or technique unless the user is clearly recovered and the week has enough rest.

## Output Format

When responding after an update, keep it concise:

```markdown
Updated `journey.md`.

Change: ...
Do today: ...
Next session: ...
Watch: ...
```

## Resource Use

- `references/day-adjustment-rules.md`: load before making training changes.
- `scripts/record_adjustment.py`: append a structured adjustment entry to the journey document.
