from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.database import get_db
from src.models.career_teacher import CreateCareerTeacherRequest
from src.services.career_teacher import CareerTeacherService


router = APIRouter(
    prefix="/career_teacher",
    tags=["Career Teacher"]
)


@router.post("")
async def create_career_teacher(
    career_teacher_request: CreateCareerTeacherRequest, db: Session = Depends(get_db)
):
    career_teacher_service = CareerTeacherService(db)
    return career_teacher_service.create_career_teacher(career_teacher_request)


@router.get("")
async def get_all_career_teachers(db: Session = Depends(get_db)):
    career_teacher_service = CareerTeacherService(db)
    return career_teacher_service.get_all_career_teachers()


@router.get("/{career_teacher_id}")
async def get_career_teacher_by_id(
    career_teacher_id: int, db: Session = Depends(get_db)
):
    career_teacher_service = CareerTeacherService(db)
    return career_teacher_service.get_career_teacher_by_id(career_teacher_id)


@router.put("/{career_teacher_id}")
async def update_career_teacher(
    career_teacher_id: int,
    career_teacher_request: CreateCareerTeacherRequest,
    db: Session = Depends(get_db),
):
    career_teacher_service = CareerTeacherService(db)
    return career_teacher_service.update_career_teacher(
        career_teacher_id, career_teacher_request
    )


@router.delete("/{career_teacher_id}")
async def delete_career_teacher(career_teacher_id: int, db: Session = Depends(get_db)):
    career_teacher_service = CareerTeacherService(db)
    return career_teacher_service.delete_career_teacher(career_teacher_id)
