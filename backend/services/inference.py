import torch

from ml.models.multimodal_model import MultimodalTradingModel


class InferenceService:
    """
    Stateless inference service.
    Loads model once, serves predictions.
    """

    def __init__(self, model_path: str, input_dim: int):
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

        self.model = MultimodalTradingModel(input_dim=input_dim)
        self.model.load_state_dict(
            torch.load(model_path, map_location=self.device)
        )
        self.model.to(self.device)
        self.model.eval()

    @torch.no_grad()
    def predict(
        self,
        market_x: torch.Tensor,
        input_ids: torch.Tensor,
        attention_mask: torch.Tensor,
    ) -> dict:
        market_x = market_x.to(self.device)
        input_ids = input_ids.to(self.device)
        attention_mask = attention_mask.to(self.device)

        output = self.model(
            market_x,
            input_ids,
            attention_mask,
        )

        return {
            "p_up": float(output["p_up"].mean().cpu()),
            "expected_return": float(output["expected_return"].mean().cpu()),
            "uncertainty": float(output["uncertainty"].mean().cpu()),
        }
