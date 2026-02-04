from sqlalchemy.orm import Session
from backend.db.audit_models import AuditLog


class AuditLogger:
    def __init__(self, db: Session):
        self.db = db

    def log(
        self,
        event_type: str,
        payload: dict,
        user_id: int | None = None,
    ):
        entry = AuditLog(
            event_type=event_type,
            payload=payload,
            user_id=user_id,
        )
        self.db.add(entry)
        self.db.commit()
