from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database import get_db
from app.schemas.home import HomeCreate, HomeUpdate, HomeResponse
from app.controllers.home import create_home, get_home, update_home, delete_home
from app.exceptions.base import NotFoundException, BadRequestException

router = APIRouter()

@router.post("/", response_model=HomeResponse)
def create_home_api(home_data: HomeCreate, db: Session = Depends(get_db)):
    try:
        return create_home(home_data, db)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error",
        )

@router.get("/{home_id}", response_model=HomeResponse)
def get_home_api(home_id: int, db: Session = Depends(get_db)):
    try:
        return get_home(home_id, db)
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

@router.put("/{home_id}", response_model=HomeResponse)
def update_home_api(home_id: int, home_data: HomeUpdate, db: Session = Depends(get_db)):
    try:
        return update_home(home_id, home_data, db)
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

@router.delete("/{home_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_home_api(home_id: int, db: Session = Depends(get_db)):
    try:
        delete_home(home_id, db)
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
