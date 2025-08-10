# FastAPI Authentication Service

A professional FastAPI backend application with SQLModel and PostgreSQL for user authentication and management.

## Features

-   User registration and authentication
-   JWT token-based security
-   SQLModel ORM with PostgreSQL
-   Database migrations with Alembic
-   Docker containerization
-   FastAPI automatic API documentation

## Getting Started

### Using Docker Compose

```bash
docker compose up
```

### Local Development

1. Install dependencies:

    ```bash
    uv sync
    ```

2. Run the application:
    ```bash
    uv run uvicorn app.main:app --reload
    ```

## API Documentation

Once the application is running, visit:

-   Swagger UI: http://localhost:8000/docs
-   ReDoc: http://localhost:8000/redoc
