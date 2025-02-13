from sklearn.pipeline import Pipeline

from src.model.pipelines.base import BasePipelineFactory
from src.model.estimators import Classifier


class ModelFactory(BasePipelineFactory):
    def __init__(
        self,
        transformer: Pipeline,
        classifier: Classifier
    ) -> None:
        self._transformer = transformer
        self._classifier = classifier
