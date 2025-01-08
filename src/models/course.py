from src.database import Base
from sqlalchemy import String, Integer, Column
from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, Boolean
from src.database import Base  

class Course(Base):
    __tablename__ = "courses"
    id = Column(Integer, primary_key=True, index=True)
    semester_id = Column(String, index=True)  
    name = Column(String, index=True)
    active = Column(Boolean, index=True)
    at_laboratory = Column(Boolean, index=True)
    
    # Configuración de ejemplos (opcional, no es estándar de SQLAlchemy)
    __example__ = {
        "from_attributes": True,
        "arbitrary_types_allowed": True,
        "json_schema_extra": {
            "examples": [
                {
                    "semester_id": "1",
                    "name": "Física I",
                    "active": True,
                    "at_laboratory": False
                },
            ]
        }
    }

class CreateCourseRequest(BaseModel):  # Modelo para validación y entrada
    semester_id : int
    name: str
    active: bool
    at_laboratory: bool
    model_config = {
        "from_attributes": True,
        "arbitrary_types_allowed": True,
        "json_schema_extra": {
            "examples": [
                {
                    "semester_id": "1",
                    "name": "Física I",
                    "active": True,
                    "at_laboratory": False
                },
            ]
        }
    }