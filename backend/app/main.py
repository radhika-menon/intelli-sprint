from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.models.activity import Activity
from app.models.sprint_week import SprintWeek
from app.models.sprint_activity import SprintActivity
from app.schemas.activity import ActivityCreate, ActivityResponse
from app.schemas.sprint_week import SprintWeekCreate, SprintWeekResponse
from app.schemas.sprint_activity import SprintActivityCreate, SprintActivityResponse

# Note: FastAPI + Pydantic will automatically convert SQLAlchemy objects to
# JSON, handle date to string conversion and ensure the response model is
# correctly serialised. The response_model parameter in the route decorator
# specifies the expected output format, and FastAPI will take care of the
# conversion. So ORM objects can be returned directly from the route handlers
# without needing to manually convert them to dictionaries or JSON.


app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/activities")
def create_activity(activity: ActivityCreate, db: Session = Depends(get_db)):
    new_activity = Activity(name=activity.name)
    db.add(new_activity)
    db.commit()
    db.refresh(new_activity)

    return {"id": new_activity.id, "name": new_activity.name}

@app.get("/activities", response_model=list[ActivityResponse])
def get_activities(db: Session = Depends(get_db)):
    return db.query(Activity).all()

@app.post("/sprint-weeks")  
def create_sprint_week(data: SprintWeekCreate, db: Session = Depends(get_db)):
    new_sprint_week = SprintWeek(
        week_start_date=data.week_start_date,
        semester_week=data.semester_week
    )
    db.add(new_sprint_week)
    db.commit()
    db.refresh(new_sprint_week)

    return {
        "id": new_sprint_week.id,
        "week_start_date": new_sprint_week.week_start_date.isoformat(),
        "semester_week": new_sprint_week.semester_week
    }


@app.get("/sprint-weeks", response_model=list[SprintWeekResponse])
def get_sprint_weeks(db: Session = Depends(get_db)):
    return db.query(SprintWeek).all()


@app.post("/sprint-weeks/{sprint_week_id}/activities", response_model=list[SprintActivityResponse])
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


@app.get("/sprint-weeks/{sprint_week_id}/activities", response_model=list[SprintActivityResponse])
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