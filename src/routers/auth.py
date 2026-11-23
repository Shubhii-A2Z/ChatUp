from dtos import LoginResponseDTO, LoginRequestDTO
from fastapi import APIRouter

router=APIRouter(prefix="/api/auth", tags=["auth"])

@router.post(
    path="/login",
    response_model=LoginResponseDTO
)
def login(body: LoginRequestDTO)->LoginResponseDTO:
    return LoginResponseDTO(
        user_id=body.user_id.strip(),
        display_name=body.display_name.strip()
    )