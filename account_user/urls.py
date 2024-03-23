from rest_framework_nested import routers
from .views import *
from django.urls import include, path

router = routers.DefaultRouter()

router.register('signup', SignUp, basename='signup')
# router.register('get_inf', GetUserInfo, basename='get_info')
# router.register('login', login, basename='login')

urlpatterns = router.urls + [
    path('login/', login.as_view(), name='login'),
    # path('get_user_info/',
    #  get_user_info.as_view({'get': 'list'}), name='get_user_info'),
    path('', include(router.urls))
]
