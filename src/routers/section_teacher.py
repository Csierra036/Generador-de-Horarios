from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.database import get_db
from src.models.teacher import CreateTeacherRequest
from src.services.section_teacher import SectionTeacherService

router = APIRouter(
    prefix="/teacher_section",  # Prefijo más descriptivo
    tags=["Teacher Section"],  # Tag actualizado
)


@router.post("")
async def create_teacher_section(
    teacher_section_request: CreateTeacherRequest, db: Session = Depends(get_db)
):
    teacher_section_service = SectionTeacherService(
        db
    )  # Instancia el servicio con la sesión de la BD
    return teacher_section_service.create_teacher_section(teacher_section_request)


@router.get("")
async def get_all_teacher_sections(db: Session = Depends(get_db)):
    teacher_section_service = SectionTeacherService(db)
    return teacher_section_service.get_all_teacher_sections()


@router.get("/{teacher_section_id}")  # Ruta para obtener por ID
async def get_teacher_section_by_id(
    teacher_section_id: int, db: Session = Depends(get_db)
):
    teacher_section_service = SectionTeacherService(db)
    return teacher_section_service.get_teacher_section_by_id(teacher_section_id)


@router.put("/{teacher_section_id}")  # Ruta para actualizar por ID
async def update_teacher_section(
    teacher_section_id: int,
    teacher_section_request: CreateTeacherRequest,
    db: Session = Depends(get_db),
):
    teacher_section_service = SectionTeacherService(db)
    return teacher_section_service.update_teacher_section(
        teacher_section_id, teacher_section_request
    )


@router.delete("/{teacher_section_id}")  # Ruta para eliminar por ID
async def delete_teacher_section(
    teacher_section_id: int, db: Session = Depends(get_db)
):
    teacher_section_service = SectionTeacherService(db)
    return teacher_section_service.delete_teacher_section(teacher_section_id)
