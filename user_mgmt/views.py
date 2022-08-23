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
        def get_queryset(self):
            search_term = self.request.query_params.get('search_terms')
            if search_term:
                queryset = Book.objects.filter(title__contains=search_term)
            else:
                queryset = Book.objects.all()

            return queryset





