from src.database import Base
from sqlalchemy import String, Integer, Boolean, ForeignKey, Column
from pydantic import BaseModel
from sqlalchemy.orm import relationship


class Section(Base):
    __tablename__ = "sections"
    id = Column(Integer, primary_key=True, index=True)
    course_id = Column(Integer, ForeignKey("courses.id"), index=True)
    modality_id = Column(Integer, ForeignKey("modality.id"), index=True)
    academic_period_id = Column(Integer, ForeignKey("academic_period.id"), index=True)
    name = Column(Integer, index=True)

    # Relaciones
    course = relationship("Course", back_populates="sections")
    modality = relationship("Modality", back_populates="sections")
    academic_period = relationship("AcademicPeriod", back_populates="sections")
    teacher_section = relationship("SectionTeacher", back_populates="section")

    model_config = {
        "from_attributes": True,
        "arbitrary_types_allowed": True,
        "json_schema_extra": {
            "examples": [
                {
                    "course_id": "4",
                    "modality_id": "1",
                    "academic_period_id": "2",
                    "name": "3",
                },
            ]
        },
    }


class CreateSectionRequest(BaseModel):
    course_id: int
    modality_id: int
    academic_period_id: int
    name: int
    model_config = {
        "from_attributes": True,
        "arbitrary_types_allowed": True,
        "json_schema_extra": {
            "examples": [
                {
                    "course_id": "4",
                    "modality_id": "1",
                    "academic_period_id": "2",
                    "name": "3",
                },
            ]
        },
    }
