from src.database import Base
from sqlalchemy import Integer, ForeignKey, Column
from pydantic import BaseModel
from sqlalchemy.orm import relationship


class CareerTeacher(Base):
    __tablename__ = "career_teacher"

    id = Column(Integer, primary_key=True, index=True)
    # career_id = Column(Integer, ForeignKey("careers.id"), index=True)
    # teacher_id = Column(Integer, ForeignKey("teachers.id"), index=True)

    # career = relationship("Career", back_populates="career_teachers")
    # teacher = relationship("Teacher", back_populates="career_teachers")

    model_config = {
        "from_attributes": True,
        "arbitrary_types_allowed": True,
        "json_schema_extra": {
            "examples": [
                {
                    "career_id": 1,
                    "teacher_id": 2,
                },
            ]
        },
    }


class CreateCareerTeacherRequest(BaseModel):
    career_id: int
    teacher_id: int

    model_config = {
        "from_attributes": True,
        "arbitrary_types_allowed": True,
        "json_schema_extra": {
            "examples": [
                {
                    "career_id": 1,
                    "teacher_id": 2,
                },
            ]
        },
    }
