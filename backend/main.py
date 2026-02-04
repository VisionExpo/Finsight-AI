from fastapi import FastAPI
from backend.api import predict

app = FastAPI(title="ArthaQuant API")

app.include_router(predict.router)
