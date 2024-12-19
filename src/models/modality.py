from src.database import Base
from sqlalchemy import Column, Integer, String
from pydantic import BaseModel

# Modelo para la tabla "modality" en la base de datos
class Modality(Base):
    __tablename__ = "modality"
    id = Column(Integer, primary_key=True, index=True)  # Identificador único
    name = Column(String, unique=True, nullable=False, index=True)  # Nombre de la modalidad

    # Configuración adicional para generar esquemas JSON de ejemplo
    model_config = {
        "from_attributes": True,
        "arbitrary_types_allowed": True,
        "json_schema_extra": {
            "examples": [
                {"id": 1, "name": "Online"},
                {"id": 2, "name": "In-person"}
            ]
        }
    }

# Modelo Pydantic para validar y estructurar las solicitudes de creación
class CreateModalityRequest(BaseModel):
    name: str  # Nombre de la modalidad (obligatorio)

    # Configuración adicional para generar esquemas JSON de ejemplo
    model_config = {
        "from_attributes": True,
        "arbitrary_types_allowed": True,
        "json_schema_extra": {
            "examples": [
                {"name": "Online"},
                {"name": "In-person"}
            ]
        }
    }
