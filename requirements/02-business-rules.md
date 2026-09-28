---
file: business-rules
baseline: draft
updated: 2026-09-28
---
# Business rules

## 1. Rules and validations
- **RULE-01** Only 2 leave types for now: Annual and Sick. (src: S1 L9)
- **RULE-02** Annual = 18 days per year, Sick = 12 days per year. (src: S1 L10) → OQ-05
- **RULE-03** An employee cannot apply more than the available balance. (src: S2 L6) → OQ-02
- **RULE-04** ⚠ Sick leave: employees can apply even if balance is 0, "we adjust later". Conflicts with RULE-05. (src: S2 L10) → OQ-01
- **RULE-05** ⚠ Sick leave should also check balance, "otherwise people misuse it". Conflicts with RULE-04. (src: S3 L6) → OQ-01
- **RULE-06** The same employee cannot have two leaves on the same dates. (src: S2 L7) → OQ-03
- **RULE-07** A manager must give a reason when rejecting. (src: S2 L8) → OQ-10
- **RULE-08** A manager should NOT approve their own leave. (src: S3 L5) → OQ-08
- **RULE-09** ⚠ Leave status is one of: pending / approved / rejected (source lists the statuses the employee should see). (src: S2 L9) → OQ-09

## 2. Calculations
- **RULE-10** Balance should reduce automatically after approval. (src: S1 L8) → OQ-02
- **RULE-11** Days = count all days from start to end (weekends also counted for POC). (src: S5 L11) → OQ-04

## 3. Edge cases found
| Edge case | Covered by | Open question |
|---|---|---|
| Sick leave applied when balance is 0 | RULE-04, RULE-05 (conflict) | OQ-01 |
| Request for exactly the available balance / one day more | RULE-03 | OQ-02 |
| Two pending requests, each within balance, together above it | — | OQ-02 |
| Balance too low at approval time although it was enough at apply time | — | OQ-02 |
| Request partly overlapping another request | RULE-06 | OQ-03 |
| Request on dates of an earlier rejected request | — | OQ-03 |
| Start date = end date (1 day or 0?) | RULE-11 | OQ-04 |
| Half-day leave | — | OQ-04 |
| From date after to date; dates in the past; very long leave | — | OQ-06 |
| Missing reason when applying | — | OQ-06 |
| Leave spanning year end (which year's balance) | — | OQ-05 |
| Employee joining mid-year; unused balance at year end | — | OQ-05 |
| Manager's own leave; employee with no manager | RULE-08 | OQ-08 |
| Manager deciding a request outside their team | — | OQ-07 |
| Approving or rejecting an already decided request | — | OQ-09 |
| Approve without comment | — | OQ-10 |
| Two decisions on the same request at the same time; two overlapping applies at the same time | — | OQ-24 |
| Missing or unknown X-User-Id header | — | OQ-12 |
| Apply with an employee id different from the caller | — | OQ-11 |
