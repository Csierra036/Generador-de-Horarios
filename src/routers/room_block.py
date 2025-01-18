from fastapi import APIRouter
from src.models.room_block import CreateRoomBlockRequest
from src.services.room_block import RoomBlockService

# Instancia del servicio para room_block
room_block_service = RoomBlockService

# Configuración del router
router = APIRouter(
    prefix="/room_block",
    tags=['RoomBlock']
)

# Endpoint para crear un registro en "room_block"
@router.post("")
async def create_room_block(room_block_request: CreateRoomBlockRequest):
    return room_block_service.create_room_block(room_block_request)

# Endpoint para obtener todos los registros
@router.get("")
async def get_all_room_blocks():
    return room_block_service.get_all_room_blocks()

# Endpoint para actualizar un registro existente
@router.put("")
async def update_room_block(room_block_id: int, room_block_request: CreateRoomBlockRequest):
    return room_block_service.update_room_block(room_block_id, room_block_request)

# Endpoint para eliminar un registro
@router.delete("")
async def delete_room_block(room_block_id: int):
    return room_block_service.delete_room_block(room_block_id)
