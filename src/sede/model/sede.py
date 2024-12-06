from src.database import Base
from sqlalchemy import String, Integer, Column
from pydantic import BaseModel

class Sede(Base):  # Modelo para la base de datos
    __tablename__ = "sedes"
    id = Column(Integer, primary_key = True, index = True)
    name = Column(String, index = True)  # Ejemplo: "UNEG VILLA ASIA"
    location = Column(String, index = True)  # Ejemplo: "PUERTO ORDAZ"
    model_config = {
        "from_attributes": True,
        "arbitrary_types_allowed": True,
        "json_schema_extra": {
            "examples": [
                {
                    "nombre": "UNEG VILLA ASIA",
                    "ubicacion": "PUERTO ORDAZ"
                },
            ]
        }
    }


class CreateSedeRequest(BaseModel):  # Modelo para validación y entrada
    name: str
    location: str
    model_config = {
        "from_attributes": True,
        "arbitrary_types_allowed": True,
        "json_schema_extra": {
            "examples": [
                {
                    "name": "UNEG VILLA ASIA",
                    "location": "PUERTO ORDAZ"
                },
            ]
        }
    }
