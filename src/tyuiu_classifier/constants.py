from typing import Literal

from pathlib import Path


# Директория проекта:
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Пред обученные модели и енкодеры:
LABEL_BINARIZER_PATH = BASE_DIR / "fitted_models" / "label_binarizer.joblib"
LABEL_ENCODER_PATH = BASE_DIR / "fitted_models" / "label_encoder.joblib"
ONE_HOT_ENCODER_PATH = BASE_DIR / "fitted_models" / "one_hot_encoder.joblib"
STANDARD_SCALER_PATH = BASE_DIR / "fitted_models" / "standard_scaler.joblib"
CLASSIFIER_PATH = BASE_DIR / "fitted_models" / "classifier.joblib"


MIN_POINTS = 0
MAX_POINTS = 310

MIN_GPA = 3
MAX_GPA = 5

AVAILABLE_YEARS = Literal[
    2019,
    2020,
    2021,
    2022,
    2023,
    2024
]

GENDER_MAPPING = {
    "male": "М",
    "female": "Ж"
}
