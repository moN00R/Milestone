from rest_framework import serializers
from .models import User_info


class UserinfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_info
        fields = '__all__'
