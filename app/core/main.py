from fastapi import FastAPI
from app.db.base import Base
from app.db.session import engine

app = FastAPI(title="Enterprise FastAPI Backend")

@app.get("/health")
def health_check():
    return {"status": "ok"}
