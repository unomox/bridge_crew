FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y \
    git curl ca-certificates jq unzip bash \
    yamllint nodejs npm \
    python3 python3-pip \
  && rm -rf /var/lib/apt/lists/*

# Markdown linter
RUN npm install -g markdownlint-cli@0.39.0

# hadolint (Dockerfile linter)
ENV HADOLINT_VERSION=2.12.0
RUN curl -sSL -o /usr/local/bin/hadolint \
    https://github.com/hadolint/hadolint/releases/download/v${HADOLINT_VERSION}/hadolint-Linux-x86_64 \
  && chmod +x /usr/local/bin/hadolint

# actionlint (GitHub Actions linter)
ENV ACTIONLINT_VERSION=1.6.27
RUN curl -sSL -o /tmp/actionlint.tar.gz \
    https://github.com/rhysd/actionlint/releases/download/v${ACTIONLINT_VERSION}/actionlint_${ACTIONLINT_VERSION}_linux_amd64.tar.gz \
  && tar -C /usr/local/bin -xzf /tmp/actionlint.tar.gz actionlint \
  && rm /tmp/actionlint.tar.gz

WORKDIR /workspace

# Add any project-specific setup below; keep base image minimal and reproducible.

# Python developer tools (versions pinned for reproducibility)
RUN python3 -m pip install --no-cache-dir \
    ruff==0.6.4 \
    black==24.8.0 \
    pytest==8.2.0 \
    pytest-cov==5.0.0 \
    bandit==1.7.9 \
    pip-audit==2.7.3


