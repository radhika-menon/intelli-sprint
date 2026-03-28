from typing import List
from app.models.enums import ActivityStatus, WeekDay
from pydantic import BaseModel, ConfigDict


class SprintActivityCreate(BaseModel):
    activity_id: int
    days: List[WeekDay]
    status: ActivityStatus = ActivityStatus.planned

class SprintActivityResponse(BaseModel):
    id: int
    activity_id: int
    sprint_week_id: int
    assigned_day: WeekDay
    status: ActivityStatus

    model_config = ConfigDict(from_attributes=True)