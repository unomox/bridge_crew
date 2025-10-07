## Architecture — Bridge Crew Agentic Workflow

### Components
- **Orchestrator (Commander Riker)**: Plans work, delegates tasks, aggregates outputs, manages risks, drives approvals.
- **Specialists**:
  - Data: code analysis, data extraction, context building, automation.
  - La Forge: build systems, CI/CD, packaging, environments, infra.
  - Worf: security review, threat modeling, dependency and secret scanning.
  - Troi: UX/copy/stakeholder empathy, requirement refinement.
  - Crusher: quality engineering, test strategy, validation gates.
- **Adapters**: Repo, CI, issue tracker, knowledge base, secret manager.
- **Memory Layer**: Run history, decisions, embeddings, artifacts registry.
- **Observability**: Structured logs, metrics, traces, dashboards.
 - **Execution Environment**: Docker containers for agents; docker-compose for local orchestration; GitHub Actions for CI parity.

### Data Flows (high level)
1. Picard creates or refines backlog items.
2. Orchestrator plans and assigns tasks to specialists.
3. Specialists produce artifacts and status updates.
4. Orchestrator composes PRs/MRs and requests reviews.
5. CI runs automated gates; security and quality checks report back.
6. Picard approves; release pipeline executes; artifacts stored.

### Code Layout
- Orchestrator: `src/core/orchestrator/riker.py`
- Agent base types: `src/core/agents/base.py`

### Integration Points
- GitHub REST/GraphQL APIs for issues/PRs
- GitHub Actions workflows and artifacts
- Vector store and document store
- Secret manager (GitHub Secrets or external)

### Observability and Audit
- Correlation IDs per plan, task, and PR/MR
- Decision records linked from commits and PR descriptions
- Retained logs and metrics for retrospectives


