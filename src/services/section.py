from fastapi import HTTPException
from src.database import DatabaseConnection, CustomSQLAlchemyRepository
from sqlalchemy.orm import Session
from models.section import Section, CreateSectionRequest

class SectionService:
    def __init__(self, db_session: Session):
        # Se instancia el repositorio con el modelo Section y la sesión actual
        self.repository = CustomSQLAlchemyRepository(db=db_session, model=Section)
    
    def get_all_sections(self):
        return self.repository.get_all()
    
    def get_section_by_id(self, section_id: int):
        section = self.repository.get(section_id)
        if not section:
            raise HTTPException(status_code=404, detail=f"Section with ID {section_id} not found")
        return section
    
    def create_section(self, section_data: CreateSectionRequest):
        # Se asegura de convertir los datos de entrada en un diccionario compatible
        return self.repository.create(section_data.dict())

    def update_section(self, section_id: int, section_data: CreateSectionRequest):
        section = self.repository.get(section_id)
        if not section:
            raise HTTPException(status_code=404, detail=f"Section with ID {section_id} not found")
        return self.repository.update(section, section_data.dict())

    def delete_section(self, section_id: int):
        section = self.repository.get(section_id)
        if not section:
            raise HTTPException(status_code=404, detail=f"Section with ID {section_id} not found")
        return self.repository.delete(section_id)
