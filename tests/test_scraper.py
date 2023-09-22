from fastapi import status
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_scraper() -> None:
    response = client.get("/api/v1/scraper")
    assert response.status_code == status.HTTP_200_OK
    assert isinstance(response.content, list)
