from sklearn.pipeline import Pipeline

from src.model.base import BasePipelineFactory
from src.model.encoders import (
    LabelBinarizer, 
    LabelEncoder, 
    OneHotEncoder
)
from src.model.scalers import StandardScaler


class TransformerFactory(BasePipelineFactory):
    def __init__(
        self,
        label_binarizer: LabelBinarizer = LabelBinarizer(),
        label_encoder: LabelEncoder = LabelEncoder(),
        one_hot_encoder: OneHotEncoder = OneHotEncoder(),
        standard_scaler: StandardScaler = StandardScaler(),
    ) -> None:
        self._label_binarizer = label_binarizer
        self._label_encoder = label_encoder
        self._one_hot_encoder = one_hot_encoder
        self._standard_scaler = standard_scaler
    
    def create_pipeline(self) -> Pipeline:
        steps = [(name, step) for name, step in self.__dict__.items()]
        return Pipeline(steps)
