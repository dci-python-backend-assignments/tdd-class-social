# from django.shortcuts import render
# from rest_framework.request import Request
# from rest_framework.response import Response
# from rest_framework.views import APIView

from posts.models import Post, User, Comment
from rest_framework.viewsets import ModelViewSet
# from rest_framework import permissions, status, filters
from posts.serializers import PostSerializer, UserSerializer, CommentSerializer


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


class UserViewSet(ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


# class CommentViewSet(ModelViewSet):
#     """
#     API endpoint that allows groups to be viewed or edited.
#     """
#     queryset = Comment.objects.all()
#     serializer_class = CommentSerializer


# class BookApiView(APIView):
#     def post(self, request: Request):
#         # logger.info(request.data)
#         serializer = BookSerializer(data=request.data)
#         if serializer.is_valid():
#             return Response(data=request.data)
#         else:
#             return Response(data=serializer.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
#
#     def get(self, request: Request):
#         # logger.info('GET received ..')
#         # queryset = Book.objects.all()
#         # serializer = BookSerializer(initial=queryset)
#         # return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response({'message': 'Hi'}, status=status.HTTP_200_OK)
