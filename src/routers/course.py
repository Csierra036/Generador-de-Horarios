from fastapi import APIRouter
from src.models.course import CreateCourseRequest
from src.services.course import CourseService

course_service = CourseService

router = APIRouter(
    prefix="/teacher",
    tags=['Teacher']
)

@router.post("")
async def create_course(teacher_request: CreateCourseRequest):
    return course_service.create_teacher(teacher_request)

@router.get("")
async def get_all_courses():
    return course_service.get_all_teachers

@router.put("")
async def update_course(teacher_id: int, teacher_request: CreateCourseRequest):
    return course_service.update_teacher(teacher_id, teacher_request)

@router.delete("")
async def delete_course(teacher_id: int):
    return course_service.delete_teacher(teacher_id)