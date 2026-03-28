from fastapi.testclient import TestClient
from app.main import app, get_db
from app.db.base import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import date

# Create test DB
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False}
)

TestingSessionLocal = sessionmaker(bind=engine)

# Override get_db
def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

# Apply override
app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)

Base.metadata.create_all(bind=engine)

def test_create_activity():
    response = client.post("/activities", json={"name": "Build API endpoints"})

    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Build API endpoints"

def test_get_activities():
    client.post("/activities", json={"name": "Task 1"})

    response = client.get("/activities")

    assert response.status_code == 200
    data = response.json()
    assert len(data) >= 1

# Assert on response values to ensure correct data is returned, e.g.
# week_start_date is correctly formatted and semester_week is correct, instead
# of internal object representation which may not be JSON serializable. This
# also ensures the API is returning data in the expected format for clients.
def test_create_sprint_week():
    response = client.post(
        "/sprint-weeks", 
        json={
            "week_start_date": "2026-03-10", 
            "semester_week": 1
            }
        )

    assert response.status_code == 200
    data = response.json()
    # confirm that a database is created and the returned data contains the
    # expected fields with correct values.
    assert "id" in data
    assert data["week_start_date"] == "2026-03-10"
    assert data["semester_week"] == 1

def test_get_sprint_weeks():
    client.post(
        "/sprint-weeks", 
        json={
            "week_start_date": "2026-03-10", 
            "semester_week": 1
            }
        )

    response = client.get("/sprint-weeks")

    assert response.status_code == 200
    data = response.json()

    # This checks that the API is returning a list of sprint weeks and that the
    # data for the created sprint week is correctly formatted and included in
    # the response. It also ensures that the API is correctly serialising date
    # fields to ISO format strings, which is important for client compatibility.
    assert any(
        sprint["semester_week"] == 1 and sprint["week_start_date"] == "2026-03-10"
    for sprint in data
    )

def test_add_activity_to_sprint():
    # Create activity
    activity_response = client.post("/activities", json={"name": "Test Activity"})
    activity_id = activity_response.json()["id"]

    # Create sprint week
    sprint_response = client.post(
        "/sprint-weeks", 
        json={
            "week_start_date": "2026-03-10", 
            "semester_week": 1
            }
        )
    sprint_week_id = sprint_response.json()["id"]

    # Add activity to sprint week
    response = client.post(
        f"/sprint-weeks/{sprint_week_id}/activities",
        json={
            "activity_id": activity_id,
            "days": ["Mon", "Wed"],
            "status": "Planned"         
        }
    )

    assert response.status_code == 200
    assert len(response.json()) == 2
    for entry in response.json():
        assert entry["activity_id"] == activity_id
        assert entry["sprint_week_id"] == sprint_week_id
        assert entry["status"] == "Planned"
        assert entry["assigned_day"] in ["Mon", "Wed"]  
    
def test_add_activity_to_nonexistent_sprint():
    response = client.post(
        "/sprint-weeks/999/activities",
        json={
            "activity_id": 1,
            "days": ["Mon"],
            "status": "Planned"
        }
    )

    assert response.status_code == 404
    assert response.json()["detail"] == "Sprint week not found"

def test_add_nonexistent_activity_to_sprint():
    # Create sprint week
    sprint_response = client.post(
        "/sprint-weeks", 
        json={
            "week_start_date": "2026-03-10", 
            "semester_week": 1
            }
        )
    sprint_week_id = sprint_response.json()["id"]

    response = client.post(
        f"/sprint-weeks/{sprint_week_id}/activities",
        json={
            "activity_id": 999,
            "days": ["Mon"],
            "status": "Planned"
        }
    )

    assert response.status_code == 404
    assert response.json()["detail"] == "Activity not found"   

def test_get_activities_for_sprint_week():
    # Create activity
    activity_response = client.post("/activities", json={"name": "Test Activity"})
    activity_id = activity_response.json()["id"]

    # Create sprint week
    sprint_response = client.post(
        "/sprint-weeks", 
        json={
            "week_start_date": "2026-03-10", 
            "semester_week": 1
            }
        )
    sprint_week_id = sprint_response.json()["id"]

    # Add activity to sprint week
    client.post(
        f"/sprint-weeks/{sprint_week_id}/activities",
        json={
            "activity_id": activity_id,
            "days": ["Mon", "Wed"],
            "status": "Planned"
        }
    )   

    response= client.get(f"/sprint-weeks/{sprint_week_id}/activities")  

    assert response.status_code == 200
    data = response.json()
    assert len(data) == 2
    for entry in data:
        assert entry["activity_id"] == activity_id
        assert entry["sprint_week_id"] == sprint_week_id
        assert entry["status"] == "Planned"
        assert entry["assigned_day"] in ["Mon", "Wed"]    

def test_invalid_status_for_sprint_activity():
    # Create activity
    activity_response = client.post("/activities", json={"name": "Test Activity"})
    activity_id = activity_response.json()["id"]

    # Create sprint week
    sprint_response = client.post(
        "/sprint-weeks", 
        json={
            "week_start_date": "2026-03-10", 
            "semester_week": 1
            }
        )
    sprint_week_id = sprint_response.json()["id"]

    response = client.post(
        f"/sprint-weeks/{sprint_week_id}/activities",
        json={
            "activity_id": activity_id,
            "days": ["Mon"],
            "status": "Ongoing"  # Invalid status
        }
        )   
    assert response.status_code == 422

def test_invalid_day_for_sprint_activity():
    # Create activity
    activity_response = client.post("/activities", json={"name": "Test Activity"})
    activity_id = activity_response.json()["id"]

    # Create sprint week
    sprint_response = client.post(
        "/sprint-weeks", 
        json={
            "week_start_date": "2026-03-10", 
            "semester_week": 1
            }
        )
    sprint_week_id = sprint_response.json()["id"]

    response = client.post(
        f"/sprint-weeks/{sprint_week_id}/activities",
        json={
            "activity_id": activity_id,
            "days": ["Monday"],  # Invalid day format, should be "Mon"
            "status": "Planned"
        }
        )
    assert response.status_code == 422