from fastapi import APIRouter, Depends
from backend.api.dependencies import require_feature

router = APIRouter(prefix="/backtest", tags=["backtest"])


@router.post("")
def run_backtest(
    user_id: int,
    allowed=Depends(require_feature("backtesting")),
):
    return {"status": "backtest started"}
