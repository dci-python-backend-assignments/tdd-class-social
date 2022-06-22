from unittest.mock import patch, Mock

import pytest
from fastapi.testclient import TestClient

from class_social.main import app


@pytest.fixture
def http_test_client():
    return TestClient(app)


def test_given_valid_new_user_data_the_system_must_register_the_user_and_return_200_ok(http_test_client):
    with patch('class_social.users.user_controller') as controller_mock:
        controller_mock.get_users = Mock(return_value='users')
        response = http_test_client.get('/users')
        assert response.status_code == 200
        assert response.json() == 'users'
