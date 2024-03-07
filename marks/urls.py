from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers
from . import views

router = routers.DefaultRouter()

router.register('mark', views.StudentMarkView)

urlpatterns = router.urls + [
    
]
