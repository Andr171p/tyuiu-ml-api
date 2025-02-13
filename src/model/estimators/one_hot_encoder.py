from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pandas import DataFrame

from joblib import load
from sklearn.base import BaseEstimator, TransformerMixin

from src.config import settings


class OneHotEncoder(BaseEstimator, TransformerMixin):
    def __init__(self, column: str = "direction") -> None:
        self._encoder = load(settings.models.ohe)
        self.column = column

    def fit(self, X: "DataFrame", y=None) -> "OneHotEncoder":
        self._encoder.fit(X[self.column])
        return self

    def transform(self, X: "DataFrame", y=None) -> "DataFrame":
        encoded = self._encoder.transform(X[self.column].to_numpy().reshape(-1, 1))
        category_names = self._encoder.get_feature_names_out()
        for i, category_name in enumerate(category_names):
            X[f"{self.column}{category_name[2:]}"] = encoded[:, i]
        X.drop(columns=self.column, inplace=True)
        return X
