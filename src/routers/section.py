from fastapi import APIRouter, Depends
from src.models.section import CreateSectionRequest
from src.services.section import SectionService
from sqlalchemy.orm import Session
from src.database import get_db


router = APIRouter(
    prefix="/section",
    tags=['Section']
)

@router.post("")
async def create_section(section_request: CreateSectionRequest, db: Session = Depends(get_db)):
    section_service = SectionService(db)
    return section_service.create_section(section_request)


@router.get("")
async def get_all_sections(db: Session = Depends(get_db)):
    section_service = SectionService(db)
    return section_service.get_all_sections


@router.put("")
async def update_section(section_id: int, section_request: CreateSectionRequest, db: Session = Depends(get_db)):
    section_service = SectionService(db)
    return section_service.update_section(section_id, section_request)


@router.delete("")
async def delete_section(section_id: int, db: Session = Depends(get_db)):
    section_service = SectionService(db)
    return section_service.delete_section(section_id)