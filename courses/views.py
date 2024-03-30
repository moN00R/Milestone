from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import CourseType, Course
from .serializers import CourseTypeserializer, CoursesSerializer


class GetCourseTypeView(ModelViewSet):
    http_method_names = ('get', )
    permission_classes = (IsAuthenticated, )
    queryset = CourseType.objects.all()
    serializer_class = CourseTypeserializer

class GetCoursesView(ModelViewSet):
    http_method_names = ('get',)
    permission_classes = (IsAuthenticated, )
    queryset = Course.objects.filter(active=True)
    serializer_class = CoursesSerializer