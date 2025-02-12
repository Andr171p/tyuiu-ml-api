from src.model import TransformerFactory, ModelFactory
from src.model.encoders import (
    LabelBinarizer,
    LabelEncoder,
    OneHotEncoder
)
from src.model.scalers import StandardScaler
from src.model.classifiers import Classifier


class ModelService:
    def predict_applicant(self) -> ...:
        ...
        
    def predict_applicants(self) -> ...:
        ...
        
    ...

