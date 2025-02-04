from fastapi import APIRouter, Depends
from src.models.room_block import CreateRoomBlockRequest
from src.services.room_block import RoomBlockService
from sqlalchemy.orm import Session
from src.database import get_db


router = APIRouter(
    prefix="/room_block",
    tags=['RoomBlock']
)


@router.post("")
async def create_room_block(room_block_request: CreateRoomBlockRequest, db: Session = Depends(get_db)):
    room_block_service = RoomBlockService(db)
    return room_block_service.create_room_block(room_block_request)


@router.get("")
async def get_all_room_blocks(db: Session = Depends(get_db)):
    room_block_service = RoomBlockService(db)
    return room_block_service.get_all_room_blocks()


@router.put("")
async def update_room_block(room_block_id: int, room_block_request: CreateRoomBlockRequest, db: Session = Depends(get_db)):
    room_block_service = RoomBlockService(db)
    return room_block_service.update_room_block(room_block_id, room_block_request)


@router.delete("")
async def delete_room_block(room_block_id: int, db: Session = Depends(get_db)):
    room_block_service = RoomBlockService(db)
    return room_block_service.delete_room_block(room_block_id)
