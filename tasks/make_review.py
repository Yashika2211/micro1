"""Regenerate tasks/REVIEW.md from tasks/tasks.jsonl.

Usage: python tasks/make_review.py
"""
import json
from pathlib import Path

HERE = Path(__file__).parent


def cell(text):
    return str(text).replace("|", "\\|").replace("\n", " ")


def main():
    tasks = [json.loads(line) for line in (HERE / "tasks.jsonl").read_text().splitlines() if line.strip()]
    verified = sum(t["verified_by_expert"] for t in tasks)
    out = [
        "# Expert review of expected answers",
        "",
        f"Verified: **{verified} / {len(tasks)}**. An answer is final only once `verified_by_expert` is `true` in `tasks.jsonl`.",
        "",
        "To verify a task: check the expected answer and rationale, then set `verified_by_expert: true`"
        " (or tell Claude what to fix) and rerun `python tasks/make_review.py`.",
        "",
        "| ID | Category | Difficulty | Expected answer | Rationale | Sources | Verified |",
        "|---|---|---|---|---|---|---|",
    ]
    for t in tasks:
        out.append("| " + " | ".join(cell(x) for x in [
            t["id"], t["category"], t["difficulty"], t["expected_answer"],
            t["rationale"], "; ".join(t["sources"]),
            "yes" if t["verified_by_expert"] else "**no**",
        ]) + " |")
    out += ["", "## Prompts", ""]
    for t in tasks:
        out += [f"### {t['id']}", "", "```text", t["prompt"], "```", ""]
        if t["rubric"]:
            out += ["Rubric:", ""] + [f"- ({c['weight']}) {c['criterion']}" for c in t["rubric"]] + [""]
    (HERE / "REVIEW.md").write_text("\n".join(out))
    print(f"Wrote REVIEW.md ({len(tasks)} tasks, {verified} verified)")


if __name__ == "__main__":
    main()
