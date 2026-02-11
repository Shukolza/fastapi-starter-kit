# FastAPI Starter Kit

![Python version](https://img.shields.io/badge/Python%20version-3.7+-3776AB?logo=python&logoColor=3776AB)

**FastAPI Starter Kit** is a minimalist, almost-production-ready template designed to skip the boring part of project setup. No more copy-pasting `database.py` and struggling with async Alembic setup.

With this template you can instantly start writing your business logic without wasting time on creating another \_\_init\_\_.py!

## Tech Stack & Why?

- **SQLAlchemy 2.0 (Async)**: Using the latest features such as `MappedAsDataclass` for clean, type-safe models.
- **Alembic**: Pre-configured for asynchronous migrations.
- **SQLite (aiosqlite)**: Default DB for zero-config startup, but easily swappable to PostgreSQL.

## Who is this for?

- **MVP Builders**: When you need to ship a backend with auth _yesterday_.
- **Developers**: Tired of creating 20+ files and `__init__.py` markers manually every single time.
- **Students**: Who want to see a clean, service-oriented architecture instead of a "main.py" mess.

## Quick Start

### 1. Clone the repo

```bash
git clone https://github.com/shukolza/fastapi-starter-kit
cd fastapi-starter-kit
```

### 2. Set up environment

```bash
python -m venv venv
source venv/bin/activate  # Or `venv\Scripts\activate` on Windows
pip install -r requirements.txt
```

### 3. Configure `.env`

Rename `.env.example` to `.env` file in the root directory and configure the values:

```env
JWT_SECRET_KEY="CHANGE ME"
JWT_EXPIRE_MIN="0" # 0 means 'does not expire', change for production!
DB_URL="sqlite+aiosqlite:///app.db"
```

### 4. Run Migrations

```bash
alembic upgrade head
```

### 5. Start the engine

```bash
uvicorn src.main:app --reload
```

Check that everything is ok and test endpoints: `http://127.0.0.1:8000/docs`

## Implemented Features

The template comes with a pre-configured core logic to handle the most common backend tasks:

### Authentication & Authorization

- **Registration**: `POST /auth/register` - creates a new user, hashes the password using Argon2, and stores it in the database.
- **Login**: `POST /auth/login` - validates credentials and returns a JWT access token. Fully compatible with OpenAPI (Swagger) OAuth2 flow.
- **Current User Dependency**: A pre-made `get_current_user` dependency in `src/api/deps.py` to protect your routes and retrieve the authenticated user object.

### Database Architecture

- **Async Engine**: Configured via `sqlalchemy.ext.asyncio`.
- **Base Model**: Uses `MappedAsDataclass` and `DeclarativeBase` for full type-hinting support and automatic `__init__` generation.
- **User Model**: Includes `id`, `username`, `email`, and `password_hash` fields.
- **Migrations**: Async-ready Alembic environment with automatic model discovery in `env.py`.

### Service Layer

- **UserService**: Encapsulates business logic for user management, including password verification and database interaction, separating it from the API layer.
- **Exceptions**: A custom exception hierarchy in `src/core/exceptions.py` for handling auth and registration errors, which are then mapped to FastAPI HTTP exceptions.

### Configuration

- **Environment Management**: Powered by `pydantic-settings`. Validates `.env` variables on startup.
- **JWT Logic**: Customizable token expiration logic. Setting `JWT_EXPIRE_MIN` to `0` removes the `exp` claim, making tokens valid indefinitely for development purposes.

## Contributing

This is a community-driven template. Feel free to open an issue or submit a pull request if you have ideas on how to make this boilerplate even more "no-boilerplate".

License: MIT (do whatever you want except for suing me)
