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
        fields = ['username', 'password', 'email']

    def create(self, validated_data):
        institution = Institution(**validated_data)
        institution.save()
        return institution

class StudentSerializer(HyperlinkedModelSerializer):

    class Meta:
        model = Student
        fields = '__all__'


class TeacherSerializer(HyperlinkedModelSerializer):

    class Meta:
        model = Teacher
        fields = '__all__'


