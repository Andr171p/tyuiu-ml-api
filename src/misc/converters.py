from typing import List, Union

from pydantic import BaseModel
from pandas import DataFrame


def convert_schema_to_dataframe(schema: BaseModel) -> DataFrame:
    return DataFrame([schema.model_dump()])


def convert_schemas_to_dataframe(schemas: List[BaseModel]) -> DataFrame:
    return DataFrame([schema.model_dump() for schema in schemas])
