import requests
from rest_framework.viewsets import ModelViewSet, generics
from account_user.models import User_info
from .serializers import UserinfoSerializer, LoginSerializer
from rest_framework.permissions import IsAdminUser
from rest_framework_simplejwt.views import TokenObtainPairView


class SignUp(ModelViewSet):
    http_method_names = ['post']
    queryset = User_info.objects.all()
    serializer_class = UserinfoSerializer
    permission_classes = [IsAdminUser]


class login(TokenObtainPairView):
    http_method_names = ['post']
    queryset = User_info.objects.all()
    serializer_class = LoginSerializer
    permission_classes = []


# class GetUserInfo(generics.ListAPIView):
#     permission_classes = []
#     queryset = User_info.objects.all()

#     def list(self, request, *args, **kwargs):
#         # student = self.request.user
#         url = f'https://milestone.erpnext-syr.com/api/method/ebx_milestone.apis.get_assessment_result?assessment_result=EDU-RES-2024-00008'
#         headers = {'Authorization': f'token d5b1dcd838aad11:84d91436b74a1c7'}
#         response = requests.get(url, headers=headers)
#         response_data_student = response.json
#         print(response_data_student)
#         return requests.Response(response_data_student)
