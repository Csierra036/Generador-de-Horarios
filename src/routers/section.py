from fastapi import APIRouter
from src.models.section import CreateSectionRequest
from src.services.section import SectionService

section_service = SectionService

router = APIRouter(
    prefix="/section",
    tags=['Section']
)

@router.post("")
async def create_section(section_request: CreateSectionRequest):
    return section_service.create_section(section_request)

@router.get("")
async def get_all_sections():
    return section_service.get_all_sections

@router.put("")
async def update_section(section_id: int, section_request: CreateSectionRequest):
    return section_service.update_section(section_id, section_request)

@router.delete("")
async def delete_section(section_id: int):
    return section_service.delete_section(section_id)