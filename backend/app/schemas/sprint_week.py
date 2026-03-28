from datetime import date
from pydantic import BaseModel, ConfigDict

class SprintWeekCreate(BaseModel):
    week_start_date: date
    semester_week: int

class SprintWeekResponse(BaseModel):
    id: int
    week_start_date: date
    semester_week: int

    # This tells Pydantic to read data from the SQLAlchemy model attributes
    # when creating the response model, allowing us to return ORM objects
    # directly from our route handlers without needing to convert them to
    # dictionaries or JSON.
    model_config = ConfigDict(from_attributes=True)