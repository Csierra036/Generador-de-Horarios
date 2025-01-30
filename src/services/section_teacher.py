from fastapi import HTTPException
from src.database import DatabaseConnection, CustomSQLAlchemyRepository
from sqlalchemy.orm import Session
from src.models.section_teacher import (
    CreateSectionTeacherRequest,
)  # Importa los modelos correctos


class TeacherSectionService:  # Nombre más descriptivo
    def __init__(self, db_session: Session):
        self.repository = CustomSQLAlchemyRepository(
            db=db_session, model=CreateSectionTeacherRequest
        )  # Usa el modelo Teacher_Section

    def get_all_teacher_sections(self):
        """Obtiene todas las asignaciones de profesor-sección."""
        return self.repository.get_all()

    def get_teacher_section_by_id(self, teacher_section_id: int):
        """Obtiene una asignación profesor-sección por ID."""
        teacher_section = self.repository.get(teacher_section_id)
        if not teacher_section:
            raise HTTPException(
                status_code=404,
                detail=f"Teacher_Section with ID {teacher_section_id} not found",
            )
        return teacher_section

    def create_teacher_section(self, teacher_section_data: CreateSectionTeacherRequest):
        """Crea una nueva asignación profesor-sección."""
        return self.repository.create(teacher_section_data.dict())

    def update_teacher_section(
        self, teacher_section_id: int, teacher_section_data: CreateSectionTeacherRequest
    ):
        """Actualiza una asignación profesor-sección existente."""
        teacher_section = self.repository.get(teacher_section_id)
        if not teacher_section:
            raise HTTPException(
                status_code=404,
                detail=f"Teacher_Section with ID {teacher_section_id} not found",
            )
        return self.repository.update(teacher_section, teacher_section_data.dict())

    def delete_teacher_section(self, teacher_section_id: int):
        """Elimina una asignación profesor-sección por ID."""
        teacher_section = self.repository.get(teacher_section_id)
        if not teacher_section:
            raise HTTPException(
                status_code=404,
                detail=f"Teacher_Section with ID {teacher_section_id} not found",
            )
        return self.repository.delete(teacher_section_id)
