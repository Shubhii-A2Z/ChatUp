from pydantic import BaseModel, Field

class ChatRequestDTO(BaseModel):
    message: str=Field(..., description="The message to send")