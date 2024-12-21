from fastapi import HTTPException
from src.database import DatabaseConnection, CustomSQLAlchemyRepository
from sqlalchemy.orm import Session
from src.salones.models.model import Salon, CreateSalonRequest

class SalonService:
    def __init__(self, db_session: Session):
        # Se instancia el repositorio con el modelo Teacher y la sesión actual
        self.repository = CustomSQLAlchemyRepository(db=db_session, model=Salon)

    def get_all_salones(self):
        """Obtiene todos los salones."""
        return self.repository.get_all()

    def get_salon_by_id(self, salon_id: int):
        """Obtiene un salon por ID."""
        salon = self.repository.get(salon_id)
        if not salon:
            raise HTTPException(status_code=404, detail=f"Salon with ID {salon_id} not found")
        return salon

    def create_salon(self, salon_data: CreateSalonRequest):
        """Crea un nuevo salon."""
        # Se asegura de convertir los datos de entrada en un diccionario compatible
        return self.repository.create(salon_data.dict())

    def update_salon(self, salon_id: int, salon_data: CreateSalonRequest):
        """Actualiza un salon existente."""
        salon = self.repository.get(salon_id)
        if not salon:
            raise HTTPException(status_code=404, detail=f"Salon with ID {salon_id} not found")
        return self.repository.update(salon, salon_data.dict())

    def delete_salon(self, salon_id: int):
        """Elimina un salon por ID."""
        salon = self.repository.get(salon_id)
        if not salon:
            raise HTTPException(status_code=404, detail=f"Salon with ID {salon_id} not found")
        return self.repository.delete(salon_id)