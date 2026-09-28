---
file: open-questions
updated: 2026-09-28
---
# Open questions
Types: conflict · gap · ambiguity · change · assumption
Status: open · answered: DEC-nn · deferred

| ID | Type | Question | Sources | Owner | Blocking | Status |
|---|---|---|---|---|---|---|
| OQ-01 | conflict | Can Sick leave be applied when balance is 0? HR: "Sick leave - employees can apply even if balance is 0, we adjust later". Manager: "Sick leave should also check balance, otherwise people misuse it". If allowed: what does "we adjust later" mean — may the balance go negative, is there a limit, who adjusts? | S2 L10; S3 L6 | Priya (HR) | yes | open |
| OQ-02 | gap | What is the "available balance"? Does it subtract pending (not yet approved) requests, or only approved ones ("reduce automatically after approval")? Is the balance checked only when applying, or again when approving (e.g. two pending requests that fit alone but not together)? What error does the employee get? | S2 L6; S1 L8 | Priya (HR) | yes | open |
| OQ-03 | gap | "Same employee cannot have two leaves on same dates" — does a partial overlap also count? Do rejected requests count, or only pending and approved ones? | S2 L7 | Priya (HR) | yes | open |
| OQ-04 | ambiguity | "Count all days from start to end" — are both start and end dates included (start = end → 1 day)? Are half days possible? Are public holidays counted like weekends? | S5 L11 | Priya (HR) | yes | open |
| OQ-05 | gap | "18 / 12 days per year" — which year (calendar or other)? For a leave spanning year end, which year's balance is used? How is the balance for a new year created? Carry-forward of unused days? Joiners mid-year (full or pro-rata)? | S1 L10; S5 L9 | Priya (HR) | yes | open |
| OQ-06 | gap | Validation of an apply request: is the reason required? Are past dates allowed? Is from date after to date rejected? Any maximum length of a leave? What error is returned for invalid input? | S5 L2 | Priya (HR) | no | open |
| OQ-07 | gap | Who is "my team" — only employees whose manager id is the manager (direct reports) or also indirect reports? Can a manager approve / reject a request outside their team? What happens if they try? | S3 L3; S5 L4; S5 L8 | Ravi (Eng Manager) | yes | open |
| OQ-08 | gap | "A manager should NOT approve his own leave" — who then approves a manager's leave? What happens for an employee with no manager id? May a manager reject their own leave? | S3 L5; S5 L8 | Ravi (Eng Manager) | yes | open |
| OQ-09 | gap | Statuses and transitions: is a new request always "pending"? Are pending → approved and pending → rejected the only allowed transitions? Can an approved or rejected request be changed again? Are there other statuses (cancel is out of scope)? | S2 L9; S2 L11 | Ravi (Eng Manager) | yes | open |
| OQ-10 | gap | S5 says "approve / reject with comment"; S2 requires a reason only when rejecting. Is the comment optional on approve? Is the rejection "reason" the same field as the "manager comment"? | S2 L8; S5 L5; S5 L10 | Ravi (Eng Manager) | no | open |
| OQ-11 | ambiguity | Apply leave takes "employee id" as input, while the caller is identified by the X-User-Id header. Can a user apply leave for another employee? If the two differ, which one is used or is it an error? | S5 L2; S4 L8 | Ganesh (Tech lead) | yes | open |
| OQ-12 | gap | What happens when the X-User-Id header is missing, empty, or names an unknown user? Which error is returned? | S4 L8 | Ganesh (Tech lead) | no | open |
| OQ-13 | gap | No source says how employees, their manager ids and their yearly balances get into the system (no API for them is listed). How are they created or loaded for the POC and demo? | S5 L8; S5 L9 | Ganesh (Tech lead) | yes | open |
| OQ-14 | gap | Does HR have any role in the new system (today HR updates Excel; HR says for Sick leave "we adjust later")? E.g. view all leaves, adjust balances? | S1 L5; S2 L10 | Priya (HR) | no | open |
| OQ-15 | ambiguity | "Logs must not contain personal data" — which fields count as personal data (name, email, employee id, leave reason, sick leave)? | S4 L9 | Ganesh (Tech lead) | no | open |
| OQ-16 | gap | Tests: Testcontainers or H2? The source says "(decide)". | S4 L7 | Ganesh (Tech lead) | no | open |
| OQ-17 | ambiguity | "Want a simple system" — does "simple" imply any measurable need, or is it only a description of the scope in S1 L7? | S1 L7 | Ganesh Kumar S (Product Owner) | no | open |
| OQ-18 | gap | Audit: the leave request data has no "decided by" or "decided time". Must the system keep who approved / rejected and when? | S5 L10 | Ganesh (Tech lead) | no | open |
| OQ-19 | gap | No volume or performance needs are stated (number of employees, team size, requests per day, response time). Are there any for the POC or demo? | — (gap checklist) | Ganesh Kumar S (Product Owner) | no | open |
| OQ-20 | ambiguity | S5 is headed "API ideas (rough)". Is this API list confirmed and complete for the POC? | S5 L1 | Ganesh (Tech lead) | no | open |
| OQ-21 | gap | Stated out of scope: UI and cancel. Please confirm whether these are also out of scope: email / notifications, public holidays, half days, real SSO, HR reports. Is "a UI team may build on it later" a requirement on the API today? | S1 L11; S2 L11 | Ganesh Kumar S (Product Owner) | no | open |
| OQ-22 | ambiguity | "Demo needed to leadership end of October" — what is the exact date, and what must the demo show? | S1 L12 | Ganesh Kumar S (Product Owner) | no | open |
| OQ-23 | ambiguity | Source provenance: the manifest says S1 was given by "Ganesh (eng), Priya (HR), Ravi", but S1 lists attendees "Mahender (eng), Rani (HR), Ravi". Which is correct? | S1 L3; manifest | Ganesh Kumar S (Product Owner) | no | open |
| OQ-24 | gap | Concurrency: what should happen if two decisions are made on the same request at the same time, or if an employee sends two overlapping requests at the same time? | S2 L7; S5 L5 | Ganesh (Tech lead) | no | open |
