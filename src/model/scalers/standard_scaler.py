from typing import TYPE_CHECKING, Union

if TYPE_CHECKING:
    from numpy import ndarray
    from pandas import DataFrame

from joblib import load
from sklearn.base import BaseEstimator, TransformerMixin

from src.config import settings


class StandardScaler(BaseEstimator, TransformerMixin):
    def __init__(self) -> None:
        self._scaler = load(settings.models.scaler)

    def fit(self, X: Union["DataFrame", "ndarray"], y=None) -> "StandardScaler":
        self._scaler.fit(X)
        return self

    def transform(self, X: Union["DataFrame", "ndarray"]) -> "ndarray":
        scaled = self._scaler.transform(X)
        return scaled
