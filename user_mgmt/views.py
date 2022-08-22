from rest_framework.viewsets import ModelViewSet

from user_mgmt.models import BaseUser
from user_mgmt.serializers import BaseUserSerializer


class BaseUserViewSet(ModelViewSet):
    queryset = BaseUser.objects.all()
    serializer_class = BaseUserSerializer
