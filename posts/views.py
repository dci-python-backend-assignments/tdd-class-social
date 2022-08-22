# from django.shortcuts import render
# from rest_framework.request import Request
# from rest_framework.response import Response
# from rest_framework.views import APIView

from posts.models import Post, User, Comment, Profile, FollowersCount
from rest_framework.viewsets import ModelViewSet
# from rest_framework import permissions, status, filters
from posts.serializers import UserSerializer, ProfileSerializer, FollowersCountSerializer, CommentSerializer, PostSerializer


class UserViewSet(ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ProfileViewSet(ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class FollowersCountVieSet(ModelViewSet):
    queryset = FollowersCount.objects.all()
    serializer_class = FollowersCountSerializer


class PostViewSet(ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_queryset(self):
        search_term = self.request.query_params.get('search_terms')
        if search_term:
            queryset = Post.objects.filter(creotor__contains=search_term)
        else:
            queryset = Post.objects.all()
        return queryset


class CommentViewSet(ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


