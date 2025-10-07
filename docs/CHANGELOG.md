## Documentation Changelog

### 2025-10-07
- Initialize bridge-crew agentic workflow documentation set: SRS, Architecture, Roles, Workflow, Operations, Communication, RACI, Testing Strategy, Risk Register, Prompts, Templates, Glossary.
 - Standardize on GitHub and Docker; add DevelopmentSchedule; add GitHub templates and Docker scaffolding.
 - Add CI workflow, ADRs, DevSetup, CONTRIBUTING, CODEOWNERS, and issue config.
 - Add neutral lint baseline (markdownlint, yamllint, hadolint, actionlint), wire into CI, add LanguageTooling doc.
 - Select Python as primary language; add Ruff, Black, Pytest; update Docker, CI, and docs; scaffold src/ and tests/.
 - Week 3: Add Riker orchestrator skeleton, base agent interface, unit tests, and backlog entry BC-1.
 - Add Data specialist agent and integrate delegation path; add tests.
 - Week 3: BC-2 — Add La Forge agent and enable Docker Buildx layer caching in CI; add backlog entry.
 - Week 3: BC-3 — Add Crusher agent; enforce coverage with pytest-cov; update CI and docs; add backlog entry.
 - Week 3: BC-4 — Add Worf agent; integrate Bandit and pip-audit into CI; add backlog entry.
 - Week 3: BC-5 — Add Troi agent; enhance PR/backlog templates; update communication protocol; add backlog entry.
 - Week 3: BC-6 — Add structured JSON logging with correlation IDs; integrate into Riker and Data; tests and docs; add backlog entry.


