from fastapi import APIRouter
from pydantic import BaseModel


class UserModel(BaseModel):
    id: str
    name: str
    email: str
    password: str


class UserController:
    def get_users(self):
        pass


# API Routes

users_routes = APIRouter()
user_controller = UserController()


@users_routes.get('/users')
def get_users():
    users = user_controller.get_users()
    return users
