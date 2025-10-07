## Developer Setup — GitHub + Docker

### Prerequisites
- Install Docker Desktop (with Compose v2)
- GitHub access

### Clone
```bash
git clone <repo-url>
cd <repo>
```

### Start Dev Container
```bash
docker compose -f docker/docker-compose.yml up -d
```

### Open a Shell in the Container
```bash
docker compose -f docker/docker-compose.yml exec dev bash
```

### Build the Base Image (optional)
```bash
docker build -t bridge-crew-dev -f docker/Dockerfile .
```

### CI Parity Check
```bash
docker compose -f docker/docker-compose.yml config
```

### Run Linters (inside container)
```bash
chmod +x scripts/lint.sh
./scripts/lint.sh
```

Linters included: markdownlint, yamllint, hadolint, actionlint.

See `docs/Operations.md` and `docs/DevelopmentSchedule.md` for workflows.

