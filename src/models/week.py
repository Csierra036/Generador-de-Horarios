from src.database import Base
from sqlalchemy import String, Integer, Boolean, ForeignKey, Column
from sqlalchemy.orm import relationship
from pydantic import BaseModel


class Week(Base):
    __tablename__ = "weeks"
    id = Column(Integer, primary_key=True, index=True)
    period_id = Column(Integer, ForeignKey("academic_period.id"), index=True)
    number = Column(Integer, index=True)

    academic_period = relationship("AcademicPeriod", back_populates="week")
    time_block = relationship("TimeBlock", back_populates="week")

    model_config = {
        "from_attributes": True,
        "arbitrary_types_allowed": True,
        "json_schema_extra": {
            "examples": [
                {
                    "period_id": "null",
                    "number": "1",
                },
            ]
        },
    }


class CreateWeekRequest(BaseModel):
    period_id: Integer
    number: Integer
    model_config = {
        "from_attributes": True,
        "arbitrary_types_allowed": True,
        "json_schema_extra": {
            "examples": [
                {
                    "period_id": "1",
                    "number": "1",
                },
            ]
        },
    }