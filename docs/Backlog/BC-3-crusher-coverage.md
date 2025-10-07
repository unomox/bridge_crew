## [Backlog] Crusher: Coverage threshold and reporting

### Problem Statement
Ensure baseline quality by enforcing a minimum test coverage in CI and surfacing coverage details.

### Acceptance Criteria
- [ ] Coverage enforced via pytest-cov with `--cov-fail-under`.
- [ ] Coverage printed in PR job logs.
- [ ] Crusher agent present in codebase.

### Constraints and Assumptions
- Threshold initial target: 80% (adjust in `pyproject.toml`).

### Risks
- Threshold may be too strict; tune post-pilot.

### Links
- Config: `pyproject.toml`
- CI: `.github/workflows/ci.yml`


