from src.database import Base
from sqlalchemy import String, Integer, Boolean, ForeignKey, Column
from sqlalchemy.orm import relationship
from pydantic import BaseModel

class SectionWeeks(Base):
    __tablename__ = "section_weeks"
    
    id = Column(Integer, primary_key=True, index=True)
    section_id = Column(Integer, ForeignKey("sections.id"), index=True)
    week_id = Column(Integer, ForeignKey("weeks.id"), index=True)
    
    # Relaciones
    section = relationship("Section", back_populates="section_weeks")
    week = relationship("Weeks", back_populates="section_weeks")
    
    model_config = {
        "from_attributes": True,
        "arbitrary_types_allowed": True,
        "json_schema_extra": {
            "examples": [
                {
                    "section_id": "1",
                    "week_id": "1"
                },
            ]
        }
    }

class CreateSectionWeeksRequest(BaseModel):
    section_id: int
    week_id: int
    
    model_config = {
        "from_attributes": True,
        "arbitrary_types_allowed": True,
        "json_schema_extra": {
            "examples": [
                {
                    "section_id": "1",
                    "week_id": "1"
                },
            ]
        }
    }