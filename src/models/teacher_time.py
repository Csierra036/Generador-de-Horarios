from src.database import Base
from sqlalchemy import Integer, Boolean, ForeignKey, Column
from pydantic import BaseModel
from sqlalchemy.orm import relationship


class TeacherTime(Base):
    __tablename__ = "teacher_time"

    id = Column(Integer, primary_key=True, index=True)
    teacher_id = Column(Integer, ForeignKey("teachers.id"), index=True)
    time_block_id = Column(Integer, ForeignKey("time_blocks.id"), index=True)
    academic_period_id = Column(Integer, ForeignKey("academic_period.id"), index=True)
    available = Column(Boolean, default=True)

    teacher = relationship("Teacher", back_populates="teacher_times")
    time_block = relationship("TimeBlock", back_populates="teacher_times")
    academic_period = relationship("AcademicPeriod", back_populates="teacher_times")

    model_config = {
        "from_attributes": True,
        "arbitrary_types_allowed": True,
        "json_schema_extra": {
            "examples": [
                {
                    "teacher_id": 1,
                    "time_block_id": 2,
                    "academic_period_id": 3,
                    "available": True,
                },
            ]
        },
    }


class CreateTeacherTimeRequest(BaseModel):
    teacher_id: int
    time_block_id: int
    academic_period_id: int
    available: bool = True

    model_config = {
        "from_attributes": True,
        "arbitrary_types_allowed": True,
        "json_schema_extra": {
            "examples": [
                {
                    "teacher_id": 1,
                    "time_block_id": 2,
                    "academic_period_id": 3,
                    "available": True,
                },
            ]
        },
    }
