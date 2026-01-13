from fastapi.testclient import TestClient
from app.core.main import app

client = TestClient(app)

def test_user_registration():
    response = client.post(
        "/api/v1/users/",
        json={"email": "test@example.com", "password": "password123"}

    )
    assert response.status_code == 201