#!/usr/bin/env python3
"""Weekly ai-discoverability cycle, meant for Windows Task Scheduler on the machine that holds the keys.

    python scripts/ai_discoverability_cycle.py            # refresh every review sheet tab, apply rows marked "fix", refresh the roster, commit + push
    python scripts/ai_discoverability_cycle.py --no-fix   # refresh only
    python scripts/ai_discoverability_cycle.py --no-git   # don't commit/push

Order: git pull -> --all --sheet (new checks appear as "open", vanished ones get "cleared <date>") -> --all --fix --apply --yes
(only rows a human set to "fix") -> --all (docs/ai-bot-policy.md) -> commit the change logs, client files and roster, push.
Everything it does is logged under changes/<provider>/<slug>/; the sheet tab is the queue and the audit trail.

Schedule (run once from PowerShell in the repo; Monday 07:10, after the weekend Ahrefs crawls):
    schtasks /Create /TN "LHF ai-discoverability weekly" /SC WEEKLY /D MON /ST 07:10 /TR "python C:\\Users\\greg\\Documents\\Low-Hanging-Fruit\\scripts\\ai_discoverability_cycle.py" /F
"""
import argparse, datetime, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LOG = ROOT / "changes" / "_cycle-ai-discoverability.log"

def run(args, check=False):
    print("$", " ".join(args), flush=True)
    r = subprocess.run(args, cwd=ROOT, text=True, capture_output=True)
    print(r.stdout, end=""); print(r.stderr, end="", file=sys.stderr)
    if check and r.returncode: sys.exit(f"failed: {' '.join(args)}")
    return r

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--no-fix", action="store_true"); ap.add_argument("--no-git", action="store_true")
    a = ap.parse_args()
    py = sys.executable; script = str(ROOT / "scripts" / "ai_discoverability.py")
    stamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    with LOG.open("a", encoding="utf-8") as log: log.write(f"\n=== {stamp} ===\n")
    if not a.no_git: run(["git", "pull", "--rebase", "--quiet"])
    r1 = run([py, script, "--all", "--sheet"])
    r2 = run([py, script, "--all", "--fix", "--apply", "--yes"]) if not a.no_fix else None
    r3 = run([py, script, "--all"])
    with LOG.open("a", encoding="utf-8") as log:
        for r in (r1, r2, r3):
            if r: log.write(r.stdout + (r.stderr or ""))
    if not a.no_git:
        run(["git", "add", "-A"])
        if run(["git", "diff", "--cached", "--quiet"]).returncode:
            run(["git", "commit", "-q", "-m", f"ai-discoverability cycle {stamp}"]); run(["git", "push", "-q"])
        else: print("nothing to commit")

if __name__ == "__main__":
    main()
