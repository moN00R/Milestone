from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import *
from .serializers import *


# to get all courses in the course page
class CourseView(ModelViewSet):
    http_method_names = 'get'
    queryset = Course.objects.filter(active=True)
    serializer_class = CourseSerializer
    permission_classes = ()

# to book for course and get a subscription for a user and delete it


class BookingCourseView(ModelViewSet):
    queryset = Subscription.objects.all()
    http_method_names = ['post', 'get', 'delete']
    serializer_class = SubscriptionSerializer
    permission_classes = [IsAuthenticated]

# class StudentMarkView(ModelViewSet):
#     serializer_class = [StudentMarkSerializer]
#     permission_classes = [IsAuthenticated]

#     def get_queryset(self):
#         return self.request.user

#     def get_serializer_context(self):
#         context = super().get_serializer_context()
#         context['user'] = self.request.user
#         return context

#     queryset = Subscription.objects.all()
