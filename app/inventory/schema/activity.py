from pydantic import BaseModel, Field
from datetime import date
from uuid import UUID
from typing import Optional

class ActivityBase(BaseModel):
    name: str = Field(..., title="Activity name")
    description: Optional[str] = Field(..., title="Activity description")

    class Config:
        from_attributes = True

class ActivityCreate(ActivityBase):
    start_date: Optional[date] = Field(..., title="Activity start date")
    end_date: Optional[date] = Field(..., title="Activity end date")
    status: Optional[str] = Field(..., title="Activity status")

class ActivityUpdate(ActivityBase):
    activityId: UUID = Field(..., title="Activity ID")
    start_date: date = Field(None, title="Activity start date")
    end_date: date = Field(None, title="Activity end date")
    status: str = Field(None, title="Activity status")