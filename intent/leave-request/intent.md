---
id: INT-001
slug: leave-request
title: Apply and approve leave with correct balances
originator: Ganesh Kumar S (Product Owner)
product_owner: Ganesh Kumar S
status: draft        # draft | accepted | rejected | specified | planned | implemented | released
created: 2026-09-28
baseline: c5fe796a8a4aabc18fdc499e2a41e9eef5325e9c
---

# Intent: Apply and approve leave with correct balances

## Problem
Leave requests arrive by email, managers answer by email and HR copies the result into Excel (BR-01).
Emails get lost, so employees do not know where their request stands. The Excel balances are wrong, and HR spends **2 days every month** correcting them (BR-02).

## Proposed outcome
Employees apply for their own leave in one system. Their manager approves or rejects it there. The balance is always right because the system counts days, checks the balance and updates it on approval (BR-03). Leadership sees this working in an API-only demo by end of October.

## Success criteria
- [ ] An employee can apply for Annual or Sick leave for themselves only (type, from date, to date, reason). Any other type is refused (BR-04, API-01, RULE-01, DEC-09).
- [ ] Days are counted start to end with both days included, weekends and holidays included and no half days, so one day off = 1 day (RULE-11, DEC-04).
- [ ] For both Annual and Sick, a request above the available balance (total − approved − pending) is refused with a message that says the requested and available days. A request for exactly the available balance is accepted (RULE-02, RULE-03, RULE-05, DEC-01, DEC-02).
- [ ] A request that overlaps any pending or approved leave of the same employee, fully or partly, is refused. A request that overlaps only a rejected one is accepted (RULE-06, DEC-03).
- [ ] A request that crosses the calendar year end is refused (RULE-12, DEC-05).
- [ ] An employee with no manager cannot apply; the refusal says there is no approver (RULE-14, DEC-07).
- [ ] A new request is pending. The employee sees all their own requests with status and their balance per type for the year (BR-06, BR-07, API-02, RULE-09, DATA-05).
- [ ] A manager sees all pending requests of their direct reports in one list, and nobody else's (BR-08, API-03, RULE-13, DEC-06).
- [ ] A manager approves or rejects in a single call with a comment. A rejection without a reason is refused (BR-05, BR-09, API-04, RULE-07).
- [ ] A manager cannot decide their own leave or a request from outside their team. A manager's own leave is decided by their own manager (RULE-08, RULE-13, DATA-04, DEC-07).
- [ ] Only a pending request can be decided. A second decision on an approved or rejected request is refused (RULE-09, DEC-08).
- [ ] On approval the balance is checked again and then reduced by the request's days, and it never goes negative (RULE-03, RULE-05, RULE-10, DEC-02).
- [ ] Each request keeps its employee, type, dates, days, status, reason, manager comment and created time (DATA-03, DATA-06).
- [ ] Employees, managers and yearly balances are present at start from seed data, with no function to create them (CON-03, DATA-01, DATA-02, DEC-10).
- [ ] No personal data appears in the logs (NFR-01).
- [ ] The leadership demo shows apply → approve/reject → updated balance by the date agreed in OQ-22 (CON-01, CON-02).

## Requirements in this intent
| Group | IDs |
|---|---|
| Business requirements | BR-01, BR-02, BR-03, BR-04, BR-05, BR-06, BR-07, BR-08, BR-09 |
| Business rules | RULE-01, RULE-02, RULE-03, RULE-05, RULE-06, RULE-07, RULE-08, RULE-09, RULE-10, RULE-11, RULE-12, RULE-13, RULE-14 |
| API and data needs | API-01, API-02, API-03, API-04, DATA-01, DATA-02, DATA-03, DATA-04, DATA-05, DATA-06 |
| Tech, NFR, constraints | TECH-01, TECH-02, TECH-03, TECH-04, TECH-05, TECH-06, TECH-07, TECH-08, NFR-01, CON-01, CON-02, CON-03, ASM-02 |
| Decisions applied | DEC-01, DEC-02, DEC-03, DEC-04, DEC-05, DEC-06, DEC-07, DEC-08, DEC-09, DEC-10 |

**Not in this intent:** BR-10 (no UI; the baseline puts it out of scope) · BR-11 (no cancel; the baseline puts it out of scope) · ASM-01 (a future UI team is unconfirmed, and nothing is built for it now; see OQ-21) · DEC-11 (it concerns source provenance and does not affect the product).

## Affected users and systems
| Who / what | How they are affected |
|---|---|
| Employee | Applies for leave and follows its status and balance without email |
| Manager | Decides their direct reports' requests from one list |
| HR | No manual Excel balance fixing. Their role in the system is still open (OQ-14) |
| Leadership | Sees the demo (CON-02) |
| Email + Excel process | Replaced for leave requests and balances |

## Constraints
- Tech is fixed by TECH-01 to TECH-08. The spec adds no other stack.
- Caller identity is TECH-06 only (no real sign-in).
- API only, with no UI (CON-01). Seed data only (CON-03).
- ASM-02: the API needs list is a starting list, not a final one.
- Demo deadline is end of October (CON-02).

## Out of scope
- UI (BR-10, CON-01) and cancelling a request (BR-11).
- Creating employees, managers or balances through the system (CON-03).
- Carry-forward, pro-rata for joiners, and half days (RULE-02, RULE-11).
- Anything listed in OQ-21 (notifications, real sign-in, HR reports) until the Product Owner confirms it.

## Open questions
| OQ | Question (short) | Owner |
|---|---|---|
| OQ-06 | Apply validation: is a reason required, are past dates allowed, from > to, maximum length, which error | Priya (HR) |
| OQ-10 | Is the comment optional on approve? Is the rejection reason the same as the manager comment? | Ravi (Eng Manager) |
| OQ-12 | Caller identity missing, empty or unknown: what happens? | Ganesh (Tech lead) |
| OQ-14 | Does HR have any role in the system? | Priya (HR) |
| OQ-15 | Which fields count as personal data for logs? | Ganesh (Tech lead) |
| OQ-16 | Tests: Testcontainers or H2? | Ganesh (Tech lead) |
| OQ-17 | Does "simple" imply any measurable need? | Ganesh Kumar S (PO) |
| OQ-18 | Must the system keep who decided and when? | Ganesh (Tech lead) |
| OQ-19 | Any volume or response-time needs for the POC or demo? | Ganesh Kumar S (PO) |
| OQ-20 | Is the rough API needs list confirmed and complete? | Ganesh (Tech lead) |
| OQ-21 | Are notifications, real sign-in and HR reports out of scope? Is a future UI a need today? | Ganesh Kumar S (PO) |
| OQ-22 | Exact demo date and what the demo must show | Ganesh Kumar S (PO) |
| OQ-24 | Two decisions, or two overlapping applies, at the same moment | Ganesh (Tech lead) |
| OQ-25 | Approval re-check: is the request itself left out of pending? If the re-check fails, is the approval refused or the request rejected? | Priya (HR) |
| OQ-26 | Which years are seeded? What happens when applying for a year with no balance? | Priya (HR) |

## Decision log
| Date | Gate | Decision | By | Notes |
|---|---|---|---|---|
| 2026-09-28 | Draft | Written from baseline c5fe796 | Claude | status draft |
