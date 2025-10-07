## ADR 0001 — Adopt GitHub and Docker for Workflow

Status: Accepted
Date: 2025-10-07

### Context
We need a reproducible, host-agnostic developer experience and a first-class CI platform. The team operates on multiple OSes; Windows PowerShell should be avoided for core orchestration in favor of containers.

### Decision
Adopt GitHub as the primary code hosting, issues, and PR review platform. Use GitHub Actions for CI/CD. Containerize development and execution environments using Docker and docker-compose for local parity with CI.

### Consequences
- Pros: Reproducibility, simpler onboarding, consistent CI parity.
- Cons: Docker dependency; learning curve for compose; runner limits on Actions.

### References
- `docs/Operations.md`
- `docs/DevelopmentSchedule.md`
- `.github/workflows/ci.yml`

