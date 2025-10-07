## [Backlog] La Forge: CI Docker layer caching and speedups

### Problem Statement
Reduce CI times by enabling Docker Buildx with local cache reuse across jobs.

### Acceptance Criteria
- [ ] Build, lint, and test jobs use Buildx with cache.
- [ ] Cache reuses layers across workflow steps.
- [ ] CI duration improves versus baseline.

### Constraints and Assumptions
- GitHub Actions runners; no external registry cache used in v1.

### Risks
- Cache invalidation; excessive cache size.

### Links
- Workflow: `.github/workflows/ci.yml`


