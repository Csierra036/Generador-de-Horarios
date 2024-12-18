from fastapi import APIRouter
from src.models.modality import CreateModalityRequest
from src.services.modality import ModalityService

# Instancia del servicio de modalidades
modality_service = ModalityService

# Configuración del router para las rutas relacionadas con "modality"
router = APIRouter(
    prefix="/modality",
    tags=['Modality']
)

# Endpoint para crear una modalidad
@router.post("")
async def create_modality(modality_request: CreateModalityRequest):
    return modality_service.create_modality(modality_request)

# Endpoint para obtener todas las modalidades
@router.get("")
async def get_all_modalities():
    return modality_service.get_all_modalities()

# Endpoint para actualizar una modalidad
@router.put("")
async def update_modality(modality_id: int, modality_request: CreateModalityRequest):
    return modality_service.update_modality(modality_id, modality_request)

# Endpoint para eliminar una modalidad
@router.delete("")
async def delete_modality(modality_id: int):
    return modality_service.delete_modality(modality_id)
