from pydantic import BaseModel
from typing import List


class BacktestMetrics(BaseModel):
    total_return: float
    sharpe_ratio: float
    max_drawdown: float
    trades: int


class BacktestResult(BaseModel):
    equity_curve: List[float]
    metrics: BacktestMetrics
