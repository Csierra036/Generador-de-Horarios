from fastapi import HTTPException
from src.database import DatabaseConnection, CustomSQLAlchemyRepository
from sqlalchemy.orm import Session
from src.models.classroom import Classroom, CreateClassroomRequest

class ClassroomService:
    def __init__(self, db_session: Session):
        # Se instancia el repositorio con el modelo Salon y la sesión actual
        self.repository = CustomSQLAlchemyRepository(db=db_session, model=Classroom)

    def get_all_Classroomes(self):
        """Obtiene todos los Classrooms."""
        return self.repository.get_all()

    def get_Classroom_by_id(self, Classroom_id: int):
        """Obtiene un Classroom por ID."""
        Classroom = self.repository.get(Classroom_id)
        if not Classroom:
            raise HTTPException(status_code=404, detail=f"Classroom with ID {Classroom_id} not found")
        return Classroom

    def create_Classroom(self, Classroom_data: CreateClassroomRequest):
        """Crea un nuevo Classroom."""
        # Se asegura de convertir los datos de entrada en un diccionario compatible
        return self.repository.create(Classroom_data.dict())

    def update_Classroom(self, Classroom_id: int, Classroom_data: CreateClassroomRequest):
        """Actualiza un Classroom existente."""
        Classroom = self.repository.get(Classroom_id)
        if not Classroom:
            raise HTTPException(status_code=404, detail=f"Classroom with ID {Classroom_id} not found")
        return self.repository.update(Classroom, Classroom_data.dict())

    def delete_Classroom(self, Classroom_id: int):
        """Elimina un Classroom por ID."""
        Classroom = self.repository.get(Classroom_id)
        if not Classroom:
            raise HTTPException(status_code=404, detail=f"Classroom with ID {Classroom_id} not found")
        return self.repository.delete(Classroom_id)