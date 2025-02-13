from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from sklearn.pipeline import Pipeline

from src.model.estimators import (
    LabelBinarizer,
    LabelEncoder,
    OneHotEncoder,
    StandardScaler,
    Classifier
)
from src.model.pipelines import TransformerFactory, ModelFactory


def get_model_pipeline() -> "Pipeline":
    transformer_factory = TransformerFactory(
        label_binarizer=LabelBinarizer(),
        label_encoder=LabelEncoder(),
        one_hot_encoder=OneHotEncoder(),
        standard_scaler=StandardScaler()
    )
    transformer = transformer_factory.create_pipeline()
    model_factory = ModelFactory(
        transformer=transformer,
        classifier=Classifier()
        )
    model_pipeline = model_factory.create_pipeline()
    return model_pipeline
