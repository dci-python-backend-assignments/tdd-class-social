from rest_framework.serializers import HyperlinkedModelSerializer

from user_mgmt.models import BaseUser, Institution, Student, Teacher


class BaseUserSerializer(HyperlinkedModelSerializer):

    class Meta:
        model = BaseUser
        fields = ['id', 'username', 'password', 'email', 'created_on', 'is_active', 'address',
                  'website', 'about', 'connections', 'url']

class InstitutionSerializer(HyperlinkedModelSerializer):

    class Meta:
        model = Institution
        fields = ['id', 'username', 'password', 'email', 'created_on', 'is_active', 'address', 'phone_number', 'avatar',
                  'website', 'about', 'url', 'name', 'head_of_organization', 'research_institution', 'education_institution']


class StudentSerializer(HyperlinkedModelSerializer):

    class Meta:
        model = Student
        fields = '__all__'


class TeacherSerializer(HyperlinkedModelSerializer):

    class Meta:
        model = Teacher
        fields = '__all__'
