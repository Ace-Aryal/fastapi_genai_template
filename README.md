# FastAPI GenAI Template

A minimal FastAPI template with AI infrastructure, Celery worker support, PostgreSQL/Redis helpers, and Docker-ready startup.

## Folder Structure

- `main.py` - application entrypoint importing the FastAPI app from `infrastructures.server.fastapi`
- `Dockerfile` - container image definition for running the app
- `docker-compose.yml` - production-style container orchestration
- `docker-compose.dev.yml` - development container orchestration with live reload
- `pyproject.toml` - project metadata and dependencies

- `core/`
  - `config.py` - app configuration helpers
  - `constants.py` - shared application constants
  - `exceptions.py` - custom exception definitions
  - `logging.py` - logging setup
  - `settings.py` - environment-based settings

- `infrastructures/`
  - `ai/` - AI integration layers
    - `langchain_agents.py` - LangChain agent helpers
    - `langchain_llms.py` - LangChain LLM wrappers
    - `system_prompts/` - system prompt templates for AI workflows
  - `bg_workers/`
    - `celery.py` - Celery worker configuration
  - `cloud/`
    - `elastic_beanstalk.py` - AWS Elastic Beanstalk helpers
  - `database/`
    - `base.py` - SQLAlchemy base model setup
    - `connection.py` - DB connection utilities
    - `session.py` - DB session management
  - `redis/`
    - `app.py` - Redis client setup
  - `server/`
    - `fastapi.py` - FastAPI application instance
    - `root_router.py` - API routing setup
  - `storage/` - storage helpers and abstractions

- `modules/` - feature-specific domain modules
  - `auth/` - authentication feature
    - `jobs/` - background jobs
    - `models/` - data models
    - `repositories/` - data access layer
    - `routes/` - API routes
    - `schemas/` - request/response schemas
    - `services/` - business logic
    - `utils/` - helper utilities

- `utils/`
  - `date_utils.py` - common date utilities

## Getting Started

### Prerequisites

- Python 3.12+
- `uv` installed or available via `pip install uv`
- Docker and Docker Compose if running in containers

### Local development (UV)

1. Clone the repo:

   ```bash
   git clone https://github.com/ace-aryal/fastapi_genai_template.git
   cd fastapi_genai_template
   ```

2. Install dependencies:

   ```bash
   python -m pip install --upgrade pip
   python -m pip install .
   ```

3. Start the app:

   ```bash
   uv run uvicorn main:app --reload
   ```

4. Open your browser:
   - Swagger UI: `http://127.0.0.1:8000/docs`
   - ReDoc: `http://127.0.0.1:8000/redoc`

### Running with Docker

#### Build and run using Docker Compose

```bash
docker compose up --build
```

This starts the `api` service on port `8000`.

#### Development with live reload

```bash
docker compose -f docker-compose.dev.yml up --build
```

The development compose file mounts the repository and runs `uv run uvicorn main:app --host 0.0.0.0 --port 8000 --reload`.

### Direct Docker build

```bash
docker build -t fastapi-genai-template .
docker run -p 8000:8000 fastapi-genai-template
```

## Documentation

FastAPI generates interactive API docs automatically at runtime:

- Swagger UI: `/docs`
- ReDoc: `/redoc`

> Example: `http://127.0.0.1:8000/docs`

## Notes

- `main.py` loads the FastAPI app from `infrastructures.server.fastapi`.
- Use `.env` or environment variables for runtime configuration if supported by `core.settings`.
- Adjust Docker compose and app settings to match your database or message broker setup.
