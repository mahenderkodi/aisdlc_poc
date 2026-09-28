---
file: coverage
updated: 2026-09-28
---
# Coverage

## Summary
| Source | Type | Non-empty lines / pages | Mapped | N/A | Unmapped |
|---|---|---|---|---|---|
| S1 | meeting notes | 11 | 8 | 3 | 0 |
| S2 | email | 11 | 6 | 5 | 0 |
| S3 | chat message | 5 | 4 | 1 | 0 |
| S4 | tech notes | 10 | 9 | 1 | 0 |
| S5 | API and data notes | 10 | 9 | 1 | 0 |

**Unmapped must be 0 for every source.**

## Ledger
| Source | Line | Text (first words) | Mapped to |
|---|---|---|---|
| S1 | L1 | Kickoff meeting - Leave … | N/A: title |
| S1 | L2 | Date: 28-Sep-2026 | N/A: date |
| S1 | L3 | Attendees: Mahender (eng) … | N/A: attendee list; manifest owner corrected per DEC-11 (OQ-23) |
| S1 | L5 | Today leave requests come by email … | BR-01; OQ-14 |
| S1 | L6 | Problem: emails get lost … | BR-02 |
| S1 | L7 | Want a simple system: employee applies … | BR-03, BR-04, BR-05, API-01; OQ-17 |
| S1 | L8 | Balance should reduce automatically … | RULE-10; OQ-02, OQ-25 |
| S1 | L9 | Only 2 leave types for now … | RULE-01 |
| S1 | L10 | Annual = 18 days per year … | RULE-02, RULE-12; OQ-05, OQ-26 |
| S1 | L11 | No UI for POC, only API … | BR-10, CON-01, ASM-01; OQ-21 |
| S1 | L12 | Demo needed to leadership … | CON-02; OQ-22 |
| S2 | L1 | From: Priya (HR) | N/A: email header |
| S2 | L2 | Subject: Leave rules for … | N/A: email subject |
| S2 | L4 | Hi Ganesh, | N/A: greeting |
| S2 | L5 | Rules we follow: | N/A: lead-in |
| S2 | L6 | 1. Employee cannot apply more … | RULE-03; OQ-02, OQ-25 |
| S2 | L7 | 2. Same employee cannot have two … | RULE-06; OQ-03, OQ-24 |
| S2 | L8 | 3. Manager must give a reason … | RULE-07, API-04; OQ-10 |
| S2 | L9 | 4. Employee should see status … | BR-06, RULE-09, API-02; OQ-09 |
| S2 | L10 | 5. Sick leave - employees can apply … | RULE-04 (withdrawn: DEC-01); OQ-01, OQ-14 |
| S2 | L11 | We don't need cancel for now. | BR-11; OQ-09, OQ-21 |
| S2 | L12 | Thanks, Priya | N/A: sign-off |
| S3 | L1 | Ravi (Eng Manager) - chat message | N/A: header |
| S3 | L3 | As a manager I want to see all pending … | BR-08, API-03, RULE-13; OQ-07 |
| S3 | L4 | Approve / reject should be one click … | BR-09, API-04 |
| S3 | L5 | A manager should NOT approve … | RULE-08; OQ-08 |
| S3 | L6 | Sick leave should also check balance … | RULE-05; OQ-01 |
| S4 | L1 | Tech notes (Ganesh) | N/A: header |
| S4 | L2 | Java 21, Spring Boot 3.x, Maven | TECH-01 |
| S4 | L3 | MySQL 8 running locally in Docker … | TECH-07 |
| S4 | L4 | Flyway for DB migrations | TECH-02 |
| S4 | L5 | REST JSON API, OpenAPI/Swagger docs | TECH-03 |
| S4 | L6 | Layered: controller -> service … | TECH-04 |
| S4 | L7 | JUnit 5 + Testcontainers or H2 … | TECH-05; OQ-16 |
| S4 | L8 | No real SSO: pass user id … | TECH-06, API-01; OQ-11, OQ-12 |
| S4 | L9 | Logs must not contain personal data | NFR-01; OQ-15 |
| S4 | L10 | Should run with: mvn spring-boot:run | TECH-08 |
| S5 | L1 | API ideas (rough) | ASM-02; OQ-20 |
| S5 | L2 | apply leave: employee id, type … | API-01, BR-04; OQ-06, OQ-11 |
| S5 | L3 | get my leaves + balance | API-02, BR-07 |
| S5 | L4 | manager: list pending for my team | API-03, BR-08, RULE-13; OQ-07 |
| S5 | L5 | manager: approve / reject with comment | API-04, BR-05; OQ-10, OQ-24 |
| S5 | L7 | Data | N/A: section header |
| S5 | L8 | employee: id, name, email, manager id | DATA-01, DATA-04, RULE-13, RULE-14, CON-03; OQ-07, OQ-08, OQ-13 |
| S5 | L9 | leave balance: employee, type, year … | DATA-02, DATA-05, CON-03; OQ-05, OQ-13, OQ-26 |
| S5 | L10 | leave request: id, employee, type … | DATA-03, DATA-06; OQ-10, OQ-18 |
| S5 | L11 | Days = count all days from start … | RULE-11; OQ-04 |
