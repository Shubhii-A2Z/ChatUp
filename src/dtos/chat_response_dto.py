from pydantic import BaseModel, Field

class ChatResponseDTO(BaseModel):
    reply: str=Field(..., description="The reply to message")
    thread_id: str=Field(..., description="The thread id")