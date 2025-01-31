from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.database import get_db
from src.models.teacher_time import CreateTeacherTimeRequest
from src.services.teacher_time import TeacherTimeService


router = APIRouter(prefix="/teacher_time", tags=["Teacher Time"])


@router.post("")
async def create_teacher_time(
    teacher_time_request: CreateTeacherTimeRequest, db: Session = Depends(get_db)
):
    teacher_time_service = TeacherTimeService(db)
    return teacher_time_service.create_teacher_time(teacher_time_request)


@router.get("")
async def get_all_teacher_times(db: Session = Depends(get_db)):
    teacher_time_service = TeacherTimeService(db)
    return teacher_time_service.get_all_teacher_times()


@router.get("/{teacher_time_id}")
async def get_teacher_time_by_id(teacher_time_id: int, db: Session = Depends(get_db)):
    teacher_time_service = TeacherTimeService(db)
    return teacher_time_service.get_teacher_time_by_id(teacher_time_id)


@router.put("/{teacher_time_id}")
async def update_teacher_time(
    teacher_time_id: int,
    teacher_time_request: CreateTeacherTimeRequest,
    db: Session = Depends(get_db),
):
    teacher_time_service = TeacherTimeService(db)
    return teacher_time_service.update_teacher_time(
        teacher_time_id, teacher_time_request
    )


@router.delete("/{teacher_time_id}")
async def delete_teacher_time(teacher_time_id: int, db: Session = Depends(get_db)):
    teacher_time_service = TeacherTimeService(db)
    return teacher_time_service.delete_teacher_time(teacher_time_id)
