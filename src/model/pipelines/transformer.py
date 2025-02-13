from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.model.estimators import (
        LabelBinarizer, 
        LabelEncoder, 
        OneHotEncoder,
        StandardScaler
    )

from sklearn.pipeline import Pipeline

from src.model.pipelines.base import BasePipelineFactory


class TransformerFactory(BasePipelineFactory):
    def __init__(
        self,
        label_binarizer: "LabelBinarizer",
        label_encoder: "LabelEncoder",
        one_hot_encoder: "OneHotEncoder",
        standard_scaler: "StandardScaler",
    ) -> None:
        self._label_binarizer = label_binarizer
        self._label_encoder = label_encoder
        self._one_hot_encoder = one_hot_encoder
        self._standard_scaler = standard_scaler
