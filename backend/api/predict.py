import torch
from fastapi import APIRouter

from backend.schemas.predict import PredictRequest, PredictResponse
from backend.services.inference import InferenceService

router = APIRouter()

# singleton inference service
inference_service = InferenceService(
    model_path="models/fusion_model.pt",
    input_dim=10,
)


@router.post("/predict", response_model=PredictResponse)
def predict(req: PredictRequest):
    market_x = torch.tensor(req.market_sequence).unsqueeze(0)
    input_ids = torch.tensor(req.input_ids).unsqueeze(0)
    attention_mask = torch.tensor(req.attention_mask).unsqueeze(0)

    out = inference_service.predict(
        market_x,
        input_ids,
        attention_mask,
    )

    return PredictResponse(**out)
