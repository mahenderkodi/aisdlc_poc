---
file: decisions
updated: 2026-09-28
---
# Decisions
Filled by the question owners. The intake skill applies them on `recheck`.

| ID | Answers | Decision | Decided by | Date | Effect on items |
|---|---|---|---|---|---|
| DEC-01 | OQ-01 | Sick leave checks the balance exactly like Annual. No negative balance. | Priya (HR) + Ravi (Eng Manager) | 2026-09-28 | RULE-04 withdrawn, RULE-05 kept |
| DEC-02 | OQ-02 | Available = total − approved − pending. Checked when applying and again when approving. Error explains requested vs available days. | Priya (HR) | 2026-09-28 | RULE-03, RULE-10 |
| DEC-03 | OQ-03 | Any overlap (full or partial) is refused. Only pending and approved requests count; rejected ones do not. | Priya (HR) | 2026-09-28 | RULE-06 |
| DEC-04 | OQ-04 | Start and end dates are both included (same day = 1 day). No half days. Holidays and weekends are counted. | Priya (HR) | 2026-09-28 | RULE-11 |
| DEC-05 | OQ-05 | Calendar year. A request must fall inside one calendar year (spanning year end is refused — apply twice). Balances are loaded per year. No carry-forward, no pro-rata in the POC. | Priya (HR) | 2026-09-28 | RULE-02 |
| DEC-06 | OQ-07 | "My team" = direct reports only (employee.manager_id = me). Deciding outside the team is refused. | Ravi (Eng Manager) | 2026-09-28 | new rule |
| DEC-07 | OQ-08 | A manager's leave is approved by their own manager. An employee with no manager cannot apply (refused: no approver). A manager cannot approve or reject their own leave. | Ravi (Eng Manager) | 2026-09-28 | RULE-08 |
| DEC-08 | OQ-09 | New requests start as pending. Only pending → approved and pending → rejected are allowed. Approved and rejected are final. | Ravi (Eng Manager) | 2026-09-28 | RULE-09 |
| DEC-09 | OQ-11 | The employee is always the caller from X-User-Id. Employee id is not sent in the body; nobody applies for someone else. | Ganesh (Tech lead) | 2026-09-28 | API items |
| DEC-10 | OQ-13 | Employees, managers and yearly balances are loaded as seed data at startup. No API to create them in the POC. | Ganesh (Tech lead) | 2026-09-28 | new constraint |
| DEC-11 | OQ-23 | Attendee names in S1 are as written in the file; manifest owner column corrected to match. | Ganesh Kumar S (PO) | 2026-09-28 | manifest |
