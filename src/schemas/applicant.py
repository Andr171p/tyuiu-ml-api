from typing import Literal

from pydantic import BaseModel


class ApplicantSchema(BaseModel):
    year: int
    gender: Literal["М", "Ж"]
    gpa: float
    points: int
    direction: str
