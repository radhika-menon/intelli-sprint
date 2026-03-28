from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.activity import ActivityCreate, ActivityResponse
from app.dependencies import get_db
from app.models.activity import Activity

router = APIRouter(prefix="/activities", tags=["activities"])

@router.post("/")
def create_activity(activity: ActivityCreate, db: Session = Depends(get_db)):
    new_activity = Activity(name=activity.name)
    db.add(new_activity)
    db.commit()
    db.refresh(new_activity)

    return {"id": new_activity.id, "name": new_activity.name}

@router.get("/", response_model=list[ActivityResponse])
def get_activities(db: Session = Depends(get_db)):
    return db.query(Activity).all()
