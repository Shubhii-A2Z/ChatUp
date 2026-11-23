from typing import Annotated
from http import HTTPStatus
from fastapi import Header, HTTPException, Depends

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