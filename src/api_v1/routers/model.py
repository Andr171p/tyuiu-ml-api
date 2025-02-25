from fastapi import APIRouter, status
from fastapi.responses import JSONResponse

from dishka.integrations.fastapi import FromDishka, DishkaRoute

from src.schemas import ApplicantSchema, ApplicantsSchema
from src.services import ModelService


model_router = APIRouter(
    prefix="/api/v1/model",
    route_class=DishkaRoute,
    tags=["Binary classification model"]
)


@model_router.post(path="/applicant/")
async def predict_applicant_probability(
    applicant: ApplicantSchema,
    model_service: FromDishka[ModelService]
) -> JSONResponse:
    probability = model_service.predict_applicant_probability(applicant)
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={"probability": probability}
    )
    
    
@model_router.post(path="/applicants/")
async def predict_applicants_probabilities(
    applicants: ApplicantsSchema,
    model_service: FromDishka[ModelService]
) -> JSONResponse:
    probabilities = model_service.predict_applicants_probabilities(applicants.applicants)
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={"probabilities": probabilities}
    )
