from schemas import ThreadResponse
from fastapi import APIRouter, Query

router=APIRouter(prefix="/api/threads", tags=["threads"])

@router.get(
    path="/",
    response_model=ThreadResponse
)
def list_threads(user_id: str=Query(..., description="The ID of user"))->list[ThreadResponse]:
    return []