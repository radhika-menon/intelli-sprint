from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy import Enum as SQLAlchemyEnum
from datetime import datetime
from app.db.base import Base
from app.models.enums import ActivityStatus, WeekDay

class SprintActivity(Base):
    __tablename__ = "sprint_activities"

    id = Column(Integer, primary_key=True, index=True)
    # Foreign keys to link to sprint_weeks and activities tables
    sprint_week_id = Column(Integer, ForeignKey("sprint_weeks.id"))
    activity_id = Column(Integer, ForeignKey("activities.id"))

    # User-assigned day of the week for the activity
    # Note: since an activity can span multiple days, there will be multiple entries in this  
    # table for the same activity with different assigned_day values.
    assigned_day = Column(
      SQLAlchemyEnum(WeekDay),
      nullable=False
      )

    # Status of the activity (planned, in progress, achieved, on hold, dropped)
    status = Column(
      SQLAlchemyEnum(ActivityStatus),
      default=ActivityStatus.planned
  )