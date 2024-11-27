from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

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

    return app

app = start_app()

@app.get("", description="Welcome to UNEG", status_code=200)
def read_root():
    return {"message": "Hello, Admin!"}