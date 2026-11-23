from typing import Literal
from pydantic import BaseModel, Field


class ThreadCreate(BaseModel):
    title: str=Field("New Thread", description="The title of the thread")

class ThreadUpdate(BaseModel):
    title: str=Field(..., description="The title of the thread")

class ThreadResponse(BaseModel):
    thread_id: str=Field(..., description="The id of the thread")
    title: str=Field(..., description="The title of the thread")
    created_at: str | None=Field(None, description="The timestamp of creation of the thread")
    updated_at: str | None=Field(None, description="The timestamp of update of the thread")

class MessageItem(BaseModel):
    role: Literal["user", "assistant"]=Field(..., description="The role of message item")
    content: str=Field(..., description="The content of message")

class MessageResponse(BaseModel):
    thread_id: str=Field(..., description="The id of the thread")
    messages: list[MessageItem]