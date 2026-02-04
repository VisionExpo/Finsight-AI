from pydantic import BaseModel
from typing import List


class PredictRequest(BaseModel):
    symbol: str
    market_sequence: List[List[float]]  # (T, F)
    input_ids: List[int]
    attention_mask: List[int]


class PredictResponse(BaseModel):
    p_up: float
    expected_return: float
    uncertainty: float
