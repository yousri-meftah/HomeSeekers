from pydantic import BaseModel
from typing import Optional

class HomeBase(BaseModel):
    address: str
    description: Optional[str]
    department_id: Optional[int]

class HomeCreate(HomeBase):
    pass

class HomeUpdate(HomeBase):
    pass

class HomeResponse(HomeBase):
    id: int
    owner_id: int
    created_at: str

