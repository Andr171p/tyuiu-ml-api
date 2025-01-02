import os
from pathlib import Path
from typing import Literal
from dotenv import load_dotenv
from pydantic_settings import BaseSettings


BASE_DIR: Path = Path(__file__).resolve().parent.parent

ENV_PATH: Path = BASE_DIR / ".env"

load_dotenv(ENV_PATH)


class ModelSettings(BaseSettings):
    ohe: Path = BASE_DIR / "trained_models" / "one-hot-encoder.joblib"
    scaler: Path = BASE_DIR / "trained_models" / "standard-scaler.joblib"
    label: Path = BASE_DIR / "trained_models" / "label-encoder.joblib"
    clf: Path = BASE_DIR / "trained_models" / "classifier.joblib"

    class FeaturesSettings(BaseSettings):
        label_feature: str = "gender"
        ohe_feature: str = "direction"

    features: FeaturesSettings = FeaturesSettings()


class S3Settings(BaseSettings):
    access_key: str = os.getenv("S3_ACCESS_KEY")
    secret_key: str = os.getenv("S3_SECRET_KEY")
    endpoint_url: str = os.getenv("S3_ENDPOINT_URL")

    class BucketSettings(BaseSettings):
        name: Literal["pipeline"] = "pipeline"

        clf_file: Literal["classifier"] = "classifier"

    bucket: BucketSettings = BucketSettings()


class APISettings(BaseSettings):
    name: str = "Classifier API"
    prefix: str = "/api/v1"


class Settings(BaseSettings):
    s3: S3Settings = S3Settings()
    ml: ModelSettings = ModelSettings()
    api_v1: APISettings = APISettings()


settings = Settings()
