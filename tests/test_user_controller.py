import datetime
from unittest.mock import patch

import pytest

from class_social.db import DBException
from class_social.models import User, Institution, Student
from class_social.users import UserController, UserControllerError

users_list = [
    User(id='someid', name='Mathias', username='mathias', password='somepass', email='mathias@mathias',
         created_on=datetime.datetime.now(), is_active=True, address="some_address"),
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
                associates=[], association_requests=[student],
                head_of_organization='Mathias',
                research_institution=False, education_institution=True)

institution_association_request_non_empty_list_1 = \
    Institution(id='1', username='institution1', password='124', email='institution1@somee.com',
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


def test_confirm_associations_operation_if_institution_have_no_association_requests_fails():
    with patch('class_social.users.user_controller') as mocked_user_controller:
        mocked_user_controller.confirm_associations.side_effect = TypeError

        controller = UserController()

        with pytest.raises(UserControllerError):
            controller.confirm_associations(institution_with_no_associates_requests_at_all)


def test_confirm_associations_operation_if_the_association_requests_is_an_empty_list_fails():
    with patch('class_social.users.user_controller') as mocked_user_controller:
        mocked_user_controller.confirm_associations.side_effect = UserControllerError

        controller = UserController()

        with pytest.raises(UserControllerError):
            controller.confirm_associations(institution_association_request_list_empty)


def test_confirm_associations_operation_if_they_are_association_requests_clear_associations_requests_return_done():
    controller = UserController()
    result = controller.confirm_associations(institution_association_request_non_empty_list)
    assert institution_association_request_non_empty_list.association_requests == []
    assert institution_association_request_non_empty_list.associates != []
    assert result == 'Done'


def test_confirm_associations_operation_if_teacher_or_student_associated_is_not_in_attribute_institution_fails():
    controller = UserController()

    controller.confirm_associations(institution_association_request_non_empty_list_1)
    assert student_with_an_institution_associated.institution == institution_associated_with_a_user
