from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from user_mgmt.models import BaseUser, Student, Institution
from user_mgmt.serializers import BaseUserSerializer, StudentSerializer, InstitutionSerializer


class BaseUserViewSet(ModelViewSet):
    queryset = BaseUser.objects.all()
    serializer_class = BaseUserSerializer


class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class InstitutionViewSet(ModelViewSet):
    queryset = Institution.objects.all()
    serializer_class = InstitutionSerializer

    def get_queryset(self):
        search_term = self.request.query_params.get('search_institution')
        if search_term:
            queryset = Institution.objects.filter(title__contains=search_term)
        else:
            queryset = Institution.objects.all()

        return queryset

#
# class InstitutionApiView(APIView):
#
#     def post(self, request: Request):
#         serializer = BookSerializer(data=request.data)
#         if serializer.is_valid():
#             return Response(data=request.data)
#         else:
#             return Response(data=serializer.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
#
#     def get(self, request: Request):
#         return Response(data="Hello World!", status=status.HTTP_200_OK)
