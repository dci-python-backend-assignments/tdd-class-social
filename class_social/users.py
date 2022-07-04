from fastapi import APIRouter, HTTPException

from class_social import db
from class_social.db import DBException
from class_social.models import User


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
    def edit_user_profile(self, user, changes):
        id_ = user.id
        if get_user_by_id(id_) is None:
            raise HTTPException(status_code=404)
        try:
            if isinstance(user, User) and type(changes) == dict:
                for attribute, new_value in changes.items():
                    setattr(user, attribute, new_value)
                return user
            else:
                raise UserControllerError('Error wrong input type')
        except UserControllerError:
            raise UserControllerError('Error wrong input type')

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

# edit user profile by providing dict with changes
@users_routes.patch('/users')
def edit_user_profile(user: User, changes: dict) -> User:
    user = user_controller.edit_user_profile(user, changes)
    return user
