# Plan: Indian Income Tax Expert Eval (Step 0, awaiting approval)

## The gap (one sentence)
Frontier models confidently compute Indian individual income tax using **outdated or
mis-combined rules**: pre-2025 slabs, the old ₹7L rebate limit, pre-July-2024
capital-gains rates. They also apply the Section 87A rebate and other reliefs to income
where those reliefs don't apply, and they rarely ask for facts (regime, residency,
acquisition date) that change the answer.

## Scope
- **Tax year: FY 2025-26 (AY 2026-27)**, the year being filed in 2026. All expected
  answers are pinned to this year so they can be checked against the Finance Act 2025
  and current CBDT/e-filing guidance.
- Resident individuals, below 60, unless the task says otherwise.
- Out of scope: corporate tax, GST, TDS procedure, and the new Income Tax Act 2025
  (effective 1 Apr 2026). Its provisions could be a later extension.

## Failure categories
| Code | Category | Example of the failure |
|---|---|---|
| `stale_rule` | Applies a superseded slab, rate or limit | 87A rebate capped at ₹7L/₹25,000; LTCG at 10% with ₹1L exemption |
| `calc_error` | Right rule, wrong arithmetic | Marginal relief near ₹12L, surcharge plus marginal relief, 4% cess base |
| `rule_interaction` | Misses how two rules combine | 87A rebate wrongly offset against 111A/112A special-rate tax; loss set-off order |
| `missed_clarification` | Answers when a needed fact is missing | Doesn't ask regime, residency, or property acquisition date (pre/post 23 Jul 2024) |
| `control` | Easy baseline, models should pass | Plain salary under the new regime, no edge cases |

## Task mix (10 tasks)
- 2 control (easy)
- 6 edge cases (medium/hard) across `stale_rule`, `calc_error`, `rule_interaction`
- 2 judgment (`missed_clarification`): the correct answer flags the ambiguity or gives
  both branches

## Task schema (`tasks/tasks.jsonl`, one JSON object per line)
```json
{
  "id": "itx-003",
  "category": "rule_interaction",
  "difficulty": "hard",
  "prompt": "exact text sent to the model",
  "expected_answer": "62400",
  "grading_type": "numeric_tolerance",
  "tolerance": 1,
  "answer_regex": null,
  "rubric": null,
  "rationale": "why this is correct + section/source",
  "why_models_fail": "hypothesis",
  "sources": ["Finance Act 2025, First Schedule Part III", "s.87A proviso"],
  "verified_by_expert": false
}
```
- `grading_type`: `exact` | `numeric_tolerance` | `regex` | `rubric`
- `rubric` (rubric tasks only): `[{"criterion": "...", "weight": 0.4}, ...]`, weights sum to 1
- Every prompt ends with: *"End your response with a line: FINAL ANSWER: <value>"*

## Directory layout
```
micro1/
├── README.md               # the 8 required sections
├── PLAN.md                 # this file
├── config.yaml             # model IDs, temperature, runs, judge model
├── run_eval.py             # python run_eval.py --models all --runs 3 [--dry-run]
├── grader.py               # deterministic grading + LLM judge for rubric tasks
├── providers.py            # Anthropic / OpenAI / Google / mock adapters, retries
├── requirements.txt        # pinned
├── .env.example  .gitignore  make_zip.sh
├── tasks/
│   ├── tasks.jsonl
│   └── REVIEW.md           # verification table for the expert
├── grading/
│   ├── judge_prompt.md
│   ├── calibration/        # 15-20 hand-labeled responses + labels.jsonl
│   └── RELIABILITY.md      # accuracy + Cohen's kappa
├── tests/test_grader.py
└── results/
    ├── raw/<model>/<task_id>_run<n>.json
    ├── scores.csv  summary.md  scores_by_category.png
```

## Open questions for the expert
1. Your expertise for README section 3: years, role, day-to-day work.
2. Is FY 2025-26 the right year to pin, or do you want FY 2026-27 (Budget 2026)?
3. Any real case you've seen a model get wrong?
