import datetime
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
    # {"w1","wasi", "123456w","wasi@atwasi.c","2023-03-27T00:00:00.000+00:00",True,"Wasi","someaddress 123","wasi.co","con1","about me about me"}, # TODO a user dictionary here OR remove it completely!!


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
    'role': 'Teacher'
    },
    'creation_date': datetime.datetime.now(),
    'type_of_post': 'Text'
}]


def test_given_an_existent_creator_role_for_the_user_system_must_return_post_list_and_200_ok(http_test_client):
    with patch('class_social.posts.post_controller') as controller_mock:
        controller_mock.get_posts_by_creator_role = Mock(return_value=valid_post_list)
        response = http_test_client.get('posts/creator/Teacher')
        print(response.text)
        assert response.status_code == 200


def test_given_a_nonexistent_creator_role_system_must_return_404_ok(http_test_client):
    with patch('class_social.posts.post_controller') as controller_mock:
        controller_mock.get_posts_by_creator_role = Mock(return_value=None)
        response = http_test_client.get('/posts/creator/anything')
        assert response.status_code == 404


def test_given_invalid_new_post_format_422(http_test_client):
    response = http_test_client.post('/posts', json={})
    assert response.status_code == 422


def test_given_valid_new_post_entry_the_system_must_submit_the_post_and_return_200_ok(http_test_client):
    with patch('class_social.posts.post_controller') as controller_mock:
        controller_mock.post_a_post = Mock(return_value=None)
        response = http_test_client.post('/posts', json=valid_post)
        assert response.status_code == 200
