from fastapi import APIRouter, HTTPException
from class_social import db
from class_social.db import DBException
from class_social.models import User

# ------------Controller-----------------


class UserControllerError(Exception):
    pass


# since the self was not used inside the UserController methods we created @static methods out of them
class UserController:
    @staticmethod
    def insert_users(user):
        try:
            user_list = db.load_users()
            user_list.append(user)
            db.save_users(user_list)
        except DBException:
            raise UserControllerError('Error trying to save users in the DB')

    @staticmethod
    def get_user_by_id(id):
        users_list = db.load_users()
        for user in users_list:
            if user.id == id:
                return user
        return None

    @staticmethod
    def get_users():
        try:
            return db.load_users()

        except DBException:
            raise UserControllerError('Error trying to load users from DB')


# ---------------API Routes-------------------

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
