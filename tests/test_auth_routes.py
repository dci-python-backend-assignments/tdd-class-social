from unittest.mock import patch, Mock
import pytest
from fastapi.testclient import TestClient
from class_social.main import app
from class_social.models import Token


@pytest.fixture
def http_test_client():
    return TestClient(app)


valid_user = {
    "id": 'c1',
    "name": 'Mathias',
    "username": 'mathias',
    "password": 'somepass',
    "email": 'mathias@mathias',
    "created_on": "2023-03-27T00:00:00.000+00:00",
    "is_active": True,
    "address": 'some_address'
}
valid_user_info = {

    "username": 'mathias',
    "password": 'somepass',

}
valid_token = {"access_token": "some_token", "token_type": "Bearer"}

# todo check if this test is necessary for security reasons
# def test_get_request_returns_405(http_test_client):
#     # login endpoint does only expect a post request get requests will be denied
#
#     # to pass the test see the main file and comment out the lines which include other routes than auth_route
#     response = http_test_client.get("/users/auth")
#     assert response.status_code == 405


def test_post_request_without_body_returns_422(http_test_client):
    # body should have username, password (and fullname)
    with patch('class_social.auth.auth_controller') as controller_mock:
        # we need to mock all the methods of the auth_controller which hase been used inside the post_authenticate_user
        controller_mock.get_user_by_username = Mock(return_value=valid_user)  # the get_user_by_username returns user
        controller_mock.check_username_password = Mock(return_value=True)  # the check_username_password returns bool
        controller_mock.encode_jwt_token = Mock(return_value="string")  # the encode_jwt_token returns a string

        response = http_test_client.post("/users/auth")
        assert response.status_code == 422


def test_post_request_with_improper_body_returns_422(http_test_client):
    # both username and password is required
    with patch('class_social.auth.auth_controller') as controller_mock:
        # we need to mock all the methods of the auth_controller which hase been used inside the post_authenticate_user
        controller_mock.get_user_by_username = Mock(return_value=valid_user)  # the get_user_by_username returns user
        controller_mock.check_username_password = Mock(return_value=True)  # the check_username_password returns bool
        controller_mock.encode_jwt_token = Mock(return_value="string")  # the encode_jwt_token returns a string

        response = http_test_client.post("/users/auth", json={"username": "mathias"})
        assert response.status_code == 422


def test_post_request_with_proper_body_returns_200_with_jwt_token(http_test_client):
    with patch('class_social.auth.auth_controller') as controller_mock:
        # we need to mock all the methods of the auth_controller which hase been used inside the post_authenticate_user
        controller_mock.get_user_by_username = Mock(return_value=valid_user)  # the get_user_by_username returns user
        controller_mock.check_username_password = Mock(return_value=True)  # the check_username_password returns bool
        controller_mock.encode_jwt_token = Mock(return_value="string")  # the encode_jwt_token returns a string

        response = http_test_client.post('/users/auth', json={"username": "mathias", "password": "wrong_pass"})
        # response = http_test_client.post('/users/auth', json=valid_user_info) # this is the same as the above line
        assert response.status_code == 200
        assert len(response.json()) == 2
        # assert type(response.text) is Token
