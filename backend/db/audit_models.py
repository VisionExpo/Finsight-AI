from sqlalchemy import Column, Integer, String, DateTime, JSON
from datetime import datetime
from backend.db.models import Base


class AuditLog(Base):
    __tablename__ = "audit_logs"

    id = Column(Integer, primary_key=True, index=True)
    event_type = Column(String, index=True)  # prediction | trade | drift | retrain
    user_id = Column(Integer, nullable=True)

    payload = Column(JSON)  # inputs + outputs snapshot
    created_at = Column(DateTime, default=datetime.utcnow)
