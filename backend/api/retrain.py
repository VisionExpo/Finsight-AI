from fastapi import APIRouter
from datetime import datetime

from backend.services.drift_retrain_bridge import DriftRetrainBridge

router = APIRouter(prefix="/retrain", tags=["retrain"])

bridge = DriftRetrainBridge()


@router.post("")
def retrain(
    reference: list[float],
    current: list[float],
    model_name: str = "fusion_model",
):
    job = bridge.evaluate_and_trigger(
        reference=reference,
        current=current,
        model_name=model_name,
    )

    if job:
        return {"status": "retraining_triggered", "job": job}

    return {"status": "no_retraining_needed"}
