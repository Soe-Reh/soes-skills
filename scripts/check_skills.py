"""Check every skills/*/SKILL.md: frontmatter, name matches folder, description present and short, license for bundled skills."""
import json, pathlib, re, sys

root = pathlib.Path(__file__).resolve().parent.parent
bundled = {u["skill"] for u in json.loads((root / "UPSTREAM.json").read_text())}
errors = []
dirs = sorted(p for p in (root / "skills").iterdir() if p.is_dir())
for d in dirs:
    f = d / "SKILL.md"
    if not f.exists():
        errors.append(f"{d.name}: missing SKILL.md"); continue
    m = re.match(r"^---\n(.*?)\n---\n", f.read_text(), re.S)
    if not m:
        errors.append(f"{d.name}: no frontmatter"); continue
    fm = m.group(1)
    name = re.search(r"^name:\s*(.+)$", fm, re.M)
    if not name or name.group(1).strip() != d.name:
        errors.append(f"{d.name}: name must equal folder name")
    desc = re.search(r"^description:\s*(.*)$", fm, re.M)
    if not desc:
        errors.append(f"{d.name}: missing description")
    elif d.name not in bundled and (not desc.group(1).startswith("Use when") or len(desc.group(1)) > 500):
        errors.append(f"{d.name}: own-skill description must start 'Use when' and be <=500 chars")
    if d.name in bundled and not list(d.glob("LICENSE*")):
        errors.append(f"{d.name}: bundled skill needs its LICENSE")
for b in bundled - {d.name for d in dirs}:
    errors.append(f"{b}: in UPSTREAM.json but no folder")
print("\n".join(errors) or f"ok: {len(dirs)} skills")
sys.exit(1 if errors else 0)
