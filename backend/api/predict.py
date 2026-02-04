from backend.services.audit_logger import AuditLogger
from backend.db.session import SessionLocal

@router.post("/predict", response_model=PredictResponse)
def predict(req: PredictRequest):
    db = SessionLocal()
    audit = AuditLogger(db)

    market_x = torch.tensor(req.market_sequence).unsqueeze(0)
    input_ids = torch.tensor(req.input_ids).unsqueeze(0)
    attention_mask = torch.tensor(req.attention_mask).unsqueeze(0)

    out = inference_service.predict(
        market_x,
        input_ids,
        attention_mask,
    )

    audit.log(
        event_type="prediction",
        payload={
            "symbol": req.symbol,
            "output": out,
        },
    )

    db.close()
    return PredictResponse(**out)
