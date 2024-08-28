from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database import get_db
from app.schemas.contract import ContractCreate, ContractUpdate, ContractResponse
from app.controllers.contract import create_contract, get_contract, update_contract, delete_contract
from app.exceptions.base import NotFoundException, BadRequestException
from redis.asyncio import Redis
from redis_db import get_redis

router = APIRouter()

@router.post("/", response_model=ContractResponse)
def create_contract_api(contract_data: ContractCreate,
                        db: Session = Depends(get_db),

                        ):
    try:
        return create_contract(contract_data, db)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error",
        )

@router.get("/{contract_id}", response_model=ContractResponse)
def get_contract_api(contract_id: int, db: Session = Depends(get_db),redis: Redis = Depends(get_redis)):
    try:
        return get_contract(contract_id, db,redis)
    except NotFoundException as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e),
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error",
        )

@router.put("/{contract_id}", response_model=ContractResponse)
def update_contract_api(contract_id: int, contract_data: ContractUpdate, db: Session = Depends(get_db)):
    try:
        return update_contract(contract_id, contract_data, db)
    except NotFoundException as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e),
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error",
        )

@router.delete("/{contract_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_contract_api(contract_id: int, db: Session = Depends(get_db)):
    try:
        delete_contract(contract_id, db)
    except NotFoundException as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e),
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error",
        )
