import numpy as np

from backend.services.execution import PaperExecutionEngine
from backend.services.portfolio import Portfolio
from backend.schemas.trading import TradeSignal


class BacktestEngine:
    """
    Replays historical signals using the paper execution engine.
    """

    def __init__(self, initial_capital: float = 1_000_000):
        self.initial_capital = initial_capital
        self.execution_engine = PaperExecutionEngine()

    def run(
        self,
        signals: list[TradeSignal],
        prices: list[float],
    ):
        portfolio = Portfolio(self.initial_capital)
        equity_curve = []

        for signal, price in zip(signals, prices):
            trade = self.execution_engine.generate_trade(
                signal=signal,
                current_price=price,
                capital=portfolio.cash,
            )

            if trade:
                portfolio.apply_trade(trade)

            equity = portfolio.cash + sum(
                qty * price for qty in portfolio.positions.values()
            )
            equity_curve.append(equity)

        return equity_curve, portfolio.trade_log
