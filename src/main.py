from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.routers.teacher import router as teacher_router
#from src.sede.router.router import router as sede_router
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
    
    #app.include_router(teacher_router)
    #app.include_router(sede_router)  # Agregado el router de sede

    return app

#app = start_app()

