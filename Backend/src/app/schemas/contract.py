from pydantic import BaseModel
from datetime import date
from typing import Optional

class ContractBase(BaseModel):
    home_id: int
    renter_id: int
    start_date: date
    end_date: date
    rent_amount: float
    payment_due_date: date
    annual_increase_percentage: float
    deposit_amount: float

class ContractCreate(ContractBase):
    pass

class ContractUpdate(ContractBase):
    pass

class ContractResponse(ContractBase):
    id: int
    created_at: str

