from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from sklearn.pipeline import Pipeline

from abc import ABC, abstractmethod


class BasePipelineFactory(ABC):
    @abstractmethod
    def create_pipeline(self) -> "Pipeline":
        raise NotImplemented
