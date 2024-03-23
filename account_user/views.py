import requests
from rest_framework.viewsets import ModelViewSet, generics
from account_user.models import User_info, UserData
from account_user.serializers import UserinfoSerializer, LoginSerializer, GetUserInfoSerializer
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from django.http import JsonResponse


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


class GetUserInfo(generics.RetrieveAPIView):
    http_method_names = ['get']
    queryset = UserData.objects.all()
    serializer_class = GetUserInfoSerializer
    permission_classes = [IsAuthenticated]

    def retrieve(self, request, *args, **kwargs):
        student = self.request.user
        url = f'https://milestone.erpnext-syr.com/api/method/ebx_milestone.apis.get_student_programs?student_id={student.username}'
        headers = {'Authorization': f'token d5b1dcd838aad11:84d91436b74a1c7'}
        info_response = requests.get(url, headers=headers)
        user_info_response = info_response.json()

        assessment_result = user_info_response['message'][0]['assessment_result_id']
        url2 = f'https://milestone.erpnext-syr.com/api/method/ebx_milestone.apis.get_assessment_result?assessment_result={assessment_result}'
        user_mark = requests.get(url2, headers=headers)
        user_mark_response = user_mark.json()

        data = [user_info_response, user_mark_response]
        return Response(data)
