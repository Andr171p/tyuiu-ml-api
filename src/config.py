import os
from pathlib import Path
from typing import Literal
from dotenv import load_dotenv
from pydantic_settings import BaseSettings


BASE_DIR: Path = Path(__file__).resolve().parent.parent

ENV_PATH: Path = BASE_DIR / ".env"

load_dotenv(ENV_PATH)


class ModelsSettings(BaseSettings):
    lb: Path = BASE_DIR / "models" / "label_binarizer.joblib"
    le: Path = BASE_DIR / "models" / "label_encoder.joblib"
    ohe: Path = BASE_DIR / "models" / "one_hot_encoder.joblib"
    scaler: Path = BASE_DIR / "models" / "standard_scaler.joblib"
    model: Path = BASE_DIR / "models" / "model.joblib"


class APISettings(BaseSettings):
    name: str = "Classifier API"
    prefix: str = "/api/v1"


class Settings(BaseSettings):
    api: APISettings = APISettings()
    models: ModelsSettings = ModelsSettings()


settings = Settings()
