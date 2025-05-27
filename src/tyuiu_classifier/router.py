from fastapi import APIRouter, status

from dishka.integrations.fastapi import FromDishka, DishkaRoute

from .classifier import BinaryClassifier
from .schemas import Applicant, Applicants, Prediction


classifier_router = APIRouter(
    prefix="/api/v1/classifier",
    tags=["Classifier"],
    route_class=DishkaRoute
)


@classifier_router.post(
    path="/predict",
    status_code=status.HTTP_200_OK,
    response_model=Prediction
)
async def predict_applicant(
        applicant: Applicant,
        binary_classifier: FromDishka[BinaryClassifier]
) -> Prediction:
    probability = binary_classifier.predict(applicant)
    return Prediction(direction=applicant.direction, probability=probability)


@classifier_router.post(
    path="/predict-batch",
    status_code=status.HTTP_200_OK,
    response_model=list[Prediction]
)
async def predict_applicants(
        applicants: Applicants,
        binary_classifier: FromDishka[BinaryClassifier]
) -> list[Prediction]:
    probabilities = binary_classifier.predict_batch(applicants)
    return [
        Prediction(direction=applicant.direction, probability=probability)
        for applicant, probability in zip(applicants.applicants, probabilities)
    ]
