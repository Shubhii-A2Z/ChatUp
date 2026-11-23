from dtos import MemoryListResponseDTO
from fastapi import APIRouter, Query

router=APIRouter(prefix="/api/memory", tags=["memory"])

@router.get(
    path="/",
    response_model=MemoryListResponseDTO
)
def login(user_id: str=Query(..., description="The ID of user"))->MemoryListResponseDTO:
    return MemoryListResponseDTO(
        semantic=[],
        episodic=[],
        profile=[],
        procedural=[]
    )