from django.contrib import admin
from posts.models import Post, Comment

admin.site.register(Post)
admin.site.register(Comment)