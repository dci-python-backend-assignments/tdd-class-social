import uvicorn
from fastapi import FastAPI

from class_social.users import users_routes
from class_social.posts import posts_routes

app = FastAPI()
app.include_router(users_routes)
app.include_router(posts_routes)


if __name__ == '__main__':
    uvicorn.run(app='class_social.main:app')
