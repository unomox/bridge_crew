## Contributing

### Workflow
- Use GitHub Issues with the Backlog template.
- Open PRs using the PR template; link issues ("closes #ID").
- Ensure CI checks pass (build, lint, tests, security scan).

### Coding and Docs
- Prefer containerized tools; avoid host-specific scripts.
- Update docs and ADRs for meaningful changes.
- Keep PRs focused and well-scoped.

### Reviews
- Riker consolidates; specialists review domain-specific aspects.
- Picard provides acceptance.

### Security and Quality
- No secrets in code; rely on GitHub Secrets.
- Tests and scans must pass for merge.

