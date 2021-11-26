from typing import Sequence, Union
from datetime import date, datetime, time, timedelta

from bqsc import Table

class Prediction(Table):
    product_code: Union[int, Sequence[int]]
    week: Union[date, Sequence[date]]
    prediction: Union[float, Sequence[float]]
    observation: Union[float, Sequence[float]]
    exec_id: Union[str, Sequence[str]]
    ...


