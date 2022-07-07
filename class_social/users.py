from fastapi import APIRouter, HTTPException

from pydantic import ValidationError
from class_social import db
from class_social.db import DBException
from class_social.models import User


class UserControllerError(Exception):
    def __init__(self, message):
        self.message = message


class UserController:

    def insert_users(self, user):
        try:
            if self.is_email_in_database(user) is False:
                user_list = db.load_users()
                user_list.append(user)
                db.save_users([user for user in user_list])
            else:
                raise UserControllerError("Email already exists")
        except DBException:
            raise UserControllerError('Error trying to save users in the DB')


    def get_user_by_id(self, id):
        users_list = db.load_users()
        for user in users_list:
            if user.id == id:
                return user
        return None


    def get_user_by_is_active(self, id):
        try:
            users_list = db.load_users()
            for user in users_list:
                if user.id == id and user.is_active is True:
                    return user
        except:
            raise ValidationError("The information is not boolean")


    def get_users(self):
        try:
            return db.load_users()
        except DBException:
            raise UserControllerError('Error trying to load users from DB')

    def is_email_in_database(self, email):
        users_list = db.load_users()
        for user in users_list:
            if user.email == email:
                return True   
        return False


# API Routes

users_routes = APIRouter()
user_controller = UserController()


@users_routes.post('/users')
def post_users(user: User) -> User:
    try:
        user = user_controller.insert_users(user)
        return user
    except UserControllerError as e:
        raise HTTPException(status_code=400, detail=e.message)


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


@users_routes.get('/users/{id}/is_active')
def get_user_is_active_to_be_true(id: str):
    user = user_controller.get_user_by_is_active(id)

    if user.is_active is True:
        return user

    raise HTTPException(status_code=404)

