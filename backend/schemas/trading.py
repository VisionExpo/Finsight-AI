from pydantic import BaseModel
from datetime import datetime
from typing import Optional


# ----------------------------
# MODEL OUTPUT (Signal)
# ----------------------------

class TradeSignal(BaseModel):
    """
    Output of the ML system.
    This is NOT a trade.
    """
    symbol: str

    p_up: float
    expected_return: float
    uncertainty: float

    model_version: Optional[str] = None
    timestamp: datetime


# ----------------------------
# EXECUTED TRADE (Paper Only)
# ----------------------------

class ExecutedTrade(BaseModel):
    """
    Result of execution logic.
    Generated only after passing risk & confidence checks.
    """
    symbol: str
    side: str  # BUY or SELL

    quantity: int
    execution_price: float

    signal_p_up: float
    signal_uncertainty: float

    timestamp: datetime


# ----------------------------
# PORTFOLIO SNAPSHOT (Optional)
# ----------------------------

class PortfolioSnapshot(BaseModel):
    """
    Lightweight portfolio state for analytics & audits.
    """
    cash: float
    positions: dict[str, int]
    total_value: float
    timestamp: datetime
