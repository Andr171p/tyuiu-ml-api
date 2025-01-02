from typing import Any, Self

from sklearn.pipeline import Pipeline

from src.ml.base import BaseClassifier
from src.ml.models import Classifier
from src.ml.pipeline.transformer import Transformer
from src.ml.utils import transform_data


class Model(Transformer, BaseClassifier):
    def __init__(self) -> None:
        super().__init__()
        self._classifier = Pipeline([
            ("transformer", self._transformer),
            ("classifier", Classifier())
        ])

    def fit(self, X: Any, y: Any) -> Self:
        self._classifier.fit()
        return self._classifier

    def predict_proba(self, X: Any) -> Any:
        data = transform_data(X)
        print(data)
        y = self._classifier.predict_proba(X=data)
        return y


model_pipeline = Model()


'''from src.api_v1.schemas.applicant import ApplicantSchema

a = ApplicantSchema(
    gender="М",
    gpa=4.2,
    priority=1,
    points=237,
    direction="08.05.00 Техника и технологии строительства"
)
b = ApplicantSchema(
    gender="М",
    gpa=4.2,
    priority=1,
    points=231,
    direction="09.03.01 Информатика и вычислительная техника"
)
ml = ModelPipeline()
x = [a.model_dump(), b.model_dump()]
d = ml.predict_proba(x)
print([float(i[1]) for i in d])'''
