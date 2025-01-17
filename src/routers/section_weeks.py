from fastapi import APIRouter
from src.models.section_weeks import CreateSectionWeeksRequest
from src.services.section_weeks import SectionWeeksService

section_weeks_service = SectionWeeksService

router = APIRouter(
    prefix="/section-weeks",
    tags=['SectionWeeks']
)

@router.post("")
async def create_section_week(section_weeks_request: CreateSectionWeeksRequest):
    return section_weeks_service.create_section_week(section_weeks_request)

@router.get("")
async def get_all_section_weeks():
    return section_weeks_service.get_all_section_weeks()

@router.get("/section/{section_id}")
async def get_weeks_by_section(section_id: int):
    return section_weeks_service.get_weeks_by_section(section_id)

@router.get("/week/{week_id}")
async def get_sections_by_week(week_id: int):
    return section_weeks_service.get_sections_by_week(week_id)

@router.put("")
async def update_section_week(section_id: int, week_id: int, section_weeks_request: CreateSectionWeeksRequest):
    return section_weeks_service.update_section_week(section_id, week_id, section_weeks_request)

@router.delete("")
async def delete_section_week(section_id: int, week_id: int):
    return section_weeks_service.delete_section_week(section_id, week_id)