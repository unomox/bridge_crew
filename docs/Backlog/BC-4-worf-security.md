## [Backlog] Worf: Security scanning (Bandit, pip-audit)

### Problem Statement
Add Python security static analysis and dependency vulnerability scanning to CI.

### Acceptance Criteria
- [ ] Bandit runs on `src/` in CI security job.
- [ ] pip-audit runs against `requirements-dev.txt`.
- [ ] Findings reported in job logs.

### Constraints and Assumptions
- Allow non-blocking initially (informational); tighten later.

### Risks
- False positives; tune configuration later.

### Links
- CI workflow: `.github/workflows/ci.yml`


