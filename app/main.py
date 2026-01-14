import time
from fastapi import FastAPI
from sqlalchemy.exc import OperationalError

from app.api.v1.router import api_router
from app.db.session import engine
from app.db.base import Base

app = FastAPI(title="FastAPI Enterprise Backend")

app.include_router(api_router, prefix="/api/v1")


@app.on_event("startup")
def on_startup():
    retries = 10
    while retries:
        try:
            Base.metadata.create_all(bind=engine)
            print("Database connected")
            break
        except OperationalError:
            retries -= 1
            print("Waiting for database...")
            time.sleep(2)
    else:
        raise Exception("Database not available")
