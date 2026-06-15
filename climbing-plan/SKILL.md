---
name: climbing-plan
description: Create and maintain climbing training plans from a journey document. Use when Codex is asked to read the past week of climbing, summarize logged sessions, update a climbing journey, write next-week climbing plans, adjust 3-day-per-week Kilterboard or bouldering training, or maintain a V12 climbing goal without branded coach terminology.
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
7. Include warmup, primary climbing work, strength accessories, recovery, success criteria, and adjustment rules.
8. Preserve user logs exactly unless the user asks for cleanup.
9. Run `scripts/quality_check.py` against the repository or edited document before finishing.

## Planning Rules

- Treat the athlete's baseline as V9 outdoors, V10 Kilterboard, 3 climbing days per week, and a V12 Kilterboard goal by the end of 2026 unless the journey says otherwise.
- Prioritize finger strength, limit bouldering, pulling power, body tension, and technique under fatigue.
- Do not turn every week into a max week. Adjust volume down when the past week shows high fatigue, tweaky fingers, poor sleep, or repeated missed sessions.
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

**Day 1 - Max strength and limit board**
- ...

**Day 2 - Volume and technique**
- ...

**Day 3 - Power and project links**
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
