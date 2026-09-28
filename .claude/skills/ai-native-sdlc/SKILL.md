---
name: ai-native-sdlc
description: Router for the AI-native SDLC in this repo. Use when asked "where are we", "what's next", "which skill should I use", when starting any new piece of work, or when unsure which stage a change is in. Reads git branches, requirements baseline status and intent/*/intent.md status, then names the next skill, the file it will produce and the human gate that follows.
---

# AI-native SDLC — router

## 1. Find where the work is
Check, in this order:
1. `git log --merges --oneline` — which gates are already passed (`gate-N:` merges).
2. `requirements/` — does a baseline exist and is it merged (gate-0)?
3. `intent/<slug>/intent.md` — the `status:` field.

| What you find | Stage | Next skill | Produces | Next gate (who) |
|---|---|---|---|---|
| Raw inputs, no baseline | 0 Requirements | `sdlc-requirements-intake` | requirements/*.md | Gate 0 — Product Owner |
| Baseline merged, no intent | 1 Plan | `sdlc-intent` | intent/<slug>/intent.md | Gate 1 — Product Owner |
| intent `status: accepted` | 2 Design | `sdlc-spec` (+ doc and policy skills) | spec.md + docs/ | Gate 2 — Product Owner |
| intent `status: specified` | 3 Build | `sdlc-plan` (plan mode) | plan.md | Gate 3 — Engineer |
| intent `status: planned` | 3–4 Build/Test | implement; `sdlc-feedback-loop` | code + tests | checks green |
| intent `status: implemented` | 5 Deploy | `sdlc-pr-review`, `sdlc-release` | PR, VERSION, CHANGELOG | Gate 4 code owner · Gate 5 release manager |
| intent `status: released` | 6 Maintain | `sdlc-close-loop` | new intent from a breach | Gate 6 — Service owner |

A skill that does not exist yet in `.claude/skills/` → say so and stop; do not improvise its job.

## 2. Work that skips the chain
| Situation | Instead |
|---|---|
| Typo, dependency bump, small bug with a clear repro | failing test first, then fix (no intent) |
| Change to CLAUDE.md, a skill or a hook | run agent evals before merging |
| A rule that must never break | needs a hook, not only a skill |

## 3. Always
- Never skip a gate. The agent never approves its own work.
- Before starting, say: the skill you will use, the file you will produce, the gate that follows.
- Each stage works on its own branch: `req/…`, `intent/<slug>`, `spec/<slug>`, `plan/<slug>`, `feat/<slug>`.