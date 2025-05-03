from pathlib import Path
from typing import Any, Union

import numpy as np
import pandas as pd
from joblib import load
from sklearn.utils.validation import check_is_fitted
from sklearn.base import BaseEstimator, TransformerMixin, ClassifierMixin

from .constants import GENDER_MAPPING


class LabelBinarizer(BaseEstimator, TransformerMixin):
    def __init__(self, file_path: Path) -> None:
        self._estimator = load(file_path)

    def fit(self, X: pd.DataFrame) -> "LabelBinarizer":
        self._estimator.fit(X["gender"])
        return self

    def transform(self, X: pd.DataFrame) -> pd.DataFrame:
        X["gender"] = X["gender"].apply(lambda x: GENDER_MAPPING[x])
        X["gender"] = self._estimator.transform(X["gender"])
        return X


class LabelEncoder(BaseEstimator, TransformerMixin):
    def __init__(self, file_path: Path) -> None:
        self._estimator = load(file_path)

    def fit(self, X: pd.DataFrame) -> "LabelEncoder":
        self._estimator.fit(X["year"])
        return self

    def transform(self, X: pd.DataFrame) -> pd.DataFrame:
        X["year"] = self._estimator.transform(X["year"])
        return X


class OneHotEncoder(BaseEstimator, TransformerMixin):
    def __init__(self, file_path: Path) -> None:
        self._estimator = load(file_path)

    def fit(self, X: pd.DataFrame) -> "OneHotEncoder":
        self._estimator.fit(X["direction"])
        return self

    def transform(self, X: pd.DataFrame) -> pd.DataFrame:
        encoded = self._estimator.transform(X["direction"].to_numpy().reshape(-1, 1))
        category_names = self._estimator.get_feature_names_out()
        for i, category_name in enumerate(category_names):
            X[f"direction{category_name[2:]}"] = encoded[:, i]
        X.drop(columns="direction", inplace=True)
        return X


class StandardScaler(BaseEstimator, TransformerMixin):
    def __init__(self, file_path: Path) -> None:
        self._estimator = load(file_path)

    def fit(self, X: Union[pd.DataFrame, np.ndarray]) -> "StandardScaler":
        self._estimator.fit(X)
        return self

    def transform(self, X: Union[pd.DataFrame, np.ndarray]) -> np.ndarray:
        scaled = self._estimator.transform(X)
        return scaled


class Classifier(BaseEstimator, ClassifierMixin):
    def __init__(self, file_path: Path) -> None:
        self._model = load(file_path)

    def fit(self,
            X: Union[pd.DataFrame, np.ndarray],
            y: Union[pd.DataFrame, np.ndarray]
    ) -> "Classifier":
        self._model.fit(X, y)
        return self

    def predict(self, X: Union[pd.DataFrame, np.ndarray]) -> Any:
        check_is_fitted(self, "_model")
        y_pred =  self._model.predict(X)
        return y_pred

    def predict_proba(self, X: Union[pd.DataFrame, np.ndarray]) -> Any:
        check_is_fitted(self, "_model")
        y_score = self._model.predict_proba(X)
        return y_score

