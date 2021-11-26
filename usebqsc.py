import os
import json
from datetime import date

import bqsc
from bqsc.table import dataframe


def load_schema(path):
    with open(path) as f:
        return json.load(f)


Prediction = bqsc.load("prediction.json")
pred = Prediction()
pred.product_code = ["a", "b", "c"]
pred.week = [date(2021, 11, i+1) for i in range(3)]
pred.preidction = [100.0, 101.0, 102.0]
pred.observation = [100.0, 101.0, 102.0]
pred.exec_id = "exec_1234"
df = dataframe(pred)


df.to_gbq(
    "20211126_pydata.prediction",
    if_exists="append",
    project_id=os.getenv("GOOGLE_CLOUD_PROJECT"),
    table_schema=load_schema("prediction.json")
)
