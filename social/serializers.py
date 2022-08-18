from rest_framework.serializers import HyperlinkedModelSerializer

from social.models import BaseUser


class BaseUserSerializer(HyperlinkedModelSerializer):

    class Meta:
        model = BaseUser
        fields = ['id', 'username', 'password', 'email', 'is_active', 'address',
                  'website', 'about', 'connections', 'role', 'url']

        # 'created_on'
