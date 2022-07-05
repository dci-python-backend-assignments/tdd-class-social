from unittest.mock import patch, Mock

import pytest
from fastapi.testclient import TestClient
from class_social.main import app

@pytest.fixture
def http_test_client():
    return TestClient(app)

post_user = {
    "id": '1234',
    "name": 'Wasi',
    "username": 'wasi',
    "password": 'somepass',
    "email": 'wasi@mathias',
    "created_on": "2023-03-27T00:00:00.000+00:00",
    "is_active": True,
    "address": 'some address 123'
}

valid_post = {
    "title": 'Our First Post',
    "body": 'Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam' \
            ' nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, s' \
            'ed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd g' \
            'ubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, ' \
            'sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo' \
            ' duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet.',
    "creator": post_user, # TODO a user dictionary here OR remove it completely!!
    "creation_date": '2023-03-27T00:00:00.000+00:00',
    "type_of_post": 'some type'
}

def test_given_invalid_new_post_format_422(http_test_client):
    response = http_test_client.post('/posts', json={})
    assert response.status_code == 422