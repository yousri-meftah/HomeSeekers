from sqlalchemy.orm import Session
from app.models import Department
from app.schemas.department import DepartmentCreate, DepartmentUpdate,Departments
from app.exceptions.base import NotFoundException

def create_department(department_data: DepartmentCreate, db: Session):
    new_department = Department(**department_data.dict())
    db.add(new_department)
    db.commit()
    db.refresh(new_department)
    return new_department

def get_department(department_id: int, db: Session):
    department = db.query(Department).filter(Department.id == department_id).first()
    if not department:
        raise NotFoundException(detail="Department not found")
    return department

def get_departments(db: Session):
    department = db.query(Department).all()
    return department

def update_department(department_id: int, department_data: DepartmentUpdate, db: Session):
    department = db.query(Department).filter(Department.id == department_id).first()
    if not department:
        raise NotFoundException(detail="Department not found")

    for key, value in department_data.dict(exclude_unset=True).items():
        setattr(department, key, value)

    db.commit()
    db.refresh(department)
    return department

def delete_department(department_id: int, db: Session):
    department = db.query(Department).filter(Department.id == department_id).first()
    if not department:
        raise NotFoundException(detail="Department not found")

    db.delete(department)
    db.commit()
