from rest_framework_nested import routers
from . import views
from django.urls import path

router = routers.DefaultRouter()
router.register(
    'user/<name:char>/<ERB_Student_Id:char>/<phonenumber:char>/<password:char>', views.get_user_info)

urlpatterns = router.urls + [

]
