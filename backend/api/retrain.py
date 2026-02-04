from backend.services.audit_logger import AuditLogger
from backend.db.session import SessionLocal

@router.post("")
def retrain(reference: list[float], current: list[float], model_name: str):
    db = SessionLocal()
    audit = AuditLogger(db)

    job = bridge.evaluate_and_trigger(
        reference=reference,
        current=current,
        model_name=model_name,
    )

    audit.log(
        event_type="retrain",
        payload={
            "model": model_name,
            "triggered": bool(job),
        },
    )

    db.close()
    return {"status": "logged"}
