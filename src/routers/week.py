from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.database import get_db
from src.models.week import CreateWeekRequest
from src.services.week import WeekService

router = APIRouter(prefix="/week", tags=["Week"])


@router.post("")
async def create_week(week_request: CreateWeekRequest, db: Session = Depends(get_db)):
    week_service = WeekService(db)
    return week_service.create_week(week_request)


@router.get("")
async def get_all_weeks(db: Session = Depends(get_db)):
    week_service = WeekService(db)
    return week_service.get_all_weeks()


@router.get("/{week_id}")
async def get_week_by_id(week_id: int, db: Session = Depends(get_db)):
    week_service = WeekService(db)
    return week_service.get_week_by_id(week_id)


@router.put("/{week_id}")
async def update_week(
    week_id: int, week_request: CreateWeekRequest, db: Session = Depends(get_db)
):
    week_service = WeekService(db)
    return week_service.update_week(week_id, week_request)


@router.delete("/{week_id}")
async def delete_week(week_id: int, db: Session = Depends(get_db)):
    week_service = WeekService(db)
    return week_service.delete_week(week_id)
