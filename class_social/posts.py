<<<<<<< HEAD
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
=======
from fastapi import APIRouter, HTTPException
from class_social import db
from class_social.db import DBException


class PostControllerError(Exception):
    pass


class PostController:
    def get_posts_by_creator_role(self, role):
        result_post = []

        posts_list = db.load_posts()

        for post in posts_list:

            if post.creator.role == role:

                 result_post.append(post)

        return result_post



# API Routes

posts_routes = APIRouter()
post_controller = PostController()


@posts_routes.get('/posts/creator/{role}')
def get_posts_by_creator_role(role: str):
    post = post_controller.get_posts_by_creator_role(role)

    if post is not None:
        return post

    raise HTTPException(status_code=404)

>>>>>>> 37639a09d642612441a8e0b51125b116e1a17e87
