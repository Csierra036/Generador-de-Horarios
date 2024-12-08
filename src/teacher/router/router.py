from fastapi import APIRouter
from src.teacher.model.teacher import CreateTeacherRequest
from src.teacher.service.service import TeacherService

teacher_service = TeacherService

router = APIRouter(
    prefix="/teacher",
    tags=['Teacher']
)

@router.post("")
async def create_teacher(teacher_request: CreateTeacherRequest):
    return teacher_service.create_teacher(teacher_request)

@router.get("")
async def get_all_teachers():
    return teacher_service.get_all_teachers

@router.put("")
async def update_teacher(teacher_id: int, teacher_request: CreateTeacherRequest):
    return teacher_service.update_teacher(teacher_id, teacher_request)

@router.delete("")
async def delate_teacher(teacher_id: int):
    return teacher_service.delete_teacher(teacher_id)