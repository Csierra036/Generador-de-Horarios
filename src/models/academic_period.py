from src.database import Base
from sqlalchemy import String, Integer, Boolean, ForeignKey, Column, relationship
from pydantic import BaseModel

class AcademicPeriod(Base):
    __tablename__ = "academic_period"
    id = Column(Integer, primary_key = True, index = True)
    name = Column(String, index = True)
    year = Column(Integer, index = True)
    number = Column(Integer, index = True)
    actual = Column(Boolean, index = True)

    weeks = relationship("Weeks", back_populates = "academic_period")

    model_config = {
        "from_attributes": True,
        "arbitrary_types_allowed": True,
        "json_schema_extra": {
            "examples": [
                {
                    "name": "null",
                    "year": "1",
                    "number": "2",
                    "actual": "true"
                },
            ]
        }
    }

class CreateAcademicPeriodRequest(BaseModel):
    name: String
    year = Integer
    number = Integer
    actual = Boolean
    model_config = {
        "from_attributes": True,
        "arbitrary_types_allowed": True,
        "json_schema_extra": {
            "examples": [
                {
                    "name": "null",
                    "year": "1",
                    "number": "2",
                    "actual": "true"
                },
            ]
        }
    }