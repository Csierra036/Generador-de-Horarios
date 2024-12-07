from fastapi import HTTPException
from sqlalchemy.orm import Session
from src.database import CustomSQLAlchemyRepository
from src.models.time_block import TimeBlock, CreateTimeBlockRequest

class TimeBlockService:
    def __init__(self, db_session: Session):
        # Se instancia el repositorio con el modelo TimeBlock y la sesión actual
        self.repository = CustomSQLAlchemyRepository(db=db_session, model=TimeBlock)

    def get_all_time_blocks(self):
        """Obtiene todos los bloques de tiempo."""
        return self.repository.get_all()

    def get_time_block_by_id(self, time_block_id: int):
        """Obtiene un bloque de tiempo por ID."""
        time_block = self.repository.get(time_block_id)
        if not time_block:
            raise HTTPException(status_code=404, detail=f"TimeBlock with ID {time_block_id} not found")
        return time_block

    def create_time_block(self, time_block_data: CreateTimeBlockRequest):
        """Crea un nuevo bloque de tiempo."""
        return self.repository.create(time_block_data.model_dump())

    def update_time_block(self, time_block_id: int, time_block_data: CreateTimeBlockRequest):
        """Actualiza un bloque de tiempo existente."""
        time_block = self.repository.get(time_block_id)
        if not time_block:
            raise HTTPException(status_code=404, detail=f"TimeBlock with ID {time_block_id} not found")
        return self.repository.update(time_block, time_block_data.model_dump())

    def delete_time_block(self, time_block_id: int):
        """Elimina un bloque de tiempo por ID."""
        time_block = self.repository.get(time_block_id)
        if not time_block:
            raise HTTPException(status_code=404, detail=f"TimeBlock with ID {time_block_id} not found")
        return self.repository.delete(time_block_id)
