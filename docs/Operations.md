## Operations — Runtime, Observability, and Incident Response

### Environments
- Local developer environment via Docker and docker-compose:
  - Mount repository into container; run tools inside container.
  - Use the same images locally and in CI for parity.
- CI runners on GitHub Actions with pinned container images.

### Observability
- Structured logs with correlation IDs: planId, taskId, prId.
- Metrics: plan lead time, gate pass/fail, build duration, flaky rate.
- Traces for multi-agent task handoffs.
- Dashboards for runs, success rates, and regressions.
  - Implementation: `src/core/observability/logging.py` with JSON output and correlationId.

### Secrets and Access
- Least-privilege access for each agent to repos, CI, trackers.
- Use secret manager; never log secrets; rotate regularly.

### CI/CD Integration
- Pre-merge: lint, unit tests, security scans, SAST/secret scan.
- Post-merge: integration/e2e, deployment to staging; manual gate for prod.
- Neutral linters (markdownlint, yamllint, hadolint, actionlint) run inside the Docker image for portability.

### Incident Management
- On failure: Riker aggregates context, assigns owner (specialist), proposes fix.
- Create incident record with timeline, impacted scope, temporary mitigations.
- Post-incident review with action items tracked as backlog.

### Backups and Retention
- Retain decision records, logs, and metrics for retrospectives.
- Artifact registry for build outputs and test reports.


