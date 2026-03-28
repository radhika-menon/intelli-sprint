from datetime import datetime
from sqlalchemy import Column, Integer, Date, DateTime
from app.db.base import Base

class SprintWeek(Base):
    __tablename__ = "sprint_weeks"

    id = Column(Integer, primary_key=True, index=True)
    week_start_date = Column(Date, nullable=False)
    semester_week = Column(Integer, nullable=False)
    created_at = Column(DateTime, default=datetime.now)