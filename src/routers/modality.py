from fastapi import APIRouter, Depends
from src.models.modality import CreateModalityRequest
from src.services.modality import ModalityService
from sqlalchemy.orm import Session
from src.database import get_db


router = APIRouter(
    prefix="/modality",
    tags=['Modality']
)


@router.post("")
async def create_modality(modality_request: CreateModalityRequest, db: Session = Depends(get_db)):
    modality_service = ModalityService(db)
    return modality_service.create_modality(modality_request)


@router.get("")
async def get_all_modalities(db: Session = Depends(get_db)):
    modality_service = ModalityService(db)
    return modality_service.get_all_modalities()


@router.put("")
async def update_modality(modality_id: int, modality_request: CreateModalityRequest, db: Session = Depends(get_db)):
    modality_service = ModalityService(db)
    return modality_service.update_modality(modality_id, modality_request)


@router.delete("")
async def delete_modality(modality_id: int, db: Session = Depends(get_db)):
    modality_service = ModalityService(db)
    return modality_service.delete_modality(modality_id)
