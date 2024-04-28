import requests
from rest_framework.viewsets import ModelViewSet, generics
from account_user.models import User_info, UserData
from account_user.serializers import UserinfoSerializer, LoginSerializer, GetUserInfoSerializer, ChangePasswordSerializer
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response


class SignUpView(ModelViewSet):
    http_method_names = ('post', )
    permission_classes = [IsAdminUser]
    queryset = User_info.objects.all()
    serializer_class = UserinfoSerializer


class LoginView(TokenObtainPairView):
    http_method_names = ('post', )
    queryset = User_info.objects.all()
    serializer_class = LoginSerializer
    permission_classes = ()


class GetUserInfoView(generics.RetrieveAPIView):
    http_method_names = ('get', )
    permission_classes = [IsAuthenticated]
    queryset = UserData.objects.all()
    serializer_class = GetUserInfoSerializer

    def retrieve(self, request, *args, **kwargs):
        student = self.request.user
        url = f'https://milestone.erpnext-syr.com/api/method/ebx_milestone.apis.get_student_programs?student_id={student.username}'
        headers = {'Authorization': f'token d5b1dcd838aad11:84d91436b74a1c7'}
        user_info_request = requests.get(url, headers=headers)
        user_info_response = user_info_request.json()
        user_info = [user_info_response['message'][0]]
        
        assessment_result_id = user_info[0]['assessment_result_id']
        url2 = f'https://milestone.erpnext-syr.com/api/method/ebx_milestone.apis.get_assessment_result?assessment_result={assessment_result_id}'
        headers = {'Authorization': f'token d5b1dcd838aad11:84d91436b74a1c7'}
        user_mark_request = requests.get(url2, headers=headers)
        user_mark_response = user_mark_request.json()
        user_mark = [user_mark_response["message"]]
        data = {'user_info':user_info, 'user_mark': user_mark}
        return Response(data)


class ChangePasswordView(generics.UpdateAPIView):
    permission_classes = (IsAuthenticated, )
    queryset = User_info.objects.all()
    serializer_class = ChangePasswordSerializer

    def get_object(self):
        return self.request.user
