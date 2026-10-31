# Expert review of expected answers

Verified: **0 / 10**. An answer is final only once `verified_by_expert` is `true` in `tasks.jsonl`.

To verify a task: check the expected answer and rationale, then set `verified_by_expert: true` (or tell Claude what to fix) and rerun `python tasks/make_review.py`.

| ID | Category | Difficulty | Expected answer | Rationale | Sources | Verified |
|---|---|---|---|---|---|---|
| itx-001 | control | easy | 124800 | Standard deduction Rs 75,000 (new regime, s.16(ia)) -> taxable Rs 16,00,000. Slabs FY25-26 (s.115BAC(1A) as amended by Finance Act 2025): 4-8L @5% = 20,000; 8-12L @10% = 40,000; 12-16L @15% = 60,000 -> 1,20,000. No 87A rebate (income > 12L). Cess 4% = 4,800. Total 1,24,800. | Finance Act 2025, s.115BAC(1A) slabs; s.16(ia) standard deduction Rs 75,000 | **no** |
| itx-002 | control | easy | 111800 | Taxable = 12,00,000 - 50,000 (std deduction, old regime) - 1,50,000 (80C) - 25,000 (80D) = 9,75,000. Old slabs: 2.5-5L @5% = 12,500; 5-9.75L @20% = 95,000 -> 1,07,500. No 87A (income > 5L). Cess 4% = 4,300. Total 1,11,800. | Finance Act 2025, First Schedule Part III (old regime rates); ss.80C, 80D, 16(ia) | **no** |
| itx-003 | stale_rule | medium | 0 | Taxable = 12,75,000 - 75,000 = 12,00,000. Slab tax = 20,000 + 40,000 = 60,000. s.87A rebate (new regime, FY25-26): total income <= 12,00,000, rebate up to 60,000 -> tax nil. Cess on nil = 0. | s.87A as amended by Finance Act 2025; s.115BAC(1A) | **no** |
| itx-004 | calc_error | hard | 10400 | Taxable = 12,10,000. Slab tax = 60,000 + 10,000 x 15% = 61,500. Marginal relief under s.87A (new regime): tax cannot exceed income above 12L = 10,000. Tax 10,000 + cess 4% = 400 -> 10,400. | s.87A second proviso (marginal relief), Finance Act 2025 | **no** |
| itx-005 | rule_interaction | hard | 41600 | Salary taxable 9,00,000; total income 11,00,000 (<= 12L, so 87A applies). Tax on normal income: 20,000 + 10,000 = 30,000, fully rebated under 87A. Rebate is NOT available against tax on special-rate income (s.111A) per the Finance Act 2025 amendment. Basic exemption already exhausted by salary. STCG tax 20% x 2,00,000 = 40,000 + cess 1,600 = 41,600. EXPERT CHECK: confirm 87A exclusion for s.111A income for FY25-26. | s.87A as amended by Finance Act 2025 (no rebate on special-rate income); s.111A as amended by Finance (No.2) Act 2024 (20%) | **no** |
| itx-006 | stale_rule | medium | 25000 | s.112A for transfers on/after 23 Jul 2024: 12.5% on LTCG exceeding Rs 1,25,000. (3,25,000 - 1,25,000) x 12.5% = 25,000. Basic exemption already used by salary. | s.112A as amended by Finance (No.2) Act 2024 | **no** |
| itx-007 | rule_interaction | hard | 449102 | Proviso to s.112(1) (Finance (No.2) Act 2024): for land/building acquired before 23 Jul 2024, a resident individual/HUF may compute tax as lower of (a) 12.5% without indexation = 60,00,000 x 12.5% = 7,50,000, or (b) 20% with indexation: indexed cost = 30,00,000 x 376/167 = 67,54,491; LTCG = 22,45,509; tax = 4,49,102. Lower = 4,49,102. EXPERT CHECK: CII 376 for FY25-26. | s.112(1) proviso, Finance (No.2) Act 2024; CBDT notification of CII for FY 2025-26 | **no** |
| itx-008 | calc_error | hard | 1227200 | Slab tax on 51L: 3,00,000 (up to 24L) + 27,00,000 x 30% = 11,10,000. Surcharge 10% = 1,11,000. Marginal relief: tax at 50L = 10,80,000; tax+surcharge capped at 10,80,000 + 1,00,000 = 11,80,000 (surcharge reduced to 70,000). Cess 4% = 47,200. Total 12,27,200. | Finance Act 2025, First Schedule Part III (surcharge and marginal relief); s.115BAC(1A) | **no** |
| itx-009 | missed_clarification | judgment | Cannot be determined without the acquisition date (and residency/other facts); should ask or give conditional answers. | The answer depends on the acquisition date (STCG at slab rates vs LTCG; indexation option only for pre-23-Jul-2024 acquisitions), residency (option only for residents), and exemptions. A confident single number is wrong. | s.112(1) proviso, Finance (No.2) Act 2024; ss.2(42A), 54EC, 54F | **no** |
| itx-010 | missed_clarification | judgment | Depends on the HRA exemption amount; new regime approx Rs 81,900 vs old regime approx Rs 1,17,000 before HRA; break-even HRA exemption approx Rs 1.69 lakh. | New: 14L - 75k = 13.25L -> 60,000 + 18,750 = 78,750 (no marginal relief: 78,750 < 1.25L) + cess = 81,900. Old (no HRA): 14L - 50k - 1.5L - 2L = 10L -> 1,12,500 + cess = 1,17,000. Old wins only if HRA exemption > about 1,68,750. Answer depends on missing HRA facts. | s.115BAC(1A) and (2); s.10(13A) and Rule 2A (HRA); s.24(b) | **no** |

## Prompts

### itx-001

```text
Assume FY 2025-26 (AY 2026-27), a resident individual below 60 years of age, and no income other than what is stated. A salaried employee has gross salary of Rs 16,75,000 and opts for the new tax regime under section 115BAC. There are no other deductions or exemptions. What is the total tax payable including health and education cess?

Show your working. End your response with exactly one line in the form 'FINAL ANSWER: <amount in rupees as a plain integer>'.
```

### itx-002

```text
Assume FY 2025-26 (AY 2026-27), a resident individual below 60 years of age, and no income other than what is stated. A salaried employee opts for the OLD tax regime. Gross salary is Rs 12,00,000. She invested Rs 1,50,000 in PPF (section 80C) and paid a health insurance premium of Rs 25,000 for herself and her spouse (section 80D). No HRA or other exemptions. What is the total tax payable including cess?

Show your working. End your response with exactly one line in the form 'FINAL ANSWER: <amount in rupees as a plain integer>'.
```

### itx-003

```text
Assume FY 2025-26 (AY 2026-27), a resident individual below 60 years of age, and no income other than what is stated. A salaried employee has gross salary of Rs 12,75,000 and opts for the new tax regime. No other income, deductions or exemptions. What is the total tax payable including cess?

Show your working. End your response with exactly one line in the form 'FINAL ANSWER: <amount in rupees as a plain integer>'.
```

### itx-004

```text
Assume FY 2025-26 (AY 2026-27), a resident individual below 60 years of age, and no income other than what is stated. A salaried employee has gross salary of Rs 12,85,000 and opts for the new tax regime. No other income, deductions or exemptions. What is the total tax payable including cess?

Show your working. End your response with exactly one line in the form 'FINAL ANSWER: <amount in rupees as a plain integer>'.
```

### itx-005

```text
Assume FY 2025-26 (AY 2026-27), a resident individual below 60 years of age, and no income other than what is stated. An individual opts for the new tax regime. Gross salary is Rs 9,75,000. In January 2026 she also sold listed equity shares (STT paid on purchase and sale) held for 8 months, making a short-term capital gain of Rs 2,00,000 under section 111A. What is her total tax payable including cess?

Show your working. End your response with exactly one line in the form 'FINAL ANSWER: <amount in rupees as a plain integer>'.
```

### itx-006

```text
Assume FY 2025-26 (AY 2026-27), a resident individual below 60 years of age, and no income other than what is stated. An individual's taxable salary (after standard deduction) is Rs 15,00,000 under the new regime. On 15 August 2025 he sold listed equity shares (STT paid on purchase and sale) bought in 2021, realising a long-term capital gain of Rs 3,25,000 under section 112A. What is the income tax attributable to this capital gain alone, before surcharge and cess?

Show your working. End your response with exactly one line in the form 'FINAL ANSWER: <amount in rupees as a plain integer>'.
```

### itx-007

```text
Assume FY 2025-26 (AY 2026-27), a resident individual below 60 years of age, and no income other than what is stated. A resident individual sold a residential house on 10 October 2025 for Rs 90,00,000. He bought it in FY 2010-11 for Rs 30,00,000; no improvements, no transfer expenses, and he will not claim any exemption under sections 54/54EC/54F. Cost Inflation Index: FY 2010-11 = 167, FY 2025-26 = 376. Compute the income tax on this long-term capital gain before surcharge and cess, choosing the option that legally minimises tax.

Show your working. End your response with exactly one line in the form 'FINAL ANSWER: <amount in rupees as a plain integer>'.
```

### itx-008

```text
Assume FY 2025-26 (AY 2026-27), a resident individual below 60 years of age, and no income other than what is stated. An individual under the new tax regime has total taxable income of Rs 51,00,000, entirely from salary (already net of standard deduction). What is the total tax payable including surcharge and cess?

Show your working. End your response with exactly one line in the form 'FINAL ANSWER: <amount in rupees as a plain integer>'.
```

### itx-009

```text
My father sold a plot of land in September 2025 for Rs 80 lakh. He had bought it for Rs 20 lakh. How much capital gains tax will he have to pay?

End your response with exactly one line in the form 'FINAL ANSWER: <your answer or recommendation in one sentence>'.
```

Rubric:

- (0.3) Asks for or flags the acquisition date / holding period as necessary (short-term vs long-term, and pre/post 23 July 2024)
- (0.3) Explains that for land acquired before 23 Jul 2024 a resident individual may choose the lower of 12.5% without indexation or 20% with indexation
- (0.2) Flags residency status and/or other income, or exemptions (54EC / 54F) as affecting the final liability
- (0.2) Does not present a single unconditional tax figure as the answer; any numbers are clearly labelled as illustrative under stated assumptions

### itx-010

```text
I'm salaried with a gross salary of Rs 14,00,000 for FY 2025-26. I pay Rs 2,00,000 interest on a home loan for the flat I live in, invest Rs 1,50,000 under 80C, and my salary includes HRA. Which tax regime should I choose, old or new?

End your response with exactly one line in the form 'FINAL ANSWER: <your answer or recommendation in one sentence>'.
```

Rubric:

- (0.3) Identifies that the HRA exemption (needs rent paid, basic salary, metro/non-metro) is missing and decisive
- (0.3) Computes new-regime tax correctly (about Rs 81,900 including cess) and notes s.24(b) interest on self-occupied property is not allowed in the new regime
- (0.2) Computes old-regime tax before HRA correctly (about Rs 1,17,000 including cess) or gives the break-even HRA exemption (about Rs 1.69 lakh)
- (0.2) Gives a conditional recommendation rather than an unconditional one
