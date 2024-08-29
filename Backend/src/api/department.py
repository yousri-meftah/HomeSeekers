from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database import get_db
from app.schemas.department import DepartmentCreate, DepartmentUpdate, DepartmentResponse,Departments
from app.controllers.department import create_department, get_department, update_department, delete_department,get_departments
from app.exceptions.base import NotFoundException
from redis_db import get_redis
from redis.asyncio import Redis
import json


router = APIRouter()

@router.post("/", response_model=DepartmentResponse)
def create_department_api(department_data: DepartmentCreate, db: Session = Depends(get_db)):
    try:
        return create_department(department_data, db)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error",
        )

@router.get("/{department_id}", response_model=DepartmentResponse)
def get_department_api(department_id: int, db: Session = Depends(get_db)):
    try:
        result =  get_department(department_id, db)
        return DepartmentResponse(**result.__dict__)
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

@router.get("/", response_model=Departments)
async def departments( db: Session = Depends(get_db) , redis :Redis = Depends(get_redis)):
    try:
        """cached_data = await redis.get("departments")
        if cached_data:
            return Departments.parse_raw(cached_data)"""
        res = []

        result =  get_departments(db)
        for val in result:
            res.append(DepartmentResponse(**val.__dict__))
        final_result = Departments(data=res)
        #await redis.set("departments",json.dumps(final_result.dict()))
        return final_result
    except NotFoundException as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e),
        )
    except Exception as e:
        print(e)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error",
        )

@router.put("/{department_id}", response_model=DepartmentResponse)
def update_department_api(department_id: int, department_data: DepartmentUpdate, db: Session = Depends(get_db)):
    try:
        return update_department(department_id, department_data, db)
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

@router.delete("/{department_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_department_api(department_id: int, db: Session = Depends(get_db)):
    try:
        delete_department(department_id, db)
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
