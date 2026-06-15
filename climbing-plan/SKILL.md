---
name: climbing-plan
description: Create and maintain climbing training plans from a journey document. Use when Codex is asked to read the past week of climbing, summarize logged sessions, auto-discover upcoming Climbing Google Calendar blocks, update a climbing journey, write next-week climbing plans with exercise guide links, sync plan text into calendar event descriptions without changing event details, adjust 3-day-per-week Kilterboard or bouldering training, or maintain a V12 climbing goal without branded coach terminology.
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
3. Read `references/finger-strength-research-2026.md` when the user asks for research-backed planning, finger pain decisions, hangboard progression, V12 preparation, strength standards, or scientific evidence.
4. Read `references/exercise-guide.md` when the plan includes strength, mobility, core, hangboard, or technique exercises.
5. Extract the last 7 calendar days of climbing notes. Accept dated headings, checklists, or a `Past Week Log` section.
6. Summarize what changed: sessions completed, hard attempts, volume, board grades, finger work, pulling work, core work, recovery, skin, and pain signals.
7. If calendar sync is requested or implied, discover upcoming `Climbing` events first and use those exact dates/times as the training days.
8. Write a new `## Current Plan` for the next week. If a current plan already exists, move the old one under `## Plan History` before replacing it.
9. Keep the plan to 3 climbing days unless the user explicitly requests otherwise or the calendar only contains a different number of climbing blocks.
10. Include day-specific timing when the user provides weekdays/dates or when calendar events are discovered.
11. Include morning mobility, readiness check, session warmup, primary climbing work, strength accessories, cooldown, recovery, success criteria, and adjustment rules.
12. Include exercise guide links and brief execution descriptions for non-obvious exercises, either inline or as an `Exercise guide links` section.
13. Preserve user logs exactly unless the user asks for cleanup.
14. If the user asks to update calendar events, follow the Calendar Sync workflow below after the journey plan is updated.
15. Run `scripts/quality_check.py` against the repository or edited document before finishing.

## Planning Rules

- Treat the athlete's baseline as V9 outdoors, V10 Kilterboard, 3 climbing days per week, and a V12 Kilterboard goal by the end of 2026 unless the journey says otherwise.
- If the athlete reports inconsistent session quality, finger pain after hard Kilter attempts, or feeling like capacity is missing, prioritize a capacity block before max-output work.
- During a capacity block, bias toward repeatable submaximal board volume, 5x5-style climbing or strength, movement quality, and pain-free finger loading.
- Return to max finger strength, limit bouldering, and V11-V13 attempts only after sessions feel consistent and finger irritation is quiet for at least 2 weeks.
- Treat max hangs as a later high-intensity strength block, usually 1 to 2 sessions per week, only after a quiet-finger capacity phase.
- Keep finger pain at 0 to 3 out of 10. If pain is sharp, nervy, localized to a pulley, worsening during a session, or worse the next morning, remove hard crimping and recommend clinical assessment instead of training through it.
- Use taping only as support or proprioceptive feedback. Never use taping as permission to add max hangs or harder board attempts.
- Do not turn every week into a max week. Adjust volume down when the past week shows high fatigue, tweaky fingers, poor sleep, or repeated missed sessions.
- When the user gives specific training days or calendar events are discovered, map the core sessions onto those days and name the date and time for each session.
- Add a short morning routine for each climbing day: breathing, hips, thoracic spine, shoulders, wrists, fingers, and a readiness check.
- Add guide links and one-line execution cues for morning mobility, strength, core, fingerboard, and technique exercises when they appear in the plan.
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

**Day 1 - Weekday, YYYY-MM-DD - Capacity baseline**
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

**Day 3 - Weekday, YYYY-MM-DD - Capacity strength and links**
- Morning:
- Session warmup:
- Climb:
- Train:
- Cooldown:
- ...

**Recovery and guardrails**
- ...

**Exercise guide links**
- ...

**What to log next week**
- ...
```

## Resource Use

- `references/training-framework.md`: load before writing plans.
- `references/finger-strength-research-2026.md`: load for evidence-based planning, finger pain, hangboard progression, max-strength blocks, capacity blocks, or V12 readiness questions.
- `references/exercise-guide.md`: load when exercises or technique drills need execution links.
- `scripts/find_journey.py`: locate the journey file when the path is not provided.
- `scripts/quality_check.py`: scan edited files for accidental banned brand wording.

## Calendar Sync

When the user asks to put the climbing plan into Google Calendar, or when they call the skill expecting calendar-backed planning:

1. Use the Google Calendar connector.
2. Search from the moment the skill is called through the following 7 days with query `Climbing` in `America/Toronto`, unless the user gives another date range.
3. Treat discovered `Climbing` events as the source of truth for training dates and times.
4. Read matching events before writing.
5. For recurring events, update individual instances with `update_scope: this_instance`.
6. Put each day's plan in that day's event description: title line, then visually bold section headers for morning routine, session warmup, climb, train, cooldown, guide links, and log-after bullets. Prefer Calendar-safe bold Unicode heading text such as `𝗠𝗼𝗿𝗻𝗶𝗻𝗴 𝗽𝗿𝗲𝗽, 𝟴-𝟭𝟬 𝗺𝗶𝗻:` because the connector may escape raw HTML tags.
7. Do not create, delete, move, resize, rename, recolor, change attendees, change reminders, change location, add/remove Meet links, or change recurrence. Only update the event description.
8. If no matching event exists for a planned day, leave the calendar unchanged for that day and mention that no matching time block was found.
9. Re-read updated events and report exact dates whose descriptions changed.
