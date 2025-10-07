## Pull Request Process — Bridge Crew

### Purpose
Standardize how PRs are prepared, reviewed by agents, and approved by Picard.

### Steps
1. Branch from `main` using `feature/<id>-<short-title>`.
2. Include description using the PR template; link backlog issue ("closes #<id>").
3. Ensure checks pass in CI: linters, Ruff/Black, Pytest, security scan.
4. Attach evidence: logs, test reports, decision records (ADRs), risk notes.
5. Agent reviews:
   - Data: analysis and context sanity
   - La Forge: CI/build reliability
   - Worf: security risks
   - Crusher: test strategy and coverage
   - Riker: orchestration summary and risks
6. Picard review and acceptance.

### Notes
- Keep PRs focused and incremental; avoid unrelated changes.
- Update docs and ADRs for notable decisions.


