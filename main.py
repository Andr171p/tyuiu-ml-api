from src.model.pipelines import TransformerPipelineFactory
from src.model.pipelines import ModelPipelineFactory
from src.model.classifiers import Classifier


transformer_factory = TransformerPipelineFactory()
transformer = transformer_factory.create_pipeline()
model_factory = ModelPipelineFactory(
    transformer=transformer,
    classifier=Classifier()
)
model = model_factory.create_pipeline()
print(model)