from typing import TYPE_CHECKING, Any, Union

if TYPE_CHECKING:
    from numpy import ndarray
    from pandas import DataFrame

from joblib import load
from sklearn.base import BaseEstimator, ClassifierMixin
from sklearn.utils.validation import check_is_fitted

from src.config import settings


class Classifier(BaseEstimator, ClassifierMixin):
    def __init__(self) -> None:
        self._model = load(settings.models.model)

    def fit(
            self,
            X: Union["DataFrame", "ndarray"],
            y: Union["DataFrame", "ndarray"]
    ) -> "Classifier":
        self._clf.fit(X, y)
        return self

    def predict(self, X: Union["DataFrame", "ndarray"]) -> Any:
        check_is_fitted(self, "_model")
        y_pred =  self._clf.predict(X)
        return y_pred

    def predict_proba(self, X: Union["DataFrame", "ndarray"]) -> Any:
        check_is_fitted(self, "_model")
        y_score = self._clf.predict_proba(X)
        return y_score
