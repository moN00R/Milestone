from rest_framework import serializers
from .models import Library

class GetBookesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Library
        fields = ('id', 'name', 'file', 'publish')
            