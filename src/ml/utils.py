import io
from typing import List, Dict, Any

import joblib
import pandas as pd


def transform_data(
        data: Dict[str, Any] | List[Dict[str, Any]]
) -> pd.DataFrame:
    if isinstance(data, dict):
        df = pd.DataFrame(data, index=[0])
        return df
    elif isinstance(data, list):
        df = pd.DataFrame(data)
        print(type(df))
        return df


def get_upper_columns(data: pd.DataFrame) -> pd.DataFrame:
    upper_columns = {col: col.capitalize() for col in data.columns}
    return data.rename(columns=upper_columns)


def load_object(body: bytes) -> Any:
    return joblib.load(io.BytesIO(body))
