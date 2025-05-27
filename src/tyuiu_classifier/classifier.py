from sklearn.pipeline import Pipeline

from .schemas import Applicant, Applicants
from .estimators import (
    LabelBinarizer,
    LabelEncoder,
    OneHotEncoder,
    StandardScaler,
    Classifier
)


class BinaryClassifier:
    def __init__(
            self,
            label_binarizer: LabelBinarizer,
            label_encoder: LabelEncoder,
            one_hot_encoder: OneHotEncoder,
            standard_scaler: StandardScaler,
            classifier: Classifier
    ) -> None:
        transformer = Pipeline([
            ("label_binarize", label_binarizer),
            ("label_encode", label_encoder),
            ("one_hot_encode", one_hot_encoder),
            ("scale", standard_scaler)
        ])
        classifier = [
            ("transform", transformer),
            ("predict", classifier)
        ]
        self.pipeline = Pipeline(classifier)

    def predict(self, applicant: Applicant) -> float:
        df = applicant.to_df()
        proba = self.pipeline.predict_proba(df)
        return float(proba[0][-1])

    def predict_batch(self, applicants: Applicants) -> list[float]:
        df = applicants.to_df()
        probas = self.pipeline.predict_proba(df)
        return [float(proba[-1]) for proba in probas]
