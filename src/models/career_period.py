from src.database import Base
from sqlalchemy import String, Integer, Boolean, ForeignKey, Column
from pydantic import BaseModel
from sqlalchemy.orm import relationship


class Career_Period(Base):
    __tablename__ = "career_period"
    id = Column(Integer, primary_key=True, index=True)
    career_id = Column(Integer, ForeignKey("career.id"), index=True)
    period_id = Column(Integer, ForeignKey("period.id"), index=True)
    schedule_generated = Column(Boolean, default=False)

    # Relaciones (Opcional, si necesitas acceder a Career y Period desde Career_Period)
    career = relationship("Career", back_populates="career_periods")
    period = relationship("Period", back_populates="career_periods")

    model_config = {
        "from_attributes": True,
        "arbitrary_types_allowed": True,
        "json_schema_extra": {
            "examples": [
                {"career_id": 1, "period_id": 2, "schedule_generated": "false"},
            ]
        },
    }


class CreateCareerPeriodRequest(BaseModel):
    career_id: int
    period_id: int
    schedule_generated: bool = False

    model_config = {
        "from_attributes": True,
        "arbitrary_types_allowed": True,
        "json_schema_extra": {
            "examples": [
                {"career_id": 1, "period_id": 2, "schedule_generated": "false"},
            ]
        },
    }
