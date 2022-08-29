from rest_framework.serializers import HyperlinkedModelSerializer, HyperlinkedRelatedField
from posts.models import Post, Comment
from user_mgmt.models import BaseUser


class PostSerializer(HyperlinkedModelSerializer):
    creator = HyperlinkedRelatedField(
        queryset=BaseUser.objects.all(), many=False,
        view_name='baseuser-detail')
    comments = HyperlinkedRelatedField(
        required=False,
        queryset=Comment.objects.all(), many=True,
        view_name='comment-detail')

    class Meta:
        model = Post
        fields = ['url', 'title', 'content', 'creator', 'type_of_post', 'likes', 'shares', 'saves', 'created_at',
                  'comments', 'updated_at', 'attachments']


class CommentSerializer(HyperlinkedModelSerializer):
    user = HyperlinkedRelatedField(
        queryset=BaseUser.objects.all(), many=False,
        view_name='baseuser-detail')
    post = HyperlinkedRelatedField(
        queryset=Post.objects.all(), many=False,
        view_name='post-detail')
    likes = HyperlinkedRelatedField(
        queryset=BaseUser.objects.all(), many=True,
        view_name='user-detail')

    class Meta:
        model = Comment
        fields = ['url', 'user', 'content', 'post', 'commented_date', 'likes']
