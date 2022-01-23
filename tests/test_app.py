from app import create_app
from fastapi.testclient import TestClient

app = create_app()
test_client = TestClient(app)

def test_health_endpoint():
    response = test_client.get("/health")

    assert response.json() == {"health": "OK"}