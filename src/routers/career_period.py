from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.database import get_db
from src.models.career_period import CreateCareerPeriodRequest
from src.services.career_period import CareerPeriodService


router = APIRouter(prefix="/career_period", tags=["Career Period"])


@router.post("")
async def create_career_period(
    career_period_request: CreateCareerPeriodRequest, db: Session = Depends(get_db)
):
    career_period_service = CareerPeriodService(db)
    return career_period_service.create_career_period(career_period_request)


@router.get("")
async def get_all_career_periods(db: Session = Depends(get_db)):
    career_period_service = CareerPeriodService(db)
    return career_period_service.get_all_career_periods()


@router.get("/{career_period_id}")
async def get_career_period_by_id(career_period_id: int, db: Session = Depends(get_db)):
    career_period_service = CareerPeriodService(db)
    return career_period_service.get_career_period_by_id(career_period_id)


@router.put("/{career_period_id}")
async def update_career_period(
    career_period_id: int,
    career_period_request: CreateCareerPeriodRequest,
    db: Session = Depends(get_db),
):
    career_period_service = CareerPeriodService(db)
    return career_period_service.update_career_period(
        career_period_id, career_period_request
    )


@router.delete("/{career_period_id}")
async def delete_career_period(career_period_id: int, db: Session = Depends(get_db)):
    career_period_service = CareerPeriodService(db)
    return career_period_service.delete_career_period(career_period_id)
