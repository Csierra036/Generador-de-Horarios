from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from src.teacher.router.router import router as teacher_router

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
    return app

app = start_app()
