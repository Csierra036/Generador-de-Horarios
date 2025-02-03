from src.database import Base
from sqlalchemy import Integer, ForeignKey, Column, Boolean
from pydantic import BaseModel
from sqlalchemy.orm import relationship


class ClassTime(Base):
    __tablename__ = "class_time"

    id = Column(Integer, primary_key=True, index=True)
    # class_room_id = Column(Integer, ForeignKey("classrooms.id"), index=True)
    # time_block_id = Column(Integer, ForeignKey("time_blocks.id"), index=True)
    available = Column(Boolean, default=True)
    # class_room = relationship("ClassRoom", back_populates="class_times")
    # time_block = relationship("TimeBlock", back_populates="class_times")

    model_config = {
        "from_attributes": True,
        "arbitrary_types_allowed": True,
        "json_schema_extra": {
            "examples": [
                {
                    "class_room_id": 1,
                    "time_block_id": 2,
                },
            ]
        },
    }


class CreateClassTimeRequest(BaseModel):
    class_room_id: int
    time_block_id: int

    model_config = {
        "from_attributes": True,
        "arbitrary_types_allowed": True,
        "json_schema_extra": {
            "examples": [
                {
                    "class_room_id": 1,
                    "time_block_id": 2,
                },
            ]
        },
    }
