from rest_framework_nested import routers
from books.views import *
from django.urls import include, path


router = routers.DefaultRouter()

router.register('books', LibraryView, basename='books')

urlpatterns = router.urls
