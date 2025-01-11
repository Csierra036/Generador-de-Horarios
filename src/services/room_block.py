from fastapi import HTTPException
from src.database import CustomSQLAlchemyRepository
from sqlalchemy.orm import Session
from src.models.room_block import RoomBlock, CreateRoomBlockRequest

# Servicio para manejar la lógica de negocio de "room_block"
class RoomBlockService:
    def __init__(self, db_session: Session):
        # Repositorio personalizado con el modelo RoomBlock
        self.repository = CustomSQLAlchemyRepository(db=db_session, model=RoomBlock)

    # Obtener todos los registros
    def get_all_room_blocks(self):
        return self.repository.get_all()

    # Obtener un registro por su ID
    def get_room_block_by_id(self, room_block_id: int):
        room_block = self.repository.get(room_block_id)
        if not room_block:
            raise HTTPException(status_code=404, detail=f"RoomBlock with ID {room_block_id} not found")
        return room_block

    # Crear un nuevo registro
    def create_room_block(self, room_block_data: CreateRoomBlockRequest):
        return self.repository.create(room_block_data.dict())

    # Actualizar un registro existente
    def update_room_block(self, room_block_id: int, room_block_data: CreateRoomBlockRequest):
        room_block = self.repository.get(room_block_id)
        if not room_block:
            raise HTTPException(status_code=404, detail=f"RoomBlock with ID {room_block_id} not found")
        return self.repository.update(room_block, room_block_data.dict())

    # Eliminar un registro
    def delete_room_block(self, room_block_id: int):
        room_block = self.repository.get(room_block_id)
        if not room_block:
            raise HTTPException(status_code=404, detail=f"RoomBlock with ID {room_block_id} not found")
        return self.repository.delete(room_block_id)
