from fastapi import FastAPI
from app.api.v1.auth import router as auth_router

app = FastAPI(
    title="FastAPI Enterprise Backend",
    version="0.1.0",
)

app.include_router(auth_router)


@app.get("/")
def root():
    return {"status": "ok"}
