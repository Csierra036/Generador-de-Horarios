from fastapi import APIRouter
from src.models.time_block import CreateTimeBlockRequest
from src.services.time_block import TimeBlockService
from sqlalchemy.orm import Session

# Instanciamos el servicio TimeBlock
time_block_service = TimeBlockService

# Creamos el router para los bloques de tiempo
router = APIRouter(
    prefix="/time-block",  # Definimos el prefijo para las rutas
    tags=["TimeBlock"]  # Etiqueta para organizar las rutas en la documentación de Swagger
)

# Ruta para crear un nuevo bloque de tiempo
@router.post("")
async def create_time_block(time_block_request: CreateTimeBlockRequest):
    """Crea un nuevo bloque de tiempo."""
    return time_block_service.create_time_block(time_block_request)

# Ruta para crear varios horarios segun el dia, semana, cantidad de bloques y comienzo de bloque
@router.get("")
async def create_all_time_block(num_time_block: int, start_num_time_block: int, day: int, week_id: int):
    """Crea todos los bloques de tiempo segun ciertos parametros"""
    return create_all_time_block(num_time_block, start_num_time_block, day, week_id)

# Ruta para obtener todos los bloques de tiempo
@router.get("")
async def get_all_time_blocks():
    """Obtiene todos los bloques de tiempo."""
    return time_block_service.get_all_time_blocks()

# Ruta para obtener un bloque de tiempo por su ID
@router.get("/{time_block_id}")
async def get_time_block_by_id(time_block_id: int):
    """Obtiene un bloque de tiempo por ID."""
    return time_block_service.get_time_block_by_id(time_block_id)

# Ruta para actualizar un bloque de tiempo por su ID
@router.put("/{time_block_id}")
async def update_time_block(time_block_id: int, time_block_request: CreateTimeBlockRequest):
    """Actualiza un bloque de tiempo existente."""
    return time_block_service.update_time_block(time_block_id, time_block_request)

# Ruta para eliminar un bloque de tiempo por su ID
@router.delete("/{time_block_id}")
async def delete_time_block(time_block_id: int):
    """Elimina un bloque de tiempo por ID."""
    return time_block_service.delete_time_block(time_block_id)
