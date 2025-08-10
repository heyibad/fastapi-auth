from typing import Optional
from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    """Base user schema."""

    email: EmailStr
    username: str
    first_name: Optional[str] = None
    last_name: Optional[str] = None


class UserCreateRequest(UserBase):
    """User creation request schema."""

    password: str


class UserUpdateRequest(BaseModel):
    """User update request schema."""

    email: Optional[EmailStr] = None
    username: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None


class UserResponse(UserBase):
    """User response schema."""

    id: int
    is_active: bool

    class Config:
        from_attributes = True


class Token(BaseModel):
    """Token response schema."""

    access_token: str
    token_type: str


class TokenData(BaseModel):
    """Token data schema."""

    username: Optional[str] = None


class LoginRequest(BaseModel):
    """Login request schema."""

    username: str
    password: str
