import datetime
from unittest.mock import patch, Mock

import pytest
from fastapi.testclient import TestClient

from class_social.main import app


@pytest.fixture
def http_test_client():
    return TestClient(app)


valid_post_list = [{
    'title': 'Some_title',
    'body': 'text_content',
    'creator': {'id': 'c1',
    'name': 'Mathias',
    'username': 'mathias',
    'password': 'somepass',
    'email': 'mathias@mathias',
    'created_on': "2023-03-27T00:00:00.000+00:00",
    'is_active': True,
    'address': 'some_address',
    'role': 'Student'
    },
    'creation_date': datetime.datetime.now(),
    'type_of_post': 'Text'
},
{
    'title': 'Some_title_2',
    'body': 'image_content',
    'creator': {'id': 'c2',
    'name': 'Mat',
    'username': 'mat',
    'password': 'some_pass',
    'email': 'mathias@mat',
    'created_on': "2023-03-27T00:00:00.000+00:00",
    'is_active': True,
    'address': 'some_address',
    'role': 'Student'
    },
    'creation_date': datetime.datetime.now(),
    'type_of_post': 'Image'
},
{
    'title': 'Some_title_2',
    'body': 'image_content',
    'creator': {'id': 'c3',
    'name': 'Mat',
    'username': 'mat',
    'password': 'some_pass',
    'email': 'mathias@mat',
    'created_on': "2023-03-27T00:00:00.000+00:00",
    'is_active': True,
    'address': 'some_address',
    'role': 'Teacher'
    },
    'creation_date': datetime.datetime.now(),
    'type_of_post': 'Image'
},
{
    'title': 'Some_title_2',
    'body': 'image_content',
    'creator': {'id': 'c4',
    'name': 'Mat',
    'username': 'mat',
    'password': 'some_pass',
    'email': 'mathias@mat',
    'created_on': "2023-03-27T00:00:00.000+00:00",
    'is_active': True,
    'address': 'some_address',
    'role': 'Institution'
    },
    'creation_date': datetime.datetime.now(),
    'type_of_post': 'Image'
}
]


def test_given_an_id_for_an_existent_user_system_must_return_200_ok(http_test_client):
    with patch('class_social.posts.post_controller') as controller_mock:
        controller_mock.get_posts_by_creator_role = Mock(return_value=valid_post_list)
        response = http_test_client.get('/posts/creator/{role}')
        assert response.status_code == 200


def test_given_a_nonexistent_creator_role_system_must_return_404_ok(http_test_client):
    with patch('class_social.users.user_controller') as controller_mock:
        controller_mock.get_posts_by_creator_role = Mock(return_value=None)
        response = http_test_client.get('/posts/creator/nonexistent_role')
        assert response.status_code == 404
