from app.db.base import Base
from app.db.session import engine
from app.models import activity, sprint_week, sprint_activity
from app.models.activity import Activity
from app.models.sprint_week import SprintWeek
from app.models.sprint_activity import SprintActivity
from app.models.enums import WeekDay, ActivityStatus
from datetime import date

# Test to ensure that the database tables are created correctly based on the SQLAlchemy models
# defined in Base.
def test_tables_created():
    tables = Base.metadata.tables.keys()

    assert "activities" in tables
    assert "sprint_weeks" in tables
    assert "sprint_activities" in tables

def test_create_activity(db):
    # Create a new activity
    new_activity = Activity(name="Write README for backend")
    db.add(new_activity)
    db.commit()
    db.refresh(new_activity)

    result = db.query(Activity).filter_by(name="Write README for backend").first()

    # Verify the activity was created
    assert result is not None
    assert result.name == "Write README for backend"

def test_create_sprint_week(db):
    # Create a new sprint week
    new_sprint_week = SprintWeek(
        week_start_date=date(2026, 3, 20),
        semester_week=2
    )
    db.add(new_sprint_week)
    db.commit()
    db.refresh(new_sprint_week)

    result = db.query(SprintWeek).filter_by(semester_week=2).first()

    # Verify the sprint week was created
    assert result is not None
    assert result.week_start_date == date(2026, 3, 20)

def test_link_activity_to_sprint_week(db):
    # Create a new activity
    new_activity = Activity(name="Fill high school EOI form")
    db.add(new_activity)
    db.commit()
    db.refresh(new_activity)

    # Create a new sprint week
    new_sprint_week = SprintWeek(
        week_start_date=date(2026, 3, 23),
        semester_week=3
    )
    db.add(new_sprint_week)
    db.commit()
    db.refresh(new_sprint_week)

    # Link the activity to the sprint week with assigned day and status
    sprint_activity = SprintActivity(
        sprint_week_id=new_sprint_week.id,
        activity_id=new_activity.id,
        assigned_day=WeekDay.Mon,
        status=ActivityStatus.in_progress
    )
    db.add(sprint_activity)
    db.commit()
    db.refresh(sprint_activity)

    result = db.query(SprintActivity).first()

    # Verify the link was created correctly
    assert result is not None
    assert result.sprint_week_id == new_sprint_week.id
    assert result.activity_id == new_activity.id

def test_activity_multiple_days(db):
    # Create a new activity
    new_activity = Activity(name="Prepare lecture slides for MR 108")
    db.add(new_activity)
    db.commit()
    db.refresh(new_activity)

    # Create a new sprint week
    new_sprint_week = SprintWeek(
        week_start_date=date(2026, 3, 23),
        semester_week=3
    )
    db.add(new_sprint_week)
    db.commit()
    db.refresh(new_sprint_week)

    # Link the same activity to multiple days in the sprint week
    for day in [WeekDay.Mon, WeekDay.Tue, WeekDay.Wed]:
        sprint_activity = SprintActivity(
            sprint_week_id=new_sprint_week.id,
            activity_id=new_activity.id,
            assigned_day=day,
            status=ActivityStatus.planned
        )
        db.add(sprint_activity)
    
    db.commit()

    results = db.query(SprintActivity).filter_by(activity_id=new_activity.id).all()

    # Verify that there are multiple entries for the same activity with different assigned days
    assert len(results) == 3

def test_name_not_null(db):
    # Attempt to create an activity without a name (should fail due to nullable=False)
    new_activity = Activity(name=None)
    db.add(new_activity)
    try:
        db.commit()
        assert False, "Expected an exception due to null name"
    except Exception as e:
        db.rollback()  # Rollback the failed transaction
        assert "NOT NULL constraint failed" in str(e)