from typing import Literal, List

from pydantic import BaseModel


class ApplicantSchema(BaseModel):
    year: int
    gender: Literal["male", "female"]
    gpa: float
    points: int
    direction: str
    
    
class ApplicantsSchema(BaseModel):
    applicants: List[ApplicantSchema]
