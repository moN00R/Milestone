from rest_framework_nested import routers
from .views import *
from django.urls import include, path

router = routers.DefaultRouter()

router.register('get', get_user_info, basename='get')
# router.register('login', login, basename='login')

urlpatterns = router.urls + [
    path('login/', login.as_view(), name='login'),
    path('', include(router.urls))
]
