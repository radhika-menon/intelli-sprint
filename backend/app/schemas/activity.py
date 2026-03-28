from pydantic import BaseModel, ConfigDict

class ActivityCreate(BaseModel):
    name: str

class ActivityResponse(BaseModel):
    id: int
    name: str

    model_config = ConfigDict(from_attributes=True)