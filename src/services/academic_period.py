from fastapi import HTTPException
from src.database import DatabaseConnection, CustomSQLAlchemyRepository
from sqlalchemy.orm import Session
from src.models.academic_period import AcademicPeriod, CreateAcademicPeriodRequest


class AcademicPeriodService:
    def __init__(self, db_session: Session):
        self.repository = CustomSQLAlchemyRepository(
            db=db_session, model=AcademicPeriod
        )

    def get_all_academic_periods(self):
        return self.repository.get_all()

    def get_academic_period_by_id(self, academic_period_id: int):
        academic_period = self.repository.get(academic_period_id)
        if not academic_period:
            raise HTTPException(
                status_code=404,
                detail=f"AcademicPeriod with ID {academic_period_id} not found",
            )
        return academic_period

    def create_academic_period(self, academic_period_data: CreateAcademicPeriodRequest):
        return self.repository.create(academic_period_data.dict())

    def update_academic_period(
        self, academic_period_id: int, academic_period_data: CreateAcademicPeriodRequest
    ):
        academic_period = self.repository.get(academic_period_id)
        if not academic_period:
            raise HTTPException(
                status_code=404,
                detail=f"AcademicPeriod with ID {academic_period_id} not found",
            )
        return self.repository.update(academic_period, academic_period_data.dict())

    def delete_academic_period(self, academic_period_id: int):
        academic_period = self.repository.get(academic_period_id)
        if not academic_period:
            raise HTTPException(
                status_code=404,
                detail=f"AcademicPeriod with ID {academic_period_id} not found",
            )
        return self.repository.delete(academic_period_id)
