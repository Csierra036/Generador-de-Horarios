from src.database import Base
from sqlalchemy import Integer, ForeignKey, Column
from pydantic import BaseModel
from sqlalchemy.orm import relationship


class CareerCampus(Base):
    __tablename__ = "career_campus"
    id = Column(Integer, primary_key=True, index=True)
    career_id = Column(Integer, ForeignKey("careers.id"), index=True)
    campus_id = Column(Integer, ForeignKey("campus.id"), index=True)

    # Relaciones (Opcional)
    career = relationship("Career", back_populates="career_campuses")
    campus = relationship("Campus", back_populates="career_campuses")


class CreateCareerCampusRequest(BaseModel):
    career_id: int
    campus_id: int
