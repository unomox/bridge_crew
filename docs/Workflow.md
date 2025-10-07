## Workflow — Ceremonies and Daily Operations

### Ceremonies
- **Backlog Refinement**: Picard + Riker shape items; Troi validates stakeholder intent; Worf flags security impacts; Crusher plans validation; La Forge checks feasibility.
- **Sprint Planning**: Riker proposes plan; specialists confirm estimates; risks recorded.
- **Daily Sync**: Brief updates; blockers surfaced; Riker rebalances tasks.
- **Review & Demo**: Specialists present; Riker summarizes; Picard accepts or requests changes.
- **Retro**: Metrics review; risks and improvements captured.

### Daily Execution Loop
1. Riker pulls prioritized item and drafts an execution plan.
2. Specialists produce artifacts and status updates.
3. Riker composes PR/MR with:
   - Linked issue/backlog item
   - Summary, rationale, decision links
   - Test notes and validation evidence
4. CI runs gates; Worf/Crusher review reports; La Forge resolves build issues.
5. Picard reviews; approve or request changes.

### Code References
- Orchestrator module: `src/core/orchestrator/riker.py`
- Base agent definitions: `src/core/agents/base.py`

### Approvals and Gates
- Human approvals required for scope changes, architecture, and releases.
- Automated gates: lint, unit/integration tests, security scans.
- Decision records required for meaningful trade-offs.

### Communication Protocol (see `docs/Communication.md`)
- Structured messages with: Context → Intent → Plan → Actions → Evidence → Next steps → Risks.
- Each artifact links to its decision record when applicable.


