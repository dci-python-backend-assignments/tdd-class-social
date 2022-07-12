from unittest.mock import patch, Mock

import pytest
from fastapi.testclient import TestClient

from class_social.main import app
from class_social.models import User


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
    "address": 'some_address',
    "role": "Teacher"
}

valid_obj_user = User(id='someid', name='Mathias', username='mathias', password='somepass', email='mathias@mathias',
          created_on="2023-03-27T00:00:00.000+00:00", is_active=True, address="some_address", role="Teacher")

valid_obj_user2 = User(id='someid', name='Mathias', username='mathias', password='somepass', email='mathias@mathias',
          created_on="2023-03-27T00:00:00.000+00:00", is_active=False, address="some_address", role="Teacher")


def test_given_valid_new_user_data_the_system_must_register_the_user_and_return_200_ok(http_test_client):
    with patch('class_social.users.user_controller') as controller_mock:
        controller_mock.insert_users = Mock(return_value=None)
        response = http_test_client.post('/users', data=bytes(valid_obj_user.json(), "UTF-8"))
        assert response.status_code == 200


def test_given_invalid_new_user_data_the_system_must_return_422(http_test_client):
    response = http_test_client.post('/users', json={})
    assert response.status_code == 422


def test_given_an_id_for_an_existent_user_system_must_return_200_ok(http_test_client):
    with patch('class_social.users.user_controller') as controller_mock:
        controller_mock.get_user_by_id = Mock(return_value=valid_obj_user)
        response = http_test_client.get('/users/c1')
        assert response.status_code == 200


def test_given_an_nonexistent_user_id_system_must_return_404_ok(http_test_client):
    with patch('class_social.users.user_controller') as controller_mock:
        controller_mock.get_user_by_id = Mock(return_value=None)
        response = http_test_client.get('/users/nonexistent_id')
        assert response.status_code == 404


def test_given_is_active_is_true_for_an_existent_user_system_must_return_200_ok(http_test_client):
    with patch('class_social.users.user_controller') as controller_mock:
        controller_mock.get_user_by_is_active = Mock(return_value=valid_obj_user)
        response = http_test_client.get('/users/someid/is_active')
        assert response.status_code == 200


def test_given_is_active_is_false_for_an_existent_user_system_must_return_404_ok(http_test_client):
    with patch('class_social.users.user_controller') as controller_mock:
        controller_mock.get_user_by_is_active = Mock(return_value=valid_obj_user2)
        response = http_test_client.get('/users/someid/is_active')
        assert response.status_code == 404


def test_must_always_return_a_list_of_users_and_200_ok(http_test_client):
    with patch('class_social.users.user_controller') as controller_mock:
        controller_mock.get_users = Mock(return_value=[])
        response = http_test_client.get('/users')
        assert response.status_code == 200

        controller_mock.get_users = Mock(return_value=[valid_obj_user])
        response = http_test_client.get('/users')
        assert response.status_code == 200

def test_must_return_edited_user_and_200_ok(http_test_client):
    with patch('class_social.users.user_controller') as controller_mock:
        controller_mock.edit_user_profile = Mock(return_value=valid_user)
        response = http_test_client.patch('/users/{user_id}/profile', json={"user": valid_user, "changes": {}})
        assert response.status_code == 200

def test_institution_confirm_users_if_the_data_is_not_valid__and_422_ok(http_test_client):
    with patch('class_social.users.user_controller') as controller_mock:
        controller_mock.institution_confirm_users = Mock(return_value=None)
        response = http_test_client.get('/user_confirmation/institution')
        assert response.status_code == 422


def test_institution_confirm_users_always_return_a_none_and_200_ok(http_test_client):
    with patch('class_social.users.user_controller') as controller_mock:
        controller_mock.institution_confirm_users = Mock(return_value=None)
        response = http_test_client.get('/user_confirmation/institution', json=valid_user)
        assert response.status_code == 200


