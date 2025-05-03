from pathlib import Path
from pydantic_settings import BaseSettings


BASE_DIR = Path(__file__).resolve().parent.parent.parent


class Settings(BaseSettings):
    LABEL_BINARIZER_PATH: Path = BASE_DIR / "fitted_models" / "label_binarizer.joblib"
    LABEL_ENCODER_PATH: Path = BASE_DIR / "fitted_models" / "label_encoder.joblib"
    ONE_HOT_ENCODER_PATH: Path = BASE_DIR / "fitted_models" / "one_hot_encoder.joblib"
    STANDARD_SCALER_PATH: Path = BASE_DIR / "fitted_models" / "standard_scaler.joblib"
    CLASSIFIER_PATH: Path = BASE_DIR / "fitted_models" / "classifier.joblib"
