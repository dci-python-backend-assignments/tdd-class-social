from rest_framework.viewsets import ModelViewSet

from social.models import BaseUser
from social.serializers import BaseUserSerializer


class BaseUserViewSet(ModelViewSet):
    queryset = BaseUser.objects.all()
    serializer_class = BaseUserSerializer
