from backend.db.session import engine
from backend.db.models import Base
from backend.db.audit_models import AuditLog


def init_db():
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    init_db()
