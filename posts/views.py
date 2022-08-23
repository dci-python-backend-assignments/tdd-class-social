from posts.models import Post, Comment
from rest_framework.viewsets import ModelViewSet
from posts.serializers import CommentSerializer, PostSerializer


class PostViewSet(ModelViewSet):
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
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
