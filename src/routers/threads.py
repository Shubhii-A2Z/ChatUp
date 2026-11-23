from utils import UserIdDependency
from schemas import ThreadResponse
from fastapi import APIRouter, Query

router=APIRouter(prefix="/api/threads", tags=["threads"])

@router.get(
    path="/",
    response_model=ThreadResponse
)
def list_threads(_user_id: UserIdDependency)->list[ThreadResponse]:
    return []