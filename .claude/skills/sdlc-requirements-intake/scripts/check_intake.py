"""Deterministic Gate 0 checks for sdlc-requirements-intake.
Run from the repo root:  python .claude/skills/sdlc-requirements-intake/scripts/check_intake.py
Exit code 0 = all checks pass, 1 = problems found (listed)."""
import re, sys
from pathlib import Path

REQ = Path("requirements")
RAW = REQ / "raw"
ITEM_FILES = ["01-business-requirements.md", "02-business-rules.md",
              "03-api-and-data.md", "04-tech-and-environment.md"]
ID_RE = re.compile(r"\*\*((?:BR|RULE|API|DATA|TECH|NFR|CON|ASM)-\d{2,})\*\*")
SRC_RE = re.compile(r"\(src:\s*([^)]+)\)")
problems = []

def fail(msg): problems.append(msg)

# 1. Manifest: every source listed and its file exists
manifest = RAW / "manifest.md"
if not manifest.exists():
    sys.exit("STOP: requirements/raw/manifest.md is missing")
sources = {}
for row in manifest.read_text(encoding="utf-8-sig").splitlines():
    m = re.match(r"\|\s*(S\d+)\s*\|\s*([^|]+?)\s*\|", row)
    if m:
        sid, rel = m.group(1), m.group(2)
        sources[sid] = RAW / rel
        if not (RAW / rel).exists():
            fail(f"manifest: {sid} file not found: {rel}")

# 2. Every requirement item has a unique ID and a valid source citation
ids, cited = {}, set()
for name in ITEM_FILES:
    f = REQ / name
    if not f.exists():
        fail(f"missing output file: {name}"); continue
    for n, line in enumerate(f.read_text(encoding="utf-8-sig").splitlines(), 1):
        for iid in ID_RE.findall(line):
            if iid in ids:
                fail(f"duplicate ID {iid} ({ids[iid]} and {name}:{n})")
            ids[iid] = f"{name}:{n}"
            src = SRC_RE.search(line)
            if not src:
                fail(f"{name}:{n} {iid} has no (src: ...)")
                continue
            for sid in re.findall(r"S\d+", src.group(1)):
                cited.add(sid)
                if sid not in sources:
                    fail(f"{name}:{n} {iid} cites unknown source {sid}")

# 3. Open questions: every OQ has an owner and a status
oq = REQ / "open-questions.md"
oq_ids = set()
if oq.exists():
    for row in oq.read_text(encoding="utf-8-sig").splitlines():
        cells = [c.strip() for c in row.strip().strip("|").split("|")]
        if cells and re.fullmatch(r"OQ-\d{2,}", cells[0]):
            oq_ids.add(cells[0])
            if len(cells) < 7 or not cells[4] or not cells[6]:
                fail(f"open-questions: {cells[0]} needs owner and status")
else:
    fail("missing output file: open-questions.md")

# 4. Coverage: every non-empty line of every .txt/.md source is in the ledger
cov = REQ / "coverage.md"
ledger = {}
if cov.exists():
    for row in cov.read_text(encoding="utf-8-sig").splitlines():
        cells = [c.strip() for c in row.strip().strip("|").split("|")]
        if len(cells) >= 4 and re.fullmatch(r"S\d+", cells[0]) and re.fullmatch(r"L\d+", cells[1]):
            ledger[(cells[0], int(cells[1][1:]))] = cells[3]
            for ref in re.findall(r"(?:BR|RULE|API|DATA|TECH|NFR|CON|ASM|OQ)-\d{2,}", cells[3]):
                if ref not in ids and ref not in oq_ids:
                    fail(f"coverage: {cells[0]} {cells[1]} maps to unknown ID {ref}")
else:
    fail("missing output file: coverage.md")

for sid, path in sources.items():
    if not path.exists():
        continue                      # already reported above
    if path.suffix.lower() not in (".txt", ".md"):
        print(f"note: {sid} is not plain text - check its page/slide coverage by hand")
        continue
    for n, line in enumerate(path.read_text(encoding="utf-8-sig").splitlines(), 1):
        if line.strip():
            target = ledger.get((sid, n))
            if target is None:
                fail(f"coverage: {sid} line {n} not in ledger: {line.strip()[:60]}")
            elif not target:
                fail(f"coverage: {sid} line {n} has empty 'Mapped to'")
    if sid not in cited and not any(k[0] == sid for k in ledger):
        fail(f"source {sid} is never cited")

# Report
print(f"sources: {len(sources)}  items: {len(ids)}  open questions: {len(oq_ids)}  ledger lines: {len(ledger)}")
if problems:
    print(f"\nFAIL - {len(problems)} problem(s):")
    for p in problems: print("  -", p)
    sys.exit(1)
print("PASS - all Gate 0 checks OK")