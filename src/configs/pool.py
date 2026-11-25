from configs import get_settings
from psycopg_pool import ConnectionPool

def create_pool()->ConnectionPool:
    settings=get_settings()

    return ConnectionPool(
        conninfo=settings.database_url,
        kwargs={
            "row_factory": settings.postgres_row_factory
        },
        min_size=settings.postgres_pool_min_size,
        max_size=settings.postgres_pool_max_size,
        open=settings.postgres_pool_open
    )