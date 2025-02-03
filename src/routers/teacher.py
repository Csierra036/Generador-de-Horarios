from fastapi import APIRouter,Depends
from src.models.teacher import CreateTeacherRequest
from src.services.teacher import TeacherService
from sqlalchemy.orm import Session
from src.database import get_db

router = APIRouter(
    prefix="/teacher",
    tags=['Teacher']
)

@router.post("")
async def create_teacher(teacher_request: CreateTeacherRequest, db: Session = Depends(get_db)):
    teacher_service = TeacherService(db)
    return teacher_service.create_teacher(teacher_request)

@router.get("")
async def get_all_teachers(db: Session = Depends(get_db)):
    teacher_service = TeacherService(db)
    return teacher_service.get_all_teachers()

@router.put("")
async def update_teacher(teacher_id: int, teacher_request: CreateTeacherRequest, db: Session = Depends(get_db)):
    teacher_service = TeacherService(db)
    return teacher_service.update_teacher(teacher_id, teacher_request)

@router.delete("")
async def delete_teacher(teacher_id: int, db: Session = Depends(get_db)):
    teacher_service = TeacherService(db)
    return teacher_service.delete_teacher(teacher_id)