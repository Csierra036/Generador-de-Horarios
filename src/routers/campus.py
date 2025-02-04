from src.models.campus import CreateCampusRequest
from src.services.campus import CampusService
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.database import get_db

router = APIRouter(
    prefix="/campus",
    tags=["Campus"]
)


@router.post("")
async def create_campus(campus_request: CreateCampusRequest, db: Session= Depends(get_db)):
    campus_service = CampusService(db)
    return campus_service.create_campus(campus_request)


@router.get("")
async def get_all_campus(db: Session= Depends(get_db)):
    campus_service = CampusService(db)
    return campus_service.get_all_campuses()


@router.get("/{campus_id}")
async def get_campus_by_id(campus_id: int, db: Session= Depends(get_db)):
    campus_service = CampusService(db)
    return campus_service.get_campus_by_id(campus_id)


@router.put("/{campus_id}")
async def update_campus(campus_id: int, campus_request: CreateCampusRequest, db: Session= Depends(get_db)):
    campus_service = CampusService(db)
    return campus_service.update_campus(campus_id, campus_request)


@router.delete("/{sede_id}")
async def delete_campus(campus_id: int, db: Session= Depends(get_db)):
    campus_service = CampusService(db)
    return campus_service.delete_campus(campus_id)
