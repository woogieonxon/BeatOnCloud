import pytest


@pytest.fixture()
def client():
    app = create_app()
    return app.test_client()


def test_index(client):
    res = client.get("/")
    assert res.status.code == 200
