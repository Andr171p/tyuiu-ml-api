from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from dishka.integrations.fastapi import setup_dishka

from src.api_v1.container import container
from src.api_v1.routers import model_router
from src.config import settings


app = FastAPI()

app.include_router(model_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

setup_dishka(
    app=app,
    container=container
)
