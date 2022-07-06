import datetime
from unittest.mock import patch

import pytest

from class_social.db import DBException
from class_social.models import User, Post
from class_social.users import UserController, UserControllerError
from class_social.posts import PostController, PostControllerError

posts_list = [
    Post(title='Some_title', body='Text_content', creator=User(id='someid', name='Mathias', username='mathias', password='somepass', email='mathias@mathias',
         created_on=datetime.datetime.now(), is_active=True, address="some_address", role='Student'), creation_date=datetime.datetime.now(), type_of_post='text'),
    Post(title='Some_title2', body='Text_content2', creator=User(id='someid_2', name='Andreas', username='andreas', password='somepass', email='andreas@mathias',
           created_on=datetime.datetime.now(), is_active=True, address="some_address", role='Student'), creation_date=datetime.datetime.now(), type_of_post='text')
]


def test_get_posts_by_student_system_must_show_the_post_posted_by_student_and_return_200_ok():
    with patch('class_social.db.load_posts') as mocked_load_posts:
        mocked_load_posts.return_value = posts_list
        controller = PostController()
        result = controller.get_posts_by_creator_role('Student')
        assert result == posts_list


def test_get_posts_by_creator_role_must_return_none_if_no_post_is_found_with_the_specified_role():
    with patch('class_social.db.load_posts') as mocked_load_posts:
        mocked_load_posts.return_value = []
        controller = PostController()
        result = controller.get_posts_by_creator_role('non-existent-role')

        assert result == []
