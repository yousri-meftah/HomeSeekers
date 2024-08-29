from pydantic import BaseModel
from datetime import datetime

class DepartmentBase(BaseModel):
    name: str

class DepartmentCreate(DepartmentBase):
    pass

class DepartmentUpdate(DepartmentBase):
    pass

class DepartmentResponse(DepartmentBase):
    id: int| None
    created_at: datetime | None

class Departments(BaseModel):
    data : list[DepartmentResponse]
