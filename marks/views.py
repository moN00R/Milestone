from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import StudentMark
from .serializers import StudentMarksSerializer
# Create your views here.


class StudentMarkView(ModelViewSet):
    queryset = StudentMark.objects.all()
    serializer_class = StudentMarksSerializer
    permission_classes = [IsAuthenticated]
