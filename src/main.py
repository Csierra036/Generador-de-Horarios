from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.routers.career import router as career_router
from src.routers.campus import router as campus_router
from src.routers.classroom import router as classroom_router
from src.routers.course import router as course_router
from src.routers.modality import router as modality_router
from src.routers.section import router as section_router
from src.routers.teacher import router as teacher_router
from src.routers.time_block import router as time_block_router
import psycopg2

def start_app() -> FastAPI:

    app = FastAPI(
        title = "Generador-Horarios",
        description = "API diseñada para gestionar generador de horarios",
        version = "v0.0.1",
        debug = True
    )

    origins = ["*"]
    app.add_middleware(
        CORSMiddleware,
        allow_origins = origins,
        allow_credentials = True,
        allow_methods = ["*"],
        allow_headers = ["*"],
    )
    app.include_router(career_router)
    app.include_router(campus_router)
    app.include_router(classroom_router)
    app.include_router(course_router)
    app.include_router(section_router)
    app.include_router(modality_router)
    app.include_router(career_router)
    app.include_router(campus_router)
    app.include_router(classroom_router)
    app.include_router(course_router)
    app.include_router(section_router)
    app.include_router(modality_router)
    app.include_router(teacher_router)
    app.include_router(time_block_router)
    return app

app = start_app()

