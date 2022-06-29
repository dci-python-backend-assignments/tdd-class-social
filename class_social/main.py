import uvicorn
from fastapi import FastAPI

from class_social.models import User
from class_social.users import users_routes, edit_user_profile2

app = FastAPI()
app.include_router(users_routes)


if __name__ == '__main__':

    valid_user = User(id='c1', name='Mathias', username='mathias', password='somepass', email='mathias@mathias', created_on="2023-03-27T00:00:00.000+00:00", is_active=True, address='some_address')

    edit_user_profile2(valid_user)

    #uvicorn.run(app='class_social.main:app')
