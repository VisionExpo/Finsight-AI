from backend.services.drift import DriftDetector
from backend.services.retrainer import RetrainingService


class DriftRetrainBridge:
    """
    Decides whether drift warrants retraining.
    """

    def __init__(self, p_value_threshold=0.05):
        self.detector = DriftDetector(p_value_threshold)
        self.retrainer = RetrainingService()

    def evaluate_and_trigger(
        self,
        reference: list[float],
        current: list[float],
        model_name: str,
    ):
        result = self.detector.ks_drift(reference, current)

        if result["drift_detected"]:
            return self.retrainer.trigger_retrain(
                model_name=model_name,
                reason="distribution_drift_detected",
            )

        return None
