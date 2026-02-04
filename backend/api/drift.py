from backend.services.audit_logger import AuditLogger
from backend.db.session import SessionLocal

@router.post("", response_model=DriftResult)
def detect_drift(reference: list[float], current: list[float]):
    db = SessionLocal()
    audit = AuditLogger(db)

    result = detector.ks_drift(reference, current)

    audit.log(
        event_type="drift",
        payload=result,
    )

    db.close()
    return result
