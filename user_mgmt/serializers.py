from rest_framework.serializers import HyperlinkedModelSerializer

from user_mgmt.models import BaseUser


class BaseUserSerializer(HyperlinkedModelSerializer):

    class Meta:
        model = BaseUser
        fields = ['id', 'username', 'password', 'email', 'created_on', 'is_active', 'address',
                  'website', 'about', 'connections', 'url']
