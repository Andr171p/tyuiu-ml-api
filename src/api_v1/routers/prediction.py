from fastapi import APIRouter, status
from fastapi.responses import JSONResponse

from src.repository.prediction import PredictionRepository
from src.schemas.applicant import (
    ApplicantSchema,
    ApplicantsSchema,
    ApplicantResponse,
    ApplicantsResponse
)
from src.config import settings


prediction_router = APIRouter(
    prefix=f"{settings.api_v1.prefix}/classifier",
    tags=["Probability prediction"]
)


@prediction_router.post(path="/predict/applicant/", response_model=ApplicantResponse)
async def predict_applicant(applicant: ApplicantSchema) -> JSONResponse:
    prediction = PredictionRepository.predict_applicant(applicant)
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            "data": {
                "status": "ok",
                "prediction": prediction
            }
        }
    )


@prediction_router.post(path="/predict/applicants/", response_model=ApplicantsResponse)
async def predict_applicants(applicants: ApplicantsSchema) -> JSONResponse:
    predictions = PredictionRepository.predict_applicants(applicants)
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            "status": "ok",
            "predictions": predictions
        }
    )
