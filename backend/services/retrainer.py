import subprocess
from datetime import datetime

from backend.schemas.retrain import RetrainJob


class RetrainingService:
    """
    Orchestrates retraining jobs.
    """

    def trigger_retrain(self, model_name: str, reason: str) -> RetrainJob:
        # fire-and-forget retraining process
        subprocess.Popen(
            ["python", "ml/training/train_fusion.py"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )

        return RetrainJob(
            model_name=model_name,
            reason=reason,
            triggered_at=datetime.utcnow(),
        )
