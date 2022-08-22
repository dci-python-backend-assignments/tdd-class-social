# from rest_framework import serializers
from rest_framework.serializers import HyperlinkedModelSerializer, HyperlinkedRelatedField

from posts.models import Post, User, Comment, Profile, FollowersCount


class UserSerializer(HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = '__all__'


class ProfileSerializer(HyperlinkedModelSerializer):
    # User = HyperlinkedRelatedField(
    #     queryset=User.objects.all(), many=False,
    #     view_name='user-detail')

    class Meta:
        model = Profile
        fields = '__all__'


class PostSerializer(HyperlinkedModelSerializer):
    creator = HyperlinkedRelatedField(
        queryset=User.objects.all(), many=False,
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
        # fields = ['url', 'title', 'content', 'creator', 'type_of_post', 'likes_for_this_post', 'shares_for_this_post', 'creation_date', 'comments', ]
        # fields = ['url', '__all__', 'comments', 'shares_for_this_post' ]
        fields = '__all__'


class CommentSerializer(HyperlinkedModelSerializer):
    user = HyperlinkedRelatedField(
        queryset=User.objects.all(), many=False,
        view_name='user-detail')
    post = HyperlinkedRelatedField(
        queryset=Post.objects.all(), many=False,
        view_name='post-detail')
    likes = HyperlinkedRelatedField(
        queryset=User.objects.all(), many=True,
        view_name='user-detail')
    reply = HyperlinkedRelatedField(
        queryset=User.objects.all(), many=True,
        view_name='user-detail')

    class Meta:
        model = Comment
        # fields = ['url', 'user', 'content', 'post', 'commented_date', ]
        fields = '__all__'


class FollowersCountSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = FollowersCount
        fields = '__all__'


