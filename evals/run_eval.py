#!/usr/bin/env python3
"""Run the ste-ko scenarios under three conditions with the Claude Code CLI.

Conditions:
    none   no extra instructions
    short  the short rules block (RULES below)
    full   the whole SKILL.md appended to the system prompt

Each call runs in an empty directory with settings, skills, and tools off,
so project files and user settings cannot change the result.
Output files are resumable: an existing output is not run again.

Usage:
    run_eval.py run  [--model sonnet] [--effort low] [--gens 3] [--out evals/out]
    run_eval.py summarize [--out evals/out]

Needs: the `claude` CLI, logged in. Each call uses account quota.
The numbers measure form only. They do not measure answer quality.
"""
import argparse
import json
import os
import subprocess
import sys
import tempfile
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from reader_metrics import analyze, hard_violations  # noqa: E402

SKILL = HERE.parent / "skills" / "ste-ko" / "SKILL.md"
SCENARIOS = HERE / "scenarios.json"
CONDITIONS = ["none", "short", "full"]

RULES = """답변 문체 규칙:
- 첫 문장에 결론을 쓴다. 한 문장에는 동작이나 사실을 하나만 쓴다.
- 설명 문장은 25어절 이하, 절차 문장은 20어절 이하로 쓴다.
- 능동태로 쓴다. 한 대상에는 한 단어만 쓴다.
- 줄표(—)와 세미콜론(;)을 쓰지 않는다. 인사말과 맺음말을 쓰지 않는다.
- 확인한 것과 확인하지 못한 것을 구분한다. 확신 수준을 바꾸지 않는다.
- 절차는 번호 목록, 비교는 표로 쓴다.
- 사용자가 준 오류 문구와 로그는 원문 그대로 인용한다."""


def call(prompt, cond, model, effort, cwd):
    cmd = ["claude", "-p", "--setting-sources", "", "--disable-slash-commands",
           "--tools", "", "--no-session-persistence",
           "--model", model, "--effort", effort]
    if cond == "short":
        cmd += ["--append-system-prompt", RULES]
    elif cond == "full":
        cmd += ["--append-system-prompt", SKILL.read_text(encoding="utf-8")]
    cmd.append(prompt)
    last = ""
    for attempt in range(3):
        r = subprocess.run(cmd, capture_output=True, text=True, cwd=cwd, timeout=300)
        if r.returncode == 0 and r.stdout.strip():
            return r.stdout.strip()
        last = f"code {r.returncode}; stderr: {r.stderr[:200]!r}; stdout: {r.stdout[:200]!r}"
        time.sleep(5 * (attempt + 1))
    raise RuntimeError(f"claude failed after 3 tries: {last}")


def run(args):
    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    scenarios = json.loads(SCENARIOS.read_text(encoding="utf-8"))
    with tempfile.TemporaryDirectory() as cwd:
        for g in range(1, args.gens + 1):
            for s in scenarios:
                for cond in CONDITIONS:
                    path = out / f"{cond}__{s['id']}__g{g}.md"
                    if path.exists() and path.stat().st_size > 0:
                        continue
                    text = call(s["prompt"], cond, args.model, args.effort, cwd)
                    path.write_text(text + "\n", encoding="utf-8")
                    print(f"done {cond:5s} {s['id']} g{g}", flush=True)
    summarize(args)


def summarize(args):
    out = Path(args.out)
    keys = ["eojeol", "sentences", "avg_eojeol_per_sentence", "max_eojeol_in_sentence",
            "sentences_over_limit", "em_dash", "semicolon", "bold_spans", "headers",
            "list_items", "table_rows", "openers", "closers", "stock_phrases",
            "nominalizations", "end_formal", "end_polite", "end_plain"]
    quotes = {s["id"]: s["must_quote"] for s in json.loads(SCENARIOS.read_text(encoding="utf-8"))
              if s.get("must_quote")}
    rows = {}
    for cond in CONDITIONS:
        ms = []
        q_pass = q_total = 0
        for p in sorted(out.glob(f"{cond}__*__g*.md")):
            text = p.read_text(encoding="utf-8")
            ms.append(analyze(text))
            sid = p.name.split("__")[1]
            if sid in quotes:
                q_total += 1
                q_pass += all(q in text for q in quotes[sid])
        if not ms:
            continue
        n = len(ms)
        row = {k: round(sum(m[k] for m in ms) / n, 1) for k in keys}
        row["hard_violations"] = round(sum(hard_violations(m) for m in ms) / n, 2)
        row["n"] = n
        row["error_quote_pass"] = f"{q_pass}/{q_total}"
        rows[cond] = row
    cols = ["n"] + keys + ["hard_violations", "error_quote_pass"]
    print("\nmean per answer")
    print("| metric | " + " | ".join(rows) + " |")
    print("|---|" + "---|" * len(rows))
    for c in cols:
        print(f"| {c} | " + " | ".join(str(rows[k][c]) for k in rows) + " |")
    (out / "summary.json").write_text(json.dumps(rows, ensure_ascii=False, indent=2),
                                      encoding="utf-8")


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    sub = ap.add_subparsers(dest="cmd", required=True)
    r = sub.add_parser("run")
    r.add_argument("--model", default="sonnet")
    r.add_argument("--effort", default="low")
    r.add_argument("--gens", type=int, default=3)
    r.add_argument("--out", default=str(HERE / "out"))
    r.set_defaults(fn=run)
    s = sub.add_parser("summarize")
    s.add_argument("--out", default=str(HERE / "out"))
    s.set_defaults(fn=summarize)
    args = ap.parse_args()
    args.fn(args)


if __name__ == "__main__":
    main()
