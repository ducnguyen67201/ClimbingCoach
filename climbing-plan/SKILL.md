---
name: climbing-plan
description: Create and maintain climbing training plans from a journey document. Use when Codex is asked to read the past week of climbing, summarize logged sessions, update a climbing journey, write next-week climbing plans, sync climbing plans into Google Calendar events, adjust 3-day-per-week Kilterboard or bouldering training, or maintain a V12 climbing goal without branded coach terminology.
---

# Climbing Plan

## Overview

Use this skill to turn recent climbing logs into a focused next-week plan inside a single journey document. Keep the voice practical, direct, and athlete-specific.

## Default Files

- Prefer `/Users/ducmac/Desktop/workspace/climbingcoach/journey.md` when it exists.
- If the user gives another path, use that path.
- If the journey path is unclear, run `scripts/find_journey.py` from the likely workspace root and use the best match.
- If no journey document exists, create `journey.md` with the sections shown in the repository starter document.

## Workflow

1. Locate and read the journey document.
2. Read `references/training-framework.md` before writing or changing a plan.
3. Extract the last 7 calendar days of climbing notes. Accept dated headings, checklists, or a `Past Week Log` section.
4. Summarize what changed: sessions completed, hard attempts, volume, board grades, finger work, pulling work, core work, recovery, skin, and pain signals.
5. Write a new `## Current Plan` for the next week. If a current plan already exists, move the old one under `## Plan History` before replacing it.
6. Keep the plan to 3 climbing days unless the user explicitly requests otherwise.
7. Include day-specific timing when the user provides weekdays or dates.
8. Include morning mobility, readiness check, session warmup, primary climbing work, strength accessories, cooldown, recovery, success criteria, and adjustment rules.
9. Preserve user logs exactly unless the user asks for cleanup.
10. If the user asks to update calendar events, follow the Calendar Sync workflow below after the journey plan is updated.
11. Run `scripts/quality_check.py` against the repository or edited document before finishing.

## Planning Rules

- Treat the athlete's baseline as V9 outdoors, V10 Kilterboard, 3 climbing days per week, and a V12 Kilterboard goal by the end of 2026 unless the journey says otherwise.
- Prioritize finger strength, limit bouldering, pulling power, body tension, and technique under fatigue.
- Do not turn every week into a max week. Adjust volume down when the past week shows high fatigue, tweaky fingers, poor sleep, or repeated missed sessions.
- When the user gives specific training days, map the three core sessions onto those days and name the date for each session.
- Add a short morning routine for each climbing day: breathing, hips, thoracic spine, shoulders, wrists, fingers, and a readiness check.
- Write plans that can be executed in a normal gym session without needing extra explanation.
- Use neutral wording such as "climbing coach", "training plan", "weekly plan", or "board plan".
- Avoid the old app or coach brand name in every generated file and response.

## Journey Update Format

Use this structure when replacing `## Current Plan`:

```markdown
## Current Plan

### Week of YYYY-MM-DD

**Past week readout**
- ...

**Main focus**
- ...

**Day 1 - Weekday, YYYY-MM-DD - Max strength and limit board**
- Morning:
- Session warmup:
- Climb:
- Train:
- Cooldown:
- ...

**Day 2 - Weekday, YYYY-MM-DD - Volume and technique**
- Morning:
- Session warmup:
- Climb:
- Train:
- Cooldown:
- ...

**Day 3 - Weekday, YYYY-MM-DD - Power and project links**
- Morning:
- Session warmup:
- Climb:
- Train:
- Cooldown:
- ...

**Recovery and guardrails**
- ...

**What to log next week**
- ...
```

## Resource Use

- `references/training-framework.md`: load before writing plans.
- `scripts/find_journey.py`: locate the journey file when the path is not provided.
- `scripts/quality_check.py`: scan edited files for accidental banned brand wording.

## Calendar Sync

When the user asks to put the climbing plan into Google Calendar:

1. Use the Google Calendar connector.
2. Search bounded to the planned week with query `Climbing`.
3. Read matching events before writing.
4. For recurring Tuesday/Friday style events, update individual instances with `update_scope: this_instance` unless the user explicitly asks to change the full series.
5. Put each day's plan in that day's event description: title line, morning routine, session warmup, climb, train, cooldown, and log-after bullets.
6. Preserve existing title, time, attendees, color, reminders, location, and meeting links unless the user asks to change them.
7. If the journey has a planned climbing day but no matching calendar event exists, create a `Climbing` event at the user's established climbing block time when obvious from the week, usually 17:30-22:00 in `America/Toronto`.
8. Re-read updated events and report exact dates changed.
