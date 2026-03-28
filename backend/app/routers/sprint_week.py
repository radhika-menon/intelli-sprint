from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.sprint_week import SprintWeekCreate, SprintWeekResponse
from app.dependencies import get_db
from app.models.sprint_week import SprintWeek

router = APIRouter(prefix="/sprint-weeks", tags=["sprint_weeks"])

# Note: FastAPI + Pydantic will automatically convert SQLAlchemy objects to
# JSON, handle date to string conversion and ensure the response model is
# correctly serialised. The response_model parameter in the route decorator
# specifies the expected output format, and FastAPI will take care of the
# conversion. So ORM objects can be returned directly from the route handlers
# without needing to manually convert them to dictionaries or JSON.

@router.post("/")  
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


@router.get("/", response_model=list[SprintWeekResponse])
def get_sprint_weeks(db: Session = Depends(get_db)):
    return db.query(SprintWeek).all()
