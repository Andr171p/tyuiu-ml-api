from sklearn.pipeline import Pipeline

from src.model.base import BasePipelineFactory
from src.model.classifiers import Classifier


class ModelFactory(BasePipelineFactory):
    def __init__(
        self,
        transformer: Pipeline,
        classifier: Classifier
    ) -> None:
        self._transformer = transformer
        self._classifier = classifier
        
    def create_pipeline(self) -> Pipeline:
        steps = [(name, step) for name, step in self.__dict__.items()]
        return Pipeline(steps=steps)
