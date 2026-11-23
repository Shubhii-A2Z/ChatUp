from pydantic import BaseModel, Field


class LoginResponseDTO(BaseModel):
    user_id: str=Field(..., description="The user id")
    display_name: str=Field(..., description="The display name")