from unittest.mock import patch, Mock
from class_social.auth import AuthenticationController
from class_social.models import User, UserAuthenticate
import datetime

users_list = [
    User(id='someid', name='Mathias', username='mathias', password='somepass', email='mathias@mathias',
         created_on=datetime.datetime.now(), is_active=True, address="some_address")
]


def test_get_user_by_username_must_return_none_if_no_user_is_found_with_the_specified_id():
    with patch('class_social.db.load_users') as mocked_load_users:
        mocked_load_users.return_value = []
        controller = AuthenticationController()
        result = controller.get_user_by_username('nonexistent')
        assert result is None


def test_get_users_by_username_must_return_the_specified_user_object_if_user_exists():
    with patch('class_social.db.load_users') as mocked_load_users:
        mocked_load_users.return_value = users_list
        controller = AuthenticationController()
        result = controller.get_user_by_username('mathias')
        assert type(result) is User
        assert result == users_list[0]


def test_check_username_password_return_true_if_request_password_is_equal_to_db_password():
    controller = AuthenticationController()
    controller.get_user_by_username = Mock(return_value=users_list[0])
    user = UserAuthenticate(username='mathias', password='somepass')
    result = controller.check_username_password(user)
    print(result)
    assert type(result) is bool
    assert result is True


def test_check_username_password_return_false_if_request_password_is_not_equal_to_db_password():
    controller = AuthenticationController()
    controller.get_user_by_username = Mock(return_value=users_list[0])
    user = UserAuthenticate(username='mathias', password='wrong_pass')
    result = controller.check_username_password(user)
    print(result)
    assert type(result) is bool
    assert result is False


def test_check_username_password_return_false_if_request_username_is_not_equal_to_db_username(): #
    controller = AuthenticationController()
    controller.get_user_by_username = Mock(return_value=None)
    user = UserAuthenticate(username='mathias', password='somepass') # Todo check why it is not failing incase of proper values
    result = controller.check_username_password(user)
    print(result)
    assert type(result) is bool
    assert result is False


def test_encode_jwt_token_return_string():
    controller = AuthenticationController()
    user = UserAuthenticate(username='mathias', password='somepass')
    result = controller.encode_jwt_token(data={"sub": user.username})
    assert type(result) is str
