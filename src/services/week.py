from fastapi import HTTPException
from sqlalchemy import String, Integer, Boolean, ForeignKey, Column
from src.database import DatabaseConnection, CustomSQLAlchemyRepository
from sqlalchemy.orm import relationship
from pydantic import BaseModel
from sqlalchemy.orm import Session
from src.models.week import Week, CreateWeekRequest

class WeekService:
    def __init__(self, db_session: Session):
        self.repository = CustomSQLAlchemyRepository(db=db_session, model=Week)

    def get_all_weeks(self):
        return self.repository.get_all()

    def get_week_by_id(self, week_id: int):
        teacher = self.repository.get(week_id)
        if not teacher:
            raise HTTPException(
                status_code=404, detail=f"Teacher with ID {week_id} not found"
            )
        return teacher

    def create_week(self, week_data: CreateWeekRequest):
        return self.repository.create(week_data.dict())

    def update_week(self, week_id: int, week_data: CreateWeekRequest):
        teacher = self.repository.get(week_id)
        if not teacher:
            raise HTTPException(
                status_code=404, detail=f"Week with ID {week_id} not found"
            )
        return self.repository.update(teacher, week_data.dict())

    def delete_week(self, week_id: int):
        teacher = self.repository.get(week_id)
        if not teacher:
            raise HTTPException(
                status_code=404, detail=f"Week with ID {week_id} not found"
            )
        return self.repository.delete(week_id)
