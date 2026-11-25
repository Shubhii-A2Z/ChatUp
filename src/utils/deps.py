from configs import create_pool, get_settings
from psycopg_pool import ConnectionPool
from functools import lru_cache
from typing import Annotated
from http import HTTPStatus
from fastapi import Header, HTTPException, Depends


@lru_cache
def get_db_pool()->ConnectionPool:
    """Returns a cached connection pool for database connections."""
    return create_pool()


def require_user_id(
    x_user_id: str | None=Header(None, alias="X-User-Id")
)->str:
    """Extract the required X-User-Id from request header and validate it."""

    if x_user_id is None:
        raise HTTPException(status_code=HTTPStatus.UNAUTHORIZED, detail="X-User-Id header required")

    user_id=x_user_id.strip()

    if user_id is None:
        raise HTTPException(status_code=HTTPStatus.UNAUTHORIZED, detail="X-User-Id header invalid")
    return user_id


# Dependency Injection for user_id: Used in routers to inject the user_id as a parameter which depends on require_user_id function
UserIdDependency=Annotated[str, Depends(require_user_id)]

# Dependency Injection for database connection pool: Used in routers to inject the database connection pool as a parameter which depends on get_db_pool function
PoolDependency=Annotated[ConnectionPool, Depends(get_db_pool)]