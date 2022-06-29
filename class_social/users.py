from fastapi import APIRouter, HTTPException

from class_social import db
from class_social.db import DBException
from class_social.models import User

from collections import namedtuple


class UserControllerError(Exception):
    pass


class UserController:

    def insert_users(self, user):
        try:
            user_list = db.load_users()
            user_list.append(user)
            db.save_users(user)
        except DBException:
            raise UserControllerError('Error trying to save users in the DB')

    def get_user_by_id(self, id):
        users_list = db.load_users()
        for user in users_list:
            if user.id == id:
                return user
        return None

    def get_users(self):
        try:
            db.load_users()
        except DBException:
            raise UserControllerError('Error trying to load users from DB')

    # edit user profile
    def edit_user_profile(self, user):

        profile_to_edit = dict(user)
        for k, v in profile_to_edit.items():
            if k == 'name':
                profile_to_edit[k] = 'Franz'
        db.save_users(user)
        user = namedtuple("User", profile_to_edit.keys())(*profile_to_edit.values())

        return user

        # API Routes

users_routes = APIRouter()
user_controller = UserController()


@users_routes.post('/users')
def post_users(user: User) -> User:
    user = user_controller.insert_users(user)
    return user


@users_routes.get('/users')
def get_users():
    users = user_controller.get_users()
    return users


@users_routes.get('/users/{id}')
def get_user_by_id(id: str):
    user = user_controller.get_user_by_id(id)

    if user is not None:
        return user

    raise HTTPException(status_code=404)

# edit user profile
@users_routes.patch('/users')
def edit_user_profile(user: User) -> User:
    user = user_controller.edit_user_profile(user)
    return user