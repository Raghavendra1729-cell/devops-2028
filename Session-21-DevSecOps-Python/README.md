# Session 21 — DevSecOps Python Project: Manual and Docker Compose Deployment

**Name:** Raghavendra  
**Enrollment number:** 24BCS10250

## Assignment

Deploy the **DevSecOps-Python** project (TaskBoard) in two ways and document both:

1. **Manually, without Docker.** Run PostgreSQL, the FastAPI backend and the React frontend by hand.
2. **With Docker.** Write Dockerfiles for the frontend and backend, then deploy all three services with `docker-compose`.

The code is in [`DevSecOps-Python/`](DevSecOps-Python/), taken from the course repository's `session21-python` folder. Only the application parts were copied (`backend/`, `frontend/`, `docker-compose.yml`). Terraform, Helm and monitoring files are not needed for this homework.

## Application overview

| Layer | Technology | Port |
|---|---|---|
| Frontend | React (Vite build), served by Nginx in Docker | `5173` (Vite dev server, manual) / `3000` (Docker) |
| Backend | FastAPI, SQLAlchemy, Alembic, Prometheus metrics | `8000` |
| Database | PostgreSQL 16 | `5432` |

Backend endpoints: `GET /health`, `GET /ready`, `GET /metrics`, `GET /docs`, and the task API (`GET/POST /api/tasks`, `GET /api/tasks/stats`, `GET/PUT/DELETE /api/tasks/{id}`).

```mermaid
flowchart LR
    B[Browser] --> F[Frontend :3000 / :5173]
    F -->|/api| A[FastAPI backend :8000]
    A --> P[(PostgreSQL :5432)]
    M[/metrics/] -.-> A
```

> **A note on the screenshots.** The command output is real. I ran each command and captured its output. The terminal and browser frames were drawn around it with a script so every image shows the command or URL it came from.

---

## Part 1 — Manual deployment (no Docker)

Prerequisites: PostgreSQL 16, Python 3.13 and Node.js 20 or newer. On macOS, PostgreSQL comes from `brew install postgresql@16`.

### Step 1 — PostgreSQL

Start PostgreSQL, then create the `taskboard` role and database that the application expects:

```bash
brew services start postgresql@16
pg_isready
createuser taskboard
psql postgres -c "ALTER USER taskboard WITH PASSWORD 'taskboard';"
createdb -O taskboard taskboard
```

![PostgreSQL setup](images/manual-1-postgres-setup.png)

### Step 2 — Backend setup and database migration

```bash
cd DevSecOps-Python/backend
python3.13 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env          # DATABASE_URL points at localhost:5432
alembic upgrade head          # creates the tasks table
```

Alembic ran the `0001_create_tasks` migration, and `\dt` shows the `tasks` and `alembic_version` tables.

![Backend setup and Alembic migration](images/manual-2-backend-setup.png)

### Step 3 — Start the backend

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

![Uvicorn running](images/manual-3-backend-uvicorn.png)

### Step 4 — Start the frontend

```bash
cd DevSecOps-Python/frontend
npm install
npm run dev -- --host 0.0.0.0     # http://localhost:5173
```

The Vite dev server proxies `/api` to the backend on port 8000.

![Vite dev server](images/manual-4-frontend-vite.png)

### Manual deployment — results

**UI — http://localhost:5173**

![UI running manually](images/manual-ui-localhost-5173.png)

**Swagger UI — http://localhost:8000/docs**

![Swagger UI](images/manual-backend-docs.png)

**Health check — http://localhost:8000/health**

![Health](images/manual-backend-health.png)

**Metrics — http://localhost:8000/metrics**

![Metrics](images/manual-backend-metrics.png)

### Stop the manual deployment

```bash
# Ctrl+C in the uvicorn and vite terminals
brew services stop postgresql@16
```

---

## Part 2 — Docker deployment with docker-compose

### Dockerfiles

**`backend/Dockerfile`** — Python 3.12 slim. It installs the dependencies, copies the app and the Alembic files, and runs as non-root user `10001`. On start it applies the migrations and then launches Uvicorn.

```dockerfile
FROM python:3.12-slim
WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt && useradd --create-home --uid 10001 appuser
COPY alembic.ini ./
COPY alembic ./alembic
COPY app ./app
USER 10001
EXPOSE 8000
CMD ["sh", "-c", "alembic upgrade head && uvicorn app.main:app --host 0.0.0.0 --port 8000"]
```

**`frontend/Dockerfile`** — multi-stage build. Node builds the React app. The static files are then served by the unprivileged Nginx image, which runs as a non-root user on port 8080.

```dockerfile
# Stage 1: build the React app with Node
FROM node:22-alpine AS build
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build

# Stage 2: serve the static build with Nginx (unprivileged image, runs as non-root on 8080)
FROM nginxinc/nginx-unprivileged:1.27-alpine
COPY --from=build /app/dist /usr/share/nginx/html
COPY nginx.conf /etc/nginx/conf.d/default.conf
EXPOSE 8080
```

`nginx.conf` serves the React app and proxies `/api/` and `/health` to the `backend` service.

### docker-compose.yml

```yaml
services:
  postgres:
    image: postgres:16-alpine
    environment:
      POSTGRES_DB: taskboard
      POSTGRES_USER: taskboard
      POSTGRES_PASSWORD: taskboard
    ports: ["5432:5432"]
    volumes: [postgres-data:/var/lib/postgresql/data]
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U taskboard -d taskboard"]
      interval: 5s
      timeout: 3s
      retries: 10

  backend:
    build: ./backend
    environment:
      DATABASE_URL: postgresql+psycopg://taskboard:taskboard@postgres:5432/taskboard
    depends_on:
      postgres:
        condition: service_healthy
    restart: unless-stopped
    ports: ["8000:8000"]

  frontend:
    build: ./frontend
    depends_on: [backend]
    ports: ["3000:8080"]

volumes:
  postgres-data:
```

### Deploy

```bash
cd DevSecOps-Python
docker-compose up -d --build
docker-compose ps
```

**`docker-compose up -d --build`**

![docker-compose up -d --build](images/docker-compose-up.png)

**`docker-compose ps`** — all three services are up and Postgres reports `healthy`.

![docker-compose ps](images/docker-compose-ps.png)

### Docker deployment — results

**UI — http://localhost:3000**

![UI on localhost:3000](images/docker-ui-localhost-3000.png)

**Swagger UI — http://localhost:8000/docs**

![Swagger UI](images/docker-backend-docs.png)

**Health check — http://localhost:8000/health**

![Health](images/docker-backend-health.png)

**Metrics — http://localhost:8000/metrics**

![Metrics](images/docker-backend-metrics.png)

### Clean up

```bash
docker-compose down        # add -v to also delete the database volume
```

---

## Problems I hit and how I fixed them

| Problem | Cause | Fix |
|---|---|---|
| Backend container exited right after `docker-compose up` and `/health` returned nothing | `depends_on` only waits for the Postgres container to start, not for the database to accept connections. `alembic upgrade head` failed with `Connection refused`. | Added a Postgres `healthcheck` and `depends_on: condition: service_healthy`, plus `restart: unless-stopped` on the backend. |
| Frontend container ran as root | The plain `nginx` image starts as root and listens on port 80. | Switched to `nginxinc/nginx-unprivileged` (runs as user `nginx`, port 8080). Compose maps `3000:8080` and `nginx.conf` listens on 8080. |
| `npm run dev` could not reach the API in the manual run | `vite.config.js` proxied `/api` to port `8080`, but the backend listens on `8000`. | Changed the proxy target to `http://localhost:8000`. |
| UI showed someone else's name | The sample frontend hard-codes the original author's name. | Replaced it with my name in `frontend/src/main.jsx`. |

Both Docker images run as non-root (`appuser` / `nginx`), checked with `docker exec <container> id`.
