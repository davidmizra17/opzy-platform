import pytest


@pytest.mark.django_db
def test_start_session_creates_visitor(client):
    response = client.post("/api/v1/public/visitors", {}, content_type="application/json")
    assert response.status_code == 201
    body = response.json()
    assert body["visitor_id"] and body["token"]


@pytest.mark.django_db
def test_start_session_reuses_visitor(client):
    first = client.post("/api/v1/public/visitors", {}, content_type="application/json").json()
    second = client.post(
        "/api/v1/public/visitors",
        {"visitor_id": first["visitor_id"]},
        content_type="application/json",
    ).json()
    assert second["visitor_id"] == first["visitor_id"]
    assert second["token"] != first["token"]
