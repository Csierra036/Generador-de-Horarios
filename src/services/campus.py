from fastapi import HTTPException
from src.database import CustomSQLAlchemyRepository
from sqlalchemy.orm import Session
from src.models.campus import Campus, CreateCampusRequest


class CampusService:
    def __init__(self, db_session: Session):
        # Se instancia el repositorio con el modelo Campus y la sesión actual
        self.repository = CustomSQLAlchemyRepository(db=db_session, model=Campus)

    def get_all_campuses(self):
        """Obtiene todas las Campuss."""
        return self.repository.get_all()

    def get_campus_by_id(self, Campus_id: int):
        """Obtiene una Campus por ID."""
        Campus = self.repository.get(Campus_id)
        if not Campus:
            raise HTTPException(
                status_code=404, detail=f"Campus with ID {Campus_id} not found"
            )
        return Campus

    def create_campus(self, Campus_data: CreateCampusRequest):
        """Crea una nueva Campus."""
        # Se asegura de convertir los datos de entrada en un diccionario compatible
        return self.repository.create(Campus_data.dict())

    def update_campus(self, Campus_id: int, Campus_data: CreateCampusRequest):
        """Actualiza una Campus existente."""
        Campus = self.repository.get(Campus_id)
        if not Campus:
            raise HTTPException(
                status_code=404, detail=f"Campus with ID {Campus_id} not found"
            )
        return self.repository.update(Campus, Campus_data.dict())

    def delete_campus(self, Campus_id: int):
        """Elimina una Campus por ID."""
        Campus = self.repository.get(Campus_id)
        if not Campus:
            raise HTTPException(
                status_code=404, detail=f"Campus with ID {Campus_id} not found"
            )
        return self.repository.delete(Campus_id)
