from sqlalchemy.orm import Session
from redis.asyncio import Redis
from app.models import Contract
from app.schemas.contract import ContractCreate, ContractUpdate
from app.exceptions.base import NotFoundException

def create_contract(contract_data: ContractCreate, db: Session, redis: Redis):
    new_contract = Contract(**contract_data.dict())
    db.add(new_contract)
    db.commit()
    db.refresh(new_contract)
    redis.set(f"contract_{new_contract.id}", new_contract)
    return new_contract

def get_contract(contract_id: int, db: Session, redis: Redis):
    cached_contract = redis.get(f"contract_{contract_id}")
    if cached_contract:
        return cached_contract
    contract = db.query(Contract).filter(Contract.id == contract_id).first()
    if not contract:
        raise NotFoundException(detail="Contract not found")
    redis.set(f"contract_{contract.id}", contract)
    return contract

def update_contract(contract_id: int, contract_data: ContractUpdate, db: Session, redis: Redis):
    contract = db.query(Contract).filter(Contract.id == contract_id).first()
    if not contract:
        raise NotFoundException(detail="Contract not found")

    for key, value in contract_data.dict(exclude_unset=True).items():
        setattr(contract, key, value)

    db.commit()
    db.refresh(contract)
    redis.set(f"contract_{contract.id}", contract)
    return contract

def delete_contract(contract_id: int, db: Session, redis: Redis):
    contract = db.query(Contract).filter(Contract.id == contract_id).first()
    if not contract:
        raise NotFoundException(detail="Contract not found")

    db.delete(contract)
    db.commit()
    redis.delete(f"contract_{contract.id}")
