from fastapi import HTTPException
from src.database import DatabaseConnection, CustomSQLAlchemyRepository
from sqlalchemy.orm import Session
from src.models.section_weeks import SectionWeeks, CreateSectionWeeksRequest

class SectionWeeksService:
    def __init__(self, db_session: Session):
        # Se instancia el repositorio con el modelo SectionWeeks y la sesión actual
        self.repository = CustomSQLAlchemyRepository(db=db_session, model=SectionWeeks)
    
    def get_all_section_weeks(self):
        return self.repository.get_all()
    
    def get_section_week(self, section_id: int, week_id: int):
        section_week = self.repository.filter_by(
            section_id=section_id,
            week_id=week_id
        ).first()
        if not section_week:
            raise HTTPException(
                status_code=404,
                detail=f"Relation with section ID {section_id} and week ID {week_id} not found"
            )
        return section_week
    
    def get_weeks_by_section(self, section_id: int):
        section_weeks = self.repository.filter_by(section_id=section_id).all()
        if not section_weeks:
            raise HTTPException(
                status_code=404,
                detail=f"No weeks found for section ID {section_id}"
            )
        return section_weeks
    
    def get_sections_by_week(self, week_id: int):
        section_weeks = self.repository.filter_by(week_id=week_id).all()
        if not section_weeks:
            raise HTTPException(
                status_code=404,
                detail=f"No sections found for week ID {week_id}"
            )
        return section_weeks
    
    def create_section_week(self, section_week_data: CreateSectionWeeksRequest):
        # Verificar si la relación ya existe
        existing = self.repository.filter_by(
            section_id=section_week_data.section_id,
            week_id=section_week_data.week_id
        ).first()
        
        if existing:
            raise HTTPException(
                status_code=400,
                detail="This section-week relation already exists"
            )
        
        # Se convierte los datos de entrada en un diccionario compatible
        return self.repository.create(section_week_data.dict())
    
    def update_section_week(self, section_id: int, week_id: int, section_week_data: CreateSectionWeeksRequest):
        section_week = self.get_section_week(section_id, week_id)
        return self.repository.update(section_week, section_week_data.dict())
    
    def delete_section_week(self, section_id: int, week_id: int):
        section_week = self.get_section_week(section_id, week_id)
        return self.repository.delete(section_week.id)