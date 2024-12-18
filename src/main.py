from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.routers.teacher import router as teacher_router
from src.routers.time_block import router as time_block_router
from src.routers import teacher


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
    app.include_router(teacher_router)
    app.include_router(time_block_router)  # Agregado el router de sede

    return app

app = start_app()

