from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from sklearn.pipeline import Pipeline

from src.model.model_provider import get_model_pipeline


class Model:
    def __init__(self, pipeline: "Pipeline" = get_model_pipeline()) -> None:
        self._pipeline = pipeline
    
    def predict(self, X: Any) -> Any:
        prediction = self._pipeline.predict(X)
        return prediction
    
    def predict_probability(self, X: Any) -> Any:
        probability = self._pipeline.predict_proba(X)
        return probability
