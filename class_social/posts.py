from fastapi import HTTPException, APIRouter

from class_social import db
from class_social.models import Post
from class_social.db import DBException

class PostControllerError(Exception):
    pass

class PostController:

    def post_a_post(self, post):
        try:
            post_list = db.load_posts()
            post_list.append(post)
            db.save_posts(post_list)
        except DBException:
            raise PostControllerError('Wrong format')


post_routes = APIRouter()
post_controller = PostController()

@post_routes.post('/posts')
def insert_posts(post: Post) -> Post:
    post = post_controller.post_a_post(post)
