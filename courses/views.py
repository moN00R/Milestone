from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import CourseType, Course, Subscription
from .serializers import CourseTypeserializer, CoursesSerializer, BookingSerializer


class GetCourseTypeView(ModelViewSet):
    http_method_names = ('get', )
    permission_classes = ()
    queryset = CourseType.objects.all()
    serializer_class = CourseTypeserializer

class GetCoursesView(ModelViewSet):
    http_method_names = ('get',)
    permission_classes = ()
    queryset = Course.objects.select_related('category').filter(active=True)
    serializer_class = CoursesSerializer


class BookingCourseView(ModelViewSet):
    http_method_names = ('post', 'get')
    queryset = Subscription.objects.select_related('course').filter(course__active=True, course__open_to_booking=True)
    permission_classes = ()
    serializer_class = BookingSerializer

    
    
