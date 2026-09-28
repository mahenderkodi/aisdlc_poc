"""Gate 1 checks for sdlc-intent.
Run from the repo root:  python .claude/skills/sdlc-intent/scripts/check_intent.py <slug>
Exit 0 = pass, 1 = problems found."""
import re, sys
from pathlib import Path

if len(sys.argv) != 2:
    sys.exit("usage: check_intent.py <slug>")
slug = sys.argv[1]
f = Path("intent") / slug / "intent.md"
if not f.exists():
    sys.exit(f"STOP: {f} not found")
text = f.read_text(encoding="utf-8-sig")
problems, warnings = [], []

# 1. Frontmatter
fm = re.match(r"---\n(.*?)\n---\n", text.replace("\r\n", "\n"), re.S)
if not fm:
    problems.append("frontmatter block (--- ... ---) missing")
else:
    for key in ("id", "slug", "title", "originator", "product_owner", "status", "created", "baseline"):
        if not re.search(rf"^{key}:\s*\S", fm.group(1), re.M):
            problems.append(f"frontmatter: '{key}' missing or empty")

# 2. Required sections, in order
sections = ["Problem", "Proposed outcome", "Success criteria", "Requirements in this intent",
            "Affected users and systems", "Constraints", "Out of scope", "Open questions", "Decision log"]
pos = -1
for s in sections:
    m = re.search(rf"^## {re.escape(s)}\s*$", text, re.M)
    if not m:
        problems.append(f"section missing: ## {s}")
    elif m.start() < pos:
        problems.append(f"section out of order: ## {s}")
    else:
        pos = m.start()

# 3. Every active baseline item is either in this intent or explicitly left out
ID = r"(?:BR|RULE|API|DATA|TECH|NFR|CON|ASM)-\d{2,}"
baseline = set()
for rf in Path("requirements").glob("0*.md"):
    for line in rf.read_text(encoding="utf-8-sig").splitlines():
        m = re.search(rf"\*\*({ID})\*\*", line)
        if m and "~~" not in line and "withdrawn" not in line.lower():
            baseline.add(m.group(1))
mentioned = set(re.findall(ID, text))
for missing in sorted(baseline - mentioned):
    problems.append(f"baseline item {missing} is neither covered nor listed as 'not in this intent'")
for unknown in sorted(mentioned - baseline):
    problems.append(f"intent mentions {unknown}, which is not an active baseline item")

# 4. Every success criterion points to requirement IDs
sc = re.search(r"^## Success criteria\s*$(.*?)^## ", text, re.M | re.S)
if sc:
    for line in sc.group(1).splitlines():
        if line.strip().startswith("- [") and not re.search(ID, line):
            problems.append(f"success criterion without requirement ID: {line.strip()[:70]}")

# 5. Soft checks (warnings only)
body = text[fm.end():] if fm else text
lines = [l for l in body.splitlines() if l.strip()]
if len(lines) > 90:
    warnings.append(f"{len(lines)} non-empty lines - is this still one page? consider splitting")
for word in ("controller", "endpoint", "table ", "class ", "repository", "microservice"):
    if word in body.lower():
        warnings.append(f"design word '{word.strip()}' found - intent should not contain design")

print(f"intent: {f}  baseline items: {len(baseline)}  referenced: {len(mentioned & baseline)}")
for w in warnings: print("  warning:", w)
if problems:
    print(f"\nFAIL - {len(problems)} problem(s):")
    for p in problems: print("  -", p)
    sys.exit(1)
print("PASS - intent ready for Gate 1")