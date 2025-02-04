from fastapi import APIRouter, HTTPException, Depends
from typing import List
from src.models.classroom import Classroom, CreateClassroomRequest
from src.services.classroom import ClassroomService
from sqlalchemy.orm import Session
from src.database import get_db


router = APIRouter(
    prefix="/Classroom",
    tags=['Classrooms']
)


@router.post("", status_code=201)
def crear_Classroom(Classroom: CreateClassroomRequest, db: Session = Depends(get_db)):
    Classroom_service = ClassroomService(db)
    respuesta = Classroom_service.create_Classroom(Classroom)
    return respuesta


@router.get("")
def obtener_Classroomes(db: Session = Depends(get_db)):
    Classroom_service = ClassroomService(db)
    respuesta = Classroom_service.get_all_Classroomes()
    return respuesta


@router.get("/{Classroom_id}")
def obtener_Classroom(Classroom_id: int, db: Session = Depends(get_db)):
    Classroom_service = ClassroomService(db)
    respuesta = Classroom_service.get_Classroom_by_id(Classroom_id)
    if respuesta:
        return respuesta
    raise HTTPException(status_code=404, detail="Salón no encontrado")


@router.put("/{Classroom_id}")
def actualizar_Classroom(Classroom_id: int, Classroom: CreateClassroomRequest, db: Session = Depends(get_db)):
    Classroom_service = ClassroomService(db)
    respuesta = Classroom_service.update_Classroom(Classroom_id, Classroom)
    return respuesta


@router.delete("/{Classroom_id}")
def borrar_Classroom(Classroom_id: int, db: Session = Depends(get_db)):
    Classroom_service = ClassroomService(db)
    respuesta = Classroom_service.delete_Classroom(Classroom_id)
    return respuesta
