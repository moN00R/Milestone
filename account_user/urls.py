from rest_framework_nested import routers
from .views import *
from django.urls import include, path

router = routers.DefaultRouter()

router.register('signup', SignUp, basename='signup')
# router.register('get_user_info', GetUserInfo, basename='get_user_info')


urlpatterns = router.urls + [
    path('login/', login.as_view(), name='login'),
    path('profil/', GetUserInfo.as_view(), name='get_user_info'),
    path('', include(router.urls))
]
