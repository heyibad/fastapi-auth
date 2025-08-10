from datetime import datetime
from typing import Optional
from sqlmodel import SQLModel, Field


class TimestampedModel(SQLModel):
    """Base model with timestamp fields."""

    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: Optional[datetime] = Field(default=None)


class BaseModel(TimestampedModel):
    """Base model with ID and timestamp fields."""

    id: Optional[int] = Field(default=None, primary_key=True)
