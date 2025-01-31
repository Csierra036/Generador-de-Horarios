from fastapi import HTTPException
from src.database import CustomSQLAlchemyRepository
from sqlalchemy.orm import Session
from src.models.teacher_time import TeacherTime, CreateTeacherTimeRequest


class TeacherTimeService:
    def __init__(self, db_session: Session):
        self.repository = CustomSQLAlchemyRepository(db=db_session, model=TeacherTime)

    def get_all_teacher_times(self):
        return self.repository.get_all()

    def get_teacher_time_by_id(self, teacher_time_id: int):
        teacher_time = self.repository.get(teacher_time_id)
        if not teacher_time:
            raise HTTPException(
                status_code=404,
                detail=f"TeacherTime with ID {teacher_time_id} not found",
            )
        return teacher_time

    def create_teacher_time(self, teacher_time_data: CreateTeacherTimeRequest):
        return self.repository.create(teacher_time_data.dict())

    def update_teacher_time(
        self, teacher_time_id: int, teacher_time_data: CreateTeacherTimeRequest
    ):
        teacher_time = self.repository.get(teacher_time_id)
        if not teacher_time:
            raise HTTPException(
                status_code=404,
                detail=f"TeacherTime with ID {teacher_time_id} not found",
            )
        return self.repository.update(teacher_time, teacher_time_data.dict())

    def delete_teacher_time(self, teacher_time_id: int):
        teacher_time = self.repository.get(teacher_time_id)
        if not teacher_time:
            raise HTTPException(
                status_code=404,
                detail=f"TeacherTime with ID {teacher_time_id} not found",
            )
        return self.repository.delete(teacher_time_id)
