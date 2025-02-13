from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pandas import DataFrame

from joblib import load
from sklearn.base import BaseEstimator, TransformerMixin

from src.config import settings


class LabelEncoder(BaseEstimator, TransformerMixin):
    def __init__(self) -> None:
        self._encoder = load(settings.models.le)

    def fit(self, X: "DataFrame", y=None) -> "LabelEncoder":
        self._encoder.fit(X["year"])
        return self

    def transform(self, X: "DataFrame", y=None) -> "DataFrame":
        X["year"] = self._encoder.transform(X["year"])
        return X
