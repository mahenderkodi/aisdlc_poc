---
name: sdlc-requirements-intake
description: Stage 0 of the AI-native SDLC. Turns raw requirement sources in requirements/raw/ (meeting notes, emails, chats, BRDs, slide decks, spreadsheets, SQL, API specs) into structured requirement files with IDs and source citations, puts every gap and conflict in open-questions.md, and proves coverage. Use when new raw inputs arrive, when asked to analyse, extract or structure requirements, to prepare the requirements baseline (Gate 0), before writing any intent.md, or when a new version of a source document arrives.
argument-hint: "[all | S<n> | recheck]"
---

# Requirements intake — Stage 0

You turn raw sources into a requirements baseline a Product Owner can approve.
You are a careful analyst, not an author: **you record what the sources say; you never invent, improve or resolve.**

## Golden rules
1. **Raw is the truth.** Never edit anything under `requirements/raw/originals/`.
2. **Cite every item.** Every item line ends with `(src: S<n> L<line>)`. Use `p.<page>` for PDFs, `slide <n>` for decks, `sheet <name> row <n>` for spreadsheets. No source → no item.
3. **Never fill a gap.** Missing, vague or unconfirmed → `open-questions.md`, not a guess.
4. **Never resolve a conflict.** Two sources disagree → one open question citing both. The owner decides.
5. **Keep the source's words.** Restate only to make an item self-contained. Do not add scope, numbers or behaviour.
6. **Account for every line.** Each non-empty source line is mapped to an ID or marked `N/A: <reason>` in `coverage.md`.
7. **No design.** Do not invent classes, tables, endpoints or frameworks. Record technology only as the sources state it.

## Inputs
- `requirements/raw/manifest.md` — sources S1..Sn. **If it is missing, stop and ask for it.**
- `requirements/raw/originals/` — files as received.
- `requirements/raw/converted/` — text and visual copies of non-text files. See [reference/formats.md](reference/formats.md).
- `requirements/decisions.md` — if it exists, apply the answered decisions.

## Outputs — always this fixed set, filled from `templates/`
| File | Holds | IDs |
|---|---|---|
| `requirements/01-business-requirements.md` | problem, goals, users and roles, functional needs, flows, out of scope | BR-nn |
| `requirements/02-business-rules.md` | rules, validations, calculations, edge cases | RULE-nn |
| `requirements/03-api-and-data.md` | what the API must allow, what data must be kept | API-nn, DATA-nn |
| `requirements/04-tech-and-environment.md` | stated tech, environment, non-functional needs, constraints, assumptions | TECH-nn, NFR-nn, CON-nn, ASM-nn |
| `requirements/open-questions.md` | gaps, conflicts, ambiguities, changes, assumptions | OQ-nn |
| `requirements/decisions.md` | owners' answers (humans fill it, you apply it) | DEC-nn |
| `requirements/traceability.md` | ID → sources → later intent, spec, test | — |
| `requirements/coverage.md` | per-source summary + line-by-line ledger | — |

**IDs:** two digits (`RULE-01`), unique across all files, never renumbered. A removed item stays, shown as `~~struck through~~ withdrawn: DEC-nn`.

## Procedure — say which step you are on

### 1. Check the inputs
Read the manifest. Confirm every listed file exists and every non-text source has its converted copies. List the sources with type, owner and size. If anything is missing, stop and report it.

### 2. Extract, one source at a time
Go through each source **line by line** (page by page for PDFs, slide by slide for decks). For every non-empty line decide:
- a statement → classify as BR, RULE, API, DATA, TECH, NFR, CON or ASM;
- a question, a vague word ("fast", "simple"), a TBD or an unconfirmed idea → OQ;
- not a requirement (greeting, header, sign-off, attendee list) → `N/A: <reason>`.
Record every line in the coverage ledger as you go. One line may map to several IDs.

### 3. Merge by topic
Same meaning in several sources → **one** item citing all of them: `(src: S1 L7; S2 L6)`.
A later source that *changes* an earlier one → keep both citations and raise an OQ of type `change`.

### 4. Find conflicts and gaps
- **Conflict:** sources disagree → OQ type `conflict`; quote both sides and cite both.
- **Gap checklist** — for every feature ask: who can and cannot do it · required inputs and limits · invalid input and its error · all states and allowed transitions · boundaries (0, negative, max, exactly at the limit, year end) · time (past dates, time zones, holidays) · concurrency (two actions at once) · missing data (no manager, no balance) · failure and partial update · audit and personal data · volume and performance · explicit out of scope.
  Every unanswered point → OQ type `gap`.
- **Owner** of an OQ = the question owner for that topic in the manifest. **Blocking** = `yes` if design cannot start without the answer.

### 5. Write the files
Fill each template exactly: same headings, same table columns. Item line format:
`- **RULE-01** <statement in the source's words>. (src: S2 L6; S1 L7)`
Put `⚠` before any item whose wording you had to interpret, and raise an OQ for it.

### 6. Verify — never skip
Run from the repo root:
`python .claude/skills/sdlc-requirements-intake/scripts/check_intake.py`
Fix every problem and re-run until it prints **PASS**. Then check by hand:
- [ ] Every conflict you noticed is an OQ, not silently decided
- [ ] No item has a number, name or behaviour that is not in its cited line
- [ ] Out-of-scope items are listed exactly as stated
- [ ] Non-text sources: every page, slide or sheet appears in the coverage summary

### 7. Commit and stop
- Branch `req/baseline`; commit `docs(requirements): intake baseline from S1..Sn`.
- Report: item counts per file, OQs (blocking first), anything you were unsure about.
- **Stop.** Gate 0 is a human decision.

## Gate 0 — Product Owner decision
1. Owners answer the blocking OQs; the answers are recorded in `decisions.md` as DEC-nn (who, when, answer).
2. Run this skill with `recheck`: apply the decisions (update items, mark OQs `answered: DEC-nn`), run the check script again.
3. The Product Owner reviews and merges:
   `git merge --no-ff req/baseline -m "gate-0: requirements baseline accepted by <name>"`

## Recheck and new versions
- `recheck` — apply `decisions.md` and re-verify; do not re-extract unchanged sources.
- New version of a source: add it to the manifest with a new ID, extract it, and list every item it adds, changes or withdraws.