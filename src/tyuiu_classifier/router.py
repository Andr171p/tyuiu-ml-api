from fastapi import APIRouter, status
from dishka.integrations.fastapi import FromDishka, DishkaRoute

from .classifier import BinaryClassifier
from .schemas import (
    Applicant,
    Applicants,
    ProbabilityResponse,
    ProbabilitiesResponse
)


classifier_router = APIRouter(
    prefix="/api/v1/classifier",
    tags=["Classifier"],
    route_class=DishkaRoute
)


@classifier_router.post(
    path="/predict",
    status_code=status.HTTP_200_OK,
    response_model=ProbabilityResponse
)
async def predict_applicant(
        applicant: Applicant,
        binary_classifier: FromDishka[BinaryClassifier]
) -> ProbabilityResponse:
    probability = binary_classifier.predict(applicant)
    return ProbabilityResponse(probability=probability)


@classifier_router.post(
    path="/predict-batch",
    status_code=status.HTTP_200_OK,
    response_model=ProbabilitiesResponse
)
async def predict_applicants(
        applicants: Applicants,
        binary_classifier: FromDishka[BinaryClassifier]
) -> ProbabilitiesResponse:
    probabilities = binary_classifier.predict_batch(applicants)
    return ProbabilitiesResponse(probabilities=probabilities)
