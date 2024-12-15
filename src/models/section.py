from src.database import Base
from sqlalchemy import String, Integer, Boolean, ForeignKey, Column
from pydantic import BaseModel

class Section(Base):
    __tablename__ = "section"
    id = Column(Integer, primary_key = True, index = True)
    course_id = Column(Integer, ForeignKey("course.id"), index = True)
    modality_id = Column(Integer, ForeignKey("modality.id"), index = True)
    academic_period_id = Column(Integer, ForeignKey("academic_period.id"), index = True)
    name = Column(Integer, index = True)
    model_config = {
        "from_attributes": True,
        "arbitrary_types_allowed": True,
        "json_schema_extra": {
            "examples": [
                {
                    "course_id": "4",
                    "modality_id": "1",
                    "academic_period_id": "2",
                    "name": "3"
                },
            ]
        }
    }


class CreateSectionRequest(BaseModel):
    course_id = int
    modality_id = int
    academic_period_id = int
    name = int
    model_config = {
        "from_attributes": True,
        "arbitrary_types_allowed": True,
        "json_schema_extra": {
            "examples": [
                {
                    "course_id": "4",
                    "modality_id": "1",
                    "academic_period_id": "2",
                    "name": "3"
                },
            ]
        }
    }