from backend.services.backtest import BacktestEngine
from backend.services.metrics import sharpe_ratio, max_drawdown
from backend.schemas.backtest import BacktestResult, BacktestMetrics


def run_backtest(signals, prices):
    engine = BacktestEngine()
    equity_curve, trades = engine.run(signals, prices)

    metrics = BacktestMetrics(
        total_return=(equity_curve[-1] / equity_curve[0]) - 1,
        sharpe_ratio=sharpe_ratio(equity_curve),
        max_drawdown=max_drawdown(equity_curve),
        trades=len(trades),
    )

    return BacktestResult(
        equity_curve=equity_curve,
        metrics=metrics,
    )
