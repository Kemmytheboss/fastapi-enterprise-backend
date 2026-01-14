from fastapi import FastAPI
from app.db.base import Base
from app.db.session import engine
from app.api.v1.router import api_router

app = FastAPI(title="Enterprise FastAPI Backend")

@app.on.event("startup")
def on_startup():
    # Create database tables
    Base.metadata.create_all(bind=engine)

@app.get("/health")
def health_check():
    return {"status": "ok"}

app.include_router(api_router, prefix="/api/v1")
