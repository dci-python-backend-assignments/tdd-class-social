import uvicorn
from fastapi import FastAPI

from class_social.file_importing import upload_router
from class_social.users import users_routes
from class_social.posts import posts_routes

app = FastAPI()
app.include_router(users_routes)    # comment this to pass the first test auth routes
app.include_router(posts_routes)    # comment this to pass the first test auth routes
app.include_router(upload_router)


if __name__ == '__main__':
    uvicorn.run(app='class_social.main:app')
