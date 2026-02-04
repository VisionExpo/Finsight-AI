from pydantic import BaseModel


class SubscriptionOut(BaseModel):
    tier: str

    class Config:
        orm_mode = True
