from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers
from django.urls import path, include
from . import views

router = routers.DefaultRouter()

router.register('course', views.CourseView)

router.register('sub', views.BookingCourseView)

urlpatterns = router.urls + [

]
