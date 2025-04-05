import logging
from typing import List

from src.model import Model
from src.schemas import ApplicantSchema
from src.misc.converters import (
    convert_schema_to_dataframe,
    convert_schemas_to_dataframe
)


log = logging.getLogger(__name__)


class ModelService:
    _model = Model()
    
    def predict_applicant(self, applicant: ApplicantSchema) -> int:
        dataframe = convert_schema_to_dataframe(applicant)
        prediction = self._model.predict(dataframe)
        log.info("Successfully predicted applicant")
        return int(prediction[0])
        
    def predict_applicants(self, applicants: List[ApplicantSchema]) -> List[int]:
        dataframe = convert_schemas_to_dataframe(applicants)
        predictions = self._model.predict(dataframe)
        log.info("Successfully predicted applicants")
        return [int(prediction) for prediction in predictions]
        
    def predict_applicant_probability(
        self, 
        applicant: ApplicantSchema
    ) -> float:
        dataframe = convert_schema_to_dataframe(applicant)
        probability = self._model.predict_probability(dataframe)
        log.info("Successfully predicted probability of applicant")
        return float(probability[0][-1])
    
    def predict_applicants_probabilities(
        self, 
        applicants: List[ApplicantSchema]
    ) -> List[float]:
        dataframe = convert_schemas_to_dataframe(applicants)
        probabilities = self._model.predict_probability(dataframe)
        log.info("Successfully predicted probabilities of applicants")
        return [float(probability[-1]) for probability in probabilities]
