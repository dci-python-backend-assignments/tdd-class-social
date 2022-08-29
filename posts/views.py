from rest_framework import generics
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from posts.serializers import *
from user_mgmt.serializers import *


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostByRole(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    # renderer_classes = [TemplateHTMLRenderer]

    def get(self, request, *args, **kwargs):
        if kwargs == {'role': 'students'}:
            print('role is student')
            student_ids = Student.objects.values_list('baseuser_ptr_id')
            student_posts = Post.objects.filter(creator__id__in=student_ids)
            serializer = PostSerializer(student_posts, many=True, context={'request': request})
            return Response({"student_posts": serializer.data}, template_name='posts/posts_by_role.html')
        elif kwargs == {'role': 'teachers'}:
            print('role is teacher')
            teacher_ids = Teacher.objects.values_list('baseuser_ptr_id')
            teacher_posts = Post.objects.filter(creator__id__in=teacher_ids)
            serializer = PostSerializer(teacher_posts, many=True, context={'request': request})
            return Response({"teacher_posts": serializer.data}, template_name='posts/posts_by_role.html')
        elif kwargs == {'role': 'institutions'}:
            print('role is institution')
            institution_ids = Institution.objects.values_list('baseuser_ptr_id')
            institution_posts = Post.objects.filter(creator__id__in=institution_ids)
            serializer = PostSerializer(institution_posts, many=True, context={'request': request})
            return Response({"institution_posts": serializer.data}, template_name='posts/posts_by_role.html')
        else:
            serializer = PostSerializer([], many=True, context={'request': request})
            return Response({"No Posts by this role yet": serializer.data}, template_name='posts/posts_by_role.html')


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
