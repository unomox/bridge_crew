## Testing Strategy — Quality Gates and Coverage

### Levels
- Unit tests: fast, isolated; target 80%+ critical paths.
- Integration tests: service boundaries and adapters.
- E2E tests: user flows; smoke on each PR, full on main nightly.
- Non-functional: performance budgets; security scans; accessibility checks.

### Gates
- Pre-merge: lint (markdownlint, yamllint, hadolint, actionlint), unit+integration, SAST/secret scans.
  - Python: add Ruff and Black checks; run Pytest.
  - Coverage: enforce threshold via pytest-cov; report term-missing.
- Pre-release: e2e, performance baseline, security review.
- Post-release: canary and monitoring alerts.

### Test Data and Environments
- Seed deterministic fixtures; avoid prod data.
- Environment parity: local mirrors CI where feasible.

### Flakiness and Reliability
- Track flaky tests; quarantine with expiry; prioritize fix.

### Reporting
- PR shows pass/fail, coverage delta, and critical findings. Neutral linters and Python checks run in CI via Docker for portability.


