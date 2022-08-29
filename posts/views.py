from rest_framework import generics
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from posts.serializers import *
from user_mgmt.serializers import *


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


class PostByRole(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    # renderer_classes = [TemplateHTMLRenderer]

    def get(self, request, *args, **kwargs):
        print(kwargs)
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
