from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from backend.db.models import Base


class Subscription(Base):
    __tablename__ = "subscriptions"

    id = Column(Integer, primary_key=True, index=True)
    tier = Column(String, default="FREE")  # FREE | PRO | QUANT

    user_id = Column(Integer, ForeignKey("users.id"), unique=True)
    user = relationship("User")
