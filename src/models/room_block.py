from src.database import Base
from sqlalchemy import Integer, Boolean, ForeignKey, Column
from pydantic import BaseModel
from sqlalchemy.orm import relationship


# Modelo para la tabla "room_block"
class RoomBlock(Base):
    __tablename__ = "room_blocks"
    id = Column(Integer, primary_key=True, index=True)  # Identificador único
    block_id = Column(Integer, ForeignKey("time_blocks.id"), index=True)  # Relación con la tabla "bloque_clases"
    room_id = Column(Integer, ForeignKey("classrooms.id"), index=True)  # Relación con la tabla "salones
    available = Column(Boolean, default=True)  # Indica si está disponible

    # Relaciones con otras tablas
    block = relationship("BlockClass", back_populates="room_blocks")
    room = relationship("Room", back_populates="room_blocks")

    # Configuración para generar ejemplos JSON
    model_config = {
        "from_attributes": True,
        "arbitrary_types_allowed": True,
        "json_schema_extra": {
            "examples": [
                {"block_id": 1, "room_id": 2, "available": True},
            ]
        },
    }


# Modelo Pydantic para la validación de datos al crear registros
class CreateRoomBlockRequest(BaseModel):
    block_id: int  # ID del bloque
    room_id: int  # ID del salón
    available: bool = True  # Disponible por defecto

    # Configuración para generar ejemplos JSON
    model_config = {
        "from_attributes": True,
        "arbitrary_types_allowed": True,
        "json_schema_extra": {
            "examples": [
                {"block_id": 1, "room_id": 2, "available": True},
            ]
        },
    }
