from fastapi import APIRouter, HTTPException

from pydantic import ValidationError
from class_social import db
from class_social.db import DBException
from class_social.models import User


class UserControllerError(Exception):
    def __init__(self, message):
        self.message = message

    """since the self was not used inside the UserController methods we 
    created @static methods out of them. This also means we remove the 'self' """


class UserController:

    @staticmethod
    def insert_users(user):
        try:
            if user.is_email_in_database(user) is False:   # changed to comply with static methods.
                user_list = db.load_users()
                user_list.append(user)
                db.save_users([user for user in user_list])
            else:
                raise UserControllerError("Email already exists")
        except DBException:
            raise UserControllerError('Error trying to save users in the DB')

    @staticmethod
    def get_user_by_id_(id_):
        users_list = db.load_users()
        for user in users_list:
            if user.id_ == id_:
                return user
        return None

    @staticmethod
    def get_user_by_is_active(id_):
        try:
            users_list = db.load_users()
            for user in users_list:
                if user.id_ == id_ and user.is_active is True:
                    return user
        except:
            raise ValidationError("The information is not boolean")

    @staticmethod
    def get_users():
        try:
            return db.load_users()
        except DBException:
            raise UserControllerError('Error trying to load users from DB')

    @staticmethod
    def is_email_in_database(email):
        users_list = db.load_users()
        for user in users_list:
            if user.email == email:
                return True
            else:
                return False

# ----------------------------------------------------------------- #20_begin
    @staticmethod
    def get_user_by_username_and_password(self, username, password):
        users_list = db.load_users()
        for user in users_list:
            if user.username == username and user.password == password:
                return user
        return None
# ---------------------------------------------------------------- #20_end

# ----------------------------------------------------------------- #20 to complicate the matter a bit-start
def get_user_password_strong(s):
    users_list = db.load_users()
    for user, password in users_list:
        if len(list(set(s) & set(password.ascii_lowercase))) > 0 and len(
            list(set(s) & set(password.ascii_uppercase))) > 0 and len(list(set(s) & set(password.digits))) > 0 and len(
                list(set(s) & set(password.punctuation))) > 0:
            return "strong"
        else:
            return "weak"

# ----------------------------------------------------------------- #20 to complicate the matter a bit- end
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


@users_routes.get('/users/{id_}')
def get_user_by_id(id_: str):
    user = user_controller.get_user_by_id_(id_)

    if user is not None:
        return user

    raise HTTPException(status_code=404)


@users_routes.get('/users/{id_}/is_active')
def get_user_is_active_to_be_true(id_: str):
    user = user_controller.get_user_by_is_active(id_)

    if user.is_active is True:
        return user

    raise HTTPException(status_code=404)


# --------------------------------------------------------------- #20_begin

@users_routes.get('/users/{username}/{password}')
def get_user_by_username_and_password(username: str, password: str):
    user = user_controller.get_user_by_username_and_password(username, password)

    if user is not None:
        return user
    raise HTTPException(status_code=404)
# --------------------------------------------------------------- #20_end
