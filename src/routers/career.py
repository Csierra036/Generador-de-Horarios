from fastapi import APIRouter
from models.career import CreateCareerRequest
from src.services.career import CareerService
from src.models.career import Career

career_service = CareerService

router = APIRouter(
    prefix="/career",
    tags=['Career']
)

@router.post("")
async def create_career(career_request: CreateCareerRequest):
    return career_service.create_career(career_request)


@router.get("")
async def get_all_career():
    return career_service.get_all_careers


@router.put("")
async def update_career(career_id: int, career_request: CreateCareerRequest):
    return career_service.update_career(career_id, career_request)


@router.delete("")
async def delete_career(career_id: int):
    return career_service.delete_career(career_id)