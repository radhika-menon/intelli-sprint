from fastapi import FastAPI
from app.db.base import Base
from app.db.session import engine

# Import routers
from app.routers import activity, sprint_week, sprint_activity


app = FastAPI()

# Create database tables
Base.metadata.create_all(bind=engine)

# Include routers
app.include_router(activity.router)
app.include_router(sprint_week.router)
app.include_router(sprint_activity.router)


@app.get("/")
def root():
    return {"message": "Intelli Sprint API running"}