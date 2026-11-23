from utils import UserIdDependency
from dtos import MemoryListResponseDTO
from fastapi import APIRouter, Query

router=APIRouter(prefix="/api/memory", tags=["memory"])

@router.get(
    path="/",
    response_model=MemoryListResponseDTO
)
def list_memory(_user_id: UserIdDependency)->MemoryListResponseDTO:
    return MemoryListResponseDTO(
        semantic=[],
        episodic=[],
        profile=[],
        procedural=[]
    )