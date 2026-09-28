---
file: business-rules
baseline: draft
updated: 2026-09-28
---
# Business rules

## 1. Rules and validations
- **RULE-01** Only 2 leave types for now: Annual and Sick. (src: S1 L9)
- **RULE-02** Annual = 18 days per year, Sick = 12 days per year. The year is the calendar year. Balances are loaded per year. No carry-forward, no pro-rata in the POC. (src: S1 L10; DEC-05) → OQ-26
- **RULE-03** An employee cannot apply more than the available balance. Available = total − approved − pending. Checked when applying and again when approving. The error explains requested vs available days. (src: S2 L6; DEC-02) → OQ-25
- ~~**RULE-04** Sick leave: employees can apply even if balance is 0, "we adjust later". (src: S2 L10)~~ withdrawn: DEC-01
- **RULE-05** Sick leave also checks the balance, exactly like Annual. No negative balance. (src: S3 L6; DEC-01)
- **RULE-06** The same employee cannot have two leaves on the same dates. Any overlap (full or partial) is refused. Only pending and approved requests count; rejected ones do not. (src: S2 L7; DEC-03)
- **RULE-07** A manager must give a reason when rejecting. (src: S2 L8) → OQ-10
- **RULE-08** A manager cannot approve or reject their own leave. A manager's leave is approved by their own manager. (src: S3 L5; DEC-07)
- **RULE-09** Leave status is one of: pending / approved / rejected. New requests start as pending. Only pending → approved and pending → rejected are allowed. Approved and rejected are final. (src: S2 L9; DEC-08)
- **RULE-12** A request must fall inside one calendar year; a request spanning year end is refused (apply twice). (src: S1 L10; DEC-05)
- **RULE-13** "My team" = direct reports only (employee.manager_id = me). A manager deciding a request outside their team is refused. (src: S3 L3; S5 L4; S5 L8; DEC-06)
- **RULE-14** An employee with no manager cannot apply leave (refused: no approver). (src: S5 L8; DEC-07)

## 2. Calculations
- **RULE-10** Balance should reduce automatically after approval. (src: S1 L8; DEC-02)
- **RULE-11** Days = count all days from start to end, start and end both included (same day = 1 day). Weekends and holidays are counted. No half days. (src: S5 L11; DEC-04)

## 3. Edge cases found
| Edge case | Covered by | Open question |
|---|---|---|
| Sick leave applied when balance is 0 | RULE-05 (refused) | OQ-01 → DEC-01 |
| Request for exactly the available balance / one day more | RULE-03 | OQ-02 → DEC-02 |
| Two pending requests, each within balance, together above it | RULE-03 (pending counts) | OQ-02 → DEC-02 |
| Balance too low at approval time although it was enough at apply time | RULE-03 (checked again at approval) | OQ-02 → DEC-02; OQ-25 |
| Request partly overlapping another request | RULE-06 (refused) | OQ-03 → DEC-03 |
| Request on dates of an earlier rejected request | RULE-06 (allowed) | OQ-03 → DEC-03 |
| Start date = end date (1 day or 0?) | RULE-11 (1 day) | OQ-04 → DEC-04 |
| Half-day leave | RULE-11 (no half days) | OQ-04 → DEC-04 |
| From date after to date; dates in the past; very long leave | — | OQ-06 |
| Missing reason when applying | — | OQ-06 |
| Leave spanning year end (which year's balance) | RULE-12 (refused) | OQ-05 → DEC-05 |
| Employee joining mid-year; unused balance at year end | RULE-02 (no pro-rata, no carry-forward) | OQ-05 → DEC-05 |
| Leave in a year with no balance loaded | — | OQ-26 |
| Manager's own leave; employee with no manager | RULE-08, RULE-14 | OQ-08 → DEC-07 |
| Manager deciding a request outside their team | RULE-13 (refused) | OQ-07 → DEC-06 |
| Approving or rejecting an already decided request | RULE-09 (final) | OQ-09 → DEC-08 |
| Approve without comment | — | OQ-10 |
| Two decisions on the same request at the same time; two overlapping applies at the same time | — | OQ-24 |
| Missing or unknown X-User-Id header | — | OQ-12 |
| Apply with an employee id different from the caller | API-01 (no employee id in body) | OQ-11 → DEC-09 |
