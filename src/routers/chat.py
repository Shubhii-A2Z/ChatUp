from utils import UserIdDependency
from schemas import MessageResponse
from fastapi import APIRouter, Query

router=APIRouter(prefix="/api/threads", tags=["chat"])

@router.get(
    path="/{threadId}/messages",
    response_model=MessageResponse
)
def list_thread_messages(thread_id: str, _user_id: UserIdDependency)->MessageResponse:
    return MessageResponse(
        thread_id=thread_id,
        messages=[]
    )