from sqlalchemy.orm import Session
from backend.db.subscription_models import Subscription


def get_user_tier(db: Session, user_id: int) -> str:
    sub = db.query(Subscription).filter(
        Subscription.user_id == user_id
    ).first()

    return sub.tier if sub else "FREE"
