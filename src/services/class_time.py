from fastapi import HTTPException
from src.database import CustomSQLAlchemyRepository
from sqlalchemy.orm import Session
from src.models.class_time import ClassTime, CreateClassTimeRequest


class ClassTimeService:
    def __init__(self, db_session: Session):
        self.repository = CustomSQLAlchemyRepository(db=db_session, model=ClassTime)

    def get_all_class_times(self):
        return self.repository.get_all()

    def get_class_time_by_id(self, class_time_id: int):
        class_time = self.repository.get(class_time_id)
        if not class_time:
            raise HTTPException(
                status_code=404,
                detail=f"ClassTime with ID {class_time_id} not found",
            )
        return class_time

    def create_class_time(self, class_time_data: CreateClassTimeRequest):
        return self.repository.create(class_time_data.dict())

    def update_class_time(
        self, class_time_id: int, class_time_data: CreateClassTimeRequest
    ):
        class_time = self.repository.get(class_time_id)
        if not class_time:
            raise HTTPException(
                status_code=404,
                detail=f"ClassTime with ID {class_time_id} not found",
            )
        return self.repository.update(class_time, class_time_data.dict())

    def delete_class_time(self, class_time_id: int):
        class_time = self.repository.get(class_time_id)
        if not class_time:
            raise HTTPException(
                status_code=404,
                detail=f"ClassTime with ID {class_time_id} not found",
            )
        return self.repository.delete(class_time_id)
