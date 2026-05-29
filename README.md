# MaternAI

A safe space for women to record and share their birth stories.

Childbirth is a moment that is both **longed for and feared**. Sharing real experiences—with honesty and care—strengthens each woman's **confidence** and **power to make decisions**. This project exists to support that conversation: to listen, learn, and choose with more information and less isolation.

---

## About the project

**MaternAI** is an API built with **FastAPI**, **SQLModel**, and **PostgreSQL**, designed to:

- Create and retrieve birth stories (location, care type, delivery mode, rating, and more)
- Provide a clear technical foundation for a future web or mobile app
- Keep a clean separation of layers: routes → services → database

---

## Stack

| Technology | Purpose |
|------------|---------|
| [FastAPI](https://fastapi.tiangolo.com/) | HTTP API |
| [SQLModel](https://sqlmodel.tiangolo.com/) | Models and ORM |
| [PostgreSQL](https://www.postgresql.org/) | Database |
| [asyncpg](https://github.com/MagicStack/asyncpg) | Async Postgres driver |
| [Pydantic Settings](https://docs.pydantic.dev/latest/concepts/pydantic_settings/) | Configuration via `.env` |

---

## Prerequisites

- Python 3.11+
- Docker (recommended for Postgres) or a local Postgres installation
- `git`

---

## Configuring `.env`

The application reads environment variables from a **`.env`** file at the project root (`app/database/config.py`).

### 1. Create the `.env` file

In the project folder (`maternai-t/`):

```bash
cp .env.example .env
# or create it manually:
touch .env
```

### 2. Set the variables

```env
# PostgreSQL user and password
POSTGRES_USER=root
POSTGRES_PASSWORD=your_password_here
POSTGRES_DB=birth_db
POSTGRES_SERVER=localhost
POSTGRES_PORT=5432

# Connection URL (must use the async driver)
DB_SOURCE=postgresql+asyncpg://root:your_password_here@localhost:5432/birth_db
```

| Variable | Description |
|----------|-------------|
| `POSTGRES_USER` | Database user |
| `POSTGRES_PASSWORD` | Database password |
| `POSTGRES_DB` | Database name |
| `POSTGRES_SERVER` | Host (usually `localhost`) |
| `POSTGRES_PORT` | Port (default `5432`) |
| `DB_SOURCE` | Full URL for SQLAlchemy async |

### 3. Important rules

1. **`DB_SOURCE` must use `postgresql+asyncpg://`** — do not use `postgresql://` alone, because the API is async.
2. **User and password** in `DB_SOURCE` must **match** `POSTGRES_USER` and `POSTGRES_PASSWORD`.
3. **Do not commit** `.env` with real passwords. It is listed in `.gitignore`; use local dev credentials only.
4. After changing `.env`, **restart** the server (`fastapi dev`).

### Correct URL example

```text
postgresql+asyncpg://USER:PASSWORD@localhost:5432/birth_db
```

---

## Start PostgreSQL (Docker)

```bash
docker run --name postgres_birth \
  -e POSTGRES_USER=root \
  -e POSTGRES_PASSWORD=your_password_here \
  -e POSTGRES_DB=birth_db \
  -p 5432:5432 \
  -d postgres
```

If the container already exists:

```bash
docker start postgres_birth
```

---

## Install and run

```bash
# 1. Go to the project folder
cd maternai-t

# 2. Create and activate the virtual environment
python -m venv venv
source venv/bin/activate    # macOS/Linux
# venv\Scripts\activate   # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Verify .env and test import
python -c "from app.main import app; print('OK')"

# 5. Start the API
fastapi dev app/main.py
```

The API will be available at:

- **Swagger UI:** http://127.0.0.1:8000/docs
- **Scalar docs:** http://127.0.0.1:8000/scalar

On first startup, tables are created automatically (`create_db_tables`).

---

## Main endpoints

| Method | Route | Description |
|--------|-------|-------------|
| `GET` | `/{story_id}` | Get a story by ID |
| `POST` | `/story` | Create a new story |
| `PATCH` | `/{story_id}` | Update a story (sent fields only) |
| `DELETE` | `/{story_id}` | Delete a story |

---

## Project structure

```text
app/
├── main.py              # FastAPI entrypoint + lifespan
├── api/
│   ├── router.py        # HTTP routes
│   ├── dependencies.py  # Dependency injection
│   └── schemas/         # Pydantic models (API)
├── services/
│   └── story.py         # Business logic
└── database/
    ├── config.py        # .env loading
    ├── session.py       # Async engine and session
    └── models.py        # SQLModel tables
```

---

## Troubleshooting

| Error | Fix |
|-------|-----|
| `No module named 'psycopg2'` | Use `postgresql+asyncpg://` in `DB_SOURCE` and run `pip install asyncpg` |
| `No module named 'greenlet'` | Run `pip install greenlet` |
| `password authentication failed` | Password in `.env` does not match Postgres — align both |
| `command not found: fastapi` | Run `source venv/bin/activate` |
| `connection refused` | Postgres is not running — start the Docker container |

---

## License and contributing

This repository is under active development. Suggestions and improvements are welcome.

**MaternAI** — because every story matters, and no woman should go through this alone.
