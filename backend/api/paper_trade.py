from backend.services.audit_logger import AuditLogger
from backend.db.session import SessionLocal

@router.post("/trade")
def paper_trade(req: PaperTradeRequest):
    db = SessionLocal()
    audit = AuditLogger(db)

    signal = TradeSignal(
        symbol=req.symbol,
        p_up=req.p_up,
        expected_return=req.expected_return,
        uncertainty=req.uncertainty,
        timestamp=req.timestamp,
    )

    trade = execution_engine.generate_trade(
        signal=signal,
        current_price=req.price,
        capital=portfolio.cash,
    )

    if trade:
        portfolio.apply_trade(trade)

        audit.log(
            event_type="trade",
            payload={
                "symbol": trade.symbol,
                "side": trade.side,
                "quantity": trade.quantity,
                "price": trade.price,
            },
        )

        db.close()
        return {"status": "executed", "trade": trade.dict()}

    db.close()
    return {"status": "no_trade"}
