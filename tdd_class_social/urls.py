from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.conf.urls.static import static
from posts.views import *
from user_mgmt.views import *

router = DefaultRouter()
router.register(r'users', BaseUserViewSet)
router.register(r'institutions', InstitutionViewSet)
router.register(r'students', StudentViewSet)
router.register(r'teachers', TeacherViewSet)
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('institutions/register', RegisterInstitution.as_view()),
    path('posts_by=<str:role>/', PostByRole.as_view(), name='<str:role>_posts'),
    path('name=<str:name>/', FilterInstitutionViewSet.as_view()),
]

