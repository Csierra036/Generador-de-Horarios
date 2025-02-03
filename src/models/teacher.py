from src.database import Base
from sqlalchemy import String, Integer, Boolean, ForeignKey, Column, func, DateTime
from pydantic import BaseModel
from src.models.career_teacher import CareerTeacher
from sqlalchemy.orm import relationship


class Teacher(Base):
    __tablename__ = "teachers"
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, index=True)
    last_name = Column(String, index=True)
    created_at = Column(DateTime, default=func.now())  # Se establece al crear
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())  # Se actualiza automáticamente

    # Relaciones
    # teacher_section = relationship("SectionTeacher", back_populates="teacher")
    # teacher_times = relationship("TeacherTime", back_populates="teacher")
    # career_teachers = relationship( CareerTeacher, back_populates="teacher")
    model_config = {
        "from_attributes": True,
        "arbitrary_types_allowed": True,
        "json_schema_extra": {
            "examples": [
                {"first_name": "Juan", "last_name": "Pedro"},
            ]
        },
    }


class CreateTeacherRequest(BaseModel):
    first_name: str
    last_name: str
    model_config = {
        "from_attributes": True,
        "arbitrary_types_allowed": True,
        "json_schema_extra": {
            "examples": [
                {"first_name": "Juan", "last_name": "Pedro"},
            ]
        },
    }
