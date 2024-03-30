from rest_framework import serializers
from .models import Course, CourseType

class CourseTypeserializer(serializers.ModelSerializer):
    class Meta:
        model = CourseType
        fields = (
            'id', 
            'name'     
        )

class CoursesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = (
            'id',
            'name', 
            'description', 
            'image', 
            'days', 
            'hours', 
            'category',
            'active',
        )
    
    category = CourseTypeserializer()