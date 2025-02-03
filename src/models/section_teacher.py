from src.database import Base
from sqlalchemy import String, Integer, Boolean, ForeignKey, Column
from pydantic import BaseModel
from sqlalchemy.orm import relationship


class SectionTeacher(Base):
    __tablename__ = "section_teacher"
    id = Column(Integer, primary_key=True, index=True)
    section_id = Column(Integer, ForeignKey("sections.id"), index=True)
    teacher_id = Column(Integer, ForeignKey("teachers.id"), index=True)
    assigned_hours = Column(Integer, index=True)

    # Relaciones

    # section = relationship("Section", back_populates="teacher_section")
    # teacher = relationship("Teacher", back_populates="teacher_section")

    model_config = {
        "from_attributes": True,
        "arbitrary_types_allowed": True,
        "json_schema_extra": {
            "examples": [
                {"section_id": 1, "teacher_id": 2, "assigned_hours": 3},
            ]
        },
    }


class CreateSectionTeacherRequest(BaseModel):
    section_id: int
    teacher_id: int
    assigned_hours: int
    model_config = {
        "from_attributes": True,
        "arbitrary_types_allowed": True,
        "json_schema_extra": {
            "examples": [
                {"section_id": 1, "teacher_id": 2, "assigned_hours": 3},
            ]
        },
    }
