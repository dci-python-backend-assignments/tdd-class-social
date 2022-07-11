from typing import Dict, Union, Any
from fastapi import APIRouter, HTTPException
from class_social import db
from class_social.models import User, UserAuthenticate, Token
from datetime import timedelta
import datetime
import bcrypt
import jwt


# -------authentication controller
# These constants go in a specific config file
ACCESS_TOKEN_EXPIRE_MINUTES = 15
SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
JWT_ALGORITHM = "HS256"


class AuthenticationController:
    # for the authentication todo make test for this controller
    @staticmethod
    def get_user_by_username(username):
        users_list = db.load_users()
        for user in users_list:
            if user.username == username:
                return user
        return None

    def check_username_password(self, user: UserAuthenticate):
        db_user: User = self.get_user_by_username(username=user.username)
        if db_user is not None:
            db_pass = db_user.password.encode('utf8')  # this line depends on whether the password is encoded in the
            # user registration--> delete the .encode if necessary and choose the alternative return
            request_pass = user.password.encode('utf8')  # same here
            # return bcrypt.checkpw(request_pass, db_pass)  # todo check why the test case will not pass in case we choose this return?

            # alternative without bcrypt
            if db_pass == request_pass:
                return True
            else:
                return False
        else:
            return False


    @staticmethod
    def encode_jwt_token(*, data: dict, expires_delta: datetime.timedelta = None):

        to_encode = data.copy()
        if expires_delta:
            expire = datetime.datetime.utcnow() + expires_delta
        else:
            expire = datetime.datetime.utcnow() + datetime.timedelta(minutes=15)
        to_encode.update({"exp": expire})

        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=JWT_ALGORITHM)
        print(f"encoded _jwt here {encoded_jwt}")
        return encoded_jwt  # in order to have the jw.encode we need to install the module PyJwT pip install PyJWT


# -----------/users/auth routes ----------------

auth_routes = APIRouter()
auth_controller = AuthenticationController()


# this get method must be deleted not be written but the first test is still needed to prevent unauthorized from getting access
# when they try to type http://127.0.0.1:8000/users/auth

# the tests won't pass even if the method is not implemented if the main includes other routes that have a get method
# @auth_routes.get("/users/auth", status_code=405)
# def get_authentication_info():
#      raise HTTPException(status_code=405, detail="method not allowed") #todo check if the above explanation is correct
#

@auth_routes.post("/users/auth", response_model=Token, tags=["users"])
def post_authenticate_user(user: UserAuthenticate) -> Dict[str, Union[str, Any]]:
    db_user = auth_controller.get_user_by_username(username=user.username)
    if db_user is None:
        raise HTTPException(status_code=403, detail="Username or password is incorrect")
    else:
        is_password_correct = auth_controller.check_username_password(user)
        if is_password_correct is False:
            raise HTTPException(status_code=403, detail="Username or password is incorrect")
        else:
            access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
            access_token = auth_controller.encode_jwt_token(
                data={"sub": user.username}, expires_delta=access_token_expires)
            return {"access_token": access_token, "token_type": "Bearer"}

# This file is missing