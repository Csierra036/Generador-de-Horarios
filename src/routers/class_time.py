from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.database import get_db
from src.models.class_time import CreateClassTimeRequest
from src.services.class_time import ClassTimeService


router = APIRouter(prefix="/class_time", tags=["Class Time"])


@router.post("")
async def create_class_time(
    class_time_request: CreateClassTimeRequest, db: Session = Depends(get_db)
):
    class_time_service = ClassTimeService(db)
    return class_time_service.create_class_time(class_time_request)


@router.get("")
async def get_all_class_times(db: Session = Depends(get_db)):
    class_time_service = ClassTimeService(db)
    return class_time_service.get_all_class_times()


@router.get("/{class_time_id}")
async def get_class_time_by_id(class_time_id: int, db: Session = Depends(get_db)):
    class_time_service = ClassTimeService(db)
    return class_time_service.get_class_time_by_id(class_time_id)


@router.put("/{class_time_id}")
async def update_class_time(
    class_time_id: int,
    class_time_request: CreateClassTimeRequest,
    db: Session = Depends(get_db),
):
    class_time_service = ClassTimeService(db)
    return class_time_service.update_class_time(class_time_id, class_time_request)


@router.delete("/{class_time_id}")
async def delete_class_time(class_time_id: int, db: Session = Depends(get_db)):
    class_time_service = ClassTimeService(db)
    return class_time_service.delete_class_time(class_time_id)
