from fastapi import HTTPException
from sqlalchemy.orm import Session
from src.database import CustomSQLAlchemyRepository
from src.models.modality import Modality, CreateModalityRequest

# Servicio para manejar la lógica de negocio de "modality"
class ModalityService:
    def __init__(self, db_session: Session):
        # Repositorio personalizado para la tabla "modality"
        self.repository = CustomSQLAlchemyRepository(db=db_session, model=Modality)

    # Método para obtener todas las modalidades
    def get_all_modalities(self):
        return self.repository.get_all()

    # Método para obtener una modalidad por su ID
    def get_modality_by_id(self, modality_id: int):
        modality = self.repository.get(modality_id)
        if not modality:
            raise HTTPException(status_code=404, detail=f"Modality with ID {modality_id} not found")
        return modality

    # Método para crear una nueva modalidad
    def create_modality(self, modality_data: CreateModalityRequest):
        return self.repository.create(modality_data.dict())

    # Método para actualizar una modalidad existente
    def update_modality(self, modality_id: int, modality_data: CreateModalityRequest):
        modality = self.repository.get(modality_id)
        if not modality:
            raise HTTPException(status_code=404, detail=f"Modality with ID {modality_id} not found")
        return self.repository.update(modality, modality_data.dict())

    # Método para eliminar una modalidad
    def delete_modality(self, modality_id: int):
        modality = self.repository.get(modality_id)
        if not modality:
            raise HTTPException(status_code=404, detail=f"Modality with ID {modality_id} not found")
        return self.repository.delete(modality_id)
