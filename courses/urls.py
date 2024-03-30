from rest_framework_nested import routers
from courses.views import *
from django.urls import include, path


router = routers.DefaultRouter()

router.register('category', GetCourseTypeView, basename='category')
router.register('course', GetCoursesView, basename='course')

urlpatterns = router.urls 
