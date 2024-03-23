from rest_framework import serializers
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import User_info, UserData
from django.contrib.auth.hashers import make_password
import requests


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


class GetUserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserData
        fields = ['assessment_result_id',
                  'program', 'program_group',
                  'instructor',
                  'student_group_date'
                  ]

    extra_kwargs = {'assessment_result_id': {'read_only': True},
                    'program': {'read_only': True},
                    'program_group': {'read_only': True},
                    'instructor': {'read_only': True},
                    'student_group_date': {'read_only': True}}

    assessment_result_id = serializers.CharField(max_length=100)
    program = serializers.CharField(max_length=100)
    program_group = serializers.CharField(max_length=100)
    instructor = serializers.CharField(max_length=100)
    student_group_date = serializers.DateField
