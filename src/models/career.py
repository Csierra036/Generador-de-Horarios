from src.database import Base
from sqlalchemy import String, Integer, Boolean, ForeignKey, Column
from pydantic import BaseModel
from sqlalchemy.orm import relationship


class Career(Base):
    __tablename__ = "careers"
    id = Column(Integer, primary_key=True, index=True)
    fullname = Column(String, index=True)

    career_periods = relationship("Career_Period", back_populates="career")
    career_campuses = relationship("Career_Campus", back_populates="career")
    career_teachers = relationship("Career", back_populates="career")

    model_config = {
        "from_attributes": True,
        "arbitrary_types_allowed": True,
        "json_schema_extra": {"examples": [{"fullname": "Ingenieria en Informatica"}]},
    }


class CreateCareerRequest(BaseModel):
    fullname: str
    model_config = {
        "from_attributes": True,
        "arbitrary_types_allowed": True,
        "json_schema_extra": {
            "examples": [
                {
                    "fullname": "Ingenieria en Informatica",
                }
            ]
        },
    }
