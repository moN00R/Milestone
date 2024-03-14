from rest_framework_nested import routers
from . import views
from django.urls import path

router = routers.DefaultRouter()
router.register('', views.get_user_info)

urlpatterns = router.urls + [
    # path('', views.get_user_info, name='get_user_info'),
]
