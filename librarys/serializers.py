from rest_framework import serializers
from .models import Library
from rest_framework.pagination import PageNumberPagination

class LibrarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Library
        fields = "__all__"

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['mesage'] = "success"
        return representation
