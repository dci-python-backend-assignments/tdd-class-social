from rest_framework import generics
from rest_framework.viewsets import ModelViewSet

from user_mgmt.models import BaseUser, Institution, Student, Teacher
from user_mgmt.serializers import BaseUserSerializer, InstitutionSerializer, StudentSerializer, TeacherSerializer, \
    UpdateSerializer


class BaseUserViewSet(ModelViewSet):
    queryset = BaseUser.objects.all()
    serializer_class = BaseUserSerializer


class InstitutionViewSet(ModelViewSet):
    queryset = Institution.objects.all()
    serializer_class = InstitutionSerializer


class RegisterInstitution(generics.CreateAPIView):
    queryset = Institution.objects.all()
    serializer_class = InstitutionSerializer

    def create(self, validated_data):
        institution = Institution(**validated_data)
        institution.save()
        return institution


class UpdateBaseUser(generics.UpdateAPIView):
    queryset = BaseUser.objects.all()
    serializer_class = UpdateSerializer

    def update(self, validated_data):
        user = BaseUser(**validated_data)
        user.save()
        return user


class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class TeacherViewSet(ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
