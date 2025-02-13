from src.services import ModelService
from src.schemas import ApplicantSchema


applicant = ApplicantSchema(
    year=2023,
    gender="Ж",
    gpa=4.7,
    points=200,
    direction="27.03.04 Управление в технических системах"
)
applicant_1 = ApplicantSchema(
    year=2023,
    gender="Ж",
    gpa=4.7,
    points=0,
    direction="27.03.04 Управление в технических системах"
)
model_service = ModelService()
pred = model_service.predict_probability_of_applicant(applicant)
print(pred)
