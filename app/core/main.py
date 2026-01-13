from fastapi import FastAPI
from app.db.base import Base
from app.db.session import engine

from app.api.v1.endpoints.router import api_router
app.include_router(api_router, prefix="/api/v1")

app = FastAPI(title="Enterprise FastAPI Backend")

@app.get("/health")
def health_check():
    return {"status": "ok"}
