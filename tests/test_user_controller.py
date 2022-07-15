import datetime

from unittest.mock import patch, Mock
from fastapi import HTTPException


import pytest

from class_social.db import DBException
from class_social.models import User, Student, Institution
from class_social.users import UserController, UserControllerError

users_list = [
    User(id='someid', name='Mathias', username='mathias', password='somepass', email='mathias@mathias',
         created_on=datetime.datetime.now(), is_active=True, address="some_address", role='Teacher')
]
student = Student(id='someid', name='Mathias', username='mathias', password='somepass', email='mathias@mathias',
                  date_of_birth='1985-03-27T00:00:00.000+00:00', gender='male', phone_number='124442',
                  created_on=datetime.datetime.now(), is_active=True, address="some_address")

student_1 = Student(id='som3id', name='Mat', username='mat1', password='som3pass', email='mat@mathi',
                    date_of_birth='1985-03-27T00:00:00.000+00:00', gender='male', phone_number='12442',
                    created_on=datetime.datetime.now(), is_active=True, address="some_1_address")

institution_association_request_list_empty = \
    Institution(id='1', username='institution1', password='124', email='institution1@somee.com',
                created_on=datetime.datetime.now(), is_active=True, name='thesomeinstitut', address='lincon str 123',
                phone_numbers=['1234121', '1134123'],
                associates=[], association_requests=[],
                head_of_organization='Mathias',
                research_institution=False, education_institution=True)

institution_with_no_associates_requests_at_all = \
    Institution(id='2', username='someinstitution', password='123', email='someinstitut@somee.com',
                created_on=datetime.datetime.now(), is_active=True, name='thesomeinstitut', address='lincon str 123',
                phone_numbers=['1234121', '1134123'], associates=[],
                head_of_organization='Mathias',
                research_institution=False, education_institution=True)

institution_association_request_non_empty_list = \
    Institution(id='1', username='institution1', password='124', email='institution1@somee.com',
                created_on=datetime.datetime.now(), is_active=True, name='thesomeinstitut', address='lincon str 123',
                phone_numbers=['1234121', '1134123'],
                associates=[], association_requests=[student, student_1],
                head_of_organization='Mathias',
                research_institution=False, education_institution=True)

institution_association_request_non_empty_list_1 = \
    Institution(id='2', username='institution1', password='124', email='institution1@somee.com',
                created_on=datetime.datetime.now(), is_active=True, name='thesomeinstitut', address='lincon str 123',
                phone_numbers=['1234121', '1134123'],
                associates=[], association_requests=[student],
                head_of_organization='Mathias',
                research_institution=False, education_institution=True)

institution_associated_with_a_user = \
    Institution(id='1', username='institution1', password='124', email='institution1@somee.com',
                created_on=datetime.datetime.now(), is_active=True, name='thesomeinstitut', address='lincon str 123',
                phone_numbers=['1234121', '1134123'],
                associates=[student_1], association_requests=[],
                head_of_organization='Mathias',
                research_institution=False, education_institution=True)

student_with_an_institution_associated = \
    Student(id='someid', name='Mathias', username='mathias', password='somepass', email='mathias@mathias',
            date_of_birth='1985-03-27T00:00:00.000+00:00', gender='male', phone_number='124442',
            created_on=datetime.datetime.now(), is_active=True, address="some_address",
            institution=institution_associated_with_a_user)

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


# test for editing profile
def test_if_user_was_edited_it_still_should_be_the_same_object_and_changes_be_incorporated():
    with patch('class_social.db.load_users') as mocked_load_users:
        valid_user = User(id='c1', name='Mathias', username='mathias', password='somepass', email='mathias@mathias',
                          created_on="2023-03-27T00:00:00.000+00:00", is_active=True, address='some_address')
        expected_user = User(id='c1', name='Franz', username='mathias', password='somepass', email='mathias@mathias',
                          created_on="2023-03-27T00:00:00.000+00:00", is_active=True, address='Somestreet 69')
        mocked_load_users.return_value = [expected_user]
        controller = UserController()
        original_user = Mock(return_value=valid_user)
        result = controller.edit_user_profile(valid_user.id, dict(name='Franz', address='Somestreet 69'))

        # test if changed user is different from original user
        assert result != original_user
        # test if changes have been incorporated successfully
        assert [result] == mocked_load_users.return_value


def test_exception_error_404_must_be_raised_if_user_nonexistent():
    with patch('class_social.db.load_users') as mocked_load_users:
        valid_user = User(id='c1', name='Mathias', username='mathias', password='somepass', email='mathias@mathias',
                          created_on="2023-03-27T00:00:00.000+00:00", is_active=True, address='some_address')
        mocked_load_users.return_value = users_list
        controller = UserController()
        controller.side_effect = HTTPException(status_code=404)

        with pytest.raises(HTTPException):
            controller.edit_user_profile(valid_user, dict(name='Franz', address='Somestreet 69'))


def test_confirm_associations_operation_if_they_are_association_requests_clear_associations_requests_return_done():
    controller = UserController()
    controller.confirm_associations(institution_association_request_non_empty_list)
    assert institution_association_request_non_empty_list.association_requests == []
    assert institution_association_request_non_empty_list.associates != []


def test_confirm_associations_operation_if_teacher_or_student_associated_is_not_in_attribute_institution_fails():
    controller = UserController()

    controller.confirm_associations(institution_association_request_non_empty_list_1)
    assert student_with_an_institution_associated.institution == institution_associated_with_a_user


def test_confirm_associations_operation_if_institution_have_no_association_requests_fails():
    with patch('class_social.users.user_controller') as mocked_user_controller:
        mocked_user_controller.confirm_associations.side_effect = TypeError

        controller = UserController()

        with pytest.raises(UserControllerError):
            controller.confirm_associations(institution_with_no_associates_requests_at_all)