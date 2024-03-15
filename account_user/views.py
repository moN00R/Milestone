from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from account_user.models import User_info
from .serializers import UserinfoSerializer, LoginSerializer
from rest_framework.permissions import IsAuthenticated
from milstone.settings import REST_FRAMEWORK
from rest_framework_simplejwt.views import TokenObtainPairView


class get_user_info(ModelViewSet):
    http_method_names = ['post']
    queryset = User_info.objects.all()
    serializer_class = UserinfoSerializer
    permission_classes = [IsAuthenticated]


class login(TokenObtainPairView):
    http_method_names = ['post']
    queryset = User_info.objects.all()
    serializer_class = LoginSerializer
    permission_classes = []
    
    def perform_authentication(self, request):
        return super().perform_authentication(request)
