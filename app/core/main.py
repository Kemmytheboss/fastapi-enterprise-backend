from fastapi import FastAPI

app = FastAPI(title="Enterprise FastAPI Backend")

@app.get("/health")
def health_check():
    return {"status": "ok"}
