from django.shortcuts import render
from .models import Library
from .serializers import GetBookesSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated


class LibraryView(ModelViewSet):
    http_method_names = ('get', )
    permission_classes =(IsAuthenticated, ) 
    queryset = Library.objects.filter(publish=True)
    serializer_class = GetBookesSerializer
