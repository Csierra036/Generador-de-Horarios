from fastapi import HTTPException
from src.database import DatabaseConnection, CustomSQLAlchemyRepository
from sqlalchemy.orm import Session
from models.career import Career, CreateCareerRequest

class CareerService:
    def __init__(self, db_session: Session):
        # Se instancia el repositorio con el modelo career y la sesión actual
        self.repository = CustomSQLAlchemyRepository(db=db_session, model=Career)

    def get_all_carrers(self):
        """Obtiene todos las carreras."""
        return self.repository.get_all()

    def get_career_by_id(self, career_id: int):
        """Obtiene una carrera por ID."""
        career = self.repository.get(career_id)
        if not career:
            raise HTTPException(status_code=404, detail=f"Career with ID {career_id} not found")
        return career

    def create_career(self, career_data: CreateCareerRequest):
        """Crea un nueva carrera."""
        # Se asegura de convertir los datos de entrada en un diccionario compatible
        return self.repository.create(career_data.dict())

    def update_career(self, career_id: int, career_data: CreateCareerRequest):
        """Actualiza una carrera existente."""
        career = self.repository.get(career_id)
        if not career:
            raise HTTPException(status_code=404, detail=f"Career with ID {career_id} not found")
        return self.repository.update(career, career_data.dict())

    def delete_career(self, career_id: int):
        """Elimina una carrera por ID."""
        career = self.repository.get(career_id)
        if not career:
            raise HTTPException(status_code=404, detail=f"Career with ID {career_id} not found")
        return self.repository.delete(career_id)