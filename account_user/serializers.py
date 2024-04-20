from rest_framework import serializers
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import User_info, UserData
from django.contrib.auth.hashers import make_password, check_password 
from rest_framework.exceptions import ValidationError


class UserinfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_info
        fields = ['id', 'name', 'username', 'phonenumber', 'password']

        extra_kwargs = {'password': {'read_only': True}}

    def create(self, validated_data):
        validated_data['password'] = 'milestone@123'
        user = User_info.objects.create(
            name=validated_data['name'],
            username=validated_data['username'],
            phonenumber=validated_data['phonenumber'],
            password=make_password(validated_data['password'])
        )
        return user


class LoginSerializer(TokenObtainPairSerializer):
    class Meta:
        model = User_info
        fields = ['username', 'password',]
        extra_kwargs = {
            'password': {'write_only': True},
        }
   

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        user = User_info.objects.filter(username=username).first()

        if not user:
            raise AuthenticationFailed({'username':'User not found'})

        if not user.check_password(password):
            raise AuthenticationFailed({'password':'Incorrect password'})

        return super().validate(attrs)


class GetUserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserData
        fields = ['assessment_result_id',
                  'program', 
                  'program_group',
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


class ChangePasswordSerializer(serializers.ModelSerializer):

    old_password = serializers.CharField(required=True, max_length=25)
    new_password1 = serializers.CharField(required=True, max_length=25)
    new_password2 = serializers.CharField(required=True, max_length=25)
    
    class Meta:
        model = User_info
        fields = ('old_password', 'new_password1', 'new_password2')
        
    
    
    def validate(self, attrs):
        user = self.context['request'].user
        old_password = attrs['old_password']
        new_password1 = attrs['new_password1']
        new_password2 = attrs['new_password2']
        print("moor")
        if not check_password(old_password, user.password):  
            raise ValidationError({'old_password':'Incorrect password'})
        
        if len(new_password1) < 3:
            raise ValidationError({'password':'password is too wick.'})
        
        if new_password1 != new_password2:
            raise ValidationError({'new_password2':'passwords do not match'})
        
        return super().validate(attrs)

    def update(self, instance, validated_data):
        user = self.context['request'].user
        user.set_password(validated_data['new_password1'])
        user.save()
        return super().update(instance, validated_data)


  
  