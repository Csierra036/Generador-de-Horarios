from fastapi import HTTPException
from src.database import CustomSQLAlchemyRepository
from sqlalchemy.orm import Session
from src.models.career_campus import Career_Campus, CreateCareerCampusRequest


class CareerCampusService:
    def __init__(self, db_session: Session):
        self.repository = CustomSQLAlchemyRepository(db=db_session, model=Career_Campus)

    def get_all_career_campuses(self):
        return self.repository.get_all()

    def get_career_campus_by_id(self, career_campus_id: int):
        career_campus = self.repository.get(career_campus_id)
        if not career_campus:
            raise HTTPException(
                status_code=404,
                detail=f"Career_Campus with ID {career_campus_id} not found",
            )
        return career_campus

    def create_career_campus(self, career_campus_data: CreateCareerCampusRequest):
        return self.repository.create(career_campus_data.dict())

    def update_career_campus(
        self, career_campus_id: int, career_campus_data: CreateCareerCampusRequest
    ):
        career_campus = self.repository.get(career_campus_id)
        if not career_campus:
            raise HTTPException(
                status_code=404,
                detail=f"Career_Campus with ID {career_campus_id} not found",
            )
        return self.repository.update(career_campus, career_campus_data.dict())

    def delete_career_campus(self, career_campus_id: int):
        career_campus = self.repository.get(career_campus_id)
        if not career_campus:
            raise HTTPException(
                status_code=404,
                detail=f"Career_Campus with ID {career_campus_id} not found",
            )
        return self.repository.delete(career_campus_id)
