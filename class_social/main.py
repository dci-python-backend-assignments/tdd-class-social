import uvicorn
from fastapi import FastAPI

from class_social.users import users_routes

app = FastAPI()
app.include_router(users_routes)


if __name__ == '__main__':

    uvicorn.run(app='class_social.main:app')
