from fastapi import HTTPException
from src.database import CustomSQLAlchemyRepository
from sqlalchemy.orm import Session
from src.models.career_teacher import CareerTeacher, CreateCareerTeacherRequest


class CareerTeacherService:
    def __init__(self, db_session: Session):
        self.repository = CustomSQLAlchemyRepository(db=db_session, model=CareerTeacher)

    def get_all_career_teachers(self):
        return self.repository.get_all()

    def get_career_teacher_by_id(self, career_teacher_id: int):
        career_teacher = self.repository.get(career_teacher_id)
        if not career_teacher:
            raise HTTPException(
                status_code=404,
                detail=f"CareerTeacher with ID {career_teacher_id} not found",
            )
        return career_teacher

    def create_career_teacher(self, career_teacher_data: CreateCareerTeacherRequest):
        return self.repository.create(career_teacher_data.dict())

    def update_career_teacher(
        self, career_teacher_id: int, career_teacher_data: CreateCareerTeacherRequest
    ):
        career_teacher = self.repository.get(career_teacher_id)
        if not career_teacher:
            raise HTTPException(
                status_code=404,
                detail=f"CareerTeacher with ID {career_teacher_id} not found",
            )
        return self.repository.update(career_teacher, career_teacher_data.dict())

    def delete_career_teacher(self, career_teacher_id: int):
        career_teacher = self.repository.get(career_teacher_id)
        if not career_teacher:
            raise HTTPException(
                status_code=404,
                detail=f"CareerTeacher with ID {career_teacher_id} not found",
            )
        return self.repository.delete(career_teacher_id)
