from typing import Optional
from sqlmodel import SQLModel, Field
from .base import BaseModel


class User(BaseModel, table=True):
    """User model for authentication."""

    __tablename__ = "users"

    email: str = Field(index=True, unique=True)
    username: str = Field(index=True, unique=True)
    hashed_password: str
    is_active: bool = Field(default=True)
    is_superuser: bool = Field(default=False)
    first_name: Optional[str] = None
    last_name: Optional[str] = None


class UserCreate(SQLModel):
    """Schema for creating a user."""

    email: str
    username: str
    password: str
    first_name: Optional[str] = None
    last_name: Optional[str] = None


class UserUpdate(SQLModel):
    """Schema for updating a user."""

    email: Optional[str] = None
    username: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    is_active: Optional[bool] = None


class UserRead(SQLModel):
    """Schema for reading a user (public data)."""

    id: int
    email: str
    username: str
    is_active: bool
    first_name: Optional[str] = None
    last_name: Optional[str] = None
