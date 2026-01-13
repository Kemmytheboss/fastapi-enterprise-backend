from pydantic import BaseSettings

class Settings(BaseSettings):
     DATABASE_URL: str = "postgresql://postgres:postgres@db:5432/app"
    SECRET_KEY: str = "supersecretkey"
    ALGORITHM: str = "HS256"

settings = Settings()