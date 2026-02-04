from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

from backend.db.session import SessionLocal
from backend.services.subscription import get_user_tier
from backend.services.feature_gates import is_feature_allowed


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def require_feature(feature: str):
    def checker(user_id: int, db: Session = Depends(get_db)):
        tier = get_user_tier(db, user_id)
        if not is_feature_allowed(tier, feature):
            raise HTTPException(
                status_code=403,
                detail=f"{feature} not allowed for tier {tier}",
            )
        return True

    return checker
