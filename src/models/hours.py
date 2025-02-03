from src.database import Base
from sqlalchemy import String, Integer, Boolean, ForeignKey, Column
from sqlalchemy.orm import relationship
from pydantic import BaseModel

class Hours(Base):
    __tablename__ = "hours"
    id = Column(Integer, primary_key = True, index = True)
    name = Column(String, index = True)
    start = Column(String, index = True)
    end = Column(String, index = True)

    # time_block = relationship("TimeBlock", back_populates = "hours")

    model_config = {
        "from_attributes": True,
        "arbitrary_types_allowed": True,
        "json_schema_extra": {
            "examples": [
                {
                    "name": "null",
                    "start": "7:50",
                    "end": "8:40",
                },
            ]
        }
    }

class CreateHoursRequest(BaseModel):
    name: String
    start: String
    end: String
    model_config = {
        "from_attributes": True,
        "arbitrary_types_allowed": True,
        "json_schema_extra": {
            "examples": [
                {
                    "name": "null",
                    "start": "7:50",
                    "end": "8:40",
                },
            ]
        }
    }