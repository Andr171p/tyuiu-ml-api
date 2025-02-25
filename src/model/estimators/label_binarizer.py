from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pandas import DataFrame
    
from joblib import load
from sklearn.base import BaseEstimator, TransformerMixin

from src.config import settings


class LabelBinarizer(BaseEstimator, TransformerMixin):
    def __init__(self) -> None:
        self._binarizer = load(settings.models.lb)
        
    def fit(self, X: "DataFrame", y=None) -> "LabelBinarizer":
        self._binarizer.fit(X["gender"])
        return self
        
    def transform(self, X: "DataFrame", y=None) -> "DataFrame":
        gender_map = {"male": "М", "female": "Ж"}
        X["gender"] = X["gender"].apply(lambda x: gender_map[x])
        X["gender"] = self._binarizer.transform(X["gender"])
        return X
