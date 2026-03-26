from app.db.base import Base
from app.db.session import engine

# Import models so they register with Base
from app.models import activity, sprint_week, sprint_activity

# Test to ensure that the database tables are created correctly based on the SQLAlchemy models
# defined in Base.
def test_tables_created():
    tables = Base.metadata.tables.keys()

    assert "activities" in tables
    assert "sprint_weeks" in tables
    assert "sprint_activities" in tables