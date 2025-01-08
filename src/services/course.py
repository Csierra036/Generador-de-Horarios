from fastapi import HTTPException
from src.database import CustomSQLAlchemyRepository
from sqlalchemy.orm import Session
from src.models.course import Course, CreateCourseRequest

class CourseService:
    def __init__(self, db_session: Session):
        # Se instancia el repositorio con el modelo Course y la sesión actual
        self.repository = CustomSQLAlchemyRepository(db=db_session, model=Course)

    def get_all_courses(self):
        """Obtiene todas los cursos."""
        return self.repository.get_all()

    def get_course_by_id(self, Course_id: int):
        """Obtiene un curso por ID."""
        Course = self.repository.get(Course_id)
        if not Course:
            raise HTTPException(status_code=404, detail=f"Course with ID {Course_id} not found")
        return Course

    def create_course(self, Course_data: CreateCourseRequest):
        """Crea un curso"""
        # Se asegura de convertir los datos de entrada en un diccionario compatible
        return self.repository.create(Course_data.dict())

    def update_course(self, Course_id: int, Course_data: CreateCourseRequest):
        """Actualiza un curso existente."""
        Course = self.repository.get(Course_id)
        if not Course:
            raise HTTPException(status_code=404, detail=f"Course with ID {Course_id} not found")
        return self.repository.update(Course, Course_data.dict())

    def delete_course(self, Course_id: int):
        """Elimina un curso por ID."""
        Course = self.repository.get(Course_id)
        if not Course:
            raise HTTPException(status_code=404, detail=f"Course with ID {Course_id} not found")
        return self.repository.delete(Course_id)
