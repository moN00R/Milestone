from django.shortcuts import get_object_or_404, render
from .serializers import *
from .models import Library
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
# Create your views here.


class LibraryView(ModelViewSet):
    http_method_names = ['get']
    queryset = Library.objects.filter(publish=True)
    serializer_class = LibrarySerializer
    permission_classes = ()
