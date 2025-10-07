## [Backlog] Observability: Structured logging with correlation IDs

### Problem Statement
Introduce structured JSON logging with correlation IDs to enable traceability across orchestrator and agents.

### Acceptance Criteria
- [ ] Provide logging utility emitting JSON with ts, level, event, correlationId, attributes.
- [ ] Integrate logging in Riker.plan/delegate and Data.perform.
- [ ] Tests validate JSON structure.

### Links
- Code: `src/core/observability/logging.py`, `src/core/orchestrator/riker.py`, `src/core/agents/data.py`


