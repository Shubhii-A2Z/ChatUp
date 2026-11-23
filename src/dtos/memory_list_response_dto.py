from pydantic import BaseModel, Field

class MemoryListResponseDTO(BaseModel):
    semantic: list[str]=Field(..., description="The semantic memory")
    episodic: list[str]=Field(..., description="The episodic memory")
    profile: list[str]=Field(..., description="The profile memory")
    procedural: list[str]=Field(..., description="The procedural memory")