---
file: api-and-data
baseline: draft
updated: 2026-09-28
---
# API and data needs
> What the system must allow and keep — not the design. Endpoints, tables and types are decided in the spec (Stage 2).

## 1. API needs
- **API-01** An employee can apply leave with: employee id, type, from date, to date, reason. (src: S5 L2; S1 L7) → OQ-06, OQ-11
- **API-02** An employee can get their leaves + balance, including status pending / approved / rejected. (src: S5 L3; S2 L9)
- **API-03** A manager can list pending requests for their team. (src: S5 L4; S3 L3) → OQ-07
- **API-04** A manager can approve / reject with comment, in one API call. (src: S5 L5; S3 L4; S2 L8) → OQ-10

## 2. Data needs
### employee
- **DATA-01** employee keeps: id, name, email, manager id. (src: S5 L8) → OQ-13

### leave balance
- **DATA-02** leave balance keeps: employee, type, year, total, used. (src: S5 L9) → OQ-05, OQ-13

### leave request
- **DATA-03** leave request keeps: id, employee, type, from, to, days, status, reason, manager comment, created time. (src: S5 L10) → OQ-18

## 3. Relationships stated by sources
- **DATA-04** ⚠ An employee has a manager, referenced by manager id (that the manager is also an employee is not stated). (src: S5 L8) → OQ-08
- **DATA-05** ⚠ A leave balance belongs to an employee and is kept by type and year. (src: S5 L9) → OQ-05
- **DATA-06** A leave request belongs to an employee. (src: S5 L10)
