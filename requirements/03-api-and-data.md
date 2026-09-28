---
file: api-and-data
baseline: draft
updated: 2026-09-28
---
# API and data needs
> What the system must allow and keep — not the design. Endpoints, tables and types are decided in the spec (Stage 2).

## 1. API needs
- **API-01** An employee can apply leave with: type, from date, to date, reason. The employee is always the caller from X-User-Id; employee id is not sent in the body; nobody applies for someone else. (src: S5 L2; S1 L7; S4 L8; DEC-09) → OQ-06
- **API-02** An employee can get their leaves + balance, including status pending / approved / rejected. (src: S5 L3; S2 L9)
- **API-03** A manager can list pending requests for their team (direct reports only). (src: S5 L4; S3 L3; DEC-06)
- **API-04** A manager can approve / reject with comment, in one API call. (src: S5 L5; S3 L4; S2 L8) → OQ-10

## 2. Data needs
### employee
- **DATA-01** employee keeps: id, name, email, manager id. Loaded as seed data at startup (CON-03). (src: S5 L8; DEC-10)

### leave balance
- **DATA-02** leave balance keeps: employee, type, year, total, used. Loaded as seed data at startup (CON-03). (src: S5 L9; DEC-05; DEC-10) → OQ-26

### leave request
- **DATA-03** leave request keeps: id, employee, type, from, to, days, status, reason, manager comment, created time. (src: S5 L10) → OQ-18

## 3. Relationships stated by sources
- **DATA-04** An employee has a manager, referenced by manager id; the manager is also an employee (team = employees whose manager_id is the manager; a manager's leave is approved by their own manager). (src: S5 L8; DEC-06; DEC-07)
- **DATA-05** A leave balance belongs to an employee and is kept by type and calendar year. (src: S5 L9; DEC-05)
- **DATA-06** A leave request belongs to an employee. (src: S5 L10)
