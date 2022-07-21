# from rest_framework import serializers
from rest_framework.serializers import HyperlinkedModelSerializer, HyperlinkedRelatedField

from posts.models import Post, User, Comment


class PostSerializer(HyperlinkedModelSerializer):
    creator = HyperlinkedRelatedField(
        queryset=User.objects.all(), many=True,
        view_name='user-detail')
    comments = HyperlinkedRelatedField(
        queryset=Comment.objects.all(), many=True,
        view_name='comment-detail')
    likes_for_this_post = HyperlinkedRelatedField(
        queryset=User.objects.all(), many=True,
        view_name='user-detail')
    shares_for_this_post = HyperlinkedRelatedField(
        queryset=User.objects.all(), many=True,
        view_name='user-detail')

    class Meta:
        model = Post
        fields = ['url', 'title', 'content', 'creator', 'type_of_post', 'likes_for_this_post', 'shares_for_this_post', 'creation_date', 'comments', ]


class CommentSerializer(HyperlinkedModelSerializer):
    user = HyperlinkedRelatedField(
        queryset=User.objects.all(), many=True,
        view_name='user-detail')
    post = HyperlinkedRelatedField(
        queryset=Post.objects.all(), many=True,
        view_name='post-detail')

    class Meta:
        model = Comment
        fields = ['url', 'user', 'content', 'post', 'commented_date', ]


class UserSerializer(HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ['url',  'name', ]


