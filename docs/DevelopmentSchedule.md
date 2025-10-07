## Development Schedule — Bridge Crew Agentic Workflow (GitHub + Docker)

### Overview
Phased plan to implement the agentic workflow, focusing on GitHub and Docker to ensure reproducibility and avoid host-specific scripts.

### Milestones
- M0: Foundations — Docs, roles, prompts, GitHub/Docker scaffolding
- M1: Tooling Parity — Local Docker matches CI; baseline CI runs
- M2: Pilot Sprint — One end-to-end story through the workflow
- M3: Quality Gates — Lint, tests, security scans enforced
- M4: Observability — Logs/metrics stored; decision records standardized
- M5: Harden & Expand — Wider agent roles; risk mitigations applied
- M6: Launch — Stable workflow with acceptance criteria and SLAs

### Week-by-Week Plan (6 weeks)
Week 1 — Foundations
- Finalize SRS, Architecture, Roles, Workflow docs
- Add GitHub templates (PR, backlog issue)
- Add Docker image and docker-compose for local parity
- Define decision record template and communication protocol

Week 2 — Tooling Parity
- Validate local Docker workflows match CI runtime
- Create minimal GitHub Actions workflows (build, lint, test placeholders)
- Configure required PR checks and branch protections

Week 3 — Pilot Sprint
- Select one backlog item; Riker plans and delegates
- Specialists produce artifacts; PR via GitHub
- Run gates; Picard review and acceptance

Week 4 — Quality Gates
- Implement/enable linting and unit test suites
- Add security scanning (SAST and secret scans)
- Establish coverage thresholds and reporting

Week 5 — Observability and Reliability
- Add structured run logs and correlation IDs
- Store decision records; link to PRs
- Track flaky tests; stabilize CI (caching, retries)

Week 6 — Harden & Launch
- Address top risks from Risk Register
- Document runbooks; finalize SLAs and success metrics
- Run 2–3 items through the full workflow; launch

### Two-Week Sprint Cadence (example)
Day 1: Sprint Planning (Riker proposes; Picard prioritizes; estimates set)
Day 2–3: Implementation and initial PRs; CI gates run
Day 4–5: Reviews (Worf, Crusher), fixes, and merges
Day 6: Integration and staging validation; observability checks
Day 7: Demo to Picard; acceptance; retrospective and action items
Day 8–9: Harden gates; address performance/security follow-ups
Day 10: Prep next sprint; backlog refinement

### Responsibilities per Milestone
- Picard: Approvals, priority, acceptance
- Riker: Plans, delegation, risk management, PR composition
- Data: Analysis, repo context, metrics
- La Forge: Docker/CI parity, caching, reliability
- Worf: Security gates and reviews
- Troi: Requirement clarity and UX considerations
- Crusher: Test strategy, coverage, release readiness

### Deliverables and Gates
- Deliverables: PRs with templates, ADRs, test reports, scan results, logs
- Gates: Required checks (lint/test/scan), human reviews (Picard + relevant specialists)

### Dependencies
- GitHub repository access and protections
- Docker (Engine) local and within CI runners
- Secrets configured for CI jobs (if needed)

### Calendar Template (copy/paste)
- Weekly: Planning (Mon), Daily sync (Tu–Th), Review/Demo (Fri), Retro (Fri)
- Monthly: Architecture review and risk review


