import pytest
from sqlalchemy.orm import Session
from src.app.models import Department
from src.database import SessionLocal


@pytest.fixture(scope="function")
def db_session():
    db = SessionLocal()
    transaction = db.begin()  # Start a transaction
    try:
        yield db
        transaction.rollback()  # Rollback the transaction after the test
    finally:
        db.close()

def test_create_department(db_session: Session):
    new_department = Department(name="Engineering")
    db_session.add(new_department)
    db_session.commit()

    department = db_session.query(Department).filter_by(name="Engineering").first()
    assert department is not None
    assert department.name == "Engineering"

def test_read_department(db_session: Session):
    department = db_session.query(Department).filter_by(name="Engineering").first()
    assert department is not None
    assert department.name == "Engineering"

def test_update_department(db_session: Session):
    department = db_session.query(Department).filter_by(name="Engineering").first()
    department.name = "Updated Engineering"
    db_session.commit()

    updated_department = db_session.query(Department).filter_by(name="Updated Engineering").first()
    assert updated_department.name == "Updated Engineering"

def test_delete_department(db_session: Session):
    department = db_session.query(Department).filter_by(name="Updated Engineering").first()
    db_session.delete(department)
    db_session.commit()

    deleted_department = db_session.query(Department).filter_by(name="Updated Engineering").first()
    assert deleted_department is None
