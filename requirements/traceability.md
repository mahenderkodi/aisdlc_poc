---
file: traceability
updated: 2026-09-28
---
# Traceability
Stage 0 fills ID, summary and sources. Later stages fill the rest.

| ID | Summary | Sources | Intent | Spec section | Test |
|---|---|---|---|---|---|
| BR-01 | Current process: email + Excel | S1 L5 | | | |
| BR-02 | Problem: lost emails, wrong balances, 2 HR days/month | S1 L6 | | | |
| BR-03 | Goal: simple apply / approve system | S1 L7 | | | |
| BR-04 | Employee applies leave | S1 L7; S5 L2 | | | |
| BR-05 | Manager approves or rejects with comment | S1 L7; S5 L5 | | | |
| BR-06 | Employee sees status | S2 L9 | | | |
| BR-07 | Employee gets own leaves and balance | S5 L3 | | | |
| BR-08 | Manager lists direct reports' pending requests | S3 L3; S5 L4; DEC-06 | | | |
| BR-09 | Approve / reject in one API call | S3 L4 | | | |
| BR-10 | Out of scope: UI | S1 L11 | | | |
| BR-11 | Out of scope: cancel | S2 L11 | | | |
| RULE-01 | Leave types Annual and Sick only | S1 L9 | | | |
| RULE-02 | Annual 18, Sick 12 days per calendar year; no carry-forward / pro-rata | S1 L10; DEC-05 | | | |
| RULE-03 | Available = total − approved − pending; checked at apply and approve | S2 L6; DEC-02 | | | |
| ~~RULE-04~~ | withdrawn: DEC-01 | S2 L10; DEC-01 | | | |
| RULE-05 | Sick leave checks balance like Annual; no negative | S3 L6; DEC-01 | | | |
| RULE-06 | No overlap with pending/approved leaves | S2 L7; DEC-03 | | | |
| RULE-07 | Reason required on reject | S2 L8 | | | |
| RULE-08 | Manager cannot decide own leave; own manager decides it | S3 L5; DEC-07 | | | |
| RULE-09 | Statuses and transitions; approved/rejected final | S2 L9; DEC-08 | | | |
| RULE-10 | Balance reduces on approval | S1 L8; DEC-02 | | | |
| RULE-11 | Days = all days start to end inclusive; no half days | S5 L11; DEC-04 |
| RULE-12 | Request must fall inside one calendar year | S1 L10; DEC-05 | | | |
| RULE-13 | Team = direct reports; outside team refused | S3 L3; S5 L4; S5 L8; DEC-06 | | | |
| RULE-14 | No manager → cannot apply | S5 L8; DEC-07 | | | |
| API-01 | Apply leave as the caller (no employee id in body) | S5 L2; S1 L7; S4 L8; DEC-09 | | | |
| API-02 | Get my leaves + balance | S5 L3; S2 L9 | | | |
| API-03 | Manager lists direct reports' pending requests | S5 L4; S3 L3; DEC-06 | | | |
| API-04 | Manager approves / rejects with comment | S5 L5; S3 L4; S2 L8 | | | |
| DATA-01 | employee fields (seed data) | S5 L8; DEC-10 | | | |
| DATA-02 | leave balance fields (seed data) | S5 L9; DEC-05; DEC-10 | | | |
| DATA-03 | leave request fields | S5 L10 | | | |
| DATA-04 | employee → manager (also an employee) via manager id | S5 L8; DEC-06; DEC-07 | | | |
| DATA-05 | balance per employee, type, calendar year | S5 L9; DEC-05 | | | |
| DATA-06 | leave request → employee | S5 L10 | | | |
| TECH-01 | Java 21, Spring Boot 3.x, Maven | S4 L2 | | | |
| TECH-02 | Flyway migrations | S4 L4 | | | |
| TECH-03 | REST JSON, OpenAPI/Swagger | S4 L5 | | | |
| TECH-04 | Layered controller → service → repository | S4 L6 | | | |
| TECH-05 | JUnit 5 + Testcontainers or H2 | S4 L7 | | | |
| TECH-06 | X-User-Id header, no SSO; caller = applicant | S4 L8; DEC-09 | | | |
| TECH-07 | MySQL 8 in Docker (docker-compose) | S4 L3 | | | |
| TECH-08 | Run with mvn spring-boot:run | S4 L10 | | | |
| NFR-01 | No personal data in logs | S4 L9 | | | |
| CON-01 | API only, no UI | S1 L11 | | | |
| CON-02 | Leadership demo end of October | S1 L12 | | | |
| CON-03 | Seed data at startup; no create API | S5 L8; S5 L9; DEC-10 | | | |
| ASM-01 | ⚠ UI team may build on API later | S1 L11 | | | |
| ASM-02 | ⚠ S5 API list is "rough" | S5 L1 | | | |
