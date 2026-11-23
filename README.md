## Database migrations (Alembic)

From the project root, with the virtualenv active and Postgres running (`docker compose up -d postgres`):

1. **Initialize Alembic migration** (once per project):

   ```bash
   uv run alembic init alembic
   ```

   Configure `alembic.ini` (`sqlalchemy.url`) and `alembic/env.py` before creating revisions.

2. **Create the first migration** (edit the generated file under `alembic/versions/` as needed):

   ```bash
   uv run alembic revision -m "initial migration"
   ```

3. **Apply migrations** to the database:

   ```bash
   uv run alembic upgrade head
   ```

4. **Create a new migration** (when you change models):

   ```bash
   uv run alembic revision --autogenerate -m "Descriptive message about changes"
   ```

5. **View migration history**:

   ```bash
   uv run alembic history
   ```

6. **Rollback the last migration**:

   ```bash
   uv run alembic downgrade -1
   ```