from fastapi import HTTPException
from src.database import DatabaseConnection, CustomSQLAlchemyRepository
from sqlalchemy.orm import Session
from src.models.career_period import Career_Period, CreateCareerPeriodRequest


class CareerPeriodService:
    def __init__(self, db_session: Session):
        self.repository = CustomSQLAlchemyRepository(db=db_session, model=Career_Period)

    def get_all_career_periods(self):
        return self.repository.get_all()

    def get_career_period_by_id(self, career_period_id: int):
        career_period = self.repository.get(career_period_id)
        if not career_period:
            raise HTTPException(
                status_code=404,
                detail=f"Career_Period with ID {career_period_id} not found",
            )
        return career_period

    def create_career_period(self, career_period_data: CreateCareerPeriodRequest):
        return self.repository.create(career_period_data.dict())

    def update_career_period(
        self, career_period_id: int, career_period_data: CreateCareerPeriodRequest
    ):
        career_period = self.repository.get(career_period_id)
        if not career_period:
            raise HTTPException(
                status_code=404,
                detail=f"Career_Period with ID {career_period_id} not found",
            )
        return self.repository.update(career_period, career_period_data.dict())

    def delete_career_period(self, career_period_id: int):
        career_period = self.repository.get(career_period_id)
        if not career_period:
            raise HTTPException(
                status_code=404,
                detail=f"Career_Period with ID {career_period_id} not found",
            )
        return self.repository.delete(career_period_id)
