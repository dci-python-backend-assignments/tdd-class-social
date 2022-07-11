from pathlib import Path

import pytest


from fastapi.testclient import TestClient
from class_social.main import app


@pytest.fixture
def http_test_client():
    return TestClient(app)


def test_must_always_return_a_list_of_files_and_200_ok(http_test_client):
    _test_file = Path("kk.png")
    _files = {"files": _test_file.open("rb")}
    response = http_test_client.post('/teacher/upload', files=_files)
    assert response.status_code == 200


def test_when_invalid_data_is_received_return_unprocessable_data_and_422(http_test_client):
    _files = {}
    response = http_test_client.post('/teacher/upload', files=_files)
    assert response.status_code == 422


def test_when_no_data_is_received_return_422_unprocessable_data(http_test_client):
    response = http_test_client.post('/teacher/upload')
    assert response.status_code == 422

