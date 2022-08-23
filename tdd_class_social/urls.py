from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from posts.views import PostViewSet, CommentViewSet
from user_mgmt.views import BaseUserViewSet
router = DefaultRouter()
router.register(r'users', BaseUserViewSet)
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
