import logging

from src.tyuiu_classifier import create_fastapi_app


logging.basicConfig(level=logging.INFO)

app = create_fastapi_app()
