## Bridge Crew Agentic Workflow Documentation

This documentation defines an agentic development workflow modeled after the Enterprise bridge crew. The primary user is Captain Picard (Product Owner), and the primary agent is Commander Riker (Lead Engineer/Orchestrator). Specialist agents reflect core engineering roles.

### Contents
- **SRS**: Overall goals, requirements, success criteria (`docs/SRS.md`)
- **Architecture**: Components, integration points, data flows (`docs/Architecture.md`)
- **Roles**: Bridge-crew personas, responsibilities, RACI overview (`docs/Roles.md`)
- **Workflow**: Planning, execution, approvals, and communication (`docs/Workflow.md`)
- **Operations**: Runtime, observability, incident response (`docs/Operations.md`)
- **Communication**: Message standards and decision records (`docs/Communication.md`)
- **Prompts**: Persona prompt templates (`docs/Prompts/`)
- **Support**: RACI, testing, risk, glossary, templates (`docs/RACI.md`, `docs/TestingStrategy.md`, `docs/RiskRegister.md`, `docs/Glossary.md`, `docs/Templates/Backlog.md`)
- **Changelog**: Documentation change history (`docs/CHANGELOG.md`)
 - **Schedule**: Detailed development schedule and milestones (`docs/DevelopmentSchedule.md`)
 - **ADRs**: Decision records (`docs/ADR/`)
 - **Dev Setup**: Containerized developer setup (`docs/DevSetup.md`), contributing (`CONTRIBUTING.md`)
 - **Language Tooling**: Language-agnostic baseline and options (`docs/LanguageTooling.md`)

### How to use
- **Start with the SRS** to align on scope and non-functional requirements.
- **Review Roles** to select which specialist agents to enable.
- **Follow Workflow** to run ceremonies and daily execution.
- **Adopt Prompts** for each persona; tailor guardrails to your tooling.
- **Operationalize** with `Operations.md` and `TestingStrategy.md`.

### Conventions
- Documentation changes are tracked in `docs/CHANGELOG.md`.
- Use decision records referenced in `Communication.md` for key choices.


