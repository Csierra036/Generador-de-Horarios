from fastapi import APIRouter
from src.models.campus import CreateCampusRequest
from src.services.campus import CampusService

sede_service = CampusService

router = APIRouter(prefix="/sede", tags=["Sede"])


@router.post("")
async def create_sede(sede_request: CreateCampusRequest):
    return sede_service.create_sede(sede_request)


@router.get("")
async def get_all_sedes():
    return sede_service.get_all_sedes


@router.get("/{sede_id}")
async def get_sede_by_id(sede_id: int):
    return sede_service.get_sede_by_id(sede_id)


@router.put("/{sede_id}")
async def update_sede(sede_id: int, sede_request: CreateCampusRequest):
    return sede_service.update_sede(sede_id, sede_request)


@router.delete("/{sede_id}")
async def delete_sede(sede_id: int):
    return sede_service.delete_sede(sede_id)
