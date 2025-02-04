from fastapi import APIRouter, Depends
from src.models.course import CreateCourseRequest
from src.services.course import CourseService
from sqlalchemy.orm import Session
from src.database import get_db


router = APIRouter(
    prefix="/course",
    tags=['Course']
)

@router.post("")
async def create_course(course_request: CreateCourseRequest, db: Session = Depends(get_db)):
    course_service = CourseService(db)
    return course_service.create_course(course_request)


@router.get("")
async def get_all_courses(db: Session = Depends(get_db)):
    course_service = CourseService(db)
    return course_service.get_all_courses()


@router.put("")
async def update_course(course_id: int, course_request: CreateCourseRequest, db: Session = Depends(get_db)):
    course_service = CourseService(db)
    return course_service.update_course(course_id, course_request)


@router.delete("")
async def delete_course(teacher_id: int, db: Session = Depends(get_db)):
    course_service = CourseService(db)
    return course_service.delete_course(teacher_id)