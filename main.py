from typing import Final, Literal

import logging
from pathlib import Path

import joblib
import pandas as pd
import uvicorn
from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from sklearn.base import ClassifierMixin
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import LabelBinarizer, LabelEncoder, OneHotEncoder, StandardScaler

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__)

BASE_DIR = Path(__file__).resolve().parent
FITTED_MODELS_DIR = BASE_DIR / "fitted_models"  # Директория с пред-обученными моделями

# Максимальная и минимальная сумма баллов ЕГЭ
MIN_POINTS, MAX_POINTS = 0, 310
# Средний балл аттестата
MIN_GPA, MAX_GPA = 3, 5
# Доступные года для предсказания
MIN_YEAR, MAX_YEAR = 2019, 2024

# Преобразование бинарных признаков в числовые данные (0 или 1)
label_binarizer: Final[LabelBinarizer] = joblib.load(FITTED_MODELS_DIR / "label_binarizer.joblib")
# Преобразование категориальных признаков в числовые данные
label_encoder: Final[LabelEncoder] = joblib.load(FITTED_MODELS_DIR / "label_encoder.joblib")
# Стандартизация всех данных таблицы
standard_scaler: Final[StandardScaler] = joblib.load(FITTED_MODELS_DIR / "standard_scaler.joblib")
# Качественные различия в количественные
one_hot_encoder: Final[OneHotEncoder] = joblib.load(FITTED_MODELS_DIR / "one_hot_encoder.joblib")
# Модель бинарной классификации
classifier: Final[ClassifierMixin] = joblib.load(FITTED_MODELS_DIR / "classifier.joblib")

pipeline = Pipeline([
    ("transform", Pipeline([
        ("label_binarize", label_binarizer),
        ("label_encode", label_encoder),
        ("one_hot_encode", one_hot_encoder),
        ("scale", standard_scaler)
    ])),
    ("classify", classifier)
])  # Пайплайн для предсказания вероятности поступления


class Applicant(BaseModel):
    year: int = Field(ge=MIN_YEAR, le=MAX_YEAR)
    gender: Literal["male", "female"]
    gpa: float = Field(ge=MIN_GPA, le=MAX_GPA)
    points: int = Field(ge=MIN_POINTS, le=MAX_POINTS)
    direction: str


def applicants_to_df(applicants: list[Applicant]) -> pd.DataFrame:
    """Преобразует массив абитуриентов в pandas DataFrame"""
    return pd.DataFrame([applicant.model_dump() for applicant in applicants])


app: Final[FastAPI] = FastAPI(title="ML модель для предсказания вероятности поступления")


@app.post(
    path="/api/v1/model/predict",
    status_code=status.HTTP_200_OK,
    response_model=list[float],
    summary="Получение предсказания ML модели"
)
def predict(applicants: list[Applicant]) -> list[float]:
    applicants_df = applicants_to_df(applicants)
    probabilities = pipeline.predict_proba(applicants_df)
    return [float(probability[-1]) for probability in probabilities]


@app.exception_handler(ValueError)
def handle_value_error(request: Request, exc) -> JSONResponse:  # noqa: ARG001
    logger.error(exc)
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST, content={"detail": str(exc)}
    )


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="info")  # noqa: S104
