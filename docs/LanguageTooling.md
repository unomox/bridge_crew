## Language and Tooling Options

This project is language-agnostic at the workflow layer. Until a language is selected, neutral linters run in CI via Docker:
- Markdown: markdownlint
- YAML: yamllint
- Dockerfiles: hadolint
- GitHub Actions: actionlint

Primary language selected: Python.

Python toolchain in use:
- Ruff (lint)
- Black (format check)
- Pytest (tests)

Configs: `pyproject.toml`; Dev deps: `requirements-dev.txt`.
CI: see `.github/workflows/ci.yml`.

