from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import UserinfoSerializer
from .models import User_info


class get_user_info(ModelViewSet):
    http_method_names = ['get']
    queryset = User_info.objects.all()
    serializer_class = UserinfoSerializer
    permission_classes = ()

    def list(self, request, *args, **kwargs):
        data = super().list(request, *args, **kwargs)
        return data
    
    
    
    

