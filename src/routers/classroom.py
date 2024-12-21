from fastapi import APIRouter, HTTPException
from typing import List
from src.models.classroom import Classroom, CreateClassroomRequest
from src.services.classroom import ClassroomService


Classroom_service = ClassroomService

router = APIRouter(
    prefix="/Classroom",
    tags=['Classrooms']
)
# Crear un nuevo salón

@router.post("", status_code=201)
def crear_Classroom(Classroom: CreateClassroomRequest):
    respuesta = Classroom_service.create_Classroom(Classroom)
    return respuesta

# Leer todos los Classroomes
@router.get("")
def obtener_Classroomes():
    respuesta = Classroom_service.get_all_Classroomes()
    return respuesta

# Leer un salón por ID
@router.get("/{Classroom_id}")
def obtener_Classroom(Classroom_id: int):
    respuesta = Classroom_service.get_Classroom_by_id(Classroom_id)
    if respuesta:
        return respuesta
    raise HTTPException(status_code=404, detail="Salón no encontrado")

# Actualizar un salón
@router.put("/{Classroom_id}")
def actualizar_Classroom(Classroom_id: int, Classroom: CreateClassroomRequest):
    respuesta = Classroom_service.update_Classroom(Classroom_id, Classroom)
    return respuesta

# Borrar un salón
@router.delete("/{Classroom_id}")
def borrar_Classroom(Classroom_id: int):
    respuesta = Classroom_service.delete_Classroom(Classroom_id)
    return respuesta
