from fastapi import HTTPException
from src.database import CustomSQLAlchemyRepository
from sqlalchemy.orm import Session
from src.models.campus import Sede, CreateSedeRequest

class SedeService:
    def __init__(self, db_session: Session):
        # Se instancia el repositorio con el modelo Sede y la sesión actual
        self.repository = CustomSQLAlchemyRepository(db=db_session, model=Sede)

    def get_all_sedes(self):
        """Obtiene todas las sedes."""
        return self.repository.get_all()

    def get_sede_by_id(self, sede_id: int):
        """Obtiene una sede por ID."""
        sede = self.repository.get(sede_id)
        if not sede:
            raise HTTPException(status_code=404, detail=f"Sede with ID {sede_id} not found")
        return sede

    def create_sede(self, sede_data: CreateSedeRequest):
        """Crea una nueva sede."""
        # Se asegura de convertir los datos de entrada en un diccionario compatible
        return self.repository.create(sede_data.dict())

    def update_sede(self, sede_id: int, sede_data: CreateSedeRequest):
        """Actualiza una sede existente."""
        sede = self.repository.get(sede_id)
        if not sede:
            raise HTTPException(status_code=404, detail=f"Sede with ID {sede_id} not found")
        return self.repository.update(sede, sede_data.dict())

    def delete_sede(self, sede_id: int):
        """Elimina una sede por ID."""
        sede = self.repository.get(sede_id)
        if not sede:
            raise HTTPException(status_code=404, detail=f"Sede with ID {sede_id} not found")
        return self.repository.delete(sede_id)
