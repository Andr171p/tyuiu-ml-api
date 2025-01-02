from typing import List

from src.ml.pipeline import Model
from src.schemas.applicant import (
    ApplicantSchema,
    ApplicantsSchema
)


class PredictionRepository:
    model = Model()

    @classmethod
    def predict_applicant(cls, applicant: ApplicantSchema) -> float:
        prediction = cls.model.predict_proba(applicant.model_dump())
        return float(prediction[0][1])

    @classmethod
    def predict_applicants(cls, applicants: ApplicantsSchema) -> List[float]:
        predictions = cls.model.predict_proba(applicants.model_dump()["applicants"])
        return [
            prediction[1]
            for prediction in predictions
        ]
