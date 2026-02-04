from pydantic import BaseModel
from datetime import datetime


class RetrainJob(BaseModel):
    model_name: str
    reason: str
    triggered_at: datetime
