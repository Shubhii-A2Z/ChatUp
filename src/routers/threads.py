from datetime import datetime
from services import ThreadService
from utils import UserIdDependency, PoolDependency
from schemas import ThreadResponse, ThreadCreate
from fastapi import APIRouter, Query

router=APIRouter(prefix="/api/threads", tags=["threads"])

@router.get(
    path="/",
    response_model=list[ThreadResponse]
)
def list_threads(pool: PoolDependency, user_id: UserIdDependency)->list[ThreadResponse]:
    thread_service=ThreadService(pool)
    threads=thread_service.get_threads_for_user(user_id=user_id)
    return [
        ThreadResponse(
            thread_id=row["thread_id"],
            title=row["title"],
            created_at=_timestamp(row.get("created_at")),
            updated_at=_timestamp(row.get("updated_at"))
        )
        for row in threads
    ]


@router.post(
    path="/",
    response_model=ThreadResponse
)
def create_thread(body: ThreadCreate, pool: PoolDependency, user_id: UserIdDependency)->ThreadResponse:
    thread_service=ThreadService(pool)
    new_thread=thread_service.create_new_thread(user_id=user_id, title=body.title)

    return ThreadResponse(
        thread_id=new_thread["thread_id"],
        title=new_thread["title"],
        created_at=_timestamp(new_thread.get("created_at")),
        updated_at=_timestamp(new_thread.get("updated_at"))
    )


def _timestamp(value: object)->str | None:
    if value is None:
        return None
    if isinstance(value, datetime):
        return value.isoformat()
    return str(value)