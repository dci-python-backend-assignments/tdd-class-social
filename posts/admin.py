from django.contrib import admin

from posts.models import Profile, Post, Comment, FollowersCount

# Register your models here.
admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(FollowersCount)
