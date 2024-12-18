from src.database import Base
from sqlalchemy import String, Integer, Boolean, ForeignKey, Column
from sqlalchemy.orm import relationship
from pydantic import BaseModel

class TimeBlock(Base):
    __tablename__ = "time_blocks"
    id = Column(Integer, primary_key = True, index = True)
    hour_id = Column(Integer, ForeignKey("hours.id"), index = True)
    week_id= Column(Integer, ForeignKey("weeks.id"), index = True)
    day = Column(Integer, index = True)

    hours = relationship("Hours", back_populates = "time_block")
    weeks = relationship("Weeks", back_populates = "time_block") 
    model_config = {
        "from_attributes": True,
        "arbitrary_types_allowed": True,
        "json_schema_extra": {
            "examples": [
                {
                    "hour_id": "1",
                    "week_id": "4",
                    "day": "5",
                },
            ]
        }
    }


class CreateTimeBlockRequest(BaseModel):
    hour_id : int
    week_id : int
    day : int
    model_config = {
        "from_attributes": True,
        "arbitrary_types_allowed": True,
        "json_schema_extra": {
            "examples": [
                {
                    "hour_id": "1",
                    "week_id": "4",
                    "day": "5",
                },
            ]
        }
    }