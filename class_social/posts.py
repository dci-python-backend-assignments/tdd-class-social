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

