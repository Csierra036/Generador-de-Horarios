from fastapi import APIRouter
from src.career.model.career import CreateCareerRequest
from src.career.services.service import CareerService

teacher_service = CareerService

router = APIRouter(
    prefix="/career",
    tags=['Career']
)

@router.post("")
async def create_career(teacher_request: CreateCareerRequest):
    return teacher_service.create_career(teacher_request)


@router.get("")
async def get_all_career():
    return teacher_service.get_all_careers


@router.put("")
async def update_career(teacher_id: int, teacher_request: CreateCareerRequest):
    return teacher_service.update_career(teacher_id, teacher_request)


@router.delete("")
async def delete_career(teacher_id: int):
    return teacher_service.delete_career(teacher_id)