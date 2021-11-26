import pandas as pd
import os
import json
from datetime import date, timedelta

import bqsc
from bqsc.table import dataframe


def load_schema(path):
    with open(path) as f:
        return json.load(f)


schema = load_schema("prediction.json")

Prediction = bqsc.load("prediction.json")
pred = Prediction()
pred.product_code = [1, 2, 3]
pred.week = [f"2021-11-{i}" for i in range(3)]
pred.prediction = [100.0, 101.0, 102.0]
pred.observation = [100.0, 101.0, 102.0]
pred.exec_id = "exec_1234"

df = dataframe(pred)

# df = pd.DataFrame({
#     "product_code": [1, 2, 3],
#     "week": [date(2021, 11, 20) + timedelta(days=i) for i in range(3)],
#     "prediction": [100, 101, 102],
#     "observation": [100, 100, 100],
#     "exec_id": "exec_1234"
# })

df.to_gbq(
    "20211126_pydata.prediction",
    if_exists="append",
    project_id=os.getenv("GOOGLE_CLOUD_PROJECT"),
    table_schema=schema
)
