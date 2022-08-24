from rest_framework.relations import HyperlinkedRelatedField
from rest_framework.serializers import HyperlinkedModelSerializer

from user_mgmt.models import BaseUser, Institution, Student


class BaseUserSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = BaseUser
        fields = ['id', 'username', 'password', 'email', 'created_on', 'is_active', 'address',
                  'website', 'about', 'connections', 'url', 'avatar', 'phone_number']


class InstitutionSerializer(HyperlinkedModelSerializer):

    class Meta:
        model = Institution
        fields = ['id', 'username', 'password', 'email', 'created_on', 'is_active', 'address',
                  'website', 'about', 'connections', 'url', 'avatar', 'phone_number', 'name', 'associates',
                  'head_of_organization', 'research_institution','education_institution', 'courses']


class StudentSerializer(HyperlinkedModelSerializer):
    institution = HyperlinkedRelatedField(
        queryset=Institution.objects.all(), many=True,
        view_name='institution-detail')

    class Meta:
        model = Student
        fields = ['url', 'first_name', 'last_name', 'courses', 'institution', 'interests', 'date_of_birth', 'gender']

