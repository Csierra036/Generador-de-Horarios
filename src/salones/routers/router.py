from fastapi import APIRouter, HTTPException
from typing import List
from src.salones.models.model import Salon, CreateSalonRequest
from src.salones.service.service import SalonService
salon_service = SalonService


router = APIRouter(
    prefix="/salon",
    tags=['Salones']
)



# Crear un nuevo salón

@router.post("", status_code=201)
def crear_salon(salon: CreateSalonRequest):

    respuesta = salon_service.create_salon(Salon)
    return respuesta

# Leer todos los salones
@router.get("")
def obtener_salones():
    respuesta = salon_service.get_all_salones()
    return respuesta

# Leer un salón por ID
@router.get("/{salon_id}")
def obtener_salon(salon_id: int):
    respuesta = salon_service.get_salon_by_id(salon_id)
    if respuesta:
        return respuesta
    raise HTTPException(status_code=404, detail="Salón no encontrado")

# Actualizar un salón
@router.put("/{salon_id}")
def actualizar_salon(salon_id: int, salon: CreateSalonRequest):
    respuesta = salon_service.update_salon(salon_id, salon)
    return respuesta

# Borrar un salón
@router.delete("/{salon_id}")
def borrar_salon(salon_id: int):
    respuesta = salon_service.delete_salon(salon_id)
    return respuesta
   
