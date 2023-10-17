from pydantic import BaseModel, RootModel
from datetime import datetime
from typing import List


class GetAnalyticsRequestSchema(BaseModel):
    startDate: datetime
    endDate: datetime
    metrics: List[str]
    incomeType: str


class Value(BaseModel):
    date: str
    value: float


class ModelItem(BaseModel):
    name: str
    type: str
    values: List[Value]


class GetAnalyticsResponseSchema(RootModel):
    root: List[ModelItem]
