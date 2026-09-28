---
file: business-requirements
baseline: draft        # draft | accepted (Gate 0)
sources: S1..S5
updated: 2026-09-28
---
# Business requirements

## 1. Problem and goals
- **BR-01** Today leave requests come by email, the manager replies on email, and HR updates Excel. (src: S1 L5)
- **BR-02** Problem: emails get lost, the Excel balance is wrong, and HR spends 2 days every month fixing balances. (src: S1 L6)
- **BR-03** Goal: a simple system where an employee applies leave and a manager approves or rejects it. (src: S1 L7) → OQ-17

## 2. Users and roles
| Role | Can do | Cannot do | Source |
|---|---|---|---|
| Employee | apply leave for themselves (BR-04, API-01); see own leaves, status and balance (BR-06, BR-07) | apply more than available balance (RULE-03, RULE-05); have two overlapping leaves (RULE-06); apply across year end (RULE-12); apply with no manager (RULE-14); apply for someone else (API-01); cancel — not needed for now (BR-11) | S1 L7; S2 L6; S2 L7; S2 L9; S2 L11; S3 L6; S5 L2; S5 L3; DEC-01; DEC-05; DEC-07; DEC-09 |
| Manager | see all pending requests of their direct reports in one list (BR-08, RULE-13); approve or reject with comment (BR-05); their own leave is decided by their own manager (RULE-08) | approve or reject their own leave (RULE-08); decide a request outside their team (RULE-13); reject without a reason (RULE-07); change a decided request (RULE-09) | S1 L7; S2 L8; S3 L3; S3 L4; S3 L5; S5 L4; S5 L5; DEC-06; DEC-07; DEC-08 |
| HR | today updates Excel (BR-01); role in the new system not stated → OQ-14 | — | S1 L5 |

## 3. Functional requirements
- **BR-04** An employee can apply leave. (src: S1 L7; S5 L2)
- **BR-05** A manager can approve or reject a leave request, with comment. (src: S1 L7; S5 L5)
- **BR-06** An employee should see the status of their leave: pending / approved / rejected. (src: S2 L9)
- **BR-07** An employee can get their leaves and balance. (src: S5 L3)
- **BR-08** A manager wants to see all pending requests of their team in one list; "my team" = direct reports only. (src: S3 L3; S5 L4; DEC-06)
- **BR-09** Approve / reject should be one click (one API call). (src: S3 L4)

## 4. Main flows
Built only from items above; each step names its ID.
### Apply leave
1. Employee (the caller, from X-User-Id) applies leave with type, from date, to date and reason (BR-04, API-01).
2. Leave type must be Annual or Sick (RULE-01).
3. The employee must have a manager, otherwise the request is refused: no approver (RULE-14).
4. The request must fall inside one calendar year (RULE-12).
5. Days are counted from start to end, both included; weekends and holidays counted; no half days (RULE-11).
6. Request must not exceed the available balance = total − approved − pending, for Annual and Sick alike (RULE-03, RULE-05).
7. Request must not overlap, fully or partly, another pending or approved leave of the same employee (RULE-06).
8. The request starts as pending; the employee sees its status (RULE-09, BR-06).

### Approve or reject
1. Manager lists all pending requests of their direct reports (BR-08, RULE-13, API-03).
2. Manager approves or rejects in one API call, with comment (BR-05, BR-09, API-04).
3. Only requests of the manager's direct reports can be decided (RULE-13); a manager cannot decide their own leave (RULE-08).
4. Only a pending request can be decided; approved and rejected are final (RULE-09).
5. A reason is required when rejecting (RULE-07).
6. On approval the balance is checked again (RULE-03), then reduces automatically (RULE-10).
7. Employee sees the new status (BR-06, BR-07).

## 5. Out of scope
- **BR-10** Out of scope: UI — "No UI for POC, only API. Later a UI team may build on it". (src: S1 L11)
- **BR-11** Out of scope: cancel — "We don't need cancel for now." (src: S2 L11)
