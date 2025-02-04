from fastapi import APIRouter, Depends
from src.models.time_block import CreateTimeBlockRequest
from src.services.time_block import TimeBlockService
from sqlalchemy.orm import Session
from src.database import get_db


router = APIRouter(
    prefix="/time-block",
    tags=["TimeBlock"]
)


@router.post("")
async def create_time_block(time_block_request: CreateTimeBlockRequest, db: Session = Depends(get_db)):
    time_block_service = TimeBlockService(db)
    return time_block_service.create_time_block(time_block_request)


@router.get("")
async def create_all_time_block(num_time_block: int, start_num_time_block: int,
                                day: int, week_id: int , db: Session = Depends(get_db)):
    return create_all_time_block(num_time_block, start_num_time_block, day, week_id)


@router.get("")
async def get_all_time_blocks(db: Session = Depends(get_db)):
    time_block_service = TimeBlockService(db)
    return time_block_service.get_all_time_blocks()


@router.get("/{time_block_id}")
async def get_time_block_by_id(time_block_id: int, db: Session = Depends(get_db)):
    time_block_service = TimeBlockService(db)
    return time_block_service.get_time_block_by_id(time_block_id)


@router.put("/{time_block_id}")
async def update_time_block(time_block_id: int, time_block_request: CreateTimeBlockRequest,
                            db: Session = Depends(get_db)):
    
    time_block_service = TimeBlockService(db)
    return time_block_service.update_time_block(time_block_id, time_block_request)


@router.delete("/{time_block_id}")
async def delete_time_block(time_block_id: int, db: Session = Depends(get_db)):
    time_block_service = TimeBlockService(db)
    return time_block_service.delete_time_block(time_block_id)
