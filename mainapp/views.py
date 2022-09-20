from rest_framework.viewsets import ModelViewSet

from mainapp.models import User
from mainapp.serializers import UserSerializer


class UserView(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

