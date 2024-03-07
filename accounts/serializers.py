# from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer
from typing import Any, Dict
from rest_framework import serializers
from rest_framework.exceptions import ValidationError, AuthenticationFailed
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from marks.models import StudentMark
from courses.models import Subscription
from .models import *
from .tokens import create_jwt_pair_for_user
from phonenumber_field.serializerfields import PhoneNumberField


class CreateUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['phone_number', 'first_name',
                  'last_name', 'password']

        extra_kwargs = {
            'password': {'write_only': True, 'required': True, 'style': {"input_type": 'password'}, }
        }

    def validate(self, attrs):
        # phone_number = attrs.get('phone_number')
        password = attrs.get('password')

        # if len(phone_number) < 9 or len(phone_number) > 13:

        #     raise ValidationError({'mesage': 'phone number is not true'})

        if len(password) < 4:
            raise ValidationError('password is too wick')

        return super().validate(attrs)

    def create(self, validated_data):
        user = User.objects.create(
            phone_number=validated_data['phone_number'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
        )
        user.set_password(validated_data['password'])
        user.save()

        return user


class LoginUserSerializer(serializers.ModelSerializer):
    phone_number = PhoneNumberField()

    class Meta:
        model = User
        fields = ['password', 'phone_number']
        extra_kwargs = {
            'password': {'write_only': True, 'required': True, 'style': {"input_type": 'password'}, }
        }

    def validate(self, attrs):
        phone_number = attrs.get('phone_number')
        password = attrs.get('password')

        try:
            user = User.objects.get(phone_number=phone_number)
        except User.DoesNotExist:
            raise AuthenticationFailed('username does not exist.')

        if not user.check_password(password):
            raise AuthenticationFailed('incorrect password')

        tokens = create_jwt_pair_for_user(user=user)

        return tokens
