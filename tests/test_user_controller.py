import datetime

from unittest.mock import patch

import pytest

from class_social.db import DBException
from class_social.models import User
from class_social.users import UserController, UserControllerError

users_list = [
    User(id='someid', name='Mathias', username='mathias', password='somepass', email='mathias@mathias',
         created_on=datetime.datetime.now(), is_active=True, address="some_address", role='Teacher')
]


def test_get_users_by_id_must_return_none_if_no_user_is_found_with_the_specified_id():
    with patch('class_social.db.load_users') as mocked_load_users:
        mocked_load_users.return_value = []
        controller = UserController()
        result = controller.get_user_by_id('nonexistent')

        assert result is None


def test_get_users_must_return_the_specified_user_object_if_user_exists():
    with patch('class_social.db.load_users') as mocked_load_users:
        mocked_load_users.return_value = users_list
        controller = UserController()
        result = controller.get_user_by_id('someid')
        assert type(result) is User
        assert result == users_list[0]


def test_is_email_in_database_returns_a_True_if_a_user_exists():
    with patch('class_social.db.load_users') as mocked_load_users:
        mocked_load_users.return_value = users_list
        controller = UserController()
        result = controller.is_email_in_database('mathias@mathias')
        assert result is True


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


# ----------------------------------------------- #20_begin
def test_get_users_must_return_the_specified_user_if_user_exists():
    with patch('class_social.db.load_users') as mocked_load_users:
        mocked_load_users.return_value = users_list
        controller = UserController()
        result = controller.get_user_by_username_and_password('mathias', 'somepass')
        assert result == users_list[0]

# ------------------------------------------------ #20_end
