"""Self-check an AI ideas file against the narrative validator."""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
import tempfile

from report_narrative import validate_narrative


def main(argv=None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--ideas", required=True)
    ap.add_argument("--template", required=True)
    ap.add_argument("--evidence", required=True)
    args = ap.parse_args(argv)
    with tempfile.NamedTemporaryFile(suffix=".json", delete=False) as tmp:
        out = tmp.name
    cmd = [sys.executable, "scripts/build_from_ideas.py", "--ideas", args.ideas,
           "--template", args.template, "--evidence", args.evidence, "--out", out]
    proc = subprocess.run(cmd, capture_output=True, text=True)
    if proc.returncode != 0:
        print(proc.stderr or proc.stdout)
        return 2
    with open(out, encoding="utf-8") as fh:
        narrative = json.load(fh)
    with open(args.evidence, encoding="utf-8") as fh:
        evidence = json.load(fh)
    fails = validate_narrative(narrative, evidence)
    if fails:
        print("IDEAS INVALID: %d error(s)" % len(fails))
        for item in fails:
            print("-", item)
        return 1
    print("IDEAS VALID")
    return 0


if __name__ == "__main__":
    sys.exit(main())
