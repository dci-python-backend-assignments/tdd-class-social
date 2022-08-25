from posts.models import Post, Comment
from rest_framework.viewsets import ModelViewSet
from posts.serializers import CommentSerializer, PostSerializer
from user_mgmt.models import *


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_queryset(self):
        queryset = Post.objects.all()
        search_key = list(self.request.query_params.keys())
        if not search_key:
            return queryset
        elif search_key[0] == 'posts_by':
            search_term = self.request.query_params.get(search_key[0])

            if search_term == "students":
                Student_ids = Student.objects.values_list('baseuser_ptr_id')
                queryset = Post.objects.filter(creator__id__in=Student_ids)
            elif search_term == "teachers":
                Teacher_ids = Teacher.objects.values_list('baseuser_ptr_id')
                queryset = Post.objects.filter(creator__id__in=Teacher_ids)
            elif search_term == "institutions":  #
                Institution_ids = Institution.objects.values_list('baseuser_ptr_id')
                queryset = Post.objects.filter(creator__id__in=Institution_ids)

            else:
                queryset = []  # Post.objects.all()

            return queryset


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
