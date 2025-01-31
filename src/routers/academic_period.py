from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.database import get_db
from src.models.academic_period import CreateAcademicPeriodRequest
from src.services.academic_period import AcademicPeriodService


router = APIRouter(prefix="/academic_period", tags=["Academic Period"])


@router.post("")
async def create_academic_period(
    academic_period_request: CreateAcademicPeriodRequest, db: Session = Depends(get_db)
):
    academic_period_service = AcademicPeriodService(db)
    return academic_period_service.create_academic_period(academic_period_request)


@router.get("")
async def get_all_academic_periods(db: Session = Depends(get_db)):
    academic_period_service = AcademicPeriodService(db)
    return academic_period_service.get_all_academic_periods()


@router.get("/{academic_period_id}")
async def get_academic_period_by_id(
    academic_period_id: int, db: Session = Depends(get_db)
):
    academic_period_service = AcademicPeriodService(db)
    return academic_period_service.get_academic_period_by_id(academic_period_id)


@router.put("/{academic_period_id}")
async def update_academic_period(
    academic_period_id: int,
    academic_period_request: CreateAcademicPeriodRequest,
    db: Session = Depends(get_db),
):
    academic_period_service = AcademicPeriodService(db)
    return academic_period_service.update_academic_period(
        academic_period_id, academic_period_request
    )


@router.delete("/{academic_period_id}")
async def delete_academic_period(
    academic_period_id: int, db: Session = Depends(get_db)
):
    academic_period_service = AcademicPeriodService(db)
    return academic_period_service.delete_academic_period(academic_period_id)
