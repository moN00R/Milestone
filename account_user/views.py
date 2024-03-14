from rest_framework import status
from requests import Response
from rest_framework.viewsets import ModelViewSet
from account_user.models import User_info
from .serializers import UserinfoSerializer
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated, BasePermission


class get_user_info(ModelViewSet):
    http_method_names = ['post']
    queryset = User_info.objects.all()
    serializer_class = UserinfoSerializer
    permission_classes = [IsAuthenticated]
