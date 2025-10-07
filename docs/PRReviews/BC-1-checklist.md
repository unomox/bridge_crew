## Bridge Crew Review Checklist — BC-1

### Riker (Orchestrator)
- [ ] Plan summarized; links to backlog and ADRs present
- [ ] Risks captured; next steps clear

### Data (Analysis)
- [ ] Execution plan tasks appropriate and scoped
- [ ] Code layout matches `docs/Architecture.md`

### La Forge (DevOps)
- [ ] CI runs green; Docker build reproducible
- [ ] Lint/test steps correct and cacheable

### Worf (Security)
- [ ] No secrets; gitleaks clean
- [ ] Dependencies minimal and pinned where required

### Crusher (Quality)
- [ ] Tests present and meaningful
- [ ] Formatting/linting pass (Ruff/Black, neutral linters)

### Notes
- PR body references: `docs/Backlog/BC-1-initialize-riker.md`

