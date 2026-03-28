from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.sprint_activity import SprintActivityCreate, SprintActivityResponse
from app.dependencies import get_db
from app.models.sprint_week import SprintWeek
from app.models.activity import Activity
from app.models.sprint_activity import SprintActivity

router = APIRouter( prefix="/sprint-weeks/{sprint_week_id}/activities", tags=["activities"])

@router.post("/", response_model=list[SprintActivityResponse])
def add_activity_to_sprint(
    sprint_week_id: int,
    data: SprintActivityCreate,
    db: Session = Depends(get_db)
):
    # Check sprint exists
    sprint = db.query(SprintWeek).filter(SprintWeek.id == sprint_week_id).first()
    if not sprint:
        raise HTTPException(status_code=404, detail="Sprint week not found")

    # Check activity exists
    activity = db.query(Activity).filter(Activity.id == data.activity_id).first()
    if not activity:
        raise HTTPException(status_code=404, detail="Activity not found")

    created_links = []

    # Create one row per day
    for day in data.days:
        link = SprintActivity(
            sprint_week_id=sprint_week_id,
            activity_id=data.activity_id,
            assigned_day=day,
            status=data.status
        )
        db.add(link)
        created_links.append(link)

    db.commit()

    # refresh all objects
    for link in created_links:
        db.refresh(link)

    return created_links


@router.get("/", response_model=list[SprintActivityResponse])
def get_activities_for_sprint_week(
    sprint_week_id: int,
    db: Session = Depends(get_db)
):
    sprint = db.query(SprintWeek).filter(SprintWeek.id == sprint_week_id).first()
    if not sprint:
        raise HTTPException(status_code=404, detail="Sprint week not found")

    return db.query(SprintActivity).filter(
        SprintActivity.sprint_week_id == sprint_week_id
    ).all()