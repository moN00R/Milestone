from rest_framework import serializers
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import User_info
from django.contrib.auth.hashers import make_password


class UserinfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_info
        fields = ['name', 'username', 'phonenumber', 'password']

    def create(self, validated_data):
        user = User_info.objects.create(
            name=validated_data['name'],
            username=validated_data['username'],
            phonenumber=validated_data['phonenumber'],
            password=make_password(validated_data['password'])
        )
        return user


class LoginSerializer(TokenObtainPairSerializer):
    # username = serializers.CharField(required=True)
    # password = serializers.CharField(required=True)

    class Meta:
        model = User_info
        fields = ['username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        user = User_info.objects.filter(username=username).first()

        if not user:
            raise AuthenticationFailed('User not found')

        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect password')

        return super().validate(attrs)


# class GetUserInfo(serializers.ModelSerializer):
#     ERD_Student_Id = serializers.CharField(max_length=)

#     url = f'https://milestone.erpnext-syr.com/api/method/ebx_milestone.apis.get_student_programs?student_id={ERD_Student_Id}'
#     response = requests.get(url)
#     response_data = response.json()
