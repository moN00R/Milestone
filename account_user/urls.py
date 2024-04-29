from rest_framework_nested import routers
from account_user.views import *
from django.urls import include, path

router = routers.DefaultRouter()

router.register('signup', SignUpView, basename='signup')

urlpatterns = router.urls + [
    path('login/', LoginView.as_view(), name='login'),
    path('profile/', GetUserInfoView.as_view(), name='get_user_info'),
    path('get-user-info-details/<str:assessment_result>', GetUserDetailsCourse.as_view(), name='Get_user_info_details'),
    path('change-password/', ChangePasswordView.as_view(), name='change_password'),
    path('', include(router.urls))
]
