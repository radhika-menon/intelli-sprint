from fastapi import FastAPI
from app.db.base import Base
from app.db.session import engine

# Import routers
from app.routers import activity, sprint_week, sprint_activity

# CORS middleware to allow frontend to access API during development
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # for now (dev only)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create database tables
Base.metadata.create_all(bind=engine)

# Include routers
app.include_router(activity.router)
app.include_router(sprint_week.router)
app.include_router(sprint_activity.router)


@app.get("/")
def root():
    return {"message": "SprintAWeek API running"}
