import uvicorn
from fastapi import FastAPI

from class_social.users import users_routes
from class_social.posts import posts_routes
from class_social.auth import auth_routes

app = FastAPI()
app.include_router(users_routes)  # comment it out to pass the first test auth routes
app.include_router(posts_routes)  # comment it out to pass the first test auth routes
app.include_router(auth_routes)

if __name__ == '__main__':
    uvicorn.run(app='class_social.main:app')