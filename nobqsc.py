import pandas as pd
import os
import json
from datetime import date


def load_schema(path):
    with open(path) as f:
        return json.load(f)


df = pd.DataFrame({
    "product_code": [1, 2, 3],
    "week": [date(2021, 11, i+1) for i in range(3)],
    "preidction": [100.0, 101.0, 102.0],
    "observation": [100.0, 100.0, 100.0],
    "exec_id": "exec_1234"
})

df.to_gbq(
    "20211126_pydata.prediction",
    if_exists="append",
    project_id=os.getenv("GOOGLE_CLOUD_PROJECT"),
    table_schema=load_schema("prediction.json")
)
