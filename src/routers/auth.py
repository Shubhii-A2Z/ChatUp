from utils import PoolDependency
from services.users import UserService
from dtos import LoginResponseDTO, LoginRequestDTO
from fastapi import APIRouter

router=APIRouter(prefix="/api/auth", tags=["auth"])

@router.post(
    path="/login",
    response_model=LoginResponseDTO
)
def login(body: LoginRequestDTO, pool: PoolDependency)->LoginResponseDTO:
    user_service=UserService(pool)
    user=user_service.login_user(body.user_id, body.display_name)

    return LoginResponseDTO(
        user_id=user["user_id"],
        display_name=user["display_name"]
    )