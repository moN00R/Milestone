from rest_framework import serializers
from rest_framework.exceptions import ValidationError, AuthenticationFailed
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import User_info
from django.contrib.auth.hashers import make_password


class UserinfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_info
        fields = ['name', 'ERP_Student_Id', 'phonenumber', 'password']

    def create(self, validated_data):
        user = User_info.objects.create(
            name=validated_data['name'],
            ERP_Student_Id=validated_data['ERP_Student_Id'],
            phonenumber=validated_data['phonenumber'],
            password=make_password(validated_data['password'])
        )
        return user


class LoginSerializer(TokenObtainPairSerializer):
    # username = serializers.CharField(required=True)
    # password = serializers.CharField(required=True)

    class Meta:
        model = User_info
        fields = ['ERP_Student_Id', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def validate(self, attrs):
        ERP_Student_Id = attrs.get('ERP_Student_Id')
        password = attrs.get('password')

        user = User_info.objects.filter(ERP_Student_Id=ERP_Student_Id).first()

        if not user:
            raise AuthenticationFailed('User not found')

        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect password')

       
        return super().validate(attrs)
