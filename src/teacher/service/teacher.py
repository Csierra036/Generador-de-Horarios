from fastapi import HTTPException
from database import DatabaseConnection, CustomSQLAlchemyRepository
from sqlalchemy.orm import Session
from src.teacher.model.teacher import Teacher, CreateTeacherRequest

class TeacherService:
    def __init__(self, db_session: Session):
        # Se instancia el repositorio con el modelo Teacher y la sesión actual
        self.repository = CustomSQLAlchemyRepository(db=db_session, model=Teacher)

    def get_all_teachers(self):
        """Obtiene todos los profesores."""
        return self.repository.get_all()

    def get_teacher_by_id(self, teacher_id: int):
        """Obtiene un profesor por ID."""
        teacher = self.repository.get(teacher_id)
        if not teacher:
            raise HTTPException(status_code=404, detail=f"Teacher with ID {teacher_id} not found")
        return teacher

    def create_teacher(self, teacher_data: CreateTeacherRequest):
        """Crea un nuevo profesor."""
        # Se asegura de convertir los datos de entrada en un diccionario compatible
        return self.repository.create(teacher_data.dict())

    def update_teacher(self, teacher_id: int, teacher_data: CreateTeacherRequest):
        """Actualiza un profesor existente."""
        teacher = self.repository.get(teacher_id)
        if not teacher:
            raise HTTPException(status_code=404, detail=f"Teacher with ID {teacher_id} not found")
        return self.repository.update(teacher, teacher_data.dict())

    def delete_teacher(self, teacher_id: int):
        """Elimina un profesor por ID."""
        teacher = self.repository.get(teacher_id)
        if not teacher:
            raise HTTPException(status_code=404, detail=f"Teacher with ID {teacher_id} not found")
        return self.repository.delete(teacher_id)