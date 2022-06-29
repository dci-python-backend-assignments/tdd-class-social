import datetime
from unittest.mock import patch, Mock

import pytest

from class_social.db import DBException
from class_social.models import User
from class_social.users import UserController, UserControllerError

users_list = [
    User(id='someid', name='Mathias', username='mathias', password='somepass', email='mathias@mathias',
         created_on=datetime.datetime.now(), is_active=True, address="some_address")
]


def test_if_user_was_edited_it_still_should_be_valid_and_changes_be_incorporated():
    with patch('class_social.db.load_users') as mocked_load_users:
        valid_user = User(id='c1', name='Franz', username='mathias', password='somepass', email='mathias@mathias',
                          created_on="2023-03-27T00:00:00.000+00:00", is_active=True, address='some_address')
        mocked_load_users.return_value = Mock(return_value=valid_user)
        controller = UserController()
        result = controller.edit_user_profile(valid_user)

        assert result is mocked_load_users.return_value


def test_get_users_must_return_the_specified_user_object_if_user_exists():
    with patch('class_social.db.load_users') as mocked_load_users:
        mocked_load_users.return_value = users_list
        controller = UserController()
        result = controller.get_user_by_id('someid')
        assert type(result) is User
        assert result == users_list[0]


def test_insert_users_operation_must_raise_exception_if_db_operation_fails():
    with patch('class_social.db.save_users') as mocked_save_users:
        with patch('class_social.db.load_users') as mocked_load_users:
            mocked_load_users.return_value = []
            mocked_save_users.side_effect = DBException()
            controller = UserController()

            with pytest.raises(UserControllerError):
                controller.insert_users(users_list[0])


def test_get_users_operation_must_raise_exception_if_db_operation_fails():
    with patch('class_social.db.load_users') as mocked_load_users:
        mocked_load_users.side_effect = DBException()

        controller = UserController()

        with pytest.raises(UserControllerError):
            controller.get_users()
