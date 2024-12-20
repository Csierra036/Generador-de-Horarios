# Modelo de datos

from pydantic import BaseModel
from src.database import Base
from sqlalchemy import String, Integer, Column
from pydantic import BaseModel

class Salon(BaseModel):
    __tablename__ = "salones"
    id = Column(Integer, primary_key = True, index = True)
    nombre = Column(String, index = True)
    capacidad = Column(Integer, index = True)
    ubicacion = Column(String, index = True)


class CreateSalonRequest():
    nombre: str
    capacidad: int = 0
    ubicacion: str
    model_config = {
        "from_attributes": True,
        "arbitrary_types_allowed": True,
        "json_schema_extra": {
            "examples": [
                {
                    "Nombre" : "Juan",
                    "Capacidad" : 40,
                    "ubicacion" : "Pto Ordaz",

                },
            ]
        }
    }

