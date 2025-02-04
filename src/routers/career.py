from fastapi import APIRouter, Depends
from src.models.career import CreateCareerRequest
from src.services.career import CareerService
from src.models.career import Career
from sqlalchemy.orm import Session
from src.database import get_db

career_service = CareerService

router = APIRouter(
    prefix="/career",
    tags=['Career']
)

@router.post("")
async def create_career(career_request: CreateCareerRequest, db: Session= Depends(get_db)):
    career_service = CareerService(db)
    return career_service.create_career(career_request)


@router.get("")
async def get_all_career(db: Session= Depends(get_db)):
    career_service = CareerService(db)
    return career_service.get_all_carrers()


@router.put("")
async def update_career(career_id: int, career_request: CreateCareerRequest, db: Session= Depends(get_db)):
    career_service = CareerService(db)
    return career_service.update_career(career_id, career_request)


@router.delete("")
async def delete_career(career_id: int, db: Session= Depends(get_db)):
    career_service = CareerService(db)
    return career_service.delete_career(career_id)