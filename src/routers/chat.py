from schemas import MessageResponse
from fastapi import APIRouter

router=APIRouter(prefix="/api/threads", tags=["chat"])

@router.get(
    path="/{threadId}/messages",
    response_model=MessageResponse
)
def login(thread_id: str, user_id: str)->MessageResponse:
    return MessageResponse(
        thread_id=thread_id,
        messages=[]
    )