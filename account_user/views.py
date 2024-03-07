from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import UserinfoSerializer
from .models import User_info
# Create your views here.


class get_user(ModelViewSet):
    http_method_names = ['get']
    queryset = User_info.objects.all()
    serializer_class = UserinfoSerializer
    permission_classes = ()
