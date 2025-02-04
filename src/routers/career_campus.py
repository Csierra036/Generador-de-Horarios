from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.database import get_db
from src.models.career_campus import CreateCareerCampusRequest
from src.services.career_campus import CareerCampusService

router = APIRouter(
    prefix="/career_campus",
    tags=["Career Campus"]
)


@router.post("")
async def create_career_campus(
    career_campus_request: CreateCareerCampusRequest, db: Session = Depends(get_db)
):
    career_campus_service = CareerCampusService(db)
    return career_campus_service.create_career_campus(career_campus_request)


@router.get("")
async def get_all_career_campuses(db: Session = Depends(get_db)):
    career_campus_service = CareerCampusService(db)
    return career_campus_service.get_all_career_campuses()


@router.get("/{career_campus_id}")
async def get_career_campus_by_id(career_campus_id: int, db: Session = Depends(get_db)):
    career_campus_service = CareerCampusService(db)
    return career_campus_service.get_career_campus_by_id(career_campus_id)


@router.put("/{career_campus_id}")
async def update_career_campus(career_campus_id: int,
                               career_campus_request: CreateCareerCampusRequest,db: Session = Depends(get_db),
):
    career_campus_service = CareerCampusService(db)
    return career_campus_service.update_career_campus(
        career_campus_id, career_campus_request
    )


@router.delete("/{career_campus_id}")
async def delete_career_campus(career_campus_id: int, db: Session = Depends(get_db)):
    career_campus_service = CareerCampusService(db)
    return career_campus_service.delete_career_campus(career_campus_id)
