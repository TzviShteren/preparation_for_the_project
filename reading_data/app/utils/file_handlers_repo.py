import pandas as pd
from typing import Dict, Any
import json


def read_csv_file(file_path: str) -> pd.DataFrame:
    try:
        return pd.read_csv(file_path)
    except Exception as e:
        raise Exception(f"Error reading CSV file {file_path}: {str(e)}")


def read_json_file(file_path: str) -> Dict[str, Any]:
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except Exception as e:
        raise Exception(f"Error reading JSON file {file_path}: {str(e)}")