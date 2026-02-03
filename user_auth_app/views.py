from rest_framework import generics
from rest_framework.permissions import AllowAny

from .serializers import UserRegistrationSerializer


class RegistrationView(generics.CreateAPIView):
    serializer_class = UserRegistrationSerializer
    permission_classes = [AllowAny]
