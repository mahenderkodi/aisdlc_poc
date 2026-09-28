---
file: tech-and-environment
baseline: draft
updated: 2026-09-28
---
# Tech, environment and constraints

## 1. Stated tech choices
- **TECH-01** Java 21, Spring Boot 3.x, Maven. (src: S4 L2)
- **TECH-02** Flyway for DB migrations. (src: S4 L4)
- **TECH-03** REST JSON API, OpenAPI/Swagger docs. (src: S4 L5)
- **TECH-04** Layered: controller -> service -> repository. (src: S4 L6)
- **TECH-05** JUnit 5 + Testcontainers or H2 for tests (decide). (src: S4 L7) → OQ-16
- **TECH-06** No real SSO: pass user id in a header for POC (X-User-Id). (src: S4 L8) → OQ-11, OQ-12

## 2. Environment (local / CI / deploy)
- **TECH-07** MySQL 8 running locally in Docker (docker-compose). (src: S4 L3)
- **TECH-08** Should run with: mvn spring-boot:run. (src: S4 L10)

## 3. Non-functional needs
- **NFR-01** Logs must not contain personal data. (src: S4 L9) → OQ-15

## 4. Constraints and milestones
- **CON-01** No UI for POC, only API. (src: S1 L11)
- **CON-02** Demo needed to leadership end of October. (src: S1 L12) → OQ-22

## 5. Assumptions (must be confirmed)
- **ASM-01** ⚠ Later a UI team may build on the API. (src: S1 L11) → OQ-21
- **ASM-02** ⚠ The API list in S5 is headed "API ideas (rough)"; it is used as the starting list until confirmed. (src: S5 L1) → OQ-20
