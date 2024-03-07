from rest_framework_nested import routers
from . import views
from django.urls import path

router = routers.DefaultRouter()
router.register('User', views.get_user )

urlpatterns = router.urls + [
    # path('User/', views.User_info),
]
