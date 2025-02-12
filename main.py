from src.model.transformer import TransformerFactory
from src.model.model import ModelFactory
from src.model.classifiers import Classifier


transformer_factory = TransformerFactory()
transformer = transformer_factory.create_pipeline()
model_factory = ModelFactory(
    transformer=transformer,
    classifier=Classifier()
)
model = model_factory.create_pipeline()
print(model)