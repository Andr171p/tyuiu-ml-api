from typing import Literal, List

import pandas as pd

from pydantic import BaseModel, Field, field_validator

from .constants import (
    MIN_GPA,
    MAX_GPA,
    MIN_POINTS,
    MAX_POINTS,
    AVAILABLE_YEARS
)


class Applicant(BaseModel):
    year: int
    gender: Literal["male", "female"]
    gpa: float = Field(ge=MIN_GPA, le=MAX_GPA)
    points: int = Field(ge=MIN_POINTS, le=MAX_POINTS)
    direction: str

    @field_validator("year")
    def validate_year(cls, year: int) -> int:
        if year not in AVAILABLE_YEARS:
            raise ValueError("Year not in available years")
        return year

    def to_df(self) -> pd.DataFrame:
        return pd.DataFrame([self.model_dump()])


class Applicants(BaseModel):
    applicants: List[Applicant]

    def to_df(self) -> pd.DataFrame:
        return pd.DataFrame([applicant.model_dump() for applicant in self.applicants])


class ProbabilityResponse(BaseModel):
    probability: float


class ProbabilitiesResponse(BaseModel):
    probabilities: List[float]
