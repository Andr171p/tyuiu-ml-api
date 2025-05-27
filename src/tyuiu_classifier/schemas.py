from typing import Literal

import pandas as pd

from pydantic import BaseModel, Field

from .constants import (
    MIN_GPA,
    MAX_GPA,
    MIN_POINTS,
    MAX_POINTS,
    AVAILABLE_YEARS
)


class Applicant(BaseModel):
    year: AVAILABLE_YEARS
    gender: Literal["male", "female"]
    gpa: float = Field(ge=MIN_GPA, le=MAX_GPA)
    points: int = Field(ge=MIN_POINTS, le=MAX_POINTS)
    direction: str

    def to_df(self) -> pd.DataFrame:
        return pd.DataFrame([self.model_dump()])


class Applicants(BaseModel):
    applicants: list[Applicant]

    def to_df(self) -> pd.DataFrame:
        return pd.DataFrame([applicant.model_dump() for applicant in self.applicants])


class Prediction(BaseModel):
    direction: str
    probability: float
