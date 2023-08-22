from rest_framework import viewsets
from rest_framework.exceptions import MethodNotAllowed

from django.contrib.auth.models import User

from user.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def destroy(self, request, *args, **kwargs):
        raise MethodNotAllowed('DELETE')
